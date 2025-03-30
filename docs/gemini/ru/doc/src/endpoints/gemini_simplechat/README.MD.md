# Документация модуля интеграции Google Gemini API

## Оглавление
1. [Обзор](#обзор)
2. [Подробнее](#подробнее)
3. [Требования](#требования)
4. [Установка](#установка)
5. [Запуск веб-сервера](#запуск-веб-сервера)
6. [Использование](#использование)
    - [Инициализация](#инициализация)
    - [Методы класса GoogleGenerativeAI](#методы-класса-googlegenerativeai)
    - [Пример использования](#пример-использования)
7. [Дополнительно](#дополнительно)
    - [Логирование](#логирование)
    - [История чата](#история-чата)
    - [Обработка ошибок](#обработка-ошибок)
    - [Автозапуск](#автозапуск)
    - [Вызов из командной строки](#вызов-из-командной-строки)
8. [Замечания](#замечания)
9. [Лицензия](#лицензия)
10. [Автор](#автор)

## Обзор

Данный модуль предназначен для интеграции с моделями Google Generative AI (Gemini) и предоставляет класс `GoogleGenerativeAI` для удобного взаимодействия с API. Он позволяет отправлять текстовые запросы, вести диалоги, описывать изображения и загружать файлы.

## Подробнее

Модуль `GoogleGenerativeAI` обеспечивает удобный интерфейс для работы с Google Gemini API. Он поддерживает различные модели Gemini, сохраняет историю диалогов в JSON и текстовые файлы, обрабатывает ошибки с механизмом повторных попыток, позволяет настраивать параметры генерации и системные инструкции.

Этот код является частью проекта `hypotez` и предоставляет функциональность для интеграции с Google Gemini API, что позволяет использовать возможности AI для различных задач, таких как обработка текста, анализ изображений и ведение диалогов. Интеграция Gemini API дает возможность проекту `hypotez` взаимодействовать с современными AI-моделями, расширяя его функциональность и предоставляя пользователям доступ к передовым технологиям в области искусственного интеллекта.

## Требования

- Python 3.7 или выше
- Установленные библиотеки (см. `requirements.txt`).
- Действительный API ключ Google Gemini (замените в файле `config.json` на свой)
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
    Инициализирует объект `GoogleGenerativeAI` с API-ключом, именем модели и настройками генерации.
    Параметр `system_instruction` позволяет задать системные инструкции для модели.

    Args:
        api_key (str): API ключ Google Gemini.
        model_name (str, optional): Имя модели Gemini. По умолчанию "gemini-2.0-flash-exp".
        generation_config (Dict, optional): Конфигурация генерации. По умолчанию `None`.
        system_instruction (Optional[str], optional): Системные инструкции для модели. По умолчанию `None`.
    """
```

**Описание**: Инициализирует объект `GoogleGenerativeAI`.

**Параметры**:
- `api_key` (str): API ключ Google Gemini.
- `model_name` (str, optional): Имя модели Gemini. По умолчанию "gemini-2.0-flash-exp".
- `generation_config` (Dict, optional): Конфигурация генерации. По умолчанию `None`.
- `system_instruction` (Optional[str], optional): Системные инструкции для модели. По умолчанию `None`.

#### `ask`

```python
def ask(q: str, attempts: int = 15) -> Optional[str]:
    """
    Отправляет текстовый запрос `q` к модели и возвращает ответ.
    `attempts` - количество попыток, если запрос не удался.

    Args:
        q (str): Текстовый запрос.
        attempts (int, optional): Количество попыток. По умолчанию 15.

    Returns:
        Optional[str]: Ответ модели или `None` в случае неудачи.
    """
```

**Описание**: Отправляет текстовый запрос к модели.

**Параметры**:
- `q` (str): Текстовый запрос.
- `attempts` (int, optional): Количество попыток. По умолчанию 15.

**Возвращает**:
- `Optional[str]`: Ответ модели или `None` в случае неудачи.

#### `chat`

```python
def chat(q: str) -> Optional[str]:
    """
    Отправляет запрос `q` в чат, поддерживая историю диалога.
    Возвращает ответ модели.
    История чата сохраняется в JSON файл.

    Args:
        q (str): Текстовый запрос.

    Returns:
        Optional[str]: Ответ модели или `None` в случае неудачи.
    """
```

**Описание**: Отправляет запрос в чат.

**Параметры**:
- `q` (str): Текстовый запрос.

**Возвращает**:
- `Optional[str]`: Ответ модели или `None` в случае неудачи.

#### `describe_image`

```python
def describe_image(image: Path | bytes, mime_type: Optional[str] = 'image/jpeg', prompt: Optional[str] = '') -> Optional[str]:
    """
    Описывает изображение, отправленное в виде пути к файлу или байтов.
    `image`: путь к файлу изображения или байты изображения.
    `mime_type`: mime-тип изображения.
    `prompt`: текстовый промпт для описания изображения.
    Возвращает текстовое описание изображения.

    Args:
        image (Path | bytes): Путь к файлу изображения или байты изображения.
        mime_type (Optional[str], optional): Mime-тип изображения. По умолчанию 'image/jpeg'.
        prompt (Optional[str], optional): Текстовый промпт для описания изображения. По умолчанию ''.

    Returns:
        Optional[str]: Текстовое описание изображения или `None` в случае неудачи.
    """
```

**Описание**: Описывает изображение.

**Параметры**:
- `image` (Path | bytes): Путь к файлу изображения или байты изображения.
- `mime_type` (Optional[str], optional): Mime-тип изображения. По умолчанию 'image/jpeg'.
- `prompt` (Optional[str], optional): Текстовый промпт для описания изображения. По умолчанию ''.

**Возвращает**:
- `Optional[str]`: Текстовое описание изображения или `None` в случае неудачи.

#### `upload_file`

```python
def upload_file(file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
    """
    Загружает файл в Gemini API.
    `file`: путь к файлу, имя файла или файловый объект.
    `file_name`: имя файла для Gemini API.

    Args:
        file (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
        file_name (Optional[str], optional): Имя файла для Gemini API.

    Returns:
        bool: `True`, если файл успешно загружен, `False` в противном случае.
    """
```

**Описание**: Загружает файл в Gemini API.

**Параметры**:
- `file` (str | Path | IOBase): Путь к файлу, имя файла или файловый объект.
- `file_name` (Optional[str], optional): Имя файла для Gemini API.

**Возвращает**:
- `bool`: `True`, если файл успешно загружен, `False` в противном случае.

### Пример использования

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
* Логи сохраняются в следующие файлы: `info.log`, `debug.log`, `errors.log`, `log.json`.
* **Рекомендация:**  Регулярно очищайте директорию `logs`, чтобы избежать накопления больших файлов.

### История чата

История диалогов хранится в JSON и текстовых файлах в директории `external_storage/gemini_data/history/`.
* Каждый новый диалог создаёт новые файлы.
* **Рекомендация:**  Регулярно очищайте директорию `history`, чтобы избежать накопления больших файлов.

### Обработка ошибок

Программа обрабатывает сетевые ошибки, ошибки аутентификации и ошибки API с механизмом повторных попыток.

### Автозапуск

Скрипт `run.ps1` обеспечивает запуск приложения в фоновом режиме при старте системы (только для Windows).

### Вызов из командной строки

После установки, приложение можно вызывать из любой директории с помощью команды `ai`. Для корректной работы команды `ai` требуется перезагрузка терминала после установки.

## Замечания

- Обязательно замените `gs.credentials.gemini.api_key` на ваш действительный API-ключ Google Gemini в файле `config.json`.
- Убедитесь, что у вас установлен `google-generativeai`, `requests`, `grpcio`, `google-api-core` и `google-auth`.
- Убедитесь, что у вас есть файл `test.jpg` в корневой папке с программой или измените путь к изображению в примере `main`.
- Скрипт `install.ps1` требует запуска от имени администратора.

## Лицензия

Этот проект распространяется под [MIT].

## Автор

[hypo69]