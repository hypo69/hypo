# TinyTroupe: FAQ по ответственному ИИ

## Что такое TinyTroupe?

*TinyTroupe* — это экспериментальная Python-библиотека, позволяющая **моделировать** людей со специфическими личностями, интересами и целями. Эти искусственные агенты — `TinyPerson` — могут слушать нас и друг друга, отвечать и жить в симулированных средах `TinyWorld`. Это достигается за счет использования мощностей языковых моделей (LLM), в частности GPT-4, для генерации реалистичного имитируемого поведения. Это позволяет нам исследовать широкий спектр **реалистичных взаимодействий** и **типов потребителей** с **высоко настраиваемыми персонами** в **выбранных нами условиях**. Основной фокус на *понимании* поведения человека, а не на его непосредственном *поддержании* (как, например, делают помощники на базе ИИ) — это приводит, среди прочего, к специализированным механизмам и решениям, которые имеют смысл только в контексте симуляции. Это имеет значение для аспектов ответственного ИИ, как описано в остальной части этого FAQ.

Подход TinyTroupe программный: симуляции задаются как программы на Python с использованием элементов TinyTroupe и затем выполняются. Входными данными для симуляции являются описание персон (например, возраст, национальность, местоположение, интересы, работа и т. д.) и разговоры (например, программист может «разговаривать» с агентами). Выходными данными являются мысли и слова агентов, а также структурированные выдержки из них (например, сводка разговоров).

## Что может делать TinyTroupe?

Сам TinyTroupe — это не модель искусственного интеллекта (ИИ) или машинного обучения (ML). Вместо этого он полагается на внешние API для обеспечения своих интеллектуальных возможностей. TinyTroupe предоставляет элементы, в основном для:

- моделирования персон агентов, включая их мысли и слова;
- моделирования сред, в которых агенты взаимодействуют;
- извлечения структурированных результатов из симуляций для последующего использования (например, JSON с различными извлеченными элементами);
- обогащения артефактов симуляции для повышения реалистичности;
- оказания помощи в повествовании для повышения интереса к симуляции.

## Каково(ы) предполагаемое(ые) использование(ия) TinyTroupe?

TinyTroupe предназначен для:

- анализа поведения искусственных людей посредством моделирования;
- генерации синтетических артефактов посредством моделирования;
- дополнения, а не замены, генерации человеческого понимания;
- исследования различных возможностей вычислительных когнитивных архитектур, которые могут или не могут отражать реальное когнитивное мышление человека.

TinyTroupe НЕ предназначен для:

- непосредственного взаимодействия с пользователями. Скорее, программисты, использующие TinyTroupe для создания продуктов, должны создавать собственный уровень ответственного ИИ для обеспечения того, что результаты симуляции являются приемлемыми.
- принятия политических решений или любых последующих решений. Любое решение, принимаемое с использованием симуляций TinyTroupe, должно учитывать, что результаты симуляции могут не отражать реальность, и поэтому их следует использовать очень осторожно для всего, что имеет реальные последствия.

## Как оценивался TinyTroupe? Какие метрики используются для измерения производительности?

TinyTroupe оценивался с помощью различных кейсов, некоторые из которых приведены в качестве примеров в библиотеке. Он подходит для использования в этих сценариях в той мере, в какой демонстрации это показывают. Все, что выходит за эти рамки, остается исследовательской и экспериментальной работой. Расширенное тестирование отдельных модулей и сценариев также является частью библиотеки.


## Каковы ограничения TinyTroupe? Как пользователи могут свести к минимуму влияние ограничений TinyTroupe при использовании системы?

TinyTroupe НЕ показал соответствие реальному поведению человека, поэтому любая такая возможность остается лишь исследовательским или экспериментальным исследованием. Хотя в наших различных тестах этого не наблюдалось, TinyTroupe теоретически может генерировать результаты, которые могут считаться злонамеренными. Причина в том, что одним из важных теоретических случаев использования TinyTroupe является проверка **других** систем ИИ на наличие таких злонамеренных результатов, поэтому ничего не мешает ему моделировать плохих актёров. ПОЭТОМУ программисты, использующие TinyTroupe для создания собственных продуктов или услуг, ДОЛЖНЫ предоставить собственные механизмы обеспечения ответственного ИИ, поскольку TinyTroupe сам по себе не предназначен для ограничения вывода таким образом. Это ТОТ ЖЕ СЛУЧАЙ для любой другой основополагающей библиотеки LLM, такой как LangChain или Semantic Kernel, которые, как и TinyTroupe, являются всего лишь ИНСТРУМЕНТАМИ, которые следует использовать с осторожностью.

## Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?

TinyTroupe можно использовать ответственно, если:

- использовать внешние API моделей, которые сами предоставляют механизмы безопасности (например, Azure OpenAI предоставляет обширные ресурсы для этого);
- предоставить соответствующие описания персон (т. е. безвредные персоны);
- не использовать симулированные истории или поведение агентов для генерации злонамертельного контента. Если это делается, полностью осознайте, что единственным разрешенным использованием этого является проверка других систем ИИ на наличие таких нежелательных результатов.
- НЕ разрешать симуляциям контролировать реальные механизмы, если не приняты надлежащие механизмы регулирования ущерба для предотвращения реального вреда.
- если вы используете TinyTroupe для создания своего собственного продукта или услуги, ВЫ ДОЛЖНЫ предоставить собственные механизмы обеспечения ответственного ИИ, такие как проверка вывода.