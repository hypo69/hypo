# Модуль для работы с Hailuo AI
=================================================

Модуль содержит класс :class:`HailuoAI`, который используется для взаимодействия с Hailuo AI.

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [Conversation](#Conversation)
    - [HailuoAI](#HailuoAI)
- [Функции](#Функции)
    - [on_auth_async](#on_auth_async)
    - [create_authed](#create_authed)

## Обзор

Данный модуль предоставляет интерфейс для взаимодействия с Hailuo AI, включая аутентификацию и создание диалогов.

## Подробнее

Модуль `HailuoAI` предназначен для асинхронного взаимодействия с сервисом Hailuo AI. Он включает поддержку аутентификации, создания и ведения бесед, а также обработки ответов от сервера.
В данном коде используется вебдрайвер. Он импортируется из модуля `webdriver` проекта `hypotez`

```python
from src.webdirver import Driver, Chrome, Firefox, Playwright, ...
driver = Driver(Firefox)
```
После чего может использоваться как
```python
close_banner = {
  "attribute": null,
  "by": "XPATH",
  "selector": "//button[@id = 'closeXButton']",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": false,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": "click()",
  "locator_description": "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"
}

result = driver.execute_locator(close_banner)
```

## Классы

### `Conversation`
Описание назначения класса
    **Наследует** 
       `JsonConversation`

     **Аттрибуты**:
        - `token` (str): Токен аутентификации.
        - `chatID` (str): Идентификатор чата.
        - `characterID` (str): Идентификатор персонажа (по умолчанию 1).

     **Методы**:
         `__init__`: Конструктор класса.

#### `__init__`

```python
 def __init__(self, token: str, chatID: str, characterID: str = 1):
```
     Функция инициализирует объект класса `Conversation` с заданными параметрами.
     **Параметры**:
     - `token` (str): Токен аутентификации.
     - `chatID` (str): Идентификатор чата.
     - `characterID` (str): Идентификатор персонажа (по умолчанию 1).

     **Возвращает**:
     - `None`

     **Вызывает исключения**:
     - Отсутствуют.

     
     **Как работает функция**:
     1. Функция принимает токен, идентификатор чата и идентификатор персонажа в качестве аргументов.
     2. Сохраняет эти значения в атрибутах объекта для последующего использования.
     
     ```
     Инициализация -> Сохранение параметров
     ```
     **Примеры**:
     ```python
     conversation = Conversation(token="example_token", chatID="12345", characterID=2)
     ```

### `HailuoAI`

**Описание**: Класс для взаимодействия с Hailuo AI.
    **Наследует** 
       `AsyncAuthedProvider`, `ProviderModelMixin`

     **Аттрибуты**:
        - `label` (str): Метка провайдера ("Hailuo AI").
        - `url` (str): URL сервиса ("https://www.hailuo.ai").
        - `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
        - `use_nodriver` (bool): Флаг, указывающий на использование без драйвера (True).
        - `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи (True).
        - `default_model` (str): Модель по умолчанию ("MiniMax").

     **Методы**:
        - `on_auth_async`: Асинхронный метод для аутентификации.
        - `create_authed`: Асинхронный метод для создания аутентифицированного запроса.

## Функции

### `on_auth_async`

```python
    @classmethod
    async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
```

     **Назначение**: Асинхронный метод для аутентификации.

     **Параметры**:
     - `cls`: Ссылка на класс.
     - `proxy` (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
     - `**kwargs`: Дополнительные параметры.

     **Возвращает**:
     - `AsyncIterator`: Асинхронный итератор, возвращающий результаты аутентификации.

     **Вызывает исключения**:
     - Отсутствуют.
    
     **Как работает функция**:
     1. Функция пытается получить URL для логина из переменной окружения `G4F_LOGIN_URL`. Если URL найден, возвращает `RequestLogin`.
     2. Получает результаты обратного вызова браузера с использованием `get_browser_callback`.
     3. Возвращает результат аутентификации `AuthResult` с данными, полученными из `get_args_from_nodriver` и `callback_results`.
     
     ```
     Получение URL -> Получение результатов обратного вызова -> Возврат результата аутентификации
     ```
     **Примеры**:
     ```python
     async for result in HailuoAI.on_auth_async(proxy="http://proxy.example.com"):
         print(result)
     ```

### `create_authed`

```python
    @classmethod
    async def create_authed(
        cls,
        model: str,
        messages: Messages,
        auth_result: AuthResult,
        return_conversation: bool = False,
        conversation: Conversation = None,
        **kwargs
    ) -> AsyncResult:
```

     **Назначение**: Асинхронный метод для создания аутентифицированного запроса.

     **Параметры**:
     - `cls`: Ссылка на класс.
     - `model` (str): Используемая модель.
     - `messages` (Messages): Список сообщений для отправки.
     - `auth_result` (AuthResult): Результат аутентификации.
     - `return_conversation` (bool, optional): Флаг, указывающий на необходимость возврата объекта `Conversation`. По умолчанию `False`.
     - `conversation` (Conversation, optional): Объект `Conversation` для продолжения диалога. По умолчанию `None`.
     - `**kwargs`: Дополнительные параметры.

     **Возвращает**:
     - `AsyncResult`: Асинхронный результат запроса.

     **Вызывает исключения**:
     - Отсутствуют.
    
     **Как работает функция**:
     1. Извлекает параметры из `auth_result`.
     2. Создает или использует существующий объект `Conversation`.
     3. Формирует данные формы для отправки запроса.
     4. Генерирует заголовок `yy` с использованием `generate_yy_header`.
     5. Отправляет POST-запрос к сервису Hailuo AI.
     6. Обрабатывает ответы сервера, извлекая данные о заголовке чата, идентификаторе чата и содержании сообщения.
     7. Возвращает результаты в виде `TitleGeneration`, `Conversation` или содержимого сообщения.

     
     **Внутренние функции**:
     - Отсутствуют.
     
     ```
     Извлечение параметров -> Создание/использование объекта Conversation -> Формирование данных формы -> Генерация заголовка yy -> Отправка POST-запроса -> Обработка ответов -> Возврат результатов
     ```
     **Примеры**:
     ```python
     async for result in HailuoAI.create_authed(
         model="MiniMax",
         messages=[{"role": "user", "content": "Hello"}],
         auth_result=auth_result,
         return_conversation=True
     ):
         print(result)