# Модуль BingCreateImages

## Обзор

Модуль `BingCreateImages.py` предназначен для создания изображений с использованием Microsoft Designer через Bing. Он предоставляет асинхронный генератор изображений на основе текстового запроса. Этот модуль входит в подсистему `gpt4free` проекта `hypotez` и интегрируется с другими компонентами для обеспечения функциональности генерации изображений. Расположен в `hypotez/src/endpoints/gpt4free/g4f/Provider/needs_auth/BingCreateImages.py`. Для работы требуется авторизация через cookies.

## Подробнее

Модуль использует асинхронный подход для генерации изображений, что позволяет эффективно использовать ресурсы и обеспечивать неблокирующую работу. Он интегрируется с другими частями проекта, такими как `get_cookies` для получения cookies, `ImageResponse` для формирования ответа и `create_images` для фактического создания изображений.

## Классы

### `BingCreateImages`

**Описание**: Класс `BingCreateImages` является асинхронным генератором изображений, использующим Microsoft Designer в Bing. Он требует авторизации и предоставляет методы для генерации изображений на основе текстового запроса.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Аттрибуты**:
- `label` (str): Метка провайдера ("Microsoft Designer in Bing").
- `url` (str): URL для создания изображений ("https://www.bing.com/images/create").
- `working` (bool): Указывает, что провайдер работает (True).
- `needs_auth` (bool): Указывает, что требуется авторизация (True).
- `image_models` (List[str]): Список поддерживаемых моделей изображений (["dall-e-3"]).
- `models` (List[str]): Псевдоним для `image_models`.
- `cookies` (Cookies): Cookies для авторизации.
- `proxy` (str): Прокси-сервер для выполнения запросов.

**Методы**:
- `__init__(self, cookies: Cookies = None, proxy: str = None, api_key: str = None) -> None`: Инициализирует экземпляр класса `BingCreateImages`.
- `create_async_generator(cls, model: str, messages: Messages, prompt: str = None, api_key: str = None, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор изображений.
- `generate(self, prompt: str) -> ImageResponse`: Асинхронно создает markdown-форматированную строку с изображениями на основе запроса.

### `__init__`

```python
    def __init__(self, cookies: Cookies = None, proxy: str = None, api_key: str = None) -> None:
        """
        Инициализирует экземпляр класса `BingCreateImages`.
        
        Args:
            cookies (Cookies, optional): Cookies для авторизации. По умолчанию `None`.
            proxy (str, optional): Прокси-сервер для выполнения запросов. По умолчанию `None`.
            api_key (str, optional): API ключ для авторизации через cookie "_U". По умолчанию `None`.
        """
        ...
```

**Назначение**:
Инициализирует экземпляр класса `BingCreateImages`, устанавливая cookies, прокси и API ключ для дальнейшей работы с Bing Designer.

**Параметры**:
- `cookies` (Cookies, optional): Cookies для авторизации. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для выполнения запросов. По умолчанию `None`.
- `api_key` (str, optional): API ключ для авторизации через cookie "_U". По умолчанию `None`.

**Как работает функция**:
1. Проверяет наличие `api_key`. Если он предоставлен, то создает или обновляет словарь `cookies`, добавляя в него `api_key` под ключом "_U".
2. Сохраняет переданные значения `cookies` и `proxy` в атрибуты экземпляра класса для дальнейшего использования.

**Примеры**:

```python
# Пример 1: Инициализация без параметров
bing_images = BingCreateImages()

# Пример 2: Инициализация с cookies
cookies = {"_U": "some_api_key"}
bing_images = BingCreateImages(cookies=cookies)

# Пример 3: Инициализация с прокси и API ключом
bing_images = BingCreateImages(proxy="http://proxy.example.com", api_key="some_api_key")
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
        """
        Создает асинхронный генератор изображений.
        
        Args:
            model (str): Модель для генерации изображений.
            messages (Messages): Список сообщений для формирования запроса.
            prompt (str, optional): Дополнительный запрос. По умолчанию `None`.
            api_key (str, optional): API ключ для авторизации. По умолчанию `None`.
            cookies (Cookies, optional): Cookies для авторизации. По умолчанию `None`.
            proxy (str, optional): Прокси-сервер для выполнения запросов. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.
            
        Returns:
            AsyncResult: Асинхронный генератор изображений.
        """
        ...
```

**Назначение**:
Создает асинхронный генератор изображений на основе предоставленных параметров, таких как модель, сообщения, API-ключ, cookies и прокси.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Модель для генерации изображений.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (str, optional): Дополнительный запрос. По умолчанию `None`.
- `api_key` (str, optional): API ключ для авторизации. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для авторизации. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для выполнения запросов. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор изображений.

**Как работает функция**:
1. Создает экземпляр класса `BingCreateImages`, передавая cookies, proxy и api_key.
2. Генерирует изображение, используя метод `generate`, форматируя запрос с помощью `format_image_prompt`.
3. Возвращает асинхронный генератор, который выдает результат генерации изображения.

**Примеры**:

```python
# Пример создания асинхронного генератора
model = "dall-e-3"
messages = [{"role": "user", "content": "Generate an image of a cat"}]
async_generator = BingCreateImages.create_async_generator(model=model, messages=messages)
```

### `generate`

```python
    async def generate(self, prompt: str) -> ImageResponse:
        """
        Асинхронно создает markdown-форматированную строку с изображениями на основе запроса.

        Args:
            prompt (str): Prompt to generate images.

        Returns:
            ImageResponse: Объект `ImageResponse` с информацией об изображениях.

        Raises:
            MissingAuthError: Если отсутствует cookie "_U".
        """
        ...
```

**Назначение**:
Асинхронно создает markdown-форматированную строку с изображениями на основе предоставленного запроса.

**Параметры**:
- `prompt` (str): Запрос для генерации изображений.

**Возвращает**:
- `ImageResponse`: Объект `ImageResponse` с информацией об изображениях.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствует cookie "_U".

**Как работает функция**:
1. Пытается получить cookies из домена ".bing.com", если они не были переданы при инициализации класса.
2. Проверяет наличие cookie "_U", необходимого для авторизации. Если cookie отсутствует, выбрасывается исключение `MissingAuthError`.
3. Создает асинхронную сессию с использованием `create_session`, передавая cookies и proxy.
4. Генерирует изображения с помощью `create_images`, передавая асинхронную сессию и запрос.
5. Формирует объект `ImageResponse` с информацией об изображениях и возвращает его. `ImageResponse` включает в себя URL-ы сгенерированных изображений и запрос, на основе которого они были созданы. Кроме того, в `ImageResponse` добавляется словарь, который определяет параметры предварительного просмотра изображений (ширина и высота).

**Примеры**:

```python
# Пример генерации изображения
prompt = "A futuristic cityscape"
bing_images = BingCreateImages(cookies={"_U": "some_api_key"})
image_response = await bing_images.generate(prompt)
```

## Функции

В данном модуле функции отсутствуют.