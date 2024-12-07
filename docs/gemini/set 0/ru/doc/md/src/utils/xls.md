# Модуль `hypotez/src/utils/xls.py`

## Обзор

Модуль `xls.py` предоставляет функции для конвертации файлов Excel (`xls`) в формат JSON и обратно. Поддерживается чтение/запись нескольких листов.

## Функции

### `read_xls_as_dict`

**Описание**: Читает файл Excel и преобразует его в формат JSON.  По желанию, конвертирует конкретный лист и сохраняет результат в файл JSON. Обрабатывает ошибки gracefully.

**Параметры**:

- `xls_file` (str): Путь к файлу Excel.
- `json_file` (str, опционально): Путь к файлу JSON для сохранения результата. По умолчанию `None` (не сохраняется).
- `sheet_name` (Union[str, int], опционально): Имя или индекс листа для обработки. По умолчанию `None` (обрабатываются все листы).


**Возвращает**:

- Union[Dict, List[Dict], bool]: Словарь, содержащий данные из Excel в формате {«Имя листа» : [строки]},  или список словарей, если обработан один лист, или `False` в случае ошибки.

**Обрабатывает исключения**:

- `FileNotFoundError`: Возникает, если файл Excel не найден.
- `Exception`: Возникает при любых других ошибках, таких как проблемы с чтением файла или преобразованием данных.


### `save_xls_file`

**Описание**: Сохраняет данные JSON в файл Excel. Данные должны быть словарем, где ключи — имена листов, а значения — списки словарей, представляющие строки. Обрабатывает ошибки gracefully.

**Параметры**:

- `data` (Dict[str, List[Dict]]): Данные в формате JSON для сохранения в Excel. Должен быть словарем {«Имя листа» : [строки]}.
- `file_path` (str): Путь к файлу Excel для сохранения.


**Возвращает**:

- bool: `True` в случае успешного сохранения, `False` в случае ошибки.

**Обрабатывает исключения**:

- `Exception`: Возникает при любых других ошибках, таких как проблемы с записью в файл Excel.


## Логирование

Модуль использует `logging` для записи сообщений об ошибках и успешном выполнении операций.  Уровень логирования настроен на `INFO` по умолчанию.


## Примеры использования

```python
# Чтение и сохранение в JSON (опционально)
data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
if data:
    print(data)  # Вывод: {'Sheet1': [{...}]}

# Сохранение из JSON данных
data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
success = save_xls_file(data_to_save, 'output.xlsx')
if success:
    print("Успешно сохранено в output.xlsx")
```
```
```
```
```