# Модуль `test_factory.py`

## Обзор

Этот модуль содержит тесты для класса `TinyPersonFactory` из модуля `tinytroupe.factory`.  Тесты проверяют генерацию персон с заданными характеристиками,  а также корректность сгенерированной мини-биографии.

## Импорты

```python
import pytest
import os
import sys
from tinytroupe.examples import create_oscar_the_architect
from tinytroupe.control import Simulation
import tinytroupe.control as control
from tinytroupe.factory import TinyPersonFactory
from testing_utils import *
```

## Функции

### `test_generate_person`

**Описание**: Функция тестирует генерацию персоны с помощью `TinyPersonFactory`.

**Параметры**:

- `setup`: Объект, предоставляющий необходимые данные для настройки теста (из модуля `testing_utils`).

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- Возможны исключения, связанные с ошибками `pytest` или проблемами в тестируемом коде.


**Детали**: Функция создает объект `TinyPersonFactory` с заданным описанием человека (`banker_spec`), генерирует персону (`banker`), получает её мини-биографию (`minibio`) и проверяет, является ли мини-биография приемлемым описанием банковского работника с помощью функции `proposition_holds` из модуля `testing_utils`.  Функция `proposition_holds` имитирует оценку качества генерации с использованием некоторого языка-модели.


```python
def test_generate_person(setup):
    banker_spec =\\\
    """
    A vice-president of one of the largest brazillian banks. Has a degree in engineering and an MBA in finance. 
    Is facing a lot of pressure from the board of directors to fight off the competition from the fintechs.    
    """

    banker_factory = TinyPersonFactory(banker_spec)

    banker = banker_factory.generate_person()

    minibio = banker.minibio()

    assert proposition_holds(f"The following is an acceptable short description for someone working in banking: \'{minibio}\'"), f"Proposition is false according to the LLM."
```