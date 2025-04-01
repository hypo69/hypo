# Модуль `src.logger.exceptions`

## Обзор

Модуль `src.logger.exceptions` определяет пользовательские исключения, используемые в приложении. Он содержит набор классов исключений для обработки ошибок, связанных с различными компонентами приложения, такими как файловые операции, поля продукта, соединения с базой данных KeePass и ошибки PrestaShop WebService.

## Подробней

Этот модуль предоставляет специализированные классы исключений, которые позволяют более точно обрабатывать ошибки в различных частях приложения. Использование этих исключений помогает улучшить читаемость кода, облегчает отладку и позволяет более эффективно обрабатывать ошибки.

## Классы

### `CustomException`

**Описание**: Базовый класс для всех пользовательских исключений в приложении.

**Как работает класс**:
Этот класс является базовым для всех пользовательских исключений и предназначен для обработки логирования исключений. Он принимает сообщение об ошибке и оригинальное исключение (если оно есть), а также флаг, указывающий, следует ли логировать информацию об исключении. Метод `handle_exception` записывает сообщение об ошибке и, если доступно, оригинальное исключение в лог.

**Методы**:
- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` с сообщением и необязательным оригинальным исключением.
- `handle_exception(self)`: Обрабатывает исключение, логируя ошибку и оригинальное исключение, если оно доступно.

**Параметры**:
- `message` (str): Сообщение об ошибке.
- `e` (Optional[Exception], optional): Оригинальное исключение, вызвавшее это исключение. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении. По умолчанию `True`.

**Примеры**:
```python
from src.logger.exceptions import CustomException
try:
    raise ValueError('Недопустимое значение')
except ValueError as ex:
    raise CustomException('Произошла ошибка значения', ex)
```

### `FileNotFoundError`

**Описание**: Исключение, которое вызывается, когда файл не найден.

**Как работает класс**:
Этот класс является подклассом `CustomException` и `IOError`. Он используется для обозначения ситуаций, когда файл, который требуется для работы приложения, не найден.

**Примеры**:
```python
from src.logger.exceptions import FileNotFoundError
try:
    with open('missing_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as ex:
    raise FileNotFoundError('Файл не найден', ex)
```

### `ProductFieldException`

**Описание**: Исключение, которое вызывается при ошибках, связанных с полями продукта.

**Как работает класс**:
Этот класс является подклассом `CustomException`. Он используется для обозначения ошибок, связанных с полями продукта, например, когда поле продукта имеет неверный формат или отсутствует.

**Примеры**:
```python
from src.logger.exceptions import ProductFieldException
try:
    product_data = {'name': 'Продукт', 'price': 'неверная цена'}
    if not isinstance(product_data['price'], float):
        raise ProductFieldException('Неверный формат цены продукта')
except ProductFieldException as ex:
    raise ProductFieldException('Ошибка в поле продукта', ex)
```

### `KeePassException`

**Описание**: Исключение, которое вызывается при ошибках, связанных с подключением к базе данных KeePass.

**Как работает класс**:
Этот класс является подклассом исключений, специфичных для библиотеки `pykeepass`, таких как `CredentialsError`, `BinaryError`, `HeaderChecksumError`, `PayloadChecksumError` и `UnableToSendToRecycleBin`. Он используется для обработки ошибок, возникающих при взаимодействии с базой данных KeePass, таких как неверные учетные данные, поврежденные файлы и другие проблемы.

**Примеры**:
```python
from src.logger.exceptions import KeePassException
from pykeepass import pykeepass
try:
    kp = pykeepass.PyKeePass('test.kdbx', password='wrong_password')
except KeePassException as ex:
    raise KeePassException('Ошибка подключения к KeePass', ex)
```

### `DefaultSettingsException`

**Описание**: Исключение, которое вызывается при проблемах с настройками по умолчанию.

**Как работает класс**:
Этот класс является подклассом `CustomException`. Он используется для обозначения ошибок, связанных с настройками по умолчанию приложения, например, когда файл настроек отсутствует или имеет неверный формат.

**Примеры**:
```python
from src.logger.exceptions import DefaultSettingsException
try:
    default_settings = {}
    if not default_settings:
        raise DefaultSettingsException('Отсутствуют настройки по умолчанию')
except DefaultSettingsException as ex:
    raise DefaultSettingsException('Ошибка в настройках по умолчанию', ex)
```

### `WebDriverException`

**Описание**: Исключение, которое вызывается при проблемах, связанных с WebDriver.

**Как работает класс**:
Этот класс является подклассом `WDriverException` из библиотеки `selenium`. Он используется для обработки ошибок, возникающих при использовании WebDriver для автоматизации браузера.

**Примеры**:
```python
from src.logger.exceptions import WebDriverException
from selenium import webdriver
try:
    driver = webdriver.Chrome()
    driver.get('http://example.com')
    driver.quit()
except WebDriverException as ex:
    raise WebDriverException('Ошибка WebDriver', ex)
```

### `ExecuteLocatorException`

**Описание**: Исключение, которое вызывается при ошибках, связанных с исполнителями локаторов.

**Как работает класс**:
Этот класс является подклассом `CustomException`. Он используется для обозначения ошибок, возникающих при выполнении локаторов элементов на веб-странице.

**Примеры**:
```python
from src.logger.exceptions import ExecuteLocatorException
try:
    locator = '//*[@id="nonexistent"]'
    # Попытка выполнить локатор, который не существует
    raise ExecuteLocatorException(f'Не удалось выполнить локатор: {locator}')
except ExecuteLocatorException as ex:
    raise ExecuteLocatorException('Ошибка при выполнении локатора', ex)
```

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService.

**Как работает класс**:
Этот класс используется для обработки ошибок, возникающих при взаимодействии с PrestaShop WebService.

**Атрибуты**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию `None`.
- `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию пустая строка.
- `ps_error_code` (Optional[int], optional): Код ошибки от PrestaShop. По умолчанию `None`.

**Методы**:
- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` с предоставленным сообщением и деталями ошибки.
- `__str__(self)`: Возвращает строковое представление исключения.

**Параметры**:
- `msg` (str): Сообщение об ошибке.
- `error_code` (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию `None`.
- `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию пустая строка.
- `ps_error_code` (Optional[int], optional): Код ошибки от PrestaShop. По умолчанию `None`.

**Примеры**:
```python
from src.logger.exceptions import PrestaShopException
try:
    raise PrestaShopException('Ошибка подключения к PrestaShop', ps_error_msg='Неверный URL')
except PrestaShopException as ex:
    raise PrestaShopException('Произошла ошибка PrestaShop', ex)
```

### `PrestaShopAuthenticationError`

**Описание**: Исключение, которое вызывается при ошибках аутентификации PrestaShop (Unauthorized).

**Как работает класс**:
Этот класс является подклассом `PrestaShopException`. Он используется для обозначения ошибок аутентификации при взаимодействии с PrestaShop WebService.

**Примеры**:
```python
from src.logger.exceptions import PrestaShopAuthenticationError
try:
    raise PrestaShopAuthenticationError('Ошибка аутентификации PrestaShop')
except PrestaShopAuthenticationError as ex:
    raise PrestaShopAuthenticationError('Ошибка аутентификации', ex)
```