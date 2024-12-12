# Документация для `test_brainstorming_scenarios.py`

## Обзор

Этот файл содержит тесты для проверки сценария мозгового штурма с использованием библиотеки `tinytroupe`. Тест проверяет, как агенты взаимодействуют и генерируют идеи в рамках заданного сценария.

## Содержание

1.  [Функции](#функции)
    *   [`test_brainstorming_scenario`](#test_brainstorming_scenario)

## Функции

### `test_brainstorming_scenario`

**Описание**:
Тестирует сценарий мозгового штурма, где агенты обсуждают идеи для нового продукта, а затем один из агентов резюмирует их.

**Параметры**:
- `setup`: (pytest.fixture) Фикстура pytest, предоставляющая начальную настройку для тестов.
- `focus_group_world` (TinyWorld): Фикстура pytest, представляющая собой мир, где агенты могут взаимодействовать.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если предложение, сгенерированное LLM, не соответствует ожидаемым результатам.

```python
def test_brainstorming_scenario(setup, focus_group_world):
    """
    Args:
        setup (pytest.fixture): Фикстура pytest, предоставляющая начальную настройку для тестов.
        focus_group_world (TinyWorld): Фикстура pytest, представляющая собой мир, где агенты могут взаимодействовать.
    
    Returns:
        None: Функция не возвращает значения.
    
    Raises:
        AssertionError: Если предложение, сгенерированное LLM, не соответствует ожидаемым результатам.
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