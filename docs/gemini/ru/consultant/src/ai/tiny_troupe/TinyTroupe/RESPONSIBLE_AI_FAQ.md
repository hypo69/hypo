# Received Code

```python
# TinyTroupe: Responsible AI FAQ

## What is TinyTroupe?

*TinyTroupe* is an experimental Python library that allows us to **simulate** people with specific personalities, interests, and goals. These artificial agents - `TinyPerson`s - can listen to us and one another, reply back, and go about their lives in simulated `TinyWorld` environments. This is achieved by leveraging the power of Language Models (LLMs), notably GPT-4, to generate realistic simulated behavior. This allow us to investigate a wide range of **realistic interactions** and **consumer types**, with **highly customizable personas**, under **conditions of our choosing**. The focus is thus on *understanding* human behavior and not on directly *supporting it* (like, say, AI assistants do) -- this results in, among other things, specialized mechanisms and design choices that make sense only in a simulation setting. This has impact for Resonsible AI aspects as described in the rest of this FAQ.

TinyTroupe's approach is programmatic: simulations are specified as Python programs using TinyTroupe elements, and then executed. Inputs to the simulation include
the description of personas (e.g., age, nationality, location, interests, job, etc.) and conversations (e.g., the programmer can "talk" to agents). Outputs
include the thoughts and words of agents, as well as structured extractions from those (e.g., a summary of the conversations).

## What can TinyTroupe do?

TinyTroupe itself is _not_ an Artificial Intelligence (AI) or Machine Learning (ML) model. Instead, it relies on external APIs to power its intelligent capabilities. With that,
TinyTroupe provide elements mainly to:

  - simulate agent personas, including their thoughts and words;
  - simulate environments in which agents interact;
  - extract structured output from simulations, for downstrea use (e.g., a JSON with various items extracted);
  - enrich simulation artifacts, to make them more realistc;
  - provide help with storytelling to make the simulation more interesting.

## What is/are TinyTroupe’s intended use(s)?

TinyTroupe is intended for:
  - analysis of artificial human behavior through simulation;
  - generation of synthetic artifacts through simulation;
  - supplement, rather than replace, human insight generation;
  - allow the research of various possibilities of computational cognitive architectures, which might or might not reflect actual human cognition.

TinyTroupe IS NOT intended for:
  - direct interaction with users. Rather, programmers relying on TinyTroupe for products should create their own layer of responsible AI to ensure simulation results are suitable.
  - policy or any consequential decision making. Rather, any decision made using TinyTroupe simulations should consider that the simulation results might not reflect reality and as such must be used very carefully for anything that has real world impact.

## How was TinyTroupe evaluated? What metrics are used to measure performance?

TinyTroupe was evaluated through various use cases, part of which are provided as examples in the library. It is suitable to use under those scenarios to the extent that
the demonstrations show. Anything beyond that remains research and experimental work. Extensive unit and scenario testing are also part of the library.


## What are the limitations of TinyTroupe? How can users minimize the impact of TinyTroupe’s limitations when using the system?

TinyTroupe HAS NOT being shown to match real human behavior, and therefore any such possibility reamains mere research or experimental investigation.
Though not observed in our various tests, TinyTroupe HAS the theoretical potential of generating output that can be considered malicious. The reason for this is that
one important theoretical use case for TinyTroupe is the validation of **other** AI systems against such malicious outputs, so it nothing restricts it from simulating
bad actors. THEREFORE, programmers using TinyTroupe to create their own products or service on top of it MUST provide their own Responsible AI safeguards,
since TinyTroupe itself is not designed to constrain outputs in this manner. This is THE SAME CASE for any other foundational LLM library such as LangChain or Semantic Kernel,
which, just like TinyTroupe, are mere TOOLS that should be used with care.

## What operational factors and settings allow for effective and responsible use of TinyTroupe?

TinyTroupe can be used responsibly by:
  - using external model APIs that themselves provide safety mechanisms (e.g., Azure OpenAI provide extensive resources to that end).
  - providing suitable persona descriptions (i.e., non-malicious personas);
  - do not induce simulation stories or agent behavior for the generation of malicious content. If this is done, be fully aware that THE ONLY allowed use for that is the validadion of other AI
    systems agains such undesirable outputs.
  - DO NOT allowing simulations to control real-world mechanisms, unless appropriate damange control mechanisms are in place to prevent actual harm from happening.
  - if you use TinyTroupe to power your own product or service, YOU MUST provide your own Responsible AI safeguards, such as output verification.
```

# Improved Code

