# Модуль `EasyChat`

## Обзор

Модуль `EasyChat` предоставляет интерфейс для взаимодействия с сервисом EasyChat, который является провайдером для выполнения задач, связанных с генерацией текста. Этот модуль позволяет отправлять запросы к серверам EasyChat для получения ответов на основе предоставленных сообщений и параметров модели.

## Подробнее

Модуль определяет класс `EasyChat`, который наследуется от `AbstractProvider`. Он содержит настройки для подключения к сервису EasyChat, такие как URL, поддержку потоковой передачи данных и поддержку модели `gpt-3.5-turbo`. Модуль использует библиотеку `requests` для отправки HTTP-запросов к сервису.

## Классы

### `EasyChat(AbstractProvider)`

**Описание**: Класс `EasyChat` предоставляет интерфейс для взаимодействия с сервисом EasyChat.

**Наследует**:
- `AbstractProvider`: Этот класс наследуется от `AbstractProvider`, который, вероятно, является абстрактным классом, определяющим общий интерфейс для работы с различными провайдерами.

**Атрибуты**:
- `url` (str): URL-адрес сервиса EasyChat (`"https://free.easychat.work"`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-3.5-turbo` (`True`).
- `working` (bool): Показывает, работает ли провайдер (`False`).

**Методы**:
- `create_completion`: Отправляет запрос к сервису EasyChat для получения ответа на основе предоставленных сообщений и параметров модели.

## Функции

### `create_completion(model: str, messages: list[dict[str, str]], stream: bool, **kwargs: Any) -> CreateResult`

**Назначение**: Отправляет запрос к сервису EasyChat для получения ответа на основе предоставленных сообщений и параметров модели.

**Параметры**:
- `model` (str): Идентификатор используемой модели.
- `messages` (list[dict[str, str]]): Список сообщений, отправляемых в запросе.
- `stream` (bool): Указывает, использовать ли потоковую передачу данных.
- `**kwargs` (Any): Дополнительные параметры запроса.

**Возвращает**:
- `CreateResult`: Результат выполнения запроса. Тип `CreateResult` импортируется из `...typing`.

**Вызывает исключения**:
- `Exception`: Если получен код ответа, отличный от 200, или если в ответе нет данных.

**Внутренние функции**:
- Отсутствуют.

**Как работает функция**:

1. **Определение активных серверов**: Функция определяет список активных серверов EasyChat.
2. **Выбор сервера**: Выбирается случайный сервер из списка активных серверов.
3. **Формирование заголовков**: Формируются заголовки HTTP-запроса, включающие информацию о сервере, типе контента, User-Agent и другие параметры.
4. **Формирование данных запроса**: Формируются данные JSON, включающие сообщения, параметры модели (температура, штрафы и т.д.) и флаг потоковой передачи.
5. **Создание сессии**: Создается сессия `requests.Session()` для управления cookies.
6. **Инициализация cookies**: Отправляется GET-запрос к серверу для инициализации cookies.
7. **Отправка POST-запроса**: Отправляется POST-запрос к API EasyChat с заголовками и данными JSON.
8. **Обработка ответа**:
   - Если `stream` равен `False`:
     - Проверяется код ответа. Если он не равен 200, выбрасывается исключение.
     - Извлекаются данные JSON из ответа.
     - Если в данных есть ключ `"choices"`, извлекается содержимое первого сообщения и возвращается.
     - Если ключа `"choices"` нет, выбрасывается исключение.
   - Если `stream` равен `True`:
     - Обрабатывается потоковый ответ, разделяя его на части.
     - Из каждой части извлекается содержимое сообщения и возвращается.

```
Определение активных серверов
│
└───> Выбор сервера
│
└───> Формирование заголовков
│
└───> Формирование данных запроса
│
└───> Создание сессии
│
└───> Инициализация cookies
│
└───> Отправка POST-запроса
│
└───> Обработка ответа (stream=False)
│     │
│     └───> Проверка кода ответа
│     │
│     └───> Извлечение данных JSON
│     │
│     └───> Извлечение содержимого сообщения
│
└───> Обработка ответа (stream=True)
      │
      └───> Разделение потока на части
      │
      └───> Извлечение содержимого сообщения из каждой части
```

**Примеры**:

```python
# Пример использования функции create_completion
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = False
kwargs = {"temperature": 0.7}

result = EasyChat.create_completion(model, messages, stream, **kwargs)
if result:
    for r in result:
        print(r)