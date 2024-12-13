# Модуль `login.py`

## Обзор

Модуль `login.py` содержит реализацию интерфейса авторизации для веб-драйвера, предназначенного для работы с сайтом C-data.

## Оглавление

1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`login`](#login)

## Функции

### `login`

**Описание**:
Осуществляет вход на сайт C-data, используя предоставленные email и пароль.

**Параметры**:
- `self`: Экземпляр класса, в котором определен метод.

**Возвращает**:
- `bool`: Возвращает `True` после успешной авторизации.

**Вызывает исключения**:
- Отсутствуют явные исключения.

```python
def login(self):
    """
    Args:
        self: Экземпляр класса, в котором определен метод.

    Returns:
        bool: Возвращает `True` после успешной авторизации.
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