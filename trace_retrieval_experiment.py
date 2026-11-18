"""TRACE prototype: retrieval-stage experiment (offline, no LLM calls).
Compares a standard lexical baseline (word-level BM25) with character n-gram
TF-IDF and a rank-fusion hybrid on a parallel EN/RU/KZ synthetic course corpus.
Metrics: Recall@1, Recall@3, MRR. Clean queries and noisy queries (typo simulation).
Run: python trace_retrieval_experiment.py
"""
import re, json, math, random
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from corpus import T

LANGS = ["en", "ru", "kz"]
tok = lambda s: re.findall(r"\w+", s.lower())

class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.docs=[tok(d) for d in docs]; self.k1=k1; self.b=b
        self.N=len(docs); self.avg=sum(map(len,self.docs))/self.N
        df=Counter(w for d in self.docs for w in set(d))
        self.idf={w:math.log(1+(self.N-n+.5)/(n+.5)) for w,n in df.items()}
        self.tf=[Counter(d) for d in self.docs]
    def scores(self, q):
        out=np.zeros(self.N)
        for i,(tf,d) in enumerate(zip(self.tf,self.docs)):
            for w in tok(q):
                if w in tf:
                    f=tf[w]
                    out[i]+=self.idf[w]*f*(self.k1+1)/(f+self.k1*(1-self.b+self.b*len(d)/self.avg))
        return out

class Tfidf:
    def __init__(self, docs, **kw):
        self.v=TfidfVectorizer(sublinear_tf=True, **kw); self.M=self.v.fit_transform(docs)
    def scores(self, q):
        return (self.M @ self.v.transform([q]).T).toarray().ravel()

def rrf(score_lists, k=60):
    n=len(score_lists[0]); out=np.zeros(n)
    for s in score_lists:
        order=np.argsort(-s, kind="stable")
        for rank,i in enumerate(order): out[i]+=1/(k+rank+1)
    return out

def build(lang):
    docs=[t[lang][0] for t in T]
    bm=BM25(docs)
    tw=Tfidf(docs, analyzer="word", token_pattern=r"(?u)\b\w+\b", lowercase=True)
    tc=Tfidf(docs, analyzer="char_wb", ngram_range=(3,5), lowercase=True)
    return {
      "BM25-word (baseline)": bm.scores,
      "TF-IDF word": tw.scores,
      "TF-IDF char 3-5": tc.scores,
      "Hybrid (BM25+char, RRF)": lambda q,bm=bm,tc=tc: rrf([bm.scores(q), tc.scores(q)]),
    }

def noisy(q, rate, rng):
    alpha="abcdefghijklmnopqrstuvwxyz" if q.isascii() else "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    out=[]
    for ch in q:
        if ch.isalpha() and rng.random()<rate:
            op=rng.choice(["del","sub","dup"])
            if op=="sub": out.append(rng.choice(alpha))
            elif op=="dup": out.append(ch+ch)
        else: out.append(ch)
    return "".join(out)

def evaluate(rate=0.0, seeds=(0,)):
    res={}
    for lang in LANGS:
        systems=build(lang)
        for name,fn in systems.items():
            r1=r3=mrr=0; n=0
            for sd in seeds:
                rng=random.Random(sd)
                for gold,t in enumerate(T):
                    for q in t[lang][1]:
                        qq=noisy(q,rate,rng) if rate>0 else q
                        order=list(np.argsort(-fn(qq), kind="stable"))
                        rank=order.index(gold)+1
                        r1+=rank==1; r3+=rank<=3; mrr+=1/rank; n+=1
            res[(lang,name)]=(r1/n,r3/n,mrr/n,n)
    return res

if __name__=="__main__":
    out={}
    for label,rate,seeds in [("clean",0.0,(0,)),("noisy10",0.10,tuple(range(20)))]:
        r=evaluate(rate,seeds); out[label]={f"{l}|{s}":v for (l,s),v in r.items()}
        print("==",label)
        for (l,s),(a,b,c,n) in r.items(): print(f"{l} {s:28s} R@1={a:.3f} R@3={b:.3f} MRR={c:.3f} n={n}")
    json.dump(out,open("results.json","w"),ensure_ascii=False,indent=1)
