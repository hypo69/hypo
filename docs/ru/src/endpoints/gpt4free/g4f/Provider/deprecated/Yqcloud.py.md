# Модуль для работы с Yqcloud API (УСТАРЕВШИЙ)

## Обзор

Модуль `Yqcloud` предоставляет асинхронный генератор для взаимодействия с API Yqcloud (chat9.yqcloud.top), который, предположительно, предоставляет доступ к моделям, аналогичным GPT-3.5 Turbo. Этот модуль предназначен для получения ответов от модели в виде потока данных.
Модуль помечен как `deprecated`, что означает, что он не рекомендуется к использованию и может быть удален в будущем.

## Подобней

Модуль содержит класс `Yqcloud`, который является наследником `AsyncGeneratorProvider` и реализует метод `create_async_generator` для создания асинхронного генератора, который отправляет запросы к API Yqcloud и возвращает ответы в виде потока чанков.

## Классы

### `Yqcloud`

**Описание**: Класс для взаимодействия с API Yqcloud.

**Наследует**:

- `AsyncGeneratorProvider`: Предоставляет базовый интерфейс для асинхронных генераторов.

**Атрибуты**:

- `url` (str): URL API Yqcloud.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели GPT-3.5 Turbo.

**Методы**:

- `create_async_generator`: Создает асинхронный генератор для отправки запросов к API Yqcloud.

## Функции

### `_create_header`

```python
def _create_header():
    """
    Функция создает заголовок запроса для API Yqcloud.

    Returns:
        dict: Словарь с заголовками запроса.

    Как работает функция:
     1. Функция создает словарь с необходимыми заголовками для запроса к API Yqcloud.
     2. Возвращает этот словарь.
    """
    ...
```

**Назначение**: Функция создает заголовок запроса для API Yqcloud.

**Возвращает**:

- `dict`: Словарь с заголовками запроса.

**Как работает функция**:

```
Создание заголовков
│
↓
Возврат словаря заголовков
```

1.  Функция создает словарь с необходимыми заголовками для запроса к API Yqcloud, включая `accept`, `content-type`, `origin` и `referer`.
2.  Возвращает этот словарь.

**Примеры**:

```python
header = _create_header()
print(header)
# {'accept': 'application/json, text/plain, */*', 'content-type': 'application/json', 'origin': 'https://chat9.yqcloud.top', 'referer': 'https://chat9.yqcloud.top/'}
```

### `_create_payload`

```python
def _create_payload(
    messages: Messages,
    system_message: str = "",
    user_id: int = None,
    **kwargs
):
    """
    Функция создает полезную нагрузку (payload) для запроса к API Yqcloud.

    Args:
        messages (Messages): Список сообщений для отправки.
        system_message (str, optional): Системное сообщение. По умолчанию "".
        user_id (int, optional): ID пользователя. По умолчанию None.
        **kwargs: Дополнительные параметры.

    Returns:
        dict: Словарь с полезной нагрузкой для запроса.
    """
    ...
```

**Назначение**: Функция создает полезную нагрузку (payload) для запроса к API Yqcloud.

**Параметры**:

- `messages` (Messages): Список сообщений для отправки.
- `system_message` (str, optional): Системное сообщение. По умолчанию "".
- `user_id` (int, optional): ID пользователя. По умолчанию None.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:

- `dict`: Словарь с полезной нагрузкой для запроса.

**Как работает функция**:

```
Определение user_id
│
↓
Создание payload
│
↓
Возврат payload
```

1.  Функция проверяет, передан ли `user_id`. Если нет, генерирует случайный `user_id` в диапазоне от 1690000544336 до 2093025544336.
2.  Создает словарь `payload` с параметрами `prompt` (отформатированный список сообщений), `network`, `system` (системное сообщение), `withoutContext`, `stream` и `userId` (сформированный на основе `user_id`).
3.  Возвращает словарь `payload`.

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello"}]
payload = _create_payload(messages)
print(payload)
# {'prompt': 'Hello', 'network': True, 'system': '', 'withoutContext': False, 'stream': True, 'userId': '#/chat/1823456789012'}
```

### `create_async_generator`

```python
    @staticmethod
    async def create_async_generator(
        model: str,
        messages: Messages,
        proxy: str = None,
        timeout: int = 120,
        **kwargs,
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для отправки запросов к API Yqcloud.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Прокси-сервер. По умолчанию None.
            timeout (int, optional): Время ожидания запроса. По умолчанию 120.
            **kwargs: Дополнительные параметры.

        Yields:
            str: Часть ответа от API.

        Raises:
            RuntimeError: Если IP-адрес заблокирован системой защиты от злоупотреблений.
            Exception: В случае других ошибок при выполнении запроса.

        """
        ...
```

**Назначение**: Создает асинхронный генератор для отправки запросов к API Yqcloud.

**Параметры**:

- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса. По умолчанию `120`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, выдающий части ответа от API.

**Вызывает исключения**:

- `RuntimeError`: Если IP-адрес заблокирован системой защиты от злоупотреблений.
- `Exception`: В случае других ошибок при выполнении запроса.

**Как работает функция**:

```
Создание сессии
│
↓
Создание payload
│
↓
Отправка запроса
│
↓
Обработка ответа чанками
│
↓
Проверка на блокировку IP
│
↓
Выдача чанков ответа
```

1.  Функция создает асинхронную сессию с использованием `StreamSession` с заданными заголовками, прокси и таймаутом.
2.  Создает полезную нагрузку (`payload`) для запроса с использованием функции `_create_payload`.
3.  Отправляет POST-запрос к API Yqcloud (`https://api.aichatos.cloud/api/generateStream`) с созданной полезной нагрузкой.
4.  Обрабатывает ответ по частям (чанкам), декодирует каждый чанк и проверяет, не содержит ли он сообщение о блокировке IP-адреса.
5.  Если IP-адрес не заблокирован, выдает чанк ответа. В случае обнаружения блокировки IP-адреса, вызывает исключение `RuntimeError`.

**Примеры**:

```python
async def main():
    async for chunk in Yqcloud.create_async_generator(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}]):
        print(chunk, end="")

# asyncio.run(main())