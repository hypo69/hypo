# Модуль тестирования фабрики персонажей

## Обзор

Этот модуль содержит юнит-тесты для проверки корректности работы фабрики персонажей (`TinyPersonFactory`) в проекте `hypotez`. Он включает тесты для генерации персонажей на основе заданных спецификаций и проверки соответствия их кратких биографий ожидаемым характеристикам.

## Подробней

Модуль `test_factory.py` тестирует возможность создания персонажей с использованием `TinyPersonFactory`. Он проверяет, что сгенерированные персонажи соответствуют заданным спецификациям, а их краткие биографии адекватно отражают их роли и характеристики. Для этого используется функция `test_generate_person`, которая создает фабрику персонажей на основе спецификации банкира и проверяет, что сгенерированный персонаж имеет приемлемую краткую биографию для работы в банковской сфере.

## Классы

### `TinyPersonFactory`

**Описание**: Класс, отвечающий за создание персонажей на основе заданных спецификаций.

**Принцип работы**:
Класс `TinyPersonFactory` принимает на вход спецификацию персонажа и использует ее для генерации объектов `TinyPerson`. Он предоставляет метод `generate_person`, который возвращает новый экземпляр персонажа, соответствующий заданной спецификации.

**Методы**:
- `generate_person()`: Генерирует новый экземпляр персонажа на основе спецификации.

## Функции

### `test_generate_person`

```python
def test_generate_person(setup):
    """
    Генерирует персонажа на основе спецификации банкира и проверяет соответствие его краткой биографии.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.

    Returns:
        None

    Raises:
        AssertionError: Если сгенерированная краткая биография не соответствует ожидаемым характеристикам банкира.

    Example:
        >>> test_generate_person(setup)  # doctest: +SKIP
    """
```

**Назначение**: Тестирование генерации персонажа с использованием `TinyPersonFactory` и проверки соответствия его краткой биографии заданным требованиям.

**Параметры**:
- `setup`: Фикстура pytest, используемая для настройки тестовой среды.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если сгенерированная краткая биография не соответствует ожидаемым характеристикам банкира.

**Как работает функция**:

1. **Определение спецификации банкира**: Определяется строка `banker_spec`, содержащая описание банкира.
2. **Создание фабрики персонажей**: Создается экземпляр `TinyPersonFactory` с использованием спецификации банкира.
3. **Генерация персонажа**: Генерируется персонаж с помощью метода `generate_person` фабрики.
4. **Получение краткой биографии**: Получается краткая биография сгенерированного персонажа с помощью метода `minibio`.
5. **Проверка соответствия**: Проверяется, что краткая биография соответствует ожидаемым характеристикам банкира с использованием функции `proposition_holds`. Если проверка не проходит, вызывается исключение `AssertionError`.

**ASCII flowchart**:

```
A [Определение спецификации банкира]
│
B [Создание фабрики персонажей]
│
C [Генерация персонажа]
│
D [Получение краткой биографии]
│
E [Проверка соответствия]
```

**Примеры**:

```python
import pytest
from tinytroupe.examples import create_oscar_the_architect
from tinytroupe.control import Simulation
import tinytroupe.control as control
from tinytroupe.factory import TinyPersonFactory
from testing_utils import *

@pytest.fixture
def setup():
    # Здесь можно добавить код для настройки тестовой среды, если необходимо
    pass

def test_generate_person(setup):
    banker_spec = """
    A vice-president of one of the largest brazillian banks. Has a degree in engineering and an MBA in finance. 
    Is facing a lot of pressure from the board of directors to fight off the competition from the fintechs.    
    """
    banker_factory = TinyPersonFactory(banker_spec)
    banker = banker_factory.generate_person()
    minibio = banker.minibio()
    assert proposition_holds(f"The following is an acceptable short description for someone working in banking: '{minibio}'"), f"Proposition is false according to the LLM."