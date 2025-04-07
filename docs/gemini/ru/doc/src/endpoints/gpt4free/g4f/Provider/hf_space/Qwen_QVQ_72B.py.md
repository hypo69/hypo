# Модуль `Qwen_QVQ_72B`

## Обзор

Модуль `Qwen_QVQ_72B` предоставляет асинхронный интерфейс для взаимодействия с моделью Qwen QVQ-72B, размещенной на платформе Hugging Face Space. Он позволяет отправлять текстовые запросы и изображения для получения ответов от модели. Модуль поддерживает как текстовые, так и мультимодальные запросы.

## Подробнее

Модуль `Qwen_QVQ_72B` является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, использующими возможности модели Qwen QVQ-72B. Он использует асинхронные запросы для эффективной работы с API и предоставляет удобный интерфейс для отправки запросов и получения результатов. Модуль включает в себя обработку ошибок и поддержку прокси-серверов.

## Классы

### `Qwen_QVQ_72B`

**Описание**: Класс `Qwen_QVQ_72B` предоставляет методы для взаимодействия с моделью Qwen QVQ-72B.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию ответов.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Qwen QVQ-72B"`.
- `url` (str): URL платформы Hugging Face Space, `"https://qwen-qvq-72b-preview.hf.space"`.
- `api_endpoint` (str): URL API endpoint, `"/gradio_api/call/generate"`.
- `working` (bool): Флаг, указывающий, что провайдер работает, `True`.
- `default_model` (str): Модель по умолчанию, `"qwen-qvq-72b-preview"`.
- `default_vision_model` (str): Модель для обработки изображений по умолчанию, `"qwen-qvq-72b-preview"`.
- `model_aliases` (dict): Псевдонимы моделей, `{"qvq-72b": default_vision_model}`.
- `vision_models` (list): Список моделей для обработки изображений, список ключей из `model_aliases`.
- `models` (list): Список поддерживаемых моделей, идентичен `vision_models`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для отправки запросов к модели.

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls, model: str, messages: Messages,
        media: MediaListType = None,
        api_key: str = None, 
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для взаимодействия с моделью Qwen QVQ-72B.

        Args:
            model (str): Название модели.
            messages (Messages): Список сообщений для отправки.
            media (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
            api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от модели.

        Raises:
            ResponseError: Если GPU token limit превышен.
            RuntimeError: Если не удалось прочитать ответ.
        """
```

**Назначение**: Создает асинхронный генератор для отправки запросов к модели Qwen QVQ-72B.

**Параметры**:
- `cls`: Ссылка на класс `Qwen_QVQ_72B`.
- `model` (str): Название модели.
- `messages` (Messages): Список сообщений для отправки.
- `media` (MediaListType, optional): Список медиафайлов для отправки. По умолчанию `None`.
- `api_key` (str, optional): API-ключ для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от модели.

**Вызывает исключения**:
- `ResponseError`: Если GPU token limit превышен.
- `RuntimeError`: Если не удалось прочитать ответ.

**Как работает функция**:

1. **Инициализация заголовков**: Создаются заголовки запроса, включая `Accept` и `Authorization` (если предоставлен `api_key`).
2. **Создание асинхронной сессии**: Используется `ClientSession` для выполнения асинхронных HTTP-запросов.
3. **Обработка медиафайлов (если есть)**:
   - Если предоставлены медиафайлы (`media`):
     - Создается `FormData` для отправки файлов.
     - Преобразует медиафайл в байты и добавляет его в `FormData`.
     - Выполняется POST-запрос к API для загрузки файла.
     - Полученный путь к изображению добавляется в данные запроса.
   - Если медиафайлы отсутствуют, данные запроса формируются только на основе текстовых сообщений.
4. **Отправка запроса к API**:
   - Выполняется POST-запрос к API endpoint (`cls.api_endpoint`) с данными запроса.
   - Полученный `event_id` используется для получения потоковых ответов.
5. **Получение потоковых ответов**:
   - Выполняется GET-запрос к API endpoint с `event_id`.
   - Асинхронно читаются чанки данных из ответа.
   - Обрабатываются события (`event`) в чанках данных:
     - Если `event` равен `"error"`, выбрасывается исключение `ResponseError`.
     - Если `event` равен `"complete"` или `"generating"`, данные JSON парсятся.
     - Если `event` равен `"generating"`, извлекается текст из данных и возвращается как часть генератора.
     - Если `event` равен `"complete"`, цикл завершается.

```
   Начало
     ↓
   Инициализация заголовков
     ↓
   Создание асинхронной сессии
     ↓
   Проверка наличия медиафайлов
     ├── Да ── Создание FormData → Загрузка файла → Получение пути к изображению
     │   
     └── Нет ── Формирование данных запроса без медиафайлов
     ↓
   Отправка POST-запроса к API
     ↓
   Получение event_id
     ↓
   Отправка GET-запроса для потоковых ответов
     ↓
   Чтение чанков данных
     ↓
   Обработка событий (error, complete, generating)
     ↓
   Выдача данных генератора или завершение
     ↓
   Конец
```

**Примеры**:

```python
# Пример использования с текстовыми сообщениями
messages = [{"role": "user", "content": "Hello, Qwen!"}]
async for chunk in Qwen_QVQ_72B.create_async_generator(model="qwen-qvq-72b-preview", messages=messages):
    print(chunk, end="")

# Пример использования с медиафайлами
from pathlib import Path
image_path = Path("image.jpg")  # Замените на путь к вашему изображению
media = [("image/jpeg", image_path.name, image_path.read_bytes())]
messages = [{"role": "user", "content": "Describe this image."}]
async for chunk in Qwen_QVQ_72B.create_async_generator(model="qwen-qvq-72b-preview", messages=messages, media=media):
    print(chunk, end="")