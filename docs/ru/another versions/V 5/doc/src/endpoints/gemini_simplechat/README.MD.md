# Google Gemini API Интеграция

## Обзор

Этот проект предоставляет класс `GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI (Gemini). Он позволяет отправлять текстовые запросы, вести диалоги, описывать изображения и загружать файлы, используя API Google Gemini.

## Подробней

Этот код предоставляет возможность интеграции с моделями Google Gemini для выполнения различных задач, таких как обработка текста, изображений и файлов. Он включает в себя класс `GoogleGenerativeAI`, который упрощает взаимодействие с API Google Gemini, и примеры использования для демонстрации его функциональности. Проект также включает веб-интерфейс для взаимодействия с чат-ботом и скрипт для автоматической установки и настройки автозапуска приложения в Windows.

## Содержание

-   [Особенности](#особенности)
-   [Требования](#требования)
-   [Установка](#установка)
-   [Запуск веб-сервера](#запуск-веб-сервера)
-   [Использование](#использование)
    -   [Инициализация](#инициализация)
    -   [Методы класса `GoogleGenerativeAI`](#методы-класса-googlegenerativeai)
-   [Пример использования](#пример-использования)
-   [Дополнительно](#дополнительно)
    -   [Логирование](#логирование)
    -   [История чата](#история-чата)
    -   [Обработка ошибок](#обработка-ошибок)
    -   [Автозапуск](#автозапуск)
    -   [Вызов из командной строки](#вызов-из-командной-строки)
-   [Замечания](#замечания)
-   [Лицензия](#лицензия)
-   [Автор](#автор)

## Особенности

-   Поддержка различных моделей Gemini.
-   Сохранение истории диалогов в JSON и текстовый файлы.
-   Работа с текстом, изображениями и файлами.
-   Обработка ошибок с механизмом повторных попыток.
-   Возможность настраивать параметры генерации и системные инструкции.
-   Пример использования в `main()` с загрузкой и чтением изображений и файлов, а также с интерактивным чатом.
-   Веб-интерфейс для взаимодействия с чат-ботом.
-   Автоматический запуск приложения при старте системы и возможность вызова из командной строки (только для Windows).

## Требования

-   Python 3.7 или выше
-   Установленные библиотеки (см. `requirements.txt`).
-   Действительный API ключ Google Gemini (замените в файле  `config.json` на свой)
    [Получить ключ здесь](https://aistudio.google.com/app)

## Установка

1.  **Клонировать репозиторий:**

    ```bash
    git clone https://github.com/hypo69/gemini-simplechat-ru.git
    cd gemini-simplechat-ru
    ```

2.  **Установка зависимостей:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Создайте или настройте файл конфигурации:**

    В `/config.json`  можете поместить настройки, которые потребуются для вашей работы.
    Пример:

    ```json
    {
      "path": {
        "external_storage": "chat_data",
        "google_drive": "chat_data",
        "log": "/log",
        "tmp": "/tmp",
        "src": "/src",
        "root": ".",
        "endpoints": "."
      },
      "credentials": {
        "gemini": {
          "model_name": "gemini-1.5-flash-8b-exp-0924",
          "avaible_maodels": [
            "gemini-2.0-flash-exp",
            "gemini-1.5-flash-8b-exp-0924",
            "gemini-1.5-flash",
            "gemini-1.5-flash-8b"
          ],
          "api_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" // <- ВАШ КЛЮЧ GEMINI API
        }
      },
      "fast_api": {
        "host": "127.0.0.1",
        "port": "3000",
        "index_path": "html/index.html"
      },
      "now": ""
    }
    ```

    **Примечание:** API ключ необходимо заменить на свой.

4.  **Использование скрипта `install.ps1` для установки (только для Windows)**
    Для автоматической установки проекта и настройки автозапуска приложения, вы можете использовать скрипт `install.ps1`, который скопирует все файлы проекта в папку `AI Assistant` в директории `%LOCALAPPDATA%`. Также скрипт настроит запуск `main.py` при старте системы через скрипт `run.ps1` и добавит возможность вызова приложения из командной строки с помощью команды `ai`.

    **Инструкции:**

    1.  Скопируйте скрипт `install.ps1` в корневую директорию проекта.
    2.  Откройте PowerShell от имени администратора.
    3.  Перейдите в директорию проекта: `cd <путь_к_проекту>`.
    4.  Запустите скрипт, выполнив команду: `.\\install.ps1`

        Скрипт создаст папку `AI Assistant` по пути  `%LOCALAPPDATA%\\AI Assistant`, скопирует в неё все файлы проекта, настроит автозапуск приложения при старте системы через скрипт `run.ps1`, и добавит команду `ai` для вызова приложения из командной строки.

## Запуск веб-сервера

Для запуска веб-сервера используйте команду:

```bash
python main.py
```

После запуска, веб-интерфейс будет доступен по адресу http://127.0.0.1:8000.

## Использование

### Инициализация

```python
from src.ai.gemini import GoogleGenerativeAI
import gs

