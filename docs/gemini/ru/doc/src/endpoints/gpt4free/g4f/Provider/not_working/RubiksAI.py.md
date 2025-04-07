# Модуль для работы с провайдером RubiksAI
=========================================

Модуль содержит класс :class:`RubiksAI`, который используется для взаимодействия с AI-моделью Rubiks AI и получения ответов в виде асинхронного генератора.

## Обзор

Модуль RubiksAI предоставляет возможность взаимодействия с API Rubiks AI для генерации текста на основе предоставленных сообщений. Поддерживается стриминг ответов, использование системных сообщений и истории сообщений.

## Подробнее

Этот модуль позволяет использовать различные модели Rubiks AI, такие как gpt-4o-mini, gpt-4o, o1-mini и другие, для генерации текста на основе заданных запросов. Он также поддерживает использование прокси-серверов и веб-поиска для улучшения качества ответов.

## Классы

### `RubiksAI`

**Описание**: Класс для взаимодействия с API Rubiks AI.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("Rubiks AI").
- `url` (str): URL провайдера ("https://rubiks.ai").
- `api_endpoint` (str): URL API ("https://rubiks.ai/search/api/").
- `working` (bool): Указывает, работает ли провайдер (True).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель по умолчанию ('gpt-4o-mini').
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `generate_mid()`: Генерирует строку 'mid'.
- `create_referer()`: Создает URL Referer.
- `create_async_generator()`: Создает асинхронный генератор для отправки запросов к API Rubiks AI.

### `generate_mid`

```python
    @staticmethod
    def generate_mid() -> str:
        """
        Generates a 'mid' string following the pattern:
        6 characters - 4 characters - 4 characters - 4 characters - 12 characters
        Example: 0r7v7b-quw4-kdy3-rvdu-ekief6xbuuq4
        """
```

**Назначение**: Генерирует строку `mid` в формате `6 символов - 4 символа - 4 символа - 4 символа - 12 символов`.

**Как работает функция**:

1.  **Инициализация**: Определяется функция `generate_mid` без аргументов.
2.  **Создание частей**: Создаются пять частей строки, каждая из которых состоит из случайных строчных букв ASCII и цифр.
    *   Первая часть: 6 символов.
    *   Вторая часть: 4 символа.
    *   Третья часть: 4 символа.
    *   Четвертая часть: 4 символа.
    *   Пятая часть: 12 символов.
3.  **Объединение частей**: Части объединяются с использованием дефиса (-) в качестве разделителя.
4.  **Возврат результата**: Функция возвращает полученную строку.

```
    Инициализация
    ↓
    Создание частей строки:
    ├── Первая часть (6 символов)
    ├── Вторая часть (4 символа)
    ├── Третья часть (4 символа)
    ├── Четвертая часть (4 символа)
    └── Пятая часть (12 символов)
    ↓
    Объединение частей с дефисом
    ↓
    Возврат строки
```

**Примеры**:
```python
    mid = RubiksAI.generate_mid()
    print(mid)  # Например: 0r7v7b-quw4-kdy3-rvdu-ekief6xbuuq4
```

### `create_referer`

```python
    @staticmethod
    def create_referer(q: str, mid: str, model: str = '') -> str:
        """
        Creates a Referer URL with dynamic q and mid values, using urlencode for safe parameter encoding.
        """
```

**Назначение**: Создает URL Referer с динамическими значениями `q` (поисковый запрос), `mid` и `model`, используя `urlencode` для безопасного кодирования параметров.

**Параметры**:
- `q` (str): Поисковый запрос.
- `mid` (str): Идентификатор.
- `model` (str, optional): Модель. По умолчанию ''.

**Возвращает**:
- `str`: URL Referer.

**Как работает функция**:

1.  **Инициализация**: Функция `create_referer` принимает параметры `q`, `mid` и `model`.
2.  **Создание словаря параметров**: Создается словарь с параметрами `q`, `model` и `mid`.
3.  **Кодирование параметров**: Параметры кодируются с использованием `urlencode`.
4.  **Формирование URL**: Формируется URL Referer с закодированными параметрами.
5.  **Возврат URL**: Функция возвращает полученный URL.

