# Документация модуля `ask.py`

## Оглавление

1.  [Обзор](#обзор)
2.  [Классы](#классы)
    -   [`GoogleGenerativeAI`](#googlegenerativeai)
3.  [Функции](#функции)

## Обзор

Модуль `ask.py` предоставляет класс `GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI. Он позволяет отправлять текстовые запросы и получать ответы от выбранной модели.

## Классы

### `GoogleGenerativeAI`

**Описание**:
Класс для взаимодействия с моделями Google Generative AI.

**Методы**:
-   `__init__(self, api_key: str, system_instruction: str = '', model_name: str = 'gemini-2.0-flash-exp')`: Инициализирует экземпляр класса `GoogleGenerativeAI` с API ключом, системной инструкцией и названием модели.
-   `ask(self, q: str) -> str`: Отправляет текстовый запрос модели и возвращает ответ.

#### `__init__`

**Описание**:
Инициализация модели GoogleGenerativeAI.

**Параметры**:
-   `api_key` (str): Ключ API для доступа к Gemini.
-   `system_instruction` (str, optional): Инструкция для модели (системный промпт). По умолчанию ''.
-   `model_name` (str, optional): Название используемой модели Gemini. По умолчанию 'gemini-2.0-flash-exp'.

#### `ask`

**Описание**:
Отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:
-   `q` (str): Вопрос, который будет отправлен модели.

**Возвращает**:
-   `str`: Ответ от модели. В случае ошибки возвращает сообщение об ошибке.

## Функции

В данном файле функции отсутствуют.