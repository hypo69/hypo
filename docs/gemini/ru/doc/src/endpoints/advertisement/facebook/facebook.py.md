# Модуль рекламы на Facebook

## Обзор

Модуль предназначен для автоматизации действий, связанных с рекламой на платформе Facebook. Он включает в себя сценарии для входа в аккаунт, отправки сообщений и загрузки медиафайлов.

## Подробней

Модуль `facebook.py` предоставляет класс `Facebook`, который использует веб-драйвер для взаимодействия с Facebook. Он содержит методы для выполнения различных рекламных сценариев, таких как вход в аккаунт, продвижение постов и загрузка медиа.

## Классы

### `Facebook`

**Описание**: Класс для взаимодействия с Facebook через веб-драйвер.

**Принцип работы**:
Класс инициализируется с драйвером веб-браузера, именем промоутера и списком путей к файлам групп. Он предоставляет методы для входа в аккаунт, продвижения постов и событий.

**Аттрибуты**:
- `d` (Driver): Инстанс веб-драйвера для управления браузером.
- `start_page` (str): URL страницы, с которой начинается работа (по умолчанию "https://www.facebook.com/hypotez.promocodes").
- `promoter` (str): Имя промоутера.

**Методы**:
- `__init__`: Инициализирует класс `Facebook` с заданным драйвером, именем промоутера и списком путей к файлам групп.
- `login`: Выполняет сценарий входа в аккаунт Facebook.
- `promote_post`: Отправляет текст в форму сообщения для продвижения поста.
- `promote_event`: Функция для продвижения события.

## Функции

### `__init__`

```python
def __init__(self, driver: 'Driver', promoter: str, group_file_paths: list[str], *args, **kwards):
    """ Я могу передать уже запущенный инстанс драйвера. Например, из алиэкспресс
    @todo:
        - Добавить проверку на какой странице открылся фейсбук. Если открылась страница логина - выполнитл сценарий логина
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `Facebook`.

**Параметры**:
- `driver` (Driver): Инстанс веб-драйвера, используемый для взаимодействия с Facebook.
- `promoter` (str): Имя промоутера.
- `group_file_paths` (list[str]): Список путей к файлам групп.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Как работает функция**:

1. Функция принимает инстанс драйвера, имя промоутера и список путей к файлам групп.
2.  Сохраняет переданные аргументы в атрибуты экземпляра класса `Facebook`.
3.  Закомментированы строки кода, которые, предположительно, должны были переходить на начальную страницу и переключать профиль.

**Примеры**:
```python
from src.webdirver import Driver, Chrome
# Пример создания инстанса класса Facebook
driver = Driver(Chrome)
facebook = Facebook(driver, promoter='MyPromoter', group_file_paths=['/path/to/group1', '/path/to/group2'])
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

**Назначение**: Выполняет сценарий входа в аккаунт Facebook.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает функцию `login` из модуля `src.endpoints.advertisement.facebook.scenarios.login`, передавая ей инстанс класса `Facebook`.
2.  Возвращает результат выполнения функции `login`.

**Примеры**:
```python
from src.webdirver import Driver, Chrome
# Пример вызова функции login
driver = Driver(Chrome)
facebook = Facebook(driver, promoter='MyPromoter', group_file_paths=['/path/to/group1', '/path/to/group2'])
success = facebook.login()
print(f"Login successful: {success}")
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

**Назначение**: Отправляет текст в форму сообщения для продвижения поста.

**Параметры**:
- `item` (SimpleNamespace): Объект, содержащий данные для продвижения поста.

**Возвращает**:
- `bool`: `True`, если отправка выполнена успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает функцию `promote_post` из модуля `src.endpoints.advertisement.facebook.scenarios`, передавая ей инстанс веб-драйвера (`self.d`) и данные для продвижения поста (`item`).
2.  Возвращает результат выполнения функции `promote_post`.

**Примеры**:
```python
from src.webdirver import Driver, Chrome
from types import SimpleNamespace
# Пример вызова функции promote_post
driver = Driver(Chrome)
facebook = Facebook(driver, promoter='MyPromoter', group_file_paths=['/path/to/group1', '/path/to/group2'])
item = SimpleNamespace(message='Текст сообщения', image_path='/path/to/image.jpg')
success = facebook.promote_post(item)
print(f"Post promotion successful: {success}")
```

### `promote_event`

```python
def promote_event(self, event: SimpleNamespace):
    """ Пример функции для продвижения события """
    ...
```

**Назначение**: Функция для продвижения события.

**Параметры**:
- `event` (SimpleNamespace): Объект, содержащий данные о событии для продвижения.

**Как работает функция**:

Функция помечена как пример и не содержит реализации (`...`). Предположительно, она должна принимать объект `SimpleNamespace` с данными о событии и выполнять действия по его продвижению на платформе Facebook.

**Примеры**:
```python
from src.webdirver import Driver, Chrome
from types import SimpleNamespace
# Пример вызова функции promote_event
driver = Driver(Chrome)
facebook = Facebook(driver, promoter='MyPromoter', group_file_paths=['/path/to/group1', '/path/to/group2'])
event = SimpleNamespace(name='Название события', description='Описание события', date='Дата события')
facebook.promote_event(event)