# Модуль для интеграции с Google Gemini AI
=================================================

Модуль содержит класс :class:`GoogleGenerativeAI`, который используется для взаимодействия с различными AI-моделями Google Gemini. Он позволяет отправлять текстовые запросы, описывать изображения и управлять историей чата.

Пример использования
----------------------

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> response = ai.ask("What is the capital of France?")
>>> print(response)
Paris
```

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [Config](#config)
    - [GoogleGenerativeAI](#googlegenerativeai)
- [Функции](#функции)
    - [main](#main)

## Обзор

Этот модуль предназначен для интеграции с моделями Google Generative AI. Он предоставляет класс `GoogleGenerativeAI`, который упрощает взаимодействие с API Gemini, позволяя отправлять запросы, описывать изображения и управлять историей чата.

## Подробнее

Модуль использует библиотеку `google.generativeai` для взаимодействия с API Gemini. Он включает обработку ошибок, асинхронные вызовы и возможность сохранения и загрузки истории чата. Класс `GoogleGenerativeAI` инициализируется с API-ключом и предоставляет методы для отправки текстовых запросов (`ask`, `ask_async`), описания изображений (`describe_image`) и управления историей чата (`chat`, `clear_history`, `_save_chat_history`, `_load_chat_history`).

## Классы

### `Config`

Описание назначения класса
    **Наследует**
        Если класс наследует другой - дай описание наследования

     **Аттрибуты**:
        param1 (str): Описание параметров (атрибуты) класса

     **Методы**:
        function_1(): Описание назаначения функций/методов класса

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI.

**Принцип работы**:
Класс `GoogleGenerativeAI` предназначен для упрощения взаимодействия с API Google Gemini. Он инициализируется с API-ключом и предоставляет методы для отправки запросов, описания изображений и управления историей чата.

**Атрибуты**:

- `api_key` (str): API-ключ для доступа к сервисам Google Generative AI.
- `model_name` (str): Имя используемой модели Gemini. По умолчанию `"gemini-2.0-flash-exp"`.
- `dialogue_txt_path` (Path): Путь к файлу для записи диалогов.
- `generation_config` (Dict): Конфигурация генерации ответов.
- `system_instruction` (Optional[str]): Системные инструкции для модели.
- `history_dir` (Path): Путь к директории для хранения истории чата.
- `history_txt_file` (Path): Путь к файлу для хранения истории чата в текстовом формате.
- `history_json_file` (Path): Путь к файлу для хранения истории чата в формате JSON.
- `config` (SimpleNamespace): Объект с конфигурацией из файла `gemini.json`.
- `chat_history` (List[Dict]): Список словарей, содержащих историю чата.
- `model` (Any): Объект модели Gemini.
- `_chat` (Any): Объект чата.
- `MODELS` (List[str]): Список поддерживаемых моделей Gemini.

**Методы**:

- `__post_init__`: Инициализация модели GoogleGenerativeAI с дополнительными настройками.
- `normalize_answer`: Очистка вывода от Markdown, Python, JSON и HTML-тегов.
- `_start_chat`: Запуск чата с начальной настройкой.
- `clear_history`: Очищает историю чата в памяти и удаляет файл истории, если он существует.
- `_save_chat_history`: Сохраняет всю историю чата в JSON файл.
- `_load_chat_history`: Загружает историю чата из JSON файла.
- `chat`: Обрабатывает чат-запрос с различными режимами управления историей чата.
- `ask`: Отправляет текстовый запрос модели и возвращает ответ.
- `ask_async`: Асинхронно отправляет текстовый запрос модели и возвращает ответ.
- `describe_image`: Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.
- `upload_file`: Загружает файл в Google Generative AI.

#### `__post_init__`

```python
    def __post_init__(self):\n        """Инициализация модели GoogleGenerativeAI с дополнительными настройками."""
