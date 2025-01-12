# Модуль `src.logger.exceptions`

## Обзор

Модуль `src.logger.exceptions` определяет пользовательские исключения, используемые в приложении. Эти исключения предназначены для обработки ошибок, связанных с различными компонентами приложения, включая файловые операции, поля продукта, подключения к базе данных KeePass и ошибки PrestaShop WebService.

## Содержание

1.  [Классы](#Классы)
    *   [CustomException](#CustomException)
    *   [FileNotFoundError](#FileNotFoundError)
    *   [ProductFieldException](#ProductFieldException)
    *   [KeePassException](#KeePassException)
    *   [DefaultSettingsException](#DefaultSettingsException)
    *   [WebDriverException](#WebDriverException)
    *   [ExecuteLocatorException](#ExecuteLocatorException)
    *   [PrestaShopException](#PrestaShopException)
    *   [PrestaShopAuthenticationError](#PrestaShopAuthenticationError)

## Классы

### `CustomException`

**Описание**: Базовый класс для пользовательских исключений. Обрабатывает логирование исключения и предоставляет механизм для работы с исходным исключением.

**Параметры**:

*   `message` (str): Сообщение об ошибке.
*   `e` (Optional[Exception], optional): Исходное исключение, вызвавшее это исключение. По умолчанию `None`.
*   `exc_info` (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении. По умолчанию `True`.

**Методы**:

*   `__init__`: Инициализирует `CustomException` с сообщением и исходным исключением.
*   `handle_exception`: Обрабатывает исключение, логируя ошибку и исходное исключение, если оно есть.

### `FileNotFoundError`

**Описание**: Исключение, возникающее, когда файл не найден.

**Наследует от**: `CustomException`, `IOError`

### `ProductFieldException`

**Описание**: Исключение, возникающее при ошибках, связанных с полями продукта.

**Наследует от**: `CustomException`

### `KeePassException`

**Описание**: Исключение, возникающее при проблемах с подключением к базе данных KeePass.

**Наследует от**: `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError`, `UnableToSendToRecycleBin`

### `DefaultSettingsException`

**Описание**: Исключение, возникающее при проблемах с настройками по умолчанию.

**Наследует от**: `CustomException`

### `WebDriverException`

**Описание**: Исключение, возникающее при проблемах, связанных с WebDriver.

**Наследует от**: `WDriverException`

### `ExecuteLocatorException`

**Описание**: Исключение, возникающее при ошибках, связанных с исполнителями локаторов.

**Наследует от**: `CustomException`

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService.

**Параметры**:

*   `msg` (str): Пользовательское сообщение об ошибке.
*   `error_code` (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию `None`.
*   `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию `''`.
*   `ps_error_code` (Optional[int], optional): Код ошибки от PrestaShop. По умолчанию `None`.

**Методы**:

*   `__init__`: Инициализирует `PrestaShopException` с сообщением и деталями ошибки.
*   `__str__`: Возвращает строковое представление исключения.

### `PrestaShopAuthenticationError`

**Описание**: Исключение, возникающее при ошибках аутентификации PrestaShop (не авторизовано).

**Наследует от**: `PrestaShopException`