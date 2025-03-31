# Модуль login

## Обзор

Модуль `login.py` предназначен для реализации интерфейса авторизации с использованием веб-драйвера для поставщика CData. Он содержит функцию `login`, которая выполняет вход в систему CData через веб-интерфейс.

## Подробней

Этот модуль предоставляет функциональность для автоматизации процесса входа на сайт CData. Он использует локаторы элементов веб-страницы для заполнения полей электронной почты и пароля, а также для нажатия кнопки входа. Функция `login` возвращает `True` после успешного входа в систему.

## Функции

### `login`

```python
def login(self):
    """
    Выполняет вход в систему CData через веб-интерфейс.

    Args:
        self: Экземпляр класса, содержащего информацию о локаторах и методы для взаимодействия с веб-драйвером.

    Returns:
        bool: `True` в случае успешного входа в систему.

    Raises:
        Exception: Если возникает ошибка при входе в систему.

    Example:
        >>> login(self)
        True
    """
    self.get_url('https://reseller.c-data.co.il/Login')

    emaiocators['login']['email']
    password = self.locators['login']['password']

    email_locator = (self.locators['login']['email_locator']['by'], 
                        self.locators['login']['email_locator']['selector'])

    password_locator = (self.locators['login']['password_locator']['by'],
                            self.locators['login']['password_locator']['selector'])

    loginbutton_locator =  (self.locators['login']['loginbutton_locator']['by'],
                                self.locators['login']['loginbutton_locator']['selector'])


    self.print(f''' email_locator {email_locator}
            password_locator {password_locator}
            loginbutton_locator {loginbutton_locator}''')

    self.find(email_locator).send_keys(email)
    self.find(password_locator).send_keys(password)
    self.find(loginbutton_locator).click()
    self.log('C-data logged in')
    return True
```

**Как работает функция:**

1.  Переходит по URL-адресу страницы входа CData (`https://reseller.c-data.co.il/Login`).
2.  Извлекает email и пароль из `self.locators`.
3.  Определяет локаторы для полей email, пароля и кнопки входа. Локаторы используются для поиска соответствующих элементов на веб-странице.
4.  Выводит локаторы в консоль.
5.  Находит поле email с помощью `email_locator` и вводит email.
6.  Находит поле пароля с помощью `password_locator` и вводит пароль.
7.  Находит кнопку входа с помощью `loginbutton_locator` и нажимает на неё.
8.  Записывает сообщение в лог об успешном входе.
9.  Возвращает `True`.

**Параметры:**

*   `self`: Экземпляр класса, содержащего методы для взаимодействия с веб-драйвером и локаторы элементов страницы входа.

**Возвращает:**

*   `bool`: `True` в случае успешного входа в систему.

**Вызывает исключения:**

*   `Exception`: Если возникает ошибка при входе в систему, например, если не удалось найти элементы страницы или произошла ошибка при вводе данных.

**Примеры:**

```python
# Пример вызова функции login
login(self)
```