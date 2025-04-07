# Документация для модуля `gemini_simplechat`

## Обзор

Этот модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI (Gemini). Он позволяет отправлять текстовые запросы, вести диалоги, описывать изображения и загружать файлы, используя API Google Gemini. Модуль предназначен для упрощения интеграции с моделями Gemini и предоставляет удобные методы для выполнения различных задач.

## Подробнее

Модуль предназначен для работы с Google Gemini API, предоставляя класс `GoogleGenerativeAI`, который инкапсулирует взаимодействие с API. Он поддерживает различные модели Gemini, позволяет сохранять историю диалогов, работать с текстом, изображениями и файлами, а также обрабатывает ошибки с использованием механизма повторных попыток. Модуль также включает примеры использования, демонстрирующие, как загружать и читать изображения и файлы, а также как вести интерактивный чат. Веб-интерфейс, а также автоматический запуск и вызов из командной строки (только для Windows) делают модуль удобным для различных сценариев использования.

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с Google Gemini API. Предоставляет методы для отправки текстовых запросов, ведения диалогов, описания изображений и загрузки файлов.

**Принцип работы**:
Класс инициализируется с использованием API-ключа, имени модели и настроек генерации. Он использует библиотеку `google-generativeai` для взаимодействия с API Gemini. Методы класса позволяют выполнять различные операции, такие как отправка текстовых запросов, ведение диалогов с сохранением истории, описание изображений и загрузка файлов.

**Атрибуты**:

-   `api_key` (str): API-ключ Google Gemini.
-   `model_name` (str): Имя используемой модели Gemini. По умолчанию `"gemini-2.0-flash-exp"`.
-   `generation_config` (Dict): Настройки генерации. По умолчанию `None`.
-   `system_instruction` (Optional[str]): Системные инструкции для модели. По умолчанию `None`.

**Методы**:

-   `__init__(api_key: str, model_name: str = "gemini-2.0-flash-exp", generation_config: Dict = None, system_instruction: Optional[str] = None)`:
    -   Инициализирует объект `GoogleGenerativeAI` с API-ключом, именем модели и настройками генерации.
    -   Параметр `system_instruction` позволяет задать системные инструкции для модели.

-   `ask(q: str, attempts: int = 15) -> Optional[str]`:
    -   Отправляет текстовый запрос `q` к модели и возвращает ответ.
    -   `attempts` - количество попыток, если запрос не удался.

-   `chat(q: str) -> Optional[str]`:
    -   Отправляет запрос `q` в чат, поддерживая историю диалога.
    -   Возвращает ответ модели.
    -   История чата сохраняется в JSON файл.

-   `describe_image(image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = '') -> Optional[str]`:
    -   Описывает изображение, отправленное в виде пути к файлу или байтов.
    -   `image`: путь к файлу изображения или байты изображения.
    -   `mime_type`: mime-тип изображения.
    -   `prompt`: текстовый промпт для описания изображения.
    -   Возвращает текстовое описание изображения.

-   `upload_file(file: str | Path | IOBase, file_name: Optional[str] = None) -> bool`:
    -   Загружает файл в Gemini API.
    -   `file`: путь к файлу, имя файла или файловый объект.
    -   `file_name`: имя файла для Gemini API.

## Функции

### `__init__`

```python
def __init__(api_key: str, model_name: str = "gemini-2.0-flash-exp", generation_config: Dict = None, system_instruction: Optional[str] = None) -> None:
    """ Инициализирует объект `GoogleGenerativeAI` с API-ключом, именем модели и настройками генерации.
    Args:
        api_key (str): API-ключ Google Gemini.
        model_name (str, optional): Имя используемой модели Gemini. По умолчанию "gemini-2.0-flash-exp".
        generation_config (Dict, optional): Настройки генерации. По умолчанию None.
        system_instruction (Optional[str], optional): Системные инструкции для модели. По умолчанию None.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
```

**Назначение**: Инициализирует объект `GoogleGenerativeAI` с API-ключом, именем модели и настройками генерации.

**Параметры**:

-   `api_key` (str): API-ключ Google Gemini.
-   `model_name` (str, optional): Имя используемой модели Gemini. По умолчанию `"gemini-2.0-flash-exp"`.
-   `generation_config` (Dict, optional): Настройки генерации. По умолчанию `None`.
-   `system_instruction` (Optional[str], optional): Системные инструкции для модели. По умолчанию `None`.

