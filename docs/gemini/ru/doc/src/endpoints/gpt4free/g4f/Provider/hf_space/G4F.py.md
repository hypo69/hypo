# Модуль G4F для работы с Hugging Face Space

## Обзор

Модуль `G4F` предоставляет классы для взаимодействия с моделями, размещенными на Hugging Face Spaces, в частности, с моделями `roxky/Janus-Pro-7B` и `roxky/FLUX.1-dev`. Он включает поддержку как текстовых, так и графических моделей, а также методы для получения токенов GPU и форматирования запросов.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями, доступными через Hugging Face Spaces. Он обеспечивает удобный интерфейс для отправки запросов к моделям и получения результатов. Модуль использует асинхронные запросы для эффективной работы с сетевыми ресурсами и включает механизмы обработки ошибок и логирования.

## Классы

### `FluxDev`

**Описание**: Класс для взаимодействия с моделью `FLUX.1-dev` на Hugging Face Space.

**Наследует**: `BlackForestLabs_Flux1Dev`

**Атрибуты**:
- `url` (str): URL Space `https://roxky-flux-1-dev.hf.space`.
- `space` (str): Имя Space `roxky/FLUX.1-dev`.
- `referer` (str): Referer URL для запросов.

### `G4F`

**Описание**: Класс для взаимодействия с моделями `Janus-Pro-7B` и `FLUX.1-dev` через G4F framework.

**Наследует**: `DeepseekAI_JanusPro7b`

**Атрибуты**:
- `label` (str): Метка класса "G4F framework".
- `space` (str): Имя Space `roxky/Janus-Pro-7B`.
- `url` (str): URL Space `https://huggingface.co/spaces/roxky/g4f-space`.
- `api_url` (str): URL API `https://roxky-janus-pro-7b.hf.space`.
- `url_flux` (str): URL для запросов к модели flux `https://roxky-g4f-flux.hf.space/run/predict`.
- `referer` (str): Referer URL для запросов.
- `default_model` (str): Модель по умолчанию "flux".
- `model_aliases` (dict): Псевдонимы моделей, например, `{"flux-schnell": default_model}`.
- `image_models` (list): Список моделей для генерации изображений.
- `models` (list): Список поддерживаемых моделей.

**Методы**:

- `create_async_generator`: Асинхронный генератор для создания запросов к моделям.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    prompt: str = None,
    aspect_ratio: str = "1:1",
    width: int = None,
    height: int = None,
    seed: int = None,
    cookies: dict = None,
    api_key: str = None,
    zerogpu_uuid: str = "[object Object]",
    **kwargs
) -> AsyncResult:
    """Асинхронный генератор для создания запросов к моделям.

    Args:
        cls (type): Класс, для которого вызывается метод.
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        prompt (str, optional): Текст запроса. По умолчанию `None`.
        aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
        width (int, optional): Ширина изображения. По умолчанию `None`.
        height (int, optional): Высота изображения. По умолчанию `None`.
        seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
        cookies (dict, optional): Cookies для отправки с запросом. По умолчанию `None`.
        api_key (str, optional): API ключ для доступа к модели. По умолчанию `None`.
        zerogpu_uuid (str, optional): UUID для zerogpu. По умолчанию "[object Object]".
        **kwargs: Дополнительные параметры.

    Yields:
        AsyncResult: Частичные результаты запроса, такие как статусы и сгенерированные изображения.
    """
```

**Назначение**: Метод `create_async_generator` является асинхронным генератором, который отправляет запросы к указанной модели и возвращает результаты в виде чанков. Он поддерживает как текстовые, так и графические модели, а также обрабатывает параметры, специфичные для каждой модели.

**Параметры**:
- `cls` (type): Ссылка на класс.
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `prompt` (str, optional): Текст запроса. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
- `width` (int, optional): Ширина изображения. По умолчанию `None`.
- `height` (int, optional): Высота изображения. По умолчанию `None`.
- `seed` (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
- `cookies` (dict, optional): Cookies для отправки с запросом. По умолчанию `None`.
- `api_key` (str, optional): API ключ для доступа к модели. По умолчанию `None`.
- `zerogpu_uuid` (str, optional): UUID для zerogpu. По умолчанию "[object Object]".
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий частичные результаты запроса.

**Как работает функция**:

1.  **Определение модели**: Функция определяет, какую модель использовать (`flux`, `flux-dev` или другие).

2.  **Передача запроса**: Если модель `flux` или `flux-dev`, запрос передается в `FluxDev.create_async_generator`.

3.  **Обработка изображения**: Для графических моделей форматируется запрос, устанавливаются размеры изображения и генерируется случайное зерно.

4.  **Формирование payload**: Подготавливается payload с данными запроса, включая текст запроса, зерно, ширину и высоту изображения.

5.  **Асинхронный запрос**: Отправляется асинхронный POST-запрос к API модели, обрабатывается ответ и возвращается URL сгенерированного изображения.

6.  **Получение токена**: При отсутствии `api_key` выполняется попытка получения токена GPU.

7.  **Прогресс генерации**: Во время генерации изображения возвращаются промежуточные статусы.

**Внутренние функции**:

- `generate`:

    ```python
    async def generate():
        """Асинхронная функция для отправки запроса на генерацию изображения.

        Args:
            None

        Returns:
            ImageResponse: Объект `ImageResponse` с URL и альтернативным текстом сгенерированного изображения.
        """
    ```

    **Назначение**: Отправляет POST-запрос к API модели и обрабатывает ответ.

    **Параметры**:
    - Отсутствуют.

    **Возвращает**:
    - `ImageResponse`: Объект `ImageResponse` с URL и альтернативным текстом сгенерированного изображения.

```
A (Определение модели)
│
├───> B (flux или flux-dev)
│   │
│   └───> C (FluxDev.create_async_generator)
│
└───> D (Обработка изображения)
    │
    ├───> E (Формирование payload)
    │   │
    │   └───> F (Асинхронный запрос)
    │       │
    │       └───> G (Получение токена)
    │           │
    │           └───> H (Прогресс генерации)
    │
    └───> I (super().create_async_generator)
```

**Примеры**:

```python
# Пример использования для модели flux
async for chunk in G4F.create_async_generator(model="flux", messages=[{"role": "user", "content": "generate a cat image"}]):
    print(chunk)

# Пример использования для модели DeepseekAI_JanusPro7b
async for chunk in G4F.create_async_generator(model="DeepseekAI_JanusPro7b", messages=[{"role": "user", "content": "Hello, how are you?"}]):
    print(chunk)