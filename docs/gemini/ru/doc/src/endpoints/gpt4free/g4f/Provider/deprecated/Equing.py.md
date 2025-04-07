# Модуль Equing

## Обзор

Модуль `Equing` представляет собой реализацию провайдера для взаимодействия с сервисом `next.eqing.tech`. Он поддерживает потоковую передачу данных и модель `gpt-3.5-turbo`, но не поддерживает `gpt-4`.
Модуль содержит класс `Equing`, который наследуется от `AbstractProvider` и предоставляет метод для создания завершений на основе предоставленных сообщений.

## Подробнее

Этот модуль предназначен для обеспечения возможности взаимодействия с API `next.eqing.tech` для генерации текста на основе предоставленных входных данных. Он определяет параметры подключения и заголовки, необходимые для аутентификации и выполнения запросов к API.

## Классы

### `Equing(AbstractProvider)`

**Описание**: Класс `Equing` является провайдером для работы с API `next.eqing.tech`.

**Наследует**:

- `AbstractProvider`: Абстрактный базовый класс для всех провайдеров.

**Атрибуты**:

- `url` (str): URL-адрес сервиса `next.eqing.tech`. Значение: `'https://next.eqing.tech/'`.
- `working` (bool): Указывает, работает ли провайдер. Значение: `False`.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных. Значение: `True`.
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-3.5-turbo`. Значение: `True`.
- `supports_gpt_4` (bool): Указывает, поддерживает ли провайдер модель `gpt-4`. Значение: `False`.

**Методы**:

- `create_completion()`: Статический метод для создания завершений на основе предоставленных сообщений.

## Функции

### `create_completion`

```python
    @staticmethod
    @abstractmethod
    def create_completion(
        model: str,
        messages: list[dict[str, str]],
        stream: bool, **kwargs: Any) -> CreateResult:
        ...
```

**Назначение**: Создает завершение (completion) на основе предоставленных сообщений, используя API `next.eqing.tech`.

**Параметры**:

- `model` (str): Идентификатор используемой модели.
- `messages` (list[dict[str, str]]): Список сообщений, используемых для создания завершения. Каждое сообщение представляет собой словарь с ключами `role` и `content`.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
- `**kwargs` (Any): Дополнительные параметры, такие как `temperature`, `presence_penalty`, `frequency_penalty` и `top_p`.

**Возвращает**:

- `CreateResult`: Генератор, выдающий части завершения, или строку с полным завершением, в зависимости от значения параметра `stream`.

**Вызывает исключения**:

- Отсутствуют явные исключения, но могут возникнуть исключения, связанные с сетевыми запросами (`requests.post`) или обработкой JSON.

**Как работает функция**:

1.  Формирует заголовки запроса, необходимые для аутентификации и взаимодействия с API `next.eqing.tech`.
2.  Формирует JSON-данные запроса, включающие сообщения, параметры модели и другие настройки.
3.  Отправляет POST-запрос к API `next.eqing.tech` с использованием библиотеки `requests`.
4.  Если `stream` имеет значение `False`, возвращает содержимое первого сообщения из списка `choices`.
5.  Если `stream` имеет значение `True`, обрабатывает ответ построчно, извлекая содержимое каждого токена из JSON и возвращая его как часть генератора.

```
    Начало
    │
    ├───> Формирование заголовков запроса (headers)
    │
    ├───> Формирование JSON-данных запроса (json_data)
    │
    ├───> Отправка POST-запроса к API (response = requests.post(...))
    │
    ├───> Проверка stream
    │       ├───> False: Извлечение и возврат контента из ответа (yield response.json()["choices"][0]["message"]["content"])
    │       └───> True: 
    │           │
    │           ├───> Итерация по контенту ответа (for line in response.iter_content(...))
    │           │   │
    │           │   └───> Проверка наличия "content" в строке (if b'content' in line)
    │           │       │
    │           │       └───> Извлечение токена из JSON (token = line_json['choices'][0]['delta'].get('content'))
    │           │           │
    │           │           └───> Проверка наличия токена (if token)
    │           │               │
    │           │               └───> Возврат токена (yield token)
    │           │
    │           └───> Конец итерации
    │
    └───> Конец
```

**Примеры**:

```python
# Пример 1: Создание завершения без потоковой передачи данных
messages = [{"role": "user", "content": "Hello, how are you?"}]
result = Equing.create_completion(model="gpt-3.5-turbo", messages=messages, stream=False)
for item in result:
    print(item)

# Пример 2: Создание завершения с потоковой передачей данных
messages = [{"role": "user", "content": "Tell me a story."}]
result = Equing.create_completion(model="gpt-3.5-turbo", messages=messages, stream=True)
for item in result:
    print(item, end="")

# Пример 3: Создание завершения с указанием дополнительных параметров
messages = [{"role": "user", "content": "Translate 'hello' to French."}]
result = Equing.create_completion(model="gpt-3.5-turbo", messages=messages, stream=False, temperature=0.7, top_p=0.9)
for item in result:
    print(item)