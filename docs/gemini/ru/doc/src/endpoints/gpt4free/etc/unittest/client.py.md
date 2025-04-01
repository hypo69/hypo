# Модуль для тестирования клиентов gpt4free

## Обзор

Модуль содержит набор юнит-тестов для проверки корректности работы асинхронного и синхронного клиентов `gpt4free`.
Он включает тесты для проверки ответов, передачи моделей, ограничения количества токенов, потоковой передачи и остановки генерации.

## Подробней

Модуль использует библиотеку `unittest` для организации и запуска тестов. Он определяет два основных тестовых класса: `AsyncTestPassModel` и `TestPassModel`, которые содержат асинхронные и синхронные тесты соответственно. Модуль также включает моки провайдеров для имитации различных сценариев работы с API.

## Классы

### `AsyncTestPassModel`

**Описание**:
Класс, содержащий набор асинхронных тестов для проверки функциональности асинхронного клиента.

**Принцип работы**:
Класс наследуется от `unittest.IsolatedAsyncioTestCase` и содержит несколько асинхронных тестов, каждый из которых проверяет определенную функцию асинхронного клиента. Используются моки провайдеров для имитации различных сценариев работы с API.

**Методы**:

- `test_response`:
    Краткое описание метода: Проверяет, что асинхронный клиент возвращает объект типа `ChatCompletion` с ожидаемым содержимым.
- `test_pass_model`:
    Краткое описание метода: Проверяет, что асинхронный клиент правильно передает модель и возвращает ожидаемый ответ.
- `test_max_tokens`:
    Краткое описание метода: Проверяет, что асинхронный клиент правильно обрабатывает ограничение на максимальное количество токенов.
- `test_max_stream`:
    Краткое описание метода: Проверяет, что асинхронный клиент правильно обрабатывает потоковую передачу ответов.
- `test_stop`:
    Краткое описание метода: Проверяет, что асинхронный клиент правильно обрабатывает параметр `stop` для остановки генерации.

### `TestPassModel`

**Описание**:
Класс, содержащий набор синхронных тестов для проверки функциональности синхронного клиента.

**Принцип работы**:
Класс наследуется от `unittest.TestCase` и содержит несколько синхронных тестов, каждый из которых проверяет определенную функцию синхронного клиента. Используются моки провайдеров для имитации различных сценариев работы с API.

**Методы**:

- `test_response`:
    Краткое описание метода: Проверяет, что синхронный клиент возвращает объект типа `ChatCompletion` с ожидаемым содержимым.
- `test_pass_model`:
    Краткое описание метода: Проверяет, что синхронный клиент правильно передает модель и возвращает ожидаемый ответ.
- `test_max_tokens`:
    Краткое описание метода: Проверяет, что синхронный клиент правильно обрабатывает ограничение на максимальное количество токенов.
- `test_max_stream`:
    Краткое описание метода: Проверяет, что синхронный клиент правильно обрабатывает потоковую передачу ответов.
- `test_stop`:
    Краткое описание метода: Проверяет, что синхронный клиент правильно обрабатывает параметр `stop` для остановки генерации.
- `test_model_not_found`:
    Краткое описание метода: Проверяет, что клиент вызывает исключение `ModelNotFoundError`, если модель не найдена.
- `test_best_provider`:
    Краткое описание метода: Проверяет, что функция `get_model_and_provider` возвращает правильную модель и провайдера для нестандартной модели.
- `test_default_model`:
    Краткое описание метода: Проверяет, что функция `get_model_and_provider` возвращает правильную модель и провайдера для модели по умолчанию.
- `test_provider_as_model`:
    Краткое описание метода: Проверяет, что функция `get_model_and_provider` правильно обрабатывает случай, когда провайдер передается в качестве модели.
- `test_get_model`:
    Краткое описание метода: Проверяет, что функция `get_model_and_provider` возвращает правильную модель и провайдера для заданной модели.

## Функции

### `test_response` (в `AsyncTestPassModel`)

```python
async def test_response(self):
    """Проверяет, что асинхронный клиент возвращает объект типа ChatCompletion с ожидаемым содержимым.

    Args:
        self (AsyncTestPassModel): Экземпляр класса AsyncTestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр AsyncClient с моковым провайдером AsyncGeneratorProviderMock.
    2. Вызывается метод create для создания чат-комплишена с заданными параметрами.
    3. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    4. Проверяется, что содержимое ответа соответствует ожидаемому значению "Mock".

    Примеры:
        >>> client = AsyncClient(provider=AsyncGeneratorProviderMock)
        >>> response = await client.chat.completions.create(DEFAULT_MESSAGES, "")
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("Mock", response.choices[0].message.content)
    """
    ...
```

