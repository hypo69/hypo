# Модуль hypotez/src/logger/exceptions.py

## Обзор

Данный модуль определяет пользовательские исключения, используемые в приложении. Он содержит классы для обработки ошибок, связанных с различными компонентами приложения, включая операции с файлами, полями продуктов, подключениями к базе данных KeePass и ошибками веб-сервиса PrestaShop.

## Классы

### `CustomException`

**Описание**: Базовый пользовательский класс исключений. Обрабатывает логирование исключений и предоставляет механизм для работы с исходным исключением, если оно существует.

**Атрибуты**:
- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее данное пользовательское исключение.
- `exc_info` (bool): Флаг, указывающий, нужно ли регистрировать информацию об исключении.

**Методы**:
- `__init__(message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` с сообщением и необязательным исходным исключением. Вызывает метод `handle_exception()`.
- `handle_exception()`: Обрабатывает исключение, регистрируя ошибку и исходное исключение (если оно доступно).


### `FileNotFoundError`

**Описание**: Исключение, генерируемое, когда файл не найден.

**Наследование**: `CustomException`, `IOError`

### `ProductFieldException`

**Описание**: Исключение, генерируемое при ошибках, связанных с полями продукта.

**Наследование**: `CustomException`

### `KeePassException`

**Описание**: Исключение, генерируемое при проблемах с подключением к базе данных KeePass.

**Наследование**: `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin`


### `DefaultSettingsException`

**Описание**: Исключение, генерируемое при проблемах с настройками по умолчанию.

**Наследование**: `CustomException`

### `WebDriverException`

**Описание**: Исключение, генерируемое при проблемах с WebDriver.

**Наследование**: `selenium.common.exceptions.WebDriverException`

### `ExecuteLocatorException`

**Описание**: Исключение, генерируемое при ошибках, связанных с исполнителями локейторов.

**Наследование**: `CustomException`

### `PrestaShopException`

**Описание**: Общее исключение для ошибок веб-сервиса PrestaShop. Используется для обработки ошибок при взаимодействии с веб-сервисом PrestaShop.

**Атрибуты**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращённый PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке от PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки от PrestaShop.

**Методы**:
- `__init__(msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` с предоставленным сообщением и деталями ошибки.
- `__str__()`: Возвращает строковое представление исключения.


### `PrestaShopAuthenticationError`

**Описание**: Исключение для ошибок аутентификации PrestaShop (Unauthorized).

**Наследование**: `PrestaShopException`