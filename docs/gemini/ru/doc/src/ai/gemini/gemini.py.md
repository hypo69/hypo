# Модуль для интеграции с Google Generative AI
=================================================

Модуль содержит класс :class:`GoogleGenerativeAI`, который используется для взаимодействия с различными AI-моделями
Google Gemini. Он позволяет отправлять текстовые запросы, описывать изображения и загружать файлы.

Пример использования
----------------------

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> response = ai.ask("What is the capital of France?")
>>> print(response)
Paris.
```

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [Config](#config)
    - [GoogleGenerativeAI](#googlegenerativeai)
        - [Атрибуты класса](#атрибуты-класса-googlegenerativeai)
        - [Методы класса](#методы-класса-googlegenerativeai)
            - [`__post_init__`](#__post_init__)
            - [`normalize_answer`](#normalize_answer)
            - [`_start_chat`](#_start_chat)
            - [`clear_history`](#clear_history)
            - [`_save_chat_history`](#_save_chat_history)
            - [`_load_chat_history`](#_load_chat_history)
            - [`chat`](#chat)
            - [`ask`](#ask)
            - [`ask_async`](#ask_async)
            - [`describe_image`](#describe_image)
            - [`upload_file`](#upload_file)
- [Функции](#функции)
    - [`main`](#main)

## Обзор

Этот модуль предоставляет интеграцию с Google Generative AI, позволяя использовать модели Gemini для различных задач, таких как ответы на вопросы, описание изображений и загрузка файлов. Он включает в себя класс `GoogleGenerativeAI`, который упрощает взаимодействие с API Google Gemini.

## Подробнее

Модуль предназначен для упрощения работы с Google Gemini API. Он предоставляет удобный интерфейс для отправки запросов к моделям Gemini, обработки ответов и управления историей чата. Модуль также включает функции для описания изображений и загрузки файлов. Расположение модуля в проекте: `src/ai/gemini/gemini.py`.

## Классы

### `Config`
Описание назначения класса
Inherits: 
           
Attributes:
           
Methods:
           

### `GoogleGenerativeAI`

**Описание**: Класс `GoogleGenerativeAI` предназначен для взаимодействия с моделями Google Generative AI.

**Принцип работы**:
Класс инициализируется с использованием API-ключа и имени модели. Он предоставляет методы для отправки текстовых запросов, асинхронной отправки текстовых запросов, описания изображений и загрузки файлов. Класс также управляет историей чата, сохраняя и загружая ее из файлов.

#### Атрибуты класса `GoogleGenerativeAI`

- `api_key` (str): API-ключ для доступа к Google Generative AI.
- `model_name` (str): Имя используемой модели Gemini (по умолчанию "gemini-2.0-flash-exp").
- `dialogue_txt_path` (Path): Путь к файлу для записи диалогов (инициализируется в `__post_init__`).
- `generation_config` (Dict): Конфигурация генерации ответов модели (по умолчанию `{"response_mime_type": "text/plain"}`).
- `system_instruction` (Optional[str]): Системные инструкции для модели (по умолчанию `None`).
- `history_dir` (Path): Путь к директории для хранения истории чата (инициализируется в `__post_init__`).
- `history_txt_file` (Path): Путь к файлу для сохранения истории чата в текстовом формате (инициализируется в `__post_init__`).
- `history_json_file` (Path): Путь к файлу для сохранения истории чата в формате JSON (инициализируется в `__post_init__`).
- `config` (SimpleNamespace): Конфигурация, загруженная из `gemini.json` (инициализируется в `__post_init__`).
- `chat_history` (List[Dict]): Список, хранящий историю чата (по умолчанию пустой список).
- `model` (Any): Объект модели Gemini (инициализируется в `__post_init__`).
- `_chat` (Any): Объект чата (инициализируется в `__post_init__`).
- `MODELS` (List[str]): Список доступных моделей Gemini.

#### Методы класса `GoogleGenerativeAI`

### `__post_init__`

```python
def __post_init__(self):
    """Инициализация модели GoogleGenerativeAI с дополнительными настройками."""
    ...
