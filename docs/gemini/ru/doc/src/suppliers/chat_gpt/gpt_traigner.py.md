# Модуль `gpt_traigner.py`

## Обзор

Модуль `gpt_traigner.py` предназначен для сбора и обработки данных диалогов из ChatGPT для дальнейшего обучения модели. Он включает в себя функционал для извлечения диалогов из HTML-файлов, сохранения их в различных форматах (JSONL, CSV, TXT), а также для взаимодействия с моделью обучения.

## Содержание

1.  [Классы](#классы)
    *   [GPT_Traigner](#gpt_traigner)
        *   [`__init__`](#__init__)
        *   [`determine_sentiment`](#determine_sentiment)
        *   [`save_conversations_to_jsonl`](#save_conversations_to_jsonl)
        *   [`dump_downloaded_conversations`](#dump_downloaded_conversations)

## Классы

### `GPT_Traigner`

**Описание**:
Класс `GPT_Traigner` управляет процессом сбора, обработки и сохранения диалогов, полученных из ChatGPT.

**Методы**:

#### `__init__`

**Описание**:
Инициализирует экземпляр класса `GPT_Traigner`, создает экземпляр `GptGs`.

**Параметры**:
- `None`

**Возвращает**:
- `None`

#### `determine_sentiment`

**Описание**:
Определяет тональность пары диалога (положительная или отрицательная).

**Параметры**:
- `conversation_pair` (dict[str, str]): Пара диалога, представленная в виде словаря.
- `sentiment` (str, optional): Задает тональность. По умолчанию `'positive'`.

**Возвращает**:
- `str`:  Возвращает строку `'positive'` или `'negative'` в зависимости от входного параметра.

#### `save_conversations_to_jsonl`

**Описание**:
Сохраняет данные диалогов в формате JSONL.

**Параметры**:
- `data` (list[dict]): Список словарей с данными диалогов.
- `output_file` (str): Путь к файлу, в который будут сохранены данные.

**Возвращает**:
- `None`

#### `dump_downloaded_conversations`

**Описание**:
Извлекает диалоги из HTML-файлов, загруженных со страницы ChatGPT, и сохраняет их в файлы JSONL, CSV, TXT.

**Параметры**:
- `None`

**Возвращает**:
- `None`