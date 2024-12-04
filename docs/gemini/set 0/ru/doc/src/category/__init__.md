# Модуль hypotez/src/category/__init__.py

## Обзор

Данный модуль является начальной точкой доступа к модулю `category`. Он импортирует класс `Category` из подмодуля `category`.  Переменная `MODE` устанавливает режим работы, по умолчанию он равен 'dev'.

## Переменные

### `MODE`

**Описание**:  Переменная, определяющая режим работы модуля.

**Тип**: str

**Значение по умолчанию**: 'dev'


## Импорты

### `from .category import Category`

**Описание**: Импортирует класс `Category` из подмодуля `category`.

## Пример использования

```python
from hypotez.src.category import MODE
# ... далее использование MODE
```

```python
from hypotez.src.category import Category
# ... далее создание и использование экземпляра класса Category
```
```