# Модуль `src.logger.exceptions`

## Обзор

Модуль `src.logger.exceptions` содержит определения пользовательских исключений, используемых в приложении. Эти исключения предназначены для обработки ошибок, связанных с различными компонентами приложения, такими как файловые операции, поля продуктов, соединения с базами данных KeePass и ошибки веб-служб PrestaShop.

## Подробней

Модуль предоставляет набор классов исключений, которые наследуются от базового класса `CustomException` или стандартных исключений Python. Это позволяет единообразно обрабатывать ошибки и регистрировать их в системе логирования. Использование пользовательских исключений делает код более читаемым и упрощает отладку.

## Классы

### `CustomException`

**Описание**: Базовый класс для всех пользовательских исключений в приложении. Обеспечивает логирование исключений и обработку исходных исключений, если они есть.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `CustomException`.
- `handle_exception`: Обрабатывает исключение, логируя ошибку и исходное исключение (если доступно).

**Параметры**:
- `message` (str): Сообщение об ошибке.
- `e` (Optional[Exception], optional): Исходное исключение, вызвавшее данное исключение. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, следует ли логировать информацию об исключении. По умолчанию `True`.

**Примеры**
```python
try:
    raise ValueError('Неверное значение')
except ValueError as ex:
    custom_exception = CustomException('Произошла ошибка значения', ex)
```

### `FileNotFoundError`

**Описание**: Исключение, которое вызывается, когда файл не найден.

**Примеры**
```python
try:
    with open('missing_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as ex:
    print(f'Файл не найден: {ex}')
```

### `ProductFieldException`

**Описание**: Исключение, которое вызывается при ошибках, связанных с полями продуктов.

**Примеры**
```python
try:
    raise ProductFieldException('Неверное поле продукта')
except ProductFieldException as ex:
    print(f'Ошибка поля продукта: {ex}')
```

### `KeePassException`

**Описание**: Исключение, которое вызывается при проблемах с соединением к базе данных KeePass.

**Примеры**
```python
try:
    raise KeePassException('Ошибка базы данных KeePass')
except KeePassException as ex:
    print(f'Ошибка KeePass: {ex}')
```

### `DefaultSettingsException`

**Описание**: Исключение, которое вызывается при проблемах с настройками по умолчанию.

**Примеры**
```python
try:
    raise DefaultSettingsException('Ошибка настроек по умолчанию')
except DefaultSettingsException as ex:
    print(f'Ошибка настроек по умолчанию: {ex}')
```

### `WebDriverException`

**Описание**: Исключение, которое вызывается при проблемах, связанных с WebDriver.

**Примеры**
```python
try:
    raise WebDriverException('Ошибка WebDriver')
except WebDriverException as ex:
    print(f'Ошибка WebDriver: {ex}')
```

### `ExecuteLocatorException`

**Описание**: Исключение, которое вызывается при ошибках, связанных с исполнителями локаторов.

**Примеры**
```python
try:
    raise ExecuteLocatorException('Ошибка исполнителя локатора')
except ExecuteLocatorException as ex:
    print(f'Ошибка исполнителя локатора: {ex}')
```

### `PrestaShopException`

**Описание**: Общее исключение для ошибок веб-службы PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaShopException`.
- `__str__`: Возвращает строковое представление исключения.

**Параметры**:
- `msg` (str): Пользовательское сообщение об ошибке.
- `error_code` (Optional[int], optional): Код ошибки, возвращенный PrestaShop. По умолчанию `None`.
- `ps_error_msg` (str, optional): Сообщение об ошибке от PrestaShop. По умолчанию ''.
- `ps_error_code` (Optional[int], optional): Код ошибки PrestaShop. По умолчанию `None`.

**Примеры**
```python
try:
    raise PrestaShopException('Ошибка PrestaShop', ps_error_msg='Неверный формат данных')
except PrestaShopException as ex:
    print(f'Ошибка PrestaShop: {ex}')
```

### `PrestaShopAuthenticationError`

**Описание**: Исключение, которое вызывается при ошибках аутентификации PrestaShop (неавторизованный доступ).

**Примеры**
```python
try:
    raise PrestaShopAuthenticationError('Ошибка аутентификации PrestaShop')
except PrestaShopAuthenticationError as ex:
    print(f'Ошибка аутентификации PrestaShop: {ex}')
```