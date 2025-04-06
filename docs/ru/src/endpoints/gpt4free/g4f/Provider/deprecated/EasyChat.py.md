# Модуль EasyChat

## Обзор

Модуль `EasyChat` предоставляет класс `EasyChat`, который является провайдером для взаимодействия с сервисом EasyChat для генерации текста. Он поддерживает потоковую передачу данных и модель `gpt-35-turbo`.

## Подробней

Этот модуль предназначен для интеграции с сервисом EasyChat, который предоставляет API для генерации текста на основе модели GPT-3. Класс `EasyChat` наследуется от `AbstractProvider` и реализует метод `create_completion` для отправки запросов к API EasyChat и получения ответов. Модуль использует библиотеки `requests`, `json` и `random`.
Расположение файла в проекте: `hypotez/src/endpoints/gpt4free/g4f/Provider/deprecated/EasyChat.py`

## Классы

### `EasyChat(AbstractProvider)`

**Описание**:
Класс `EasyChat` предоставляет интерфейс для взаимодействия с сервисом EasyChat.

**Наследует**:
`AbstractProvider` - абстрактный класс, определяющий интерфейс для провайдеров.

**Атрибуты**:
- `url` (str): URL-адрес сервиса EasyChat (`https://free.easychat.work`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-35-turbo` (`True`).
- `working` (bool): Указывает, работает ли провайдер в данный момент (`False`).

### `create_completion`

```python
    @staticmethod
    def create_completion(
        model: str,
        messages: list[dict[str, str]],
        stream: bool, **kwargs: Any) -> CreateResult:
        """
        Отправляет запрос к API EasyChat и возвращает результат генерации текста.

        Args:
            model (str): Название используемой модели.
            messages (list[dict[str, str]]): Список сообщений для отправки в API.
            stream (bool): Указывает, использовать ли потоковую передачу данных.
            **kwargs (Any): Дополнительные параметры для запроса.

        Returns:
            CreateResult: Результат генерации текста.

        Raises:
            Exception: Если произошла ошибка при отправке запроса или получении ответа от сервера.

        Внутренние функции:
            Нет внутренних функций.

        Как работает функция:
        1. Определяется список активных серверов `active_servers`.
        2. Выбирается случайный сервер из списка `active_servers` или используется переданный в `kwargs` параметр `active_server`.
        3. Формируются заголовки `headers` для HTTP-запроса.
        4. Формируется JSON-тело `json_data` запроса, включающее сообщения, параметры модели и другие параметры.
        5. Создается сессия `requests.Session()` и инициализируются cookies с сервера.
        6. Отправляется POST-запрос к API EasyChat.
        7. Если запрос не удался (статус код не 200), выбрасывается исключение.
        8. Если не используется потоковая передача (`stream=False`):
           - Полученный JSON-ответ обрабатывается для извлечения сгенерированного текста.
           - Если в ответе есть поле "choices", извлекается первое сообщение и возвращается его содержимое.
           - Если ответа от сервера нет, выбрасывается исключение.
        9. Если используется потоковая передача (`stream=True`):
           - Итерируемся по чанкам ответа.
           - Если в чанке есть поле "content", извлекается его содержимое и возвращается.
        10. Если поле "content" не найдено, функция продолжает итерации.

        ASCII flowchart:

        Начало --> [Определение активных серверов]
        [Определение активных серверов] --> [Выбор сервера]
        [Выбор сервера] --> [Формирование заголовков]
        [Формирование заголовков] --> [Формирование JSON]
        [Формирование JSON] --> [Создание сессии]
        [Создание сессии] --> [Отправка POST-запроса]
        [Отправка POST-запроса] --> [Проверка статус-кода]
        [Проверка статус-кода] --(Статус-код != 200)--> [Выброс исключения]
        [Проверка статус-кода] --(Статус-код == 200)--> [Обработка ответа (stream=False или stream=True)]
        [Обработка ответа (stream=False или stream=True)] --> Конец

        Примеры:
            >>> EasyChat.create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Hello'}], stream=False)
            <generator object EasyChat.create_completion at 0x...>

            >>> EasyChat.create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Hello'}], stream=True, temperature=0.7)
            <generator object EasyChat.create_completion at 0x...>
        """
        active_servers = [
            "https://chat10.fastgpt.me",
            "https://chat9.fastgpt.me",
            "https://chat1.fastgpt.me",
            "https://chat2.fastgpt.me",
            "https://chat3.fastgpt.me",
            "https://chat4.fastgpt.me",
            "https://gxos1h1ddt.fastgpt.me"
        ]

        server  = active_servers[kwargs.get("active_server", random.randint(0, 5))]
        headers = {
            "authority"         : f"{server}".replace("https://", ""),
            "accept"            : "text/event-stream",
            "accept-language"   : "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3,fa=0.2",
            "content-type"      : "application/json",
            "origin"            : f"{server}",
            "referer"           : f"{server}/",
            "x-requested-with"  : "XMLHttpRequest",
            'plugins'           : '0',
            'sec-ch-ua'         : '\'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"\'',
            'sec-ch-ua-mobile'  : '?0',
            'sec-ch-ua-platform': '\'"Windows"\'',
            'sec-fetch-dest'    : 'empty',
            'sec-fetch-mode'    : 'cors',
            'sec-fetch-site'    : 'same-origin',
            'user-agent'        : '\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\'',
            'usesearch'         : 'false',
            'x-requested-with'  : 'XMLHttpRequest'
        }

        json_data = {
            "messages"          : messages,
            "stream"            : stream,
            "model"             : model,
            "temperature"       : kwargs.get("temperature", 0.5),
            "presence_penalty"  : kwargs.get("presence_penalty", 0),
            "frequency_penalty" : kwargs.get("frequency_penalty", 0),
            "top_p"             : kwargs.get("top_p", 1)
        }

        session = requests.Session()
        # init cookies from server
        session.get(f"{server}/")

        response = session.post(f"{server}/api/openai/v1/chat/completions",
            headers=headers, json=json_data, stream=stream)

        if response.status_code != 200:
            raise Exception(f"Error {response.status_code} from server : {response.reason}")
        if not stream:
            json_data = response.json()

            if "choices" in json_data:
                yield json_data["choices"][0]["message"]["content"]
            else:
                raise Exception("No response from server")

        else:
                
            for chunk in response.iter_lines():
                    
                if b"content" in chunk:
                    splitData = chunk.decode().split("data:")

                    if len(splitData) > 1:
                        yield json.loads(splitData[1])["choices"][0]["delta"]["content"]