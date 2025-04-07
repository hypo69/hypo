# Модуль `testing_utils`

## Обзор

Модуль `testing_utils` содержит набор утилитных функций, классов и фикстур, предназначенных для облегчения тестирования в проекте `hypotez`. Он включает в себя функции для работы с файловой системой, проверки результатов симуляций, создания тестовых сообщений, сравнения агентов, а также фикстуры для настройки тестового окружения. Модуль используется для организации и упрощения процесса написания и выполнения тестов, обеспечивая удобные инструменты для проверки корректности работы различных компонентов системы.

## Подробнее

Модуль предоставляет функции для кэширования результатов API-вызовов, что позволяет экономить ресурсы и ускоряет процесс тестирования. Также модуль содержит инструменты для проверки типов и содержимого действий и стимулов, используемых в симуляциях. Кроме того, модуль включает фикстуры для создания тестовых миров и агентов, что позволяет легко настраивать тестовое окружение для различных сценариев.

## Функции

### `remove_file_if_exists`

```python
def remove_file_if_exists(file_path: str) -> None:
    """
    Удаляет файл по указанному пути, если он существует.

    Args:
        file_path (str): Путь к файлу, который нужно удалить.

    Returns:
        None

    Как работает функция:
    1. Проверяет, существует ли файл по указанному пути.
    2. Если файл существует, удаляет его.

    ```
    Существует ли файл? --> Нет: Конец
    |
    Да
    |
    Удалить файл
    ```

    Примеры:
    >>> remove_file_if_exists("test_file.txt")
    """
    ...
```

### `contains_action_type`

```python
def contains_action_type(actions: list, action_type: str) -> bool:
    """
    Проверяет, содержит ли список действий действие указанного типа.

    Args:
        actions (list): Список действий для проверки.
        action_type (str): Тип действия для поиска.

    Returns:
        bool: `True`, если список содержит действие указанного типа, иначе `False`.

    Как работает функция:
    1. Перебирает все действия в списке `actions`.
    2. Для каждого действия проверяет, соответствует ли его тип `action_type`.
    3. Если соответствие найдено, возвращает `True`.
    4. Если перебор завершен и соответствие не найдено, возвращает `False`.

    ```
    Начало
    |
    Перебрать действия в списке
    |
    Соответствует ли тип действия action_type? --> Да: Вернуть True
    |                                            Нет
    |
    Конец перебора
    |
    Вернуть False
    ```

    Примеры:
    >>> actions = [{"action": {"type": "move", "content": "..."}}, {"action": {"type": "talk", "content": "..."}}]
    >>> contains_action_type(actions, "move")
    True
    >>> contains_action_type(actions, "eat")
    False
    """
    ...
```

### `contains_action_content`

```python
def contains_action_content(actions: list, action_content: str) -> bool:
    """
    Проверяет, содержит ли список действий действие с указанным содержимым.

    Args:
        actions (list): Список действий для проверки.
        action_content (str): Содержимое действия для поиска.

    Returns:
        bool: `True`, если список содержит действие с указанным содержимым, иначе `False`.

    Как работает функция:
    1. Перебирает все действия в списке `actions`.
    2. Для каждого действия проверяет, содержит ли его содержимое `action_content` (без учета регистра).
    3. Если соответствие найдено, возвращает `True`.
    4. Если перебор завершен и соответствие не найдено, возвращает `False`.

    ```
    Начало
    |
    Перебрать действия в списке
    |
    Содержит ли содержимое действия action_content? --> Да: Вернуть True
    |                                                 Нет
    |
    Конец перебора
    |
    Вернуть False
    ```

    Примеры:
    >>> actions = [{"action": {"type": "move", "content": "Go to the store"}}, {"action": {"type": "talk", "content": "Hello world"}}]
    >>> contains_action_content(actions, "store")
    True
    >>> contains_action_content(actions, "goodbye")
    False
    """
    ...
```

### `contains_stimulus_type`

```python
def contains_stimulus_type(stimuli: list, stimulus_type: str) -> bool:
    """
    Проверяет, содержит ли список стимулов стимул указанного типа.

    Args:
        stimuli (list): Список стимулов для проверки.
        stimulus_type (str): Тип стимула для поиска.

    Returns:
        bool: `True`, если список содержит стимул указанного типа, иначе `False`.

    Как работает функция:
    1. Перебирает все стимулы в списке `stimuli`.
    2. Для каждого стимула проверяет, соответствует ли его тип `stimulus_type`.
    3. Если соответствие найдено, возвращает `True`.
    4. Если перебор завершен и соответствие не найдено, возвращает `False`.

    ```
    Начало
    |
    Перебрать стимулы в списке
    |
    Соответствует ли тип стимула stimulus_type? --> Да: Вернуть True
    |                                              Нет
    |
    Конец перебора
    |
    Вернуть False
    ```

    Примеры:
    >>> stimuli = [{"type": "message", "content": "..."}}, {"type": "event", "content": "..."}}]
    >>> contains_stimulus_type(stimuli, "message")
    True
    >>> contains_stimulus_type(stimuli, "sound")
    False
    """
    ...
```