system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)
```

### Методы класса `GoogleGenerativeAI`

#### `__init__`

```python
def __init__(api_key: str, model_name: str = "gemini-2.0-flash-exp", generation_config: Dict = None, system_instruction: Optional[str] = None) -> None:
    """
    Args:
        api_key (str): Ключ API для доступа к Google Gemini.
        model_name (str, optional): Имя используемой модели Gemini. По умолчанию "gemini-2.0-flash-exp".
        generation_config (Dict, optional): Конфигурация генерации для модели Gemini. По умолчанию None.
        system_instruction (Optional[str], optional): Системные инструкции для модели. По умолчанию None.

    Returns:
        None

    Raises:
        Exception: Если api_key не предоставлен.

    Example:
        >>> ai = GoogleGenerativeAI(api_key='your_api_key', system_instruction='Отвечай кратко.')
    """
```

**Описание**: Инициализирует объект `GoogleGenerativeAI` с API-ключом, именем модели и настройками генерации.

**Как работает класс**:
Метод `__init__` является конструктором класса `GoogleGenerativeAI`. Он принимает API-ключ, имя модели, конфигурацию генерации и системные инструкции в качестве аргументов. Если API-ключ не предоставлен, метод вызывает исключение.

**Параметры**:
- `api_key` (str): Ключ API для доступа к Google Gemini.
- `model_name` (str, optional): Имя используемой модели Gemini. По умолчанию "gemini-2.0-flash-exp".
- `generation_config` (Dict, optional): Конфигурация генерации для модели Gemini. По умолчанию None.
- `system_instruction` (Optional[str], optional): Системные инструкции для модели. По умолчанию None.

**Возвращает**:
- None

**Вызывает исключения**:
- Exception: Если api_key не предоставлен.

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key='your_api_key', system_instruction='Отвечай кратко.')
```

#### `ask`

```python
def ask(q: str, attempts: int = 15) -> Optional[str]:
    """
    Args:
        q (str): Текстовый запрос для отправки в модель Gemini.
        attempts (int, optional): Количество попыток при неудачном запросе. По умолчанию 15.

    Returns:
        Optional[str]: Ответ от модели Gemini или None в случае ошибки.

    Raises:
        Exception: Если все попытки запроса не удались.

    Example:
        >>> response = ai.ask('Какой сейчас год?')
        >>> print(response)
        2024
    """
```

**Описание**: Отправляет текстовый запрос `q` к модели и возвращает ответ.

**Как работает класс**:
Метод `ask` отправляет текстовый запрос `q` к модели Gemini и возвращает ответ. Если запрос не удался, метод повторяет попытки до `attempts` раз. Если все попытки не удались, метод возвращает `None`.

**Параметры**:
- `q` (str): Текстовый запрос для отправки в модель Gemini.
- `attempts` (int, optional): Количество попыток при неудачном запросе. По умолчанию 15.

**Возвращает**:
- `Optional[str]`: Ответ от модели Gemini или None в случае ошибки.

**Вызывает исключения**:
- Exception: Если все попытки запроса не удались.

**Примеры**:

```python
response = ai.ask('Какой сейчас год?')
print(response)
```

#### `chat`

```python
def chat(q: str) -> Optional[str]:
    """
    Args:
        q (str): Текстовый запрос для отправки в чат.

    Returns:
        Optional[str]: Ответ от модели Gemini или None в случае ошибки.

    Raises:
        Exception: Если произошла ошибка при взаимодействии с моделью Gemini.

    Example:
        >>> response = ai.chat('Привет!')
        >>> print(response)
        Здравствуйте!
    """
```

**Описание**: Отправляет запрос `q` в чат, поддерживая историю диалога.

**Как работает класс**:
Метод `chat` отправляет текстовый запрос `q` в чат, поддерживая историю диалога. История чата сохраняется в JSON файл. Метод возвращает ответ от модели Gemini или `None` в случае ошибки.

**Параметры**:
- `q` (str): Текстовый запрос для отправки в чат.

**Возвращает**:
- `Optional[str]`: Ответ от модели Gemini или None в случае ошибки.

**Вызывает исключения**:
- Exception: Если произошла ошибка при взаимодействии с моделью Gemini.

**Примеры**:

```python
response = ai.chat('Привет!')
print(response)
```

#### `describe_image`

