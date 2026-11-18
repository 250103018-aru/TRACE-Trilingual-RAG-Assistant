
from corpus import T
from trace_retrieval_experiment import build

LANGUAGES = {
    "en": "English",
    "ru": "Russian",
    "kz": "Kazakh"
}

print("=" * 55)
print("TRACE — Trilingual Course Retrieval Assistant")
print("=" * 55)

while True:
    print("\nLanguages: en / ru / kz")
    lang = input("Choose language (or 'exit'): ").strip().lower()

    if lang == "exit":
        print("Goodbye!")
        break

    if lang not in LANGUAGES:
        print("Invalid language. Try again.")
        continue

    question = input("\nEnter your question: ").strip()

    if not question:
        print("Please enter a question.")
        continue

    search = build(lang)["TF-IDF char 3-5"]
    scores = search(question)

    best_index = scores.argmax()
    best_score = scores[best_index]

    print("\n" + "-" * 55)

    if best_score < 0.05:
        print("No sufficiently relevant passage found.")
    else:
        print("Language:", LANGUAGES[lang])
        print("Retrieved course passage:")
        print(T[best_index][lang][0])
        print("Source: Course topic", best_index + 1)
        print("Similarity score:", round(float(best_score), 3))

    print("-" * 55)
