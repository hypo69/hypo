# TinyTroupe: Responsible AI FAQ

## Обзор

*TinyTroupe* - это экспериментальная библиотека Python, которая позволяет **моделировать** людей с определенными личностями, интересами и целями. Эти искусственные агенты - `TinyPerson`s - могут слушать нас и друг друга, отвечать и заниматься своими делами в моделируемых средах `TinyWorld`. Это достигается за счет использования возможностей языковых моделей (LLM), особенно GPT-4, для генерации реалистичного моделируемого поведения. Это позволяет исследовать широкий спектр **реалистичных взаимодействий** и **типов потребителей** с **настраиваемыми персонажами** в **выбранных нами условиях**. Таким образом, основное внимание уделяется *пониманию* человеческого поведения, а не прямой *поддержке* его (как, например, делают AI-помощники) — это приводит, среди прочего, к специализированным механизмам и проектным решениям, которые имеют смысл только в условиях моделирования. Это оказывает влияние на аспекты Resonsible AI, как описано в остальной части этого FAQ.

Подход TinyTroupe является программным: симуляции задаются как программы на Python с использованием элементов TinyTroupe, а затем выполняются. Входные данные для симуляции включают описание персонажей (например, возраст, национальность, местоположение, интересы, работа и т. д.) и разговоры (например, программист может "разговаривать" с агентами). Выходные данные включают мысли и слова агентов, а также структурированные извлечения из них (например, сводку разговоров).

## Оглавление

1. [Что такое TinyTroupe?](#что-такое-tinytroupe)
2. [Что может делать TinyTroupe?](#что-может-делать-tinytroupe)
3. [Каковы предполагаемые области применения TinyTroupe?](#каковы-предполагаемые-области-применения-tinytroupe)
4. [Как оценивался TinyTroupe? Какие метрики используются для измерения производительности?](#как-оценивался-tinytroupe-какие-метрики-используются-для-измерения-производительности)
5. [Каковы ограничения TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?](#каковы-ограничения-tinytroupe-как-пользователи-могут-минимизировать-влияние-ограничений-tinytroupe-при-использовании-системы)
6. [Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?](#какие-операционные-факторы-и-настройки-позволяют-эффективно-и-ответственно-использовать-tinytroupe)

## Что может делать TinyTroupe?

TinyTroupe сам по себе _не_ является моделью искусственного интеллекта (AI) или машинного обучения (ML). Вместо этого он полагается на внешние API для обеспечения своих интеллектуальных возможностей. При этом TinyTroupe предоставляет элементы в основном для:
  
  - моделирования личностей агентов, включая их мысли и слова;
  - моделирования сред, в которых агенты взаимодействуют;
  - извлечения структурированных выходных данных из симуляций для последующего использования (например, JSON с различными извлеченными элементами);
  - обогащения артефактов симуляции, чтобы сделать их более реалистичными;
  - помощи в рассказывании историй, чтобы сделать симуляцию более интересной.

## Каковы предполагаемые области применения TinyTroupe?

TinyTroupe предназначен для:
  - анализа искусственного поведения человека путем моделирования;
  - генерации синтетических артефактов путем моделирования;
  - дополнения, а не замены, генерации человеческих идей;
  - исследования различных возможностей вычислительных когнитивных архитектур, которые могут или не могут отражать фактическое человеческое познание.
  
TinyTroupe НЕ предназначен для:
  - прямого взаимодействия с пользователями. Скорее, программисты, полагающиеся на TinyTroupe для продуктов, должны создать свой собственный уровень ответственного ИИ, чтобы гарантировать, что результаты моделирования являются подходящими.
  - формирования политики или принятия каких-либо важных решений. Скорее, любое решение, принятое с использованием симуляций TinyTroupe, должно учитывать, что результаты моделирования могут не отражать реальность и поэтому должны использоваться очень осторожно для всего, что имеет реальное воздействие на мир.

## Как оценивался TinyTroupe? Какие метрики используются для измерения производительности?

TinyTroupe оценивался на основе различных вариантов использования, часть которых представлена в виде примеров в библиотеке. Он подходит для использования в этих сценариях в той степени, в которой показывают демонстрации. Все, что выходит за рамки этого, остается исследовательскими и экспериментальными работами. Обширное модульное и сценарное тестирование также является частью библиотеки.

## Каковы ограничения TinyTroupe? Как пользователи могут минимизировать влияние ограничений TinyTroupe при использовании системы?

Не было показано, что TinyTroupe соответствует реальному человеческому поведению, и поэтому любая такая возможность остается лишь исследованием или экспериментальным исследованием.
Хотя в наших различных тестах этого не наблюдалось, TinyTroupe имеет теоретический потенциал для генерации выходных данных, которые можно считать вредоносными. Причина этого заключается в том, что
одним из важных теоретических вариантов использования TinyTroupe является проверка **других** систем ИИ на предмет таких вредоносных выходных данных, поэтому ничто не мешает ему моделировать
плохих актеров. СЛЕДОВАТЕЛЬНО, программисты, использующие TinyTroupe для создания собственных продуктов или услуг на его основе, ДОЛЖНЫ предоставлять свои собственные средства защиты ответственного ИИ,
поскольку TinyTroupe сам по себе не предназначен для ограничения вывода таким образом. ТО ЖЕ САМОЕ ОТНОСИТСЯ к любой другой фундаментальной библиотеке LLM, такой как LangChain или Semantic Kernel,
которые, как и TinyTroupe, являются всего лишь ИНСТРУМЕНТАМИ, которые следует использовать с осторожностью.

## Какие операционные факторы и настройки позволяют эффективно и ответственно использовать TinyTroupe?

TinyTroupe можно использовать ответственно:
  - используя внешние API-интерфейсы моделей, которые сами предоставляют механизмы безопасности (например, Azure OpenAI предоставляет обширные ресурсы для этой цели).
  - предоставляя подходящие описания персонажей (т. е. не вредоносных персонажей);
  - не инициируя симуляционные истории или поведение агентов для генерации вредоносного контента. Если это сделано, полностью осознавайте, что ЕДИНСТВЕННЫМ допустимым использованием этого является проверка других ИИ
    систем на предмет таких нежелательных выходных данных.
  - НЕ допускать, чтобы симуляции контролировали механизмы реального мира, если не установлены соответствующие механизмы контроля повреждений для предотвращения фактического вреда.
  - если вы используете TinyTroupe для поддержки своего собственного продукта или услуги, ВЫ ДОЛЖНЫ предоставлять свои собственные средства защиты ответственного ИИ, такие как проверка вывода.