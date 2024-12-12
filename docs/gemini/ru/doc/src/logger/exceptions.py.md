# src.logger.exceptions

## Обзор

Модуль `src.logger.exceptions` определяет пользовательские исключения, используемые в приложении. Эти исключения предназначены для обработки ошибок, связанных с различными компонентами приложения, включая файловые операции, поля продуктов, подключения к базе данных KeePass и ошибки PrestaShop WebService.

## Оглавление

- [Классы](#классы)
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

**Описание**: Базовый класс для всех пользовательских исключений в приложении. Он обрабатывает логирование исключения и предоставляет механизм для работы с исходным исключением, если оно существует.

**Атрибуты**:
- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее это пользовательское исключение, если таковое имеется.
- `exc_info` (bool): Флаг, указывающий, следует ли логировать информацию об исключении.

**Методы**:

#### `__init__`

**Описание**: Инициализирует `CustomException` сообщением и необязательным исходным исключением.

**Параметры**:
- `message` (str): Сообщение об ошибке.
- `e` (Optional[Exception], optional): Исходное исключение. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг для указания, нужно ли логировать информацию об исключении. По умолчанию `True`.

#### `handle_exception`

**Описание**: Обрабатывает исключение, логируя ошибку и исходное исключение, если оно доступно.

**Параметры**:
- нет

### `FileNotFoundError`

**Описание**: Исключение, возникающее, когда файл не найден.

**Наследует от**:
- `CustomException`
- `IOError`

### `ProductFieldException`

**Описание**: Исключение, возникающее при ошибках, связанных с полями продукта.

**Наследует от**:
- `CustomException`

### `KeePassException`

**Описание**: Исключение, возникающее при проблемах с подключением к базе данных KeePass.

**Наследует от**:
- `CredentialsError`
- `BinaryError`
- `HeaderChecksumError`
- `PayloadChecksumError`
- `UnableToSendToRecycleBin`

### `DefaultSettingsException`

**Описание**: Исключение, возникающее при проблемах с настройками по умолчанию.

**Наследует от**:
- `CustomException`

### `WebDriverException`

**Описание**: Исключение, возникающее при проблемах, связанных с WebDriver.

**Наследует от**:
- `WDriverException`

### `ExecuteLocatorException`

**Описание**: Исключение, возникающее при ошибках, связанных с исполнителями локаторов.

**Наследует от**:
- `CustomException`

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService. Используется для обработки ошибок, возникающих при взаимодействии с PrestaShop WebService.

**Атрибуты**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращенный PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке от PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки PrestaShop.

**Методы**:

#### `__init__`

**Описание**: Инициализирует `PrestaShopException` с предоставленным сообщением и деталями ошибки.

**Параметры**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int], optional): Код ошибки. По умолчанию `None`.
- `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию `''`.
- `ps_error_code` (Optional[int], optional): Код ошибки PrestaShop. По умолчанию `None`.

#### `__str__`

**Описание**: Возвращает строковое представление исключения.

**Возвращает**:
- `str`: Строковое представление ошибки (`ps_error_msg` если есть, иначе `msg`).

### `PrestaShopAuthenticationError`

**Описание**: Исключение, возникающее при ошибках аутентификации PrestaShop (не авторизовано).

**Наследует от**:
- `PrestaShopException`