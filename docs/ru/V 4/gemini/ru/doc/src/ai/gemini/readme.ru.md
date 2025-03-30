# Модуль интеграции Google Generative AI

## Обзор

Класс `GoogleGenerativeAI` предназначен для взаимодействия с моделями Google Generative AI. Этот класс предоставляет методы для отправки запросов, обработки ответов, управления диалогами и интеграции с различными функциональностями ИИ. Он включает в себя надежную обработку ошибок, ведение журнала и настройки конфигурации для обеспечения беспрепятственной работы.

## Подробней

Модуль `GoogleGenerativeAI` обеспечивает интеграцию с моделями Google Generative AI. Он позволяет отправлять запросы к моделям, обрабатывать ответы, управлять диалогами и взаимодействовать с другими функциями ИИ. Модуль предназначен для упрощения работы с Google Generative AI в проекте `hypotez`.

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI.

**Методы**:
- `__init__`: Инициализирует экземпляр класса.
- `config`: Получает конфигурацию из файла настроек.
- `_start_chat`: Запускает сессию чата с моделью ИИ.
- `_save_dialogue`: Сохраняет диалог в текстовые и JSON файлы.
- `ask`: Отправляет текстовый запрос модели ИИ и получает ответ.
- `chat`: Отправляет сообщение чата модели ИИ и получает ответ.
- `describe_image`: Генерирует текстовое описание изображения.
- `upload_file`: Загружает файл в модель ИИ.

**Параметры**:
- `api_key` (str): Ключ API для доступа к Google Generative AI.
- `model_name` (Optional[str], optional): Имя используемой модели. По умолчанию `None`.
- `generation_config` (Optional[Dict], optional): Конфигурация генерации. По умолчанию `None`.
- `system_instruction` (Optional[str], optional): Системная инструкция. По умолчанию `None`.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
response = ai.ask("Как дела?")
print(response)
```

## Функции

### `__init__`

```python
def __init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs):
    """
    Args:
        api_key (str): Ключ API для доступа к Google Generative AI.
        model_name (Optional[str], optional): Имя используемой модели. По умолчанию `None`.
        generation_config (Optional[Dict], optional): Конфигурация генерации. По умолчанию `None`.
        system_instruction (Optional[str], optional): Системная инструкция. По умолчанию `None`.

    Raises:
        Exception: Ошибка при инициализации Google Generative AI.
    """
```

**Описание**: Инициализирует класс `GoogleGenerativeAI` с необходимыми конфигурациями.

**Параметры**:
- `api_key` (str): Ключ API для доступа к Google Generative AI.
- `model_name` (Optional[str], optional): Имя используемой модели. По умолчанию `None`.
- `generation_config` (Optional[Dict], optional): Конфигурация генерации. По умолчанию `None`.
- `system_instruction` (Optional[str], optional): Системная инструкция. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Вызывает исключения**:
- `Exception`: Ошибка при инициализации Google Generative AI.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
```

### `config`

```python
def config(self):
    """
    Raises:
        FileNotFoundError: Если файл конфигурации не найден.
        json.JSONDecodeError: Если файл конфигурации содержит невалидный JSON.
        Exception: При возникновении других ошибок при чтении конфигурации.
    """
```

**Описание**: Получает конфигурацию из файла настроек.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл конфигурации не найден.
- `json.JSONDecodeError`: Если файл конфигурации содержит невалидный JSON.
- `Exception`: При возникновении других ошибок при чтении конфигурации.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
config = ai.config()
print(config)
```

### `_start_chat`

```python
def _start_chat(self):
    """
    Returns:
        google.generativeai.generative_models.ChatSession: Новая сессия чата.
    """
```

**Описание**: Запускает сессию чата с моделью ИИ.

**Возвращает**:
- `google.generativeai.generative_models.ChatSession`: Новая сессия чата.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
chat_session = ai._start_chat()
```

### `_save_dialogue`

