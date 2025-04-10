# Модуль `types.py`

## Обзор

Модуль `types.py` определяет абстрактные базовые классы для провайдеров, используемых в проекте `hypotez` для взаимодействия с различными языковыми моделями. Он также содержит базовый класс для провайдеров, реализующих логику повторных попыток, и класс для потоковой передачи данных.

## Подробней

Этот модуль предоставляет основные интерфейсы и структуры данных, необходимые для реализации различных провайдеров, обеспечивающих взаимодействие с внешними сервисами генерации текста. Он определяет абстрактные методы, которые должны быть реализованы в конкретных классах провайдеров, а также предоставляет базовую функциональность для обработки повторных попыток и потоковой передачи данных.

## Классы

### `BaseProvider`

**Описание**:
Абстрактный базовый класс для провайдеров.

**Принцип работы**:
Этот класс определяет интерфейс, который должны реализовывать все провайдеры. Он содержит атрибуты, описывающие возможности провайдера, такие как поддержка потоковой передачи, истории сообщений и системных сообщений, а также абстрактные методы для получения функций создания и асинхронного создания.

**Аттрибуты**:
- `url` (str): URL провайдера.
- `working` (bool): Указывает, работает ли провайдер в данный момент.
- `needs_auth` (bool): Указывает, требуется ли провайдеру аутентификация.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `params` (str): Список параметров для провайдера.

**Методы**:
- `get_create_function()`: Возвращает функцию создания для провайдера.
- `get_async_create_function()`: Возвращает асинхронную функцию создания для провайдера.
- `get_dict()`: Возвращает словарь, содержащий детали провайдера.

### `BaseRetryProvider`

**Описание**:
Базовый класс для провайдера, который реализует логику повторных попыток.

**Принцип работы**:
Этот класс расширяет `BaseProvider` и добавляет функциональность для автоматического повтора запросов к другим провайдерам в случае сбоя. Он использует список провайдеров для повторных попыток и предоставляет возможность перемешивания этого списка.

**Аттрибуты**:
- `__name__` (str): Имя провайдера.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.
- `last_provider` (Type[BaseProvider]): Последний использованный провайдер.

### `Streaming`

**Описание**:
Класс для представления потоковых данных.

**Принцип работы**:
Этот класс используется для передачи потоковых данных от провайдера к потребителю. Он содержит данные в виде строки и предоставляет метод `__str__` для получения строкового представления данных.

**Аттрибуты**:
- `data` (str): Строка данных.

## Функции

### `get_create_function`

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

**Назначение**:
Абстрактный метод для получения функции создания для провайдера.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Функция создания.

**Вызывает исключения**:
- `NotImplementedError`: Если метод не реализован в подклассе.

**Как работает функция**:

Функция `get_create_function` является абстрактным методом, который должен быть реализован в каждом подклассе `BaseProvider`. Она предназначена для возврата функции, которая будет использоваться для создания запросов к соответствующему провайдеру.

**Примеры**:

```python
class MyProvider(BaseProvider):
    def get_create_function(self):
        def create_function():
            return "Provider created"
        return create_function
```

### `get_async_create_function`

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

**Назначение**:
Абстрактный метод для получения асинхронной функции создания для провайдера.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `callable`: Асинхронная функция создания.

**Вызывает исключения**:
- `NotImplementedError`: Если метод не реализован в подклассе.

**Как работает функция**:

Функция `get_async_create_function` является абстрактным методом, который должен быть реализован в каждом подклассе `BaseProvider`. Она предназначена для возврата асинхронной функции, которая будет использоваться для асинхронного создания запросов к соответствующему провайдеру.

**Примеры**:

```python
class MyProvider(BaseProvider):
    def get_async_create_function(self):
        async def create_function():
            return "Provider created asynchronously"
        return create_function
```

### `get_dict`

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

**Назначение**:
Получение словарного представления провайдера.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `Dict[str, str]`: Словарь с деталями провайдера.

**Как работает функция**:

Функция `get_dict` возвращает словарь, содержащий имя, URL и метку (если она существует) провайдера. Этот словарь может использоваться для представления провайдера в формате, удобном для сериализации или отображения.

1.  **Формирование словаря**: Функция создает словарь, который будет содержать информацию о провайдере.
2.  **Заполнение информацией**: В словарь добавляются следующие ключи и значения:
    -   `'name'`: Имя класса провайдера (`cls.__name__`).
    -   `'url'`: URL провайдера (`cls.url`).
    -   `'label'`: Метка провайдера, которая получается с помощью `getattr(cls, 'label', None)`. Если атрибут `label` не существует, возвращается `None`.

```
graph LR
A[Начало] --> B{Формирование словаря};
B --> C{Заполнение словаря данными провайдера};
C --> D[Возврат словаря];
```

**Примеры**:

```python
class MyProvider(BaseProvider):
    url = "https://example.com"
    label = "Example Provider"

provider_dict = MyProvider.get_dict()
print(provider_dict)  # {'name': 'MyProvider', 'url': 'https://example.com', 'label': 'Example Provider'}
```
```python
class MyProvider(BaseProvider):
    url = "https://example.com"

provider_dict = MyProvider.get_dict()
print(provider_dict)  # {'name': 'MyProvider', 'url': 'https://example.com', 'label': None}