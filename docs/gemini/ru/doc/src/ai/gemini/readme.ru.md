# Модуль интеграции Google Generative AI

## Обзор

Класс `GoogleGenerativeAI` предназначен для взаимодействия с моделями Google Generative AI. Этот класс предоставляет методы для отправки запросов, обработки ответов, управления диалогами и интеграции с различными функциональностями ИИ. Он включает в себя надежную обработку ошибок, ведение журнала и настройки конфигурации для обеспечения беспрепятственной работы.

## Подробнее

Модуль предназначен для упрощения взаимодействия с Google Generative AI моделями, предоставляя удобные методы для выполнения различных задач, таких как отправка текстовых запросов, ведение диалогов, описание изображений и загрузка файлов. Он также обеспечивает надежную обработку ошибок и ведение журнала для облегчения отладки и аудита.

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI.

**Принцип работы**:
Класс `GoogleGenerativeAI` инициализируется с ключом API и другими конфигурационными параметрами. Он использует библиотеку `google.generativeai` для взаимодействия с моделями Google Generative AI. Класс предоставляет методы для отправки запросов, ведения диалогов, обработки изображений и загрузки файлов. Все взаимодействия с моделями ИИ ведутся в журнале, а диалоги сохраняются как в текстовом, так и в JSON форматах для последующего анализа.

**Методы**:
- `__init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs)`: Инициализирует класс `GoogleGenerativeAI` с необходимыми конфигурациями.
- `config()`: Получает конфигурацию из файла настроек.
- `_start_chat(self)`: Запускает сессию чата с моделью ИИ.
- `_save_dialogue(self, dialogue: list)`: Сохраняет диалог в текстовые и JSON файлы.
- `ask(self, q: str, attempts: int = 15) -> Optional[str]`: Отправляет текстовый запрос модели ИИ и получает ответ.
- `chat(self, q: str) -> str`: Отправляет сообщение чата модели ИИ и получает ответ.
- `describe_image(self, image_path: Path) -> Optional[str]`: Генерирует текстовое описание изображения.
- `upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool`: Загружает файл в модель ИИ.

## Функции

### `__init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs)`

```python
def __init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs) -> None:
    """
    Args:
        api_key (str): Ключ API для доступа к Google Generative AI.
        model_name (Optional[str], optional): Название модели для использования. По умолчанию None.
        generation_config (Optional[Dict], optional): Конфигурация генерации. По умолчанию None.
        system_instruction (Optional[str], optional): Системная инструкция для модели. По умолчанию None.
    """
```

**Назначение**: Инициализирует класс `GoogleGenerativeAI` с необходимыми конфигурациями.

**Параметры**:
- `api_key` (str): Ключ API для доступа к Google Generative AI.
- `model_name` (Optional[str], optional): Название модели для использования. По умолчанию `None`.
- `generation_config` (Optional[Dict], optional): Конфигурация генерации. По умолчанию `None`.
- `system_instruction` (Optional[str], optional): Системная инструкция для модели. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы ключевого слова.

**Как работает функция**:
1. Функция инициализирует параметры класса, такие как ключ API, имя модели, конфигурацию генерации и системную инструкцию.
2. Определяет пути для ведения журнала диалогов и хранения истории.
3. Инициализирует модель Google Generative AI с использованием предоставленного ключа API и других параметров.

```
Инициализация параметров класса
↓
Определение путей для ведения журнала
↓
Инициализация модели Google Generative AI
```

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
```

### `config()`

```python
def config(self) -> None:
    """ """
```

**Назначение**: Получает конфигурацию из файла настроек.

**Как работает функция**:
1. Функция читает и разбирает файл конфигурации, расположенный по пути `gs.path.src / 'ai' / 'gemini' / 'gemini.json'`.
2. Извлекает параметры конфигурации из файла и сохраняет их в атрибутах класса.

```
Чтение файла конфигурации
↓
Извлечение параметров конфигурации
↓
Сохранение параметров в атрибутах класса
```

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
ai.config()
```

### `_start_chat(self)`

```python
def _start_chat(self) -> None:
    """ """
```

**Назначение**: Запускает сессию чата с моделью ИИ.

**Как работает функция**:
1. Инициализирует сессию чата с пустой историей.
2. Подготавливает модель ИИ для ведения диалога.

```
Инициализация сессии чата с пустой историей
↓
Подготовка модели ИИ для ведения диалога
```

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
ai._start_chat()
```

### `_save_dialogue(self, dialogue: list)`

```python
def _save_dialogue(self, dialogue: list) -> None:
    """
    Args:
        dialogue (list): Список сообщений в диалоге.
    """
```

**Назначение**: Сохраняет диалог в текстовые и JSON файлы.

**Параметры**:
- `dialogue` (list): Список сообщений в диалоге.

**Как работает функция**:
1. Добавляет каждое сообщение в диалоге в текстовый файл.
2. Добавляет каждое сообщение в формате JSON в JSON файл.
3. Обеспечивает сохранение истории диалога для последующего анализа.

```
Добавление сообщений в текстовый файл
↓
Добавление сообщений в JSON файл
↓
Сохранение истории диалога
```

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
dialogue = ["Привет!", "Как дела?"]
ai._save_dialogue(dialogue)
```

### `ask(self, q: str, attempts: int = 15) -> Optional[str]`

```python
def ask(self, q: str, attempts: int = 15) -> Optional[str]:
    """
    Args:
        q (str): Текстовый запрос для отправки модели ИИ.
        attempts (int, optional): Максимальное количество попыток в случае ошибок. По умолчанию 15.

    Returns:
        Optional[str]: Ответ от модели ИИ или None в случае ошибки.
    """
```