```

**Назначение**: Инициализация модели `GoogleGenerativeAI` с дополнительными настройками.

**Как работает функция**:
1. **Загрузка конфигурации**: Загружает конфигурацию из файла `gemini.json` с использованием функции `j_loads_ns`.
2. **Определение путей к файлам**: Определяет пути к файлам для логирования диалогов и хранения истории чата.
3. **Инициализация модели**: Инициализирует модель Gemini с использованием API-ключа, имени модели и системных инструкций.
4. **Запуск чата**: Запускает чат с использованием метода `_start_chat`.

#### `normalize_answer`

```python
    def normalize_answer(self, text:str) -> str:\n        """Очистка вывода от \n        ```md, ```python, ```json, ```html, ит.п.\n        """
```

**Назначение**: Очистка вывода от Markdown, Python, JSON, HTML и других тегов.

**Параметры**:
- `text` (str): Текст для очистки.

**Возвращает**:
- `str`: Очищенный текст.

**Как работает функция**:

1. Функция вызывает `normalize_answer` из модуля `src.utils.string.ai_string_normalizer` для удаления нежелательных тегов и форматирования из текста.

ASCII flowchart:

```
    Текст для очистки
    ↓
    normalize_answer(text)  # Удаление тегов
    ↓
    Очищенный текст
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> text = "```python\nprint('Hello')\n```"
>>> ai.normalize_answer(text)
"print('Hello')"
```

#### `_start_chat`

```python
    def _start_chat(self):\n        """Запуск чата с начальной настройкой."""
```

**Назначение**: Запуск чата с начальной настройкой.

**Возвращает**:
- `Any`: Объект чата.

**Как работает функция**:
1. **Проверка системных инструкций**: Если системные инструкции заданы, чат запускается с этими инструкциями.
2. **Запуск чата без инструкций**: Если системные инструкции не заданы, чат запускается без них.

ASCII flowchart:

```
    Проверка system_instruction
    ↓
    Есть system_instruction?
    ├──-> Да: model.start_chat(history=[{"role": "user", "parts": [self.system_instruction]}])
    └──-> Нет: model.start_chat(history=[])
    ↓
    Объект чата
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY', system_instruction="Ты - полезный ассистент.")
>>> chat = ai._start_chat()
```

#### `clear_history`

```python
    def clear_history(self):\n        """\n        Очищает историю чата в памяти и удаляет файл истории, если он существует.\n        """
```

**Назначение**: Очищает историю чата в памяти и удаляет файл истории, если он существует.

**Как работает функция**:
1. **Очистка истории в памяти**: Очищает список `chat_history`.
2. **Удаление файла истории**: Если файл истории существует, он удаляется.

ASCII flowchart:

```
    Очистка истории чата
    ↓
    chat_history = []
    ↓
    Файл истории существует?
    ├──-> Да: history_json_file.unlink()
    └──-> Нет: Конец
    ↓
    Конец
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> ai.clear_history()
```

#### `_save_chat_history`

```python
    async def _save_chat_history(self, chat_data_folder: Optional[str | Path]):\n        """Сохраняет всю историю чата в JSON файл"""
```

**Назначение**: Сохраняет всю историю чата в JSON файл.

**Параметры**:
- `chat_data_folder` (Optional[str | Path]): Папка для хранения истории чата.

**Как работает функция**:
1. **Определение пути к файлу**: Если указана папка, путь к файлу истории устанавливается в `history.json` в указанной папке.
2. **Сохранение истории**: Если история чата не пуста, она сохраняется в JSON файл с использованием функции `j_dumps`.

ASCII flowchart:

```
    Сохранение истории чата
    ↓
    chat_data_folder указана?
    ├──-> Да: history_json_file = Path(chat_data_folder, 'history.json')
    └──-> Нет: Использовать существующий history_json_file
    ↓
    chat_history не пуста?
    ├──-> Да: j_dumps(data=self.chat_history, file_path=self.history_json_file, mode="w")
    └──-> Нет: Конец
    ↓
    Конец
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> await ai._save_chat_history('chat_history')
```

#### `_load_chat_history`

```python
    async def _load_chat_history(self, chat_data_folder: Optional[str | Path]):\n        """Загружает историю чата из JSON файла"""