```
    Инициализация
    ↓
    Создание словаря параметров
    ↓
    Кодирование параметров с urlencode
    ↓
    Формирование URL
    ↓
    Возврат URL
```

**Примеры**:
```python
    referer = RubiksAI.create_referer(q='test query', mid='test_mid', model='gpt-4o-mini')
    print(referer)  # Например: https://rubiks.ai/search/?q=test+query&model=gpt-4o-mini&mid=test_mid
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        web_search: bool = False,
        temperature: float = 0.6,
        **kwargs
    ) -> AsyncResult:
        """
        Creates an asynchronous generator that sends requests to the Rubiks AI API and yields the response.

        Parameters:
        - model (str): The model to use in the request.
        - messages (Messages): The messages to send as a prompt.
        - proxy (str, optional): Proxy URL, if needed.
        - web_search (bool, optional): Indicates whether to include search sources in the response. Defaults to False.
        """
```

**Назначение**: Создает асинхронный генератор, который отправляет запросы к API Rubiks AI и возвращает ответ.

**Параметры**:
- `model` (str): Модель для использования в запросе.
- `messages` (Messages): Сообщения для отправки в качестве запроса.
- `proxy` (str, optional): URL прокси-сервера, если необходимо.
- `web_search` (bool, optional): Указывает, следует ли включать источники поиска в ответ. По умолчанию `False`.
- `temperature` (float): Температура модели.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текст от API.

**Как работает функция**:

1.  **Инициализация**: Функция `create_async_generator` принимает параметры `model`, `messages`, `proxy`, `web_search` и `temperature`.
2.  **Подготовка данных**:
    *   Получает модель, используя `cls.get_model(model)`.
    *   Генерирует `mid_value` с помощью `cls.generate_mid()`.
    *   Создает `referer` с помощью `cls.create_referer()`.
    *   Формирует словарь `data` с сообщениями, моделью, параметрами поиска, потоковой передачей и температурой.
    *   Формирует словарь `headers` с необходимыми заголовками, включая `Referer`.
3.  **Отправка запроса**:
    *   Использует `ClientSession` для отправки асинхронного POST-запроса к `cls.api_endpoint` с заголовками, данными и прокси.
    *   Вызывает `raise_for_status(response)` для проверки статуса ответа.
4.  **Обработка ответа**:
    *   Итерируется по строкам в содержимом ответа.
    *   Декодирует каждую строку и удаляет лишние пробелы.
    *   Проверяет, начинается ли строка с `'data: '`.
    *   Извлекает данные из строки.
    *   Проверяет, являются ли данные `'[DONE]'` или `'{"done": ""}'`, чтобы завершить итерацию.
    *   Пытается загрузить данные JSON.
    *   Если обнаружены URL и заголовок, добавляет их в список `sources`, если `web_search` включен.
    *   Если обнаружены варианты выбора (`choices`), извлекает содержимое (`content`) из каждого варианта и возвращает его с помощью `yield`.
5.  **Обработка источников (sources)**:
    *   Если `web_search` включен и есть источники, возвращает объект `Sources` с источниками.

```
    Инициализация
    ↓
    Подготовка данных:
    ├── Получение модели
    ├── Генерация mid_value
    ├── Создание referer
    ├── Формирование словаря data
    └── Формирование словаря headers
    ↓
    Отправка запроса
    ↓
    Обработка ответа:
    ├── Итерация по строкам ответа
    ├── Декодирование строки
    ├── Проверка префикса 'data: '
    ├── Извлечение данных
    ├── Проверка на завершение
    ├── Загрузка JSON
    ├── Обработка URL и заголовка (если web_search)
    └── Извлечение и возврат содержимого из choices
    ↓
    Обработка источников (если web_search и sources)
```

**Примеры**:

```python
    async def example():
        messages = [{"role": "user", "content": "Tell me a joke."}]
        async for chunk in RubiksAI.create_async_generator(model='gpt-4o-mini', messages=messages):
            print(chunk, end="")

    import asyncio
    asyncio.run(example())