# TinyTroupe: Responsible AI FAQ

## Обзор

Данный документ содержит часто задаваемые вопросы (FAQ) о библиотеке TinyTroupe, предназначенной для моделирования людей с конкретными личностями, интересами и целями с использованием языковых моделей (LLM), в частности GPT-4.  Он фокусируется на ответственном использовании библиотеки,  описывая ее возможности, ограничения и рекомендации по применению.


## Содержание

- [Что такое TinyTroupe?](#что-такое-tinytroupe)
- [Что может сделать TinyTroupe?](#что-может-сделать-tinytroupe)
- [В каких целях предназначена TinyTroupe?](#в-каких-целях-предназначена-tinytroupe)
- [Как оценивалась TinyTroupe? Какие метрики используются для измерения производительности?](#как-оценивалась-tinytroupe-какие-метрики-используются-для-измерения-производительности)
- [Какие ограничения у TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?](#какие-ограничения-у-tinytroupe-как-пользователи-могут-минимизировать-влияние-ограничений-tinytroupe-при-использовании-системы)
- [Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?](#какие-операционные-факторы-и-настройки-позволяют-эффективно-и-ответственно-использовать-tinytroupe)


## Что такое TinyTroupe?

*TinyTroupe* — это экспериментальная Python-библиотека, позволяющая моделировать людей с определёнными личностями, интересами и целями.  Эти искусственные агенты — `TinyPerson` — могут слушать нас и друг друга, отвечать и жить в симулированных средах `TinyWorld`. Это достигается путём использования языковых моделей (LLM), в частности GPT-4, для генерации реалистичного моделируемого поведения.  Цель — исследование широкого спектра реалистичных взаимодействий и типов потребителей с высоконастраиваемыми персонами в заданных условиях.  Подчёркивается понимание человеческого поведения, а не его прямое использование (например, как в случае с помощниками на основе ИИ).  Это приводит к специфическим механизмам и архитектурным решениям, имеющим смысл только в контексте симуляции.

TinyTroupe работает программно: симуляции задаются как Python-программы с использованием элементов TinyTroupe, а затем выполняются. Входные данные для симуляции включают описание персон (возраст, национальность, местоположение, интересы, работа и т.д.) и диалогов (программист может «разговаривать» с агентами). Выходные данные включают мысли и слова агентов, а также структурированные извлечения из них (например, резюме диалогов).


## Что может сделать TinyTroupe?

TinyTroupe сама по себе не является моделью искусственного интеллекта (ИИ) или машинного обучения (МО).  Она полагается на внешние API для своих интеллектуальных возможностей.  TinyTroupe предоставляет элементы для:

- моделирования персон агентов, включая их мысли и слова;
- моделирования сред, в которых взаимодействуют агенты;
- извлечения структурированных выходных данных из симуляций для дальнейшего использования (например, JSON с различными извлечёнными элементами);
- обогащения артефактов симуляции для повышения реалистичности;
- предоставления помощи в повествовании для создания более интересных симуляций.


## В каких целях предназначена TinyTroupe?

TinyTroupe предназначена для:

- анализа искусственного поведения человека через симуляцию;
- генерации синтетических артефактов посредством симуляции;
- дополнения, а не замены, человеческого понимания;
- исследования различных возможностей вычислительных когнитивных архитектур, которые могут или не могут отражать истинную человеческую когницию.

TinyTroupe НЕ предназначена для:

- прямого взаимодействия с пользователями.  Программисты, использующие TinyTroupe для создания продуктов, должны создавать собственный уровень ответственного ИИ, чтобы обеспечить соответствие результатов симуляции.
- принятия решений в политике или любых других решениях с последствиями. Любое решение, основанное на результатах симуляций TinyTroupe, должно учитывать, что результаты симуляции могут не отражать реальность, и поэтому должны использоваться очень осторожно в контексте реального мира.


## Как оценивалась TinyTroupe? Какие метрики используются для измерения производительности?

TinyTroupe оценивалась через различные примеры использования, некоторые из которых предоставлены в библиотеке в виде примеров. Применимость подходит под те сценарии, в которых демонстрации показали её соответствие.  Любые выводы за пределами этих сценариев остаются областью исследований и экспериментальной работы.  К тестированию также относятся обширные юнит- и сценарийные тесты.


## Какие ограничения у TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?

Не доказано, что TinyTroupe точно воспроизводит реальное поведение человека. Таким образом, любая такая возможность остаётся в области исследований или экспериментального изучения. Несмотря на то, что в наших тестах это не наблюдалось, теоретически TinyTroupe может генерировать выходные данные, которые могут считаться злонамеренными.  Это обусловлено тем, что важный теоретический пример использования TinyTroupe — проверка других систем ИИ на устойчивость к подобным злонамеренным выходам, поэтому ничего не ограничивает её от моделирования плохих актёров.  Поэтому программисты, использующие TinyTroupe для создания собственных продуктов или сервисов, ОДНИ должны предоставить собственные механизмы ответственного ИИ, так как сама TinyTroupe не предназначена для ограничения выходных данных таким образом. Это же относится к другим библиотекам, основанным на LLM, таким как LangChain или Semantic Kernel.  Эти инструменты должны использоваться с осторожностью.


## Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?

TinyTroupe может использоваться ответственно, следуя рекомендациям:

- использование внешних API моделей, которые сами предоставляют механизмы безопасности (например, Azure OpenAI предоставляет обширные ресурсы для этой цели);
- предоставление подходящих описаний персон (т.е. не злонамеренных);
- не провоцировать симуляции историй или поведения агентов для генерации злонамеренного контента. Если это делается, будьте в курсе, что единственное разрешенное использование — проверка других систем ИИ на устойчивость к нежелательным результатам;
- НЕ допускать, чтобы симуляции контролировали реальные механизмы, если не предусмотрены соответствующие механизмы контроля ущерба для предотвращения реального вреда;
- если вы используете TinyTroupe в качестве основы для своего продукта или сервиса, ВЫ должны обеспечить собственные механизмы ответственного ИИ, такие как проверка выходных данных.