# Модуль рекламы на Facebook

## Обзор

Модуль `facebook.py` предназначен для автоматизации работы с Facebook через веб-драйвер. Он включает в себя классы и функции для логина, публикации сообщений, загрузки медиа-файлов и продвижения постов и событий.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации задач, связанных с рекламой и продвижением в Facebook. Он использует веб-драйвер для взаимодействия с сайтом Facebook и выполнения различных сценариев, таких как вход в систему, публикация сообщений и загрузка медиа-файлов.

## Классы

### `Facebook`

**Описание**: Класс для взаимодействия с Facebook через веб-драйвер.

**Принцип работы**:
Класс `Facebook` инициализируется с инстансом драйвера, именем промоутера и списком путей к файлам групп. Он предоставляет методы для выполнения различных действий в Facebook, таких как вход в систему, продвижение постов и событий.

**Аттрибуты**:

- `d` (Driver): Инстанс веб-драйвера для взаимодействия с Facebook.
- `start_page` (str): URL стартовой страницы Facebook. По умолчанию 'https://www.facebook.com/hypotez.promocodes'.
- `promoter` (str): Имя промоутера.

**Методы**:

- `__init__`: Инициализирует класс `Facebook`.
- `login`: Выполняет сценарий логина в Facebook.
- `promote_post`: Отправляет текст в форму сообщения для продвижения поста.
- `promote_event`: Пример функции для продвижения события.

### `Facebook.__init__`

```python
def __init__(self, driver: 'Driver', promoter: str, group_file_paths: list[str], *args, **kwards):
    """ Я могу передать уже запущенный инстанс драйвера. Например, из алиэкспресс
    @todo:
        - Добавить проверку на какой странице открылся фейсбук. Если открылась страница логина - выполнитл сценарий логина
    """
    self.d = driver
    self.promoter = promoter
    ...
    
    #self.driver.get_url (self.start_page)
    #switch_account(self.driver) # <- переключение профиля, если не на своей странице
```

**Назначение**: Инициализация экземпляра класса `Facebook`.

**Параметры**:

- `driver` (Driver): Инстанс веб-драйвера для взаимодействия с Facebook.
- `promoter` (str): Имя промоутера.
- `group_file_paths` (list[str]): Список путей к файлам групп.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Как работает функция**:

1.  Присваивает переданный инстанс драйвера атрибуту `self.d`.
2.  Присваивает имя промоутера атрибуту `self.promoter`.
3.  Оставляет многоточие (`...`), указывающее на незавершенную логику (возможно, инициализация или конфигурация).
4.  Закомментированы строки кода, которые, вероятно, должны переключать аккаунт, если это необходимо.

**Примеры**:

```python
from src.webdirver import Driver, Chrome
# Пример инициализации класса Facebook
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='MyPromoter', group_file_paths=['path/to/group1.txt', 'path/to/group2.txt'])
```

### `Facebook.login`

```python
def login(self) -> bool:
    """ Функция отправляет текст в форму сообщения 
    @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
    @returns `True`, если успешно, иначе `False`
    """
    ...
    return login(self)
```

**Назначение**: Выполняет сценарий входа в Facebook.

**Возвращает**:

- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает функцию `login` из модуля `.scenarios.login`, передавая ей текущий экземпляр класса `Facebook` (self).
2.  Возвращает результат выполнения функции `login`.

```
Начало
  ↓
Вызов login(self)
  ↓
Конец
```

**Примеры**:

```python
from src.webdirver import Driver, Chrome
# Пример вызова функции login
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='MyPromoter', group_file_paths=['path/to/group1.txt', 'path/to/group2.txt'])
success = facebook.login()
if success:
    print('Вход выполнен успешно')
else:
    print('Ошибка при входе')
```

### `Facebook.promote_post`

```python
def promote_post(self, item: SimpleNamespace) -> bool:
    """ Функция отправляет текст в форму сообщения 
    @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
    @returns `True`, если успешно, иначе `False`
    """
    ...
    return promote_post(self.d, item)
```

**Назначение**: Продвигает пост в Facebook.

**Параметры**:

- `item` (SimpleNamespace): Объект, содержащий данные для продвижения поста.

**Возвращает**:

- `bool`: `True`, если продвижение выполнено успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает функцию `promote_post` из модуля `.scenarios`, передавая ей драйвер и объект `item`.
2.  Возвращает результат выполнения функции `promote_post`.

```
Начало
  ↓
Вызов promote_post(self.d, item)
  ↓
Конец
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdirver import Driver, Chrome
# Пример вызова функции promote_post
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='MyPromoter', group_file_paths=['path/to/group1.txt', 'path/to/group2.txt'])
item = SimpleNamespace(message='Текст сообщения', image_path='path/to/image.jpg')
success = facebook.promote_post(item)
if success:
    print('Пост продвинут успешно')
else:
    print('Ошибка при продвижении поста')
```

### `Facebook.promote_event`

```python
def promote_event(self, event: SimpleNamespace):
    """ Пример функции для продвижения события """
    ...
```

**Назначение**: Продвигает событие в Facebook.

**Параметры**:

- `event` (SimpleNamespace): Объект, содержащий данные для продвижения события.

**Как работает функция**:

1.  Содержит многоточие (`...`), указывающее на незавершенную логику (возможно, вызов функции из модуля `.scenarios` для продвижения события).

**Примеры**:

```python
from types import SimpleNamespace
from src.webdirver import Driver, Chrome
# Пример вызова функции promote_event
driver = Driver(Chrome)
facebook = Facebook(driver=driver, promoter='MyPromoter', group_file_paths=['path/to/group1.txt', 'path/to/group2.txt'])
event = SimpleNamespace(name='Название события', description='Описание события', date='Дата события')
facebook.promote_event(event)