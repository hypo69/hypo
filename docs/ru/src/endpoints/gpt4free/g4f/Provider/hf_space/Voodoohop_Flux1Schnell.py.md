# Модуль Voodoohop_Flux1Schnell

## Обзор

Модуль `Voodoohop_Flux1Schnell` предоставляет асинхронный интерфейс для взаимодействия с сервисом Voodoohop Flux-1-Schnell, размещенным на платформе Hugging Face Spaces. Этот сервис позволяет генерировать изображения на основе текстовых запросов. Модуль предоставляет функции для форматирования запросов, отправки их в API и получения сгенерированных изображений.

## Подробней

Модуль предназначен для интеграции в систему, где требуется генерация изображений на основе текстовых описаний. Он использует асинхронные запросы для взаимодействия с API Voodoohop Flux-1-Schnell, что позволяет эффективно обрабатывать множество запросов параллельно.

## Классы

### `Voodoohop_Flux1Schnell`

**Описание**: Класс `Voodoohop_Flux1Schnell` является поставщиком (провайдером) изображений, использующим Hugging Face Space Voodoohop Flux-1-Schnell.

**Наследует**:

- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:

- `label` (str): Метка провайдера, `"Voodoohop Flux-1-Schnell"`.
- `url` (str): URL сервиса, `"https://voodoohop-flux-1-schnell.hf.space"`.
- `api_endpoint` (str): URL API endpoint, `"https://voodoohop-flux-1-schnell.hf.space/call/infer"`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера, `True`.
- `default_model` (str): Модель по умолчанию, `"voodoohop-flux-1-schnell"`.
- `default_image_model` (str): Модель изображения по умолчанию, соответствует `default_model`.
- `model_aliases` (dict): Псевдонимы моделей, `{"flux-schnell": default_model, "flux": default_model}`.
- `image_models` (list): Список моделей изображений, полученный из ключей `model_aliases`.
- `models` (list): Список моделей, соответствует `image_models`.

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
        ...
```

**Назначение**: Создает асинхронный генератор изображений на основе предоставленных параметров.

**Параметры**:

- `cls` (class): Класс, для которого создается генератор.
- `model` (str): Используемая модель.
- `messages` (Messages): Список сообщений для формирования запроса.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `prompt` (str, optional): Дополнительный текст запроса. По умолчанию `None`.
- `width` (int): Ширина изображения в пикселях. По умолчанию `768`.
- `height` (int): Высота изображения в пикселях. По умолчанию `768`.
- `num_inference_steps` (int): Количество шагов для генерации изображения. По умолчанию `2`.
- `seed` (int): Зерно для генерации случайных чисел. По умолчанию `0`.
- `randomize_seed` (bool): Флаг, указывающий на необходимость рандомизации зерна. По умолчанию `True`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий объекты `ImageResponse` с URL сгенерированных изображений.

**Вызывает исключения**:

- `ResponseError`: Если при генерации изображения произошла ошибка.

**Как работает функция**:

1.  **Подготовка параметров**:
    *   Определяются размеры изображения, гарантируя, что они кратны 8 и не меньше 32.
    *   Формируется промпт на основе предоставленных сообщений.

2.  **Формирование запроса**:
    *   Создается полезная нагрузка (payload) с данными, необходимыми для запроса к API, включая промпт, зерно, размеры изображения и количество шагов генерации.

3.  **Отправка запроса и обработка ответа**:
    *   Используется асинхронная сессия для отправки POST-запроса к API endpoint.
    *   Проверяется статус ответа и извлекается `event_id` из JSON-ответа.

4.  **Ожидание и получение результатов**:
    *   В цикле отправляются GET-запросы к API для получения статуса события (генерации изображения).
    *   Обрабатываются поступающие события, разделяя их по типу (`error`, `complete`).
    *   В случае ошибки выбрасывается исключение `ResponseError`.
    *   При получении события `complete` извлекается URL изображения из JSON-данных и возвращается объект `ImageResponse`.

```text
    Начало
    │
    ├── Подготовка параметров (ширина, высота, промпт)
    │
    ├── Формирование запроса (payload)
    │
    ├── Отправка POST-запроса к API
    │   │
    │   └── Получение event_id
    │
    ├── Цикл ожидания и получения результатов
    │   │
    │   ├── Отправка GET-запросов к API
    │   │
    │   ├── Обработка событий (error, complete)
    │   │   │
    │   │   ├── Если error:  ResponseError
    │   │   │
    │   │   └── Если complete: Извлечение URL изображения и возврат ImageResponse
    │   │
    │   └── Конец цикла при получении complete
    │
    └── Завершение
```

**Примеры**:

Пример 1: Генерация изображения с использованием минимальных параметров.

```python
    model = "voodoohop-flux-1-schnell"
    messages = [{"role": "user", "content": "A cat playing guitar"}]
    async for image_response in Voodoohop_Flux1Schnell.create_async_generator(model=model, messages=messages):
        print(image_response.images)
```

Пример 2: Генерация изображения с указанием размеров и зерна.

```python
    model = "voodoohop-flux-1-schnell"
    messages = [{"role": "user", "content": "A dog running in a park"}]
    width = 512
    height = 512
    seed = 42
    async for image_response in Voodoohop_Flux1Schnell.create_async_generator(
        model=model, messages=messages, width=width, height=height, seed=seed
    ):
        print(image_response.images)