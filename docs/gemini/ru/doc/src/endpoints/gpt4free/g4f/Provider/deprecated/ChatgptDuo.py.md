# Модуль ChatgptDuo
## Обзор
Модуль `ChatgptDuo` предоставляет асинхронный класс `ChatgptDuo`, который является провайдером для взаимодействия с моделью `gpt-3.5-turbo` через сайт `chatgptduo.com`. Он позволяет отправлять запросы к модели и получать ответы.

## Подорбней

Этот модуль является частью набора провайдеров в проекте `hypotez`, предназначенных для работы с различными сервисами, предоставляющими доступ к языковым моделям. `ChatgptDuo` предоставляет асинхронный интерфейс для взаимодействия с `chatgptduo.com`. Он использует `StreamSession` для выполнения HTTP-запросов и форматирует сообщения для отправки. Данный модуль deprecated, это значит что он устарел и скорее всего не поддерживается

## Классы

### `ChatgptDuo`

**Описание**: Асинхронный провайдер для взаимодействия с моделью `gpt-3.5-turbo` через сайт `chatgptduo.com`.

**Принцип работы**:
Класс `ChatgptDuo` наследуется от `AsyncProvider` и переопределяет метод `create_async` для отправки запросов к API `chatgptduo.com`. Он также имеет метод `get_sources` для получения источников, используемых для формирования ответа.

**Методы**:
- `create_async`: Асинхронный метод для создания запроса к модели и получения ответа.
- `get_sources`: Метод для получения источников, использованных при формировании ответа.

**Параметры**:
- `url` (str): URL сайта `chatgptduo.com`.
- `supports_gpt_35_turbo` (bool): Поддержка модели `gpt-3.5-turbo`.
- `working` (bool): Статус работоспособности провайдера.

## Функции

### `create_async`

```python
    async def create_async(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        timeout: int = 120,
        **kwargs
    ) -> str:
        """
        Асинхронно создает запрос к модели и возвращает ответ.

        Args:
            cls (type[ChatgptDuo]): Класс `ChatgptDuo`.
            model (str): Название модели (не используется в данной реализации).
            messages (Messages): Список сообщений для отправки в запросе.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            timeout (int, optional): Максимальное время ожидания ответа в секундах. По умолчанию `120`.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            str: Ответ от модели.

        Raises:
            Exception: Если возникает ошибка при выполнении запроса.

        Как работает функция:
        1. Инициализирует асинхронную сессию `StreamSession` с параметрами `impersonate="chrome107"`, `proxies` и `timeout`.
        2. Форматирует список сообщений `messages` с помощью функции `format_prompt`.
        3. Подготавливает данные для отправки в запросе, включая `prompt`, `search` и `purpose`.
        4. Отправляет POST-запрос к `f"{cls.url}/"` с подготовленными данными.
        5. Проверяет статус ответа и вызывает исключение в случае ошибки.
        6. Извлекает JSON из ответа.
        7. Извлекает источники из ответа и сохраняет их в `cls._sources`.
        8. Возвращает ответ от модели.

        Внутри функции происходят следующие действия и преобразования:
            A. Инициализация асинхронной сессии с заданными параметрами.
            |
            -- B. Форматирование списка сообщений в строку.
            |
            C. Подготовка данных для отправки в запросе.
            |
            D - E. Отправка POST-запроса и проверка статуса ответа.
            |
            F. Извлечение JSON из ответа и извлечение источников.
            |
            G. Возврат ответа от модели.

        Где:
            Инициализация сессии: Создание и настройка асинхронной сессии для выполнения HTTP-запросов.
            Форматирование сообщений: Преобразование списка сообщений в строку, пригодную для отправки в запросе.
            Подготовка данных: Формирование словаря с данными, необходимыми для отправки в запросе.
            Отправка запроса: Отправка POST-запроса к API и проверка статуса ответа.
            Извлечение JSON: Разбор JSON-ответа от API.
            Извлечение источников: Извлечение списка источников, использованных для формирования ответа.
            Возврат ответа: Возврат ответа от модели.

        Примеры:
            Пример 1:
            ```python
            messages = [{"role": "user", "content": "Hello"}
            await ChatgptDuo.create_async(model="gpt-3.5-turbo", messages=messages)
            ```

            Пример 2 (с использованием прокси):
            ```python
            messages = [{"role": "user", "content": "Hello"}
            await ChatgptDuo.create_async(model="gpt-3.5-turbo", messages=messages, proxy="http://proxy.example.com")
            ```

            Пример 3 (с указанием времени ожидания):
            ```python
            messages = [{"role": "user", "content": "Hello"}
            await ChatgptDuo.create_async(model="gpt-3.5-turbo", messages=messages, timeout=60)
            ```
        """
        async with StreamSession(
            impersonate="chrome107",
            proxies={"https": proxy},
            timeout=timeout
        ) as session:
            prompt = format_prompt(messages),\
            data = {
                "prompt": prompt,
                "search": prompt,
                "purpose": "ask",
            }
            response = await session.post(f"{cls.url}/", data=data)
            response.raise_for_status()
            data = response.json()

            cls._sources = [{
                "title": source["title"],
                "url": source["link"],
                "snippet": source["snippet"]
            } for source in data["results"]]

            return data["answer"]
```

### `get_sources`

```python
    @classmethod
    def get_sources(cls):
        """
        Возвращает источники, использованные при формировании ответа.

        Args:
            cls (type[ChatgptDuo]): Класс `ChatgptDuo`.

        Returns:
            list[dict]: Список словарей с информацией об источниках.

        Как работает функция:
        1. Возвращает значение атрибута `cls._sources`, который содержит список источников.

        Внутри функции происходит следующее действие:
            A. Возврат списка источников.

        Где:
            Возврат списка: Функция возвращает список словарей, содержащих информацию об источниках.

        Примеры:
            Пример 1:
            ```python
            sources = ChatgptDuo.get_sources()
            print(sources)
            ```
        """
        return cls._sources