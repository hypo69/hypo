# Документация для TinyTroupe: Responsible AI FAQ

## Обзор

Этот документ предоставляет ответы на часто задаваемые вопросы о библиотеке `TinyTroupe` и аспектах ответственного использования ИИ (Responsible AI) в контексте этой библиотеки.

## Подробней

`TinyTroupe` - это экспериментальная библиотека на языке Python, которая позволяет **моделировать** поведение людей с определенными личностями, интересами и целями. Эти искусственные агенты, называемые `TinyPerson`, могут слушать, отвечать и жить своей жизнью в смоделированных средах `TinyWorld`. Это достигается за счет использования мощных языковых моделей (LLM), таких как GPT-4, для генерации реалистичного поведения. Это позволяет исследовать широкий спектр **реалистичных взаимодействий** и **типов потребителей** с **настраиваемыми личностями** в **выбранных условиях**.

Основное внимание уделяется *пониманию* человеческого поведения, а не непосредственной *поддержке* (как это делают AI-помощники). Это приводит, среди прочего, к специализированным механизмам и конструктивным решениям, которые имеют смысл только в контексте моделирования.

Подход `TinyTroupe` является программным: моделирование задается как программы на Python с использованием элементов `TinyTroupe`, а затем выполняется. Входные данные для моделирования включают описание личностей (например, возраст, национальность, местоположение, интересы, работа и т. д.) и разговоры (например, программист может "разговаривать" с агентами). Выходные данные включают мысли и слова агентов, а также структурированные извлечения из них (например, сводку разговоров).

## Функции

### `Что может TinyTroupe?`

`TinyTroupe` сама по себе не является моделью искусственного интеллекта (AI) или машинного обучения (ML). Вместо этого она полагается на внешние API для обеспечения своих интеллектуальных возможностей. `TinyTroupe` предоставляет элементы для:

- моделирования личностей агентов, включая их мысли и слова;
- моделирования сред, в которых агенты взаимодействуют;
- извлечения структурированных выходных данных из моделирования для последующего использования (например, JSON с различными извлеченными элементами);
- обогащения артефактов моделирования, чтобы сделать их более реалистичными;
- помощи в рассказывании историй, чтобы сделать моделирование более интересным.

### `Каковы предполагаемые цели использования TinyTroupe?`

`TinyTroupe` предназначена для:

- анализа искусственного человеческого поведения посредством моделирования;
- генерации синтетических артефактов посредством моделирования;
- дополнения, а не замены, генерации человеческого понимания;
- исследования различных возможностей вычислительных когнитивных архитектур, которые могут отражать или не отражать фактическое человеческое познание.

`TinyTroupe` НЕ предназначена для:

- прямого взаимодействия с пользователями. Программисты, полагающиеся на `TinyTroupe` для продуктов, должны создать свой собственный уровень ответственного AI, чтобы гарантировать, что результаты моделирования подходят.
- принятия решений в области политики или каких-либо важных решений. Любое решение, принятое с использованием моделирования `TinyTroupe`, должно учитывать, что результаты моделирования могут не отражать реальность и поэтому должны использоваться очень осторожно для всего, что имеет реальное влияние на мир.

### `Как оценивалась TinyTroupe? Какие метрики используются для измерения производительности?`

`TinyTroupe` оценивалась с помощью различных вариантов использования, часть из которых представлена в качестве примеров в библиотеке. Она подходит для использования в этих сценариях в той степени, в которой показывают демонстрации. Все, что выходит за рамки этого, остается исследовательской и экспериментальной работой. Обширное модульное и сценарное тестирование также являются частью библиотеки.

### `Каковы ограничения TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?`

Не было показано, что `TinyTroupe` соответствует реальному человеческому поведению, и поэтому любая такая возможность остается простым исследованием или экспериментальным исследованием.

Хотя это не наблюдалось в наших различных тестах, `TinyTroupe` имеет теоретический потенциал для генерации вывода, который можно считать вредоносным. Причина этого в том, что одним из важных теоретических вариантов использования `TinyTroupe` является проверка **других** AI-систем на наличие таких вредоносных выходных данных, поэтому ничто не мешает ей моделировать плохих актеров. Поэтому программисты, использующие `TinyTroupe` для создания собственных продуктов или услуг на ее основе, ДОЛЖНЫ предоставить свои собственные средства защиты ответственного AI, поскольку `TinyTroupe` сама по себе не предназначена для ограничения выходных данных таким образом. Это ТОТ ЖЕ САМЫЙ СЛУЧАЙ для любой другой базовой библиотеки LLM, такой как LangChain или Semantic Kernel, которые, как и `TinyTroupe`, являются простыми ИНСТРУМЕНТАМИ, которые следует использовать с осторожностью.

### `Какие операционные факторы и параметры позволяют эффективно и ответственно использовать TinyTroupe?`

`TinyTroupe` можно использовать ответственно, если:

- использовать внешние API моделей, которые сами предоставляют механизмы безопасности (например, Azure OpenAI предоставляет обширные ресурсы для этой цели).
- предоставлять подходящие описания личностей (т. е. не вредоносные личности);
- не вызывать сюжетные линии моделирования или поведение агентов для генерации вредоносного контента. Если это сделано, полностью осознавайте, что ЕДИНСТВЕННЫМ разрешенным использованием этого является проверка других AI-систем на наличие таких нежелательных выходных данных.
- НЕ позволяйте моделированию контролировать механизмы реального мира, если не предусмотрены соответствующие механизмы контроля повреждений для предотвращения фактического причинения вреда.
- если вы используете `TinyTroupe` для поддержки своего собственного продукта или услуги, ВЫ ДОЛЖНЫ предоставить свои собственные средства защиты ответственного AI, такие как проверка выходных данных.