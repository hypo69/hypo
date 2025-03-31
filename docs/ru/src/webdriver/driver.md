# Модуль `driver.py`

## Обзор

Модуль `driver.py` предназначен для работы с веб-драйверами Selenium. Основная цель класса `Driver` - предоставить унифицированный интерфейс для взаимодействия с веб-драйверами Selenium. Класс предлагает методы для инициализации драйвера, навигации, управления куки, обработки исключений и других операций.

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
  - [`Driver`](#driver)
    - [`__init__`](#__init__)
    - [`__init_subclass__`](#__init_subclass__)
    - [`__getattr__`](#__getattr__)
    - [`scroll`](#scroll)
    - [`locale`](#locale)
    - [`get_url`](#get_url)
    - [`window_open`](#window_open)
    - [`wait`](#wait)
    - [`_save_cookies_localy`](#_save_cookies_localy)
    - [`fetch_html`](#fetch_html)

## Подробнее

Модуль `driver.py` предоставляет класс `Driver`, который упрощает работу с веб-драйверами Selenium. Он включает в себя методы для инициализации драйвера, навигации по веб-страницам, управления куки и обработки исключений. Этот класс полезен для веб-скрапинга и автоматизации тестирования.

## Классы

### `Driver`

**Описание**:
Класс `Driver` предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами Selenium. Он включает методы для инициализации драйвера, навигации, управления куки и обработки исключений.

**Как работает класс**:
1.  **Инициализация**: При создании экземпляра класса `Driver` происходит инициализация веб-драйвера Selenium, переданного в качестве аргумента `webdriver_cls`.
2.  **Навигация**: Класс предоставляет методы для навигации по URL-адресам, прокрутки страниц и извлечения содержимого.
3.  **Управление куки**: Класс позволяет сохранять и управлять куки.
4.  **Обработка исключений**: Класс включает механизмы для логирования ошибок и обработки исключений, возникающих в процессе работы с веб-драйвером.
5. **Проксирование атрибутов**: Класс позволяет получать доступ к атрибутам экземпляра веб-драйвера напрямую через экземпляр класса `Driver` с помощью метода `__getattr__`.

#### `__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    if not hasattr(webdriver_cls, 'get'):
        raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
    self.driver = webdriver_cls(*args, **kwargs)
```

**Назначение**:
Инициализирует экземпляр класса `Driver` с использованием указанного класса веб-драйвера Selenium.

**Как работает функция**:
1. Проверяет, является ли переданный класс `webdriver_cls` допустимым классом веб-драйвера, проверяя наличие атрибута `get`. Если атрибут отсутствует, выбрасывается исключение `TypeError`.
2. Инициализирует веб-драйвер, создавая экземпляр класса `webdriver_cls` с переданными аргументами `*args` и `**kwargs`, и сохраняет его в атрибуте `self.driver`.

**Параметры**:

*   `webdriver_cls`: Класс веб-драйвера (например, Chrome, Firefox).
*   `*args`: Позиционные аргументы для инициализации драйвера.
*   `**kwargs`: Именованные аргументы для инициализации драйвера.

**Вызывает исключения**:

*   `TypeError`: Если `webdriver_cls` не является допустимым классом веб-драйвера.

#### `__init_subclass__`

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    super().__init_subclass__(**kwargs)
    if browser_name is None:
        raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
    cls.browser_name = browser_name
```

**Назначение**:
Автоматически вызывается при создании подкласса `Driver`.

**Как работает функция**:
1. Вызывает метод `__init_subclass__` родительского класса `Driver` с переданными аргументами `**kwargs`.
2. Проверяет, был ли указан аргумент `browser_name`. Если аргумент отсутствует, выбрасывается исключение `ValueError`.
3. Устанавливает атрибут класса `browser_name` равным переданному значению `browser_name`.

**Параметры**:

*   `browser_name`: Название браузера.
*   `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:

*   `ValueError`: Если не указан аргумент `browser_name`.

#### `__getattr__`

```python
def __getattr__(self, item):
    return getattr(self.driver, item)
```

**Назначение**:
Обеспечивает проксирование доступа к атрибутам драйвера.

**Как работает функция**:
1. Пытается получить атрибут `item` из объекта `self.driver` с помощью функции `getattr()`.
2. Возвращает значение полученного атрибута.

**Параметры**:

*   `item`: Имя атрибута.

#### `scroll`

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

**Назначение**:
Прокручивает страницу в указанном направлении.

**Как работает функция**:

1.  Определяет внутреннюю функцию `carousel`, которая выполняет прокрутку страницы на заданное количество "кадров" (`scrolls`) в определенном направлении (`direction`). Размер каждого "кадра" задается параметром `frame_size`, а задержка между прокрутками - параметром `delay`.
2.  В зависимости от значения параметра `direction` (которое может быть `forward`, `down`, `backward`, `up` или `both`), функция вызывает `carousel` с соответствующим знаком (`-` для обратного направления) или без него.
3.  Если `direction` равно `both`, функция вызывает `carousel` дважды: один раз для прокрутки вниз, а затем один раз для прокрутки вверх.
4.  В случае возникновения ошибки в процессе прокрутки, функция логирует ошибку и возвращает `False`.

**Параметры**:

*   `scrolls` (int): Количество прокруток. По умолчанию 1.
*   `frame_size` (int): Размер прокрутки в пикселях. По умолчанию 600.
*   `direction` (str): Направление прокрутки ('both', 'down', 'up'). По умолчанию 'both'.
*   `delay` (float): Задержка между прокрутками в секундах. По умолчанию 0.3.

**Возвращает**:

*   `bool`: `True`, если прокрутка выполнена успешно, `False` в случае ошибки.

**Примеры**:

```python
driver.scroll(scrolls=2, direction='down', delay=0.5)  # Прокрутить дважды вниз с задержкой 0.5 секунды
driver.scroll(direction='both')  # Прокрутить вверх и вниз по одному разу
```

#### `locale`

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

**Назначение**:
Определяет язык страницы на основе мета-тегов или JavaScript.

**Как работает функция**:
1. Пытается найти мета-тег `Content-Language` с помощью CSS-селектора `"meta[http-equiv='Content-Language']"`.
2. Если мета-тег найден, возвращает значение его атрибута `content`, которое представляет собой код языка страницы.
3. Если мета-тег не найден или произошла ошибка, функция логирует отладочное сообщение и пытается определить язык страницы с помощью JavaScript, вызывая метод `self.get_page_lang()`.
4. Если определение языка с помощью JavaScript также не удалось, функция логирует еще одно отладочное сообщение и возвращает `None`.

**Возвращает**:

*   `Optional[str]`: Код языка, если он найден, иначе `None`.

#### `get_url`

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

**Назначение**:
Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

**Как работает функция**:

1.  Пытается скопировать текущий URL в переменную `_previous_url`. Если это не удается, логирует ошибку и возвращает `False`.
2.  Пытается перейти по указанному URL с помощью метода `self.driver.get(url)`.
3.  Ожидает завершения загрузки страницы, проверяя свойство `self.ready_state`.
4.  Если URL отличается от предыдущего URL, сохраняет предыдущий URL в свойстве `self.previous_url`.
5.  Сохраняет куки локально с помощью метода `self._save_cookies_localy()`.
6.  В случае возникновения исключений `WebDriverException`, `InvalidArgumentException` или других исключений, логирует соответствующие ошибки и возвращает `False`.

**Параметры**:

*   `url` (str): URL для перехода.

**Возвращает**:

*   `bool`: `True`, если навигация выполнена успешно, `False` в противном случае.

#### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    self.execute_script('window.open();')
    self.switch_to.window(self.window_handles[-1])
    if url:
        self.get(url)
```

**Назначение**:
Открывает новую вкладку в текущем окне браузера и переключается на нее.

**Как работает функция**:

1.  Выполняет JavaScript-код `window.open();`, который открывает новую вкладку в браузере.
2.  Переключается на новую вкладку, используя метод `self.switch_to.window(self.window_handles[-1])`.
3.  Если указан URL, переходит по этому URL в новой вкладке с помощью метода `self.get(url)`.

**Параметры**:

*   `url` (Optional[str]): URL для открытия в новой вкладке.

#### `wait`

```python
def wait(self, delay: float = .3) -> None:
    time.sleep(delay)
```

**Назначение**:
Ожидает указанное количество времени.

**Как работает функция**:

1.  Приостанавливает выполнение текущего потока на указанное количество секунд с помощью функции `time.sleep(delay)`.

**Параметры**:

*   `delay` (float): Время ожидания в секундах. По умолчанию 0.3.

#### `_save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
    try:
        with open(gs.cookies_filepath, 'wb') as cookiesfile:
            pickle.dump(self.driver.get_cookies(), cookiesfile)
    except Exception as ex:
        logger.error('Error saving cookies:', ex)
```

**Назначение**:
Сохраняет текущие куки веб-драйвера в локальный файл.

**Как работает функция**:

1.  Пытается открыть файл, путь к которому указан в `gs.cookies_filepath`, в бинарном режиме для записи.
2.  Сохраняет текущие куки веб-драйвера, полученные с помощью метода `self.driver.get_cookies()`, в открытый файл с использованием модуля `pickle`.
3.  В случае возникновения ошибки логирует ошибку.

#### `fetch_html`

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

**Назначение**:
Получает HTML-контент из файла или веб-страницы.

**Как работает функция**:

1.  Проверяет, начинается ли URL с префикса `file://`. Если это так, пытается прочитать HTML-контент из локального файла.
    *   Удаляет префикс `file://` из URL.
    *   Извлекает путь к файлу с помощью регулярного выражения.
    *   Проверяет, существует ли файл по указанному пути.
    *   Если файл существует, пытается открыть его в режиме чтения с кодировкой UTF-8 и прочитать его содержимое в атрибут `self.html_content`.
    *   В случае возникновения ошибки при чтении файла или если файл не найден, логирует ошибку и возвращает `False`.
2.  Если URL начинается с префикса `http://` или `https://`, пытается получить HTML-контент с веб-страницы.
    *   Вызывает метод `self.get_url(url)` для перехода по указанному URL.
    *   Если переход выполнен успешно, сохраняет исходный код страницы в атрибут `self.html_content`.
    *   В случае возникновения ошибки логирует ошибку и возвращает `False`.
3.  Если URL не начинается ни с одного из поддерживаемых префиксов, логирует ошибку и возвращает `False`.

**Параметры**:

*   `url` (str): Путь к файлу или URL для получения HTML-контента.

**Возвращает**:

*   `Optional[bool]`: `True`, если контент успешно получен, `False` в случае ошибки.

**Примеры**:

```python
# Чтение HTML-контента из локального файла
driver.fetch_html('file:///C:/path/to/file.html')

# Получение HTML-контента с веб-страницы
driver.fetch_html('https://example.com')
```