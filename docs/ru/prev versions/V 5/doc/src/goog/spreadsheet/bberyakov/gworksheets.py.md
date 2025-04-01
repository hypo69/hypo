# Модуль gworksheets

## Обзор

Модуль `gworksheets.py` предназначен для работы с Google Sheets, предоставляя функциональность для создания, открытия и управления листами (worksheets) в Google Spreadsheets. Он включает класс `GWorksheet`, который расширяет базовый класс `Worksheet` и предоставляет методы для настройки заголовков, категорий и направления текста листов.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для упрощения взаимодействия с Google Sheets. Он использует классы `Spreadsheet` и `Worksheet` из модуля `global_settingspread`, а также класс `GSRender` из модуля `goog.grender` для рендеринга данных в Google Sheets. Модуль позволяет создавать новые листы, открывать существующие, очищать данные на листах, а также устанавливать направление текста.

## Классы

### `GWorksheet`

**Описание**: Класс `GWorksheet` предназначен для работы с отдельными листами в Google Sheets. Он предоставляет методы для управления листом, такие как установка заголовка, категории и направления текста.

**Как работает класс**:
Класс `GWorksheet` инициализируется с использованием объекта `sh` (предположительно, представляющего Google Spreadsheet) и названия листа `ws_title`. В конструкторе вызывается метод `get`, который либо создает новый лист, либо открывает существующий. Класс также использует объект `GSRender` для выполнения операций рендеринга, таких как установка направления текста и запись заголовков.

**Методы**:
- `__init__`: Инициализирует объект `GWorksheet`, получая существующий лист или создавая новый.
- `get`: Получает или создает лист в Google Sheets.
- `header`: Устанавливает заголовок для листа.
- `category`: Устанавливает категорию для листа.
- `direction`: Устанавливает направление текста для листа.

**Параметры**:
- `sh`: Объект, представляющий Google Spreadsheet.
- `ws`: Объект, представляющий Google Worksheet.
- `render`: Объект `GSRender`, используемый для рендеринга данных.

**Примеры**:

```python
# Пример создания объекта GWorksheet
# gws = GWorksheet(sh, ws_title='MySheet')
```

## Функции

### `__init__`

```python
def __init__(self, sh, ws_title: str = 'new', rows = None, cols = None, direcion = 'rtl', wipe_if_exist: bool = True, *args, **kwards) -> None:
    """
    Args:
        sh: Описание параметра `sh`.
        ws_title (str, optional): Описание параметра `ws_title`. По умолчанию 'new'.
        rows: Описание параметра `rows`.
        cols: Описание параметра `cols`.
        direcion (str, optional): Описание параметра `direcion`. По умолчанию 'rtl'.
        wipe_if_exist (bool, optional): Описание параметра `wipe_if_exist`. По умолчанию `True`.
        *args: Описание параметра `*args`.
        **kwards: Описание параметра `**kwards`.

    Returns:
        None: Описание возвращаемого значения.

    """
    self.sh = sh
    self.get(self.sh, ws_title)
    ...
```

**Как работает функция**:
Конструктор класса `GWorksheet`. Принимает объект `sh` (вероятно, Spreadsheet), название листа `ws_title`, количество строк, количество колонок, направление текста и флаг очистки данных. Вызывает метод `get` для получения или создания листа.

**Параметры**:
- `sh`: Объект, представляющий Google Spreadsheet.
- `ws_title` (str, optional): Название листа. По умолчанию 'new'.
- `rows`: Количество строк в листе (если создается новый лист).
- `cols`: Количество колонок в листе (если создается новый лист).
- `direcion` (str, optional): Направление текста. По умолчанию 'rtl'.
- `wipe_if_exist` (bool, optional): Флаг, указывающий, нужно ли очищать лист, если он уже существует. По умолчанию `True`.
- `*args`: Дополнительные аргументы.
- `**kwards`: Дополнительные именованные аргументы.

**Возвращает**:
- `None`

**Примеры**:

```python
# Пример создания объекта GWorksheet
# gws = GWorksheet(sh, ws_title='MySheet', rows=100, cols=10)
```

### `get`

