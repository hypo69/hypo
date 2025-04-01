# Документация модуля `base_provider.py`

## Обзор

Модуль `base_provider.py` предназначен для определения базового класса провайдера, который служит основой для создания различных провайдеров, используемых в проекте `hypotez` для взаимодействия с различными сервисами. Модуль также содержит импорты необходимых типов и классов для работы с провайдерами и их ответами.

## Подробней

Этот модуль определяет абстрактный класс `AbstractProvider`, от которого наследуются конкретные реализации провайдеров. Он задает структуру и общие методы, которые должны быть реализованы в каждом провайдере. Это позволяет обеспечить единообразие и упростить добавление новых провайдеров.

## Классы

### `AbstractProvider`

**Описание**: Абстрактный базовый класс для всех провайдеров.

**Принцип работы**:
Класс `AbstractProvider` определяет интерфейс, которому должны соответствовать все провайдеры. Он содержит абстрактные методы, такие как `_create_completion` и `conversation`, которые должны быть реализованы в дочерних классах.

**Аттрибуты**:
- `name` (str): Имя провайдера.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных.
- `needs_auth` (bool): Указывает, требуется ли аутентификация для использования провайдера.
- `working` (bool): Указывает, работает ли провайдер в данный момент.

**Методы**:
- `_create_completion(prompt: str, stream: bool, conversation: BaseConversation, **kwargs) -> str | Generator[str, None, None] | None`: Абстрактный метод для создания завершения.
- `conversation(prompt: str, stream: bool = False, **kwargs) -> BaseConversation`: Метод для создания и обработки разговора с провайдером.

### `ProviderUtils`

**Описание**: Класс, предоставляющий утилиты для работы с провайдерами.

**Принцип работы**:
Класс `ProviderUtils` содержит методы для логирования ответов провайдеров и обработки ошибок. Он используется для упрощения процесса отладки и мониторинга работы провайдеров.

**Методы**:
- `log_response(text: str)`: Метод для логирования ответа провайдера.

## Функции

### `format_prompt`

```python
def format_prompt(prompt: str, model: str) -> str:
    """Форматирует промпт для использования с определенной моделью.

    Args:
        prompt (str): Исходный промпт.
        model (str): Имя модели.

    Returns:
        str: Отформатированный промпт.

    Raises:
        Exception: Если модель не поддерживается.

    """
```

**Назначение**: Форматирует промпт для использования с определенной моделью.

**Параметры**:
- `prompt` (str): Исходный промпт.
- `model` (str): Имя модели.

**Возвращает**:
- `str`: Отформатированный промпт.

**Вызывает исключения**:
- `Exception`: Если модель не поддерживается.

**Как работает функция**:
1. Функция принимает на вход исходный промпт и имя модели.
2. Если модель равна "llama2", функция добавляет к промпту специальные токены `<s>[INST] ` и ` </s>`.
3. Если модель не поддерживается, функция вызывает исключение.
4. В конце функция возвращает отформатированный промпт.

```
Форматирование промпта
│
prompt, model
│
Проверка модели (llama2)
│
Добавление токенов (если llama2)
│
Возврат отформатированного промпта
│
Конец
```

**Примеры**:

```python
prompt = "Hello, how are you?"
model = "llama2"
formatted_prompt = format_prompt(prompt, model)
print(formatted_prompt)  # Вывод: <s>[INST] Hello, how are you? </s>

prompt = "Tell me a joke."
model = "gemini"
try:
    formatted_prompt = format_prompt(prompt, model)
except Exception as ex:
    print(f"Error: {ex}")  # Вывод: Error: Model not supported
```

### `get_cookies`

```python
def get_cookies(url: str, selenium: bool = False) -> dict[str, str]:
    """Получает cookies для указанного URL.

    Args:
        url (str): URL для получения cookies.
        selenium (bool): Использовать Selenium для получения cookies.

    Returns:
        dict[str, str]: Словарь cookies.

    Raises:
        Exception: Если не удалось получить cookies.

    """
```

**Назначение**: Получает cookies для указанного URL.

**Параметры**:
- `url` (str): URL для получения cookies.
- `selenium` (bool): Использовать Selenium для получения cookies.

**Возвращает**:
- `dict[str, str]`: Словарь cookies.

**Вызывает исключения**:
- `Exception`: Если не удалось получить cookies.

**Как работает функция**:
1. Функция принимает на вход URL и флаг, указывающий, использовать ли Selenium для получения cookies.
2. Если `selenium` равен `True`, функция использует Selenium для получения cookies.
3. Если `selenium` равен `False`, функция пытается получить cookies без использования Selenium.
4. В случае успеха функция возвращает словарь cookies.
5. Если не удалось получить cookies, функция вызывает исключение.

```
Получение cookies
│
url, selenium
│
Проверка selenium
│
Получение cookies (с Selenium или без)
│
Возврат словаря cookies
│
Конец
```

**Примеры**:

```python
url = "https://example.com"
cookies = get_cookies(url)
print(cookies)  # Вывод: {'cookie1': 'value1', 'cookie2': 'value2', ...}

url = "https://example.com"
selenium = True
cookies = get_cookies(url, selenium)
print(cookies)  # Вывод: {'cookie1': 'value1', 'cookie2': 'value2', ...}