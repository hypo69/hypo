# Модуль `firefox`

## Обзор

Модуль `firefox` предоставляет класс `Firefox`, расширяющий стандартный `webdriver.Firefox` из Selenium. Он предназначен для управления браузером Firefox, включая настройку профиля, установку параметров запуска (например, в режиме киоска), управление прокси и установку пользовательских настроек.

## Подробнее

Этот модуль позволяет автоматизировать взаимодействие с браузером Firefox через WebDriver, предоставляя удобные инструменты для настройки и управления браузером. Он включает в себя функциональность для установки пользовательского профиля, управления прокси и выполнения JavaScript-кода на страницах.

## Классы

### `Firefox`

**Описание**: Класс `Firefox` является расширением класса `selenium.webdriver.Firefox`. Он предоставляет дополнительные возможности для настройки и управления браузером Firefox.

**Наследует**:
- `selenium.webdriver.Firefox`

**Аттрибуты**:
- `driver_name` (str): Имя драйвера, по умолчанию `'firefox'`.
- `service` (Service): Сервис WebDriver для Firefox.

**Методы**:
- `__init__(self, profile_name: Optional[str] = None, geckodriver_version: Optional[str] = None, firefox_version: Optional[str] = None, user_agent: Optional[str] = None, proxy_file_path: Optional[str] = None, options: Optional[List[str]] = None, window_mode: Optional[str] = None, *args, **kwargs) -> None`: Инициализирует экземпляр класса `Firefox`, настраивает параметры запуска браузера, устанавливает пользовательский профиль, прокси и другие опции.
- `set_proxy(self, options: Options) -> None`: Настраивает прокси для Firefox на основе переданных опций.
- `_payload(self) -> None`: Загружает исполнителей для локаторов и JavaScript сценариев.

### `__init__`

```python
 def __init__(self, profile_name: Optional[str] = None,
                 geckodriver_version: Optional[str] = None,
                 firefox_version: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 proxy_file_path: Optional[str] = None,
                 options: Optional[List[str]] = None,
                 window_mode: Optional[str] = None,
                 *args, **kwargs) -> None:
        """"""
```

**Назначение**: Инициализация экземпляра класса `Firefox`. Отвечает за настройку и запуск драйвера Firefox с заданными параметрами, такими как профиль, версия, пользовательский агент, прокси и режим окна.

**Параметры**:
- `profile_name` (Optional[str], optional): Имя пользовательского профиля Firefox. По умолчанию `None`.
- `geckodriver_version` (Optional[str], optional): Версия geckodriver. По умолчанию `None`.
- `firefox_version` (Optional[str], optional): Версия Firefox. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Пользовательский агент в формате строки. По умолчанию `None`.
- `proxy_file_path` (Optional[str], optional): Путь к файлу с прокси. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список опций для Firefox. По умолчанию `None`.
- `window_mode` (Optional[str], optional): Режим окна браузера (`windowless`, `kiosk`, `full_window` и т.д.). По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка при запуске WebDriver (например, несовместимость версий Firefox и geckodriver).
- `Exception`: Если возникает любая другая ошибка в процессе инициализации.

**Как работает функция**:

1. **Инициализация**:
   - Записывает информацию о запуске Firefox WebDriver в лог.
   - Инициализирует переменные `profile` и `options_obj` в `None`.

2. **Загрузка конфигурации**:
   - Загружает конфигурационные параметры Firefox из файла `firefox.json` с использованием функции `j_loads_ns`.

3. **Определение путей**:
   - Определяет пути к исполняемым файлам `geckodriver` и `firefox` на основе конфигурации.

4. **Инициализация сервиса**:
   - Создает экземпляр класса `Service`, передавая путь к `geckodriver`.

5. **Настройка опций**:
   - Создает экземпляр класса `Options` для настройки опций Firefox.
   - Добавляет опции, указанные в конфигурационном файле, если они есть.
   - Устанавливает режим окна, если он указан в параметре `window_mode`.
   - Добавляет опции, переданные при инициализации.
   - Добавляет заголовки из конфигурационного файла.
   - Устанавливает пользовательский агент.

6. **Настройка прокси**:
   - Если в конфигурации включена поддержка прокси, вызывает метод `set_proxy` для настройки прокси.

