# Документация для модуля `gemini-simplechat`

## Обзор

Этот документ описывает модуль `Google Gemini API Интеграция`, предназначенный для взаимодействия с моделями Google Generative AI (Gemini). Модуль предоставляет класс `GoogleGenerativeAI` для отправки текстовых запросов, ведения диалогов, описания изображений и загрузки файлов, используя API Google Gemini.

## Подробнее

Модуль поддерживает различные модели Gemini, сохраняет историю диалогов в JSON и текстовые файлы, работает с текстом, изображениями и файлами. Он также включает обработку ошибок с механизмом повторных попыток и возможность настраивать параметры генерации и системные инструкции. В `main()` представлен пример использования с загрузкой и чтением изображений и файлов, а также с интерактивным чатом. Также реализован веб-интерфейс для взаимодействия с чат-ботом, автоматический запуск приложения при старте системы и возможность вызова из командной строки (только для Windows).

## Установка

Для установки модуля необходимо выполнить следующие шаги:

1.  Клонировать репозиторий:
    ```bash
    git clone https://github.com/hypo69/gemini-simplechat-ru.git
    cd gemini-simplechat-ru
    ```

2.  Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3.  Создать или настроить файл конфигурации `config.json` и поместить в него необходимые настройки, включая API ключ Google Gemini.

4.  Использовать скрипт `install.ps1` для установки (только для Windows) для автоматической установки проекта и настройки автозапуска приложения.

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI (Gemini).

**Принцип работы**:
Класс инициализируется с API-ключом, именем модели и настройками генерации. Он предоставляет методы для отправки текстовых запросов, ведения диалогов, описания изображений и загрузки файлов. История диалогов сохраняется в JSON и текстовые файлы. Класс обрабатывает ошибки с механизмом повторных попыток.

**Аттрибуты**:
-   `api_key` (str): API-ключ Google Gemini.
-   `model_name` (str): Имя используемой модели Gemini.
-   `generation_config` (Dict): Настройки генерации текста.
-   `system_instruction` (Optional[str]): Системные инструкции для модели.

**Методы**:
-   `__init__`: Инициализирует объект `GoogleGenerativeAI`.
-   `ask`: Отправляет текстовый запрос к модели и возвращает ответ.
-   `chat`: Отправляет запрос в чат, поддерживая историю диалога и возвращает ответ модели.
-   `describe_image`: Описывает изображение, отправленное в виде пути к файлу или байтов.
-   `upload_file`: Загружает файл в Gemini API.

## Функции

### `__init__`

```python
def __init__(api_key: str, model_name: str = "gemini-2.0-flash-exp", generation_config: Dict = None, system_instruction: Optional[str] = None) -> None:
    """ Инициализирует объект `GoogleGenerativeAI` с API-ключом, именем модели и настройками генерации.
    Args:
        api_key (str): API-ключ Google Gemini.
        model_name (str, optional): Имя используемой модели Gemini. По умолчанию "gemini-2.0-flash-exp".
        generation_config (Dict, optional): Настройки генерации текста. По умолчанию `None`.
        system_instruction (Optional[str], optional): Системные инструкции для модели. По умолчанию `None`.
    Returns:
        None
    """
```

**Назначение**: Инициализация объекта `GoogleGenerativeAI`.

**Параметры**:
-   `api_key` (str): API-ключ Google Gemini.
-   `model_name` (str, optional): Имя используемой модели Gemini. По умолчанию "gemini-2.0-flash-exp".
-   `generation_config` (Dict, optional): Настройки генерации текста. По умолчанию `None`.
-   `system_instruction` (Optional[str], optional): Системные инструкции для модели. По умолчанию `None`.

**Возвращает**:
-   `None`

**Как работает функция**:

1.  Присваивает переданные значения атрибутам объекта `GoogleGenerativeAI`.

2.  Инициализирует клиент Gemini API с использованием переданного API-ключа.

3.  Устанавливает системные инструкции для модели Gemini, если они предоставлены.

4.  Инициализирует историю чата.

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI
from src import gs

system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)
```

### `ask`

```python
def ask(q: str, attempts: int = 15) -> Optional[str]:
    """ Отправляет текстовый запрос `q` к модели и возвращает ответ.
    Args:
        q (str): Текстовый запрос.
        attempts (int, optional): Количество попыток, если запрос не удался. По умолчанию 15.
    Returns:
        Optional[str]: Ответ модели или `None` в случае неудачи.
    """
```

**Назначение**: Отправка текстового запроса к модели Gemini и получение ответа.

**Параметры**:
-   `q` (str): Текстовый запрос.
-   `attempts` (int, optional): Количество попыток, если запрос не удался. По умолчанию 15.

**Возвращает**:
-   `Optional[str]`: Ответ модели или `None` в случае неудачи.

**Как работает функция**:

1.  Выполняет запрос к модели Gemini с заданным текстом.

2.  В случае неудачи повторяет попытку заданное количество раз.

3.  Возвращает полученный ответ или `None` в случае неудачи после всех попыток.

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI
from src import gs

system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

response = ai.ask("Какой самый большой город в мире?")
if response:
    print(response)
else:
    print("Не удалось получить ответ.")
```

### `chat`

