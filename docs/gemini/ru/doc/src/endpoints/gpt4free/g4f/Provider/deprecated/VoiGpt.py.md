# Модуль VoiGpt

## Обзор

Модуль `VoiGpt` предоставляет класс `VoiGpt`, который является провайдером для взаимодействия с сайтом VoiGpt.com. Этот модуль позволяет отправлять запросы к VoiGpt и получать ответы, используя токен CSRF для аутентификации. Модуль поддерживает работу с моделью `gpt-3.5-turbo`, историю сообщений и не поддерживает потоковую передачу данных.

## Подробней

Этот модуль предназначен для использования в проекте `hypotez` для обеспечения взаимодействия с сервисом VoiGpt. Для работы с этим провайдером необходимо получить CSRF токен/cookie с сайта voigpt.com.

## Классы

### `VoiGpt(AbstractProvider)`

**Описание**: Класс `VoiGpt` является провайдером для VoiGpt.com.

**Наследует**:
- `AbstractProvider`: Абстрактный класс-провайдер, определяющий интерфейс для всех провайдеров в проекте.

**Атрибуты**:
- `url` (str): URL сайта VoiGpt.com.
- `working` (bool): Указывает, работает ли провайдер в данный момент (по умолчанию `False`).
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-3.5-turbo` (по умолчанию `True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (по умолчанию `True`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (по умолчанию `False`).
- `_access_token` (str): Приватный атрибут для хранения CSRF токена.

### `create_completion`

```python
    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool,
        proxy: str = None,
        access_token: str = None,
        **kwargs
    ) -> CreateResult:
        """
        Создает запрос к VoiGpt.com и возвращает результат.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            stream (bool): Определяет, использовать ли потоковую передачу.
            proxy (str, optional): Прокси для использования. По умолчанию `None`.
            access_token (str, optional): CSRF токен для аутентификации. По умолчанию `None`.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            CreateResult: Объект, содержащий результат запроса.

        Raises:
            RuntimeError: Если получен некорректный ответ от сервера.
        """
        if not model:
            model = "gpt-3.5-turbo"
        if not access_token:
            access_token = cls._access_token
        if not access_token:
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "de-DE,de;q=0.9,en-DE;q=0.8,en;q=0.7,en-US;q=0.6",
                "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Linux\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            }
            req_response = requests.get(cls.url, headers=headers)
            access_token = cls._access_token = req_response.cookies.get("csrftoken")

        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "de-DE,de;q=0.9,en-DE;q=0.8,en;q=0.7,en-US;q=0.6",
            "Cookie": f"csrftoken={access_token};",
            "Origin": "https://voigpt.com",
            "Referer": "https://voigpt.com/",
            "Sec-Ch-Ua": "'Google Chrome';v='119', 'Chromium';v='119', 'Not?A_Brand';v='24'",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "'Windows'",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "X-Csrftoken": access_token,
        }

        payload = {
            "messages": messages,
        }
        request_url = f"{cls.url}/generate_response/"
        req_response = requests.post(request_url, headers=headers, json=payload)
        try:
            response = json.loads(req_response.text)
            yield response["response"]
        except:
            raise RuntimeError(f"Response: {req_response.text}")
```

**Назначение**: Создает запрос к VoiGpt.com и возвращает результат.

**Параметры**:
- `model` (str): Модель для использования. Если не указана, используется `"gpt-3.5-turbo"`.
- `messages` (Messages): Список сообщений для отправки.
- `stream` (bool): Определяет, использовать ли потоковую передачу. В данном классе всегда `False`.
- `proxy` (str, optional): Прокси для использования. По умолчанию `None`.
- `access_token` (str, optional): CSRF токен для аутентификации. Если не указан, используется сохраненный токен или получается новый. По умолчанию `None`.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `CreateResult`: Объект, содержащий результат запроса. В данном случае возвращается генератор, выдающий текст ответа.

**Вызывает исключения**:
- `RuntimeError`: Если получен некорректный ответ от сервера.

**Как работает функция**:

1.  **Инициализация**:
    *   Проверяет, указана ли модель. Если нет, устанавливает значение по умолчанию `"gpt-3.5-turbo"`.
    *   Проверяет, передан ли токен доступа (`access_token`). Если нет, пытается использовать сохраненный токен (`cls._access_token`). Если и он отсутствует, запрашивает новый токен с сайта.
2.  **Получение CSRF-токена (при необходимости)**:
    *   Если `access_token` не предоставлен, функция отправляет GET-запрос на главную страницу `cls.url` для получения CSRF-токена.
    *   Заголовки запроса включают информацию о браузере и типе запроса.
    *   Полученный CSRF-токен извлекается из cookies ответа и сохраняется в `cls._access_token`.
3.  **Формирование заголовков запроса**:
    *   Создаются заголовки `headers` для последующего POST-запроса.
    *   В `headers` включается CSRF-токен в виде cookie и в поле `X-Csrftoken`.
4.  **Формирование полезной нагрузки (payload)**:
    *   Создается словарь `payload`, содержащий сообщения (`messages`), которые необходимо отправить.
5.  **Отправка POST-запроса**:
    *   Формируется URL запроса `request_url` путем добавления `/generate_response/` к базовому URL `cls.url`.
    *   Отправляется POST-запрос на `request_url` с заголовками `headers` и полезной нагрузкой `payload`.
6.  **Обработка ответа**:
    *   Пытается извлечь текст ответа из JSON-формата, используя `json.loads(req_response.text)`.
    *   Извлекает значение ключа `"response"` из полученного JSON-объекта.
    *   Возвращает (через `yield`) извлеченный текст ответа.
7.  **Обработка ошибок**:
    *   Если в процессе обработки ответа возникает исключение (например, не удается распарсить JSON), возбуждается исключение `RuntimeError` с текстом ответа от сервера.

**Внутренние функции**: Нет

**ASCII-схема работы функции**:

```
    Начало
     ↓
    Проверка наличия model и access_token
     ↓
    Если access_token отсутствует:
     →  Запрос CSRF-токена с сайта
     ↓
    Формирование заголовков запроса
     ↓
    Формирование payload с сообщениями
     ↓
    Отправка POST-запроса на /generate_response/
     ↓
    Попытка извлечения ответа из JSON
     ↓
    Успех: →  Возврат текста ответа через yield
     ↓
    Ошибка: →  Выброс RuntimeError с текстом ответа
     ↓
    Конец
```

**Примеры**:

Пример 1:
```python
from typing import List, Dict, Generator

class MockMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_dict(self) -> Dict[str, str]:
        return {"role": self.role, "content": self.content}

Messages = List[MockMessage]

class MockCreateResult:
    def __init__(self, result: str):
        self.result = result
    def __iter__(self) -> Generator[str, None, None]:
            yield self.result

# Создаем список сообщений
messages: Messages = [
    MockMessage(role="user", content="Hello, how are you?").to_dict(),
    MockMessage(role="assistant", content="I am fine, thank you!").to_dict()
]

# Запускаем  create_completion с минимальным набором параметров
# Внимание: для реальной работы требуется действительный CSRF-токен
# и возможно, потребуется настройка прокси
try:
    # Mocking access_token
    VoiGpt._access_token = "test_csrf_token"

    result: MockCreateResult = VoiGpt.create_completion(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=False,
    )
    print(next(iter(result)))  # Вывод результата
except RuntimeError as ex:
    print(f"Ошибка: {ex}")
```

Пример 2:
```python
from typing import List, Dict, Generator

class MockMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_dict(self) -> Dict[str, str]:
        return {"role": self.role, "content": self.content}

Messages = List[MockMessage]

class MockCreateResult:
    def __init__(self, result: str):
        self.result = result
    def __iter__(self) -> Generator[str, None, None]:
            yield self.result

# Создаем список сообщений
messages: Messages = [
    MockMessage(role="user", content="Привет, как дела?").to_dict(),
    MockMessage(role="assistant", content="У меня все хорошо, спасибо!").to_dict()
]

# Запускаем  create_completion с указанием прокси и токена
# Внимание: для реальной работы требуется действительный CSRF-токен
# и корректные настройки прокси
try:
    # Mocking access_token
    VoiGpt._access_token = "test_csrf_token"

    result: MockCreateResult = VoiGpt.create_completion(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=False,
        proxy="http://your_proxy:8080",
        access_token="your_csrf_token"
    )
    print(next(iter(result)))  # Вывод результата
except RuntimeError as ex:
    print(f"Ошибка: {ex}")
```

В обоих примерах предполагается, что `Messages` и `CreateResult` - это классы, определенные в других модулях.
Для целей тестирования я использовал `MockMessage` и `MockCreateResult`. Обратите внимание, что для реального использования
потребуется действительный CSRF-токен и, возможно, настроенный прокси-сервер.