```

**Назначение**: Инициализация модели `GoogleGenerativeAI` с дополнительными настройками, такими как загрузка конфигурации, определение путей к файлам истории и инициализация модели Gemini.

**Как работает функция**:

1.  **Загрузка конфигурации**: Загружает конфигурацию из файла `gemini.json` с использованием функции `j_loads_ns`.
2.  **Определение путей к файлам истории**: Определяет пути к файлам для сохранения истории чата в текстовом и JSON форматах.
3.  **Инициализация модели**: Инициализирует модель Gemini с использованием API-ключа и конфигурации.
4.  **Запуск чата**: Запускает чат с начальной настройкой, используя метод `_start_chat`.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
```

### `normalize_answer`

```python
def normalize_answer(self, text:str) -> str:
    """Очистка вывода от 
    ```md, ```python, ```json, ```html, ит.п.
    """
    ...
```

**Назначение**: Очистка текстового вывода модели от нежелательных элементов, таких как markdown-разметка, код Python, JSON, HTML и т.п.

**Параметры**:
- `text` (str): Текст для очистки.

**Возвращает**:
- `str`: Очищенный текст.

**Как работает функция**:

1.  Вызывает функцию `normalize_answer` из модуля `src.utils.string.ai_string_normalizer`, чтобы удалить нежелательные элементы из текста.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
cleaned_text = ai.normalize_answer("```python\nprint('Hello')\n```")
print(cleaned_text)  # Hello
```

### `_start_chat`

```python
def _start_chat(self):
    """Запуск чата с начальной настройкой."""
    ...
```

**Назначение**: Запуск чата с начальной настройкой, включая системные инструкции, если они предоставлены.

**Возвращает**:
- `Any`: Объект чата.

**Как работает функция**:

1.  Проверяет, предоставлены ли системные инструкции.
2.  Если системные инструкции предоставлены, запускает чат с использованием этих инструкций.
3.  Если системные инструкции не предоставлены, запускает чат без начальной истории.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY', system_instruction="You are a helpful assistant.")
chat = ai._start_chat()
```

### `clear_history`

```python
def clear_history(self):
    """
    Очищает историю чата в памяти и удаляет файл истории, если он существует.
    """
    ...
```

**Назначение**: Очищает историю чата в памяти и удаляет файл истории, если он существует.

**Как работает функция**:

1.  Очищает список `chat_history`, хранящий историю чата в памяти.
2.  Проверяет, существует ли файл истории (`history_json_file`).
3.  Если файл существует, удаляет его и логирует информацию об удалении.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
ai.clear_history()
```

### `_save_chat_history`

```python
async def _save_chat_history(self, chat_data_folder: Optional[str | Path]):
    """Сохраняет всю историю чата в JSON файл"""
    ...
```

**Назначение**: Сохраняет историю чата в JSON файл.

**Параметры**:
- `chat_data_folder` (Optional[str | Path]): Папка для сохранения файла истории.

**Как работает функция**:

1.  Определяет путь к файлу истории (`history_json_file`) на основе предоставленной папки.
2.  Сохраняет историю чата в JSON файл с использованием функции `j_dumps`.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
await ai._save_chat_history('chat_history')
```

### `_load_chat_history`

```python
async def _load_chat_history(self, chat_data_folder: Optional[str | Path]):
    """Загружает историю чата из JSON файла"""
    ...
```

**Назначение**: Загружает историю чата из JSON файла.

**Параметры**:
- `chat_data_folder` (Optional[str | Path]): Папка, содержащая файл истории.

**Как работает функция**:

1.  Определяет путь к файлу истории (`history_json_file`) на основе предоставленной папки.
2.  Проверяет, существует ли файл истории.
3.  Если файл существует, загружает историю чата из файла с использованием функции `j_loads`.
4.  Восстанавливает историю чата в объекте чата (`_chat`).

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
await ai._load_chat_history('chat_history')
```

### `chat`

```python
async def chat(self, q: str, chat_data_folder: Optional[str | Path], flag: str = "save_chat") -> Optional[str]:
    """
    Обрабатывает чат-запрос с различными режимами управления историей чата.

    Args:
        q (str): Вопрос пользователя.
        chat_data_folder (Optional[str | Path]): Папка для хранения истории чата.
        flag (str): Режим управления историей. Возможные значения: 
                    "save_chat", "read_and_clear", "clear", "start_new".

    Returns:
        Optional[str]: Ответ модели.
    """
    ...
