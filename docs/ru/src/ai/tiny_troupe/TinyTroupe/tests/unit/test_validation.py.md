# `test_validation.py`

## Обзор

Этот файл содержит модульные тесты для проверки валидации персонажей, созданных с помощью `TinyPersonFactory`, используя `TinyPersonValidator`. Тесты проверяют, насколько хорошо сгенерированные персонажи соответствуют заданным ожиданиям.

## Оглавление
- [Функции](#Функции)
  - [`test_validate_person`](#test_validate_person)

## Функции

### `test_validate_person`

**Описание**:
Тестирует валидацию персонажей, созданных с помощью `TinyPersonFactory` и проверенных с использованием `TinyPersonValidator`.

**Параметры**:
- `setup` (fixture): Фикстура pytest для настройки тестовой среды.

**Возвращает**:
- `None`

**Пример использования**:

```python
def test_validate_person(setup):
    # Тест для банкира
    banker_spec = """
    A vice-president of one of the largest brazillian banks. Has a degree in engineering and an MBA in finance.
    Is facing a lot of pressure from the board of directors to fight off the competition from the fintechs.
    """
    banker_factory = TinyPersonFactory(banker_spec)
    banker = banker_factory.generate_person()
    banker_expectations = """
    He/she is:
    - Wealthy
    - Very intelligent and ambitious
    - Has a lot of connections
    - Is in his 40s or 50s

    Tastes:
    - Likes to travel to other countries
    - Either read books, collect art or play golf
    - Enjoy only the best, most expensive, wines and food
    - Dislikes communists, unions and the like

    Other notable traits:
    - Has some stress issues, and might be a bit of a workaholic
    - Deep knowledge of finance, economics and financial technology
    - Is a bit of a snob
    - Might pretend to be a hard-core woke, but in reality that's just a facade to climb the corporate ladder
    """
    banker_score, banker_justification = TinyPersonValidator.validate_person(banker, expectations=banker_expectations, include_agent_spec=False, max_content_length=None)
    print("Banker score: ", banker_score)
    print("Banker justification: ", banker_justification)
    assert banker_score > 0.5, f"Validation score is too low: {banker_score:.2f}"

    # Тест для буддийского монаха
    monk_spec = """
    A poor buddhist monk living alone and isolated in a remote montain.
    """
    monk_spec_factory = TinyPersonFactory(monk_spec)
    monk = monk_spec_factory.generate_person()
    monk_expectations = """
    Some characteristics of this person:
    - Is very poor, and in fact do not seek money
    - Has no formal education, but is very wise
    - Is very calm and patient
    - Is very humble and does not seek attention
    - Honesty is a core value
    """
    monk_score, monk_justification = TinyPersonValidator.validate_person(monk, expectations=monk_expectations, include_agent_spec=False, max_content_length=None)
    print("Monk score: ", monk_score)
    print("Monk justification: ", monk_justification)
    assert monk_score > 0.5, f"Validation score is too low: {monk_score:.2f}"

    # Тест с неправильными ожиданиями
    wrong_expectations_score, wrong_expectations_justification = TinyPersonValidator.validate_person(monk, expectations=banker_expectations, include_agent_spec=False, max_content_length=None)
    assert wrong_expectations_score < 0.5, f"Validation score is too high: {wrong_expectations_score:.2f}"
    print("Wrong expectations score: ", wrong_expectations_score)
    print("Wrong expectations justification: ", wrong_expectations_justification)
```