```python
def _save_dialogue(self, dialogue: list):
    """
    Args:
        dialogue (list): Список сообщений для сохранения.

    Raises:
        OSError: Если возникает ошибка при создании директории или записи в файл.
        TypeError: Если возникает ошибка при сериализации JSON.
    """
```

**Описание**: Сохраняет диалог в текстовые и JSON файлы.

**Параметры**:
- `dialogue` (list): Список сообщений для сохранения.

**Вызывает исключения**:
- `OSError`: Если возникает ошибка при создании директории или записи в файл.
- `TypeError`: Если возникает ошибка при сериализации JSON.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
dialogue = [{"role": "user", "parts": ["Привет"]}, {"role": "model", "parts": ["Здравствуйте"]}]
ai._save_dialogue(dialogue)
```

### `ask`

```python
def ask(self, q: str, attempts: int = 15) -> Optional[str]:
    """
    Args:
        q (str): Текст запроса.
        attempts (int, optional): Количество попыток выполнения запроса. По умолчанию 15.

    Returns:
        Optional[str]: Ответ от модели ИИ или None в случае неудачи.

    Raises:
        Exception: Если все попытки завершились неудачей.
    """
```

**Описание**: Отправляет текстовый запрос модели ИИ и получает ответ.

**Параметры**:
- `q` (str): Текст запроса.
- `attempts` (int, optional): Количество попыток выполнения запроса. По умолчанию 15.

**Возвращает**:
- `Optional[str]`: Ответ от модели ИИ или `None` в случае неудачи.

**Вызывает исключения**:
- `Exception`: Если все попытки завершились неудачей.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
response = ai.ask("Как дела?")
print(response)
```

### `chat`

```python
def chat(self, q: str) -> str:
    """
    Args:
        q (str): Текст сообщения для чата.

    Returns:
        str: Ответ от модели ИИ.

    Raises:
        Exception: Если произошла ошибка во время чата.
    """
```

**Описание**: Отправляет сообщение чата модели ИИ и получает ответ.

**Параметры**:
- `q` (str): Текст сообщения для чата.

**Возвращает**:
- `str`: Ответ от модели ИИ.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка во время чата.

**Примеры**:
```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
response = ai.chat("Привет")
print(response)
```

### `describe_image`

```python
def describe_image(self, image_path: Path) -> Optional[str]:
    """
    Args:
        image_path (Path): Путь к изображению.

    Returns:
        Optional[str]: Описание изображения или None в случае неудачи.

    Raises:
        FileNotFoundError: Если файл изображения не найден.
        Exception: Если произошла ошибка при описании изображения.
    """
```

**Описание**: Генерирует текстовое описание изображения.

**Параметры**:
- `image_path` (Path): Путь к изображению.

**Возвращает**:
- `Optional[str]`: Описание изображения или `None` в случае неудачи.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл изображения не найден.
- `Exception`: Если произошла ошибка при описании изображения.

**Примеры**:
```python
from pathlib import Path
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
image_path = Path("example.jpg")
description = ai.describe_image(image_path)
if description:
    print(description)
```

### `upload_file`

```python
def upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
    """
    Args:
        file (str | Path | IOBase): Путь к файлу, сам файл или объект IOBase.
        file_name (Optional[str], optional): Имя файла. По умолчанию None.

    Returns:
        bool: True в случае успеха, False в случае неудачи.

    Raises:
        FileNotFoundError: Если файл не найден.
        Exception: Если произошла ошибка при загрузке файла.
    """
```

**Описание**: Загружает файл в модель ИИ.

**Параметры**:
- `file` (str | Path | IOBase): Путь к файлу, сам файл или объект `IOBase`.
- `file_name` (Optional[str], optional): Имя файла. По умолчанию `None`.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в случае неудачи.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `Exception`: Если произошла ошибка при загрузке файла.

**Примеры**:
```python
from pathlib import Path
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
file_path = Path("example.txt")
success = ai.upload_file(file_path)
print(success)