### `test_pass_model` (в `AsyncTestPassModel`)

```python
async def test_pass_model(self):
    """Проверяет, что асинхронный клиент правильно передает модель и возвращает ожидаемый ответ.

    Args:
        self (AsyncTestPassModel): Экземпляр класса AsyncTestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр AsyncClient с моковым провайдером ModelProviderMock.
    2. Вызывается метод create для создания чат-комплишена с заданными параметрами.
    3. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    4. Проверяется, что содержимое ответа соответствует ожидаемому значению "Hello".

    Примеры:
        >>> client = AsyncClient(provider=ModelProviderMock)
        >>> response = await client.chat.completions.create(DEFAULT_MESSAGES, "Hello")
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("Hello", response.choices[0].message.content)
    """
    ...
```

### `test_max_tokens` (в `AsyncTestPassModel`)

```python
async def test_max_tokens(self):
    """Проверяет, что асинхронный клиент правильно обрабатывает ограничение на максимальное количество токенов.

    Args:
        self (AsyncTestPassModel): Экземпляр класса AsyncTestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр AsyncClient с моковым провайдером YieldProviderMock.
    2. Формируется список сообщений, каждое из которых содержит часть фразы.
    3. Вызывается метод create для создания чат-комплишена с ограничением max_tokens=1.
    4. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    5. Проверяется, что содержимое ответа соответствует ожидаемому значению "How ".
    6. Вызывается метод create для создания чат-комплишена с ограничением max_tokens=2.
    7. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    8. Проверяется, что содержимое ответа соответствует ожидаемому значению "How are ".

    Примеры:
        >>> client = AsyncClient(provider=YieldProviderMock)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["How ", "are ", "you", "?"]]
        >>> response = await client.chat.completions.create(messages, "Hello", max_tokens=1)
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("How ", response.choices[0].message.content)
        >>> response = await client.chat.completions.create(messages, "Hello", max_tokens=2)
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("How are ", response.choices[0].message.content)
    """
    ...
```

### `test_max_stream` (в `AsyncTestPassModel`)

```python
async def test_max_stream(self):
    """Проверяет, что асинхронный клиент правильно обрабатывает потоковую передачу ответов.

    Args:
        self (AsyncTestPassModel): Экземпляр класса AsyncTestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр AsyncClient с моковым провайдером YieldProviderMock.
    2. Формируется список сообщений, каждое из которых содержит часть фразы.
    3. Вызывается метод create для создания чат-комплишена с параметром stream=True.
    4. Асинхронно перебираются чанки ответа и проверяется их тип (ChatCompletionChunk).
    5. Проверяется, что содержимое каждого чанка является строкой.
    6. Повторяются шаги 3-5 с ограничением max_tokens=2.
    7. Проверяется, что количество полученных чанков равно 3.
    8. Проверяется, что содержимое каждого чанка соответствует ожидаемому значению "You ".

    Примеры:
        >>> client = AsyncClient(provider=YieldProviderMock)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["How ", "are ", "you", "?"]]
        >>> response = client.chat.completions.create(messages, "Hello", stream=True)
        >>> async for chunk in response:
        ...     chunk: ChatCompletionChunk = chunk
        ...     self.assertIsInstance(chunk, ChatCompletionChunk)
        ...     if chunk.choices[0].delta.content is not None:
        ...         self.assertIsInstance(chunk.choices[0].delta.content, str)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["You ", "You ", "Other", "?"]]
        >>> response = client.chat.completions.create(messages, "Hello", stream=True, max_tokens=2)
        >>> response_list = []
        >>> async for chunk in response:
        ...     response_list.append(chunk)
        >>> self.assertEqual(len(response_list), 3)
        >>> for chunk in response_list:
        ...     if chunk.choices[0].delta.content is not None:
        ...         self.assertEqual(chunk.choices[0].delta.content, "You ")
    """
    ...
```

### `test_stop` (в `AsyncTestPassModel`)