```python
def chat(q: str) -> Optional[str]:
    """ Отправляет запрос `q` в чат, поддерживая историю диалога.
    Args:
        q (str): Текстовый запрос.
    Returns:
        Optional[str]: Ответ модели.
    """
```

**Назначение**: Отправка запроса в чат, поддерживая историю диалога и получение ответа.

**Параметры**:
-   `q` (str): Текстовый запрос.

**Возвращает**:
-   `Optional[str]`: Ответ модели.

**Как работает функция**:

1.  Добавляет запрос пользователя в историю чата.

2.  Выполняет запрос к модели Gemini с учетом истории чата.

3.  Добавляет ответ модели в историю чата.

4.  Сохраняет историю чата в JSON файл.

5.  Возвращает полученный ответ.

**Примеры**:

```python
from src.ai.gemini import GoogleGenerativeAI
from src import gs

system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

response = ai.chat("Привет, Gemini!")
if response:
    print(response)
else:
    print("Не удалось получить ответ.")

response = ai.chat("Как дела?")
if response:
    print(response)
else:
    print("Не удалось получить ответ.")
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
        Optional[str]: Текстовое описание изображения.
    """
```

**Назначение**: Описание изображения с использованием Gemini API.

**Параметры**:
-   `image` (Path | bytes): Путь к файлу изображения или байты изображения.
-   `mime_type` (Optional[str], optional): Mime-тип изображения. По умолчанию 'image/jpeg'.
-   `prompt` (Optional[str], optional): Текстовый промпт для описания изображения. По умолчанию ''.

**Возвращает**:
-   `Optional[str]`: Текстовое описание изображения.

**Как работает функция**:

1.  Определяет, представлено ли изображение в виде пути к файлу или байтов.

2.  Считывает изображение из файла, если предоставлен путь к файлу.

3.  Подготавливает запрос к Gemini API с изображением и текстовым промптом.

4.  Отправляет запрос к Gemini API и получает текстовое описание изображения.

5.  Возвращает полученное описание.

**Примеры**:

```python
import asyncio
from pathlib import Path
from src.ai.gemini import GoogleGenerativeAI
from src import gs

system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

async def main():
    image_path = Path("test.jpg")  # Замените на путь к вашему изображению
    prompt = "Проанализируй это изображение. Перечисли все объекты, которые ты можешь распознать."
    description = await ai.describe_image(image_path, prompt=prompt)
    if description:
        print(description)
    else:
        print("Не удалось получить описание изображения.")

if __name__ == "__main__":
    asyncio.run(main())
```

### `upload_file`

```python
def upload_file(file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
    """ Загружает файл в Gemini API.
    Args:
        file (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
        file_name (Optional[str], optional): Имя файла для Gemini API.
    Returns:
        bool: `True`, если файл успешно загружен, `False` в противном случае.
    """
```

**Назначение**: Загрузка файла в Gemini API.

**Параметры**:
-   `file` (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
-   `file_name` (Optional[str], optional): Имя файла для Gemini API.

**Возвращает**:
-   `bool`: `True`, если файл успешно загружен, `False` в противном случае.

**Как работает функция**:

1.  Определяет тип входного файла (путь, имя или файловый объект).

2.  Открывает файл, если предоставлен путь или имя файла.

3.  Подготавливает запрос к Gemini API с файлом.

4.  Отправляет запрос к Gemini API и проверяет результат.

5.  Возвращает `True`, если файл успешно загружен, `False` в противном случае.

**Примеры**:

```python
import asyncio
from pathlib import Path
from src.ai.gemini import GoogleGenerativeAI
from src import gs

system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

async def main():
    file_path = Path("test.txt")
    with open(file_path, "w") as f:
        f.write("Hello, Gemini!")

    file_upload = await ai.upload_file(file_path, 'test_file.txt')
    print(file_upload)

if __name__ == "__main__":
    asyncio.run(main())
```

## Дополнительно

-   **Логирование:** Все диалоги и ошибки записываются в соответствующие файлы в директории `external_storage/gemini_data/log`. Рекомендуется регулярно очищать директорию `logs`, чтобы избежать накопления больших файлов.

-   **История чата:** История диалогов хранится в JSON и текстовых файлах в директории `external_storage/gemini_data/history/`. Рекомендуется регулярно очищать директорию `history`, чтобы избежать накопления больших файлов.

-   **Обработка ошибок:** Программа обрабатывает сетевые ошибки, ошибки аутентификации и ошибки API с механизмом повторных попыток.

-   **Автозапуск:** Скрипт `run.ps1` обеспечивает запуск приложения в фоновом режиме при старте системы (только для Windows).

-   **Вызов из командной строки:** После установки, приложение можно вызывать из любой директории с помощью команды `ai`. Для корректной работы команды `ai` требуется перезагрузка терминала после установки.

## Замечания

-   Обязательно замените `gs.credentials.gemini.api_key` на ваш действительный API-ключ Google Gemini в файле `config.json`.

-   Убедитесь, что у вас установлен `google-generativeai`, `requests`, `grpcio`, `google-api-core` и `google-auth`.

-   Убедитесь, что у вас есть файл `test.jpg` в корневой папке с программой или измените путь к изображению в примере `main`.

-   Скрипт `install.ps1` требует запуска от имени администратора.