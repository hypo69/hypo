# Модуль `login`

## Обзор

Модуль `login.py` предназначен для реализации авторизации пользователя на сайте `reseller.c-data.co.il`. Он использует веб-драйвер для автоматизации процесса входа в систему, заполняя поля электронной почты и пароля, а также нажимая кнопку входа.

## Подробней

Этот модуль предоставляет функцию `login`, которая выполняет вход пользователя в систему C-data, используя предоставленные учетные данные и локаторы элементов на странице входа. Модуль использует атрибуты `self` для доступа к URL, локаторам элементов и методам веб-драйвера.

## Функции

### `login`

```python
def login(self):
    """
    Выполняет авторизацию пользователя на сайте reseller.c-data.co.il.

    Args:
        self: Объект класса, содержащий информацию о веб-драйвере, URL и локаторах элементов.

    Returns:
        bool: Возвращает True после успешной авторизации.

    Raises:
        Exception: Если возникает ошибка во время процесса авторизации.

    Как работает функция:
     1. Функция открывает страницу авторизации по URL `https://reseller.c-data.co.il/Login`.
     2. Извлекает локаторы для полей электронной почты, пароля и кнопки входа из атрибута `self.locators`.
     3. Находит элементы электронной почты и пароля на странице, используя извлеченные локаторы, и вводит соответствующие учетные данные.
     4. Находит кнопку входа, используя извлеченный локатор, и нажимает ее.
     5. Логирует успешную авторизацию.
     6. Возвращает `True` в случае успешной авторизации.

    Внутри функции происходят следующие действия и преобразования:

    A: Открытие страницы авторизации
    |
    -- B: Извлечение локаторов элементов
    |
    C: Ввод учетных данных
    |
    D: Нажатие кнопки входа
    |
    E: Логирование успешной авторизации

    Где:
    - Открытие страницы авторизации: Переход по URL `https://reseller.c-data.co.il/Login`.
    - Извлечение локаторов элементов: Получение данных о локаторах для полей ввода email и password, а также для кнопки login.
    - Ввод учетных данных: Поиск элементов на странице и заполнение полей email и password.
    - Нажатие кнопки входа: Поиск и клик по кнопке, инициирующей вход в систему.
    - Логирование успешной авторизации: Запись в лог информации об успешном входе в систему.
    """
    self.get_url('https://reseller.c-data.co.il/Login')

    email = self.locators['login']['email']
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