```python
async def test_stop(self):
    """Проверяет, что асинхронный клиент правильно обрабатывает параметр `stop` для остановки генерации.

    Args:
        self (AsyncTestPassModel): Экземпляр класса AsyncTestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр AsyncClient с моковым провайдером YieldProviderMock.
    2. Формируется список сообщений, каждое из которых содержит часть фразы.
    3. Вызывается метод create для создания чат-комплишена с параметром stop=["and"].
    4. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    5. Проверяется, что содержимое ответа соответствует ожидаемому значению "How are you?".

    Примеры:
        >>> client = AsyncClient(provider=YieldProviderMock)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["How ", "are ", "you", "?"]]
        >>> response = await client.chat.completions.create(messages, "Hello", stop=["and"])
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("How are you?", response.choices[0].message.content)
    """
    ...
```

### `test_response` (в `TestPassModel`)

```python
def test_response(self):
    """Проверяет, что синхронный клиент возвращает объект типа ChatCompletion с ожидаемым содержимым.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр Client с моковым провайдером AsyncGeneratorProviderMock.
    2. Вызывается метод create для создания чат-комплишена с заданными параметрами.
    3. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    4. Проверяется, что содержимое ответа соответствует ожидаемому значению "Mock".

    Примеры:
        >>> client = Client(provider=AsyncGeneratorProviderMock)
        >>> response = client.chat.completions.create(DEFAULT_MESSAGES, "")
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("Mock", response.choices[0].message.content)
    """
    ...
```

### `test_pass_model` (в `TestPassModel`)

```python
def test_pass_model(self):
    """Проверяет, что синхронный клиент правильно передает модель и возвращает ожидаемый ответ.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр Client с моковым провайдером ModelProviderMock.
    2. Вызывается метод create для создания чат-комплишена с заданными параметрами.
    3. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    4. Проверяется, что содержимое ответа соответствует ожидаемому значению "Hello".

    Примеры:
        >>> client = Client(provider=ModelProviderMock)
        >>> response = client.chat.completions.create(DEFAULT_MESSAGES, "Hello")
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("Hello", response.choices[0].message.content)
    """
    ...
```

### `test_max_tokens` (в `TestPassModel`)

```python
def test_max_tokens(self):
    """Проверяет, что синхронный клиент правильно обрабатывает ограничение на максимальное количество токенов.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр Client с моковым провайдером YieldProviderMock.
    2. Формируется список сообщений, каждое из которых содержит часть фразы.
    3. Вызывается метод create для создания чат-комплишена с ограничением max_tokens=1.
    4. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    5. Проверяется, что содержимое ответа соответствует ожидаемому значению "How ".
    6. Вызывается метод create для создания чат-комплишена с ограничением max_tokens=2.
    7. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    8. Проверяется, что содержимое ответа соответствует ожидаемому значению "How are ".

    Примеры:
        >>> client = Client(provider=YieldProviderMock)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["How ", "are ", "you", "?"]]
        >>> response = client.chat.completions.create(messages, "Hello", max_tokens=1)
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("How ", response.choices[0].message.content)
        >>> response = client.chat.completions.create(messages, "Hello", max_tokens=2)
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("How are ", response.choices[0].message.content)
    """
    ...
```

### `test_max_stream` (в `TestPassModel`)

```python
def test_max_stream(self):
    """Проверяет, что синхронный клиент правильно обрабатывает потоковую передачу ответов.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр Client с моковым провайдером YieldProviderMock.
    2. Формируется список сообщений, каждое из которых содержит часть фразы.
    3. Вызывается метод create для создания чат-комплишена с параметром stream=True.
    4. Перебираются чанки ответа и проверяется их тип (ChatCompletionChunk).
    5. Проверяется, что содержимое каждого чанка является строкой.
    6. Повторяются шаги 3-5 с ограничением max_tokens=2.
    7. Проверяется, что количество полученных чанков равно 3.
    8. Проверяется, что содержимое каждого чанка соответствует ожидаемому значению "You ".

    Примеры:
        >>> client = Client(provider=YieldProviderMock)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["How ", "are ", "you", "?"]]
        >>> response = client.chat.completions.create(messages, "Hello", stream=True)
        >>> for chunk in response:
        ...     self.assertIsInstance(chunk, ChatCompletionChunk)
        ...     if chunk.choices[0].delta.content is not None:
        ...         self.assertIsInstance(chunk.choices[0].delta.content, str)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["You ", "You ", "Other", "?"]]
        >>> response = client.chat.completions.create(messages, "Hello", stream=True, max_tokens=2)
        >>> response_list = list(response)
        >>> self.assertEqual(len(response_list), 3)
        >>> for chunk in response_list:
        ...     if chunk.choices[0].delta.content is not None:
        ...         self.assertEqual(chunk.choices[0].delta.content, "You ")
    """
    ...
```