```python
def describe_image(image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = '') -> Optional[str]:
    """
    Args:
        image (Path | bytes): Путь к файлу изображения или байты изображения.
        mime_type (Optional[str], optional): MIME-тип изображения. По умолчанию 'image/jpeg'.
        prompt (Optional[str], optional): Текстовый промпт для описания изображения. По умолчанию ''.

    Returns:
        Optional[str]: Текстовое описание изображения или None в случае ошибки.

    Raises:
        Exception: Если произошла ошибка при взаимодействии с моделью Gemini.

    Example:
        >>> image_path = Path('test.jpg')
        >>> description = ai.describe_image(image_path, prompt='Опиши изображение.')
        >>> print(description)
        На изображении изображен ...
    """
```

**Описание**: Описывает изображение, отправленное в виде пути к файлу или байтов.

**Как работает класс**:
Метод `describe_image` принимает путь к файлу изображения или байты изображения, MIME-тип и текстовый промпт в качестве аргументов. Он отправляет изображение и промпт в модель Gemini и возвращает текстовое описание изображения.

**Параметры**:
- `image` (Path | bytes): Путь к файлу изображения или байты изображения.
- `mime_type` (Optional[str], optional): MIME-тип изображения. По умолчанию 'image/jpeg'.
- `prompt` (Optional[str], optional): Текстовый промпт для описания изображения. По умолчанию ''.

**Возвращает**:
- `Optional[str]`: Текстовое описание изображения или None в случае ошибки.

**Вызывает исключения**:
- Exception: Если произошла ошибка при взаимодействии с моделью Gemini.

**Примеры**:

```python
image_path = Path('test.jpg')
description = ai.describe_image(image_path, prompt='Опиши изображение.')
print(description)
```

#### `upload_file`

```python
def upload_file(file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
    """
    Args:
        file (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
        file_name (Optional[str], optional): Имя файла для Gemini API. По умолчанию None.

    Returns:
        bool: True, если файл успешно загружен, False в противном случае.

    Raises:
        Exception: Если произошла ошибка при загрузке файла.

    Example:
        >>> file_path = Path('test.txt')
        >>> success = ai.upload_file(file_path, 'test_file.txt')
        >>> print(success)
        True
    """
```

**Описание**: Загружает файл в Gemini API.

**Как работает класс**:
Метод `upload_file` принимает путь к файлу, имя файла или файловый объект и имя файла для Gemini API в качестве аргументов. Он загружает файл в Gemini API и возвращает `True`, если файл успешно загружен, `False` в противном случае.

**Параметры**:
- `file` (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
- `file_name` (Optional[str], optional): Имя файла для Gemini API. По умолчанию None.

**Возвращает**:
- `bool`: True, если файл успешно загружен, False в противном случае.

**Вызывает исключения**:
- Exception: Если произошла ошибка при загрузке файла.

**Примеры**:

```python
file_path = Path('test.txt')
success = ai.upload_file(file_path, 'test_file.txt')
print(success)
```

## Пример использования

```python
import asyncio
from pathlib import Path
from src.ai.gemini import GoogleGenerativeAI
from src import gs
from src.utils.jjson import j_loads

# Замените на свой ключ API
system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
ai = GoogleGenerativeAI(api_key=gs.credentials.gemini.api_key, system_instruction=system_instruction)

async def main():
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

## Дополнительно

### Логирование

Все диалоги и ошибки записываются в соответствующие файлы в директории `external_storage/gemini_data/log`.

*   Логи сохраняются в следующие файлы: `info.log`, `debug.log`, `errors.log`, `log.json`.
*   **Рекомендация:**  Регулярно очищайте директорию `logs`, чтобы избежать накопления больших файлов.

### История чата

История диалогов хранится в JSON и текстовых файлах в директории `external_storage/gemini_data/history/`.

*   Каждый новый диалог создаёт новые файлы.
*   **Рекомендация:**  Регулярно очищайте директорию `history`, чтобы избежать накопления больших файлов.

### Обработка ошибок

Программа обрабатывает сетевые ошибки, ошибки аутентификации и ошибки API с механизмом повторных попыток.

### Автозапуск

Скрипт `run.ps1` обеспечивает запуск приложения в фоновом режиме при старте системы (только для Windows).

### Вызов из командной строки

После установки, приложение можно вызывать из любой директории с помощью команды `ai`. Для корректной работы команды `ai` требуется перезагрузка терминала после установки.

## Замечания

-   Обязательно замените `gs.credentials.gemini.api_key` на ваш действительный API-ключ Google Gemini в файле `config.json`.
-   Убедитесь, что у вас установлен `google-generativeai`, `requests`, `grpcio`, `google-api-core` и `google-auth` .
-   Убедитесь, что у вас есть файл `test.jpg` в корневой папке с программой или измените путь к изображению в примере `main`.
-   Скрипт `install.ps1` требует запуска от имени администратора.

## Лицензия

Этот проект распространяется под [MIT].

## Автор

[hypo69]