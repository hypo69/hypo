# Модуль `test_brainstorming_scenarios.py`

## Обзор

Этот модуль содержит тесты для сценариев мозгового штурма, использующих фреймворк TinyTroupe. Тесты проверяют, что агенты могут эффективно взаимодействовать в рамках заданных сценариев мозгового штурма, извлекать и обобщать результаты.

## Импорты

```python
import pytest
import logging
logger = logging.getLogger("tinytroupe")

import sys
# ... (импорты)
import tinytroupe.control as control
from tinytroupe.control import Simulation
from testing_utils import *
```

## Функции

### `test_brainstorming_scenario`

**Описание**: Эта функция тестирует сценарий мозгового штурма, где участники обсуждают идеи для новых функций в Microsoft Word. Она проверяет, что агенты могут извлекать и обобщать результаты обсуждения.

**Аргументы**:

- `setup`: (Описание аргумента) -  Предполагается, что это настройка, необходимая для запуска теста, например, инициализация окружения.
- `focus_group_world`: (Описание аргумента) - объект `TinyWorld`, представляющий фокус-группу для проведения мозгового штурма.


**Возвращает**:
-  Ничего не возвращает.


**Вызывает исключения**:
-  `AssertionError`: Если утверждение `proposition_holds` не выполняется, то есть результаты не соответствуют ожидаемому выводу.


**Детали реализации**:

1. Функция получает `focus_group_world` и запускает симуляцию.
2. Вызывает метод `broadcast` на `world`, чтобы запустить обсуждение.
3. Запускает симуляцию.
4. Получает агента "Lisa"
5. Задает вопрос агенту о суммарных идеях.
6. Создает экземпляр `ResultsExtractor`.
7. Извлекает результаты из агента, используя `extract_results_from_agent`.
8. Выводит результаты в консоль.
9. Использует `proposition_holds` для проверки, соответствуют ли результаты ожидаемым.
10. Исключает `AssertionError`, если утверждение ложно.


```python
def test_brainstorming_scenario(setup, focus_group_world):
    world = focus_group_world

    world.broadcast("""
             Folks, we need to brainstorm ideas for a new product. Your mission is to discuss potential AI feature ideas
             to add to Microsoft Word. In general, we want features that make you or your industry more productive,
             taking advantage of all the latest AI technologies.

             Please start the discussion now.
             """)
    
    world.run(1)

    agent = TinyPerson.get_agent_by_name("Lisa")

    agent.listen_and_act("Can you please summarize the ideas that the group came up with?")

    from tinytroupe.extraction import ResultsExtractor

    extractor = ResultsExtractor()

    results = extractor.extract_results_from_agent(agent, 
                            extraction_objective="Summarize the the ideas that the group came up with, explaining each idea as an item of a list. Describe in details the benefits and drawbacks of each.", 
                            situation="A focus group to brainstorm ideas for a new product.")

    print("Brainstorm Results: ", results)

    assert proposition_holds(f"The following contains some ideas for new product features or entirely new products: \'{results}\'"), f"Proposition is false according to the LLM."
```
```
## Вспомогательные функции (testing_utils)

### `proposition_holds`

**Описание**: (Необходимо описать функцию `proposition_holds` из файла `testing_utils`, если она доступна.)


##  Заключение

Этот модуль предоставляет функциональные тесты, которые проверяют работу агентов в сценариях мозгового штурма. Он демонстрирует как агенты могут взаимодействовать и извлекать результаты, что является важным аспектом фреймворка TinyTroupe.
```
```python