**Назначение**: Отправляет текстовый запрос модели ИИ и получает ответ.

**Параметры**:
- `q` (str): Текстовый запрос для отправки модели ИИ.
- `attempts` (int, optional): Максимальное количество попыток в случае ошибок. По умолчанию `15`.

**Возвращает**:
- `Optional[str]`: Ответ от модели ИИ или `None` в случае ошибки.

**Как работает функция**:
1. Обрабатывает несколько попыток в случае ошибок сети или недоступности сервиса.
2. Ведет журнал ошибок и повторяет попытки с экспоненциальной задержкой.
3. Сохраняет диалог в файлы истории.

```
Отправка запроса модели ИИ
↓
Обработка ошибок сети или недоступности сервиса
↓
Ведение журнала ошибок и повторные попытки
↓
Сохранение диалога в файлы истории
```

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
response = ai.ask("Как дела?")
print(response)
```

### `chat(self, q: str) -> str`

```python
def chat(self, q: str) -> str:
    """
    Args:
        q (str): Сообщение чата для отправки модели ИИ.

    Returns:
        str: Ответ от модели ИИ.
    """
```

**Назначение**: Отправляет сообщение чата модели ИИ и получает ответ.

**Параметры**:
- `q` (str): Сообщение чата для отправки модели ИИ.

**Возвращает**:
- `str`: Ответ от модели ИИ.

**Как работает функция**:
1. Использует сессию чата, инициализированную методом `_start_chat`.
2. Ведет журнал ошибок и возвращает текст ответа.

```
Использование сессии чата
↓
Отправка сообщения чата модели ИИ
↓
Ведение журнала ошибок
↓
Возврат текста ответа
```

**Примеры**:

```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
ai._start_chat()
response = ai.chat("Как дела?")
print(response)
```

### `describe_image(self, image_path: Path) -> Optional[str]`

```python
def describe_image(self, image_path: Path) -> Optional[str]:
    """
    Args:
        image_path (Path): Путь к изображению.

    Returns:
        Optional[str]: Сгенерированное описание изображения или None в случае ошибки.
    """
```

**Назначение**: Генерирует текстовое описание изображения.

**Параметры**:
- `image_path` (Path): Путь к изображению.

**Возвращает**:
- `Optional[str]`: Сгенерированное описание изображения или `None` в случае ошибки.

**Как работает функция**:
1. Кодирует изображение в base64 и отправляет его модели ИИ.
2. Возвращает сгенерированное описание или ведет журнал ошибки, если операция не удалась.

```
Кодирование изображения в base64
↓
Отправка изображения модели ИИ
↓
Возврат сгенерированного описания
↓
Ведение журнала ошибки в случае неудачи
```

**Примеры**:

```python
from pathlib import Path
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
image_path = Path("image.jpg")
description = ai.describe_image(image_path)
print(description)
```

### `upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool`

```python
def upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool:
    """
    Args:
        file (str | Path | IOBase): Файл для загрузки.
        file_name (Optional[str], optional): Имя файла. По умолчанию None.

    Returns:
        bool: True в случае успеха, False в случае неудачи.
    """
```

**Назначение**: Загружает файл в модель ИИ.

**Параметры**:
- `file` (str | Path | IOBase): Файл для загрузки.
- `file_name` (Optional[str], optional): Имя файла. По умолчанию `None`.

**Возвращает**:
- `bool`: `True` в случае успеха, `False` в случае неудачи.

**Как работает функция**:
1. Обрабатывает загрузку файла и ведет журнал успеха или неудачи.
2. Предоставляет логику повторных попыток в случае ошибок.

```
Обработка загрузки файла
↓
Ведение журнала успеха или неудачи
↓
Предоставление логики повторных попыток
```

**Примеры**:

```python
from pathlib import Path
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
file_path = Path("file.txt")
success = ai.upload_file(file_path)
print(success)
```

## Обработка ошибок

Класс включает в себя комплексную обработку ошибок для различных сценариев:
- **Ошибки сети**: Повторяет попытки с экспоненциальной задержкой.
- **Недоступность сервиса**: Ведет журнал ошибок и повторяет попытки.
- **Лимиты квот**: Ведет журнал и ждет перед повторной попыткой.
- **Ошибки аутентификации**: Ведет журнал и прекращает дальнейшие попытки.
- **Неверный ввод**: Ведет журнал и повторяет попытки с таймаутом.
- **Ошибки API**: Ведет журнал и прекращает дальнейшие попытки.

## Ведение журнала и история

Все взаимодействия с моделями ИИ ведутся в журнале, и диалоги сохраняются как в текстовых, так и в JSON форматах для последующего анализа. Это обеспечивает отслеживаемость всех операций и возможность их просмотра для отладки или аудита.

## Зависимости

- `google.generativeai`
- `requests`
- `grpc`
- `google.api_core.exceptions`
- `google.auth.exceptions`
- `src.logger`
- `src.utils.printer`
- `src.utils.file`
- `src.utils.date_time`
- `src.utils.convertors.unicode`
- `src.utils.jjson`

## Пример использования

```python
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
response = ai.ask("Как дела?")
print(response)
```

Этот пример инициализирует класс `GoogleGenerativeAI` и отправляет запрос модели ИИ, выводя ответ.

---

Для получения более подробной информации обратитесь к исходному коду и комментариям внутри класса `GoogleGenerativeAI`.