# Модуль `facebook`

## Обзор

Модуль `facebook` предназначен для автоматизации работы с Facebook через веб-драйвер. Он предоставляет классы и функции для выполнения различных сценариев, таких как вход в систему, публикация сообщений, загрузка медиафайлов и продвижение постов. Модуль взаимодействует с Facebook для автоматизации маркетинговых и рекламных задач.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для управления рекламными кампаниями в Facebook. Он позволяет автоматизировать такие задачи, как вход в аккаунт, публикация контента и продвижение постов. Код использует веб-драйвер для взаимодействия с Facebook, что позволяет имитировать действия пользователя и автоматизировать рутинные операции.

## Классы

### `Facebook`

**Описание**: Класс для взаимодействия с Facebook через веб-драйвер.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Facebook`.
- `login`: Выполняет вход в Facebook.
- `promote_post`: Отправляет текст в форму сообщения для продвижения поста.
- `promote_event`: Функция для продвижения события.

**Параметры**:
- `driver` ('Driver'): Экземпляр веб-драйвера для управления браузером.
- `promoter` (str): Имя промоутера.
- `group_file_paths` (list[str]): Список путей к файлам групп.
- `start_page` (str): URL страницы, с которой начинается работа (по умолчанию 'https://www.facebook.com/hypotez.promocodes').

**Примеры**
```python
# Пример создания экземпляра класса Facebook
from selenium import webdriver
from src.endpoints.advertisement.facebook.facebook import Facebook

# Инициализация веб-драйвера (пример для Chrome)
driver = webdriver.Chrome()

# Создание экземпляра класса Facebook
facebook_instance = Facebook(driver=driver, promoter='my_promoter', group_file_paths=['path/to/group_file.txt'])
```

## Функции

### `login`

```python
def login(self) -> bool:
    """
    Выполняет вход в Facebook.

    Returns:
        bool: `True`, если вход выполнен успешно, иначе `False`.
    """
```

**Описание**: Функция выполняет вход в Facebook.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Примеры**:
```python
# Пример вызова функции login
from selenium import webdriver
from src.endpoints.advertisement.facebook.facebook import Facebook

# Инициализация веб-драйвера
driver = webdriver.Chrome()
facebook_instance = Facebook(driver=driver, promoter='my_promoter', group_file_paths=['path/to/group_file.txt'])

if facebook_instance.login():
    print('Вход выполнен успешно')
else:
    print('Ошибка при входе')
```

### `promote_post`

```python
def promote_post(self, item: SimpleNamespace) -> bool:
    """
    Функция отправляет текст в форму сообщения для продвижения поста.
    @param message: сообщение текстом. Знаки `;` будут заменеы на `SHIFT+ENTER`
    @returns `True`, если успешно, иначе `False`
    """
```

**Описание**: Функция отправляет текст в форму сообщения для продвижения поста.

**Параметры**:
- `item` (SimpleNamespace): Объект с данными для продвижения поста.

**Возвращает**:
- `bool`: `True`, если отправка выполнена успешно, иначе `False`.

**Примеры**:
```python
# Пример вызова функции promote_post
from selenium import webdriver
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.facebook import Facebook

# Инициализация веб-драйвера
driver = webdriver.Chrome()
facebook_instance = Facebook(driver=driver, promoter='my_promoter', group_file_paths=['path/to/group_file.txt'])

# Создание объекта SimpleNamespace с данными для поста
item = SimpleNamespace(message='Текст сообщения для продвижения')

if facebook_instance.promote_post(item):
    print('Пост успешно отправлен')
else:
    print('Ошибка при отправке поста')
```

### `promote_event`

```python
def promote_event(self, event: SimpleNamespace):
    """ Пример функции для продвижения события """
```

**Описание**: Функция для продвижения события.

**Параметры**:
- `event` (SimpleNamespace): Объект с данными о событии для продвижения.

**Примеры**:
```python
# Пример вызова функции promote_event
from selenium import webdriver
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.facebook import Facebook

# Инициализация веб-драйвера
driver = webdriver.Chrome()
facebook_instance = Facebook(driver=driver, promoter='my_promoter', group_file_paths=['path/to/group_file.txt'])

# Создание объекта SimpleNamespace с данными о событии
event = SimpleNamespace(name='Название события', description='Описание события')

facebook_instance.promote_event(event)
print('Запрос на продвижение события отправлен')