# Модуль `G4F`

## Обзор

Модуль `G4F` предоставляет класс `G4F`, который является частью фреймворка для взаимодействия с различными моделями, включая `flux` и `DeepseekAI_JanusPro7b`. Он предназначен для генерации изображений на основе текстовых запросов, используя API Hugging Face Spaces.

## Подробней

Модуль содержит класс `G4F`, который наследует функциональность от `DeepseekAI_JanusPro7b` и `BlackForestLabs_Flux1Dev`. Он обеспечивает возможность генерации изображений, используя различные модели, размещенные на Hugging Face Spaces. Модуль также включает методы для получения токенов GPU и форматирования запросов изображений.

## Классы

### `FluxDev`

**Описание**: Класс `FluxDev` предоставляет методы для работы с моделью `FLUX.1-dev` от Black Forest Labs, размещенной на Hugging Face Spaces.

### `G4F`

**Описание**: Класс `G4F` расширяет возможности `DeepseekAI_JanusPro7b` и `BlackForestLabs_Flux1Dev`, предоставляя методы для генерации изображений с использованием различных моделей, включая `flux`.

**Наследует**:
- `DeepseekAI_JanusPro7b`: Предоставляет базовую функциональность для взаимодействия с моделями DeepseekAI.
- `BlackForestLabs_Flux1Dev`: Предоставляет методы для работы с моделью `FLUX.1-dev` от Black Forest Labs.

**Атрибуты**:
- `url` (str): URL для доступа к Hugging Face Space.
- `space` (str): Имя Hugging Face Space.
- `referer` (str): Referer для HTTP-запросов.
- `default_model` (str): Модель по умолчанию ("flux").
- `model_aliases` (dict): Псевдонимы моделей.
- `image_models` (list): Список моделей, поддерживающих генерацию изображений.
- `models` (list): Список всех поддерживаемых моделей.

**Методы**:
- `create_async_generator`: Асинхронный генератор для создания изображений на основе текстового запроса.

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
        Асинхронный генератор для создания изображений на основе текстового запроса.

        Args:
            model (str): Название модели для генерации изображения.
            messages (Messages): Список сообщений для формирования запроса.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            cookies (dict, optional): Cookie для HTTP-запросов. По умолчанию `None`.
            api_key (str, optional): API ключ для доступа к сервису. По умолчанию `None`.
            zerogpu_uuid (str, optional): UUID для ZeroGPU. По умолчанию "[object Object]".
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий результаты генерации изображения.

        Raises:
            Exception: Если возникает ошибка при генерации изображения.
        """
        ...
```

**Как работает функция**:

1. **Обработка выбора модели**: Функция проверяет, какую модель следует использовать для генерации изображения. Если выбрана модель "flux" или "flux-dev", она делегирует обработку классу `FluxDev`. Если выбрана модель, отличная от `default_model` класса `G4F`, она делегирует обработку родительскому классу (`DeepseekAI_JanusPro7b`).

2. **Подготовка параметров**: Если используется модель `default_model` класса `G4F`, функция подготавливает параметры для запроса. Это включает корректировку ширины и высоты изображения, форматирование текстового запроса и генерацию случайного зерна, если оно не предоставлено.

3. **Формирование payload**: Функция формирует словарь `payload`, который содержит данные для запроса к API Hugging Face Space. Этот словарь включает текстовый запрос, зерно, ширину, высоту и другие параметры.

4. **Асинхронный запрос**: Функция создает асинхронную сессию с использованием `aiohttp.ClientSession` и выполняет POST-запрос к API Hugging Face Space. Перед этим она получает токен GPU, если `api_key` не предоставлен.

5. **Генерация изображения**: Функция отправляет запрос и обрабатывает ответ, возвращая URL сгенерированного изображения. В процессе генерации она также возвращает промежуточные статусы, используя `Reasoning`.

6. **Асинхронный генератор**: Функция использует асинхронный генератор для возврата промежуточных результатов и статусов, позволяя вызывающему коду отслеживать прогресс генерации изображения.

**Внутренние функции**:

- **generate()**:
    ```python
    async def generate():
        """
        Выполняет асинхронный POST-запрос к API Hugging Face Space и возвращает URL сгенерированного изображения.

        Returns:
            ImageResponse: Объект ImageResponse, содержащий URL изображения и альтернативный текст.

        Raises:
            Exception: Если возникает ошибка при выполнении запроса.
        """
        ...
    ```

    **Как работает внутренняя функция `generate()`**:

    1. **Выполнение POST-запроса**: Функция выполняет асинхронный POST-запрос к `cls.url_flux` с использованием `aiohttp.ClientSession`. Запрос включает JSON-payload с параметрами генерации изображения, а также заголовки, содержащие токен GPU и UUID.

    2. **Обработка ответа**: После получения ответа функция проверяет статус код с помощью `raise_for_status` и преобразует тело ответа в JSON.

    3. **Извлечение URL изображения**: Из JSON-ответа извлекается URL сгенерированного изображения.

    4. **Возврат ImageResponse**: Функция возвращает объект `ImageResponse`, который содержит URL изображения и альтернативный текст (prompt).

     A
     ↓
     Получение токена GPU (если api_key отсутствует)
     ↓
     → Формирование headers (x-zerogpu-token, x-zerogpu-uuid)
     ↓
     B = POST запрос к API Hugging Face Space (cls.url_flux)
     ↓
     C = Обработка ответа (проверка статус кода, преобразование в JSON)
     ↓
     D = Извлечение URL изображения из JSON
     ↓
     E = Создание и возврат ImageResponse(image_url, alt=prompt)
     ↓
     F

**Примеры**:

1. Генерация изображения с использованием модели `flux`:

```python
async for chunk in G4F.create_async_generator(
    model="flux",
    messages=[{"role": "user", "content": "A beautiful landscape"}],
    width=512,
    height=512
):
    print(chunk)
```

2. Генерация изображения с использованием модели `DeepseekAI_JanusPro7b.default_image_model`:

```python
async for chunk in G4F.create_async_generator(
    model=DeepseekAI_JanusPro7b.default_image_model,
    messages=[{"role": "user", "content": "A futuristic city"}],
    width=512,
    height=512,
    api_key="your_api_key"
):
    print(chunk)