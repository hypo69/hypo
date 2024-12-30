# Модуль `GoogleGenerativeAI`

## Обзор

Этот модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI, такими как Gemini. Он позволяет отправлять текстовые запросы к модели и получать ответы.

## Содержание

- [Классы](#classes)
  - [`GoogleGenerativeAI`](#googlegenerativeai)
- [Функции](#functions)
  - [`__init__`](#__init__)
  - [`ask`](#ask)

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI.

**Методы**:
- [`__init__`](#__init__): Инициализация модели.
- [`ask`](#ask): Отправляет запрос модели и возвращает ответ.

## Функции

### `__init__`

**Описание**: Инициализирует модель GoogleGenerativeAI.

```python
def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp")
```

**Параметры**:
- `api_key` (str): Ключ API для доступа к генеративной модели.
- `model_name` (str, optional): Название модели для использования. По умолчанию "gemini-2.0-flash-exp".

**Возвращает**:
- `None`

### `ask`

**Описание**: Отправляет текстовый запрос модели и возвращает ответ.

```python
def ask(self, q: str) -> str:
```

**Параметры**:
- `q` (str): Вопрос, который будет отправлен модели.

**Возвращает**:
- `str`: Ответ от модели.

**Raises**:
- `Exception`: Если произошла ошибка при взаимодействии с моделью.

**Пример обработки исключения:**

```python
try:
    response = self.model.generate_content(q)
    return response.text
except Exception as ex:
    return f"Error: {str(ex)}"
```