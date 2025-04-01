# Модуль `CodeLinkAva`

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с API CodeLinkAva, который использует модель GPT-3.5 Turbo. Он позволяет отправлять сообщения и получать ответы в режиме реального времени.

## Подробней

Модуль `CodeLinkAva` является частью проекта `hypotez` и предназначен для работы с API CodeLinkAva. Он использует библиотеку `aiohttp` для выполнения асинхронных HTTP-запросов и предоставляет асинхронный генератор, который позволяет получать ответы от API в режиме реального времени. Модуль поддерживает модель GPT-3.5 Turbo и может быть использован для различных задач, таких как чат-боты, ответы на вопросы и т.д.

## Классы

### `CodeLinkAva`

**Описание**: Класс `CodeLinkAva` является провайдером асинхронного генератора.

**Принцип работы**:
Класс наследует `AsyncGeneratorProvider` и переопределяет метод `create_async_generator` для создания асинхронного генератора, который взаимодействует с API CodeLinkAva.

**Атрибуты**:
- `url` (str): URL API CodeLinkAva.
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель GPT-3.5 Turbo.
- `working` (bool): Указывает, работает ли провайдер в данный момент.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с API CodeLinkAva.

## Функции

### `create_async_generator`

```python
    async def create_async_generator(
        cls,
        model: str,
        messages: list[dict[str, str]],
        **kwargs
    ) -> AsyncGenerator:
        """Создает асинхронный генератор для взаимодействия с API CodeLinkAva.

        Args:
            model (str): Название модели.
            messages (list[dict[str, str]]): Список сообщений для отправки в API.
            **kwargs: Дополнительные аргументы для отправки в API.

        Returns:
            AsyncGenerator: Асинхронный генератор, который выдает ответы от API.

        Как работает функция:
        1. Функция `create_async_generator` создает асинхронный генератор, который взаимодействует с API CodeLinkAva для получения ответов на основе предоставленных сообщений.
        2. Внутри функции устанавливаются заголовки HTTP-запроса, необходимые для взаимодействия с API.
        3. Создается асинхровая сессия с использованием `aiohttp.ClientSession` для отправки запросов.
        4. Формируется тело запроса `data`, включающее сообщения, температуру и другие параметры.
        5. Отправляется POST-запрос к API CodeLinkAva (`https://ava-alpha-api.codelink.io/api/chat`) с телом запроса `data`.
        6. Полученные данные из ответа обрабатываются построчно. Если строка начинается с "data: ", она декодируется из JSON.
        7. Если строка содержит "data: [DONE]", генератор завершает работу.
        8. Из JSON-ответа извлекается содержимое (`content`) из поля `choices[0].delta.content`, которое является частью ответа модели.
        9. Если `content` существует, оно передается в генератор для выдачи пользователю.

        Внутри функции происходят следующие действия и преобразования:
        A. Определение заголовков запроса
        |
        -- B. Создание асинхронной сессии
        |
        C. Формирование тела запроса
        |
        D. Отправка POST-запроса к API
        |
        E. Обработка ответа построчно
        |
        F. Извлечение и передача содержимого в генератор

        Где:
        A (определение_заголовков): Установка необходимых HTTP-заголовков для запроса.
        B (создание_асинхронной_сессии): Создание асинхронной сессии для отправки HTTP-запросов.
        C (формирование_тела_запроса): Формирование тела запроса с сообщениями и параметрами.
        D (отправка_POST_запроса): Отправка POST-запроса к API с сформированным телом запроса.
        E (обработка_ответа_построчно): Обработка полученных данных из ответа API построчно.
        F (извлечение_и_передача_содержимого): Извлечение содержимого из JSON-ответа и передача его в генератор.

        Примеры:
            Пример 1:
            ```python
            model = "gpt-3.5-turbo"
            messages = [{"role": "user", "content": "Hello, how are you?"}]
            async_generator = CodeLinkAva.create_async_generator(model, messages)
            async for response in async_generator:
                print(response, end="")
            ```

            Пример 2:
            ```python
            model = "gpt-3.5-turbo"
            messages = [
                {"role": "user", "content": "What is the capital of France?"},
                {"role": "assistant", "content": "The capital of France is Paris."},
                {"role": "user", "content": "What is the capital of Germany?"}
            ]
            async_generator = CodeLinkAva.create_async_generator(model, messages)
            async for response in async_generator:
                print(response, end="")
            ```
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
            "Origin": cls.url,
            "Referer": f"{cls.url}/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }
        async with ClientSession(
                headers=headers
            ) as session:
            data = {
                "messages": messages,
                "temperature": 0.6,
                "stream": True,
                **kwargs
            }
            async with session.post("https://ava-alpha-api.codelink.io/api/chat", json=data) as response:
                response.raise_for_status()
                async for line in response.content:
                    line = line.decode()
                    if line.startswith("data: "):\
                        if line.startswith("data: [DONE]"):\
                            break
                        line = json.loads(line[6:-1])

                        content = line["choices"][0]["delta"].get("content")
                        if content:\
                            yield content