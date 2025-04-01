# Модуль Voodoohop_Flux1Schnell
## Обзор

Модуль предоставляет асинхронный интерфейс для взаимодействия с сервисом Voodoohop Flux-1-Schnell, расположенным по адресу "https://voodoohop-flux-1-schnell.hf.space". Этот сервис предназначен для генерации изображений на основе текстовых запросов (prompt). Модуль позволяет отправлять запросы на генерацию изображений и получать результаты в асинхронном режиме.

## Подробней

Модуль использует `aiohttp` для выполнения асинхронных HTTP-запросов к API Voodoohop Flux-1-Schnell. Он поддерживает настройку параметров генерации изображений, таких как ширина, высота, количество шагов инференса и seed для воспроизводимости результатов.

## Классы

### `Voodoohop_Flux1Schnell`
Описание класса для взаимодействия с сервисом Voodoohop Flux-1-Schnell.
**Наследует:**
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты:**
- `label` (str): Отображаемое имя провайдера ("Voodoohop Flux-1-Schnell").
- `url` (str): URL сервиса ("https://voodoohop-flux-1-schnell.hf.space").
- `api_endpoint` (str): URL API endpoint ("https://voodoohop-flux-1-schnell.hf.space/call/infer").
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `default_model` (str): Модель, используемая по умолчанию ("voodoohop-flux-1-schnell").
- `default_image_model` (str): Модель для генерации изображений по умолчанию (совпадает с `default_model`).
- `model_aliases` (dict): Псевдонимы для моделей ({"flux-schnell": default_model, "flux": default_model}).
- `image_models` (list): Список поддерживаемых моделей для генерации изображений (ключи из `model_aliases`).
- `models` (list): Список всех поддерживаемых моделей (совпадает с `image_models`).

### `create_async_generator`
```python
@classmethod
async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        prompt: str = None,
        width: int = 768,
        height: int = 768,
        num_inference_steps: int = 2,
        seed: int = 0,
        randomize_seed: bool = True,
        **kwargs
) -> AsyncResult:
    """
    Асинхронно генерирует изображения на основе текстового запроса.

    Args:
        cls (Voodoohop_Flux1Schnell): Класс, для которого вызывается метод.
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений, используемых для формирования запроса.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
        width (int, optional): Ширина генерируемого изображения. По умолчанию 768.
        height (int, optional): Высота генерируемого изображения. По умолчанию 768.
        num_inference_steps (int, optional): Количество шагов инференса. По умолчанию 2.
        seed (int, optional): Seed для воспроизводимости результатов. По умолчанию 0.
        randomize_seed (bool, optional): Флаг для рандомизации seed. По умолчанию `True`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий изображения.

    Raises:
        ResponseError: Если при генерации изображения произошла ошибка.

    """
```
**Назначение**:
Метод `create_async_generator` асинхронно генерирует изображения на основе текстового запроса, используя API сервиса Voodoohop Flux-1-Schnell. Он формирует полезную нагрузку (payload) с параметрами запроса, отправляет её на API endpoint и получает результаты в виде потока данных.

**Как работает функция**:

1. **Подготовка параметров**:
   - Убедимся, что ширина и высота кратны 8 и не меньше 32.
   - Форматирует текстовый запрос (prompt) из списка сообщений.
2. **Формирование полезной нагрузки (payload)**:
   - Создает словарь `payload` с данными для запроса, включающими prompt, seed, флаг рандомизации seed, ширину, высоту и количество шагов инференса.
3. **Отправка запроса и обработка ответа**:
   - Создает асинхронную сессию с помощью `ClientSession`.
   - Отправляет POST-запрос на `api_endpoint` с JSON-payload и прокси (если указан).
   - Проверяет статус ответа с помощью `raise_for_status`.
   - Извлекает `event_id` из JSON-ответа.
4. **Получение и обработка событий**:
   - В цикле отправляет GET-запросы на `api_endpoint/{event_id}` для получения статуса генерации.
   - Читает данные из ответа по частям (до `\n\n`).
   - Анализирует тип события (`event_type`):
     - Если `error`, вызывает исключение `ResponseError`.
     - Если `complete`, извлекает URL изображения из JSON-данных и возвращает объект `ImageResponse` через `yield`.
   - Завершает работу генератора после получения события `complete`.

**Внутренние функции**:
- Отсутствуют

**ASCII flowchart**:

```
    [Настройка параметров]
        ↓
    [Формирование payload]
        ↓
    [Отправка POST-запроса]
        ↓
    [Получение event_id]
        ↓
    [Цикл GET-запросов к api_endpoint/{event_id}]
        |
        [Чтение данных из ответа]
        ↓
        [Анализ типа события]
        |
        [error] --→ [Вызов ResponseError]
        |
        [complete] --→ [Извлечение URL изображения]
        |
        [Возврат ImageResponse через yield]
        ↓
    [Завершение генератора]
```

**Примеры**:

```python
# Пример использования (требуется асинхронный контекст)
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.Voodoohop_Flux1Schnell import Voodoohop_Flux1Schnell
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    messages: Messages = [{"role": "user", "content": "A beautiful cat"}]
    generator = Voodoohop_Flux1Schnell.create_async_generator(
        model="voodoohop-flux-1-schnell",
        messages=messages,
        width=512,
        height=512,
        num_inference_steps=10,
        seed=42,
        randomize_seed=False
    )
    async for image_response in await generator:
        print(f"Image URL: {image_response.images[0]}")
        break  # Получаем только первое изображение для примера

if __name__ == "__main__":
    asyncio.run(main())
```
```python
# Пример использования с прокси (требуется асинхронный контекст)
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.Voodoohop_Flux1Schnell import Voodoohop_Flux1Schnell
from src.endpoints.gpt4free.g4f.typing import Messages

async def main():
    messages: Messages = [{"role": "user", "content": "A futuristic cityscape"}]
    generator = Voodoohop_Flux1Schnell.create_async_generator(
        model="voodoohop-flux-1-schnell",
        messages=messages,
        width=512,
        height=512,
        num_inference_steps=10,
        seed=42,
        proxy="http://your_proxy:8080",
        randomize_seed=False
    )
    async for image_response in await generator:
        print(f"Image URL: {image_response.images[0]}")
        break

if __name__ == "__main__":
    asyncio.run(main())

```
```python
# Пример обработки ошибки ResponseError (требуется асинхронный контекст)
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.Voodoohop_Flux1Schnell import Voodoohop_Flux1Schnell
from src.endpoints.gpt4free.g4f.typing import Messages
from src.endpoints.gpt4free.g4f.errors import ResponseError

async def main():
    messages: Messages = [{"role": "user", "content": "This will cause an error"}]
    try:
        generator = Voodoohop_Flux1Schnell.create_async_generator(
            model="voodoohop-flux-1-schnell",
            messages=messages,
            width=512,
            height=512,
            num_inference_steps=10,
            seed=42,
            randomize_seed=False
        )
        async for image_response in await generator:
            print(f"Image URL: {image_response.images[0]}")
            break
    except ResponseError as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    asyncio.run(main())
```
-------------------------------------------------------------------------------------