**Возвращает**:

-   `None`

**Вызывает исключения**:

-   Не вызывает исключений.

**Как работает функция**:

1.  Функция инициализирует объект `GoogleGenerativeAI`, сохраняя переданные параметры в атрибуты класса.
2.  Создается клиент Gemini API с использованием API-ключа.
3.  Устанавливаются системные инструкции для модели, если они предоставлены.

```
A[Инициализация GoogleGenerativeAI]
|
B[Сохранение параметров в атрибуты класса]
|
C[Создание клиента Gemini API]
|
D[Установка системных инструкций (если есть)]
```

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI

# Пример инициализации с API-ключом и системными инструкциями
ai = GoogleGenerativeAI(api_key="YOUR_API_KEY", system_instruction="You are a helpful assistant.")

# Пример инициализации с API-ключом и именем модели
ai = GoogleGenerativeAI(api_key="YOUR_API_KEY", model_name="gemini-1.5-flash-8b")
```

### `ask`

```python
def ask(q: str, attempts: int = 15) -> Optional[str]:
    """ Отправляет текстовый запрос `q` к модели и возвращает ответ.
    Args:
        q (str): Текстовый запрос.
        attempts (int, optional): Количество попыток, если запрос не удался. По умолчанию 15.

    Returns:
        Optional[str]: Ответ модели или None в случае неудачи.

    Raises:
        Exception: Если не удается получить ответ после нескольких попыток.
    """
```

**Назначение**: Отправляет текстовый запрос к модели Gemini и возвращает ответ.

**Параметры**:

-   `q` (str): Текстовый запрос.
-   `attempts` (int, optional): Количество попыток, если запрос не удался. По умолчанию `15`.

**Возвращает**:

-   `Optional[str]`: Ответ модели или `None` в случае неудачи.

**Вызывает исключения**:

-   `Exception`: Если не удается получить ответ после нескольких попыток.

**Как работает функция**:

1.  Функция отправляет текстовый запрос `q` к модели Gemini.
2.  Если запрос не удался, функция повторяет попытки до `attempts` раз.
3.  В случае успеха функция возвращает ответ модели.
4.  В случае неудачи после нескольких попыток функция возвращает `None`.

```
A[Получение текстового запроса]
|
B[Отправка запроса к модели Gemini]
|
C[Проверка ответа]
|
D[Успех: Возврат ответа]
|
E[Неудача: Повтор попытки (до attempts раз)]
|
F[Неудача после attempts попыток: Возврат None]
```

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI

# Пример отправки текстового запроса
ai = GoogleGenerativeAI(api_key="YOUR_API_KEY")
response = ai.ask("What is the capital of France?")
if response:
    print(response)
else:
    print("Failed to get response.")
```

### `chat`

```python
def chat(q: str) -> Optional[str]:
    """ Отправляет запрос `q` в чат, поддерживая историю диалога.
    Args:
        q (str): Текстовый запрос.

    Returns:
        Optional[str]: Ответ модели или None в случае неудачи.

    Raises:
        Exception: Если не удается получить ответ.
    """
```

**Назначение**: Отправляет запрос в чат, поддерживая историю диалога.

**Параметры**:

-   `q` (str): Текстовый запрос.

**Возвращает**:

-   `Optional[str]`: Ответ модели или `None` в случае неудачи.

**Вызывает исключения**:

-   `Exception`: Если не удается получить ответ.

**Как работает функция**:

1.  Функция отправляет запрос `q` в чат, поддерживая историю диалога.
2.  История чата сохраняется в JSON файл.
3.  Функция возвращает ответ модели.

```
A[Получение текстового запроса]
|
B[Добавление запроса в историю чата]
|
C[Отправка запроса к модели Gemini]
|
D[Получение ответа]
|
E[Добавление ответа в историю чата]
|
F[Сохранение истории чата в JSON файл]
|
G[Возврат ответа]
```

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI

# Пример отправки запроса в чат
ai = GoogleGenerativeAI(api_key="YOUR_API_KEY")
response = ai.chat("Hello, Gemini!")
if response:
    print(response)
else:
    print("Failed to get response.")
