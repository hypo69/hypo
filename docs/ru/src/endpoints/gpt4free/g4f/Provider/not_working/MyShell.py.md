# Модуль для работы с провайдером MyShell
## Обзор

Модуль `MyShell` предназначен для взаимодействия с сервисом MyShell AI через его API. Он предоставляет класс `MyShell`, который является подклассом `AbstractProvider` и реализует методы для отправки запросов к MyShell и получения ответов. Этот модуль поддерживает модели `gpt-3.5-turbo` и потоковую передачу данных.

## Подробнее

Модуль использует `WebDriverSession` для обхода Cloudflare и отправки запросов к API MyShell. Он форматирует сообщения, отправляет их в API и обрабатывает ответы, возвращая их в виде потока, если это поддерживается. Расположение модуля в структуре проекта `hypotez` указывает на его роль как одного из провайдеров для взаимодействия с различными AI-моделями.

## Классы

### `MyShell`

**Описание**: Класс `MyShell` предоставляет интерфейс для взаимодействия с сервисом MyShell AI.

**Наследует**:
- `AbstractProvider`: Наследует базовый класс для провайдеров, определяющий общие методы и атрибуты.

**Атрибуты**:
- `url` (str): URL-адрес сервиса MyShell AI.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий, поддерживает ли провайдер модель `gpt-3.5-turbo`.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.

**Методы**:
- `create_completion`: Метод для создания запроса к MyShell и получения ответа.

## Функции

### `create_completion`

```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool,
        proxy: str = None,
        timeout: int = 120,
        webdriver = None,
        **kwargs
    ) -> CreateResult:
        """ Функция создает запрос к MyShell и возвращает ответ.

        Args:
            model (str): Идентификатор модели, которую необходимо использовать.
            messages (Messages): Список сообщений для отправки в MyShell.
            stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            timeout (int, optional): Время ожидания ответа в секундах. По умолчанию 120.
            webdriver: Инстанс веб-драйвера для обхода защиты Cloudflare.
            **kwargs: Дополнительные аргументы.

        Returns:
            CreateResult: Результат запроса к MyShell.

        Raises:
            Exception: Если возникает ошибка при отправке запроса или обработке ответа.
        """
```

**Назначение**: Создание запроса к MyShell и получение ответа.

**Параметры**:
- `model` (str): Идентификатор модели, которую необходимо использовать.
- `messages` (Messages): Список сообщений для отправки в MyShell.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания ответа в секундах. По умолчанию 120.
- `webdriver` (webdriver): Инстанс веб-драйвера для обхода защиты Cloudflare.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `CreateResult`: Результат запроса к MyShell.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при отправке запроса или обработке ответа.

**Как работает функция**:

1.  **Инициализация**: Функция `create_completion` принимает параметры для настройки запроса к MyShell.
2.  **Обход Cloudflare**: Используется `WebDriverSession` для обхода защиты Cloudflare.
3.  **Формирование данных**: Создается словарь `data` с параметрами запроса, включая `botId`, `conversation_scenario` и `message`.
4.  **Отправка запроса**: С помощью JavaScript и `fetch` отправляется POST-запрос к API MyShell.
5.  **Обработка ответа**: Полученный ответ обрабатывается построчно, извлекаются данные из строк, начинающихся с `data:`, и возвращаются в виде потока.

```
Инициализация параметров
│
│
↓
Создание сессии WebDriver для обхода Cloudflare
│
│
↓
Формирование данных запроса (botId, conversation_scenario, message)
│
│
↓
Отправка POST-запроса к API MyShell через JavaScript fetch
│
│
↓
Обработка потока ответов, извлечение данных из строк 'data: '
│
│
↓
Возврат данных в виде потока (yield chunk)
```

**Примеры**:

```python
# Пример вызова функции create_completion
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, MyShell!"}]
stream = True
proxy = "http://your_proxy:8080"
timeout = 120
webdriver = None  # Здесь должен быть инстанс веб-драйвера

result = MyShell.create_completion(
    model=model, messages=messages, stream=stream, proxy=proxy, timeout=timeout, webdriver=webdriver
)
```
```python
#Второй пример вызова функции create_completion
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Как мне создать REST API?"}]
stream = False # Выключили стриминг
result = MyShell.create_completion(model=model, messages=messages, stream=stream)