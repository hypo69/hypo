# Модуль Aivvm

## Обзор

Модуль `Aivvm` предоставляет класс `Aivvm`, который является провайдером для взаимодействия с моделями GPT через API `chat.aivvm.com`. Он поддерживает потоковую передачу данных и модели GPT-3.5 Turbo и GPT-4.

## Подробней

Модуль содержит класс `Aivvm`, который наследуется от `AbstractProvider` и реализует метод `create_completion` для отправки запросов к API `chat.aivvm.com` и получения ответов от моделей GPT. Модуль также определяет словарь `models`, содержащий информацию о поддерживаемых моделях.

## Классы

### `Aivvm`

**Описание**: Класс `Aivvm` предоставляет интерфейс для взаимодействия с моделями GPT через API `chat.aivvm.com`.

**Принцип работы**:
Класс `Aivvm` наследуется от `AbstractProvider` и переопределяет метод `create_completion` для отправки запросов к API `chat.aivvm.com`. Он использует библиотеку `requests` для отправки POST-запросов и получения ответов.

**Параметры класса**:
- `url` (str): URL API `chat.aivvm.com`.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модели GPT-3.5 Turbo.
- `supports_gpt_4` (bool): Указывает, поддерживает ли провайдер модели GPT-4.

**Методы**:
- `create_completion`: Отправляет запрос к API `chat.aivvm.com` и возвращает ответ от модели GPT.

## Функции

### `create_completion`

```python
    @classmethod
    def create_completion(cls,
        model: str,
        messages: Messages,
        stream: bool,
        **kwargs
    ) -> CreateResult:
        """
        Создает запрос к API chat.aivvm.com и возвращает ответ от модели GPT.

        Args:
            model (str): Идентификатор модели GPT для использования.
            messages (Messages): Список сообщений для отправки в модель.
            stream (bool): Указывает, должна ли быть включена потоковая передача данных.
            **kwargs: Дополнительные аргументы для запроса.

        Returns:
            CreateResult: Результат запроса к API.

        Raises:
            ValueError: Если модель не поддерживается.

        Как работает функция:
         1. Проверяет, указана ли модель. Если нет, использует "gpt-3.5-turbo" по умолчанию.
         2. Проверяет, поддерживается ли указанная модель. Если нет, вызывает исключение ValueError.
         3. Формирует словарь json_data с данными для отправки в запросе.
         4. Преобразует словарь json_data в строку JSON.
         5. Формирует словарь headers с заголовками для запроса.
         6. Отправляет POST-запрос к API chat.aivvm.com с данными и заголовками.
         7. Обрабатывает ответ от API и возвращает его.

         Внутри функции происходят следующие действия и преобразования:
         A. Проверка и выбор модели.
         |
         B. Формирование данных запроса.
         |
         C. Отправка POST-запроса к API.
         |
         D. Обработка ответа от API.

        Примеры:
            Пример 1:
            model = "gpt-3.5-turbo"
            messages = [{"role": "user", "content": "Hello, how are you?"}]
            stream = True
            kwargs = {"temperature": 0.7}
            Aivvm.create_completion(model, messages, stream, **kwargs)

            Пример 2:
            model = "gpt-4"
            messages = [{"role": "user", "content": "Tell me a joke."}]
            stream = False
            kwargs = {}
            Aivvm.create_completion(model, messages, stream, **kwargs)
        """