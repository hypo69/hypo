# Модуль для тестирования клиентской части `gpt4free`

## Обзор

Модуль содержит набор юнит-тестов для проверки корректной работы асинхронного и синхронного клиентов `gpt4free`. Он включает тесты для проверки ответов, передачи моделей, обработки максимального количества токенов, стриминга и остановки генерации.

## Подробнее

Модуль использует `unittest` для организации тестов и включает моки провайдеров для изоляции тестируемого кода. Он проверяет как асинхронные (`AsyncClient`), так и синхронные (`Client`) реализации.

## Классы

### `AsyncTestPassModel`

**Описание**: Класс, содержащий асинхронные тесты для проверки функциональности `AsyncClient`.

**Наследует**: `unittest.IsolatedAsyncioTestCase`

**Методы**:

- `test_response()`:
    ```python
    async def test_response(self):
        """
        Тестирует получение ответа от асинхронного клиента с использованием мок-провайдера.

        Args:
            self (AsyncTestPassModel): Экземпляр класса `AsyncTestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому.
        """
    ```

- `test_pass_model()`:
    ```python
    async def test_pass_model(self):
        """
        Тестирует передачу модели асинхронному клиенту и проверку корректности ответа.

        Args:
            self (AsyncTestPassModel): Экземпляр класса `AsyncTestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому.
        """
    ```

- `test_max_tokens()`:
    ```python
    async def test_max_tokens(self):
        """
        Тестирует ограничение на максимальное количество токенов при генерации ответа асинхронным клиентом.

        Args:
            self (AsyncTestPassModel): Экземпляр класса `AsyncTestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому количеству токенов.
        """
    ```

- `test_max_stream()`:
    ```python
    async def test_max_stream(self):
        """
        Тестирует стриминг ответов от асинхронного клиента и проверку корректности чанков.

        Args:
            self (AsyncTestPassModel): Экземпляр класса `AsyncTestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный чанк не является экземпляром `ChatCompletionChunk` или его содержимое не соответствует ожидаемому.
        """
    ```