```

**Назначение**: Загружает историю чата из JSON файла.

**Параметры**:
- `chat_data_folder` (Optional[str | Path]): Папка, содержащая файл истории чата.

**Как работает функция**:
1. **Определение пути к файлу**: Если указана папка, путь к файлу истории устанавливается в `history.json` в указанной папке.
2. **Загрузка истории**: Если файл истории существует, он загружается с использованием функции `j_loads`.
3. **Восстановление чата**: История чата добавляется в текущий чат.

ASCII flowchart:

```
    Загрузка истории чата
    ↓
    chat_data_folder указана?
    ├──-> Да: history_json_file = Path(chat_data_folder, 'history.json')
    └──-> Нет: Использовать существующий history_json_file
    ↓
    Файл истории существует?
    ├──-> Да: history_json_file = j_loads(self.history_json_file)
    │       _chat = self._start_chat()
    │       Добавить все entry в _chat.history
    └──-> Нет: Конец
    ↓
    Конец
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> await ai._load_chat_history('chat_history')
```

#### `chat`

```python
    async def chat(self, q: str, chat_data_folder: Optional[str | Path], flag: str = "save_chat") -> Optional[str]:\n        """\n        Обрабатывает чат-запрос с различными режимами управления историей чата.\n\n        Args:\n            q (str): Вопрос пользователя.\n            chat_data_folder (Optional[str | Path]): Папка для хранения истории чата.\n            flag (str): Режим управления историей. Возможные значения: \n                        "save_chat", "read_and_clear", "clear", "start_new".\n\n        Returns:\n            Optional[str]: Ответ модели.\n        """
```

**Назначение**: Обрабатывает чат-запрос с различными режимами управления историей чата.

**Параметры**:
- `q` (str): Вопрос пользователя.
- `chat_data_folder` (Optional[str | Path]): Папка для хранения истории чата.
- `flag` (str): Режим управления историей. Возможные значения: `"save_chat"`, `"read_and_clear"`, `"clear"`, `"start_new"`.

**Возвращает**:
- `Optional[str]`: Ответ модели.

**Как работает функция**:
1. **Обработка флагов**: В зависимости от флага, история чата загружается, очищается или начинается новая история.
2. **Отправка запроса модели**: Запрос отправляется модели с использованием метода `_chat.send_message_async`.
3. **Сохранение истории**: Ответ модели добавляется в историю чата и сохраняется в файл.

ASCII flowchart:

```
    Обработка чат-запроса
    ↓
    Обработка flag
    ├──-> "save_chat": Загрузить историю
    ├──-> "read_and_clear": Загрузить историю и очистить
    ├──-> "read_and_start_new": Загрузить историю, сохранить и очистить
    ├──-> "clear": Очистить историю
    └──-> "start_new": Сохранить текущую историю и начать новую
    ↓
    Отправить запрос модели _chat.send_message_async(q)
    ↓
    Добавить запрос и ответ в chat_history
    ↓
    Сохранить историю
    ↓
    Возвращает ответ
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> response = await ai.chat("What is the capital of France?", 'chat_history', 'save_chat')
>>> print(response)
Paris
```

#### `ask`

```python
    def ask(self, q: str, attempts: int = 15, save_history:bool = False, clean_response:bool = True) -> Optional[str]:\n        """\n        Метод отправляет текстовый запрос модели и возвращает ответ.\n        """
