# Модуль hypotez/src/utils/xls.py

## Обзор

Модуль `xls.py` предоставляет функции для конвертации файлов Excel (`xls`) в JSON и обратно. Он поддерживает чтение и запись нескольких листов в файле Excel. Модуль обрабатывает потенциальные ошибки, такие как отсутствие файла, ошибки чтения/записи и ошибки при работе с листами Excel, записывая информацию об ошибках в лог.


## Функции

### `read_xls_as_dict`

**Описание**: Читает файл Excel и преобразует его в JSON. Опционально, преобразует определенный лист и сохраняет результат в файл JSON. Обрабатывает ошибки.

**Параметры**:

- `xls_file` (str): Путь к файлу Excel.
- `json_file` (str, опционально): Путь к файлу JSON для сохранения результата. По умолчанию `None` (не сохраняется).
- `sheet_name` (Union[str, int], опционально): Имя листа, который нужно преобразовать. По умолчанию `None` (обрабатываются все листы).

**Возвращает**:

- `Union[Dict, List[Dict], bool]`:
    - Если успешно, возвращает словарь, где ключи — имена листов, а значения — списки словарей, представляющие строки данных. Если указан только `xls_file`, то возвращается словарь со всеми листами.
    - Если указан `sheet_name`, возвращает лист словарей, содержащий данные из указанного листа.
    - Возвращает `False`, если произошла ошибка (например, файл не найден).

**Вызывает исключения**:

- `FileNotFoundError`: Если файл Excel не найден.
- `Exception`: Любые другие исключения, произошедшие во время обработки файла.


### `save_xls_file`

**Описание**: Сохраняет данные JSON в файл Excel. Обрабатывает ошибки.

**Параметры**:

- `data` (Dict[str, List[Dict]]): Словарь, где ключи — имена листов, а значения — списки словарей, представляющие строки данных для каждого листа.
- `file_path` (str): Путь к файлу Excel для сохранения данных.

**Возвращает**:

- bool: `True`, если сохранение прошло успешно. `False`, если произошла ошибка.

**Вызывает исключения**:

- `Exception`: Любые другие исключения, произошедшие во время сохранения в файл Excel.


## Примеры использования

```python
# Чтение файла Excel и сохранение данных в файл JSON (для листа "Sheet1")
data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
if data:
    print(data)  # Вывод данных в консоль.

# Сохранение данных из JSON в файл Excel
data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
success = save_xls_file(data_to_save, 'output.xlsx')
if success:
    print("Файл успешно сохранён в output.xlsx")
```


```python
# Чтение всех листов из файла Excel
data = read_xls_as_dict('input.xlsx')
if data:
    print(data) # Вывод всех листов.
```
```
```


## Логирование

Модуль использует `logging` для записи сообщений об ошибках и успешных операциях.  Уровень логирования по умолчанию — `INFO`.
```