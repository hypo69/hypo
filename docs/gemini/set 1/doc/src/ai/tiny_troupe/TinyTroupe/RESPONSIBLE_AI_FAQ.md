# TinyTroupe: Responsible AI FAQ

## Обзор

Данный документ содержит часто задаваемые вопросы (FAQ) о библиотеке TinyTroupe, предназначенной для моделирования людей с определенными личностями, интересами и целями.  Документ акцентирует внимание на этических аспектах использования библиотеки и ответственной разработке с использованием TinyTroupe.

## Оглавление

* [Что такое TinyTroupe?](#что-такое-tinytroupe)
* [Что может делать TinyTroupe?](#что-может-делать-tinytroupe)
* [Каково(ы) предполагаемое(ые) использование(ия) TinyTroupe?](#каково-ы-предполагаемое-ые-использование-ия-tinytroupe)
* [Как оценивалась TinyTroupe? Какие метрики используются для измерения производительности?](#как-оценивалась-tinytroupe-какие-метрики-используются-для-измерения-производительности)
* [Какие ограничения у TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?](#какие-ограничения-у-tinytroupe-как-пользователи-могут-минимизировать-влияние-ограничений-tinytroupe-при-использовании-системы)
* [Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?](#какие-операционные-факторы-и-настройки-позволяют-эффективно-и-ответственно-использовать-tinytroupe)


## Что такое TinyTroupe?

*TinyTroupe* — это экспериментальная Python-библиотека, позволяющая **моделировать** людей со специфическими личностями, интересами и целями. Эти искусственные агенты — `TinyPerson` — могут слушать нас и друг друга, отвечать и жить в симулированных средах `TinyWorld`.  Это достигается за счет использования возможностей языковых моделей (LLM), в частности GPT-4, для генерации реалистичного моделируемого поведения. Библиотека фокусируется на понимании человеческого поведения, а не на его непосредственной поддержке. Это приводит к специализированным механизмам и конструктивным решениям, имеющим смысл только в контексте моделирования.

TinyTroupe работает программно: симуляции описываются как Python-программы, использующие элементы TinyTroupe, а затем выполняются. Входные данные для моделирования включают описание персонажей (например, возраст, национальность, местоположение, интересы, работа и т. д.) и диалоги (например, программист может «разговаривать» с агентами). Выходные данные включают мысли и слова агентов, а также структурированные извлечения из них (например, сводка диалогов).


## Что может делать TinyTroupe?

TinyTroupe сама по себе не является моделью искусственного интеллекта (ИИ) или машинного обучения (МО). Вместо этого она полагается на внешние API для обеспечения своих интеллектуальных возможностей. TinyTroupe предоставляет инструменты для:

* моделирования персонажей агентов, включая их мысли и слова;
* моделирования сред, в которых агенты взаимодействуют;
* извлечения структурированных выходных данных из симуляций для последующего использования (например, JSON с различными извлеченными элементами);
* обогащения артефактов симуляции для повышения реалистичности;
* помощи в повествовании для создания более интересной симуляции.


## Каково(ы) предполагаемое(ые) использование(ия) TinyTroupe?

TinyTroupe предназначена для:

* анализа поведения искусственных людей посредством моделирования;
* генерации синтетических артефактов посредством моделирования;
* дополнения, а не замены, человеческого анализа;
* исследования различных возможностей вычислительных когнитивных архитектур, которые могут или не могут отражать реальное человеческое познание.

TinyTroupe НЕ предназначена для:

* прямого взаимодействия с пользователями. Вместо этого программисты, использующие TinyTroupe для создания продуктов, должны создавать свой собственный уровень ответственного ИИ для обеспечения соответствия результатов моделирования требованиям.
* принятия политических решений или иных решений с последствиями. Любое решение, принятое с использованием симуляций TinyTroupe, должно учитывать, что результаты симуляции могут не отражать реальность, и поэтому их следует использовать очень осторожно для любых действий с реальными последствиями.


## Как оценивалась TinyTroupe? Какие метрики используются для измерения производительности?

TinyTroupe оценивалась с использованием различных кейсов использования, некоторые из которых приведены в библиотеке в качестве примеров. Ее применимость в этих сценариях ограничена демонстрационными показателями.  Дальнейшее применение остается областью исследований и экспериментальной работы. К тестированию также относятся обширные модульные и сценарийные тесты.


## Какие ограничения у TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?

TinyTroupe НЕ показала соответствие реальному поведению человека, поэтому любая такая возможность остается всего лишь исследованием или экспериментальным изучением. Хотя в наших различных тестах этого не наблюдалось, TinyTroupe теоретически может генерировать выходные данные, которые могут считаться вредоносными. Это связано с тем, что одним из важных теоретических случаев использования TinyTroupe является проверка других систем ИИ на наличие таких вредоносных выходных данных, поэтому ничего не препятствует моделированию злоумышленников. ПОЭТОМУ программисты, использующие TinyTroupe для создания собственных продуктов или сервисов, ДОЛЖНЫ обеспечить свои собственные меры предосторожности ответственного ИИ, так как сама TinyTroupe не предназначена для ограничения выходных данных подобным образом. Это также относится к другим фундаментальным библиотекам LLM, таким как LangChain или Semantic Kernel, которые, как и TinyTroupe, являются всего лишь ИНСТРУМЕНТАМИ, которые следует использовать с осторожностью.


## Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?

TinyTroupe может быть использована ответственно:

* используя внешние API моделей, которые сами обеспечивают механизмы безопасности (например, Azure OpenAI предоставляет обширные ресурсы для этой цели);
* предоставляя соответствующие описания персонажей (т. е. безвредные персонажи);
* не подталкивайте истории симуляции или поведение агентов к генерации вредоносного контента. Если это делается, следует понимать, что единственно допустимое применение для этого заключается в проверке других систем ИИ на наличие таких нежелательных выходных данных.
* НЕ допускайте, чтобы симуляции контролировали реальные механизмы, если не предприняты соответствующие меры по контролю ущерба для предотвращения реального вреда.
* если вы используете TinyTroupe для создания собственного продукта или сервиса, вы ДОЛЖНЫ обеспечить свои собственные меры предосторожности ответственного ИИ, такие как проверка выходных данных.