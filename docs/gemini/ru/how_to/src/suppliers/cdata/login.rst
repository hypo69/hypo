Как использовать функцию login
========================================================================================

Описание
-------------------------
Функция `login(self)` предназначена для авторизации в системе C-Data через веб-драйвер. Она переходит на страницу входа, заполняет поля email и пароль, а затем нажимает кнопку входа.  Функция возвращает True, если авторизация успешна.  Функция предполагает, что `self` содержит объект веб-драйвера с методами `get_url`, `find`, `send_keys`, `click`, `print`, `log`, и атрибутом `locators`. В атрибуте `locators` хранится информация о локаторах элементов на странице входа (email, пароль, кнопка входа).

Шаги выполнения
-------------------------
1. Функция `get_url('https://reseller.c-data.co.il/Login')` переходит на страницу входа в систему C-Data.
2. Функция получает значения email и пароля из словаря `self.locators['login']`.
3. Функция получает локаторы (способ и селектор) для полей email, пароля и кнопки входа из словаря `self.locators['login']`.
4.  Функция выводит информацию о локаторах в консоль.
5. Функция заполняет поле email с помощью `self.find(email_locator).send_keys(email)`.
6. Функция заполняет поле пароля с помощью `self.find(password_locator).send_keys(password)`.
7. Функция нажимает кнопку входа с помощью `self.find(loginbutton_locator).click()`.
8. Функция записывает сообщение "C-data logged in" в лог.
9. Функция возвращает значение True.


Пример использования
-------------------------
.. code-block:: python

    # Предполагается, что driver - это объект веб-драйвера
    # и locators содержит необходимую информацию для авторизации
    import time
    from selenium import webdriver

    class MyWebdriver:
        def __init__(self):
            self.driver = webdriver.Chrome()
            self.locators = {
                'login': {
                    'email': 'your_email',
                    'password': 'your_password',
                    'email_locator': {'by': 'id', 'selector': 'email_field_id'},
                    'password_locator': {'by': 'id', 'selector': 'password_field_id'},
                    'loginbutton_locator': {'by': 'id', 'selector': 'login_button_id'},
                }
            }
        def get_url(self, url):
          self.driver.get(url)
          time.sleep(5)  # Важно для загрузки страницы
        def find(self, locator):
            return self.driver.find_element(*locator)
        def send_keys(self, element, text):
            element.send_keys(text)
        def click(self, element):
            element.click()
        def print(self, text):
            print(text)
        def log(self, text):
            print(text)


    driver = MyWebdriver()
    success = driver.login()
    if success:
        print("Авторизация успешна!")
    else:
        print("Ошибка авторизации.")