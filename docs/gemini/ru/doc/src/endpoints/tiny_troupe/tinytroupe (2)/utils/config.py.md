# Модуль конфигурации и утилиты запуска для TinyTroupe

## Обзор

Модуль `config.py` предназначен для чтения, кэширования и предоставления доступа к конфигурационным параметрам приложения TinyTroupe. Он также включает в себя функции для запуска и настройки системы логирования.

## Подробней

Этот модуль обеспечивает централизованное управление конфигурацией приложения. Он сначала пытается загрузить конфигурацию по умолчанию из файла `config.ini`, расположенного в каталоге модуля. Затем он пытается перезаписать эти значения, если существует пользовательский файл `config.ini` в текущем рабочем каталоге. Это позволяет легко настраивать приложение для различных сред без изменения исходного кода. Также модуль инициализирует систему логирования для записи сообщений о событиях и ошибках.

## Функции

### `read_config_file`

```python
def read_config_file(use_cache: bool = True, verbose: bool = True) -> configparser.ConfigParser:
    """
    Считывает конфигурационный файл.

    Args:
        use_cache (bool): Использовать ли кэшированную конфигурацию, если она существует. По умолчанию `True`.
        verbose (bool): Выводить ли подробные сообщения в консоль. По умолчанию `True`.

    Returns:
        configparser.ConfigParser: Объект `ConfigParser`, содержащий параметры конфигурации.

    Raises:
        ValueError: Если не удается найти файл конфигурации по умолчанию.

    Как работает функция:
    1. Проверяет, доступна ли кэшированная конфигурация и разрешено ли ее использование. Если да, возвращает кэшированную конфигурацию.
    2. Если кэшированная конфигурация отсутствует или ее использование не разрешено, создает новый объект `ConfigParser`.
    3. Пытается прочитать файл конфигурации по умолчанию (`config.ini`) из каталога модуля.
    4. Если файл конфигурации по умолчанию найден, он считывается, и конфигурация кэшируется.
    5. Затем пытается прочитать пользовательский файл конфигурации (`config.ini`) из текущего рабочего каталога.
    6. Если пользовательский файл конфигурации найден, он считывается, перезаписывая значения из файла конфигурации по умолчанию.
    7. Если пользовательский файл конфигурации не найден, используется только файл конфигурации по умолчанию.
    8. Если не удается найти файл конфигурации по умолчанию, вызывается исключение `ValueError`.
    9. Возвращает объект `ConfigParser`, содержащий параметры конфигурации.

    ASCII flowchart:

    A [Проверка кэша]
    |
    -- B [Кэш действителен?]
    |   | Да: C [Возврат кэша]
    |   Нет: D [Создание ConfigParser]
    |
    E [Поиск config.ini в каталоге модуля]
    |
    F [Файл найден?]
    |   | Да: G [Чтение config.ini]
    |   Нет: H [Ошибка: файл не найден]
    |
    I [Поиск config.ini в текущем каталоге]
    |
    J [Файл найден?]
    |   | Да: K [Чтение config.ini, перезапись значений]
    |   Нет: L [Использовать только default values]
    |
    M [Возврат ConfigParser]

    Примеры:
    >>> config = read_config_file()
    >>> print(config.get('Section', 'Option'))
    """
    global _config
    if use_cache and _config is not None:
        # if we have a cached config and accept that, return it
        return _config
    
    else:
        config = configparser.ConfigParser()

        # Read the default values in the module directory.
        config_file_path = Path(__file__).parent.absolute() / '../config.ini'
        print(f"Looking for default config on: {config_file_path}") if verbose else None
        if config_file_path.exists():
            config.read(config_file_path)
            _config = config
        else:
            raise ValueError(f"Failed to find default config on: {config_file_path}")

        # Now, let's override any specific default value, if there's a custom .ini config. 
        # Try the directory of the current main program
        config_file_path = Path.cwd() / "config.ini"
        if config_file_path.exists():
            print(f"Found custom config on: {config_file_path}") if verbose else None
            config.read(config_file_path) # this only overrides the values that are present in the custom config
            _config = config
            return config
        else:
            if verbose:
                print(f"Failed to find custom config on: {config_file_path}") if verbose else None
                print("Will use only default values. IF THINGS FAIL, TRY CUSTOMIZING MODEL, API TYPE, etc.") if verbose else None
        
        return config
```

### `pretty_print_config`

```python
def pretty_print_config(config: configparser.ConfigParser) -> None:
    """
    Выводит текущую конфигурацию в удобочитаемом формате.

    Args:
        config (configparser.ConfigParser): Объект `ConfigParser`, содержащий параметры конфигурации.
    Как работает функция:
    1. Выводит заголовок "Current TinyTroupe configuration".
    2. Перебирает все секции в объекте `config`.
    3. Для каждой секции выводит ее имя в формате `[section]`.
    4. Перебирает все параметры в текущей секции.
    5. Для каждого параметра выводит его имя и значение в формате `key = value`.

    ASCII flowchart:

    A [Вывод заголовка]
    |
    B [Перебор секций в конфиге]
    |
    C [Вывод имени секции]
    |
    D [Перебор параметров в секции]
    |
    E [Вывод пары ключ-значение]

    Примеры:
    >>> config = read_config_file()
    >>> pretty_print_config(config)
    """
    print()
    print("=================================")
    print("Current TinyTroupe configuration ")
    print("=================================")
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):\
            print(f"{key} = {value}")
        print()
```

### `start_logger`

```python
def start_logger(config: configparser.ConfigParser) -> None:
    """
    Инициализирует и настраивает систему логирования.

    Args:
        config (configparser.ConfigParser): Объект `ConfigParser`, содержащий параметры конфигурации.

    Как работает функция:
    1. Создает объект логгера с именем "tinytroupe".
    2. Определяет уровень логирования из конфигурации (секция `Logging`, параметр `LOGLEVEL`). Если параметр не указан, используется уровень `INFO`.
    3. Устанавливает уровень логирования для логгера.
    4. Создает обработчик консоли (`StreamHandler`).
    5. Устанавливает уровень логирования для обработчика консоли.
    6. Создает форматтер для сообщений лога.
    7. Добавляет форматтер к обработчику консоли.
    8. Добавляет обработчик консоли к логгеру.

    ASCII flowchart:

    A [Создание логгера]
    |
    B [Определение уровня логирования]
    |
    C [Установка уровня логирования]
    |
    D [Создание обработчика консоли]
    |
    E [Установка уровня для обработчика]
    |
    F [Создание форматтера]
    |
    G [Привязка форматтера к обработчику]
    |
    H [Добавление обработчика к логгеру]

    Примеры:
    >>> config = read_config_file()
    >>> start_logger(config)
    """
    # create logger
    logger = logging.getLogger("tinytroupe")
    log_level = config['Logging'].get('LOGLEVEL', 'INFO').upper()
    logger.setLevel(level=log_level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)