- `test_stop()`:
    ```python
    async def test_stop(self):
        """
        Тестирует остановку генерации ответа асинхронным клиентом по стоп-слову.

        Args:
            self (AsyncTestPassModel): Экземпляр класса `AsyncTestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому после остановки.
        """
    ```

### `TestPassModel`

**Описание**: Класс, содержащий синхронные тесты для проверки функциональности `Client`.

**Наследует**: `unittest.TestCase`

**Методы**:

- `test_response()`:
    ```python
    def test_response(self):
        """
        Тестирует получение ответа от синхронного клиента с использованием мок-провайдера.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому.
        """
    ```

- `test_pass_model()`:
    ```python
    def test_pass_model(self):
        """
        Тестирует передачу модели синхронному клиенту и проверку корректности ответа.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому.
        """
    ```

- `test_max_tokens()`:
    ```python
    def test_max_tokens(self):
        """
        Тестирует ограничение на максимальное количество токенов при генерации ответа синхронным клиентом.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому количеству токенов.
        """
    ```

- `test_max_stream()`:
    ```python
    def test_max_stream(self):
        """
        Тестирует стриминг ответов от синхронного клиента и проверку корректности чанков.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный чанк не является экземпляром `ChatCompletionChunk` или его содержимое не соответствует ожидаемому.
        """
    ```

- `test_stop()`:
    ```python
    def test_stop(self):
        """
        Тестирует остановку генерации ответа синхронным клиентом по стоп-слову.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если полученный ответ не является экземпляром `ChatCompletion` или его содержимое не соответствует ожидаемому после остановки.
        """
    ```

- `test_model_not_found()`:
    ```python
    def test_model_not_found(self):
        """
        Тестирует случай, когда модель не найдена при запросе к клиенту.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если не возникает исключение `ModelNotFoundError` при попытке использовать несуществующую модель.
        """
    ```

- `test_best_provider()`:
    ```python
    def test_best_provider(self):
        """
        Тестирует выбор наилучшего провайдера для заданной модели.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если выбранный провайдер не имеет атрибут `create_completion` или модель не соответствует ожидаемой.
        """
    ```

- `test_default_model()`:
    ```python
    def test_default_model(self):
        """
        Тестирует использование модели по умолчанию.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если выбранный провайдер не имеет атрибут `create_completion` или модель не соответствует ожидаемой.
        """
    ```

- `test_provider_as_model()`:
    ```python
    def test_provider_as_model(self):
        """
        Тестирует использование провайдера в качестве модели.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если выбранный провайдер не имеет атрибут `create_completion`, модель не является строкой или не соответствует ожидаемой модели по умолчанию для провайдера.
        """
    ```

- `test_get_model()`:
    ```python
    def test_get_model(self):
        """
        Тестирует получение модели.

        Args:
            self (TestPassModel): Экземпляр класса `TestPassModel`.

        Returns:
            None

        Raises:
            AssertionError: Если выбранный провайдер не имеет атрибут `create_completion` или модель не соответствует ожидаемой.
        """
    ```

## Функции

### `get_model_and_provider`

```python
def get_model_and_provider(model: str, provider_names: list | None = None, stream: bool = False) -> tuple[str, type[Provider.BaseProvider]]:
    """
    Определяет модель и провайдера на основе входных параметров.
    
    Args:
        model (str): Название модели.
        provider_names (list | None): Список имен провайдеров. По умолчанию `None`.
        stream (bool): Флаг стриминга. По умолчанию `False`.
        
    Returns:
        tuple[str, type[Provider.BaseProvider]]: Кортеж, содержащий название модели и тип провайдера.
    
    Raises:
        ModelNotFoundError: Если модель не найдена.
    """
```

**Назначение**: Функция `get_model_and_provider` определяет модель и провайдера, которые будут использоваться для создания ответа. Она принимает название модели, список провайдеров (если есть) и флаг стриминга. Если модель не указана, используется модель по умолчанию. Если провайдер не указан, выбирается наилучший провайдер для данной модели.

**Параметры**:
- `model` (str): Название модели, которую необходимо использовать.
- `provider_names` (list | None): Список названий провайдеров, из которых нужно выбрать. Если `None`, выбирается лучший провайдер автоматически.
- `stream` (bool): Флаг, указывающий, будет ли использоваться стриминг.

**Возвращает**:
- `tuple[str, type[Provider.BaseProvider]]`: Кортеж, содержащий название модели (str) и класс провайдера (type[Provider.BaseProvider]).

**Вызывает исключения**:
- `ModelNotFoundError`: Если указанная модель не найдена.

**Как работает функция**:

1.  Функция принимает название модели (`model`), список провайдеров (`provider_names`) и флаг стриминга (`stream`).
2.  Если название модели не предоставлено, функция устанавливает пустую строку в качестве названия модели.
3.  Если название модели совпадает с именем одного из доступных провайдеров, функция устанавливает `default_model` этого провайдера в качестве названия модели.
4.  Если список провайдеров не предоставлен (`provider_names` is None), функция вызывает `Provider.BestProvider.get_model(model, stream=stream)` для выбора наилучшего провайдера на основе указанной модели и флага стриминга.
5.  Если список провайдеров предоставлен, функция перебирает провайдеров из списка, пока не найдет подходящего.
6.  Функция возвращает кортеж, содержащий название модели и класс выбранного провайдера.
7.  Если модель не найдена, функция вызывает исключение `ModelNotFoundError`.

**ASII flowchart**:

```
A[Получение параметров: model, provider_names, stream]
|
B[Проверка model == ""]
|
C[Если да: model = "", иначе переход к D]
|
D[Проверка model in Provider.__all__]
|
E[Если да: model = Provider.default_model, иначе переход к F]
|
F[Проверка provider_names is None]
|
G[Если да: provider = Provider.BestProvider.get_model(model, stream), иначе переход к H]
|
H[Перебор provider_names для поиска подходящего провайдера]
|
I[Если провайдер найден: provider = найденный провайдер, иначе исключение ModelNotFoundError]
|
J[Возврат кортежа (model, provider)]
```

**Примеры**:

```python
# Пример 1: Использование модели по умолчанию и автоматический выбор провайдера
model, provider = get_model_and_provider("", None, False)
print(f"Модель: {model}, Провайдер: {provider}")

# Пример 2: Использование конкретной модели и автоматический выбор провайдера
model, provider = get_model_and_provider("gpt-4o", None, False)
print(f"Модель: {model}, Провайдер: {provider}")

# Пример 3: Использование провайдера в качестве модели
model, provider = get_model_and_provider("Copilot", None, False)
print(f"Модель: {model}, Провайдер: {provider}")