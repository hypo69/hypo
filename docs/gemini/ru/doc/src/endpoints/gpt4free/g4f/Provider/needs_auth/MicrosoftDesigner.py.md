# Модуль MicrosoftDesigner

## Обзор

Модуль `MicrosoftDesigner` предоставляет асинхронный интерфейс для взаимодействия с Microsoft Designer API для генерации изображений на основе текстовых запросов. Он включает в себя функциональность для получения токена доступа, отправки запросов на создание изображений и обработки ответов.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими генерации изображений через Microsoft Designer. Он использует `aiohttp` для асинхронных HTTP-запросов и включает механизмы для повторных попыток и обработки ошибок. Модуль также поддерживает использование прокси-серверов и предоставляет возможность указания размера изображений.

## Классы

### `MicrosoftDesigner`

**Описание**: Класс `MicrosoftDesigner` является асинхронным провайдером для генерации изображений через Microsoft Designer API.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы и атрибуты для моделей провайдеров.

**Атрибуты**:
- `label` (str): Метка провайдера ("Microsoft Designer").
- `url` (str): URL Microsoft Designer ("https://designer.microsoft.com").
- `working` (bool): Указывает, что провайдер в рабочем состоянии (`True`).
- `use_nodriver` (bool): Указывает на использование без драйвера (`True`).
- `needs_auth` (bool): Указывает на необходимость аутентификации (`True`).
- `default_image_model` (str): Модель изображения по умолчанию ("dall-e-3").
- `image_models` (list[str]): Список поддерживаемых моделей изображений, включая размеры ("dall-e-3", "1024x1024", "1024x1792", "1792x1024").
- `models` (list[str]): Псевдоним `image_models`.

**Методы**:

- `create_async_generator(model: str, messages: Messages, prompt: str = None, proxy: str = None, **kwargs) -> AsyncResult`
- `generate(prompt: str, image_size: str, proxy: str = None) -> ImageResponse`

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        prompt: str = None,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для генерации изображений.

        Args:
            model (str): Модель для генерации изображений.
            messages (Messages): Сообщения для генерации изображения.
            prompt (str, optional): Дополнительный запрос. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.

        Returns:
            AsyncResult: Асинхронный генератор изображений.

        Как работает функция:
        1. Определяется размер изображения на основе выбранной модели.
        2. Вызывается метод `generate` для генерации изображения.
        3. Результат возвращается как асинхронный генератор.

        Схема работы функции:

        Определение размера изображения
        │
        ├───>  Вызов метода generate для генерации изображения
        │
        └───>  Возврат результата в виде асинхронного генератора

        """
        image_size = "1024x1024"
        if model != cls.default_image_model and model in cls.image_models:
            image_size = model
        yield await cls.generate(format_image_prompt(messages, prompt), image_size, proxy)
```
**Примеры**:
```python
# Пример вызова функции
async for image in MicrosoftDesigner.create_async_generator(model="dall-e-3", messages=[{"role": "user", "content": "a cat"}], prompt="high quality"):
    print(image)
```

### `generate`

```python
    @classmethod
    async def generate(cls, prompt: str, image_size: str, proxy: str = None) -> ImageResponse:
        """Генерирует изображение на основе заданного запроса.

        Args:
            prompt (str): Текстовый запрос для генерации изображения.
            image_size (str): Размер изображения.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.

        Returns:
            ImageResponse: Ответ, содержащий сгенерированные изображения.

        Raises:
            NoValidHarFileError: Если не найден валидный HAR-файл.

        Как работает функция:
        1. Пытается прочитать токен доступа и User-Agent из HAR-файла.
        2. Если HAR-файл не найден или не содержит токен доступа, пытается получить их через `get_access_token_and_user_agent`.
        3. Вызывает `create_images` для генерации изображений.
        4. Возвращает `ImageResponse` с сгенерированными изображениями.

        Схема работы функции:

        Попытка чтения токена доступа и User-Agent из HAR-файла
        │
        ├───> Если HAR-файл не найден ИЛИ не содержит токен доступа
        │       └───> Попытка получения токена доступа и User-Agent через get_access_token_and_user_agent
        │
        └───> Вызов create_images для генерации изображений
        │
        └───> Возврат ImageResponse с сгенерированными изображениями

        """
        try:
            access_token, user_agent = readHAR("https://designerapp.officeapps.live.com")
        except NoValidHarFileError as h:
            debug.log(f"{cls.__name__}: {h}")
            try:
                access_token, user_agent = await get_access_token_and_user_agent(cls.url, proxy)
            except MissingRequirementsError:
                raise h
        images = await create_images(prompt, access_token, user_agent, image_size, proxy)
        return ImageResponse(images, prompt)
```
**Примеры**:
```python
# Пример вызова функции
image_response = await MicrosoftDesigner.generate(prompt="a cat", image_size="1024x1024")
print(image_response)
```

## Функции

### `create_images`

```python
async def create_images(prompt: str, access_token: str, user_agent: str, image_size: str, proxy: str = None, seed: int = None):
    """Создает изображения на основе заданного запроса, используя Microsoft Designer API.

    Args:
        prompt (str): Текстовый запрос для генерации изображения.
        access_token (str): Токен доступа для аутентификации.
        user_agent (str): User-Agent для HTTP-запросов.
        image_size (str): Размер изображения.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.

    Returns:
        list[str]: Список URL сгенерированных изображений.

    Как работает функция:
    1. Формирует URL для запроса к Microsoft Designer API.
    2. Если `seed` не задан, генерирует случайное число.
    3. Формирует заголовки запроса, включая `User-Agent`, токен доступа и другие необходимые параметры.
    4. Создает `FormData` с данными запроса, включая запрос, размер изображения и seed.
    5. Отправляет POST-запрос к API и получает ответ.
    6. Извлекает URL изображений из ответа и возвращает их.

    Схема работы функции:
    Формирование URL запроса
    │
    ├───>  Генерация случайного числа, если seed не задан
    │
    ├───>  Формирование заголовков запроса
    │
    ├───>  Создание FormData с данными запроса
    │
    ├───>  Отправка POST-запроса к API
    │
    └───>  Извлечение URL изображений из ответа и возврат их
    """
```
**Примеры**:
```python
# Пример вызова функции
images = await create_images(prompt="a cat", access_token="token", user_agent="agent", image_size="1024x1024")
print(images)
```

### `readHAR`

```python
def readHAR(url: str) -> tuple[str, str]:
    """Читает HAR-файлы для извлечения токена доступа и User-Agent.

    Args:
        url (str): URL для поиска в HAR-файлах.

    Returns:
        tuple[str, str]: Токен доступа и User-Agent.

    Raises:
        NoValidHarFileError: Если не найден валидный HAR-файл с токеном доступа.

    Как работает функция:
    1. Получает список HAR-файлов.
    2. Перебирает HAR-файлы и пытается загрузить каждый как JSON.
    3. Ищет записи, URL которых начинается с заданного.
    4. Извлекает токен доступа и User-Agent из заголовков запроса.
    5. Если токен доступа не найден, вызывает исключение `NoValidHarFileError`.

    Схема работы функции:

    Получение списка HAR-файлов
    │
    ├───>  Перебор HAR-файлов
    │       └───>  Загрузка HAR-файла как JSON
    │       └───>  Поиск записей, URL которых начинается с заданного
    │       └───>  Извлечение токена доступа и User-Agent из заголовков запроса
    │
    └───>  Если токен доступа не найден, вызов исключения NoValidHarFileError
    """
```
**Примеры**:
```python
# Пример вызова функции
try:
    access_token, user_agent = readHAR("https://designerapp.officeapps.live.com")
    print(f"Access Token: {access_token}")
    print(f"User Agent: {user_agent}")
except NoValidHarFileError as ex:
    print(f"Error: {ex}")
```

### `get_access_token_and_user_agent`

```python
async def get_access_token_and_user_agent(url: str, proxy: str = None):
    """Получает токен доступа и User-Agent, используя playwright.

    Args:
        url (str): URL для получения токена доступа и User-Agent.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.

    Returns:
        tuple[str, str]: Токен доступа и User-Agent.

    Как работает функция:
    1. Запускает браузер с помощью `get_nodriver`.
    2. Открывает страницу по заданному URL.
    3. Получает User-Agent из браузера.
    4. Ожидает появления токена доступа в localStorage.
    5. Извлекает токен доступа из localStorage.
    6. Закрывает страницу и останавливает браузер.

    Схема работы функции:
    Запуск браузера
    │
    ├───>  Открытие страницы по заданному URL
    │
    ├───>  Получение User-Agent из браузера
    │
    ├───>  Ожидание появления токена доступа в localStorage
    │
    ├───>  Извлечение токена доступа из localStorage
    │
    └───>  Закрытие страницы и остановка браузера
    """
```

**Примеры**:
```python
# Пример вызова функции
access_token, user_agent = await get_access_token_and_user_agent(url="https://designer.microsoft.com")
print(f"Access Token: {access_token}")
print(f"User Agent: {user_agent}")