### `contains_stimulus_content`

```python
def contains_stimulus_content(stimuli: list, stimulus_content: str) -> bool:
    """
    Проверяет, содержит ли список стимулов стимул с указанным содержимым.

    Args:
        stimuli (list): Список стимулов для проверки.
        stimulus_content (str): Содержимое стимула для поиска.

    Returns:
        bool: `True`, если список содержит стимул с указанным содержимым, иначе `False`.

    Как работает функция:
    1. Перебирает все стимулы в списке `stimuli`.
    2. Для каждого стимула проверяет, содержит ли его содержимое `stimulus_content` (без учета регистра).
    3. Если соответствие найдено, возвращает `True`.
    4. Если перебор завершен и соответствие не найдено, возвращает `False`.

    ```
    Начало
    |
    Перебрать стимулы в списке
    |
    Содержит ли содержимое стимула stimulus_content? --> Да: Вернуть True
    |                                                   Нет
    |
    Конец перебора
    |
    Вернуть False
    ```

    Примеры:
    >>> stimuli = [{"type": "message", "content": "Hello world"}, {"type": "event", "content": "Someone arrived"}}]
    >>> contains_stimulus_content(stimuli, "hello")
    True
    >>> contains_stimulus_content(stimuli, "goodbye")
    False
    """
    ...
```

### `terminates_with_action_type`

```python
def terminates_with_action_type(actions: list, action_type: str) -> bool:
    """
    Проверяет, завершается ли список действий действием указанного типа.

    Args:
        actions (list): Список действий для проверки.
        action_type (str): Тип действия, которым должен завершаться список.

    Returns:
        bool: `True`, если список завершается действием указанного типа, иначе `False`.

    Как работает функция:
    1. Проверяет, является ли список `actions` пустым. Если да, возвращает `False`.
    2. Если список не пуст, проверяет, соответствует ли тип последнего действия в списке `action_type`.
    3. Возвращает результат проверки.

    ```
    Начало
    |
    Список actions пуст? --> Да: Вернуть False
    |                       Нет
    |
    Соответствует ли тип последнего действия action_type? --> Да: Вернуть True
    |                                                        Нет
    |
    Вернуть False
    ```

    Примеры:
    >>> actions = [{"action": {"type": "move", "content": "..."}}, {"action": {"type": "talk", "content": "..."}}]
    >>> terminates_with_action_type(actions, "talk")
    True
    >>> terminates_with_action_type(actions, "move")
    False
    """
    ...
```

### `proposition_holds`

```python
def proposition_holds(proposition: str) -> bool:
    """
    Проверяет, является ли заданное утверждение истинным, используя вызов LLM.
    Это можно использовать для проверки текстовых свойств, которые трудно
    проверить механически, например, "текст содержит некоторые идеи для продукта".

    Args:
        proposition (str): Утверждение для проверки.

    Returns:
        bool: `True`, если утверждение истинно, иначе `False`.

    Raises:
        Exception: Если LLM возвращает неожиданный результат.

    Как работает функция:
    1. Формирует системное и пользовательское приглашения для LLM.
    2. Отправляет запрос в LLM.
    3. Очищает полученное сообщение от не-алфанумерических символов.
    4. Проверяет, начинается ли очищенное сообщение с "true" или "false" (без учета регистра).
    5. Возвращает `True` или `False` в зависимости от результата проверки.
    6. Если LLM возвращает неожиданный результат, выбрасывает исключение.

    ```
    Начало
    |
    Сформировать системное и пользовательское приглашения
    |
    Отправить запрос в LLM
    |
    Очистить сообщение от не-алфанумерических символов
    |
    Начинается ли сообщение с "true"? --> Да: Вернуть True
    |                                    Нет
    |
    Начинается ли сообщение с "false"? --> Да: Вернуть False
    |                                     Нет
    |
    Выбросить исключение
    ```

    Примеры:
    >>> proposition_holds("The text contains some ideas for a product")
    True
    >>> proposition_holds("The text is empty")
    False
    """
    ...
```

### `only_alphanumeric`

```python
def only_alphanumeric(string: str) -> str:
    """
    Возвращает строку, содержащую только буквенно-цифровые символы.

    Args:
        string (str): Строка для обработки.

    Returns:
        str: Строка, содержащая только буквенно-цифровые символы.

    Как работает функция:
    1. Использует генератор для перебора символов в строке.
    2. Оставляет только буквенно-цифровые символы.
    3. Объединяет оставшиеся символы в строку.

    ```
    Начало
    |
    Перебрать символы в строке
    |
    Является ли символ буквенно-цифровым? --> Да: Добавить символ в результат
    |                                          Нет
    |
    Конец перебора
    |
    Объединить символы в строку
    |
    Вернуть строку
    ```

    Примеры:
    >>> only_alphanumeric("Hello, world!")
    "Helloworld"
    >>> only_alphanumeric("123 abc")
    "123abc"
    """
    ...
```

