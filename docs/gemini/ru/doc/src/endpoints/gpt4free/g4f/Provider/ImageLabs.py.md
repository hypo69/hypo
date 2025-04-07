# Модуль ImageLabs

## Обзор

Модуль `ImageLabs` предоставляет асинхронный генератор изображений на основе API ImageLabs. Он позволяет генерировать изображения по текстовому запросу, используя асинхронные запросы к API ImageLabs. Модуль поддерживает настройку размера изображения, негативные промпты и другие параметры генерации.

## Подробней

Этот модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется генерация изображений на основе текстовых описаний. Он использует асинхронный подход для неблокирующей работы и поддерживает прокси-серверы для обхода ограничений доступа.

## Классы

### `ImageLabs`

**Описание**: Класс `ImageLabs` является поставщиком асинхронного генератора изображений, использующим API ImageLabs. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса ImageLabs.
- `api_endpoint` (str): URL API для генерации изображений.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Указывает, поддерживает ли потоковую передачу данных.
- `supports_system_message` (bool): Указывает, поддерживает ли системные сообщения.
- `supports_message_history` (bool): Указывает, поддерживает ли историю сообщений.
- `default_model` (str): Модель, используемая по умолчанию (`sdxl-turbo`).
- `default_image_model` (str): Модель изображения, используемая по умолчанию.
- `image_models` (List[str]): Список поддерживаемых моделей изображений.
- `models` (List[str]): Псевдоним `image_models`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для генерации изображений.
- `get_model`: Возвращает модель по умолчанию.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    # Image
    prompt: str = None,
    negative_prompt: str = "",
    width: int = 1152,
    height: int = 896,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для генерации изображений на основе текстового запроса.

    Args:
        cls (Type[ImageLabs]): Класс ImageLabs.
        model (str): Модель для генерации изображений.
        messages (Messages): Список сообщений, содержащих текстовый запрос.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
        negative_prompt (str, optional): Негативный промпт, указывающий, что не должно быть на изображении. По умолчанию "".
        width (int, optional): Ширина изображения в пикселях. По умолчанию 1152.
        height (int, optional): Высота изображения в пикселях. По умолчанию 896.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий объекты `ImageResponse` с URL-адресами сгенерированных изображений.

    Raises:
        Exception: Если происходит ошибка при генерации изображения.

    """
```

**Назначение**: Создает асинхронный генератор для генерации изображений на основе текстового запроса.

**Параметры**:
- `cls` (Type[`ImageLabs`]): Класс `ImageLabs`.
- `model` (str): Модель для генерации изображений.
- `messages` (`Messages`): Список сообщений, содержащих текстовый запрос.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `prompt` (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
- `negative_prompt` (str, optional): Негативный промпт, указывающий, что не должно быть на изображении. По умолчанию "".
- `width` (int, optional): Ширина изображения в пикселях. По умолчанию 1152.
- `height` (int, optional): Высота изображения в пикселях. По умолчанию 896.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий объекты `ImageResponse` с URL-адресами сгенерированных изображений.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при генерации изображения.

**Как работает функция**:

1. **Инициализация**:
   - Функция `create_async_generator` инициализирует заголовки для HTTP-запросов, включая `User-Agent`, `Content-Type` и `Referer`.
   -  Определяется текстовый запрос (`prompt`) для генерации изображения. Если `prompt` не передан явно, он извлекается из последнего сообщения в списке `messages`.

2. **Генерация изображения**:
   - Формируется полезная нагрузка (`payload`) с параметрами для запроса к API генерации изображений, включая `prompt`, `seed`, `width`, `height` и `negative_prompt`.
   - Отправляется POST-запрос к API ImageLabs (`cls.url/txt2img`) с использованием `ClientSession` из библиотеки `aiohttp`.
   - Полученный ответ преобразуется в JSON, и извлекается `task_id`, который используется для отслеживания прогресса генерации изображения.

3. **Опрос прогресса**:
   - Запускается бесконечный цикл (`while True`) для периодического опроса API о состоянии задачи генерации изображения.
   - Внутри цикла отправляется POST-запрос к API (`cls.url/progress`) с `task_id`.
   - Полученный ответ преобразуется в JSON, и проверяется статус задачи.

4. **Обработка статусов**:
   - Если статус задачи `'Done'` или если получен `final_image_url`, генератор выдает (`yield`) объект `ImageResponse` с URL-адресом сгенерированного изображения и завершает свою работу (`break`).
   - Если в статусе задачи обнаружена ошибка (`'error'`), выбрасывается исключение `Exception` с информацией об ошибке.

5. **Ожидание между опросами**:
   -  Если задача еще не завершена и не произошла ошибка, функция ожидает 1 секунду (`asyncio.sleep(1)`) перед следующей попыткой опроса.

```
Начало
 |
 | Установка заголовков и определение текстового запроса
 |
 --> Отправка POST запроса к API ImageLabs для генерации изображения
 |
 | Получение task_id
 |
 --> Цикл опроса API для отслеживания прогресса
 |
 | Проверка статуса задачи
 |
 | Если статус "Done" или получен final_image_url:
 --> Выдача ImageResponse с URL изображения
 |  |
 |  Выход из цикла
 |
 | Если в статусе есть "error":
 --> Выброс исключения Exception
 |
 | Ожидание 1 секунды
 |
Конец
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from src.endpoints.gpt4free.g4f.Provider.ImageLabs import ImageLabs
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    model = "sdxl-turbo"
    messages: Messages = [{"role": "user", "content": "A cat wearing a hat"}]
    proxy = None
    async for image_response in ImageLabs.create_async_generator(model=model, messages=messages, proxy=proxy):
        print(image_response.images)

if __name__ == "__main__":
    asyncio.run(main())
```

### `get_model`

```python
@classmethod
def get_model(cls, model: str) -> str:
    """
    Возвращает модель по умолчанию.

    Args:
        cls (Type[ImageLabs]): Класс ImageLabs.
        model (str): Модель для получения.

    Returns:
        str: Модель по умолчанию.
    """
```

**Назначение**: Возвращает модель по умолчанию.

**Параметры**:
- `cls` (Type[`ImageLabs`]): Класс `ImageLabs`.
- `model` (str): Модель для получения.

**Возвращает**:
- `str`: Модель по умолчанию.

**Как работает функция**:

Функция `get_model` просто возвращает значение атрибута `cls.default_model`, который представляет собой модель, используемую по умолчанию. Она не выполняет никаких сложных операций или проверок.

```
Начало
 |
 | Возврат значения cls.default_model
 |
Конец
```

**Примеры**:

```python
# Пример использования get_model
from src.endpoints.gpt4free.g4f.Provider.ImageLabs import ImageLabs

model = ImageLabs.get_model("any_model")
print(model)  # Output: sdxl-turbo