# Модуль `src.webdriver.driver`

## Обзор

Модуль `src.webdriver.driver` предназначен для работы с веб-драйверами Selenium. Основной целью класса `Driver` является предоставление унифицированного интерфейса для взаимодействия с веб-драйверами Selenium. Класс предлагает методы для инициализации драйвера, навигации, управления cookie, обработки исключений и других операций.

## Подробней

Этот модуль предоставляет класс `Driver`, который упрощает взаимодействие с веб-драйверами Selenium. Он включает в себя методы для навигации по страницам, управления cookie и обработки исключений, что делает его удобным инструментом для веб-скрейпинга и автоматизации тестирования.

## Классы

### `Driver`

**Описание**: Класс `Driver` предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами Selenium.

**Как работает класс**:
Класс `Driver` инициализируется с использованием класса веб-драйвера (например, `Chrome`, `Firefox`) и предоставляет методы для выполнения различных операций, таких как навигация по URL, управление cookie и обработка исключений. Он также включает механизмы для определения языка страницы и сохранения cookie.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Driver`.
- `__init_subclass__`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__`: Обеспечивает проксирование доступа к атрибутам драйвера.
- `scroll`: Прокручивает страницу в указанном направлении.
- `locale`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url`: Переходит по указанному URL и сохраняет текущие cookie.
- `window_open`: Открывает новое окно или вкладку в браузере.
- `wait`: Приостанавливает выполнение на указанное время.
- `_save_cookies_localy`: Сохраняет текущие cookie веб-драйвера в локальный файл.
- `fetch_html`: Получает HTML-контент из файла или веб-страницы.

### `Driver.__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    if not hasattr(webdriver_cls, 'get'):
        raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
    self.driver = webdriver_cls(*args, **kwargs)
```

**Описание**: Инициализирует экземпляр класса `Driver`.

**Как работает функция**:
Функция `__init__` принимает класс веб-драйвера (`webdriver_cls`) и аргументы для его инициализации. Проверяет, является ли переданный класс допустимым классом веб-драйвера, и создает экземпляр этого класса, сохраняя его в атрибуте `self.driver`.

**Параметры**:
- `webdriver_cls`: Класс веб-драйвера (например, `Chrome`, `Firefox`).
- `*args`: Позиционные аргументы для инициализации драйвера.
- `**kwargs`: Именованные аргументы для инициализации драйвера.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом веб-драйвера.

**Примеры**:
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

### `Driver.__init_subclass__`

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    super().__init_subclass__(**kwargs)
    if browser_name is None:
        raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
    cls.browser_name = browser_name
```

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Как работает функция**:
Функция `__init_subclass__` вызывается при создании подкласса `Driver`. Она проверяет, указано ли имя браузера (`browser_name`) в аргументах класса, и сохраняет его в атрибуте `browser_name` подкласса.

**Параметры**:
- `browser_name`: Имя браузера.
- `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если не указан аргумент `browser_name`.

**Примеры**:
```python
class MyDriver(Driver, browser_name='chrome'):
    pass
```

### `Driver.__getattr__`

```python
def __getattr__(self, item):
    return getattr(self.driver, item)
```

**Описание**: Обеспечивает проксирование доступа к атрибутам драйвера.

**Как работает функция**:
Функция `__getattr__` вызывается, когда происходит обращение к несуществующему атрибуту экземпляра класса `Driver`. Она перенаправляет запрос к атрибуту объекта `self.driver`, обеспечивая доступ к атрибутам и методам веб-драйвера.

**Параметры**:
- `item`: Имя атрибута.

**Примеры**:
```python
driver = Driver(Chrome)
current_url = driver.current_url  #  Обращение к атрибуту объекта driver
```

### `Driver.scroll`

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
        try:
            for _ in range(scrolls):
                self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                self.wait(delay)
            return True
        except Exception as ex:
            logger.error('Error while scrolling', exc_info=ex)
            return False

    try:
        if direction == 'forward' or direction == 'down':
            return carousel('', scrolls, frame_size, delay)
        elif direction == 'backward' or direction == 'up':
            return carousel('-', scrolls, frame_size, delay)
        elif direction == 'both':
            return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
    except Exception as ex:
        logger.error('Error in scroll function', ex)
        return False
```

**Описание**: Прокручивает страницу в указанном направлении.

**Как работает функция**:
Функция `scroll` прокручивает страницу в заданном направлении (`forward`, `backward` или `both`) на указанное количество прокруток (`scrolls`) с заданным размером фрейма (`frame_size`) и задержкой (`delay`). Она использует JavaScript для выполнения прокрутки и обрабатывает возможные исключения.

**Параметры**:
- `scrolls`: Количество прокруток. По умолчанию 1.
- `frame_size`: Размер прокрутки в пикселях. По умолчанию 600.
- `direction`: Направление прокрутки (`'both'`, `'down'`, `'up'`). По умолчанию `'both'`.
- `delay`: Задержка между прокрутками в секундах. По умолчанию `0.3`.

**Возвращает**:
- `bool`: `True`, если прокрутка выполнена успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при прокрутке страницы.

**Примеры**:
```python
driver = Driver(Chrome)
driver.get_url('https://example.com')
driver.scroll(scrolls=2, direction='down')
```

### `Driver.locale`

```python
@property
def locale(self) -> Optional[str]:
    try:
        meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
        return meta_language.get_attribute('content')
    except Exception as ex:
        logger.debug('Failed to determine site language from META', ex)
        try:
            return self.get_page_lang()
        except Exception as ex:
            logger.debug('Failed to determine site language from JavaScript', ex)
            return
```

