# Модуль MetaAI

## Обзор

Модуль `MetaAI` предоставляет асинхронный интерфейс для взаимодействия с моделью Meta AI. Он включает в себя функциональность для получения доступа к модели, отправки запросов и обработки ответов, включая текстовые и графические данные. Модуль поддерживает обновление токенов доступа и куки для поддержания активной сессии.

## Подробнее

Модуль предназначен для интеграции с другими частями проекта `hypotez`, требующими доступа к возможностям Meta AI. Он обрабатывает детали аутентификации, формирования запросов и парсинга ответов, предоставляя высокоуровневый API для упрощения взаимодействия.

## Классы

### `Sources`

**Описание**: Класс представляет собой список источников, полученных от Meta AI, каждый из которых содержит заголовок и ссылку.

**Аттрибуты**:
- `list` (List[Dict[str, str]]): Список словарей, каждый из которых содержит информацию об источнике (`title` и `link`).

**Методы**:
- `__init__(self, link_list: List[Dict[str, str]]) -> None`: Инициализирует объект `Sources` списком источников.
- `__str__(self) -> str`: Возвращает строковое представление списка источников в формате Markdown.

### `AbraGeoBlockedError`

**Описание**: Класс исключения, который вызывается, когда Meta AI недоступна в текущей стране пользователя.

### `MetaAI`

**Описание**: Класс, реализующий асинхронное взаимодействие с Meta AI.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями провайдера.

**Аттрибуты**:
- `label` (str): Метка провайдера ("Meta AI").
- `url` (str): URL Meta AI ("https://www.meta.ai").
- `working` (bool): Указывает, работает ли провайдер (True).
- `default_model` (str): Модель по умолчанию ('meta-ai').
- `session` (ClientSession): Асинхронная HTTP-сессия для выполнения запросов.
- `cookies` (Cookies): Куки для аутентификации.
- `access_token` (str): Токен доступа для аутентификации.
- `lsd` (str): Значение `lsd` параметра, необходимого для запросов.
- `dtsg` (str): Значение `dtsg` параметра, необходимого для запросов.

**Методы**:

- `__init__(self, proxy: str = None, connector: BaseConnector = None)`
    ```python
    def __init__(self, proxy: str = None, connector: BaseConnector = None):
        """
        Инициализирует экземпляр класса `MetaAI`.

        Args:
            proxy (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
            connector (BaseConnector, optional): Пользовательский коннектор aiohttp. По умолчанию `None`.
        """
    ```

- `create_async_generator(cls, model: str, messages: Messages, proxy: str = None, **kwargs) -> AsyncResult`
    ```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для получения ответов от Meta AI.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Yields:
            AsyncResult: Часть ответа от Meta AI.
        """
    ```

- `update_access_token(self, birthday: str = "1999-01-01")`
    ```python
    async def update_access_token(self, birthday: str = "1999-01-01"):
        """
        Обновляет токен доступа для Meta AI.

        Args:
            birthday (str, optional): Дата рождения пользователя. По умолчанию "1999-01-01".

        Raises:
            ResponseError: Если запрос не удался.
        """
    ```

- `prompt(self, message: str, cookies: Cookies = None) -> AsyncResult`
    ```python
    async def prompt(self, message: str, cookies: Cookies = None) -> AsyncResult:
        """
        Отправляет запрос в Meta AI и возвращает асинхронный генератор ответа.

        Args:
            message (str): Текст сообщения для отправки.
            cookies (Cookies, optional): Куки для использования. По умолчанию `None`.

        Yields:
            AsyncResult: Часть ответа от Meta AI.

        Raises:
            ResponseError: Если произошла ошибка при получении ответа.
            RuntimeError: Если в ответе есть ошибки.
        """
    ```

- `update_cookies(self, cookies: Cookies = None)`
    ```python
    async def update_cookies(self, cookies: Cookies = None):
        """
        Обновляет куки для Meta AI.

        Args:
            cookies (Cookies, optional): Куки для обновления. По умолчанию `None`.

        Raises:
            AbraGeoBlockedError: Если Meta AI недоступна в текущей стране.
            ResponseError: Если запрос не удался.
        """
    ```

- `fetch_sources(self, fetch_id: str) -> Sources`
    ```python
    async def fetch_sources(self, fetch_id: str) -> Sources:
        """
        Получает источники для ответа Meta AI.

        Args:
            fetch_id (str): Идентификатор запроса.

        Returns:
            Sources: Список источников.

        Raises:
            ResponseError: Если запрос не удался.
            RuntimeError: Если в ответе есть ошибки.
        """
    ```

- `extract_value(text: str, key: str = None, start_str = None, end_str = ',"') -> str`
    ```python
    @staticmethod
    def extract_value(text: str, key: str = None, start_str = None, end_str = ',"') -> str:
        """
        Извлекает значение из текста на основе начальной и конечной строк.

        Args:
            text (str): Текст для извлечения значения.
            key (str, optional): Ключ для поиска начальной строки. По умолчанию `None`.
            start_str (str, optional): Начальная строка для поиска значения. По умолчанию `None`.
            end_str (str, optional): Конечная строка для поиска значения. По умолчанию ',"'.

        Returns:
            str: Извлеченное значение.
        """
    ```

## Функции

### `generate_offline_threading_id()`
```python
def generate_offline_threading_id() -> str:
    """
    Генерирует идентификатор для оффлайн-тредов.

    Returns:
        str: Сгенерированный идентификатор треда.
    """
```

**Назначение**:
Функция генерирует уникальный идентификатор для оффлайн-тредов, комбинируя текущее время в миллисекундах со случайным 64-битным числом.

**Возвращает**:
- `str`: Сгенерированный идентификатор треда.

**Как работает функция**:

1. **Генерация случайного значения**:
   - Генерируется случайное 64-битное целое число с помощью `random.getrandbits(64)`.

2. **Получение текущей временной метки**:
   - Получается текущее время в миллисекундах с помощью `time.time() * 1000` и преобразуется в целое число.

3. **Комбинирование временной метки и случайного значения**:
   - Временная метка сдвигается влево на 22 бита (`timestamp << 22`), а случайное значение обрезается до 22 бит (`random_value & ((1 << 22) - 1)`). Затем они объединяются с помощью побитовой операции OR.

4. **Преобразование в строку**:
   - Полученный идентификатор преобразуется в строку.

```
Генерация случайного числа (random_value)
|
Получение текущей временной метки (timestamp)
|
Сдвиг временной метки влево на 22 бита (timestamp << 22)
|
Обрезание случайного числа до 22 бит (random_value & ((1 << 22) - 1))
|
Объединение с помощью побитового OR
|
Преобразование в строку
```

**Примеры**:

```python
offline_id = generate_offline_threading_id()
print(f"Generated offline threading ID: {offline_id}")