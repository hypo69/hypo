# Модуль `G4F`

## Обзор

Модуль предоставляет интерфейс для взаимодействия с G4F framework (GPT4Free) через Hugging Face Spaces. Он поддерживает как текстовые, так и графические запросы, используя различные модели, включая `flux` и `DeepseekAI_JanusPro7b`.

## Подробнее

Этот модуль позволяет использовать G4F framework для генерации текста и изображений, взаимодействуя с сервисами, размещенными на Hugging Face Spaces. Он включает в себя поддержку различных моделей, таких как `flux` и `DeepseekAI_JanusPro7b`, а также обеспечивает асинхронное взаимодействие с API.
Расположен в `hypotez/src/endpoints/gpt4free/g4f/Provider/hf_space/G4F.py` и отвечает за интеграцию с Hugging Face Spaces для использования G4F framework.

## Классы

### `FluxDev`

**Описание**:
Класс для взаимодействия с моделью Flux-1-dev, размещенной на Hugging Face Space.

**Наследует**:
`BlackForestLabs_Flux1Dev`

**Атрибуты**:
- `url` (str): URL Space на Hugging Face.
- `space` (str): Имя Space на Hugging Face.
- `referer` (str): Referer URL.

### `G4F`

**Описание**:
Основной класс для взаимодействия с G4F framework.

**Наследует**:
`DeepseekAI_JanusPro7b`

**Атрибуты**:
- `label` (str): Метка для идентификации провайдера.
- `space` (str): Имя Space на Hugging Face.
- `url` (str): URL Space на Hugging Face.
- `api_url` (str): URL API.
- `url_flux` (str): URL для Flux.
- `referer` (str): Referer URL.
- `default_model` (str): Модель по умолчанию (`flux`).
- `model_aliases` (dict): Алиасы для моделей.
- `image_models` (list): Список моделей для генерации изображений.
- `models` (list): Список всех поддерживаемых моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для обработки запросов.

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
    """
    Создает асинхронный генератор для обработки запросов к моделям G4F.

    Args:
        cls (type): Класс, для которого вызывается метод.
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для обработки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        prompt (str, optional): Текст запроса. По умолчанию `None`.
        aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
        width (int, optional): Ширина изображения. По умолчанию `None`.
        height (int, optional): Высота изображения. По умолчанию `None`.
        seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
        cookies (dict, optional): Куки для запроса. По умолчанию `None`.
        api_key (str, optional): API-ключ. По умолчанию `None`.
        zerogpu_uuid (str, optional): UUID для zerogpu. По умолчанию "[object Object]".
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий чанки данных.

    Raises:
        Exception: В случае ошибок при взаимодействии с API.
    """
```

**Как работает функция**:

1.  **Выбор модели**: Функция сначала определяет, какую модель использовать для обработки запроса. Если указана модель `flux` или `flux-dev`, она перенаправляет запрос в `FluxDev.create_async_generator`. Если модель не содержит `default_model` (например, "janus"), она перенаправляет запрос в `super().create_async_generator`.

2.  **Подготовка параметров**: Функция подготавливает параметры запроса, такие как `width`, `height`, `prompt` и `seed`. Ширина и высота приводятся к значениям, кратным 8, а если `prompt` не указан, он формируется на основе `messages`.

3.  **Формирование payload**: Функция формирует словарь `payload` с данными для запроса к API. Этот словарь включает `prompt`, `seed`, `width`, `height` и другие параметры.

4.  **Получение токена GPU**: Если `api_key` не указан, функция пытается получить токен GPU, вызывая `get_zerogpu_token`.

5.  **Выполнение запроса**: Функция выполняет POST-запрос к API (`cls.url_flux`) с использованием `ClientSession`. В заголовки запроса добавляются `x-zerogpu-token` и `x-zerogpu-uuid`.

6.  **Обработка ответа**: После получения ответа функция извлекает URL изображения из данных ответа и возвращает объект `ImageResponse`.

7.  **Асинхронная генерация**: Функция использует `asyncio.create_task` для выполнения запроса в фоновом режиме и возвращает промежуточные результаты (например, статус генерации) с использованием `yield`.

**Внутренние функции**:

### `generate`

```python
async def generate():
    """
    Асинхронно генерирует изображение, отправляя запрос к API и обрабатывая ответ.

    Returns:
        ImageResponse: Объект `ImageResponse` с URL сгенерированного изображения и альтернативным текстом.
    """
```

**Как работает внутренняя функция**:

1.  **Отправка POST-запроса**:
    - Отправляет асинхронный POST-запрос к `cls.url_flux` с данными `payload` через `session.post`.
    - Использует `proxy` и `headers` для настройки запроса.

2.  **Обработка ответа**:
    - Проверяет статус ответа с помощью `raise_for_status(response)`.
    - Извлекает данные из JSON-ответа с помощью `response.json()`.
    - Извлекает URL изображения из `response_data["data"][0]['url']`.

3.  **Формирование и возврат `ImageResponse`**:
    - Создает и возвращает объект `ImageResponse` с URL изображения и альтернативным текстом (prompt).

```mermaid
graph TD
    A[Начало create_async_generator] --> B{model in ("flux", "flux-dev")?};
    B -- Да --> C[FluxDev.create_async_generator];
    B -- Нет --> D{cls.default_model not in model?};
    D -- Да --> E[super().create_async_generator];
    D -- Нет --> F[Подготовка параметров (width, height, prompt, seed)];
    F --> G[Формирование payload];
    G --> H{api_key is None?};
    H -- Да --> I[Получение zerogpu_uuid и api_key];
    H -- Нет --> J[Создание headers];
    J --> K[Определение внутренней функции generate];
    K --> L[Создание асинхронной задачи task];
    L --> M[Цикл ожидания завершения задачи];
    M --> N{background_tasks is empty?};
    N -- Нет --> O[yield Reasoning(status)];
    O --> P[await asyncio.sleep(0.2)];
    P --> M;
    N -- Да --> Q[await task];
    Q --> R[yield await task (ImageResponse)];
    R --> S[yield Reasoning(status="Finished")];
    S --> T[Конец create_async_generator];
    I --> J;
    C --> T;
    E --> T;
```

**Примеры**:

1.  Генерация изображения с использованием модели `flux`:

```python
async for chunk in G4F.create_async_generator(
    model="flux",
    messages=[{"role": "user", "content": "Generate a cat image"}],
    width=512,
    height=512
):
    print(chunk)
```

2.  Генерация изображения с использованием модели `DeepseekAI_JanusPro7b.default_model`:

```python
async for chunk in G4F.create_async_generator(
    model=G4F.default_model,
    messages=[{"role": "user", "content": "Generate a dog image"}],
    width=512,
    height=512
):
    print(chunk)
```