```

**Назначение**: Отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:
- `q` (str): Вопрос пользователя.
- `attempts` (int): Количество попыток отправки запроса. По умолчанию 15.
- `save_history` (bool): Флаг сохранения истории диалога. По умолчанию `False`.
- `clean_response` (bool): Флаг очистки ответа от лишних тегов. По умолчанию `True`.

**Возвращает**:
- `Optional[str]`: Ответ модели.

**Как работает функция**:
1. **Повторные попытки**: В цикле предпринимаются попытки отправки запроса модели.
2. **Обработка ошибок**: Обрабатываются различные типы ошибок, такие как сетевые ошибки, ошибки аутентификации и ошибки API.
3. **Сохранение истории**: Если флаг `save_history` установлен, история диалога сохраняется.
4. **Очистка ответа**: Если флаг `clean_response` установлен, ответ очищается от лишних тегов.

ASCII flowchart:

```
    Отправка текстового запроса
    ↓
    Цикл attempts
    ├──-> Отправить запрос model.generate_content(q)
    │       Успешно?
    │       ├──-> Да: Вернуть ответ
    │       └──-> Нет: Обработать ошибку
    └──-> Обработка ошибок
    │       ├──-> requests.exceptions.RequestException: Сетевая ошибка
    │       ├──-> (GatewayTimeout, ServiceUnavailable): Сервис недоступен
    │       ├──-> ResourceExhausted: Превышена квота
    │       ├──-> (DefaultCredentialsError, RefreshError): Ошибка аутентификации
    │       ├──-> (ValueError, TypeError): Некорректный ввод
    │       ├──-> (InvalidArgument, RpcError): Ошибка API
    │       └──-> Exception: Неизвестная ошибка
    ↓
    Вернуть None
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> response = ai.ask("What is the capital of France?")
>>> print(response)
Paris
```

#### `ask_async`

```python
    async def ask_async(self, q: str, attempts: int = 15, save_history: bool = False, clean_response:bool = True) -> Optional[str]:\n        """\n        Метод асинхронно отправляет текстовый запрос модели и возвращает ответ.\n        """