**Описание**: Определяет язык страницы на основе мета-тегов или JavaScript.

**Как работает функция**:
Функция `locale` пытается определить язык страницы, анализируя мета-теги HTML или выполняя JavaScript-код. Если язык не удается определить, возвращается `None`.

**Возвращает**:
- `Optional[str]`: Языковой код, если он найден, иначе `None`.

**Примеры**:
```python
driver = Driver(Chrome)
driver.get_url('https://example.com')
language = driver.locale
if language:
    print(f'Page language: {language}')
```

### `Driver.get_url`

```python
def get_url(self, url: str) -> bool:
    try:
        _previous_url = copy.copy(self.current_url)
    except Exception as ex:
        logger.error("Error getting current URL", ex)
        return False
    
    try:
        self.driver.get(url)
        
        while self.ready_state != 'complete':
            """ Wait for the page to finish loading """

        if url != _previous_url:
            self.previous_url = _previous_url

        self._save_cookies_localy()
        return True
        
    except WebDriverException as ex:
        logger.error('WebDriverException', ex)
        return False

    except InvalidArgumentException as ex:
        logger.error(f"InvalidArgumentException {url}", ex)
        return False
    except Exception as ex:
        logger.error(f'Error navigating to URL: {url}\n', ex)
        return False
```

**Описание**: Переходит по указанному URL и сохраняет текущие cookie.

**Как работает функция**:
Функция `get_url` переходит по указанному URL, используя метод `driver.get(url)`. Она также сохраняет предыдущий URL и текущие cookie для последующего использования. Функция обрабатывает различные исключения, которые могут возникнуть в процессе навигации.

**Параметры**:
- `url`: URL для перехода.

**Возвращает**:
- `bool`: `True`, если навигация выполнена успешно, `False` в противном случае.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка, связанная с драйвером.
- `InvalidArgumentException`: Если URL имеет неверный формат.
- `Exception`: Если возникает любая другая ошибка при навигации.

**Примеры**:
```python
driver = Driver(Chrome)
success = driver.get_url('https://example.com')
if success:
    print('Navigation successful')
```

### `Driver.window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    self.execute_script('window.open();')
    self.switch_to.window(self.window_handles[-1])
    if url:
        self.get(url)
```

**Описание**: Открывает новое окно или вкладку в браузере.

**Как работает функция**:
Функция `window_open` открывает новое окно или вкладку в текущем браузере и переключается на него. Если указан URL, он загружается в новом окне или вкладке.

**Параметры**:
- `url`: URL для загрузки в новом окне или вкладке. По умолчанию `None`.

**Примеры**:
```python
driver = Driver(Chrome)
driver.window_open('https://example.com')  # Открывает новую вкладку и переходит на example.com
```

### `Driver.wait`

```python
def wait(self, delay: float = .3) -> None:
    time.sleep(delay)
```

**Описание**: Приостанавливает выполнение на указанное время.

**Как работает функция**:
Функция `wait` приостанавливает выполнение программы на заданное количество секунд, используя функцию `time.sleep()`.

**Параметры**:
- `delay`: Время задержки в секундах. По умолчанию `0.3`.

**Примеры**:
```python
driver = Driver(Chrome)
driver.wait(1)  #  Приостанавливает выполнение на 1 секунду
```

### `Driver._save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
    try:
        with open(gs.cookies_filepath, 'wb') as cookiesfile:
            pickle.dump(self.driver.get_cookies(), cookiesfile)
    except Exception as ex:
        logger.error('Error saving cookies:', ex)
```

**Описание**: Сохраняет текущие cookie веб-драйвера в локальный файл.

**Как работает функция**:
Функция `_save_cookies_localy` сохраняет текущие cookie веб-драйвера в локальный файл, используя модуль `pickle` для сериализации данных. Функция обрабатывает возможные исключения, которые могут возникнуть при сохранении cookie.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при сохранении cookie.

### `Driver.fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    if url.startswith('file://'):
        cleaned_url = url.replace('file://', '')
        match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
        if match:
            file_path = Path(match.group(0))
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        self.html_content = file.read()
                    return True
                except Exception as ex:
                    logger.error('Error reading file:', ex)
                    return False
            else:
                logger.error('Local file not found:', file_path)
                return False
        else:
            logger.error('Invalid file path:', cleaned_url)
            return False
    elif url.startswith('http://') or url.startswith('https://'):
        try:
            if self.get_url(url):
                self.html_content = self.page_source
                return True
        except Exception as ex:
            logger.error(f"Error fetching {url}:", ex)
            return False
    else:
        logger.error("Error: Unsupported protocol for URL:", url)
        return False
```

**Описание**: Получает HTML-контент из файла или веб-страницы.

**Как работает функция**:
Функция `fetch_html` получает HTML-контент из указанного URL. Если URL начинается с `'file://'`, функция пытается прочитать контент из локального файла. Если URL начинается с `'http://'` или `'https://'`, функция использует метод `get_url` для загрузки страницы и извлекает HTML-контент из `page_source`.

**Параметры**:
- `url`: URL файла или веб-страницы.

**Возвращает**:
- `Optional[bool]`: `True`, если контент успешно получен, `False` в случае ошибки, `None` для неподдерживаемого протокола.

**Примеры**:
```python
driver = Driver(Chrome)
success = driver.fetch_html('https://example.com')
if success:
    print(f'HTML content: {driver.html_content[:100]}...')
```
```md