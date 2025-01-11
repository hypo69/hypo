# Документация модуля `test_brainstorming_scenarios.py`

## Обзор

Этот модуль содержит тесты для проверки сценария мозгового штурма с использованием фреймворка `tinytroupe`. В нем создается тестовая среда с агентами, которые участвуют в мозговом штурме и генерируют идеи для нового продукта.

## Оглавление

- [Функции](#функции)
    - [`test_brainstorming_scenario`](#test_brainstorming_scenario)

## Функции

### `test_brainstorming_scenario`

**Описание**: Тестирует сценарий мозгового штурма, в котором агенты генерируют идеи для нового продукта (в данном случае, для Microsoft Word).

**Параметры**:
- `setup` (fixture): Фикстура pytest, которая обеспечивает начальную настройку тестовой среды.
- `focus_group_world` (TinyWorld): Экземпляр `TinyWorld`, представляющий собой тестовую среду, в которой агенты участвуют в мозговом штурме.

**Возвращает**:
- `None`: Функция ничего не возвращает, но делает проверки, используя оператор `assert`.

**Вызывает исключения**:
- `AssertionError`: Выбрасывается, если утверждение, проверяющее результаты мозгового штурма, оказывается ложным.

```python
def test_brainstorming_scenario(setup, focus_group_world):
    """
    Args:
        setup (fixture): Фикстура pytest, которая обеспечивает начальную настройку тестовой среды.
        focus_group_world (TinyWorld): Экземпляр `TinyWorld`, представляющий собой тестовую среду, в которой агенты участвуют в мозговом штурме.

    Returns:
        None: Функция ничего не возвращает, но делает проверки, используя оператор `assert`.

    Raises:
        AssertionError: Выбрасывается, если утверждение, проверяющее результаты мозгового штурма, оказывается ложным.
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