### `create_test_system_user_message`

```python
def create_test_system_user_message(user_prompt: str, system_prompt: str = "You are a helpful AI assistant.") -> list:
    """
    Создает список, содержащий одно системное сообщение и одно пользовательское сообщение.

    Args:
        user_prompt (str): Сообщение пользователя.
        system_prompt (str, optional): Системное сообщение. По умолчанию "You are a helpful AI assistant.".

    Returns:
        list: Список сообщений, содержащий системное и пользовательское сообщения.

    Как работает функция:
    1. Создает список сообщений.
    2. Добавляет системное сообщение в список.
    3. Если `user_prompt` не `None`, добавляет пользовательское сообщение в список.
    4. Возвращает список сообщений.

    ```
    Начало
    |
    Создать список сообщений
    |
    Добавить системное сообщение в список
    |
    user_prompt не None? --> Да: Добавить пользовательское сообщение в список
    |                     Нет
    |
    Вернуть список сообщений
    ```

    Примеры:
    >>> create_test_system_user_message("Hello world")
    [{'role': 'system', 'content': 'You are a helpful AI assistant.'}, {'role': 'user', 'content': 'Hello world'}]
    >>> create_test_system_user_message("Hello world", "You are a chatbot")
    [{'role': 'system', 'content': 'You are a chatbot'}, {'role': 'user', 'content': 'Hello world'}]
    """
    ...
```

### `agents_personas_are_equal`

```python
def agents_personas_are_equal(agent1: TinyPerson, agent2: TinyPerson, ignore_name: bool = False) -> bool:
    """
    Проверяет, совпадают ли конфигурации двух агентов.

    Args:
        agent1 (TinyPerson): Первый агент для сравнения.
        agent2 (TinyPerson): Второй агент для сравнения.
        ignore_name (bool, optional): Игнорировать ли имя агента при сравнении. По умолчанию `False`.

    Returns:
        bool: `True`, если конфигурации агентов совпадают, иначе `False`.

    Как работает функция:
    1. Определяет список ключей, которые нужно игнорировать при сравнении.
    2. Перебирает ключи в `_persona` первого агента.
    3. Если ключ не входит в список игнорируемых, сравнивает значение этого ключа у обоих агентов.
    4. Если значения не совпадают, возвращает `False`.
    5. Если перебор завершен и все значения совпадают, возвращает `True`.

    ```
    Начало
    |
    Определить список игнорируемых ключей
    |
    Перебрать ключи в _persona первого агента
    |
    Ключ в списке игнорируемых? --> Да: Пропустить ключ
    |                             Нет
    |
    Совпадают ли значения ключа у обоих агентов? --> Да: Продолжить перебор
    |                                              Нет
    |
    Вернуть False
    |
    Конец перебора
    |
    Вернуть True
    ```

    Примеры:
    >>> agent1 = TinyPerson(name="John", persona={"age": 30})
    >>> agent2 = TinyPerson(name="Jane", persona={"age": 30})
    >>> agents_personas_are_equal(agent1, agent2)
    False
    >>> agents_personas_are_equal(agent1, agent2, ignore_name=True)
    True
    """
    ...
```

### `agent_first_name`

```python
def agent_first_name(agent: TinyPerson) -> str:
    """
    Возвращает имя агента.

    Args:
        agent (TinyPerson): Агент, имя которого нужно получить.

    Returns:
        str: Имя агента.

    Как работает функция:

    1. Разделяет полное имя агента на слова.
    2. Возвращает первое слово.

    ```
    Начало
    |
    Разделить полное имя агента на слова
    |
    Вернуть первое слово
    ```

    Примеры:
    >>> agent = TinyPerson(name="John Doe", persona={"age": 30})
    >>> agent_first_name(agent)
    "John"
    """
    ...
```

### `get_relative_to_test_path`

```python
def get_relative_to_test_path(path_suffix: str) -> str:
    """
    Возвращает путь к тестовому файлу с указанным суффиксом.

    Args:
        path_suffix (str): Суффикс пути к файлу.

    Returns:
        str: Полный путь к файлу.

    Как работает функция:
    1. Получает путь к текущему файлу.
    2. Объединяет путь к текущему файлу с указанным суффиксом.
    3. Возвращает полученный путь.

    ```
    Начало
    |
    Получить путь к текущему файлу
    |
    Объединить путь с суффиксом
    |
    Вернуть полученный путь
    ```

    Примеры:
    >>> get_relative_to_test_path("test_file.txt")
    "/path/to/tests/test_file.txt"
    """
    ...
```

## Фикстуры

### `focus_group_world`

```python
@pytest.fixture(scope="function")
def focus_group_world() -> TinyWorld:
    """
    Создает тестовый мир с группой агентов для фокус-группы.

    Returns:
        TinyWorld: Тестовый мир с агентами.
    """
    ...
```

### `setup`

```python
@pytest.fixture(scope="function")
def setup() -> Generator[None, None, None]:
    """
    Выполняет настройку перед каждым тестом.

    Yields:
        None: None
    """
    ...