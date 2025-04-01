# Модуль для работы с провайдером Vercel
## Обзор

Модуль `Vercel.py` предоставляет интерфейс для взаимодействия с моделями искусственного интеллекта, размещенными на платформе Vercel. Он включает в себя клиентский класс для выполнения запросов к API Vercel, получения токенов и генерации текста на основе выбранной модели и входных параметров.

## Подробнее

Этот модуль предназначен для использования в проекте `hypotez` для обеспечения доступа к различным моделям ИИ через API Vercel. Он содержит определения поддерживаемых моделей, параметры конфигурации и логику для установления соединения и обмена данными с сервисом Vercel. Модуль использует `curl_cffi` для выполнения HTTP-запросов и `execjs` для выполнения JavaScript-кода, необходимого для получения токена аутентификации.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Генерирует ответ модели на основе предоставленных сообщений.

    Args:
        model (str): Идентификатор модели для генерации ответа.
        messages (list): Список сообщений, составляющих контекст диалога.
        stream (bool): Флаг, определяющий, следует ли возвращать ответ в режиме потока.
        **kwargs: Дополнительные параметры для передачи в API Vercel.

    Returns:
        Generator[str, None, None]: Генератор токенов ответа модели.

    Как работает функция:
    1.  Выводит сообщение о том, что Vercel в данный момент не работает.
    2.  Формирует строку `conversation`, представляющую собой историю сообщений между пользователем и ассистентом.
    3.  Инициализирует клиент `Client()` для взаимодействия с API Vercel.
    4.  Вызывает метод `generate` клиента для получения ответа модели.
    5.  Итерируется по токенам ответа и возвращает их в виде генератора.

    ASCII Flowchart:

    Начало --> Вывод сообщения "Vercel is currently not working." --> Конец

    ```
    Начало
    |
    Вывод сообщения "Vercel is currently not working."
    |
    Конец
    ```

    Примеры:

    ```python
    # Пример вызова функции _create_completion с минимальным набором параметров
    completion = _create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Hello'}], stream=False)

    # Пример вызова функции _create_completion с дополнительными параметрами
    completion = _create_completion(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': 'Hello'}], stream=True, temperature=0.9)
    ```
    """
```

## Классы

### `Client`

```python
class Client:
    """
    Клиент для взаимодействия с API Vercel.

    Attributes:
        session (requests.Session): Сессия для выполнения HTTP-запросов.
        headers (dict): Заголовки HTTP-запросов по умолчанию.

    Methods:
        get_token(): Получает токен аутентификации от Vercel.
        get_default_params(model_id: str): Получает параметры по умолчанию для указанной модели.
        generate(model_id: str, prompt: str, params: dict = {}): Генерирует текст на основе предоставленного запроса и параметров.
    """
```

**Принцип работы**:

Класс `Client` предназначен для упрощения взаимодействия с API Vercel. Он инициализирует сессию `requests.Session` с необходимыми заголовками и предоставляет методы для получения токена аутентификации, параметров по умолчанию для моделей и генерации текста на основе предоставленного запроса.

**Методы**:

#### `__init__`

```python
    def __init__(self):
        """
        Инициализирует клиентский класс с сессией и заголовками.
        """
```

#### `get_token`

```python
    def get_token(self):
        """
        Получает токен аутентификации от Vercel.

        Returns:
            str: Токен аутентификации в формате base64.
        """
```

#### `get_default_params`

```python
    def get_default_params(self, model_id: str):
        """
        Получает параметры по умолчанию для указанной модели.

        Args:
            model_id (str): Идентификатор модели.

        Returns:
            dict: Словарь с параметрами по умолчанию для модели.
        """
```

#### `generate`

```python
    def generate(self, model_id: str, prompt: str, params: dict = {}):
        """
        Генерирует текст на основе предоставленного запроса и параметров.

        Args:
            model_id (str): Идентификатор модели.
            prompt (str): Текст запроса.
            params (dict, optional): Дополнительные параметры для запроса. По умолчанию {}.

        Yields:
            str: Токены сгенерированного текста.

        Raises:
            Exception: Если возникает ошибка при выполнении запроса.
        """
```

### Определение параметров

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '({0})'.format(', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]]))
```

## Определение параметров
Эта строка кода формирует строку с информацией о поддержке параметров для функции `_create_completion`.

**Как работает код**
1. **Получение имени файла**:
   - `os.path.basename(__file__)` извлекает имя текущего файла (например, "Vercel.py").
   - `[:-3]` удаляет последние три символа (".py"), чтобы получить имя модуля (например, "Vercel").

2. **Формирование строки параметров**:
   - `get_type_hints(_create_completion)` возвращает словарь, содержащий аннотации типов для параметров функции `_create_completion`.
   - `_create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]` возвращает список имен параметров функции `_create_completion`.
   - Генератор списка `[f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]]` создает список строк, где каждая строка имеет формат "имя_параметра: тип_параметра".
   - `', '.join(...)` объединяет элементы списка в одну строку, разделяя их запятой и пробелом.
   - `'({0})'.format(...)` форматирует строку, вставляя строку параметров в круглые скобки.

**Пример**:

Предположим, что функция `_create_completion` имеет следующую сигнатуру:

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    ...
```

Тогда строка `params` будет иметь значение:

```
"g4f.Providers.Vercel supports: (model: str, messages: list, stream: bool, kwargs: dict)"