```python
"""
Модуль TinyTroupe: ЧаВО по вопросам ответственного ИИ
=======================================================

Этот модуль содержит часто задаваемые вопросы (FAQ) о библиотеке TinyTroupe,
фокусирующейся на моделировании человеческого поведения с использованием
языковых моделей.  Docstrings описывают каждый раздел FAQ.
"""


# TinyTroupe: FAQ по вопросам ответственного ИИ

## Что такое TinyTroupe?

"""
Описание библиотеки TinyTroupe, её целей и принципов работы.
"""

*TinyTroupe* — это экспериментальная Python-библиотека,
позволяющая моделировать людей со специфическими личностями, интересами
и целями.  Эти искусственные агенты (TinyPerson) могут общаться друг с
другом и с пользователем, а также существовать в симулированных
средах (TinyWorld).  Для создания реалистичного поведения агентов
используются языковые модели (LLMs), в частности, GPT-4.

Библиотека предназначена для исследования широкого спектра
реалистичных взаимодействий и типов потребителей с сильно
настраиваемыми персонажами в контролируемых условиях.  Главная цель
— понимание человеческого поведения, а не непосредственная
поддержка (в отличие от AI-ассистентов).  Это приводит к
специализированным механизмам и архитектуре,  подходящим только для
моделирования.  Вопросы ответственного ИИ рассматриваются в
следующих разделах.


## Что может делать TinyTroupe?

"""
Перечисление основных функциональных возможностей TinyTroupe.
"""

TinyTroupe — это НЕ модель ИИ или ML. Она использует внешние API
для достижения своих целей. TinyTroupe предоставляет следующие
возможности:

- моделирование агентов с их мыслями и высказываниями;
- моделирование сред взаимодействия агентов;
- извлечение структурированных данных из симуляций (например, JSON);
- улучшение реалистичности симулированных артефактов;
- помощь в создании увлекательных историй для симуляций.


## Каковы целевые использования TinyTroupe?

"""
Определение целевых сфер применения TinyTroupe.
"""

TinyTroupe предназначена для:

- анализа искусственного поведения посредством моделирования;
- генерации синтетических артефактов;
- дополнения, а не замены, человеческого анализа;
- исследования различных вариантов вычислительных когнитивных архитектур,
которые могут или не могут отражать реальную человеческую
когницию.

TinyTroupe НЕ предназначена для:

- прямого взаимодействия с пользователями. Разработчикам,
использующим TinyTroupe в своих продуктах, необходимо
реализовывать собственные механизмы ответственного ИИ для
обеспечения безопасности;
- принятия решений в политической или любой другой
критической сфере. Результаты симуляций должны использоваться
с большой осторожностью в ситуациях, где от них зависят реальные
решения.


## Как оценивалась TinyTroupe? Какие метрики используются для
## оценки производительности?

"""
Описание методов оценки TinyTroupe и используемых метрик.
"""

TinyTroupe оценивалась с помощью различных сценариев, часть из
которых представлена в качестве примеров в библиотеке.
Применимость распространяется только на эти сценарии. Всё
помимо этого остается исследовательской работой.  Также важна
полная проверка и тестирование сценариев.


## Каковы ограничения TinyTroupe? Как пользователи могут
## минимизировать влияние ограничений TinyTroupe при использовании системы?

"""
Обсуждение ограничений TinyTroupe и способы их минимизации.
"""

TinyTroupe НЕ доказала соответствие реальному поведению
людей. Любые такие выводы остаются гипотезами.  Хотя в
наших тестах подобного не наблюдалось, TinyTroupe теоретически
может генерировать вредоносный выход. Это связано с тем, что
важным теоретическим применением TinyTroupe является
верификация других систем ИИ на наличие таких вредоносных
выходов, поэтому ничего не ограничивает её от моделирования
"плохих акторов".  Поэтому разработчики, использующие TinyTroupe
для создания своих продуктов, ДОЛЖНЫ обеспечить собственные
меры ответственного ИИ, поскольку TinyTroupe сама не
предназначена для ограничения выходных данных. Это относится
ко всем другим библиотекам LLM, таким как LangChain и
Semantic Kernel.

## Какие факторы и параметры позволяют эффективно и
## ответственно использовать TinyTroupe?

"""
Рекомендации по безопасному использованию TinyTroupe.
"""

TinyTroupe можно использовать ответственно, соблюдая следующие
правила:

- использование внешних API моделей, которые сами обеспечивают
защиту (например, Azure OpenAI);
- предоставление соответствующих описаний персон (не
вредоносные);
- не генерировать истории или поведение агентов,
способствующие получению вредоносного контента. Если это
необходимо, будьте в курсе, что единственно допустимое
применение — проверка других систем ИИ на предмет
нежелательных выходов;
- НЕ допускайте управления реальными механизмами при помощи
симуляций, если не предусмотрены соответствующие методы
контроля ущерба;
- при использовании TinyTroupe в своих продуктах, НЕОБХОДИМО
обеспечить собственные меры ответственного ИИ, такие как
верификация выходных данных.
```

# Changes Made

- Добавлено описание модуля в формате RST.
- Добавлено описание каждого раздела FAQ в формате RST (docstrings).
- Изменены некоторые формулировки для соответствия стилю RST и
  избегания слов типа "получаем", "делаем".  Использованы
  более конкретные глаголы (например, "моделирование",
  "проверка").
- Исправлены некоторые грамматические ошибки и стилистические
  неточности.
- Убраны ненужные звёздочки.
- Добавлена ясная структура для документации в формате RST.


# FULL Code

