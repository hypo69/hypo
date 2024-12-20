# Модуль `hypotez/src/scenario/__init__.py`

## Обзор

Этот модуль предоставляет функции для выполнения сценариев, предназначенные для работы с поставщиками (например, AliExpress).  Он содержит функции для работы как с отдельными файлами сценариев, так и с наборами сценариев. Поддерживается выполнение сценариев, представленных как словарями, так и списками словарей.

## Функции

### `run_scenario_files`

**Описание**: Функция для выполнения сценариев, загруженных из списка файлов.

**Параметры**:
- `supplier` (объект `Supplier`): Объект, представляющий поставщика.
- `scenario_files` (list[str]): Список путей к файлам сценариев.

**Возвращает**:
- `None`: Функция не возвращает значение.

**Вызывает исключения**:
- `FileNotFoundError`: Если один или несколько файлов сценариев не найдены.
- `ValueError`: Если входной параметр `scenario_files` не является списком строк.
- `TypeError`: Если переданный объект `supplier` не является объектом типа `Supplier`.


### `run_scenarios`

**Описание**: Функция для выполнения сценариев, переданных в виде списка словарей.

**Параметры**:
- `supplier` (объект `Supplier`): Объект, представляющий поставщика.
- `scenarios` (list[dict] or dict): Список словарей или один словарь, представляющий сценарии.

**Возвращает**:
- `None`: Функция не возвращает значение.

**Вызывает исключения**:
- `TypeError`: Если переданный объект `scenarios` не является списком словарей или словарем.
- `TypeError`: Если переданный объект `supplier` не является объектом типа `Supplier`.


### `run_scenario_file`

**Описание**: Функция для выполнения сценария из одного файла.

**Параметры**:
- `supplier` (объект `Supplier`): Объект, представляющий поставщика.
- `scenario_file` (str): Путь к файлу сценария.


**Возвращает**:
- `None`: Функция не возвращает значение.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл сценария не найден.
- `TypeError`: Если переданный объект `supplier` не является объектом типа `Supplier`.
- `ValueError`: Если входной параметр `scenario_file` не является строкой.


### `run_scenario`

**Описание**: Функция для выполнения одного сценария (внутренняя функция).

**Параметры**:
- `supplier` (объект `Supplier`): Объект, представляющий поставщика.
- `scenario` (dict): Словарь, представляющий сценарий.

**Возвращает**:
- `None`: Функция не возвращает значение.

**Вызывает исключения**:
- `TypeError`:  Если переданный сценарий `scenario` не является словарем.
- `TypeError`: Если переданный объект `supplier` не является объектом типа `Supplier`.
- Другие исключения, которые могут быть подняты функциями, которые вызываются внутри `run_scenario`.



### `execute_PrestaShop_insert`

**Описание**: Функция для выполнения запросов вставки данных в PrestaShop.

**Параметры**:
- (не указаны - подразумевается, что функция принимает данные для вставки): параметры, необходимые для запроса вставки.

**Возвращает**:
- (не указаны - подразумевается, что функция возвращает данные о результате): результат выполнения запроса.

**Вызывает исключения**:
- `PrestaShopError`: Возникает при проблемах с подключением к базе данных PrestaShop, выполнением запроса или при других проблемах, связанных с PrestaShop.



### `execute_PrestaShop_insert_async`

**Описание**: Функция для асинхронного выполнения запросов вставки данных в PrestaShop.

**Параметры**:
- (не указаны - подразумевается, что функция принимает данные для вставки): параметры, необходимые для запроса вставки.

**Возвращает**:
- (не указаны - подразумевается, что функция возвращает данные о результате): результат выполнения асинхронного запроса.

**Вызывает исключения**:
- `PrestaShopError`: Возникает при проблемах с подключением к базе данных PrestaShop, выполнением запроса или при других проблемах, связанных с PrestaShop.


## Модульные переменные

### `MODE`

**Описание**:  Переменная, которая содержит режим работы модуля. В данном случае,  `'dev'` .


## Примеры (в коде examples):

Пример использования функций для работы со сценариями и файлами сценариев.
```
```
```
```


```
```
```


```
```


```