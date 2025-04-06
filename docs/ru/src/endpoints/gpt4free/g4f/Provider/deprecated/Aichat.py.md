# Модуль `Aichat.py`

## Обзор

Модуль `Aichat.py` представляет собой асинхронный провайдер для взаимодействия с сервисом `chat-gpt.org`. Он предоставляет функциональность для создания асинхронных запросов к API `chat-gpt.org` с использованием предоставленных cookies и прокси (при необходимости). Модуль поддерживает модель `gpt-3.5-turbo`.

## Подробнее

Модуль предназначен для интеграции с другими частями проекта `hypotez`, требующими взаимодействия с `chat-gpt.org`. Он использует асинхронные запросы для неблокирующей работы и поддерживает установку cookies для аутентификации.

## Классы

### `Aichat`

**Описание**: Класс `Aichat` является асинхронным провайдером.

**Наследует**:
- `AsyncProvider`: Наследует функциональность асинхронного провайдера.

**Атрибуты**:
- `url` (str): URL для взаимодействия с `chat-gpt.org` (`"https://chat-gpt.org/chat"`).
- `working` (bool): Флаг, указывающий на работоспособность провайдера (изначально `False`).
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-3.5-turbo` (установлен в `True`).

### `create_async`

```python
    @staticmethod
    async def create_async(
        model: str,
        messages: Messages,
        proxy: str = None, **kwargs) -> str:
        """
        Асинхронно создает запрос к chat-gpt.org и возвращает ответ.

        Args:
            model (str): Название модели.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
            **kwargs: Дополнительные аргументы, такие как `cookies`, `temperature`, `top_p`.

        Returns:
            str: Текст ответа от chat-gpt.org.

        Raises:
            RuntimeError: Если не удалось получить cookies.
            Exception: Если получен ошибочный ответ от API.
        """
```

**Параметры**:
- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений, отправляемых в запросе.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, такие как cookies, temperature и top_p.

**Возвращает**:
- `str`: Текст ответа, полученный от `chat-gpt.org`.

**Вызывает исключения**:
- `RuntimeError`: Если не удалось получить cookies.
- `Exception`: Если ответ от API содержит ошибку.

**Как работает функция**:

1. **Получение Cookies**:
   - Проверяет, переданы ли cookies через `kwargs`. Если нет, пытается получить их с помощью функции `get_cookies('chat-gpt.org')`.
   - Если cookies получить не удалось, вызывает исключение `RuntimeError`.
2. **Подготовка Заголовков**:
   - Определяет заголовки HTTP-запроса, включая `authority`, `accept`, `content-type`, `origin`, `referer`, `sec-ch-ua`, `user-agent` и другие.
3. **Создание Асинхронной Сессии**:
   - Создает асинхронную сессию с использованием `StreamSession`. Устанавливает заголовки, cookies, таймаут, прокси (если указан) и параметры impersonate и verify.
4. **Подготовка JSON-данных**:
   - Форматирует сообщения с помощью `format_prompt(messages)` и подготавливает JSON-данные для отправки, включая `message`, `temperature`, `presence_penalty`, `top_p`, `frequency_penalty`.
5. **Отправка POST-запроса**:
   - Отправляет POST-запрос к `https://chat-gpt.org/api/text` с JSON-данными.
6. **Обработка Ответа**:
   - Проверяет статус ответа и вызывает исключение `HTTPError`, если статус указывает на ошибку.
   - Извлекает JSON из ответа и проверяет поле `response`. Если `response` отсутствует или является ложным, вызывает исключение `Exception`.
   - Возвращает значение поля `message` из JSON-ответа.

```
   +-----------------------+
   |  Получение Cookies    |
   +-----------------------+
        |
        V
   +-----------------------+
   |  Подготовка Заголовков |
   +-----------------------+
        |
        V
   +-----------------------+
   |  Создание Async Session |
   +-----------------------+
        |
        V
   +-----------------------+
   |  Подготовка JSON  |
   +-----------------------+
        |
        V
   +-----------------------+
   |  Отправка POST-запроса |
   +-----------------------+
        |
        V
   +-----------------------+
   |  Обработка  |
   +-----------------------+
        |
        V
   +-----------------------+
   |  Возврат результата   |
   +-----------------------+
```

**Примеры**:

```python
# Пример вызова функции create_async
messages = [{"role": "user", "content": "Hello, world!"}]
#Предполагается, что get_cookies возвращает валидные cookies
#cookies = get_cookies('chat-gpt.org') 
#Если cookies не переданы, они будут запрошены автоматически

#async def main():
#    try:
#        response = await Aichat.create_async(model="gpt-3.5-turbo", messages=messages, temperature=0.7, cookies=cookies)
#        print(response)
#    except Exception as ex:
#        print(f"Error: {ex}")

#Пример с использованием прокси
#async def main():
#    try:
#        response = await Aichat.create_async(model="gpt-3.5-turbo", messages=messages, proxy="http://your_proxy:8080", temperature=0.7)
#        print(response)
#    except Exception as ex:
#        print(f"Error: {ex}")