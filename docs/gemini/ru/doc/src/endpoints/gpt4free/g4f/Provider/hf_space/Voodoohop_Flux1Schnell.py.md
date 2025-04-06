# Модуль Voodoohop_Flux1Schnell

## Обзор

Модуль `Voodoohop_Flux1Schnell` предоставляет асинхронный генератор изображений, использующий API Voodoohop Flux-1-Schnell. Он позволяет генерировать изображения на основе текстовых подсказок (prompt) с возможностью настройки различных параметров, таких как ширина, высота, количество шагов обработки и зерно (seed).

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими генерации изображений на основе текстовых описаний. Он использует асинхронные запросы для взаимодействия с API Voodoohop Flux-1-Schnell, что позволяет эффективно обрабатывать запросы и генерировать изображения.

## Классы

### `Voodoohop_Flux1Schnell`

**Описание**: Класс `Voodoohop_Flux1Schnell` предоставляет методы для асинхронной генерации изображений с использованием API Voodoohop Flux-1-Schnell.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, используемая для идентификации.
- `url` (str): URL главной страницы Voodoohop Flux-1-Schnell.
- `api_endpoint` (str): URL API для отправки запросов на генерацию изображений.
- `working` (bool): Флаг, указывающий, работает ли провайдер в данный момент.
- `default_model` (str): Модель, используемая по умолчанию.
- `default_image_model` (str): Модель изображения, используемая по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей для удобства использования.
- `image_models` (list): Список моделей изображений.
- `models` (list): Список моделей.

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
        """Создает асинхронный генератор изображений на основе API Voodoohop Flux-1-Schnell.

        Args:
            model (str): Модель для генерации изображений.
            messages (Messages): Список сообщений, используемых для формирования подсказки.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            prompt (str, optional): Текстовая подсказка для генерации изображения. По умолчанию `None`.
            width (int, optional): Ширина генерируемого изображения. По умолчанию 768.
            height (int, optional): Высота генерируемого изображения. По умолчанию 768.
            num_inference_steps (int, optional): Количество шагов обработки для генерации изображения. По умолчанию 2.
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию 0.
            randomize_seed (bool, optional): Флаг, указывающий, нужно ли рандомизировать зерно. По умолчанию `True`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий изображения в формате `ImageResponse`.

        Raises:
            ResponseError: Если возникает ошибка при генерации изображения.

        Как работает функция:
         1. **Подготовка параметров изображения**: Функция принимает различные параметры, такие как модель, сообщения, прокси, текстовый запрос, ширину, высоту, количество шагов обработки, зерно и флаг рандомизации зерна, для настройки процесса генерации изображения.
         2. **Корректировка размеров изображения**: Функция корректирует ширину и высоту изображения, чтобы они были кратны 8, обеспечивая совместимость с требованиями API.
         3. **Форматирование текстового запроса**: Функция форматирует текстовый запрос на основе предоставленных сообщений и запроса, подготавливая его для отправки в API.
         4. **Создание полезной нагрузки**: Функция создает полезную нагрузку (payload) с данными, необходимыми для запроса к API, включая текстовый запрос, зерно, флаг рандомизации зерна, ширину, высоту и количество шагов обработки.
         5. **Отправка запроса и обработка ответа**: Функция отправляет асинхронный POST-запрос к API с полезной нагрузкой и обрабатывает ответ, получая идентификатор события (event_id) для отслеживания статуса генерации изображения.
         6. **Цикл ожидания и получения статуса**: Функция входит в бесконечный цикл, в котором она отправляет GET-запросы к API для получения статуса генерации изображения по идентификатору события.
         7. **Обработка событий**: Функция читает события из ответа, разделяя их по типу (ошибка, завершение) и обрабатывая соответствующие данные.
         8. **Генерация изображения и возврат результата**: При получении события `complete` функция извлекает URL изображения из данных, создает объект `ImageResponse` с URL и текстовым запросом, и возвращает его через генератор.
         9. **Обработка ошибок**: Если возникает ошибка при генерации изображения, функция вызывает исключение `ResponseError` с сообщением об ошибке.
         10. **Завершение работы**: После успешной генерации и возврата изображения функция завершает свою работу.

        ```
        Подготовка параметров изображения
             │
             ▼
        Корректировка размеров изображения
             │
             ▼
        Форматирование текстового запроса
             │
             ▼
        Создание полезной нагрузки
             │
             ▼
        Отправка запроса и обработка ответа
             │
             ▼
        Цикл ожидания и получения статуса
             │
             ▼
        Обработка событий ──► Ошибка: ResponseError
             │
             ▼
        Генерация изображения и возврат результата
             │
             ▼
        Завершение работы
        ```

        """
        width = max(32, width - (width % 8))
        height = max(32, height - (height % 8))
        prompt = format_image_prompt(messages, prompt)
        payload = {
            "data": [
                prompt,
                seed,
                randomize_seed,
                width,
                height,
                num_inference_steps
            ]
        }
        async with ClientSession() as session:
            async with session.post(cls.api_endpoint, json=payload, proxy=proxy) as response:
                await raise_for_status(response)
                response_data = await response.json()
                event_id = response_data['event_id']
                while True:
                    async with session.get(f"{cls.api_endpoint}/{event_id}", proxy=proxy) as status_response:
                        await raise_for_status(status_response)
                        while not status_response.content.at_eof():
                            event = await status_response.content.readuntil(b'\n\n')
                            if event.startswith(b'event:'):
                                event_parts = event.split(b'\ndata: ')
                                if len(event_parts) < 2:
                                    continue
                                event_type = event_parts[0].split(b': ')[1]
                                data = event_parts[1]
                                if event_type == b'error':
                                    raise ResponseError(f"Error generating image: {data}")
                                elif event_type == b'complete':
                                    json_data = json.loads(data)
                                    image_url = json_data[0]['url']
                                    yield ImageResponse(images=[image_url], alt=prompt)
                                    return

```

## Функции

### `format_image_prompt`

Функция `format_image_prompt` используется для форматирования текстовых подсказок для генерации изображений. Описание этой функции отсутствует в предоставленном коде.

## Примеры

Пример использования класса `Voodoohop_Flux1Schnell` для создания асинхронного генератора изображений:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.hf_space.Voodoohop_Flux1Schnell import Voodoohop_Flux1Schnell
from src.endpoints.gpt4free.g4f.typing import Messages

async def generate_image(prompt: str):
    """Генерирует изображение на основе текстовой подсказки."""
    messages: Messages = [{"role": "user", "content": prompt}]
    generator = Voodoohop_Flux1Schnell.create_async_generator(
        model="voodoohop-flux-1-schnell",
        messages=messages
    )
    async for image_response in await generator:
        print(f"Image URL: {image_response.images[0]}")

async def main():
    """Главная функция для запуска генерации изображения."""
    await generate_image("A cat sitting on a couch")

if __name__ == "__main__":
    asyncio.run(main())
```

Этот пример показывает, как создать асинхронный генератор изображений с использованием класса `Voodoohop_Flux1Schnell` и получить URL сгенерированного изображения.