7. **Настройка профиля**:
   - Определяет директорию профиля на основе конфигурации и параметра `profile_name`.

8. **Запуск WebDriver**:
   - Пытается запустить WebDriver с заданными опциями и сервисом.
   - В случае успеха записывает информацию об успешном запуске в лог.
   - В случае неудачи перехватывает исключение `WebDriverException` и записывает сообщение об ошибке в лог, а также завершает работу программы.
   - Перехватывает любые другие исключения и записывает информацию об ошибке в лог.

9. **Вызов `_payload()`**:
    - После успешного запуска вызывает метод `_payload()` для загрузки исполнителей локаторов и JavaScript.

**ASCII flowchart**:

```
    Запуск Firefox WebDriver
    │
    ├── Загрузка конфигурации из firefox.json
    │
    ├── Определение путей к geckodriver и firefox
    │
    ├── Инициализация сервиса WebDriver
    │
    ├── Создание и настройка опций Firefox
    │   ├── Добавление опций из файла конфигурации
    │   ├── Установка режима окна
    │   ├── Добавление дополнительных опций
    │   ├── Добавление заголовков
    │   └── Установка User-Agent
    │
    ├── Настройка прокси (если включено)
    │
    ├── Настройка директории профиля
    │
    ├── Запуск WebDriver
    │   ├── Успех: Запись в лог об успешном запуске
    │   ├── Ошибка WebDriverException: Запись в лог и выход
    │   └── Другая ошибка: Запись в лог
    │
    └── Вызов _payload() для загрузки исполнителей
```

**Примеры**:

```python
from src.webdriver.firefox.firefox import Firefox
from pathlib import Path
import os

# Пример 1: Запуск Firefox с настройками по умолчанию
driver = Firefox()
driver.get("https://www.google.com")
driver.quit()

# Пример 2: Запуск Firefox с указанием версии geckodriver и firefox
driver = Firefox(geckodriver_version="v0.33.0", firefox_version="115.0")
driver.get("https://www.google.com")
driver.quit()

# Пример 3: Запуск Firefox в режиме kiosk
driver = Firefox(window_mode="kiosk")
driver.get("https://www.google.com")
driver.quit()

# Пример 4: Запуск Firefox с пользовательским профилем
profile_name = "my_custom_profile"
#  Перед запуском убедитесь, что профиль существует.  Иначе будет создан новый профиль.
profile_directory = Path(os.environ.get('LOCALAPPDATA')) / "Mozilla/Firefox/Profiles"
if not (profile_directory / profile_name).exists():
   print(f"Профиль {profile_name} не найден")
else: 
    driver = Firefox(profile_name=profile_name)
    driver.get("https://www.google.com")
    driver.quit()
```

### `set_proxy`

```python
    def set_proxy(self, options: Options) -> None:
        """
        Настройка прокси из словаря, возвращаемого get_proxies_dict.

        :param options: Опции Firefox, в которые добавляются настройки прокси.
        :type options: Options
        """
```

**Назначение**: Метод `set_proxy` предназначен для настройки прокси-сервера в браузере Firefox. Он получает опции Firefox и настраивает прокси на основе данных, полученных из словаря прокси.

**Параметры**:
- `options` (Options): Опции Firefox, в которые добавляются настройки прокси.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Получение словаря прокси**:
   - Вызывает функцию `get_proxies_dict()` для получения словаря прокси.

2. **Формирование списка прокси**:
   - Создает список `all_proxies`, объединяя прокси из `proxies_dict` с ключами `socks4` и `socks5`.

3. **Поиск рабочего прокси**:
   - Перебирает прокси из списка `all_proxies` в случайном порядке, используя `random.sample`.
   - Для каждого прокси вызывает функцию `check_proxy()` для проверки его работоспособности.
   - Если прокси работает, присваивает его переменной `working_proxy` и прерывает цикл.

4. **Настройка прокси**:
   - Если `working_proxy` найден, извлекает протокол (`protocol`) и настраивает прокси в зависимости от протокола:
     - Если протокол `http`, устанавливает HTTP прокси, используя `options.set_preference` для `network.proxy.type`, `network.proxy.http`, `network.proxy.http_port`, `network.proxy.ssl` и `network.proxy.ssl_port`.
     - Если протокол `socks4` или `socks5`, устанавливает SOCKS прокси, используя `options.set_preference` для `network.proxy.type`, `network.proxy.socks` и `network.proxy.socks_port`.
     - Записывает информацию о настроенном прокси в лог.
   - Если протокол неизвестен, записывает предупреждение в лог.
   - Если рабочий прокси не найден, записывает предупреждение в лог об отсутствии доступных прокси.

