# Модуль `src.ai.gemini.generative_ai`

## Обзор

Модуль `src.ai.gemini.generative_ai` предназначен для интеграции с моделями Google Generative AI. Он обеспечивает функциональность для отправки текстовых и мультимодальных запросов к моделям Gemini, включая возможности загрузки файлов, ведения диалога и обработки изображений.

## Оглавление

- [Класс `GoogleGenerativeAI`](#класс-googlegenerativeai)
    - [Метод `__init__`](#__init__)
    - [Свойство `config`](#свойство-config)
    - [Метод `_start_chat`](#метод-_start_chat)
    - [Метод `_save_dialogue`](#метод-_save_dialogue)
    - [Метод `_save_chat_history`](#метод-_save_chat_history)
    - [Метод `_load_chat_history`](#метод-_load_chat_history)
    - [Метод `ask`](#метод-ask)
    - [Метод `chat`](#метод-chat)
    - [Метод `describe_image`](#метод-describe_image)
    - [Метод `upload_file`](#метод-upload_file)
- [Асинхронная функция `main`](#асинхронная-функция-main)

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI.

**Параметры**:

- `api_key` (str): Ключ API для доступа к Google Generative AI.
- `model_name` (Optional[str], optional): Название используемой модели. По умолчанию `"gemini-2.0-flash-exp"`.
- `generation_config` (Optional[Dict], optional): Конфигурация генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `system_instruction` (Optional[str], optional): Инструкция для модели. По умолчанию `None`.
- `**kwargs`: Дополнительные произвольные аргументы.

**Методы**:

- [`__init__`](#__init__): Инициализирует экземпляр класса GoogleGenerativeAI.
- [`config`](#свойство-config): Возвращает конфигурацию модели из файла.
- [`_start_chat`](#метод-_start_chat): Инициализирует чат с моделью.
- [`_save_dialogue`](#метод-_save_dialogue): Сохраняет диалог в JSON файл.
- [`_save_chat_history`](#метод-_save_chat_history): Сохраняет всю историю чата в JSON файл.
- [`_load_chat_history`](#метод-_load_chat_history): Загружает историю чата из JSON файла.
- [`ask`](#метод-ask): Отправляет текстовый запрос и возвращает ответ.
- [`chat`](#метод-chat): Отправляет текстовый запрос в контексте диалога.
- [`describe_image`](#метод-describe_image): Отправляет изображение для описания.
- [`upload_file`](#метод-upload_file): Загружает файл в модель.

#### `__init__`

**Описание**: Инициализация модели GoogleGenerativeAI с дополнительными настройками.

**Параметры**:

- `api_key` (str): Ключ API для доступа к Google Generative AI.
- `model_name` (Optional[str], optional): Название используемой модели. По умолчанию `"gemini-2.0-flash-exp"`.
- `generation_config` (Optional[Dict], optional): Конфигурация генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `system_instruction` (Optional[str], optional): Инструкция для модели. По умолчанию `None`.
- `**kwargs`: Дополнительные произвольные аргументы.

#### `config`

**Описание**: Получает конфигурацию из файла настроек.

**Возвращает**:
- `SimpleNamespace`: Конфигурация модели, загруженная из файла `generative_ai.json`.

#### `_start_chat`

**Описание**: Инициализирует чат с моделью, опционально используя системные инструкции.

**Возвращает**:
- `google.generativeai.ChatSession`: Сессия чата.

#### `_save_dialogue`

**Описание**: Сохраняет диалог в JSON файл.

**Параметры**:
- `dialogue` (list): Список сообщений диалога.

#### `_save_chat_history`

**Описание**: Сохраняет всю историю чата в JSON файл.

#### `_load_chat_history`

**Описание**: Загружает историю чата из JSON файла.

#### `ask`

**Описание**: Метод отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:
- `q` (str): Текст запроса.
- `attempts` (int, optional): Количество попыток отправки запроса. По умолчанию `15`.

**Возвращает**:
- `Optional[str]`: Текст ответа от модели или `None` в случае ошибки или отсутствия ответа.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Сетевые ошибки при отправке запроса.
- `GatewayTimeout, ServiceUnavailable`: Ошибки, связанные с недоступностью сервиса.
- `ResourceExhausted`: Превышение квоты запросов.
- `DefaultCredentialsError, RefreshError`: Ошибки аутентификации.
- `ValueError, TypeError`: Ошибки, связанные с некорректными входными данными.
- `InvalidArgument, RpcError`: Ошибки API.
- `Exception`: Непредвиденные ошибки.

#### `chat`

**Описание**: Отправляет текстовый запрос в контексте диалога.

**Параметры**:
- `q` (str): Текст запроса.

**Возвращает**:
- `Optional[str]`: Текст ответа от модели или `None` в случае ошибки или отсутствия ответа.
- `Exception`: Возвращает объект исключения в случае ошибки.

#### `describe_image`

**Описание**: Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.

**Параметры**:
- `image` (Path | bytes): Путь к файлу изображения или байты изображения.
- `mime_type` (Optional[str], optional): MIME-тип изображения. По умолчанию `image/jpeg`.
- `prompt` (Optional[str], optional): Дополнительное текстовое описание запроса. По умолчанию `''`.

**Возвращает**:
- `Optional[str]`: Текстовое описание изображения или `None` в случае ошибки.

#### `upload_file`

**Описание**: Загружает файл в модель.

**Параметры**:
- `file` (str | Path | IOBase): Путь к файлу, байтовое представление файла или файловый объект.
- `file_name` (Optional[str], optional): Название файла. По умолчанию `None`.

**Возвращает**:
- `bool`: `True` в случае успешной загрузки, иначе - `False`.

## Функции

### `main`

**Описание**: Асинхронная функция для демонстрации работы с `GoogleGenerativeAI`.

**Пример использования**:
```python
async def main():
    # Замените на свой ключ API
    api_key = "YOUR_API_KEY"
    system_instruction = "Ты - полезный ассистент. Отвечай на все вопросы кратко"
    ai = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction)

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

    file_upload = await ai.upload_file(file_path,'test_file.txt')
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