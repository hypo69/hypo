# Модуль exceptions

## Обзор

Модуль `exceptions.py` содержит определения пользовательских исключений, используемых в приложении `hypotez`. Эти исключения предназначены для обработки ошибок, связанных с различными компонентами приложения, такими как файловые операции, поля продуктов, соединения с базами данных KeePass и ошибки PrestaShop WebService.

## Подробней

Этот модуль предоставляет набор пользовательских классов исключений, которые наследуются от базового класса `Exception` или других встроенных классов исключений. Использование этих исключений позволяет более точно и структурированно обрабатывать ошибки, возникающие в различных частях приложения.

## Классы

### `CustomException`

**Описание**: Базовый класс для всех пользовательских исключений в приложении. Он обеспечивает механизм журналирования исключений и обработки исходного исключения, если оно существует.

**Методы**:
- `__init__`: Инициализирует `CustomException` сообщением и необязательным исходным исключением.
- `handle_exception`: Обрабатывает исключение, логируя ошибку и исходное исключение, если оно доступно.

**Параметры**:
- `message` (str): Сообщение об ошибке.
- `e` (Optional[Exception], optional): Исходное исключение, вызвавшее это пользовательское исключение. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении. По умолчанию `True`.

**Примеры**
```python
try:
    raise CustomException('Пример ошибки', ValueError('Неверное значение'))
except CustomException as ex:
    print(f'Произошло исключение: {ex}')
```

### `FileNotFoundError`

**Описание**: Исключение, вызываемое, когда файл не найден.

**Примеры**
```python
try:
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as ex:
    print(f'Файл не найден: {ex}')
```

### `ProductFieldException`

**Описание**: Исключение, вызываемое при ошибках, связанных с полями продукта.

**Примеры**
```python
try:
    raise ProductFieldException('Неверное поле продукта')
except ProductFieldException as ex:
    print(f'Ошибка в поле продукта: {ex}')
```

### `KeePassException`

**Описание**: Исключение, вызываемое при проблемах с соединением с базой данных KeePass.

### `DefaultSettingsException`

**Описание**: Исключение, вызываемое при проблемах с настройками по умолчанию.

### `WebDriverException`

**Описание**: Исключение, вызываемое при проблемах, связанных с WebDriver.

### `ExecuteLocatorException`

**Описание**: Исключение, вызываемое при ошибках, связанных с исполнителями локаторов.

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService. Используется для обработки ошибок, возникающих при взаимодействии с PrestaShop WebService.

**Методы**:
- `__init__`: Инициализирует `PrestaShopException` с предоставленным сообщением и деталями ошибки.
- `__str__`: Возвращает строковое представление исключения.

**Параметры**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию `None`.
- `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию ''.
- `ps_error_code` (Optional[int], optional): Код ошибки PrestaShop. По умолчанию `None`.

**Примеры**
```python
try:
    raise PrestaShopException('Ошибка PrestaShop', ps_error_msg='Неверный формат данных')
except PrestaShopException as ex:
    print(f'Ошибка PrestaShop: {ex}')
```

### `PrestaShopAuthenticationError`

**Описание**: Исключение, вызываемое при ошибках аутентификации PrestaShop (несанкционированный доступ).

## Функции

В данном модуле нет отдельных функций, только классы исключений.

```python
class CustomException(Exception):
    """Base custom exception class.
    
    This is the base class for all custom exceptions in the application. It handles logging of the exception
    and provides a mechanism for dealing with the original exception if it exists.
    
    Attributes:
    ----------
    original_exception : Optional[Exception]
        The original exception that caused this custom exception, if any.
    exc_info : bool
        A flag to indicate if exception information should be logged.
    """
    
    def __init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True):\
        """Initializes the CustomException with a message and an optional original exception."""
        super().__init__(message)
        self.original_exception = e
        self.exc_info = exc_info
        self.handle_exception()

    def handle_exception(self):\
        """Handles the exception by logging the error and original exception, if available."""
        logger.error(f"Exception occurred: {self}")
        if self.original_exception:
            logger.debug(f"Original exception: {self.original_exception}")
        # Add recovery logic, retries, or other handling as necessary.
```

**Описание**: Базовый класс для всех пользовательских исключений в приложении.

**Методы**:
- `__init__`: Инициализирует `CustomException` сообщением и необязательным исходным исключением.
- `handle_exception`: Обрабатывает исключение, логируя ошибку и исходное исключение, если оно доступно.

**Параметры**:
- `message` (str): Сообщение об ошибке.
- `e` (Optional[Exception], optional): Исходное исключение, вызвавшее это пользовательское исключение. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении. По умолчанию `True`.

**Возвращает**:
- None

**Вызывает исключения**:
- None

**Как работает функция**:
1.  Инициализирует экземпляр класса `CustomException`, принимая сообщение об ошибке, исходное исключение (если есть) и флаг логирования.
2.  Вызывает метод `handle_exception` для обработки исключения.
3.  В методе `handle_exception` логирует сообщение об ошибке с использованием `logger.error`.
4.  Если присутствует исходное исключение, логирует его с использованием `logger.debug`.

**Примеры**:

```python
from src.logger import logger

try:
    raise CustomException('Пример ошибки', ValueError('Неверное значение'))
except CustomException as ex:
    logger.error(f'Произошло исключение: {ex}', exc_info=True)