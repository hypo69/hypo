# Модуль hypotez/src/logger/exceptions.py

## Обзор

Этот модуль определяет пользовательские исключения, используемые в приложении. Он содержит классы исключений для обработки ошибок, связанных с различными компонентами приложения, включая операции с файлами, полями продуктов, подключениями к базе данных KeePass и ошибками PrestaShop WebService.


## Классы

### `CustomException`

**Описание**: Базовый пользовательский класс исключения. Обрабатывает логирование исключения и предоставляет механизм для работы с исходным исключением, если оно есть.

**Атрибуты**:

- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее это пользовательское исключение, если таковое имеется.
- `exc_info` (bool): Флаг, указывающий, должна ли информация об исключении записываться в журнал.

**Методы**:

- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` сообщением и необязательным исходным исключением.
- `handle_exception(self)`: Обрабатывает исключение, записывая ошибку и исходное исключение (если оно доступно) в журнал.


### `FileNotFoundError`

**Описание**: Исключение, поднимаемое при отсутствии файла.

**Наследование**: `CustomException`, `IOError`


### `ProductFieldException`

**Описание**: Исключение, поднимаемое при ошибках, связанных с полями продуктов.

**Наследование**: `CustomException`


### `KeePassException`

**Описание**: Исключение, поднимаемое при проблемах с подключением к базе данных KeePass.

**Наследование**: `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin`


### `DefaultSettingsException`

**Описание**: Исключение, поднимаемое при проблемах с настройками по умолчанию.

**Наследование**: `CustomException`


### `WebDriverException`

**Описание**: Исключение, поднимаемое при проблемах, связанных с WebDriver.

**Наследование**: `selenium.common.exceptions.WebDriverException`


### `ExecuteLocatorException`

**Описание**: Исключение, поднимаемое при ошибках, связанных с исполнителями локаторов.

**Наследование**: `CustomException`


### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService. Используется для обработки ошибок, возникающих при взаимодействии с PrestaShop WebService.

**Атрибуты**:

- `msg` (str): Сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращённый PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке из PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки из PrestaShop.


**Методы**:

- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` с предоставленным сообщением и деталями об ошибке.
- `__str__(self)`: Возвращает строковое представление исключения.


### `PrestaShopAuthenticationError`

**Описание**: Исключение, поднимаемое при ошибках аутентификации PrestaShop WebService (Unauthorized).

**Наследование**: `PrestaShopException`


## Константы

### `MODE`

**Описание**: Строковая константа, представляющая режим работы (например, 'dev').


```