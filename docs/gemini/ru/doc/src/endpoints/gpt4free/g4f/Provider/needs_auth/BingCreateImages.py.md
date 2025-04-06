# Модуль BingCreateImages

## Обзор

Модуль `BingCreateImages` предназначен для создания изображений с использованием Microsoft Designer в Bing. Он предоставляет асинхронный генератор для получения изображений на основе текстового запроса. Модуль требует аутентификации через cookie `_U`.

## Подробнее

Модуль является частью проекта `hypotez` и интегрируется с другими компонентами для обеспечения функциональности генерации изображений. Он использует асинхронные операции для эффективной работы и предоставляет возможность указания прокси-сервера.
Расположен в `hypotez/src/endpoints/gpt4free/g4f/Provider/needs_auth/BingCreateImages.py` и служит для создания изображений через API Bing.
Модуль `BingCreateImages` отвечает за генерацию изображений через сервис Microsoft Designer в Bing, требующий аутентификации. 
Он использует cookies для аутентификации и предоставляет асинхронные методы для генерации изображений на основе заданного запроса.

## Классы

### `BingCreateImages`

**Описание**: Класс для создания изображений с использованием Microsoft Designer в Bing.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Аттрибуты**:
- `label` (str): Метка провайдера ("Microsoft Designer in Bing").
- `url` (str): URL для Bing Image Creator ("https://www.bing.com/images/create").
- `working` (bool): Указывает, работает ли провайдер (True).
- `needs_auth` (bool): Указывает, требуется ли аутентификация (True).
- `image_models` (List[str]): Список поддерживаемых моделей изображений (["dall-e-3"]).
- `models` (List[str]): Псевдоним для `image_models`.
- `cookies` (Optional[Cookies]): Cookie для аутентификации.
- `proxy` (Optional[str]): Адрес прокси-сервера.

**Методы**:
- `__init__(cookies: Cookies = None, proxy: str = None, api_key: str = None) -> None`: Инициализирует экземпляр класса.
- `create_async_generator(model: str, messages: Messages, prompt: str = None, api_key: str = None, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncResult`: Создает асинхронный генератор для получения изображений.
- `generate(prompt: str) -> ImageResponse`: Асинхронно генерирует изображения на основе запроса.

### `__init__`

```python
def __init__(self, cookies: Cookies = None, proxy: str = None, api_key: str = None) -> None:
    """
    Инициализирует экземпляр класса BingCreateImages.

    Args:
        cookies (Optional[Cookies]): Cookie для аутентификации.
        proxy (Optional[str]): Адрес прокси-сервера.
        api_key (Optional[str]): API ключ для аутентификации.
    """
```

**Параметры**:
- `cookies` (Optional[Cookies]): Cookie для аутентификации. Если не указан, будет использован `api_key`.
- `proxy` (Optional[str]): Адрес прокси-сервера.
- `api_key` (Optional[str]): API ключ для аутентификации через cookie `_U`.

**Как работает**:
1. Если передан `api_key`, он используется для установки cookie `_U`.
2. Сохраняет переданные `cookies` и `proxy` в атрибуты экземпляра класса.

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
    Создает асинхронный генератор для получения изображений.

    Args:
        model (str): Модель для генерации изображений.
        messages (Messages): Сообщения для формирования запроса.
        prompt (Optional[str]): Текст запроса.
        api_key (Optional[str]): API ключ для аутентификации.
        cookies (Optional[Cookies]): Cookie для аутентификации.
        proxy (Optional[str]): Адрес прокси-сервера.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий изображения.
    """
```

**Параметры**:
- `model` (str): Модель для генерации изображений.
- `messages` (Messages): Список сообщений для формирования запроса.
- `prompt` (Optional[str]): Текст запроса.
- `api_key` (Optional[str]): API ключ для аутентификации.
- `cookies` (Optional[Cookies]): Cookie для аутентификации.
- `proxy` (Optional[str]): Адрес прокси-сервера.
- `**kwargs`: Дополнительные параметры.

**Как работает**:
1. Создает экземпляр класса `BingCreateImages`, передавая `cookies`, `proxy` и `api_key`.
2. Форматирует запрос изображения с использованием `format_image_prompt`.
3. Возвращает асинхронный генератор, который при итерации вызывает метод `generate` для получения изображений.

**ASCII схема работы функции**:

```
Начало
  ↓
Создание экземпляра BingCreateImages
  ↓
Форматирование запроса format_image_prompt
  ↓
Вызов session.generate
  ↓
Конец (AsyncResult)
```

### `generate`

```python
async def generate(self, prompt: str) -> ImageResponse:
    """
    Асинхронно создает markdown-форматированную строку с изображениями на основе запроса.

    Args:
        prompt (str): Prompt для генерации изображений.

    Returns:
        ImageResponse: Объект ImageResponse с изображениями.

    Raises:
        MissingAuthError: Если отсутствует cookie "_U".
    """
```

**Параметры**:
- `prompt` (str): Текст запроса для генерации изображений.

**Возвращает**:
- `ImageResponse`: Объект `ImageResponse`, содержащий сгенерированные изображения и метаданные.

**Вызывает исключения**:
- `MissingAuthError`: Если отсутствует cookie `_U`, необходимый для аутентификации.

**Как работает**:
1. Проверяет наличие cookie `_U` в cookies. Если cookie отсутствует, вызывает исключение `MissingAuthError`.
2. Открывает асинхронную сессию с использованием `create_session`.
3. Генерирует изображения с использованием `create_images`.
4. Возвращает объект `ImageResponse`, содержащий сгенерированные изображения и URL для предпросмотра.

**ASCII схема работы функции**:

```
Начало
  ↓
Проверка наличия cookie "_U"
  ↓
Создание асинхронной сессии create_session
  ↓
Генерация изображений create_images
  ↓
Создание ImageResponse
  ↓
Конец (ImageResponse)
```

## Функции

В данном модуле функции отсутствуют.

## Примеры

### Инициализация класса

```python
from typing import Dict, Optional

# Пример использования с указанием cookies
cookies: Dict[str, str] = {"_U": "some_cookie_value"}
bing_images = BingCreateImages(cookies=cookies)

# Пример использования с указанием API ключа
bing_images = BingCreateImages(api_key="some_api_key")

# Пример использования с указанием прокси
bing_images = BingCreateImages(proxy="http://proxy_address:port")
```

### Создание асинхронного генератора

```python
import asyncio
from typing import List, Dict

# messages: List[Dict[str, str]]
# async def main():
#     generator = await BingCreateImages.create_async_generator(
#         model="dall-e-3",
#         messages=[{"role": "user", "content": "Generate an image of a cat."}],
#         api_key="some_api_key"
#     )
#     async for image_response in generator:
#         print(image_response)

# asyncio.run(main())
```

### Генерация изображений

```python
import asyncio

# async def main():
#     bing_images = BingCreateImages(api_key="some_api_key")
#     image_response = await bing_images.generate("Generate an image of a futuristic city.")
#     print(image_response)

# asyncio.run(main())