# Документация модуля `test_brainstorming_scenarios.py`

## Оглавление

1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`test_brainstorming_scenario`](#test_brainstorming_scenario)

## Обзор

Модуль `test_brainstorming_scenarios.py` предназначен для тестирования сценария мозгового штурма с использованием фреймворка `tinytroupe`. Он создает симуляцию, в которой агенты обсуждают и генерируют идеи для новых продуктов, а затем извлекает и анализирует результаты обсуждения.

## Функции

### `test_brainstorming_scenario`

**Описание**:
Функция `test_brainstorming_scenario` реализует сценарий мозгового штурма, в котором группа агентов обсуждает идеи для нового продукта. В данном случае, агенты генерируют идеи для новых функций AI в Microsoft Word. После обсуждения функция извлекает и проверяет результаты.

**Параметры**:
- `setup`: (pytest.fixture) Фикстура pytest для настройки тестового окружения.
- `focus_group_world` (TinyWorld): Экземпляр мира `TinyWorld`, представляющий собой окружение для симуляции.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если проверка результатов мозгового штурма не проходит.

```python
def test_brainstorming_scenario(setup, focus_group_world):
    """
    Args:
        setup (pytest.fixture): Фикстура pytest для настройки тестового окружения.
        focus_group_world (TinyWorld): Экземпляр мира `TinyWorld`, представляющий собой окружение для симуляции.

    Returns:
        None

    Raises:
        AssertionError: Если проверка результатов мозгового штурма не проходит.
    """
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