```

**Назначение**: Обрабатывает чат-запрос с различными режимами управления историей чата.

**Параметры**:

*   `q` (str): Вопрос пользователя.
*   `chat_data_folder` (Optional\[str | Path]): Папка для хранения истории чата.
*   `flag` (str): Режим управления историей. Возможные значения: "save\_chat", "read\_and\_clear", "clear", "start\_new".

**Возвращает**:

*   `Optional[str]`: Ответ модели.

**Как работает функция**:

1.  В зависимости от флага выполняет различные действия с историей чата:
    *   "save\_chat": Загружает историю чата из файла.
    *   "read\_and\_clear": Загружает историю чата из файла и очищает ее.
    *   "read\_and\_start\_new": Загружает историю чата, сохраняет и начинает новую историю.
    *   "clear": Очищает историю чата.
    *   "start\_new": Сохраняет текущую историю в архив и начинает новую историю.
2.  Отправляет запрос модели.
3.  Сохраняет запрос и ответ в истории чата.
4.  Сохраняет историю чата в файл.
5.  Возвращает ответ модели.

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
response = await ai.chat("What is the capital of France?", 'chat_history')
print(response)
```

### `ask`

```python
def ask(self, q: str, attempts: int = 15, save_history:bool = False, clean_response:bool = True) -> Optional[str]:
    """
    Метод отправляет текстовый запрос модели и возвращает ответ.
    """
    ...
```

**Назначение**: Отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:

*   `q` (str): Вопрос пользователя.
*   `attempts` (int): Количество попыток отправки запроса (по умолчанию 15).
*   `save_history` (bool): Флаг, указывающий, нужно ли сохранять историю диалога (по умолчанию `False`).
*   `clean_response` (bool): Флаг, указывающий, нужно ли очищать ответ от нежелательных элементов (по умолчанию `True`).

**Возвращает**:

*   `Optional[str]`: Ответ модели.

**Как работает функция**:

1.  Выполняет несколько попыток отправки запроса модели.
2.  В случае ошибки повторяет попытку после некоторой задержки.
3.  Если получен ответ, сохраняет историю диалога (если `save_history` is `True`).
4.  Очищает ответ от нежелательных элементов (если `clean_response` is `True`).
5.  Возвращает ответ модели.

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
response = ai.ask("What is the capital of France?")
print(response)
```

### `ask_async`

```python
async def ask_async(self, q: str, attempts: int = 15, save_history: bool = False, clean_response:bool = True) -> Optional[str]:
    """
    Метод асинхронно отправляет текстовый запрос модели и возвращает ответ.
    """
    ...
```

**Назначение**: Асинхронно отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:

*   `q` (str): Вопрос пользователя.
*   `attempts` (int): Количество попыток отправки запроса (по умолчанию 15).
*   `save_history` (bool): Флаг, указывающий, нужно ли сохранять историю диалога (по умолчанию `False`).
*   `clean_response` (bool): Флаг, указывающий, нужно ли очищать ответ от нежелательных элементов (по умолчанию `True`).

**Возвращает**:

*   `Optional[str]`: Ответ модели.

**Как работает функция**:

1.  Выполняет несколько попыток отправки запроса модели асинхронно.
2.  В случае ошибки повторяет попытку после некоторой задержки.
3.  Если получен ответ, сохраняет историю диалога (если `save_history` is `True`).
4.  Очищает ответ от нежелательных элементов (если `clean_response` is `True`).
5.  Возвращает ответ модели.

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
response = await ai.ask_async("What is the capital of France?")
print(response)
```

### `describe_image`

```python
def describe_image(
    self, image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = ''
) -> Optional[str]:
    """
    Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

    Args:
        image: Путь к файлу изображения или байты изображения

    Returns:
        str: Текстовое описание изображения.
        None: Если произошла ошибка.
    """
    ...
```

**Назначение**: Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

**Параметры**:

*   `image` (Path | bytes): Путь к файлу изображения или байты изображения.
*   `mime_type` (Optional[str]): MIME-тип изображения (по умолчанию 'image/jpeg').
*   `prompt` (Optional[str]): Дополнительный промпт для модели (по умолчанию '').

