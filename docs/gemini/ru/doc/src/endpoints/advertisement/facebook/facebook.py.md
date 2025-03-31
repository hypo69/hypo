# Модуль рекламы на Facebook

## Обзор

Модуль `facebook.py` предназначен для автоматизации взаимодействия с Facebook через веб-драйвер. Он включает в себя классы и функции для выполнения различных сценариев, таких как вход в систему, публикация сообщений и загрузка медиафайлов.

## Подробней

Модуль разработан для упрощения и автоматизации рекламных кампаний в Facebook. Он предоставляет инструменты для управления аккаунтами, публикации контента и продвижения событий.
Модуль использует веб-драйвер для имитации действий пользователя в браузере, что позволяет автоматизировать задачи, которые обычно выполняются вручную.

## Классы

### `Facebook`

**Описание**: Класс `Facebook` предназначен для взаимодействия с Facebook через веб-драйвер. Он предоставляет методы для входа в систему, публикации сообщений и загрузки медиафайлов.

**Как работает класс**:

Класс `Facebook` инициализируется с веб-драйвером и именем пользователя. Он использует веб-драйвер для автоматизации действий в Facebook, таких как вход в систему, публикация сообщений и загрузка медиафайлов.

**Методы**:

- `__init__(self, driver: 'Driver', promoter: str, group_file_paths: list[str], *args, **kwards)`: Инициализирует экземпляр класса `Facebook`.
- `login(self) -> bool`: Выполняет вход в Facebook.
- `promote_post(self, item: SimpleNamespace) -> bool`: Отправляет текст в форму сообщения.
- `promote_event(self, event: SimpleNamespace)`: Функция для продвижения события.

#### `__init__`

```python
    def __init__(self, driver: 'Driver', promoter: str, group_file_paths: list[str], *args, **kwards):
        """ Я могу передать уже запущенный инстанс драйвера. Например, из алиэкспресс
        @todo:
            - Добавить проверку на какой странице открылся фейсбук. Если открылась страница логина - выполнитл сценарий логина
        """
```

**Назначение**: Инициализация экземпляра класса `Facebook`.

**Как работает функция**:
Функция `__init__` инициализирует экземпляр класса `Facebook`, принимая в качестве аргументов драйвер веб-браузера, имя пользователя (promoter) и список путей к файлам групп. Драйвер используется для взаимодействия с Facebook через веб-браузер, имя пользователя идентифицирует пользователя Facebook, а список файлов групп может использоваться для каких-либо операций с группами в Facebook (данная функциональность в предоставленном коде не реализована, просто передается значение).

**Параметры**:
- `driver` (`'Driver'`): Инстанс веб-драйвера, используемый для взаимодействия с Facebook.
- `promoter` (`str`): Имя пользователя Facebook.
- `group_file_paths` (`list[str]`): Список путей к файлам групп.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Возвращает**:
- None

**Примеры**:
```python
# Пример инициализации класса Facebook
from selenium import webdriver
from src.endpoints.advertisement.facebook.facebook import Facebook

# Создание инстанса драйвера (пример с Chrome)
driver = webdriver.Chrome()
promoter = 'user_name'
group_file_paths = ['/path/to/group1.txt', '/path/to/group2.txt']

# Инициализация класса Facebook
facebook_instance = Facebook(driver=driver, promoter=promoter, group_file_paths=group_file_paths)
```

#### `login`

```python
    def login(self) -> bool:
        """ Функция выполняет вход в Facebook.

        Args:
            self: Экземпляр класса Facebook.

        Returns:
            bool: True, если вход выполнен успешно, иначе False.
        """
```

**Назначение**: Выполнение входа в Facebook.

**Как работает функция**:

Функция `login` вызывает функцию `login` из модуля `src.endpoints.advertisement.facebook.scenarios.login`, передавая ей текущий экземпляр класса `Facebook` (self). Функция возвращает результат выполнения функции `login` из модуля сценариев, который указывает на успешность или неуспешность выполнения входа в Facebook.

