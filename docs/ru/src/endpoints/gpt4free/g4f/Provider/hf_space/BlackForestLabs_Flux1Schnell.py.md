# Модуль BlackForestLabs_Flux1Schnell

## Обзор

Модуль `BlackForestLabs_Flux1Schnell` предоставляет асинхронный интерфейс для взаимодействия с моделью генерации изображений Flux-1-Schnell от Black Forest Labs, размещенной на платформе Hugging Face Spaces. Он позволяет генерировать изображения на основе текстовых запросов, используя API Hugging Face Space.

## Подробнее

Этот модуль является частью системы асинхронных провайдеров в проекте `hypotez` и предназначен для интеграции с другими компонентами, требующими функциональности генерации изображений. Он поддерживает настройку параметров генерации, таких как размеры изображения, количество шагов обработки и начальное зерно для воспроизводимости результатов.

## Классы

### `BlackForestLabs_Flux1Schnell`

**Описание**: Класс `BlackForestLabs_Flux1Schnell` предоставляет методы для асинхронной генерации изображений с использованием модели Flux-1-Schnell.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, генерирующих последовательность результатов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями, специфичными для провайдера.

**Атрибуты**:
- `label (str)`: Метка провайдера, используемая для идентификации.
- `url (str)`: URL главной страницы Hugging Face Space.
- `api_endpoint (str)`: URL API для взаимодействия с моделью Flux-1-Schnell.
- `working (bool)`: Указывает, что провайдер в настоящее время работоспособен.
- `default_model (str)`: Модель, используемая по умолчанию.
- `default_image_model (str)`: Модель изображения, используемая по умолчанию.
- `model_aliases (dict)`: Псевдонимы моделей для удобства использования.
- `image_models (list)`: Список поддерживаемых моделей изображений.
- `models (list)`: Список поддерживаемых моделей.

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
        Создает асинхронный генератор для получения изображений от BlackForestLabs Flux-1-Schnell.

        Args:
            model (str): Имя используемой модели.
            messages (Messages): Список сообщений, используемых для формирования запроса.
            proxy (Optional[str], optional): URL прокси-сервера для использования. По умолчанию `None`.
            prompt (Optional[str], optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
            width (int, optional): Ширина генерируемого изображения. По умолчанию 768.
            height (int, optional): Высота генерируемого изображения. По умолчанию 768.
            num_inference_steps (int, optional): Количество шагов обработки для генерации изображения. По умолчанию 2.
            seed (int, optional): Начальное зерно для генерации изображения. По умолчанию 0.
            randomize_seed (bool, optional): Флаг, указывающий, следует ли рандомизировать зерно. По умолчанию `True`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий изображения.

        Raises:
            ResponseError: Если при генерации изображения произошла ошибка.

        Example:
            >>> result = await BlackForestLabs_Flux1Schnell.create_async_generator(
            ...     model='black-forest-labs-flux-1-schnell',
            ...     messages=[{'role': 'user', 'content': 'Example prompt'}],
            ...     width=512,
            ...     height=512
            ... )
            >>> async for image in result:
            ...     print(image)
        """
        ...
```

**Назначение**:
Создает асинхронный генератор для получения изображений от BlackForestLabs Flux-1-Schnell.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для формирования запроса.
- `proxy` (Optional[str], optional): URL прокси-сервера. По умолчанию `None`.
- `prompt` (Optional[str], optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
- `width` (int, optional): Ширина генерируемого изображения. По умолчанию 768.
- `height` (int, optional): Высота генерируемого изображения. По умолчанию 768.
- `num_inference_steps` (int, optional): Количество шагов обработки для генерации изображения. По умолчанию 2.
- `seed` (int, optional): Начальное зерно для генерации изображения. По умолчанию 0.
- `randomize_seed` (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий изображения.

**Вызывает исключения**:
- `ResponseError`: Если при генерации изображения произошла ошибка.

**Как работает функция**:

1. **Подготовка параметров**: Функция принимает параметры, необходимые для генерации изображения, такие как модель, текстовый запрос, размеры изображения и другие параметры конфигурации.
2. **Форматирование запроса**: Формирует полезную нагрузку (payload) с данными, необходимыми для запроса к API Hugging Face Space.
3. **Асинхронный запрос**: Отправляет асинхронный POST-запрос к API Hugging Face Space с использованием `aiohttp.ClientSession`.
4. **Обработка ответа**: Получает `event_id` из ответа и начинает цикл опроса API для получения статуса генерации изображения.
5. **Чтение событий**: Читает события из потока ответов, пока не получит сообщение об ошибке или завершении.
6. **Генерация изображения**: В случае успешного завершения генерирует URL изображения и возвращает объект `ImageResponse`.
7. **Обработка ошибок**: Если при генерации возникает ошибка, вызывает исключение `ResponseError`.

```
A [Подготовка параметров]
|
B [Форматирование запроса]
|
C [Асинхронный POST-запрос]
|
D [Получение event_id]
|
E [Цикл опроса API]
|
F [Чтение событий]
|
G [Генерация изображения]
|
H [Обработка ошибок]
```

**Примеры**:

```python
# Пример 1: Генерация изображения с минимальными параметрами
result = await BlackForestLabs_Flux1Schnell.create_async_generator(
    model='black-forest-labs-flux-1-schnell',
    messages=[{'role': 'user', 'content': 'A cat sitting on a mat'}]
)

# Пример 2: Генерация изображения с указанием размеров и зерна
result = await BlackForestLabs_Flux1Schnell.create_async_generator(
    model='black-forest-labs-flux-1-schnell',
    messages=[{'role': 'user', 'content': 'A dog running in the park'}],
    width=512,
    height=512,
    seed=42
)

# Пример 3: Обработка результата генерации
result = await BlackForestLabs_Flux1Schnell.create_async_generator(
    model='black-forest-labs-flux-1-schnell',
    messages=[{'role': 'user', 'content': 'A bird flying in the sky'}]
)
async for image in result:
    print(image)