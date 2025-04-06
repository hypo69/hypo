# Модуль `src.logger.exceptions`

## Обзор

Модуль определяет пользовательские исключения, используемые в приложении.
Он содержит классы исключений для обработки ошибок, связанных с различными компонентами приложения, такими как файловые операции, поля продуктов, соединения с базой данных KeePass и ошибки PrestaShop WebService.

## Подробней

Этот модуль предоставляет набор пользовательских исключений, которые позволяют более эффективно и организованно обрабатывать ошибки в приложении. Использование пользовательских исключений позволяет лучше структурировать код обработки ошибок и предоставляет более конкретную информацию об источниках и типах возникающих проблем.

## Классы

### `CustomException`

**Описание**: Базовый класс для всех пользовательских исключений в приложении.

**Принцип работы**:
`CustomException` является базовым классом для всех пользовательских исключений. Он обрабатывает логирование исключений и предоставляет механизм для работы с исходным исключением, если оно существует. При создании экземпляра `CustomException`, вызывается метод `handle_exception`, который записывает информацию об исключении в лог.

**Аттрибуты**:
- `original_exception` (Optional[Exception]): Исходное исключение, вызвавшее данное пользовательское исключение, если оно есть.
- `exc_info` (bool): Флаг, указывающий, следует ли логировать информацию об исключении.

**Методы**:
- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Инициализирует `CustomException` сообщением и необязательным исходным исключением.
- `handle_exception(self)`: Обрабатывает исключение, логируя ошибку и исходное исключение, если оно доступно.

### `FileNotFoundError`

**Описание**: Исключение, вызываемое, когда файл не найден.

**Наследует**:
- `CustomException`: Наследует функциональность базового класса исключений для логирования и обработки ошибок.
- `IOError`: Наследует функциональность для обработки ошибок ввода-вывода.

### `ProductFieldException`

**Описание**: Исключение, вызываемое при ошибках, связанных с полями продуктов.

**Наследует**:
- `CustomException`: Наследует функциональность базового класса исключений для логирования и обработки ошибок.

### `KeePassException`

**Описание**: Исключение, вызываемое при проблемах с подключением к базе данных KeePass.

**Наследует**:
- `CredentialsError`: Ошибка аутентификации при подключении к базе данных KeePass.
- `BinaryError`: Ошибка при работе с бинарными данными в базе данных KeePass.
- `HeaderChecksumError`: Ошибка контрольной суммы заголовка базы данных KeePass.
- `PayloadChecksumError`: Ошибка контрольной суммы полезной нагрузки базы данных KeePass.
- `UnableToSendToRecycleBin`: Ошибка при попытке перемещения файла базы данных KeePass в корзину.

### `DefaultSettingsException`

**Описание**: Исключение, вызываемое при проблемах с настройками по умолчанию.

**Наследует**:
- `CustomException`: Наследует функциональность базового класса исключений для логирования и обработки ошибок.

### `WebDriverException`

**Описание**: Исключение, вызываемое при проблемах, связанных с WebDriver.

**Наследует**:
- `WDriverException`: Наследует функциональность исключения `WebDriverException` из библиотеки `selenium`.

### `ExecuteLocatorException`

**Описание**: Исключение, вызываемое при ошибках, связанных с исполнителями локаторов.

**Наследует**:
- `CustomException`: Наследует функциональность базового класса исключений для логирования и обработки ошибок.

### `PrestaShopException`

**Описание**: Общее исключение для ошибок PrestaShop WebService.

**Принцип работы**:
Этот класс используется для обработки ошибок, возникающих при взаимодействии с PrestaShop WebService.

**Аттрибуты**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int]): Код ошибки, возвращенный PrestaShop.
- `ps_error_msg` (str): Сообщение об ошибке от PrestaShop.
- `ps_error_code` (Optional[int]): Код ошибки PrestaShop.

**Методы**:
- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Инициализирует `PrestaShopException` предоставленным сообщением и деталями ошибки.
- `__str__(self)`: Возвращает строковое представление исключения.

### `PrestaShopAuthenticationError`

**Описание**: Исключение, вызываемое при ошибках аутентификации PrestaShop (Unauthorized).

**Наследует**:
- `PrestaShopException`: Наследует функциональность базового класса исключений для PrestaShop.

