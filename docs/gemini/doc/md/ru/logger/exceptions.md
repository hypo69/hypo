```markdown
# Модуль exceptions

## Обзор

Этот модуль определяет пользовательские исключения, используемые в приложении. Он содержит классы для обработки ошибок, связанных с файлами, полями продуктов, подключением к базе данных KeePass, и ошибками PrestaShop WebService.

## Классы

### `CustomException`

**Описание**: Базовый класс пользовательских исключений. Обрабатывает логирование исключения и предоставляет механизм для работы с исходным исключением, если оно существует.

**Атрибуты**:
- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее данное пользовательское исключение.
- `exc_info` (bool): Флаг, указывающий, должна ли информация об исключении быть записана в журнал.

**Методы**:
- `__init__(message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` с сообщением и необязательным исходным исключением.
- `handle_exception()`: Обрабатывает исключение, записывая ошибку и, если доступно, исходное исключение в журнал.


### `FileNotFoundError`

**Описание**: Исключение, поднимаемое при отсутствии файла. Наследуется от `IOError`.

**Наследуется от**: `CustomException`, `IOError`


### `ProductFieldException`

**Описание**: Исключение, поднимаемое при ошибках, связанных с полями продуктов.

**Наследуется от**: `CustomException`


### `KeePassException`

**Описание**: Исключение, поднимаемое при проблемах с подключением к базе данных KeePass.

**Наследуется от**: `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin`


### `DefaultSettingsException`

**Описание**: Исключение, поднимаемое при проблемах с настройками по умолчанию.

**Наследуется от**: `CustomException`


### `WebDriverException`

**Описание**: Исключение, поднимаемое при проблемах с WebDriver.

**Наследуется от**: `selenium.common.exceptions.WebDriverException`


### `ExecuteLocatorException`

**Описание**: Исключение, поднимаемое при ошибках, связанных с исполнителями локаторов.

**Наследуется от**: `CustomException`


### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService. Используется для обработки ошибок при взаимодействии с PrestaShop WebService.

**Атрибуты**:
- `msg` (str): Сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращённый PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке из PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки PrestaShop.

**Методы**:
- `__init__(msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException`.
- `__str__()`: Возвращает строковое представление исключения.


### `PrestaShopAuthenticationError`

**Описание**: Исключение для ошибок аутентификации PrestaShop WebService (неавторизован).

**Наследуется от**: `PrestaShopException`
```
