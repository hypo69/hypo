# Модуль `src.webdriver.driver`

## Обзор

Модуль `driver.py` предназначен для работы с веб-драйверами Selenium. Основная цель класса `Driver` - предоставить единый интерфейс для взаимодействия с веб-драйверами Selenium. Класс предлагает методы для инициализации драйвера, навигации, управления файлами cookie, обработки исключений и других операций.

## Содержание

1. [Класс `Driver`](#Класс-Driver)
    - [Инициализация](#Инициализация)
    - [Подклассы](#Подклассы)
    - [Доступ к атрибутам драйвера](#Доступ-к-атрибутам-драйвера)
    - [Прокрутка страницы](#Прокрутка-страницы)
    - [Определение языка страницы](#Определение-языка-страницы)
    - [Переход по URL](#Переход-по-URL)
    - [Открытие новой вкладки](#Открытие-новой-вкладки)
    - [Ожидание](#Ожидание)
    - [Сохранение куки локально](#Сохранение-куки-локально)
    - [Получение HTML-содержимого](#Получение-HTML-содержимого)
2. [Пример использования](#Пример-использования)
3. [Заключение](#Заключение)

## Классы

### `Driver`

**Описание**: Класс `Driver` предоставляет единый интерфейс для взаимодействия с веб-драйверами Selenium.

#### Инициализация

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    if not hasattr(webdriver_cls, 'get'):
        raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
    self.driver = webdriver_cls(*args, **kwargs)
```

**Параметры**:
- `webdriver_cls`: Класс WebDriver (например, Chrome, Firefox).
- `*args`: Позиционные аргументы для инициализации драйвера.
- `**kwargs`: Именованные аргументы для инициализации драйвера.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом WebDriver.

#### Подклассы

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    super().__init_subclass__(**kwargs)
    if browser_name is None:
        raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
    cls.browser_name = browser_name
```

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Параметры**:
- `browser_name`: Имя браузера.
- `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если аргумент `browser_name` не указан.

#### Доступ к атрибутам драйвера

```python
def __getattr__(self, item):
    return getattr(self.driver, item)
```

**Описание**: Прокси для доступа к атрибутам драйвера.

**Параметры**:
- `item`: Имя атрибута.

#### Прокрутка страницы

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

**Описание**: Прокручивает страницу в заданном направлении.

**Параметры**:
- `scrolls` (int, optional): Количество прокруток. По умолчанию `1`.
- `frame_size` (int, optional): Размер прокрутки в пикселях. По умолчанию `600`.
- `direction` (str, optional): Направление прокрутки (`'both'`, `'down'`, `'up'`). По умолчанию `'both'`.
- `delay` (float, optional): Задержка между прокрутками. По умолчанию `0.3`.

**Возвращает**:
- `bool`: `True`, если прокрутка прошла успешно, иначе `False`.

#### Определение языка страницы

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

**Возвращает**:
- `Optional[str]`: Код языка, если найден, иначе `None`.

#### Переход по URL

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

**Описание**: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если навигация прошла успешно, иначе `False`.

**Вызывает исключения**:
- `WebDriverException`: При ошибке, связанной с WebDriver.
- `InvalidArgumentException`: Если URL является недействительным.
- `Exception`: При других ошибках.

#### Открытие новой вкладки

```python
def window_open(self, url: Optional[str] = None) -> None:
    self.execute_script('window.open();')
    self.switch_to.window(self.window_handles[-1])
    if url:
        self.get(url)
```

**Описание**: Открывает новую вкладку в текущем окне браузера и переключается на нее.

**Параметры**:
- `url` (Optional[str], optional): URL для открытия в новой вкладке. По умолчанию `None`.

#### Ожидание

```python
def wait(self, delay: float = .3) -> None:
    time.sleep(delay)
```

**Описание**: Ожидает указанное количество времени.

**Параметры**:
- `delay` (float, optional): Время задержки в секундах. По умолчанию `0.3`.

#### Сохранение куки локально

```python
def _save_cookies_localy(self) -> None:
    return True  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
    try:
        with open(gs.cookies_filepath, 'wb') as cookiesfile:
            pickle.dump(self.driver.get_cookies(), cookiesfile)
    except Exception as ex:
        logger.error('Error saving cookies:', ex)
```

**Описание**: Сохраняет текущие куки веб-драйвера в локальный файл.

#### Получение HTML-содержимого

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

**Описание**: Получает HTML-содержимое из файла или веб-страницы.

**Параметры**:
- `url` (str): Путь к файлу или URL для получения HTML-содержимого.

**Возвращает**:
- `Optional[bool]`: `True`, если содержимое успешно получено, иначе `False`.

## Пример использования

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
driver.get_url('https://example.com')
```

## Заключение

Класс `Driver` предоставляет унифицированный интерфейс для работы с веб-драйверами Selenium, упрощая навигацию, управление куки, обработку исключений и другие операции. Этот класс полезен для веб-скрапинга и автоматизации тестирования.