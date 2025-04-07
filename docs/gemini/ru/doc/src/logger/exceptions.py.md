# Модуль `src.logger.exceptions`

## Обзор

Модуль `src.logger.exceptions` предназначен для определения пользовательских исключений, используемых в приложении. Он содержит набор классов исключений, которые позволяют обрабатывать ошибки, связанные с различными компонентами приложения, такими как файловые операции, поля продуктов, подключение к базам данных KeePass и ошибки PrestaShop WebService.

## Подробней

Этот модуль предоставляет базовый класс `CustomException`, от которого наследуются другие классы исключений. `CustomException` обеспечивает механизм логирования ошибок и обработки исходных исключений, если они существуют.

## Классы

### `CustomException`

**Описание**: Базовый класс для всех пользовательских исключений в приложении. Обеспечивает логирование ошибок и обработку исходного исключения, если оно доступно.

**Аттрибуты**:

- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее данное пользовательское исключение, если оно есть.
- `exc_info` (bool): Флаг, указывающий, следует ли логировать информацию об исключении.

**Методы**:

- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` с сообщением и исходным исключением (если есть).
- `handle_exception(self)`: Обрабатывает исключение, логируя ошибку и исходное исключение (если доступно).

### `FileNotFoundError`

**Описание**: Исключение, которое выбрасывается, когда файл не найден.

**Наследует**:

- `CustomException`
- `IOError`

### `ProductFieldException`

**Описание**: Исключение, которое выбрасывается при ошибках, связанных с полями продуктов.

**Наследует**:

- `CustomException`

### `KeePassException`

**Описание**: Исключение, которое выбрасывается при проблемах с подключением к базе данных KeePass.

**Наследует**:

- `CredentialsError`
- `BinaryError`
- `HeaderChecksumError`
- `PayloadChecksumError`
- `UnableToSendToRecycleBin`

### `DefaultSettingsException`

**Описание**: Исключение, которое выбрасывается при проблемах с настройками по умолчанию.

**Наследует**:

- `CustomException`

### `WebDriverException`

**Описание**: Исключение, которое выбрасывается при проблемах, связанных с WebDriver.

**Наследует**:

- `selenium.common.exceptions.WebDriverException`

### `ExecuteLocatorException`

**Описание**: Исключение, которое выбрасывается при ошибках, связанных с исполнителями локаторов.

**Наследует**:

- `CustomException`

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService. Используется для обработки ошибок, возникающих при взаимодействии с PrestaShop WebService.

**Аттрибуты**:

- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращенный PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке от PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки от PrestaShop.

**Методы**:

- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` с сообщением и деталями ошибки.
- `__str__(self)`: Возвращает строковое представление исключения.

### `PrestaShopAuthenticationError`

**Описание**: Исключение, которое выбрасывается при ошибках аутентификации PrestaShop (Unauthorized).

**Наследует**:

- `PrestaShopException`

## Функции

### `CustomException.__init__`

```python
    def __init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True):
        """Initializes the CustomException with a message and an optional original exception."""
        super().__init__(message)
        self.original_exception = e
        self.exc_info = exc_info
        self.handle_exception()
```

**Назначение**: Инициализирует экземпляр класса `CustomException`.

**Параметры**:

- `message` (str): Сообщение об ошибке.
- `e` (Optional[Exception]): Исходное исключение, которое вызвало текущее исключение (если есть).
- `exc_info` (bool): Флаг, определяющий, нужно ли логировать информацию об исключении. По умолчанию `True`.

**Как работает функция**:

1. Вызывает конструктор родительского класса `Exception`, передавая ему сообщение об ошибке.
2. Сохраняет исходное исключение в атрибуте `self.original_exception`.
3. Сохраняет значение флага `exc_info` в атрибуте `self.exc_info`.
4. Вызывает метод `self.handle_exception()` для обработки исключения.

**Примеры**:

```python
from src.logger.exceptions import CustomException

try:
    raise ValueError("Некорректное значение")
except ValueError as ex:
    custom_ex = CustomException("Произошла ошибка значения", ex)
```

### `CustomException.handle_exception`

```python
    def handle_exception(self):
        """Handles the exception by logging the error and original exception, if available."""
        logger.error(f"Exception occurred: {self}")
        if self.original_exception:
            logger.debug(f"Original exception: {self.original_exception}")
        # Add recovery logic, retries, or other handling as necessary.
```

**Назначение**: Обрабатывает исключение, логируя информацию об ошибке и исходном исключении (если оно есть).

**Как работает функция**:

1. Логирует сообщение об ошибке с использованием `logger.error`.
2. Проверяет, существует ли исходное исключение.
3. Если исходное исключение существует, логирует информацию о нем с использованием `logger.debug`.

**Примеры**:

```python
from src.logger.exceptions import CustomException
from src.logger.logger import logger  # Предполагается, что модуль logger доступен

try:
    raise ValueError("Некорректное значение")
except ValueError as ex:
    custom_ex = CustomException("Произошла ошибка значения", ex)
```

### `PrestaShopException.__init__`

```python
    def __init__(self, msg: str, error_code: Optional[int] = None, 
                 ps_error_msg: str = '', ps_error_code: Optional[int] = None):
        """Initializes the PrestaShopException with the provided message and error details."""
        self.msg = msg
        self.error_code = error_code
        self.ps_error_msg = ps_error_msg
        self.ps_error_code = ps_error_code
```

**Назначение**: Инициализирует экземпляр класса `PrestaShopException`.

**Параметры**:

- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращенный приложением. По умолчанию `None`.
- `ps_error_msg` (str): Сообщение об ошибке от PrestaShop. По умолчанию `''`.
- `ps_error_code` (Optional[int]): Код ошибки от PrestaShop. По умолчанию `None`.

**Как работает функция**:

1. Сохраняет пользовательское сообщение об ошибке в атрибуте `self.msg`.
2. Сохраняет код ошибки приложения в атрибуте `self.error_code`.
3. Сохраняет сообщение об ошибке от PrestaShop в атрибуте `self.ps_error_msg`.
4. Сохраняет код ошибки от PrestaShop в атрибуте `self.ps_error_code`.

**Примеры**:

```python
from src.logger.exceptions import PrestaShopException

ex = PrestaShopException("Ошибка при подключении к PrestaShop", ps_error_msg="Неверный логин или пароль", ps_error_code=10)
```

### `PrestaShopException.__str__`

```python
    def __str__(self):
        """Returns the string representation of the exception."""
        return repr(self.ps_error_msg or self.msg)
```

**Назначение**: Возвращает строковое представление исключения.

**Как работает функция**:

1. Возвращает строковое представление либо сообщения об ошибке от PrestaShop (`self.ps_error_msg`), если оно не пустое, либо пользовательского сообщения об ошибке (`self.msg`).

**Примеры**:

```python
from src.logger.exceptions import PrestaShopException

ex = PrestaShopException("Ошибка при подключении к PrestaShop", ps_error_msg="Неверный логин или пароль")
print(str(ex))  # Выведет: 'Неверный логин или пароль'

ex = PrestaShopException("Ошибка при подключении к PrestaShop")
print(str(ex))  # Выведет: 'Ошибка при подключении к PrestaShop'
```