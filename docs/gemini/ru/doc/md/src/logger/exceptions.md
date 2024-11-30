# Модуль hypotez/src/logger/exceptions.py

## Обзор

Этот модуль определяет пользовательские исключения, используемые в приложении. Он содержит классы для обработки ошибок, связанных с различными компонентами приложения, включая операции с файлами, полями продуктов, соединениями с базой данных KeePass и ошибками веб-сервиса PrestaShop.

## Классы

### `CustomException`

**Описание**: Базовый пользовательский класс исключений. Обрабатывает логирование исключения и предоставляет механизм обработки исходного исключения, если оно существует.

**Атрибуты**:

- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее это пользовательское исключение, если оно есть.
- `exc_info` (bool): Флаг, указывающий, должна ли информация об исключении записываться в журнал.

**Методы**:

- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` с сообщением и необязательным исходным исключением.
- `handle_exception(self)`: Обрабатывает исключение, записывая ошибку и исходное исключение (если доступно) в журнал.

### `FileNotFoundError`

**Описание**: Исключение, выбрасываемое, когда файл не найден.

**Наследование**: `CustomException`, `IOError`

### `ProductFieldException`

**Описание**: Исключение, выбрасываемое при ошибках, связанных с полями продукта.

**Наследование**: `CustomException`

### `KeePassException`

**Описание**: Исключение, выбрасываемое при проблемах подключения к базе данных KeePass.

**Наследование**: `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin`

### `DefaultSettingsException`

**Описание**: Исключение, выбрасываемое при проблемах с настройками по умолчанию.

**Наследование**: `CustomException`

### `WebDriverException`

**Описание**: Исключение, выбрасываемое при проблемах, связанных с WebDriver.

**Наследование**: `selenium.common.exceptions.WebDriverException`

### `ExecuteLocatorException`

**Описание**: Исключение, выбрасываемое при ошибках, связанных с исполнителями локаторов.

**Наследование**: `CustomException`


### `PrestaShopException`

**Описание**: Общее исключение для ошибок веб-сервиса PrestaShop. Используется для обработки ошибок при взаимодействии с веб-сервисом PrestaShop.

**Атрибуты**:

- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращённый PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке от PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки PrestaShop.

**Методы**:

- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` с предоставленным сообщением и подробностями об ошибке.
- `__str__(self)`: Возвращает строковое представление исключения.


### `PrestaShopAuthenticationError`

**Описание**: Исключение, выбрасываемое при ошибках аутентификации PrestaShop (Unauthorized).

**Наследование**: `PrestaShopException`