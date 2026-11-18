# Synthetic course corpus (16 topics x 3 languages) + 2 questions per topic per language.
# Written for the TRACE prototype; EN/RU/KZ are parallel (same content).
T = [
# 1 research question
dict(
 en=("A good research question is specific, measurable and answerable with empirical evidence; vague questions lead to unfocused studies.",
     ["What makes a research question good?","Why do vague questions produce unfocused studies?"]),
 ru=("Хороший исследовательский вопрос конкретен, измерим и допускает ответ на основе эмпирических данных; расплывчатые вопросы приводят к несфокусированным исследованиям.",
     ["Каким должен быть хороший исследовательский вопрос?","К чему приводят расплывчатые формулировки вопроса исследования?"]),
 kz=("Жақсы зерттеу сұрағы нақты, өлшенетін және эмпирикалық деректер негізінде жауап беруге болатындай болуы тиіс; түсініксіз сұрақтар бағыты анық емес зерттеулерге әкеледі.",
     ["Жақсы зерттеу сұрағы қандай болуы керек?","Түсініксіз сұрақтар зерттеуге қалай әсер етеді?"])),
# 2 hypothesis
dict(
 en=("A hypothesis is a testable statement about the relationship between variables; the null hypothesis states that there is no effect or no difference.",
     ["What is a null hypothesis?","How is a hypothesis defined in research?"]),
 ru=("Гипотеза — это проверяемое утверждение о связи между переменными; нулевая гипотеза утверждает, что эффекта или различия нет.",
     ["Что утверждает нулевая гипотеза?","Как определяется гипотеза в исследовании?"]),
 kz=("Гипотеза — айнымалылар арасындағы байланыс туралы тексеруге болатын тұжырым; нөлдік гипотеза әсердің немесе айырмашылықтың жоқ екенін айтады.",
     ["Нөлдік гипотеза нені білдіреді?","Зерттеуде гипотеза қалай анықталады?"])),
# 3 systematic review
dict(
 en=("A systematic review follows a predefined search strategy and explicit inclusion criteria in order to reduce selection bias.",
     ["How does a systematic review reduce bias?","What is defined in advance in a systematic literature search?"]),
 ru=("Систематический обзор опирается на заранее определённую стратегию поиска и явные критерии включения, чтобы снизить смещение отбора.",
     ["Как систематический обзор снижает смещение?","Что определяется заранее при систематическом поиске литературы?"]),
 kz=("Жүйелі шолу іріктеу қателігін азайту үшін алдын ала анықталған іздеу стратегиясы мен енгізу өлшемшарттарына сүйенеді.",
     ["Жүйелі шолу іріктеу қателігін қалай азайтады?","Әдебиетті жүйелі іздеуде алдын ала не анықталады?"])),
# 4 sampling
dict(
 en=("In simple random sampling every member of the population has an equal chance of being selected, which supports generalisation of results.",
     ["What is random sampling?","Which sampling method gives all members the same selection probability?"]),
 ru=("При простой случайной выборке каждый элемент генеральной совокупности имеет равные шансы попасть в выборку, что поддерживает обобщение результатов.",
     ["Что такое случайная выборка?","Какой метод отбора даёт всем участникам одинаковую вероятность?"]),
 kz=("Қарапайым кездейсоқ іріктеуде жалпы жиынтықтың әрбір мүшесінің таңдалу мүмкіндігі тең болады, бұл нәтижелерді жалпылауға мүмкіндік береді.",
     ["Кездейсоқ іріктеме дегеніміз не?","Қай әдіс барлық қатысушыларға бірдей таңдалу ықтималдығын береді?"])),
# 5 internal validity
dict(
 en=("Internal validity asks whether the observed effect was caused by the intervention itself rather than by confounding variables.",
     ["What does internal validity measure?","How do confounders threaten the conclusion that an intervention caused an effect?"]),
 ru=("Внутренняя валидность показывает, вызван ли наблюдаемый эффект самим воздействием, а не искажающими переменными.",
     ["Что оценивает внутренняя валидность?","Как искажающие факторы ставят под сомнение причинность эффекта?"]),
 kz=("Ішкі валидтілік байқалған әсердің шатастырушы айнымалылардан емес, дәл араласудың өзінен туындағанын көрсетеді.",
     ["Ішкі валидтілік нені бағалайды?","Шатастырушы факторлар себеп-салдарлық қорытындыға қалай қауіп төндіреді?"])),
# 6 reliability
dict(
 en=("Reliability means consistency of measurement; Cronbach's alpha estimates the internal consistency of a questionnaire scale.",
     ["What does Cronbach's alpha estimate?","What is measurement reliability?"]),
 ru=("Надёжность означает согласованность измерений; альфа Кронбаха оценивает внутреннюю согласованность шкалы опросника.",
     ["Что оценивает альфа Кронбаха?","Что такое надёжность измерения?"]),
 kz=("Сенімділік өлшемнің тұрақтылығын білдіреді; Кронбах альфасы сауалнама шкаласының ішкі келісімділігін бағалайды.",
     ["Кронбах альфасы нені бағалайды?","Өлшеу сенімділігі дегеніміз не?"])),
# 7 p-value
dict(
 en=("A p-value is the probability of obtaining data at least as extreme as observed, assuming the null hypothesis is true; it is not the probability that the hypothesis is true.",
     ["How should a p-value be interpreted?","Is the p-value the probability that the null hypothesis is true?"]),
 ru=("p-значение — вероятность получить данные не менее экстремальные, чем наблюдаемые, если нулевая гипотеза верна; это не вероятность истинности гипотезы.",
     ["Как интерпретировать p-значение?","Является ли p-значение вероятностью того, что нулевая гипотеза верна?"]),
 kz=("p-мәні — нөлдік гипотеза дұрыс болғанда байқалғаннан кем емес шеткері деректерді алу ықтималдығы; бұл гипотезаның ақиқат болу ықтималдығы емес.",
     ["p-мәнін қалай түсіндіру керек?","p-мәні нөлдік гипотезаның дұрыс болу ықтималдығы ма?"])),
# 8 consent
dict(
 en=("Informed consent requires that participants are told the purpose of the study, its risks, and their right to withdraw at any time.",
     ["What must participants be told before giving informed consent?","Can a participant withdraw from a study?"]),
 ru=("Информированное согласие требует, чтобы участникам сообщили о цели исследования, рисках и праве выйти из него в любой момент.",
     ["О чём нужно сообщить участникам перед получением информированного согласия?","Может ли участник выйти из исследования?"]),
 kz=("Ақпараттандырылған келісім қатысушыларға зерттеудің мақсаты, тәуекелдері және кез келген уақытта шығу құқығы туралы хабарлауды талап етеді.",
     ["Келісім бермес бұрын қатысушыларға не туралы айту керек?","Қатысушы зерттеуден шыға ала ма?"])),
# 9 citation
dict(
 en=("Citing sources acknowledges the ideas of other authors and prevents plagiarism; the APA style uses author-date in-text citations.",
     ["How does APA format in-text citations?","Why is citation necessary to avoid plagiarism?"]),
 ru=("Цитирование источников признаёт идеи других авторов и предотвращает плагиат; стиль APA использует ссылки в тексте по схеме «автор — год».",
     ["Как APA оформляет ссылки в тексте?","Зачем нужно цитирование, чтобы избежать плагиата?"]),
 kz=("Дереккөздерді дәйексөздеу басқа авторлардың идеяларын мойындайды және плагиаттың алдын алады; APA стилі мәтін ішінде «автор — жыл» үлгісіндегі сілтемелерді қолданады.",
     ["APA мәтін ішіндегі сілтемелерді қалай рәсімдейді?","Плагиаттан аулақ болу үшін дәйексөздеу не үшін қажет?"])),
# 10 thematic analysis
dict(
 en=("Thematic analysis identifies and interprets recurring patterns of meaning, called themes, in qualitative data such as interview transcripts.",
     ["What is thematic analysis used for?","How are interview transcripts analysed qualitatively?"]),
 ru=("Тематический анализ выявляет и интерпретирует повторяющиеся смысловые закономерности, называемые темами, в качественных данных, например в расшифровках интервью.",
     ["Для чего применяют тематический анализ?","Как качественно анализируют транскрипты интервью?"]),
 kz=("Тақырыптық талдау сұхбат транскрипттері сияқты сапалық деректердегі қайталанатын мағыналық үлгілерді, яғни тақырыптарды анықтап, түсіндіреді.",
     ["Тақырыптық талдау не үшін қолданылады?","Сұхбат транскрипттері сапалық тұрғыда қалай талданады?"])),
# 11 Frascati
dict(
 en=("The Frascati Manual defines research and development by five criteria: the work must be novel, creative, uncertain, systematic and transferable or reproducible.",
     ["Which criteria does the Frascati Manual use to define R&D?","Must R&D work be uncertain and reproducible?"]),
 ru=("Руководство Фраскати определяет НИОКР пятью критериями: работа должна быть новой, творческой, неопределённой по результату, систематической и передаваемой или воспроизводимой.",
     ["Какие критерии использует Руководство Фраскати для определения НИОКР?","Должна ли работа в рамках НИОКР быть неопределённой и воспроизводимой?"]),
 kz=("Фраскати нұсқаулығы ҒЗТКЖ-ны бес өлшемшартпен анықтайды: жұмыс жаңа, шығармашылық, нәтижесі белгісіз, жүйелі және берілетін немесе қайталанатын болуы тиіс.",
     ["Фраскати нұсқаулығы ҒЗТКЖ-ны анықтау үшін қандай өлшемшарттарды қолданады?","ҒЗТКЖ жұмысы белгісіздік пен қайталанғыштықты қамтуы керек пе?"])),
# 12 TRL
dict(
 en=("The technology readiness level scale runs from 1 to 9; TRL 3 is experimental proof of concept and TRL 4 is technology validated in a laboratory.",
     ["What does TRL 4 mean?","How many levels does the technology readiness scale have?"]),
 ru=("Шкала уровней технологической готовности идёт от 1 до 9; TRL 3 — экспериментальное подтверждение концепции, TRL 4 — технология, проверенная в лаборатории.",
     ["Что означает TRL 4?","Сколько уровней в шкале технологической готовности?"]),
 kz=("Технологиялық дайындық деңгейлері шкаласы 1-ден 9-ға дейін жүреді; TRL 3 — тәжірибелік тұжырымдаманы растау, TRL 4 — зертханада тексерілген технология.",
     ["TRL 4 нені білдіреді?","Технологиялық дайындық шкаласында неше деңгей бар?"])),
# 13 Gantt
dict(
 en=("A Gantt chart displays work packages along a timeline and marks milestones and deliverables, which helps to plan a project schedule.",
     ["What does a Gantt chart show?","How can a project schedule be planned with milestones?"]),
 ru=("Диаграмма Ганта отображает пакеты работ на временной шкале и отмечает вехи и результаты, что помогает планировать график проекта.",
     ["Что показывает диаграмма Ганта?","Как спланировать график проекта с помощью вех?"]),
 kz=("Гант диаграммасы жұмыс пакеттерін уақыт шкаласында көрсетеді және кезеңдер мен нәтижелерді белгілейді, бұл жоба кестесін жоспарлауға көмектеседі.",
     ["Гант диаграммасы нені көрсетеді?","Жоба кестесін кезеңдер арқылы қалай жоспарлауға болады?"])),
# 14 FAIR
dict(
 en=("The FAIR principles require research data to be findable, accessible, interoperable and reusable.",
     ["What do the FAIR data principles stand for?","How should research data be managed to be reusable?"]),
 ru=("Принципы FAIR требуют, чтобы данные исследований были находимыми, доступными, совместимыми и пригодными для повторного использования.",
     ["Что означают принципы FAIR для данных?","Как управлять данными исследования, чтобы их можно было использовать повторно?"]),
 kz=("FAIR қағидаттары зерттеу деректерінің табылатын, қолжетімді, өзара үйлесімді және қайта пайдалануға жарамды болуын талап етеді.",
     ["Деректерге арналған FAIR қағидаттары нені білдіреді?","Зерттеу деректерін қайта пайдалану үшін қалай басқару керек?"])),
# 15 CI
dict(
 en=("A 95% confidence interval is a range of values that would contain the true parameter in 95% of repeated samples from the same population.",
     ["How is a confidence interval interpreted?","What does 95% mean in a 95% confidence interval?"]),
 ru=("95-процентный доверительный интервал — диапазон значений, который содержал бы истинный параметр в 95% повторных выборок из той же совокупности.",
     ["Как интерпретируется доверительный интервал?","Что означает 95% в 95-процентном доверительном интервале?"]),
 kz=("95% сенім интервалы — сол жалпы жиынтықтан алынған қайталанған іріктемелердің 95%-ында шын параметрді қамтитын мәндер аралығы.",
     ["Сенім интервалы қалай түсіндіріледі?","95% сенім интервалындағы 95% нені білдіреді?"])),
# 16 baseline
dict(
 en=("A control group or baseline provides a point of comparison, so that the effect of a new method can be estimated against the standard approach.",
     ["Why does an experiment need a baseline?","How is the effect of a new method estimated?"]),
 ru=("Контрольная группа или базовый уровень служит точкой сравнения, чтобы оценить эффект нового метода относительно стандартного подхода.",
     ["Зачем эксперименту нужен baseline?","Как оценивается эффект нового метода?"]),
 kz=("Бақылау тобы немесе базалық деңгей салыстыру нүктесі қызметін атқарады, сонда жаңа әдістің әсерін стандартты тәсілмен салыстырып бағалауға болады.",
     ["Эксперимент үшін baseline не үшін қажет?","Жаңа әдістің әсері қалай бағаланады?"])),
]