### `test_stop` (в `TestPassModel`)

```python
def test_stop(self):
    """Проверяет, что синхронный клиент правильно обрабатывает параметр `stop` для остановки генерации.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Создается экземпляр Client с моковым провайдером YieldProviderMock.
    2. Формируется список сообщений, каждое из которых содержит часть фразы.
    3. Вызывается метод create для создания чат-комплишена с параметром stop=["and"].
    4. Проверяется, что возвращенный объект является экземпляром ChatCompletion.
    5. Проверяется, что содержимое ответа соответствует ожидаемому значению "How are you?".

    Примеры:
        >>> client = Client(provider=YieldProviderMock)
        >>> messages = [{'role': 'user', 'content': chunk} for chunk in ["How ", "are ", "you", "?"]]
        >>> response = client.chat.completions.create(messages, "Hello", stop=["and"])
        >>> self.assertIsInstance(response, ChatCompletion)
        >>> self.assertEqual("How are you?", response.choices[0].message.content)
    """
    ...
```

### `test_model_not_found` (в `TestPassModel`)

```python
def test_model_not_found(self):
    """Проверяет, что клиент вызывает исключение `ModelNotFoundError`, если модель не найдена.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.
        ModelNotFoundError: Если модель не найдена.

    Как работает функция:
    1. Определяется внутренняя функция run_exception, которая создает экземпляр Client без указания провайдера.
    2. В run_exception вызывается метод create для создания чат-комплишена.
    3. Проверяется, что при вызове run_exception возникает исключение ModelNotFoundError.

    Внутренние функции:
    - `run_exception`:
        Описание: Создает и вызывает клиент для генерации ответа.
        Как работает функция:
        1. Создается клиент Client().
        2. Вызывается метод create у client.chat.completions.create,
           который должен вызвать исключение ModelNotFoundError.
    """
    ...
```

### `test_best_provider` (в `TestPassModel`)

```python
def test_best_provider(self):
    """Проверяет, что функция `get_model_and_provider` возвращает правильную модель и провайдера для нестандартной модели.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Определяется имя нестандартной модели not_default_model = "gpt-4o".
    2. Вызывается функция get_model_and_provider с параметрами not_default_model, None, False.
    3. Проверяется, что у возвращенного провайдера есть атрибут create_completion.
    4. Проверяется, что возвращенная модель соответствует not_default_model.
    """
    ...
```

### `test_default_model` (в `TestPassModel`)

```python
def test_default_model(self):
    """Проверяет, что функция `get_model_and_provider` возвращает правильную модель и провайдера для модели по умолчанию.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Определяется имя модели по умолчанию default_model = "".
    2. Вызывается функция get_model_and_provider с параметрами default_model, None, False.
    3. Проверяется, что у возвращенного провайдера есть атрибут create_completion.
    4. Проверяется, что возвращенная модель соответствует default_model.
    """
    ...
```

### `test_provider_as_model` (в `TestPassModel`)

```python
def test_provider_as_model(self):
    """Проверяет, что функция `get_model_and_provider` правильно обрабатывает случай, когда провайдер передается в качестве модели.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Определяется имя провайдера в качестве модели provider_as_model = Copilot.__name__.
    2. Вызывается функция get_model_and_provider с параметрами provider_as_model, None, False.
    3. Проверяется, что у возвращенного провайдера есть атрибут create_completion.
    4. Проверяется, что возвращенная модель является строкой.
    5. Проверяется, что возвращенная модель соответствует Copilot.default_model.
    """
    ...
```

### `test_get_model` (в `TestPassModel`)

```python
def test_get_model(self):
    """Проверяет, что функция `get_model_and_provider` возвращает правильную модель и провайдера для заданной модели.

    Args:
        self (TestPassModel): Экземпляр класса TestPassModel.

    Returns:
        None

    Raises:
        AssertionError: Если проверка не прошла.

    Как работает функция:
    1. Вызывается функция get_model_and_provider с параметрами gpt_4o.name, None, False.
    2. Проверяется, что у возвращенного провайдера есть атрибут create_completion.
    3. Проверяется, что возвращенная модель соответствует gpt_4o.name.
    """
    ...
```