```python
def get (self, sh, ws_title: str = 'new', rows: int = 100, cols: int = 100, direction: str = 'rtl', wipe_if_exist: bool = True) :
    """
    Args:
        self: Описание параметра `self`.
        sh: Описание параметра `sh`.
        ws_title (str, optional): Описание параметра `ws_title`. По умолчанию 'new'.
        rows (int, optional): Описание параметра `rows`. По умолчанию 100.
        cols (int, optional): Описание параметра `cols`. По умолчанию 100.
        direction (str, optional): Описание параметра `direction`. По умолчанию 'rtl'.
        wipe_if_exist (bool, optional): Описание параметра `wipe_if_exist`. По умолчанию `True`.

    """
    """
    Создаю новую таблицу в книге, если ws_title == 'new', \n
    иначе открываю по ws_title \n

    `ws_title` (str) - Название таблицы(worksheet) в книге(spreadsheet) \n

    `rows` (int) - кол -во строк \n

    `cols` (int) - кол -во колонок \n

    `wipe_if_exist` (bool) - очистить от старых данных
    """
    
    if ws_title == 'new':
        #_ws = sh.add_worksheet()
        self.ws = sh.gsh.get()
        
    else:
        
        if ws_title in [_ws.title for _ws in sh.gsh.worksheets() ]:
            print (f'worksheet {ws_title} already exist !')
            #_ws = sh.worksheet(ws_title)
            self.ws = sh.gsh.worksheet(ws_title)

            if wipe_if_exist: 
                """ wipe data on worksheet  """
                #_ws.clear()
                #self.gsh.clear()
                self.ws.clear()
        
        else:
            #_ws = sh.add_worksheet (ws_title, rows, cols )
            self.ws = sh.gsh.add_worksheet (ws_title, rows, cols )
            """ new worksheet with ws_title """

    self.render.set_worksheet_direction (sh.gsh, self.ws, 'rtl')
```

**Как работает функция**:
Метод `get` получает или создает лист в Google Sheets. Если `ws_title` равно 'new', то создается новый лист. Иначе, метод пытается открыть существующий лист с указанным именем. Если лист существует и `wipe_if_exist` равно `True`, то лист очищается. Если лист не существует, то создается новый лист с указанным именем, количеством строк и колонок. В конце устанавливается направление текста для листа.

**Параметры**:
- `sh`: Объект, представляющий Google Spreadsheet.
- `ws_title` (str, optional): Название листа. По умолчанию 'new'.
- `rows` (int, optional): Количество строк в листе (если создается новый лист). По умолчанию 100.
- `cols` (int, optional): Количество колонок в листе (если создается новый лист). По умолчанию 100.
- `direction` (str, optional): Направление текста. По умолчанию 'rtl'.
- `wipe_if_exist` (bool, optional): Флаг, указывающий, нужно ли очищать лист, если он уже существует. По умолчанию `True`.

**Примеры**:

```python
# Пример получения существующего листа
# gws.get(sh, ws_title='MySheet')

# Пример создания нового листа
# gws.get(sh, ws_title='NewSheet', rows=200, cols=20)
```

### `header`

```python
def header(self, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None:
    """
    Args:
        self: Описание параметра `self`.
        world_title (str): Описание параметра `world_title`.
        range (str, optional): Описание параметра `range`. По умолчанию 'A1:Z1'.
        merge_type (str, optional): Описание параметра `merge_type`. По умолчанию 'MERGE_ALL'.

    Returns:
        None: Описание возвращаемого значения.

    """
    self.render.header(self.ws, world_title)
```

**Как работает функция**:
Метод `header` устанавливает заголовок для листа. Он вызывает метод `header` объекта `GSRender` для выполнения фактической установки заголовка.

**Параметры**:
- `world_title` (str): Текст заголовка.
- `range` (str, optional): Диапазон ячеек, в котором будет размещен заголовок. По умолчанию 'A1:Z1'.
- `merge_type` (str, optional): Тип объединения ячеек для заголовка. Может быть 'MERGE_ALL', 'MERGE_COLUMNS' или 'MERGE_ROWS'. По умолчанию 'MERGE_ALL'.

**Возвращает**:
- `None`

**Примеры**:

```python
# Пример установки заголовка
# gws.header(world_title='My Sheet Title', range='A1:C1', merge_type='MERGE_COLUMNS')
```

### `category`

```python
def category(self, ws_category_title):
    """
    Args:
        self: Описание параметра `self`.
        ws_category_title: Описание параметра `ws_category_title`.

    """
    self.render.write_category_title(self, ws_category_title)
```

**Как работает функция**:
Метод `category` устанавливает категорию для листа. Он вызывает метод `write_category_title` объекта `GSRender` для записи заголовка категории.

**Параметры**:
- `ws_category_title`: Текст заголовка категории.

**Примеры**:

```python
# Пример установки категории
# gws.category(ws_category_title='My Category')
```

### `direction`

```python
def direction(self, direction: str = 'rtl'):
    """
    Args:
        self: Описание параметра `self`.
        direction (str, optional): Описание параметра `direction`. По умолчанию 'rtl'.

    """
    self.render.set_worksheet_direction(sh = self.sh, ws = self, direction = 'rtl')
```

**Как работает функция**:
Метод `direction` устанавливает направление текста для листа. Он вызывает метод `set_worksheet_direction` объекта `GSRender` для установки направления.

**Параметры**:
- `direction` (str, optional): Направление текста. По умолчанию 'rtl' (Right-to-Left).

**Примеры**:

```python
# Пример установки направления текста
# gws.direction(direction='ltr')  # Left-to-Right
```