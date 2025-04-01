# Модуль ChatgptDuo

## Обзор

Модуль `ChatgptDuo` предоставляет асинхронный класс `ChatgptDuo`, который позволяет взаимодействовать с моделью ChatGPT Duo через API chatgptduo.com.
Этот модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется использование ChatGPT Duo.

## Подробнее

Модуль содержит класс `ChatgptDuo`, который наследует `AsyncProvider`. Он предоставляет методы для отправки запросов к ChatGPT Duo и получения ответов. 
Модуль использует `StreamSession` для асинхронных HTTP-запросов.

## Классы

### `ChatgptDuo`

**Описание**: Класс для взаимодействия с ChatGPT Duo API.

**Наследует**:
- `AsyncProvider`: Класс, предоставляющий базовую функциональность для асинхронных провайдеров.

**Атрибуты**:
- `url` (str): URL API ChatGPT Duo.
- `supports_gpt_35_turbo` (bool): Поддержка модели gpt-3.5-turbo.
- `working` (bool): Указывает, работает ли провайдер.
- `_sources` (list): Список источников, полученных от ChatGPT Duo.

**Методы**:
- `create_async`: Асинхронный метод для отправки запроса к ChatGPT Duo и получения ответа.
- `get_sources`: Возвращает источники, полученные от ChatGPT Duo.

## Функции

### `create_async`

```python
@classmethod
async def create_async(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 120,
    **kwargs
) -> str:
    """Асинхронно отправляет запрос к ChatGPT Duo и возвращает ответ.

    Args:
        cls (ChatgptDuo): Класс ChatGPT Duo.
        model (str): Имя модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `120`.
        **kwargs: Дополнительные аргументы.

    Returns:
        str: Ответ от ChatGPT Duo.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.
    """
```

**Назначение**: Отправляет запрос к ChatGPT Duo API и получает ответ.

**Параметры**:
- `cls`: Класс `ChatgptDuo`.
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию `120`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `str`: Ответ от ChatGPT Duo.

**Вызывает исключения**:
- `HTTPError`: Если возникает ошибка HTTP при выполнении запроса.

**Как работает функция**:

1. Инициализирует асинхронную сессию с использованием `StreamSession`, настраивая `impersonate` для эмуляции браузера Chrome 107, прокси (если указан) и таймаут.
2. Форматирует промпт из списка сообщений.
3. Формирует данные запроса, включающие `prompt`, `search` и `purpose`.
4. Отправляет POST-запрос к API ChatGPT Duo.
5. Обрабатывает ответ, извлекая результаты поиска и формируя список источников `_sources`, содержащий заголовки, ссылки и сниппеты.
6. Возвращает ответ от ChatGPT Duo.

```
A: Инициализация асинхронной сессии
│
B: Форматирование промпта
│
C: Формирование данных запроса
│
D: Отправка POST-запроса к API ChatGPT Duo
│
E: Обработка ответа
│
F: Возврат ответа
```

**Примеры**:

```python
# Пример использования create_async
messages = [{"role": "user", "content": "Hello, ChatGPT Duo!"}]
response = await ChatgptDuo.create_async(model="default", messages=messages)
print(response)
```

### `get_sources`

```python
@classmethod
def get_sources(cls):
    """Возвращает список источников, полученных от ChatGPT Duo.

    Args:
        cls (ChatgptDuo): Класс ChatGPT Duo.

    Returns:
        list: Список источников.
    """
```

**Назначение**: Возвращает список источников, полученных от ChatGPT Duo.

**Параметры**:
- `cls`: Класс `ChatgptDuo`.

**Возвращает**:
- `list`: Список источников.

**Как работает функция**:

1. Возвращает список источников `_sources`, сохраненный в классе `ChatgptDuo`.

```
A: Возврат списка источников
│
B: Завершение
```

**Примеры**:

```python
# Пример использования get_sources
sources = ChatgptDuo.get_sources()
print(sources)