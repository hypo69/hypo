# Модуль рекламы на Facebook

## Обзор

Модуль `facebook.py` предназначен для автоматизации взаимодействия с Facebook через веб-драйвер. Он включает в себя функции для входа в систему, продвижения постов и других действий, связанных с рекламой. Модуль использует различные сценарии, такие как вход в систему, переключение учетной записи, продвижение поста, публикация заголовка и загрузка медиафайлов.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации рекламных кампаний в Facebook. Он использует веб-драйвер для имитации действий пользователя, таких как вход в систему, публикация сообщений и загрузка медиафайлов. Модуль предоставляет классы и функции для работы с Facebook API и позволяет автоматизировать рутинные задачи, связанные с рекламой.

## Классы

### `Facebook`

**Описание**: Класс для взаимодействия с Facebook через веб-драйвер.

**Как работает класс**:
Класс `Facebook` инициализируется с драйвером веб-браузера, именем промоутера и списком путей к файлам групп. Он предоставляет методы для входа в систему, продвижения постов и событий.

**Методы**:

- `__init__`: Инициализирует класс `Facebook` с драйвером, промоутером и списком путей к файлам групп.
- `login`: Выполняет сценарий входа в Facebook.
- `promote_post`: Отправляет текст в форму сообщения для продвижения поста.
- `promote_event`: Выполняет продвижение события.

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
1. Функция принимает инстанс драйвера веб-браузера `driver`, имя промоутера `promoter` и список путей к файлам групп `group_file_paths`.
2.  Сохраняет переданные параметры `driver` и `promoter` в атрибуты экземпляра класса.
3. Выполняет настройку драйвера, например, переключение профиля, если необходимо.
4.  TODO: Добавить проверку на какой странице открылся фейсбук. Если открылась страница логина - выполнитл сценарий логина

**Параметры**:

- `driver` (Driver): Инстанс драйвера веб-браузера.
- `promoter` (str): Имя промоутера.
- `group_file_paths` (list[str]): Список путей к файлам групп.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

```python
# Пример инициализации класса Facebook
from src.endpoints.advertisement.facebook.facebook import Facebook
# from src.driver import Driver  # Предположим, что класс Driver находится в модуле src.driver
# from selenium import webdriver

# # Создание инстанса драйвера (пример с Chrome)
# driver = Driver(webdriver.Chrome)
# promoter = 'Имя промоутера'
# group_file_paths = ['path/to/group1.txt', 'path/to/group2.txt']
# facebook_instance = Facebook(driver, promoter, group_file_paths)
```

#### `login`

```python
def login(self) -> bool:
    """ Функция для входа в фейсбук аккаунт
    @param self: экземпляр класса `Facebook`
    @returns `True`, если успешно, иначе `False`
    """
```

**Назначение**: Выполнение сценария входа в Facebook.

**Как работает функция**:

1. Вызывает функцию `login` из модуля `src.endpoints.advertisement.facebook.scenarios.login`, передавая ей текущий экземпляр класса `Facebook`.
2. Функция `login` выполняет необходимые действия для входа в аккаунт Facebook через веб-драйвер.

**Параметры**:

- `self` (Facebook): Экземпляр класса `Facebook`.

**Возвращает**:

- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Вызывает исключения**:

- Отсутствуют явные исключения.

**Примеры**:

```python
# Пример вызова функции login
from src.endpoints.advertisement.facebook.facebook import Facebook
# from src.driver import Driver  # Предположим, что класс Driver находится в модуле src.driver
# from selenium import webdriver

# # Создание инстанса драйвера (пример с Chrome)
# driver = Driver(webdriver.Chrome)
# promoter = 'Имя промоутера'
# group_file_paths = ['path/to/group1.txt', 'path/to/group2.txt']
# facebook_instance = Facebook(driver, promoter, group_file_paths)

# login_result = facebook_instance.login()
# if login_result:
#     print('Вход выполнен успешно')
# else:
#     print('Ошибка при входе')
```

#### `promote_post`

```python
def promote_post(self, item: SimpleNamespace) -> bool:
    """ Функция отправляет текст в форму сообщения 
    @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
    @returns `True`, если успешно, иначе `False`
    """
```

**Назначение**: Отправка текста в форму сообщения для продвижения поста.

**Как работает функция**:

1.  Функция принимает объект `item` типа `SimpleNamespace`, содержащий данные для продвижения поста.
2. Вызывает функцию `promote_post` из модуля `src.endpoints.advertisement.facebook.scenarios`, передавая ей драйвер веб-браузера и объект `item`.
3.  Функция `promote_post` выполняет необходимые действия для отправки текста в форму сообщения и продвижения поста через веб-драйвер.

**Параметры**:

- `item` (SimpleNamespace): Объект, содержащий данные для продвижения поста.

**Возвращает**:

- `bool`: `True`, если отправка выполнена успешно, иначе `False`.

**Вызывает исключения**:

- Отсутствуют явные исключения.

**Примеры**:

```python
# Пример вызова функции promote_post
from src.endpoints.advertisement.facebook.facebook import Facebook
# from src.driver import Driver  # Предположим, что класс Driver находится в модуле src.driver
# from selenium import webdriver
from types import SimpleNamespace

# # Создание инстанса драйвера (пример с Chrome)
# driver = Driver(webdriver.Chrome)
# promoter = 'Имя промоутера'
# group_file_paths = ['path/to/group1.txt', 'path/to/group2.txt']
# facebook_instance = Facebook(driver, promoter, group_file_paths)

# item = SimpleNamespace(message='Текст сообщения для продвижения')
# promote_result = facebook_instance.promote_post(item)
# if promote_result:
#     print('Пост успешно продвинут')
# else:
#     print('Ошибка при продвижении поста')
```

#### `promote_event`

```python
def promote_event(self, event: SimpleNamespace):
    """ Пример функции для продвижения события """
```

**Назначение**: Продвижение события.

**Как работает функция**:
Функция принимает объект `event` типа `SimpleNamespace`, содержащий данные о событии для продвижения.
Выполняет необходимые действия для продвижения события через веб-драйвер.

**Параметры**:

- `event` (SimpleNamespace): Объект, содержащий данные о событии для продвижения.

**Возвращает**:

- Отсутствует возвращаемое значение.

**Вызывает исключения**:

- Отсутствуют явные исключения.

**Примеры**:

```python
# Пример вызова функции promote_event
from src.endpoints.advertisement.facebook.facebook import Facebook
# from src.driver import Driver  # Предположим, что класс Driver находится в модуле src.driver
# from selenium import webdriver
from types import SimpleNamespace

# # Создание инстанса драйвера (пример с Chrome)
# driver = Driver(webdriver.Chrome)
# promoter = 'Имя промоутера'
# group_file_paths = ['path/to/group1.txt', 'path/to/group2.txt']
# facebook_instance = Facebook(driver, promoter, group_file_paths)

# event = SimpleNamespace(name='Название события', description='Описание события')
# facebook_instance.promote_event(event)