**Возвращает**:

*   `Optional[str]`: Текстовое описание изображения.

**Как работает функция**:

1.  Подготавливает контент для запроса, преобразуя изображение в байты, если это необходимо.
2.  Отправляет запрос модели.
3.  Возвращает текстовое описание изображения.

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
description = ai.describe_image('image.jpg', prompt="Describe this image in detail.")
print(description)
```

### `upload_file`

```python
async def upload_file(
    self, file: str | Path | IOBase, file_name: Optional[str] = None
) -> bool:
    """
    https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md
    response (file_types.File)
    """
    ...
```

**Назначение**: Загружает файл в Google Generative AI.

**Параметры**:

*   `file` (str | Path | IOBase): Путь к файлу, который нужно загрузить.
*   `file_name` (Optional[str]): Имя файла (по умолчанию `None`).

**Возвращает**:

*   `bool`: `True`, если файл успешно загружен.

**Как работает функция**:

1.  Загружает файл с использованием асинхронной функции `genai.upload_file_async`.
2.  В случае ошибки пытается удалить файл и загрузить его снова.

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
file_upload = await ai.upload_file('test.txt', 'test_file.txt')
print(file_upload)
```

## Функции

### `main`

```python
async def main():
    # Замените на свой ключ API

    system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
    ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

    # Пример вызова describe_image с промптом
    image_path = Path(r"test.jpg")  # Замените на путь к вашему изображению

    if not image_path.is_file():
        print(
            f"Файл {image_path} не существует. Поместите в корневую папку с программой файл с названием test.jpg"
        )
    else:
        prompt = """Проанализируй это изображение. Выдай ответ в формате JSON,
        где ключом будет имя объекта, а значением его описание.
         Если есть люди, опиши их действия."""

        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print("Описание изображения (с JSON форматом):")
            print(description)
            try:
                parsed_description = j_loads(description)

            except Exception as ex:
                print("Не удалось распарсить JSON. Получен текст:")
                print(description)

        else:
            print("Не удалось получить описание изображения.")

        # Пример без JSON вывода
        prompt = "Проанализируй это изображение. Перечисли все объекты, которые ты можешь распознать."
        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print("Описание изображения (без JSON формата):")
            print(description)

    file_path = Path('test.txt')
    with open(file_path, "w") as f:
        f.write("Hello, Gemini!")

    file_upload = await ai.upload_file(file_path, 'test_file.txt')
    print(file_upload)

    # Пример чата
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            break
        ai_message = await ai.chat(user_message)
        if ai_message:
            print(f"Gemini: {ai_message}")
        else:
            print("Gemini: Ошибка получения ответа")


if __name__ == "__main__":
    asyncio.run(main())
```

**Назначение**: Функция `main` является точкой входа в программу и демонстрирует примеры использования класса `GoogleGenerativeAI`.

**Как работает функция**:

1.  **Инициализация `GoogleGenerativeAI`**: Создает экземпляр класса `GoogleGenerativeAI` с API-ключом и системными инструкциями.
2.  **Пример вызова `describe_image`**: Демонстрирует использование метода `describe_image` для получения описания изображения.
3.  **Создание и загрузка файла**: Создает текстовый файл и загружает его с использованием метода `upload_file`.
4.  **Пример чата**: Запускает цикл чата, в котором пользователь может вводить сообщения, а программа будет отправлять их в Google Gemini и выводить ответы.

**ASCII Flowchart**:

```
A[Инициализация GoogleGenerativeAI]
|
B[Проверка наличия файла test.jpg]
|
C[Вызов describe_image с JSON форматом]
|
D[Вывод описания изображения (с JSON форматом)]
|
E[Вызов describe_image без JSON формата]
|
F[Вывод описания изображения (без JSON формата)]
|
G[Создание файла test.txt]
|
H[Вызов upload_file для test.txt]
|
I[Запуск цикла чата с пользователем]
```

**Примеры**:

Чтобы запустить этот пример, необходимо указать действительный API-ключ Google Gemini и поместить файл `test.jpg` в корневую папку с программой.
```python
if __name__ == "__main__":
    asyncio.run(main())