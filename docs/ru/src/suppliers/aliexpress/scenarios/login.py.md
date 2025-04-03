# Модуль для выполнения сценария входа в AliExpress

## Обзор

Модуль содержит функцию `login`, которая автоматизирует процесс входа пользователя на сайт AliExpress с использованием веб-драйвера. Модуль предназначен для интеграции с классом `Supplier`, который предоставляет необходимые параметры, такие как драйвер веб-браузера и локаторы элементов страницы.

## Подробней

Этот модуль выполняет сценарий входа на сайт AliExpress. Он использует веб-драйвер для взаимодействия с элементами на странице, такими как поля ввода email, пароля и кнопки входа.
Основная цель модуля - автоматизировать процесс входа пользователя в систему, что может быть полезно для задач, требующих авторизованного доступа к сайту AliExpress.

## Функции

### `login`

```python
def login(s) -> bool:
    """Выполняет вход на AliExpress через веб-драйвер.
    Args:
        s (Supplier): Класс поставщика с запущенным экземпляром веб-драйвера и настроенными локаторами.

    Returns:
        bool: Возвращает `True` в случае успешного входа (в текущей реализации всегда `True` для отладки).

    Raises:
        Exception: Если возникают ошибки при выполнении действий входа.

    Example:
        >>> from src.suppliers.aliexpress.aliexpress import Supplier
        >>> s = Supplier()
        >>> s.driver = # some webdriver instance
        >>> s.locators = {'login': {'cookies_accept': ..., 'open_login': ..., 'email_locator': ..., 'password_locator': ..., 'loginbutton_locator': ...}}
        >>> login(s)
        True
    """
```

**Назначение**: Функция автоматизирует процесс входа пользователя на сайт AliExpress с использованием веб-драйвера.

**Параметры**:
- `s` (Supplier): Класс поставщика с запущенным экземпляром веб-драйвера и настроенными локаторами.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешного входа (в текущей реализации всегда `True` для отладки).

**Как работает функция**:

1.  **Инициализация**: Функция получает экземпляр класса `Supplier`, содержащий настроенный веб-драйвер и локаторы элементов страницы.
2.  **Получение URL**: Загружает страницу AliExpress, используя метод `_d.get_url()`.
3.  **Выполнение действий**: Выполняет клики и ввод данных в поля email, пароля и кнопки входа, используя метод `_d.execute_locator()`.
4.  **Обработка ошибок**: В случае неуспешного выполнения какого-либо из действий входа, предусмотрена логика обработки ошибок (TODO).
5.  **Завершение**: После выполнения всех действий возвращает `True` (в текущей реализации для отладки).

**ASCII flowchart**:

```
    Supplier (s)
    |
    V
    Получение веб-драйвера (_d) и локаторов (_l)
    |
    V
    Загрузка страницы AliExpress (_d.get_url())
    |
    V
    Принятие cookies (_d.execute_locator(_l['cookies_accept']))
    |
    V
    Открытие формы входа (_d.execute_locator(_l['open_login']))
    |
    V
    Ввод email (_d.execute_locator(_l['email_locator']))
    |
    V
    Ввод пароля (_d.execute_locator(_l['password_locator']))
    |
    V
    Нажатие кнопки входа (_d.execute_locator(_l['loginbutton_locator']))
    |
    V
    Возврат True
```

**Примеры**:

```python
from src.suppliers.aliexpress.aliexpress import Supplier
import selenium.webdriver as WebDriver

# Создаем экземпляр класса Supplier (пример с Chrome)
s = Supplier()
s.driver = WebDriver.Chrome() # инициализация драйвера Chrome
s.locators = {
    'login': {
        'cookies_accept': {'by': 'XPATH', 'selector': '//button[@id="accept-cookies"]'},
        'open_login': {'by': 'XPATH', 'selector': '//a[@id="open-login-form"]'},
        'email_locator': {'by': 'XPATH', 'selector': '//input[@id="email"]'},
        'password_locator': {'by': 'XPATH', 'selector': '//input[@id="password"]'},
        'loginbutton_locator': {'by': 'XPATH', 'selector': '//button[@id="login-button"]'}
    }
}

# Выполняем вход
result = login(s)
print(result)  # Вывод: True
```
```python
from src.suppliers.aliexpress.aliexpress import Supplier
import selenium.webdriver as WebDriver

# Создаем экземпляр класса Supplier (пример с Firefox)
s = Supplier()
s.driver = WebDriver.Firefox() # инициализация драйвера Firefox
s.locators = {
    'login': {
        'cookies_accept': {'by': 'XPATH', 'selector': '//button[@id="accept-cookies"]'},
        'open_login': {'by': 'XPATH', 'selector': '//a[@id="open-login-form"]'},
        'email_locator': {'by': 'XPATH', 'selector': '//input[@id="email"]'},
        'password_locator': {'by': 'XPATH', 'selector': '//input[@id="password"]'},
        'loginbutton_locator': {'by': 'XPATH', 'selector': '//button[@id="login-button"]'}
    }
}

# Выполняем вход
result = login(s)
print(result)  # Вывод: True
```
```python
from src.suppliers.aliexpress.aliexpress import Supplier
import selenium.webdriver as WebDriver

# Создаем экземпляр класса Supplier (пример с Edge)
s = Supplier()
s.driver = WebDriver.Edge() # инициализация драйвера Edge
s.locators = {
    'login': {
        'cookies_accept': {'by': 'XPATH', 'selector': '//button[@id="accept-cookies"]'},
        'open_login': {'by': 'XPATH', 'selector': '//a[@id="open-login-form"]'},
        'email_locator': {'by': 'XPATH', 'selector': '//input[@id="email"]'},
        'password_locator': {'by': 'XPATH', 'selector': '//input[@id="password"]'},
        'loginbutton_locator': {'by': 'XPATH', 'selector': '//button[@id="login-button"]'}
    }
}

# Выполняем вход
result = login(s)
print(result)  # Вывод: True