**Параметры**:

- `self`: Экземпляр класса `Facebook`.

**Возвращает**:

- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Примеры**:

```python
# Пример вызова функции login
from selenium import webdriver
from src.endpoints.advertisement.facebook.facebook import Facebook

# Создание инстанса драйвера (пример с Chrome)
driver = webdriver.Chrome()
promoter = 'user_name'
group_file_paths = ['/path/to/group1.txt', '/path/to/group2.txt']

# Инициализация класса Facebook
facebook_instance = Facebook(driver=driver, promoter=promoter, group_file_paths=group_file_paths)

# Вызов функции login
login_result = facebook_instance.login()

# Проверка результата
if login_result:
    print("Login successful")
else:
    print("Login failed")
```

#### `promote_post`

```python
    def promote_post(self, item: SimpleNamespace) -> bool:
        """ Функция отправляет текст в форму сообщения 
        @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
        @returns `True`, если успешно, иначе `False`
        """
```

**Назначение**: Отправка текста в форму сообщения в Facebook.

**Как работает функция**:

Функция `promote_post` принимает объект `SimpleNamespace` с данными для публикации и вызывает функцию `promote_post` из модуля `src.endpoints.advertisement.facebook.scenarios`, передавая ей драйвер веб-браузера и объект `item`. Функция возвращает результат выполнения функции `promote_post` из модуля сценариев, который указывает на успешность или неуспешность отправки сообщения.

**Параметры**:

- `item` (`SimpleNamespace`): Объект, содержащий данные для публикации.

**Возвращает**:

- `bool`: `True`, если отправка сообщения выполнена успешно, иначе `False`.

**Примеры**:

```python
# Пример вызова функции promote_post
from selenium import webdriver
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.facebook import Facebook

# Создание инстанса драйвера (пример с Chrome)
driver = webdriver.Chrome()
promoter = 'user_name'
group_file_paths = ['/path/to/group1.txt', '/path/to/group2.txt']

# Инициализация класса Facebook
facebook_instance = Facebook(driver=driver, promoter=promoter, group_file_paths=group_file_paths)

# Создание объекта SimpleNamespace с данными для публикации
item = SimpleNamespace(message="Hello, Facebook!")

# Вызов функции promote_post
promote_post_result = facebook_instance.promote_post(item)

# Проверка результата
if promote_post_result:
    print("Post promoted successfully")
else:
    print("Failed to promote post")
```

#### `promote_event`

```python
    def promote_event(self, event: SimpleNamespace):
        """ Пример функции для продвижения события """
```

**Назначение**: Продвижение события в Facebook.

**Как работает функция**:

Функция `promote_event` принимает объект `SimpleNamespace`, содержащий информацию о событии, которое нужно продвигать. В предоставленном коде функция не имеет реализации (`...`), но предполагает вызов соответствующих методов или функций для продвижения события в Facebook.

**Параметры**:

- `event` (`SimpleNamespace`): Объект, содержащий информацию о событии.

**Возвращает**:
- `None`

**Примеры**:

```python
# Пример вызова функции promote_event
from selenium import webdriver
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.facebook import Facebook

# Создание инстанса драйвера (пример с Chrome)
driver = webdriver.Chrome()
promoter = 'user_name'
group_file_paths = ['/path/to/group1.txt', '/path/to/group2.txt']

# Инициализация класса Facebook
facebook_instance = Facebook(driver=driver, promoter=promoter, group_file_paths=group_file_paths)

# Создание объекта SimpleNamespace с данными о событии
event = SimpleNamespace(name="My Event", date="2024-12-31", location="Online")

# Вызов функции promote_event
facebook_instance.promote_event(event)

# В данном примере предполагается, что внутри функции promote_event
# будет реализована логика продвижения события в Facebook с использованием
# данных из объекта event.
```

## Переменные модуля

- `start_page` (str): URL начальной страницы Facebook. По умолчанию `https://www.facebook.com/hypotez.promocodes`.
- `promoter` (str): Имя пользователя Facebook.