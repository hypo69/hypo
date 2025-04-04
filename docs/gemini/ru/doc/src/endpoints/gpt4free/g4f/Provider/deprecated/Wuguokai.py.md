# Модуль `Wuguokai`

## Обзор

Модуль `Wuguokai` предоставляет интерфейс для взаимодействия с сервисом `chat.wuguokai.xyz`. Он реализует класс `Wuguokai`, который наследуется от `AbstractProvider` и предназначен для создания запросов к модели GPT-3.5 Turbo. Модуль использует библиотеку `requests` для отправки HTTP-запросов и модуль `random` для генерации случайных идентификаторов пользователей.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-провайдерами. Он предоставляет стандартизированный интерфейс для отправки запросов и получения ответов от AI-моделей. Модуль `Wuguokai` использует API `chat.wuguokai.xyz` для взаимодействия с GPT-3.5 Turbo.

## Классы

### `Wuguokai`

**Описание**: Класс `Wuguokai` предоставляет методы для взаимодействия с сервисом `chat.wuguokai.xyz`.

**Наследует**:
- `AbstractProvider`: Этот класс наследуется от `AbstractProvider`, который предоставляет базовый интерфейс для всех провайдеров в проекте `hypotez`.

**Атрибуты**:
- `url` (str): URL-адрес сервиса `chat.wuguokai.xyz`.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели GPT-3.5 Turbo.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.

**Методы**:
- `create_completion()`: Метод для создания запроса к AI-модели и получения ответа.

## Функции

### `create_completion`

```python
    @staticmethod
    def create_completion(
        model: str,
        messages: list[dict[str, str]],
        stream: bool,
        **kwargs: Any,
    ) -> CreateResult:
        """ Функция создает запрос к AI-модели и получает ответ.
        Args:
            model (str): Имя модели для использования.
            messages (list[dict[str, str]]): Список сообщений для отправки в запросе.
            stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
            **kwargs (Any): Дополнительные аргументы для передачи в запрос.

        Returns:
            CreateResult: Результат создания запроса.

        Raises:
            Exception: Если возникает ошибка при выполнении запроса.
        """
```

**Назначение**: Создает запрос к AI-модели и получает ответ.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (list[dict[str, str]]): Список сообщений для отправки в запросе.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
- `**kwargs` (Any): Дополнительные аргументы для передачи в запрос.

**Возвращает**:
- `CreateResult`: Результат создания запроса.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении запроса.

**Как работает функция**:
1. Формирует заголовки HTTP-запроса, включая `user-agent`, `content-type` и другие необходимые параметры.
2. Создает полезную нагрузку (payload) запроса, включая отформатированные сообщения, идентификатор пользователя и другие опции.
3. Отправляет POST-запрос к API `ai-api20.wuguokai.xyz/api/chat-process` с использованием библиотеки `requests`.
4. Обрабатывает ответ, разделяя его на части и возвращая содержимое.
5. В случае ошибки выбрасывает исключение с информацией о статусе и причине ошибки.

```
    Начало
    │
    ├── Заголовки HTTP-запроса (headers)
    │   │
    │   └── Формирование заголовков
    │
    ├── Полезная нагрузка (data)
    │   │
    │   ├── Форматирование сообщений (format_prompt)
    │   │
    │   └── Генерация случайного идентификатора пользователя (random.randint)
    │
    ├── POST-запрос (requests.post)
    │   │
    │   ├── Отправка запроса к API (ai-api20.wuguokai.xyz/api/chat-process)
    │   │
    │   └── Обработка ответа
    │
    ├── Разделение ответа (response.text.split)
    │   │
    │   └── Проверка статуса ответа (response.status_code)
    │
    └── Возврат результата или исключения
```

**Примеры**:

```python
# Пример вызова функции create_completion
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = False
kwargs = {"proxy": {}}

# Здесь требуется инстанс класса Wuguokai
# result = Wuguokai.create_completion(model=model, messages=messages, stream=stream, **kwargs)

# print(result)