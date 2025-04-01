# Модуль `Koala`

## Обзор

Модуль `Koala` предоставляет асинхронный интерфейс для взаимодействия с сервисом `koala.sh` для генерации текста на основе предоставленных сообщений. Он использует `aiohttp` для выполнения асинхронных HTTP-запросов и предоставляет функциональность для работы с историей сообщений. Модуль входит в группу нерабочих провайдеров `gpt4free` проекта `hypotez`.

## Подробней

Этот модуль предназначен для интеграции с `koala.sh` как один из провайдеров в системе `hypotez`. Он обеспечивает асинхронную генерацию текста, отправляя запросы к API `koala.sh` и обрабатывая ответы в виде асинхронного генератора. Модуль поддерживает настройку прокси и использование истории сообщений для улучшения качества генерации.
Используется как один из провайдеров в `gpt4free`.

## Классы

### `Koala`

**Описание**: Класс `Koala` предоставляет функциональность асинхронного взаимодействия с сервисом `koala.sh` для генерации текста.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую реализацию асинхронного генератора.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдера.

**Атрибуты**:
- `url` (str): URL сервиса `koala.sh`.
- `api_endpoint` (str): URL API для взаимодействия с сервисом.
- `working` (bool): Указывает, работает ли провайдер в данный момент (в данном случае `False`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).

**Методы**:
- `create_async_generator()`: Создает асинхронный генератор для получения ответов от сервиса.
- `_parse_event_stream()`: Асинхронно обрабатывает поток событий ответа.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: Optional[str] = None,
    connector: Optional[BaseConnector] = None,
    **kwargs: Any
) -> AsyncGenerator[Dict[str, Union[str, int, float, List[Dict[str, Any]], None]], None]:
    """
    Создает асинхронный генератор для получения ответов от сервиса koala.sh.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.
        connector (Optional[BaseConnector], optional): Aiohttp коннектор. По умолчанию `None`.
        **kwargs (Any): Дополнительные аргументы.

    Returns:
        AsyncGenerator[Dict[str, Union[str, int, float, List[Dict[str, Any]], None]], None]: Асинхронный генератор, возвращающий словарь с результатами.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.
    """
    ...
```

**Назначение**: Создает и возвращает асинхронный генератор, который отправляет сообщения в API `koala.sh` и обрабатывает ответы для получения сгенерированного текста.

**Параметры**:
- `cls`: Ссылка на класс `Koala`.
- `model` (str): Имя используемой модели. Если не указано, используется `gpt-4o-mini`.
- `messages` (Messages): Список сообщений, отправляемых в API. Каждое сообщение содержит роль (`user`, `assistant`, `system`) и содержимое.
- `proxy` (Optional[str], optional): URL прокси-сервера для использования при подключении к API. По умолчанию `None`.
- `connector` (Optional[BaseConnector], optional): Пользовательский `aiohttp.BaseConnector` для управления соединениями. По умолчанию `None`.
- `**kwargs` (Any): Дополнительные параметры.

**Возвращает**:
- `AsyncGenerator[Dict[str, Union[str, int, float, List[Dict[str, Any]], None]], None]`: Асинхронный генератор, который выдает фрагменты данных, полученные от API. Каждый фрагмент представляет собой словарь.

**Как работает функция**:

1. **Подготовка заголовков**:
   - Создаются заголовки HTTP-запроса, включая `User-Agent`, `Accept`, `Referer` и другие необходимые параметры.
   - Генерируется случайный `Visitor-ID` для идентификации клиента.
2. **Подготовка данных**:
   - Из списка сообщений извлекается последний `input_text` и все сообщения с ролью `system` объединяются в строку.
   - Формируется словарь `data`, содержащий `input`, `inputHistory` и `outputHistory` на основе входных сообщений.
3. **Отправка запроса и обработка ответа**:
   - Открывается асинхронная сессия с использованием `aiohttp.ClientSession`.
   - Отправляется `POST` запрос к API `cls.api_endpoint` с подготовленными заголовками, данными и прокси (если указан).
   - Вызывается функция `raise_for_status` для проверки статуса ответа и выбрасывания исключения в случае ошибки.
   - Вызывается `cls._parse_event_stream` для обработки потока событий ответа и возвращения асинхронного генератора.

```
  Начало
     ↓
  Подготовка заголовков
     ↓
  Подготовка данных
     ↓
  Отправка POST-запроса к API
     ↓
  Обработка потока событий
     ↓
  Конец
```

**Примеры**:

```python
# Пример вызова функции с минимальными параметрами
async def example():
    messages = [{"role": "user", "content": "Hello"} ]
    async for chunk in Koala.create_async_generator(model="gpt-4o-mini", messages=messages):
        print(chunk)

# Пример вызова функции с указанием прокси
async def example_with_proxy():
    messages = [{"role": "user", "content": "Hello"}]
    async for chunk in Koala.create_async_generator(model="gpt-4o-mini", messages=messages, proxy="http://your_proxy:8080"):
        print(chunk)
```

### `_parse_event_stream`

```python
    @staticmethod
    async def _parse_event_stream(response: ClientResponse) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Асинхронно обрабатывает поток событий ответа от API koala.sh.

        Args:
            response (ClientResponse): Объект ответа от aiohttp.

        Returns:
            AsyncGenerator[Dict[str, Any], None]: Асинхронный генератор, возвращающий словарь с данными из каждого события.
        """
        ...
```

**Назначение**: Обрабатывает поток событий, полученный от API `koala.sh`, и извлекает данные из каждого события, возвращая их в виде словаря.

**Параметры**:
- `response` (ClientResponse): Объект ответа, полученный от `aiohttp.ClientSession`.

**Возвращает**:
- `AsyncGenerator[Dict[str, Any], None]`: Асинхронный генератор, который выдает словари, содержащие данные из каждого события.

**Как работает функция**:

1. **Итерация по содержимому ответа**:
   - Асинхронно итерируется по содержимому ответа (`response.content`), получая данные в виде чанков (bytes).
2. **Проверка начала чанка**:
   - Проверяет, начинается ли чанк с префикса `b"data: "`.
3. **Извлечение и преобразование данных**:
   - Если чанк начинается с `b"data: "`, извлекает данные, удаляя префикс `b"data: "`.
   - Преобразует извлеченные данные из формата JSON в словарь с помощью `json.loads()`.
   - Выдает полученный словарь.

```
  Начало
     ↓
  Итерация по содержимому ответа
     ↓
  Проверка начала чанка ("data: ")
     ├─ Да → Извлечение и преобразование данных (JSON в словарь)
     │     ↓
     └─ Нет
     ↓
  Конец
```

**Примеры**:

```python
# Пример использования _parse_event_stream
async def example_parse_event_stream(response: ClientResponse):
    async for event_data in Koala._parse_event_stream(response):
        print(event_data)