# Модуль `hypotez/src/suppliers/chat_gpt/gpt_traigner.py`

## Обзор

Данный модуль предоставляет классы и функции для обучения модели чат-бота GPT на основе данных из файлов диалогов. Он включает в себя обработку загруженных данных, определение эмоциональной окраски диалогов и сохранение результатов в различных форматах (JSONL, CSV, текстовый).

## Классы

### `GPT_Traigner`

**Описание**: Класс `GPT_Traigner` отвечает за обработку и сохранение данных диалогов чат-бота GPT.

**Атрибуты**:

* `driver`: Объект для управления веб-драйвером.

**Методы**:

#### `__init__(self)`

**Описание**: Инициализирует объект класса `GPT_Traigner`.

**Возвращает**:
  - `None`

#### `determine_sentiment(self, conversation_pair: dict[str, str], sentiment: str = 'positive') -> str`

**Описание**: Определяет эмоциональную окраску пары диалогов.

**Параметры**:
- `conversation_pair` (dict[str, str]): Пара диалогов в формате словарь.
- `sentiment` (str, optional): Начальное значение эмоциональной окраски. По умолчанию 'positive'.

**Возвращает**:
- str: Эмоциональная окраска ("positive" или "negative").

#### `save_conversations_to_jsonl(self, data: list[dict], output_file: str)`

**Описание**: Сохраняет пары диалогов в файл в формате JSONL.

**Параметры**:
- `data` (list[dict]): Список словарей, содержащих пары диалогов.
- `output_file` (str): Путь к файлу для сохранения данных.

**Возвращает**:
- `None`


#### `dump_downloaded_conversations(self)`

**Описание**: Загружает и обрабатывает файлы диалогов из указанного каталога, сохраняя результаты в формате CSV, JSONL и текстового файла.

**Возвращает**:
- `None`


## Функции

###  `j_dumps`

**Описание**:  Функция сериализует данные в JSON формат.

###  `j_loads`

**Описание**: Функция десериализует данные из JSON формата.

### `j_loads_ns`

**Описание**: Функция десериализует данные из JSON формата, обрабатывая ошибки.


### `clean_string`

**Описание**: Функция очищает строку.

### `dict2csv`

**Описание**: Функция преобразует словарь в CSV формат.

### `json2csv`

**Описание**: Функция преобразует JSON в CSV.

### `pprint`

**Описание**: Функция для красивой печати данных.



## Константы

### `MODE`

**Описание**: Переменная, хранящая режим работы (например, 'dev').


## Модули

### `header`

**Описание**: Модуль для работы с заголовками.

### `gs`

**Описание**: Модуль для работы с Google Storage.

### `logger`

**Описание**: Модуль для работы с логами.

### `GptGs`

**Описание**: Класс для работы с сервисом GPT.

### `Driver`

**Описание**: Класс для управления веб-драйвером.

### `Chrome`

**Описание**: Класс для управления веб-драйвером Chrome.

### `Firefox`

**Описание**: Класс для управления веб-драйвером Firefox.

### `Edge`

**Описание**: Класс для управления веб-драйвером Edge.


### `Model`

**Описание**: Класс для работы с моделью OpenAI.


### `Path`

**Описание**: Класс из модуля `pathlib` для работы с путями к файлам.

### `asyncio`

**Описание**: Модуль для асинхронного программирования.


### `re`

**Описание**: Модуль для работы с регулярными выражениями.


### `argparse`

**Описание**: Модуль для парсинга аргументов командной строки.

### `itertools`

**Описание**: Модуль для работы с итераторами.


### `pandas`

**Описание**: Библиотека для работы с данными.


### `aioconsole`

**Описание**: Библиотека для работы с асинхронным вводом.


### `Optional`

**Описание**: Тип данных, указывающий возможность наличия значения или `None`.