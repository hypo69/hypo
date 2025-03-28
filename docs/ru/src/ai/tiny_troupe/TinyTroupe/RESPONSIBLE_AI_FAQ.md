# TinyTroupe: Responsible AI FAQ

## Обзор

*TinyTroupe* - это экспериментальная библиотека Python, которая позволяет **моделировать** людей с определенными личностями, интересами и целями. Эти искусственные агенты - `TinyPerson` - могут слушать нас и друг друга, отвечать и заниматься своей жизнью в смоделированных средах `TinyWorld`. Это достигается за счет использования возможностей языковых моделей (LLM), особенно GPT-4, для генерации реалистичного смоделированного поведения. Это позволяет нам исследовать широкий спектр **реалистичных взаимодействий** и **типов потребителей** с **настраиваемыми персонами** в **выбранных нами условиях**. Таким образом, основное внимание уделяется *пониманию* человеческого поведения, а не *непосредственной его поддержке* (как это делают, например, AI-помощники) - это приводит, среди прочего, к специализированным механизмам и выбору дизайна, которые имеют смысл только в условиях моделирования. Это оказывает влияние на аспекты Resonsible AI, как описано в остальной части этого FAQ.

Подход TinyTroupe является программным: моделирования определяются как программы Python с использованием элементов TinyTroupe, а затем выполняются. Входные данные для моделирования включают описание персонажей (например, возраст, национальность, местоположение, интересы, работа и т. д.) и разговоров (например, программист может "разговаривать" с агентами). Выходные данные включают мысли и слова агентов, а также структурированные извлечения из них (например, краткое изложение разговоров).

## Что может делать TinyTroupe?

TinyTroupe сама по себе _не_ является моделью искусственного интеллекта (AI) или машинного обучения (ML). Вместо этого она полагается на внешние API для обеспечения своих интеллектуальных возможностей. При этом TinyTroupe предоставляет элементы в основном для:

  - моделирования персонажей агентов, включая их мысли и слова;
  - моделирования сред, в которых взаимодействуют агенты;
  - извлечения структурированного вывода из моделирования для последующего использования (например, JSON с различными извлеченными элементами);
  - обогащения артефактов моделирования, чтобы сделать их более реалистичными;
  - оказания помощи в рассказывании историй, чтобы сделать моделирование более интересным.

## Каковы предполагаемые способы использования TinyTroupe?

TinyTroupe предназначена для:
  - анализа искусственного поведения человека посредством моделирования;
  - генерации синтетических артефактов посредством моделирования;
  - дополнения, а не замены, генерации человеческих идей;
  - исследования различных возможностей вычислительных когнитивных архитектур, которые могут отражать или не отражать фактическое человеческое познание.

TinyTroupe НЕ предназначена для:
  - прямого взаимодействия с пользователями. Скорее, программисты, полагающиеся на TinyTroupe для продуктов, должны создать свой собственный уровень ответственного AI, чтобы гарантировать, что результаты моделирования будут подходящими.
  - принятия политических или каких-либо важных решений. Скорее, любое решение, принятое с использованием моделирования TinyTroupe, должно учитывать, что результаты моделирования могут не отражать реальность, и поэтому их следует использовать очень осторожно для всего, что имеет реальное влияние на мир.

## Как оценивалась TinyTroupe? Какие метрики используются для измерения производительности?

TinyTroupe оценивалась с помощью различных сценариев использования, часть из которых представлена в качестве примеров в библиотеке. Она подходит для использования в этих сценариях в той степени, в какой это показывают демонстрации. Все, что выходит за рамки этого, остается исследовательской и экспериментальной работой. Обширное модульное и сценарное тестирование также является частью библиотеки.

## Каковы ограничения TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?

Не было показано, что TinyTroupe соответствует реальному человеческому поведению, и поэтому любая такая возможность остается лишь исследованием или экспериментальным исследованием.
Хотя это не наблюдалось в наших различных тестах, TinyTroupe теоретически может генерировать вывод, который может быть расценен как злонамеренный. Причина этого в том, что
одним важным теоретическим вариантом использования TinyTroupe является проверка **других** систем AI на наличие таких злонамеренных выводов, поэтому ничто не ограничивает ее в моделировании
плохих актеров. ПОЭТОМУ программисты, использующие TinyTroupe для создания собственных продуктов или услуг на ее основе, ДОЛЖНЫ предусмотреть свои собственные меры защиты Responsible AI,
поскольку TinyTroupe сама по себе не предназначена для ограничения вывода таким образом. ТО ЖЕ САМОЕ относится и к любой другой фундаментальной библиотеке LLM, такой как LangChain или Semantic Kernel,
которые, как и TinyTroupe, являются всего лишь ИНСТРУМЕНТАМИ, которые следует использовать с осторожностью.

## Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?

TinyTroupe можно использовать ответственно, если:
  - использовать внешние API моделей, которые сами предоставляют механизмы безопасности (например, Azure OpenAI предоставляет обширные ресурсы для этой цели).
  - предоставлять подходящие описания персонажей (т. е. незлонамеренных персонажей);
  - не вызывать истории моделирования или поведение агентов для генерации злонамеренного контента. Если это сделано, полностью осознавайте, что ЕДИНСТВЕННОЕ разрешенное использование для этого - это проверка других систем искусственного интеллекта на наличие таких нежелательных выводов.
  - НЕ допускать, чтобы моделирования контролировали реальные механизмы, если не предусмотрены соответствующие механизмы контроля повреждений, чтобы предотвратить возникновение реального вреда.
  - если вы используете TinyTroupe для обеспечения работы своего собственного продукта или сервиса, ВЫ ДОЛЖНЫ предусмотреть свои собственные меры защиты Responsible AI, такие как проверка вывода.