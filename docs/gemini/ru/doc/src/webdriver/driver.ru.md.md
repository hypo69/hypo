# Модуль `driver.py`

## Обзор

Модуль `driver.py` предназначен для работы с веб-драйверами Selenium. Основное назначение класса `Driver` — обеспечение унифицированного интерфейса для взаимодействия с веб-драйверами Selenium. Класс предоставляет методы для инициализации драйвера, навигации по веб-страницам, работы с куки, обработки исключений и других операций.

## Содержание

- [Обзор](#обзор)
- [Основные функции](#основные-функции)
- [Класс `Driver`](#класс-driver)
    - [Инициализация](#инициализация)
    - [Подклассы](#подклассы)
    - [Доступ к атрибутам драйвера](#доступ-к-атрибутам-драйвера)
    - [Прокрутка страницы](#прокрутка-страницы)
    - [Определение языка страницы](#определение-языка-страницы)
    - [Переход по URL](#переход-по-url)
    - [Открытие новой вкладки](#открытие-новой-вкладки)
    - [Ожидание](#ожидание)
    - [Сохранение куки локально](#сохранение-куки-локально)
    - [Извлечение HTML-контента](#извлечение-html-контента)
- [Пример использования](#пример-использования)
- [Заключение](#заключение)

## Основные функции

1.  **Инициализация драйвера**: Создание экземпляра Selenium WebDriver.
2.  **Навигация**: Переход по URL, прокрутка и извлечение контента.
3.  **Работа с куки**: Сохранение и управление куки.
4.  **Обработка исключений**: Логирование ошибок.

## Класс `Driver`

### Инициализация

```python
class Driver:
    def __init__(self, webdriver_cls, *args, **kwargs):
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)
```

**Описание**: Инициализирует экземпляр класса `Driver` с заданным классом WebDriver.

**Параметры**:
- `webdriver_cls` (WebDriver class): Класс WebDriver (например, Chrome, Firefox).
- `*args`: Позиционные аргументы для инициализации драйвера.
- `**kwargs`: Ключевые аргументы для инициализации драйвера.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом WebDriver.

### Подклассы

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    super().__init_subclass__(**kwargs)
    if browser_name is None:
        raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
    cls.browser_name = browser_name
```

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Параметры**:
- `browser_name` (str): Имя браузера.
- `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан при создании подкласса.

### Доступ к атрибутам драйвера

```python
def __getattr__(self, item):
    return getattr(self.driver, item)
```

**Описание**: Прокси для доступа к атрибутам драйвера.

**Параметры**:
- `item` (str): Имя атрибута.

**Возвращает**:
- Атрибут `item` драйвера, если он существует.

### Прокрутка страницы

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
        try:
            for _ in range(scrolls):
                self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                self.wait(delay)
            return True
        except Exception as ex:
            logger.error('Ошибка при прокрутке', exc_info=ex)
            return False

    try:
        if direction == 'forward' or direction == 'down':
            return carousel('', scrolls, frame_size, delay)
        elif direction == 'backward' or direction == 'up':
            return carousel('-', scrolls, frame_size, delay)
        elif direction == 'both':
            return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
    except Exception as ex:
        logger.error('Ошибка в функции прокрутки', ex)
        return False
```

**Описание**: Прокручивает страницу в указанном направлении.

**Параметры**:
- `scrolls` (int, optional): Количество прокруток. По умолчанию `1`.
- `frame_size` (int, optional): Размер прокрутки в пикселях. По умолчанию `600`.
- `direction` (str, optional): Направление ('both', 'down', 'up', 'forward', 'backward'). По умолчанию `both`.
- `delay` (float, optional): Задержка между прокрутками в секундах. По умолчанию `0.3`.

**Возвращает**:
- `bool`: `True`, если прокрутка прошла успешно, `False` в противном случае.

### Определение языка страницы

```python
@property
def locale(self) -> Optional[str]:
    try:
        meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
        return meta_language.get_attribute('content')
    except Exception as ex:
        logger.debug('Не удалось определить язык сайта из META', ex)
        try:
            return self.get_page_lang()
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из JavaScript', ex)
            return
```

**Описание**: Определяет язык страницы на основе мета-тегов или JavaScript.

**Возвращает**:
- `Optional[str]`: Код языка, если найден, иначе `None`.

### Переход по URL

```python
def get_url(self, url: str) -> bool:
    try:
        _previous_url = copy.copy(self.current_url)
    except Exception as ex:
        logger.error("Ошибка при получении текущего URL", ex)
        return False
    
    try:
        self.driver.get(url)
        
        while self.ready_state != 'complete':
            """ Ожидаем завершения загрузки страницы """

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
        logger.error(f'Ошибка при переходе по URL: {url}\\n', ex)
        return False
```

**Описание**: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если переход успешен, `False` в противном случае.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка при навигации WebDriver.
- `InvalidArgumentException`: Если URL недействителен.
- `Exception`: Если возникает любая другая ошибка.

### Открытие новой вкладки

```python
def window_open(self, url: Optional[str] = None) -> None:
    self.execute_script('window.open();')
    self.switch_to.window(self.window_handles[-1])
    if url:
        self.get(url)
```

**Описание**: Открывает новую вкладку в текущем окне браузера и переключается на неё.

**Параметры**:
- `url` (Optional[str], optional): URL для открытия в новой вкладке. По умолчанию `None`.

### Ожидание

```python
def wait(self, delay: float = .3) -> None:
    time.sleep(delay)
```

**Описание**: Ожидает указанное количество времени.

**Параметры**:
- `delay` (float, optional): Время задержки в секундах. По умолчанию `0.3`.

### Сохранение куки локально

```python
def _save_cookies_localy(self) -> None:
    return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
    try:
        with open(gs.cookies_filepath, 'wb') as cookiesfile:
            pickle.dump(self.driver.get_cookies(), cookiesfile)
    except Exception as ex:
        logger.error('Ошибка при сохранении куки:', ex)
```

**Описание**: Сохраняет текущие куки веб-драйвера в локальный файл.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при сохранении куки.

### Извлечение HTML-контента

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
                    logger.error('Ошибка при чтении файла:', ex)
                    return False
            else:
                logger.error('Локальный файл не найден:', file_path)
                return False
        else:
            logger.error('Некорректный путь к файлу:', cleaned_url)
            return False
    elif url.startswith('http://') or url.startswith('https://'):
        try:
            if self.get_url(url):
                self.html_content = self.page_source
                return True
        except Exception as ex:
            logger.error(f"Ошибка при получении {url}:", ex)
            return False
    else:
        logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
        return False
```

**Описание**: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:
- `url` (str): Путь к файлу или URL для извлечения HTML-контента.

**Возвращает**:
- `Optional[bool]`: `True`, если контент успешно получен, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении файла или запросе.

## Пример использования

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
driver.get_url('https://example.com')
```

## Заключение

Класс `Driver` предоставляет унифицированный интерфейс для работы с веб-драйверами Selenium, упрощая навигацию, работу с куки, обработку исключений и другие операции. Этот класс полезен для автоматизации веб-скрапинга и тестирования.