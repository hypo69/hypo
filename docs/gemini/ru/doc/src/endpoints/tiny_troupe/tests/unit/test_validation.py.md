# Модуль тестирования валидации `TinyPerson`

## Обзор

Модуль содержит юнит-тесты для проверки валидации персонажей, созданных с использованием `TinyPersonFactory` и `TinyPersonValidator`. Он проверяет, насколько хорошо сгенерированные персонажи соответствуют заданным ожиданиям.

## Подробнее

Этот модуль проверяет функциональность создания и валидации персонажей (`TinyPerson`) на соответствие заданным характеристикам и ожиданиям. Он использует `TinyPersonFactory` для генерации персонажей на основе предоставленных спецификаций и `TinyPersonValidator` для оценки соответствия персонажа заданным ожиданиям.

## Функции

### `test_validate_person`

```python
def test_validate_person(setup):
    """
    Тестирует валидацию персонажей банкира и монаха на соответствие заданным ожиданиям.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.

    Returns:
        None

    Raises:
        AssertionError: Если оценка валидации персонажа слишком низкая или высокая.

    Example:
        >>> test_validate_person(setup)
    """
```

**Как работает функция**:

Функция `test_validate_person` выполняет следующие шаги:

1.  **Создание спецификаций и фабрик для банкира и монаха:** Определяются спецификации для банка и банкира, а также для монастыря и монаха. Создаются экземпляры `TinyPersonFactory` для каждого из них.
2.  **Генерация персонажей:** Используя фабрики, генерируются объекты персонажей банкира и монаха.
3.  **Определение ожиданий:** Определяются ожидания относительно характеристик и качеств банкира и монаха.
4.  **Валидация персонажей:** Используется `TinyPersonValidator.validate_person` для оценки соответствия каждого персонажа заданным ожиданиям.
5.  **Проверка оценок валидации:** Утверждается, что оценка валидации для банкира и монаха превышает 0.5, что указывает на достаточно высокую степень соответствия ожиданиям. Также проверяется, что оценка валидации монаха с "неправильными" ожиданиями (ожиданиями банкира) ниже 0.5.
6.  **Вывод результатов:** Выводятся оценки валидации и обоснования для каждого персонажа.

```
test_validate_person
│
├─── Определение спецификаций и фабрик для банкира
│   │   bank_spec, banker_spec
│   │   banker_factory = TinyPersonFactory(bank_spec)
│
├─── Генерация персонажа банкира
│   │   banker = banker_factory.generate_person(banker_spec)
│
├─── Определение ожиданий для банкира
│   │   banker_expectations
│
├─── Валидация персонажа банкира
│   │   banker_score, banker_justification = TinyPersonValidator.validate_person(banker, expectations=banker_expectations, include_agent_spec=False, max_content_length=None)
│
├─── Проверка оценки валидации банкира
│   │   assert banker_score > 0.5
│
├─── Определение спецификаций и фабрик для монаха
│   │   monastery_spec, monk_spec
│   │   monk_spec_factory = TinyPersonFactory(monastery_spec)
│
├─── Генерация персонажа монаха
│   │   monk = monk_spec_factory.generate_person(monk_spec)
│
├─── Определение ожиданий для монаха
│   │   monk_expectations
│
├─── Валидация персонажа монаха
│   │   monk_score, monk_justification = TinyPersonValidator.validate_person(monk, expectations=monk_expectations, include_agent_spec=False, max_content_length=None)
│
├─── Проверка оценки валидации монаха
│   │   assert monk_score > 0.5
│
└─── Валидация монаха с "неправильными" ожиданиями
    │   wrong_expectations_score, wrong_expectations_justification = TinyPersonValidator.validate_person(monk, expectations=banker_expectations, include_agent_spec=False, max_content_length=None)
    │   assert wrong_expectations_score < 0.5
```

**Примеры**:

```python
# Для запуска теста требуется настроенная среда pytest
# Пример вызова внутри pytest:
# pytest test_validation.py