```python
"""
Модуль TinyTroupe: ЧаВО по вопросам ответственного ИИ
=======================================================

Этот модуль содержит часто задаваемые вопросы (FAQ) о библиотеке TinyTroupe,
фокусирующейся на моделировании человеческого поведения с использованием
языковых моделей.  Docstrings описывают каждый раздел FAQ.
"""


# TinyTroupe: FAQ по вопросам ответственного ИИ

## Что такое TinyTroupe?

"""
Описание библиотеки TinyTroupe, её целей и принципов работы.
"""

*TinyTroupe* — это экспериментальная Python-библиотека,
позволяющая моделировать людей со специфическими личностями, интересами
и целями.  Эти искусственные агенты (TinyPerson) могут общаться друг с
другом и с пользователем, а также существовать в симулированных
средах (TinyWorld).  Для создания реалистичного поведения агентов
используются языковые модели (LLMs), в частности, GPT-4.

Библиотека предназначена для исследования широкого спектра
реалистичных взаимодействий и типов потребителей с сильно
настраиваемыми персонажами в контролируемых условиях.  Главная цель
— понимание человеческого поведения, а не непосредственная
поддержка (в отличие от AI-ассистентов).  Это приводит к
специализированным механизмам и архитектуре,  подходящим только для
моделирования.  Вопросы ответственного ИИ рассматриваются в
следующих разделах.


## Что может делать TinyTroupe?

"""
Перечисление основных функциональных возможностей TinyTroupe.
"""

TinyTroupe — это НЕ модель ИИ или ML. Она использует внешние API
для достижения своих целей. TinyTroupe предоставляет следующие
возможности:

- моделирование агентов с их мыслями и высказываниями;
- моделирование сред взаимодействия агентов;
- извлечение структурированных данных из симуляций (например, JSON);
- улучшение реалистичности симулированных артефактов;
- помощь в создании увлекательных историй для симуляций.


## Каковы целевые использования TinyTroupe?

"""
Определение целевых сфер применения TinyTroupe.
"""

TinyTroupe предназначена для:

- анализа искусственного поведения посредством моделирования;
- генерации синтетических артефактов;
- дополнения, а не замены, человеческого анализа;
- исследования различных вариантов вычислительных когнитивных архитектур,
которые могут или не могут отражать реальную человеческую
когницию.

TinyTroupe НЕ предназначена для:

- прямого взаимодействия с пользователями. Разработчикам,
использующим TinyTroupe в своих продуктах, необходимо
реализовывать собственные механизмы ответственного ИИ для
обеспечения безопасности;
- принятия решений в политической или любой другой
критической сфере. Результаты симуляций должны использоваться
с большой осторожностью в ситуациях, где от них зависят реальные
решения.


## Как оценивалась TinyTroupe? Какие метрики используются для
## оценки производительности?

"""
Описание методов оценки TinyTroupe и используемых метрик.
"""

TinyTroupe оценивалась с помощью различных сценариев, часть из
которых представлена в качестве примеров в библиотеке.
Применимость распространяется только на эти сценарии. Всё
помимо этого остается исследовательской работой.  Также важна
полная проверка и тестирование сценариев.


## Каковы ограничения TinyTroupe? Как пользователи могут
## минимизировать влияние ограничений TinyTroupe при использовании системы?

"""
Обсуждение ограничений TinyTroupe и способы их минимизации.
"""

TinyTroupe НЕ доказала соответствие реальному поведению
людей. Любые такие выводы остаются гипотезами.  Хотя в
наших тестах подобного не наблюдалось, TinyTroupe теоретически
может генерировать вредоносный выход. Это связано с тем, что
важным теоретическим применением TinyTroupe является
верификация других систем ИИ на наличие таких вредоносных
выходов, поэтому ничего не ограничивает её от моделирования
"плохих акторов".  Поэтому разработчики, использующие TinyTroupe
для создания своих продуктов, ДОЛЖНЫ обеспечить собственные
меры ответственного ИИ, поскольку TinyTroupe сама не
предназначена для ограничения выходных данных. Это относится
ко всем другим библиотекам LLM, таким как LangChain и
Semantic Kernel.

## Какие факторы и параметры позволяют эффективно и
## ответственно использовать TinyTroupe?

"""
Рекомендации по безопасному использованию TinyTroupe.
"""

TinyTroupe можно использовать ответственно, соблюдая следующие
правила:

- использование внешних API моделей, которые сами обеспечивают
защиту (например, Azure OpenAI);
- предоставление соответствующих описаний персон (не
вредоносные);
- не генерировать истории или поведение агентов,
способствующие получению вредоносного контента. Если это
необходимо, будьте в курсе, что единственно допустимое
применение — проверка других систем ИИ на предмет
нежелательных выходов;
- НЕ допускайте управления реальными механизмами при помощи
симуляций, если не предусмотрены соответствующие методы
контроля ущерба;
- при использовании TinyTroupe в своих продуктах, НЕОБХОДИМО
обеспечить собственные меры ответственного ИИ, такие как
верификация выходных данных.
```