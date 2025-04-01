# Модуль BingCreateImages

## Обзор

Модуль `BingCreateImages.py` предоставляет класс `BingCreateImages`, который позволяет генерировать изображения с использованием Microsoft Designer в Bing. Он предназначен для асинхронного создания изображений на основе текстового запроса (prompt). Модуль использует cookies для аутентификации и может работать через прокси-сервер.
В проекте `hypotez` данный модуль используется для интеграции с сервисом Bing Image Creator, позволяя пользователям генерировать изображения на основе текстовых запросов. Расположен в `src/endpoints/gpt4free/g4f/Provider/needs_auth`, что указывает на его роль как провайдера изображений, требующего аутентификации.

## Подробней

Этот модуль предоставляет функциональность для работы с Microsoft Designer в Bing для создания изображений на основе текстовых запросов. Он включает в себя:
- Асинхронную генерацию изображений с использованием Bing Image Creator.
- Поддержку cookies для аутентификации.
- Возможность использования прокси-сервера.
- Форматирование запросов для генерации изображений.
- Обработку ошибок аутентификации.

## Классы

### `BingCreateImages`

**Описание**: Класс `BingCreateImages` является асинхронным генератором изображений с использованием Microsoft Designer в Bing.
Он наследует функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общую функциональность для моделей провайдеров.

**Аттрибуты**:
- `label` (str): Метка провайдера ("Microsoft Designer in Bing").
- `url` (str): URL для создания изображений ("https://www.bing.com/images/create").
- `working` (bool): Указывает, что провайдер рабочий (True).
- `needs_auth` (bool): Указывает, что требуется аутентификация (True).
- `image_models` (List[str]): Список поддерживаемых моделей изображений (["dall-e-3"]).
- `models` (List[str]): Псевдоним для `image_models`.
- `cookies` (Optional[Cookies]): Cookies для аутентификации.
- `proxy` (Optional[str]): Прокси-сервер для использования.

**Методы**:
- `__init__(cookies: Cookies = None, proxy: str = None, api_key: str = None) -> None`: Инициализирует экземпляр класса `BingCreateImages`.
- `create_async_generator(model: str, messages: Messages, prompt: str = None, api_key: str = None, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для создания изображений.
- `generate(prompt: str) -> ImageResponse`: Асинхронно генерирует изображение на основе запроса.

## Функции

### `__init__`

```python
def __init__(self, cookies: Cookies = None, proxy: str = None, api_key: str = None) -> None:
    """Инициализирует экземпляр класса `BingCreateImages`.

    Args:
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.

    Returns:
        None

    """
```

**Назначение**: Инициализирует экземпляр класса `BingCreateImages`. Если передан `api_key`, он добавляется в cookies.

**Параметры**:
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.

**Как работает функция**:
1. Проверяет, передан ли `api_key`. Если да, то добавляет его в cookies под ключом "_U".
2. Сохраняет переданные `cookies` и `proxy` в атрибуты экземпляра класса.

**Примеры**:
```python
# Пример 1: Создание экземпляра класса без cookies и proxy
bing_images = BingCreateImages()

# Пример 2: Создание экземпляра класса с cookies и proxy
cookies = {"_U": "some_api_key"}
bing_images = BingCreateImages(cookies=cookies, proxy="http://proxy.example.com")

# Пример 3: Создание экземпляра класса с api_key
bing_images = BingCreateImages(api_key="some_api_key")
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    prompt: str = None,
    api_key: str = None,
    cookies: Cookies = None,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для создания изображений.

    Args:
        model (str): Модель для генерации изображений.
        messages (Messages): Список сообщений для генерации запроса.
        prompt (str, optional): Дополнительный запрос для генерации изображений. По умолчанию `None`.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор для создания изображений.

    """
```

**Назначение**: Создает асинхронный генератор для создания изображений на основе предоставленных параметров.

**Параметры**:
- `cls` (BingCreateImages): Ссылка на класс `BingCreateImages`.
- `model` (str): Модель для генерации изображений.
- `messages` (Messages): Список сообщений для генерации запроса.
- `prompt` (str, optional): Дополнительный запрос для генерации изображений. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для создания изображений.

**Как работает функция**:
1. Создает экземпляр класса `BingCreateImages` с переданными cookies, proxy и api_key.
2. Форматирует запрос для генерации изображений с использованием `format_image_prompt`.
3. Возвращает асинхронный генератор, который генерирует изображения на основе запроса.

**Примеры**:
```python
# Пример 1: Создание асинхронного генератора с использованием model и messages
messages = [{"role": "user", "content": "generate image of cat"}]
async_generator = BingCreateImages.create_async_generator(model="dall-e-3", messages=messages)

# Пример 2: Создание асинхронного генератора с использованием model, messages и prompt
messages = [{"role": "user", "content": "generate image"}]
async_generator = BingCreateImages.create_async_generator(model="dall-e-3", messages=messages, prompt="of cat")
```

### `generate`

```python
async def generate(self, prompt: str) -> ImageResponse:
    """
    Асинхронно создает markdown-форматированную строку с изображениями на основе запроса.

    Args:
        prompt (str): Prompt для генерации изображений.

    Returns:
        ImageResponse: Объект `ImageResponse` с изображениями.

    Raises:
        MissingAuthError: Если отсутствует cookie "_U".
    """
```

**Назначение**: Асинхронно генерирует изображение на основе запроса (prompt).

**Параметры**:
- `prompt` (str): Запрос для генерации изображений.

**Возвращает**:
- `ImageResponse`: Объект `ImageResponse` с изображениями.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствует cookie "_U".

**Как работает функция**:
1. Получает cookies из домена ".bing.com".
2. Проверяет наличие cookie "_U" в cookies. Если отсутствует, вызывает исключение `MissingAuthError`.
3. Создает асинхронную сессию с использованием `create_session`.
4. Генерирует изображения с использованием `create_images`.
5. Возвращает объект `ImageResponse` с изображениями и информацией о предпросмотре.

```
Получение cookies   Проверка наличия "_U"   Создание асинхронной сессии   Генерация изображений   Формирование ответа ImageResponse
--------------------  -----------------------  ------------------------------  ------------------------  --------------------------------------
      cookies            "_U" in cookies?              async with create_session        images = await create_images         return ImageResponse
                                                                  |
                                                                  V
                                                      MissingAuthError (если нет "_U")
```

**Примеры**:
```python
# Пример 1: Генерация изображения с использованием prompt
bing_images = BingCreateImages(cookies={"_U": "some_api_key"})
image_response = await bing_images.generate(prompt="image of cat")

# Пример 2: Обработка ошибки аутентификации
bing_images = BingCreateImages()
try:
    image_response = await bing_images.generate(prompt="image of cat")
except MissingAuthError as ex:
    print(f"Ошибка аутентификации: {ex}")