# Модуль `driver`

## Обзор

Этот модуль предоставляет базовый класс `DriverBase` для работы с веб-драйверами, обеспечивая общие методы и атрибуты, применимые к различным типам веб-драйверов (например, Chrome, Firefox, Edge).  Он инкапсулирует низкоуровневые методы взаимодействия с браузером, а также предоставляет инструменты для управления страницами, выполнение JavaScript-кода и обработки исключений.

## Классы

### `DriverBase`

**Описание**: Базовый класс для веб-драйвера, содержащий общие атрибуты и методы для всех реализаций.

**Атрибуты**:

- `previous_url` (str): URL предыдущей страницы.
- `referrer` (str): Ссылка реферера.
- `page_lang` (str): Язык страницы.
- `ready_state` (bool): Флаг готовности страницы.
- `driver_payload` (dict): Словарь с параметрами, необходимыми для драйвера.
- `js` (`JavaScript`): Объект для выполнения JavaScript-кода.
- `exec_loc` (`ExecuteLocator`): Объект для поиска элементов на странице.


**Методы**:

#### `driver_payload()`

**Описание**: Инициализирует необходимые объекты для работы с JavaScript-кодом и локатором элементов.

**Возвращает**:
- `dict`: Словарь с параметрами, необходимыми для драйвера.

#### `scroll(scrolls: int = 1, frame_size: int = 250, direction: str = 'forward', delay: float = 0.1)`

**Описание**: Прокручивает страницу в заданном направлении.

**Параметры**:
- `scrolls` (int): Количество прокруток.
- `frame_size` (int): Размер прокрутки (пиксели).
- `direction` (str): Направление прокрутки ('forward' или 'backward').
- `delay` (float): Задержка между прокрутками (секунды).

**Возвращает**:
- `None`

#### `locale()`

**Описание**: Определяет язык текущей страницы.

**Возвращает**:
- `str`: Язык страницы.


#### `get_url(url: str)`

**Описание**: Переходит по указанному URL и проверяет успешность перехода.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если переход успешен, иначе `False`.


#### `extract_domain(url: str)`

**Описание**: Извлекает доменное имя из URL.

**Параметры**:
- `url` (str): URL.

**Возвращает**:
- `str`: Доменное имя.

#### `_save_cookies_localy(to_file: Union[str, Path])`

**Описание**: Сохраняет куки в файл.

**Параметры**:
- `to_file` (Union[str, Path]): Путь к файлу для сохранения куки.


#### `page_refresh()`

**Описание**: Обновляет текущую страницу.

**Возвращает**:
- `None`


#### `window_focus()`

**Описание**: Восстанавливает фокус на текущем окне.

**Возвращает**:
- `None`

#### `wait(interval: float)`

**Описание**: Делает паузу на указанное время.

**Параметры**:
- `interval` (float): Время паузы в секундах.

**Возвращает**:
- `None`

#### `delete_driver_logs()`

**Описание**: Удаляет временные файлы и логи WebDriver.

**Возвращает**:
- `None`

### `DriverMeta`

**Описание**: Метакласс для динамического создания классов веб-драйверов.

**Методы**:

#### `__call__(cls, webdriver_cls: Type, *args, **kwargs)`

**Описание**: Создает новый класс `Driver`, унаследованный от `DriverBase` и указанного класса веб-драйвера.

**Параметры**:
- `webdriver_cls` (Type): Класс веб-драйвера.
- `*args`: Аргументы для конструктора класса веб-драйвера.
- `**kwargs`: Ключевые аргументы для конструктора класса веб-драйвера.

**Возвращает**:
- `Driver`: Новый класс веб-драйвера.


### `Driver`

**Описание**: Динамически созданный класс веб-драйвера, наследующий функциональность `DriverBase` и конкретного класса веб-драйвера (например, `Chrome`, `Firefox`).

**Использование**:

```python
from src.webdriver.driver import Driver, Chrome
driver = Driver(Chrome)
```


## Функции

(Список функций, если они есть, будет заполнен здесь)

## Обработка исключений

(Список обработанных исключений, если они есть, будет заполнен здесь)


## Зависимости

- `selenium`
- `urllib.parse`
- `copy`
- `time`
- `pickle`
- `pathlib`
- `typing`
- и другие модули, перечисленные в начале кода.


## Дополнительные заметки

(Дополнительные заметки, если необходимо)