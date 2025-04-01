# Модуль `Lockchat`

## Обзор

Модуль `Lockchat` предоставляет класс `Lockchat`, который является поставщиком (provider) для работы с API Lockchat. Он поддерживает стриминг, модели `gpt-3.5-turbo` и `gpt-4`. Lockchat использует API по адресу `http://supertest.lockchat.app`.

## Подробнее

Этот модуль предназначен для интеграции с Lockchat API для получения завершений чата. Он реализует метод `create_completion`, который отправляет запросы к API Lockchat и возвращает токены ответа. Модуль обрабатывает возможные ошибки, такие как отсутствие модели, и поддерживает стриминг ответов.

## Классы

### `Lockchat`

**Описание**: Класс `Lockchat` является поставщиком для работы с API Lockchat.

**Наследует**:
- `AbstractProvider`: Наследует от абстрактного класса `AbstractProvider`, предоставляющего базовый интерфейс для поставщиков.

**Атрибуты**:
- `url` (str): URL API Lockchat. Значение по умолчанию: `"http://supertest.lockchat.app"`.
- `supports_stream` (bool): Указывает, поддерживает ли поставщик стриминг. Значение по умолчанию: `True`.
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли поставщик модель `gpt-3.5-turbo`. Значение по умолчанию: `True`.
- `supports_gpt_4` (bool): Указывает, поддерживает ли поставщик модель `gpt-4`. Значение по умолчанию: `True`.

**Методы**:
- `create_completion`: Статический метод для создания завершения чата.

## Функции

### `create_completion`

```python
    @staticmethod
    def create_completion(
        model: str,
        messages: list[dict[str, str]],
        stream: bool, **kwargs: Any) -> CreateResult:
        """ Функция отправляет запрос к API Lockchat для создания завершения чата.
        Args:
            model (str): Имя используемой модели.
            messages (list[dict[str, str]]): Список сообщений в формате словаря, где каждый словарь содержит роли и контент сообщений.
            stream (bool): Указывает, должен ли ответ быть в режиме стриминга.
            **kwargs (Any): Дополнительные аргументы, такие как температура.

        Returns:
            CreateResult: Генератор токенов ответа.

        Raises:
            requests.exceptions.HTTPError: Если HTTP-запрос завершается с ошибкой.

        Как работает функция:
         1. **Подготовка полезной нагрузки**:
            - Извлекает значение температуры из `kwargs` или использует значение по умолчанию 0.7.
            - Создает полезную нагрузку (payload) с температурой, сообщениями, моделью и флагом стриминга.

         2. **Отправка запроса к API**:
            - Определяет заголовки, включая User-Agent.
            - Отправляет POST-запрос к API Lockchat с полезной нагрузкой и заголовками.

         3. **Обработка ответа**:
            - Генерирует исключение для HTTP-ошибок.
            - Итерируется по строкам ответа.
            - Обрабатывает ошибку, если модель не существует, и повторяет запрос.
            - Извлекает контент из токенов и возвращает его с использованием `yield`.

        Внутри функции происходят следующие действия и преобразования:
             A - Извлечение параметров запроса и формирование payload
             |
             -- B - Отправка POST запроса к API Lockchat
             |
             C - Обработка ответа: проверка на ошибки, извлечение и передача контента

        Примеры:
            >>> model = "gpt-3.5-turbo"
            >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
            >>> stream = True
            >>> for token in Lockchat.create_completion(model=model, messages=messages, stream=stream):
            ...     print(token, end="")
            I am doing well, thank you for asking. How can I assist you today?
        """
        temperature = float(kwargs.get("temperature", 0.7))
        payload = {
            "temperature": temperature,
            "messages"   : messages,
            "model"      : model,
            "stream"     : True,
        }

        headers = {
            "user-agent": "ChatX/39 CFNetwork/1408.0.4 Darwin/22.5.0",
        }
        response = requests.post("http://supertest.lockchat.app/v1/chat/completions",
                                 json=payload, headers=headers, stream=True)

        response.raise_for_status()
        for token in response.iter_lines():
            if b"The model: `gpt-4` does not exist" in token:
                print("error, retrying...")
                
                Lockchat.create_completion(
                    model       = model,
                    messages    = messages,
                    stream      = stream,
                    temperature = temperature,
                    **kwargs)

            if b"content" in token:
                token = json.loads(token.decode("utf-8").split("data: ")[1])
                token = token["choices"][0]["delta"].get("content")

                if token:
                    yield (token)