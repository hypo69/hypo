# Модуль exceptions

## Обзор

Модуль `exceptions` определяет пользовательские исключения, используемые в приложении.

## Подробней

Этот модуль содержит несколько пользовательских классов исключений для обработки ошибок, связанных с различными компонентами приложения, включая файловые операции, поля продуктов, подключения к базам данных KeePass и ошибки PrestaShop WebService.

## Содержание

- [CustomException](#customexception)
  - [Описание](#описание)
  - [Методы](#методы)
    - [`__init__`](#__init__)
    - [`handle_exception`](#handle_exception)
- [FileNotFoundError](#filenotfounderror)
- [ProductFieldException](#productfieldexception)
- [KeePassException](#keepassexception)
- [DefaultSettingsException](#defaultsettingsexception)
- [WebDriverException](#webdriverexception)
- [ExecuteLocatorException](#executelocatorexception)
- [PrestaShopException](#prestashopexception)
  - [Описание](#описание-1)
  - [Методы](#методы-1)
    - [`__init__`](#__init__-1)
    - [`__str__`](#__str__)
- [PrestaShopAuthenticationError](#prestashopauthenticationerror)

## Классы

### `CustomException`

**Описание**: Базовый класс пользовательских исключений.

**Как работает класс**: Этот класс является базовым для всех пользовательских исключений в приложении. Он обрабатывает логирование исключения и предоставляет механизм для работы с исходным исключением, если оно существует.

**Методы**:

- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`

    ```python
    def __init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True) -> None:
        """
        Инициализирует CustomException с сообщением и необязательным исходным исключением.

        Args:
            message (str): Сообщение об исключении.
            e (Optional[Exception], optional): Исходное исключение, вызвавшее данное исключение. По умолчанию None.
            exc_info (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении. По умолчанию True.
        """
    ```

- `handle_exception(self)`

    ```python
    def handle_exception(self) -> None:
        """
        Обрабатывает исключение, логируя ошибку и исходное исключение, если оно доступно.
        """
    ```

### `FileNotFoundError`

**Описание**: Исключение, возникающее, когда файл не найден.

### `ProductFieldException`

**Описание**: Исключение, возникающее при ошибках, связанных с полями продукта.

### `KeePassException`

**Описание**: Исключение, возникающее при проблемах с подключением к базе данных KeePass.

### `DefaultSettingsException`

**Описание**: Исключение, возникающее при проблемах с настройками по умолчанию.

### `WebDriverException`

**Описание**: Исключение, возникающее при проблемах, связанных с WebDriver.

### `ExecuteLocatorException`

**Описание**: Исключение, возникающее при ошибках, связанных с исполнителями локаторов.

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService.

**Как работает класс**: Этот класс используется для обработки ошибок, возникающих при взаимодействии с PrestaShop WebService.

**Методы**:

- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`

    ```python
    def __init__(self, msg: str, error_code: Optional[int] = None, 
                 ps_error_msg: str = '', ps_error_code: Optional[int] = None) -> None:
        """
        Инициализирует PrestaShopException с предоставленным сообщением и деталями ошибки.

        Args:
            msg (str): Пользовательское сообщение об ошибке.
            error_code (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию None.
            ps_error_msg (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию ''.
            ps_error_code (Optional[int], optional): Код ошибки PrestaShop. По умолчанию None.
        """
    ```

- `__str__(self)`

    ```python
    def __str__(self) -> str:
        """
        Возвращает строковое представление исключения.
        """
    ```

### `PrestaShopAuthenticationError`

**Описание**: Исключение, возникающее при ошибках аутентификации PrestaShop (Unauthorized).