```

### `describe_image`

```python
def describe_image(image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = '') -> Optional[str]:
    """ Описывает изображение, отправленное в виде пути к файлу или байтов.
    Args:
        image (Path | bytes): Путь к файлу изображения или байты изображения.
        mime_type (Optional[str], optional): mime-тип изображения. По умолчанию 'image/jpeg'.
        prompt (Optional[str], optional): Текстовый промпт для описания изображения. По умолчанию ''.

    Returns:
        Optional[str]: Текстовое описание изображения или None в случае неудачи.

    Raises:
        Exception: Если не удается получить описание изображения.
    """
```

**Назначение**: Описывает изображение, отправленное в виде пути к файлу или байтов.

**Параметры**:

-   `image` (Path | bytes): Путь к файлу изображения или байты изображения.
-   `mime_type` (Optional[str], optional): mime-тип изображения. По умолчанию `'image/jpeg'`.
-   `prompt` (Optional[str], optional): Текстовый промпт для описания изображения. По умолчанию `''`.

**Возвращает**:

-   `Optional[str]`: Текстовое описание изображения или `None` в случае неудачи.

**Вызывает исключения**:

-   `Exception`: Если не удается получить описание изображения.

**Как работает функция**:

1.  Функция получает изображение в виде пути к файлу или байтов.
2.  Если изображение передано в виде пути к файлу, функция считывает байты изображения из файла.
3.  Функция отправляет запрос к модели Gemini для описания изображения.
4.  Функция возвращает текстовое описание изображения.

```
A[Получение изображения (путь или байты)]
|
B[Чтение байтов изображения (если передан путь)]
|
C[Отправка запроса к модели Gemini для описания изображения]
|
D[Получение текстового описания изображения]
|
E[Возврат описания]
```

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI
from pathlib import Path

# Пример описания изображения по пути к файлу
ai = GoogleGenerativeAI(api_key="YOUR_API_KEY")
image_path = Path("image.jpg")
description = ai.describe_image(image_path, prompt="Describe this image in detail.")
if description:
    print(description)
else:
    print("Failed to get image description.")

# Пример описания изображения по байтам
with open("image.jpg", "rb") as f:
    image_bytes = f.read()
description = ai.describe_image(image_bytes, mime_type="image/jpeg", prompt="Describe this image.")
if description:
    print(description)
else:
    print("Failed to get image description.")
```

### `upload_file`

```python
def upload_file(file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
    """ Загружает файл в Gemini API.
    Args:
        file (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
        file_name (Optional[str], optional): Имя файла для Gemini API. По умолчанию None.

    Returns:
        bool: True в случае успеха, False в случае неудачи.

    Raises:
        Exception: Если не удается загрузить файл.
    """
```

**Назначение**: Загружает файл в Gemini API.

**Параметры**:

-   `file` (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
-   `file_name` (Optional[str], optional): Имя файла для Gemini API. По умолчанию `None`.

**Возвращает**:

-   `bool`: `True` в случае успеха, `False` в случае неудачи.

**Вызывает исключения**:

-   `Exception`: Если не удается загрузить файл.

**Как работает функция**:

1.  Функция получает файл в виде пути к файлу, имени файла или файлового объекта.
2.  Если файл передан в виде пути к файлу или имени файла, функция открывает файл и считывает его содержимое.
3.  Функция отправляет запрос к Gemini API для загрузки файла.
4.  Функция возвращает `True` в случае успеха и `False` в случае неудачи.

```
A[Получение файла (путь, имя или объект)]
|
B[Открытие и чтение файла (если передан путь или имя)]
|
C[Отправка запроса к Gemini API для загрузки файла]
|
D[Проверка результата]
|
E[Успех: Возврат True]
|
F[Неудача: Возврат False]
```

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI
from pathlib import Path

# Пример загрузки файла по пути
ai = GoogleGenerativeAI(api_key="YOUR_API_KEY")
file_path = Path("file.txt")
success = ai.upload_file(file_path, file_name="my_file.txt")
if success:
    print("File uploaded successfully.")
else:
    print("Failed to upload file.")

# Пример загрузки файла по файловому объекту
with open("file.txt", "rb") as f:
    success = ai.upload_file(f, file_name="my_file.txt")
if success:
    print("File uploaded successfully.")
else:
    print("Failed to upload file.")