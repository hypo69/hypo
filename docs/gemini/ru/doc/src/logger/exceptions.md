# Модуль hypotez/src/logger/exceptions.py

## Обзор

Данный модуль определяет пользовательские исключения, используемые в приложении. Он содержит классы для обработки ошибок, связанных с различными компонентами приложения, включая операции с файлами, полями продуктов, подключениями к базе данных KeePass и ошибками PrestaShop WebService.

## Классы

### `CustomException`

**Описание**: Базовый класс пользовательских исключений. Обрабатывает логирование исключений и предоставляет механизм для обработки исходного исключения, если оно существует.

**Атрибуты**:

- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее это пользовательское исключение, если таковое есть.
- `exc_info` (bool): Флаг, указывающий, следует ли регистрировать информацию об исключении.

**Методы**:

- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` сообщением и необязательным исходным исключением.
- `handle_exception(self)`: Обрабатывает исключение, регистрируя ошибку и исходное исключение, если оно доступно.


### `FileNotFoundError`

**Описание**: Исключение, выбрасываемое при отсутствии файла.

**Наследование**: `CustomException`, `IOError`


### `ProductFieldException`

**Описание**: Исключение, выбрасываемое при ошибках, связанных с полями продукта.

**Наследование**: `CustomException`


### `KeePassException`

**Описание**: Исключение, выбрасываемое при ошибках подключения к базе данных KeePass.

**Наследование**: `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin`


### `DefaultSettingsException`

**Описание**: Исключение, выбрасываемое при проблемах с настройками по умолчанию.

**Наследование**: `CustomException`


### `WebDriverException`

**Описание**: Исключение, выбрасываемое при ошибках, связанных с WebDriver.

**Наследование**: `selenium.common.exceptions.WebDriverException`


### `ExecuteLocatorException`

**Описание**: Исключение, выбрасываемое при ошибках, связанных с исполнителями локаторов.

**Наследование**: `CustomException`


### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService. Используется для обработки ошибок при взаимодействии с PrestaShop WebService.

**Атрибуты**:

- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращенный PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке от PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки PrestaShop.

**Методы**:

- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` с предоставленным сообщением и деталями об ошибке.
- `__str__(self)`: Возвращает строковое представление исключения.


### `PrestaShopAuthenticationError`

**Описание**: Исключение, выбрасываемое при ошибках аутентификации PrestaShop WebService (Неавторизован).

**Наследование**: `PrestaShopException`