```

**Назначение**: Асинхронно отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:
- `q` (str): Вопрос пользователя.
- `attempts` (int): Количество попыток отправки запроса. По умолчанию 15.
- `save_history` (bool): Флаг сохранения истории диалога. По умолчанию `False`.
- `clean_response` (bool): Флаг очистки ответа от лишних тегов. По умолчанию `True`.

**Возвращает**:
- `Optional[str]`: Ответ модели.

**Как работает функция**:
1. **Асинхронные повторные попытки**: В цикле предпринимаются асинхронные попытки отправки запроса модели.
2. **Асинхронная обработка ошибок**: Обрабатываются различные типы ошибок, такие как сетевые ошибки, ошибки аутентификации и ошибки API.
3. **Сохранение истории**: Если флаг `save_history` установлен, история диалога сохраняется.
4. **Очистка ответа**: Если флаг `clean_response` установлен, ответ очищается от лишних тегов.

ASCII flowchart:

```
    Асинхронная отправка текстового запроса
    ↓
    Цикл attempts
    ├──-> Отправить запрос asyncio.to_thread(self.model.generate_content, q)
    │       Успешно?
    │       ├──-> Да: Вернуть ответ
    │       └──-> Нет: Обработать ошибку
    └──-> Обработка ошибок
    │       ├──-> requests.exceptions.RequestException: Сетевая ошибка
    │       ├──-> (GatewayTimeout, ServiceUnavailable): Сервис недоступен
    │       ├──-> ResourceExhausted: Превышена квота
    │       ├──-> (DefaultCredentialsError, RefreshError): Ошибка аутентификации
    │       ├──-> (ValueError, TypeError): Некорректный ввод
    │       ├──-> (InvalidArgument, RpcError): Ошибка API
    │       └──-> Exception: Неизвестная ошибка
    ↓
    Вернуть None
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> response = await ai.ask_async("What is the capital of France?")
>>> print(response)
Paris
```

#### `describe_image`

```python
    def describe_image(\n        self, image: Path | bytes, mime_type: Optional[str] = \'image/jpeg\', prompt: Optional[str] = \'\'\n    ) -> Optional[str]:\n        """\n        Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.\n\n        Args:\n            image: Путь к файлу изображения или байты изображения\n\n        Returns:\n            str: Текстовое описание изображения.\n            None: Если произошла ошибка.\n        """
```

**Назначение**: Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

**Параметры**:
- `image` (Path | bytes): Путь к файлу изображения или байты изображения.
- `mime_type` (Optional[str]): MIME-тип изображения. По умолчанию `'image/jpeg'`.
- `prompt` (Optional[str]): Текстовый запрос для описания изображения. По умолчанию `''`.

**Возвращает**:
- `Optional[str]`: Текстовое описание изображения.

**Как работает функция**:
1. **Подготовка контента**: Преобразует изображение в байты, если передан путь к файлу.
2. **Отправка запроса**: Отправляет запрос в Gemini Pro Vision с изображением и текстовым запросом.
3. **Обработка ошибок**: Обрабатывает различные типы ошибок, такие как ошибки аутентификации и ошибки API.
4. **Возврат описания**: Возвращает текстовое описание изображения.

ASCII flowchart:

```
    Описание изображения
    ↓
    Преобразование изображения в байты (если необходимо)
    ↓
    Подготовка контента для запроса
    ↓
    Отправка запроса model.generate_content()
    ↓
    Обработка ошибок
    │   ├──-> DefaultCredentialsError: Ошибка аутентификации
    │   ├──-> (InvalidArgument, RpcError): Ошибка API
    │   ├──-> RetryError: Модель перегружена
    │   └──-> Exception: Общая ошибка
    ↓
    Возврат описания
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> image_path = Path('test.jpg')
>>> description = ai.describe_image(image_path, prompt="Describe this image.")
>>> print(description)
A picture of a cat.
```

#### `upload_file`

```python
    async def upload_file(\n        self, file: str | Path | IOBase, file_name: Optional[str] = None\n    ) -> bool:\n        """\n        https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md\n        response (file_types.File)\n        """
```

**Назначение**: Загружает файл в Google Generative AI.

**Параметры**:
- `file` (str | Path | IOBase): Путь к файлу, файл или файловый объект для загрузки.
- `file_name` (Optional[str]): Имя файла.

**Возвращает**:
- `bool`: `True`, если файл успешно загружен, `False` в противном случае.

**Как работает функция**:
1. **Загрузка файла**: Асинхронно загружает файл с использованием `genai.upload_file_async`.
2. **Обработка ошибок**: Обрабатывает ошибки при загрузке файла и пытается удалить файл в случае ошибки.

ASCII flowchart:

```
    Загрузка файла
    ↓
    Попытка загрузки файла genai.upload_file_async()
    ↓
    Успешно?
    ├──-> Да: Возвращает True
    └──-> Нет: Обработка ошибок
    │       Попытка удаления файла genai.delete_file_async()
    │       Повторная загрузка файла
    ↓
    Возвращает None
```

**Примеры**:

```python
>>> ai = GoogleGenerativeAI(api_key='YOUR_API_KEY')
>>> file_path = Path('test.txt')
>>> with open(file_path, 'w') as f:
>>>     f.write('Hello, Gemini!')
>>> await ai.upload_file(file_path, 'test_file.txt')
True
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
```

**Назначение**: Главная функция для демонстрации работы с Google Gemini AI.

**Как работает функция**:
1. **Инициализация**: Инициализирует класс `GoogleGenerativeAI` с API-ключом и системными инструкциями.
2. **Описание изображения**: Демонстрирует использование метода `describe_image` для получения описания изображения в формате JSON и без него.
3. **Загрузка файла**: Демонстрирует использование метода `upload_file` для загрузки файла.
4. **Чат**: Демонстрирует использование метода `chat` для взаимодействия с моделью в режиме чата.

ASCII flowchart:

```
    Главная функция
    ↓
    Инициализация GoogleGenerativeAI
    ↓
    Описание изображения
    ├──-> Проверка наличия файла test.jpg
    │       ├──-> Описание изображения с JSON форматом
    │       └──-> Описание изображения без JSON формата
    ↓
    Загрузка файла
    ↓
    Чат
    ├──-> Ввод сообщения пользователя
    │       ├──-> Выход из чата (exit)
    │       └──-> Получение ответа от Gemini
    ↓
    Конец
```

**Примеры**:

```python
>>> asyncio.run(main())