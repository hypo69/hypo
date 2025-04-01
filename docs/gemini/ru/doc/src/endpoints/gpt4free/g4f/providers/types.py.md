# Модуль types.py

## Обзор

Модуль определяет базовые классы и типы, используемые провайдерами в проекте `hypotez`. Он содержит абстрактные классы для базовых и отказоустойчивых провайдеров, а также класс `Streaming` для обработки потоковых данных.

## Подробнее

Этот модуль предоставляет основу для создания различных провайдеров, используемых для взаимодействия с внешними сервисами. Абстрактные классы `BaseProvider` и `BaseRetryProvider` задают интерфейс и общую логику для этих провайдеров.

## Классы

### `BaseProvider`

**Описание**: Абстрактный базовый класс для провайдера. Определяет основные атрибуты и методы, которыми должен обладать каждый провайдер.

**Принцип работы**:
Класс `BaseProvider` служит основой для создания конкретных провайдеров. Он определяет атрибуты, такие как URL провайдера, его текущее состояние (работает или нет), необходимость аутентификации, поддержку потоковой передачи и истории сообщений. Также он включает абстрактные методы для получения функций создания (create) и асинхронного создания (async create), которые должны быть реализованы в подклассах.

**Атрибуты**:
- `url` (str): URL провайдера.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `needs_auth` (bool): Указывает, требуется ли аутенфикация для работы с провайдером.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `params` (str): Список параметров для провайдера.

**Методы**:
- `get_create_function`

    ```python
    @abstractmethod
    def get_create_function() -> callable:
        """
        Get the create function for the provider.

        Returns:
            callable: The create function.
        """
        raise NotImplementedError()
    ```

    **Назначение**: Абстрактный метод для получения функции создания провайдера.

    **Возвращает**:
    - `callable`: Функция создания.

    **Вызывает исключения**:
    - `NotImplementedError`: Если метод не реализован в подклассе.

    **Как работает функция**:
    1. Метод `get_create_function` предназначен для возврата функции, которая создает экземпляр провайдера.
    2. Так как метод является абстрактным, он должен быть переопределен в каждом подклассе `BaseProvider`.
    3. При вызове этого метода в базовом классе возбуждается исключение `NotImplementedError`, указывающее на необходимость реализации в подклассе.

    **Примеры**:
    ```python
    class MyProvider(BaseProvider):
        def get_create_function(self):
            def create():
                return "Создан экземпляр MyProvider"
            return create

    provider = MyProvider()
    create_func = provider.get_create_function()
    result = create_func()
    print(result)  # Вывод: Создан экземпляр MyProvider
    ```

- `get_async_create_function`

    ```python
    @abstractmethod
    def get_async_create_function() -> callable:
        """
        Get the async create function for the provider.

        Returns:
            callable: The create function.
        """
        raise NotImplementedError()
    ```

    **Назначение**: Абстрактный метод для получения асинхронной функции создания провайдера.

    **Возвращает**:
    - `callable`: Асинхронная функция создания.

    **Вызывает исключения**:
    - `NotImplementedError`: Если метод не реализован в подклассе.

    **Как работает функция**:
    1. Метод `get_async_create_function` предназначен для возврата асинхронной функции, которая создает экземпляр провайдера.
    2. Так как метод является абстрактным, он должен быть переопределен в каждом подклассе `BaseProvider`.
    3. При вызове этого метода в базовом классе возбуждается исключение `NotImplementedError`, указывающее на необходимость реализации в подклассе.

    **Примеры**:
    ```python
    import asyncio

    class MyProvider(BaseProvider):
        def get_async_create_function(self):
            async def create():
                return "Создан асинхронный экземпляр MyProvider"
            return create

    async def main():
        provider = MyProvider()
        create_func = provider.get_async_create_function()
        result = await create_func()
        print(result)  # Вывод: Создан асинхронный экземпляр MyProvider

    asyncio.run(main())
    ```

- `get_dict`

    ```python
    @classmethod
    def get_dict(cls) -> Dict[str, str]:
        """
        Get a dictionary representation of the provider.

        Returns:
            Dict[str, str]: A dictionary with provider's details.
        """
        return {'name': cls.__name__, 'url': cls.url, 'label': getattr(cls, 'label', None)}
    ```

    **Назначение**: Метод класса для получения словарного представления провайдера.

    **Возвращает**:
    - `Dict[str, str]`: Словарь с деталями провайдера (имя, URL и метка).

    **Как работает функция**:
    1. Метод `get_dict` создает и возвращает словарь, содержащий информацию о провайдере.
    2. В словарь включаются следующие ключи:
        - `'name'`: Имя класса провайдера (`cls.__name__`).
        - `'url'`: URL провайдера (`cls.url`).
        - `'label'`: Метка провайдера, полученная с помощью `getattr(cls, 'label', None)`, которая возвращает значение атрибута `label`, если он существует, иначе `None`.

    **Примеры**:
    ```python
    class MyProvider(BaseProvider):
        url = "http://example.com"
        label = "Example Provider"

    provider_dict = MyProvider.get_dict()
    print(provider_dict)  # Вывод: {'name': 'MyProvider', 'url': 'http://example.com', 'label': 'Example Provider'}
    ```

### `BaseRetryProvider`

**Описание**: Базовый класс для провайдера, реализующий логику повторных попыток.

**Принцип работы**:
Класс `BaseRetryProvider` наследуется от `BaseProvider` и предоставляет механизм для повторных попыток при взаимодействии с провайдерами. Он содержит атрибуты для хранения списка провайдеров, используемых для повторных попыток, флага для перемешивания списка провайдеров, словаря исключений и информации о последнем использованном провайдере.

**Атрибуты**:
- `__name__` (str): Имя провайдера. По умолчанию "RetryProvider".
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных. Всегда `True`.
- `last_provider` (Type[BaseProvider]): Последний использованный провайдер.

### `Streaming`

**Описание**: Класс для представления потоковых данных.

**Принцип работы**:
Класс `Streaming` используется для обертки потоковых данных в виде строки. Он принимает данные в конструкторе и возвращает их в строковом представлении.

**Атрибуты**:
- `data` (str): Строка, содержащая потоковые данные.

**Методы**:
- `__init__`

    ```python
    def __init__(self, data: str) -> None:
        self.data = data
    ```

    **Назначение**: Конструктор класса `Streaming`.

    **Параметры**:
    - `data` (str): Строка, содержащая потоковые данные.

    **Как работает функция**:
    1. Метод `__init__` является конструктором класса `Streaming`.
    2. При создании экземпляра класса `Streaming`, конструктор принимает параметр `data` (строку) и сохраняет его в атрибуте `self.data`.

    **Примеры**:
    ```python
    streaming_data = Streaming("Пример потоковых данных")
    print(streaming_data.data)  # Вывод: Пример потоковых данных
    ```

- `__str__`

    ```python
    def __str__(self) -> str:
        return self.data
    ```

    **Назначение**: Метод для получения строкового представления объекта `Streaming`.

    **Возвращает**:
    - `str`: Строка, содержащая потоковые данные.

    **Как работает функция**:
    1. Метод `__str__` вызывается, когда объект класса `Streaming` нужно представить в виде строки.
    2. Метод возвращает значение атрибута `self.data`, которое содержит потоковые данные.

    **Примеры**:
    ```python
    streaming_data = Streaming("Пример потоковых данных")
    print(str(streaming_data))  # Вывод: Пример потоковых данных
    ```

## Типы

- `ProviderType` (`Union[Type[BaseProvider], BaseRetryProvider]`): Тип, представляющий либо базового провайдера, либо провайдера с повторными попытками.