**ASCII flowchart**:

```
    Получение словаря прокси
    │
    ├── Формирование списка всех прокси
    │
    ├── Перебор прокси в случайном порядке
    │   ├── Проверка работоспособности прокси
    │   │   ├── Прокси работает:
    │   │   │   ├── Сохранение рабочего прокси
    │   │   │   └── Выход из цикла
    │   │   └── Прокси не работает:
    │   │       └── Продолжение перебора
    │   └── Все прокси проверены
    │
    ├── Настройка прокси (если найден рабочий)
    │   ├── Определение протокола прокси
    │   ├── Настройка параметров прокси в зависимости от протокола
    │   └── Запись информации в лог
    │
    └── Запись предупреждения в лог (если нет доступных прокси)
```

**Примеры**:

```python
from src.webdriver.firefox.firefox import Firefox
from selenium.webdriver.firefox.options import Options

# Пример 1: Создание Firefox и настройка прокси
options = Options()
firefox = Firefox()
firefox.set_proxy(options)
```

### `_payload`

```python
 def _payload(self) -> None:
         """
        Загружает исполнителей для локаторов и JavaScript сценариев.
         """
```

**Назначение**: Метод `_payload` предназначен для загрузки и инициализации исполнителей (executor) для локаторов веб-элементов и JavaScript-сценариев. Это позволяет упростить и стандартизировать выполнение операций с веб-элементами и выполнение JavaScript-кода на странице.

**Параметры**:
- `self` (Firefox): Экземпляр класса `Firefox`.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Инициализация JavaScript Executor**:
   - Создает экземпляр класса `JavaScript`, передавая текущий экземпляр `Firefox` в качестве аргумента.
   - Сохраняет функции JavaScript executor в текущем экземпляре `Firefox` для дальнейшего использования. Это включает функции:
     - `get_page_lang`: для получения языка страницы.
     - `ready_state`: для получения текущего состояния готовности страницы.
     - `get_referrer`: для получения referrer страницы.
     - `unhide_DOM_element`: для отображения скрытых DOM-элементов.
     - `window_focus`: для фокусировки на окне браузера.

2. **Инициализация ExecuteLocator**:
   - Создает экземпляр класса `ExecuteLocator`, передавая текущий экземпляр `Firefox` в качестве аргумента.
   - Сохраняет методы `ExecuteLocator` в текущем экземпляре `Firefox` для дальнейшего использования. Это включает методы:
     - `execute_locator`: для выполнения локатора и возврата веб-элемента.
     - `get_webelement_as_screenshot`: для получения скриншота веб-элемента.
     - `get_webelement_by_locator`: для получения веб-элемента по локатору.
     - `get_attribute_by_locator`: для получения атрибута веб-элемента по локатору.
     - `send_message` / `send_key_to_webelement`: для отправки сообщения или ключа веб-элементу.

**ASCII flowchart**:

```
    Инициализация JavaScript Executor
    │
    ├── Создание экземпляра класса JavaScript
    │
    ├── Сохранение функций JavaScript Executor
    │   ├── get_page_lang
    │   ├── ready_state
    │   ├── get_referrer
    │   ├── unhide_DOM_element
    │   └── window_focus
    │
    └── Инициализация ExecuteLocator
        │
        ├── Создание экземпляра класса ExecuteLocator
        │
        ├── Сохранение методов ExecuteLocator
        │   ├── execute_locator
        │   ├── get_webelement_as_screenshot
        │   ├── get_webelement_by_locator
        │   ├── get_attribute_by_locator
        │   └── send_message / send_key_to_webelement
```

**Примеры**:

```python
from src.webdriver.firefox.firefox import Firefox

# Пример: Создание инстанса Firefox и вызов _payload
driver = Firefox()
driver._payload()
```

## Примеры

```python
if __name__ == "__main__":
    driver = Firefox()
    driver.get(r"https://google.com")
```