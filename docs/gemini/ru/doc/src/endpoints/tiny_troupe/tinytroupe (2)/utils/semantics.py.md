# Модуль semantics.py

## Обзор

Модуль содержит функции, связанные с семантическими операциями, такими как перефразирование текста и структурирование описаний событий в контексте ожиданий. Используются механизмы `llm` для обработки этих операций.

## Подробнее

Этот модуль предоставляет инструменты для изменения или переформулировки входных данных на основе заданных правил и для структурирования информации о событиях и ожиданиях, что полезно для анализа и модификации системных выходов.

## Функции

### `rephrase`

```python
@llm()
def rephrase(observation: str, rule: str) -> str:
    """
    Перефразирует или полностью изменяет данное наблюдение в соответствии с указанным правилом.

    Args:
        observation (str): Наблюдение, которое следует перефразировать или изменить. Это может быть сказанное, сделанное, описание событий или фактов.
        rule (str): Правило, определяющее, как должно быть изменено наблюдение.

    Returns:
        str: Перефразированное или измененное наблюдение.

    Как работает функция:
    1. Декоратор `@llm()` обрабатывает тело этой функции, используя возможности языковой модели для перефразирования входных данных.

    Примеры:
        Observation: "You know, I am so sad these days."
        Rule: "I am always happy and depression is unknown to me"
        Modified observation: "You know, I am so happy these days."
    """
```

### `restructure_as_observed_vs_expected`

```python
@llm()
def restructure_as_observed_vs_expected(description: str) -> str:
    """
    Извлекает из описания события или концепции элементы, связанные с нарушением или соответствием ожиданиям.

    Args:
        description (str): Описание события или концепции, которое либо нарушает, либо соответствует ожиданию.

    Returns:
        str: Структурированное описание, содержащее элементы OBSERVED, BROKEN EXPECTATION (или MET EXPECTATION) и REASONING.

    Как работает функция:
    1. Декоратор `@llm()` обрабатывает тело этой функции, используя языковую модель для извлечения и структурирования информации.

    Примеры:
        Input: "Ana mentions she loved the proposed new food, a spicier flavor of gazpacho. However, this goes agains her known dislike
                of spicy food."
        Output:
            "OBSERVED: Ana mentions she loved the proposed new food, a spicier flavor of gazpacho.
             BROKEN EXPECTATION: Ana should have mentioned that she disliked the proposed spicier gazpacho.
             REASONING: Ana has a known dislike of spicy food."

        Input: "Carlos traveled to Firenzi and was amazed by the beauty of the city. This was in line with his love for art and architecture."
        Output:
            "OBSERVED: Carlos traveled to Firenzi and was amazed by the beauty of the city.
             MET EXPECTATION: Carlos should have been amazed by the beauty of the city.
             REASONING: Carlos loves art and architecture."
    """