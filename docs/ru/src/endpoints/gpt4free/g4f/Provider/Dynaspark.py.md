# Модуль Dynaspark

## Обзор

Модуль `Dynaspark` предоставляет класс `Dynaspark`, который является асинхронным генератором для взаимодействия с API Dynaspark для генерации ответов на основе предоставленных сообщений и, опционально, медиа-файлов. Модуль поддерживает выбор модели, прокси и передачу изображений для обработки. Этот модуль позволяет использовать модели Gemini через API Dynaspark.

## Подробней

Модуль предназначен для асинхронного взаимодействия с сервисом Dynaspark для получения ответов на запросы, включая возможность передачи изображений. Он использует `aiohttp` для выполнения асинхронных HTTP-запросов и `FormData` для отправки данных, включая изображения.
Модуль `Dynaspark` реализует функциональность асинхронного генератора (`AsyncGeneratorProvider`) и поддерживает выбор модели, прокси и передачу медиафайлов.

## Классы

### `Dynaspark`

**Описание**: Класс `Dynaspark` является асинхронным провайдером, взаимодействующим с API Dynaspark для генерации ответов на основе текстовых сообщений и медиафайлов.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `url` (str): Базовый URL сервиса Dynaspark.
- `login_url` (Optional[str]): URL для логина (в данном случае `None`, так как аутентификация не требуется).
- `api_endpoint` (str): URL для отправки запросов на генерацию ответов.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `True`).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (в данном случае `False`).
- `use_nodriver` (bool): Флаг, указывающий на использование без драйвера (в данном случае `True`).
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи (в данном случае `True`).
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений (в данном случае `False`).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (в данном случае `False`).
- `default_model` (str): Модель, используемая по умолчанию (`gemini-1.5-flash`).
- `default_vision_model` (str): Модель для работы с изображениями, используемая по умолчанию (`gemini-1.5-flash`).
- `vision_models` (List[str]): Список поддерживаемых моделей для работы с изображениями.
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь с псевдонимами моделей, где ключ - это псевдоним, а значение - настоящее имя модели.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API Dynaspark.

## Функции

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        media: MediaListType = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для получения ответов от API Dynaspark.

        Args:
            model (str): Название модели для генерации ответа.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
            media (MediaListType, optional): Список медиафайлов для отправки в API. По умолчанию `None`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от API Dynaspark.

        Raises:
            Exception: В случае ошибок при выполнении запроса к API Dynaspark.
        """
```

**Назначение**: Метод `create_async_generator` создает асинхронный генератор, который отправляет запрос к API Dynaspark и возвращает сгенерированные ответы. Он формирует данные запроса, включая текстовые сообщения и медиафайлы (если они предоставлены), и отправляет их на указанный endpoint.

**Параметры**:
- `cls`: Ссылка на класс `Dynaspark`.
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений, используемых для генерации ответа.
- `proxy` (str, optional): Адрес прокси-сервера (если требуется). По умолчанию `None`.
- `media` (MediaListType, optional): Список медиафайлов для отправки (например, изображения). По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы (не используются в данной реализации).

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который возвращает текст ответа от API Dynaspark.

**Вызывает исключения**:
- `Exception`: Вызывается, если происходит ошибка при отправке запроса или обработке ответа от API Dynaspark.

**Как работает функция**:

1.  **Формирование заголовков**: Создаются HTTP-заголовки, включающие User-Agent, Referer и другие необходимые параметры.
2.  **Создание FormData**: Создается объект `FormData`, в который добавляются текстовые сообщения и, если есть, медиафайлы.
3.  **Отправка запроса**: Отправляется POST-запрос к API Dynaspark с использованием `aiohttp.ClientSession`.
4.  **Обработка ответа**: Полученный ответ преобразуется в текст и возвращается через асинхронный генератор.

```
Формирование заголовков и FormData -> Отправка POST-запроса в API Dynaspark -> Получение ответа -> Извлечение и выдача ответа через генератор
```

```
Начало
|
-- Формирование заголовков и FormData
|
Отправка POST-запроса в API Dynaspark
|
Получение ответа
|
Извлечение и выдача ответа через генератор
|
Конец
```

**Примеры**:

```python
import asyncio
from typing import List, Dict, AsyncGenerator

async def main():
    model = "gemini-1.5-flash"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Hello, Dynaspark!"}]

    async for response in Dynaspark.create_async_generator(model=model, messages=messages):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

```python
import asyncio
from typing import List, Dict
from pathlib import Path

async def main():
    model = "gemini-1.5-flash"
    messages: List[Dict[str, str]] = [{"role": "user", "content": "Describe this image."}]
    image_path = Path("path/to/your/image.jpg") #  <путь к изображению>
    
    #  <добавить обработку исключений если файл не существует>
    
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    media = [(image_data, image_path.name)]

    async for response in Dynaspark.create_async_generator(model=model, messages=messages, media=media):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())