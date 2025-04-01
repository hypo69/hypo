# Модуль для работы с Facebook рекламой

## Обзор

Модуль `facebook.py` предназначен для автоматизации работы с рекламой на платформе Facebook. Он включает в себя классы и функции для входа в систему, отправки сообщений, загрузки медиафайлов и продвижения постов.

## Подробнее

Этот модуль является частью проекта `hypotez` и используется для автоматизации задач, связанных с рекламой в Facebook. Он предоставляет инструменты для взаимодействия с Facebook через веб-драйвер, что позволяет автоматизировать такие действия, как вход в систему, публикация сообщений и загрузка медиафайлов.

## Классы

### `Facebook`

**Описание**: Класс `Facebook` предназначен для взаимодействия с Facebook через веб-драйвер. Он предоставляет методы для входа в систему, продвижения постов и выполнения других задач, связанных с рекламой.

**Принцип работы**:
Класс инициализируется с драйвером веб-браузера и именем пользователя, который будет продвигать контент. Он использует различные сценарии для выполнения конкретных действий, таких как вход в систему, переключение учетных записей и продвижение постов.

**Атрибуты**:
- `d` (`Driver`): Экземпляр веб-драйвера для взаимодействия с Facebook.
- `start_page` (str): URL стартовой страницы Facebook. По умолчанию `https://www.facebook.com/hypotez.promocodes`.
- `promoter` (str): Имя пользователя, который будет продвигать контент.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Facebook`.
- `login`: Выполняет сценарий входа в Facebook.
- `promote_post`: Выполняет сценарий продвижения поста в Facebook.
- `promote_event`: Пример функции для продвижения события.

### `__init__`

```python
def __init__(self, driver: 'Driver', promoter: str, group_file_paths: list[str], *args, **kwards):
    """ Я могу передать уже запущенный инстанс драйвера. Например, из алиэкспресс
    @todo:
        - Добавить проверку на какой странице открылся фейсбук. Если открылась страница логина - выполнитл сценарий логина
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `Facebook`.

**Параметры**:
- `driver` (`Driver`): Экземпляр веб-драйвера для взаимодействия с Facebook.
- `promoter` (str): Имя пользователя, который будет продвигать контент.
- `group_file_paths` (list[str]): Список путей к файлам групп.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Как работает функция**:
1. Функция принимает экземпляр веб-драйвера (`driver`), имя пользователя (`promoter`) и список путей к файлам групп (`group_file_paths`) в качестве аргументов.
2.  Сохраняет переданные параметры в атрибуты экземпляра класса (`self.d`, `self.promoter`).
3.  Устанавливает веб-драйвер для использования в экземпляре класса `Facebook`.

**Примеры**:

```python
from src.webdirver import Driver, Chrome
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='test_user', group_file_paths=['/path/to/group1.txt'])
```

### `login`

```python
def login(self) -> bool:
    """ Функция отправляет текст в форму сообщения 
    @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
    @returns `True`, если успешно, иначе `False`
    """
    ...
```

**Назначение**: Выполняет сценарий входа в Facebook.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает функцию `login` из модуля `src.endpoints.advertisement.facebook.scenarios.login`.
2.  Возвращает результат выполнения функции `login`.

**Примеры**:

```python
from src.webdirver import Driver, Chrome
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='test_user', group_file_paths=['/path/to/group1.txt'])
success = facebook.login()
if success:
    print("Вход выполнен успешно")
else:
    print("Ошибка при входе")
```

### `promote_post`

```python
def promote_post(self, item: SimpleNamespace) -> bool:
    """ Функция отправляет текст в форму сообщения 
    @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
    @returns `True`, если успешно, иначе `False`
    """
    ...
```

**Назначение**: Выполняет сценарий продвижения поста в Facebook.

**Параметры**:
- `item` (`SimpleNamespace`): Объект, содержащий данные для продвижения поста.

**Возвращает**:
- `bool`: `True`, если продвижение выполнено успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает функцию `promote_post` из модуля `src.endpoints.advertisement.facebook.scenarios`.
2.  Передает экземпляр веб-драйвера (`self.d`) и объект `item` в функцию `promote_post`.
3.  Возвращает результат выполнения функции `promote_post`.

**Примеры**:

```python
from types import SimpleNamespace
from src.webdirver import Driver, Chrome
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='test_user', group_file_paths=['/path/to/group1.txt'])
item = SimpleNamespace(message='Hello, Facebook!')
success = facebook.promote_post(item)
if success:
    print("Пост успешно продвинут")
else:
    print("Ошибка при продвижении поста")
```

### `promote_event`

```python
def promote_event(self, event: SimpleNamespace):
    """ Пример функции для продвижения события """
    ...
```

**Назначение**: Пример функции для продвижения события.

**Параметры**:
- `event` (`SimpleNamespace`): Объект, содержащий данные для продвижения события.

**Как работает функция**:
Функция в данный момент не реализована (`...`). Предположительно, она должна выполнять действия, необходимые для продвижения события в Facebook, используя данные, содержащиеся в объекте `event`.

**Примеры**:

```python
from types import SimpleNamespace
from src.webdirver import Driver, Chrome
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='test_user', group_file_paths=['/path/to/group1.txt'])
event = SimpleNamespace(name='My Event', date='2024-12-31')
facebook.promote_event(event)
```
## Функции

В данном модуле не представлено отдельных функций, не связанных с классами.