## Функции

### `CustomException.__init__`

```python
def __init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True) -> None
```

**Назначение**: Инициализирует экземпляр класса `CustomException`.

**Параметры**:
- `message` (str): Сообщение об ошибке, которое будет содержаться в исключении.
- `e` (Optional[Exception], optional): Исходное исключение, которое вызвало данное исключение. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в логи. По умолчанию `True`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:

1.  Вызывает конструктор базового класса `Exception` с переданным сообщением об ошибке.
2.  Сохраняет исходное исключение `e` в атрибуте `original_exception`.
3.  Сохраняет значение флага `exc_info` в атрибуте `exc_info`.
4.  Вызывает метод `handle_exception` для обработки исключения.

```
Инициализация
↓
Сохранение сообщения → Сохранение исходного исключения → Сохранение флага exc_info
↓
Вызов handle_exception
```

**Примеры**:

```python
from src.logger.exceptions import CustomException

try:
    raise ValueError("Пример ошибки")
except ValueError as ex:
    try:
        raise CustomException("Пользовательское исключение", ex)
    except CustomException as custom_ex:
        print(custom_ex)
```

### `CustomException.handle_exception`

```python
def handle_exception(self) -> None
```

**Назначение**: Обрабатывает исключение, логируя информацию об ошибке.

**Параметры**:
- `self`: Ссылка на экземпляр класса `CustomException`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:

1.  Логирует сообщение об ошибке, используя `logger.error`.
2.  Если присутствует исходное исключение (`self.original_exception`), логирует информацию об исходном исключении, используя `logger.debug`.

```
Логирование сообщения об ошибке
↓
Проверка наличия исходного исключения
↓
Логирование исходного исключения (если есть)
```

**Примеры**:

```python
from src.logger.exceptions import CustomException
from src.logger.logger import logger

try:
    raise ValueError("Пример ошибки")
except ValueError as ex:
    try:
        raise CustomException("Пользовательское исключение", ex)
    except CustomException as custom_ex:
        pass  # Обработка исключения уже выполнена в __init__
```

### `PrestaShopException.__init__`

```python
def __init__(self, msg: str, error_code: Optional[int] = None, 
                 ps_error_msg: str = '', ps_error_code: Optional[int] = None) -> None
```

**Назначение**: Инициализирует экземпляр класса `PrestaShopException`.

**Параметры**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию `None`.
- `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию ''.
- `ps_error_code` (Optional[int], optional): Код ошибки PrestaShop. По умолчанию `None`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:

1.  Сохраняет пользовательское сообщение об ошибке `msg` в атрибуте `self.msg`.
2.  Сохраняет код ошибки `error_code` в атрибуте `self.error_code`.
3.  Сохраняет сообщение об ошибке от PrestaShop `ps_error_msg` в атрибуте `self.ps_error_msg`.
4.  Сохраняет код ошибки PrestaShop `ps_error_code` в атрибуте `self.ps_error_code`.

```
Инициализация
↓
Сохранение пользовательского сообщения → Сохранение кода ошибки → Сохранение сообщения об ошибке PrestaShop → Сохранение кода ошибки PrestaShop
```

**Примеры**:

```python
from src.logger.exceptions import PrestaShopException

try:
    raise PrestaShopException("Ошибка при работе с PrestaShop", ps_error_msg="Неверный формат данных")
except PrestaShopException as ex:
    print(ex)
```

### `PrestaShopException.__str__`

```python
def __str__(self) -> str
```

**Назначение**: Возвращает строковое представление исключения.

**Параметры**:
- `self`: Ссылка на экземпляр класса `PrestaShopException`.

**Возвращает**:
- `str`: Строковое представление исключения.

**Как работает функция**:

1.  Если `self.ps_error_msg` не пустая строка, возвращает `self.ps_error_msg`.
2.  В противном случае возвращает `self.msg`.

```
Проверка ps_error_msg
↓
Возврат ps_error_msg (если не пустая строка) / возврат msg
```

**Примеры**:

```python
from src.logger.exceptions import PrestaShopException

try:
    raise PrestaShopException("Ошибка при работе с PrestaShop", ps_error_msg="Неверный формат данных")
except PrestaShopException as ex:
    print(str(ex))