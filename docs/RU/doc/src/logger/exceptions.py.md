# Модуль `src.logger.exceptions`

## Обзор

Модуль `src.logger.exceptions` определяет пользовательские исключения, используемые в приложении. Эти исключения предназначены для обработки ошибок, связанных с различными компонентами приложения, такими как файловые операции, поля продуктов, соединения с базами данных KeePass и ошибки PrestaShop WebService.

## Оглавление

1. [Классы](#классы)
    - [`CustomException`](#customexception)
    - [`FileNotFoundError`](#filenotfounderror)
    - [`ProductFieldException`](#productfieldexception)
    - [`KeePassException`](#keepassexception)
    - [`DefaultSettingsException`](#defaultsettingsexception)
    - [`WebDriverException`](#webdriverexception)
    - [`ExecuteLocatorException`](#executelocatorexception)
    - [`PrestaShopException`](#prestashopexception)
    - [`PrestaShopAuthenticationError`](#prestashopauthenticationerror)

## Классы

### `CustomException`

**Описание**: Базовый класс для всех пользовательских исключений в приложении. Обрабатывает логирование исключения и предоставляет механизм для работы с исходным исключением, если оно существует.

**Параметры**:
- `message` (str): Сообщение об ошибке.
- `e` (Optional[Exception], optional): Исходное исключение, вызвавшее текущее. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении. По умолчанию `True`.

**Методы**:
- `__init__(message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` с сообщением и исходным исключением.
- `handle_exception()`: Обрабатывает исключение, логируя ошибку и исходное исключение, если оно есть.

### `FileNotFoundError`

**Описание**: Исключение, вызываемое, когда файл не найден.

**Наследуется от**: `CustomException`, `IOError`

### `ProductFieldException`

**Описание**: Исключение, вызываемое при ошибках, связанных с полями продукта.

**Наследуется от**: `CustomException`

### `KeePassException`

**Описание**: Исключение, вызываемое при ошибках соединения с базой данных KeePass.

**Наследуется от**: `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin`

### `DefaultSettingsException`

**Описание**: Исключение, вызываемое при проблемах с настройками по умолчанию.

**Наследуется от**: `CustomException`

### `WebDriverException`

**Описание**: Исключение, вызываемое при проблемах, связанных с WebDriver.

**Наследуется от**: `WDriverException`

### `ExecuteLocatorException`

**Описание**: Исключение, вызываемое при ошибках, связанных с исполнителями локаторов.

**Наследуется от**: `CustomException`

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService.

**Параметры**:
- `msg` (str): Сообщение об ошибке.
- `error_code` (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию `None`.
- `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию ''.
- `ps_error_code` (Optional[int], optional): Код ошибки PrestaShop. По умолчанию `None`.

**Методы**:
- `__init__(msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` с сообщением и деталями ошибки.
- `__str__()`: Возвращает строковое представление исключения.

### `PrestaShopAuthenticationError`

**Описание**: Исключение, вызываемое при ошибках аутентификации PrestaShop (Unauthorized).

**Наследуется от**: `PrestaShopException`