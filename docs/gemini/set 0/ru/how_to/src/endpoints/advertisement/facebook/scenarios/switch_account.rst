Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Функция `switch_account` предназначена для переключения аккаунтов в Facebook. Она ищет на странице кнопку "Переключить" и, если находит, нажимает на неё.  Функция использует предопределённые локейторы, загруженные из файла `post_message.json`.

Шаги выполнения
-------------------------
1. Функция `switch_account` принимает объект `driver` (драйвер веб-драйвера), который предоставляет доступ к взаимодействию с веб-страницей.
2. Она использует метод `execute_locator` объекта `driver` для нахождения и нажатия на элемент, соответствующий локейтору `switch_to_account_button`, который загружен из файла `post_message.json`.


Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from types import SimpleNamespace
    from src import gs
    from src.webdriver import Driver
    from src.utils import j_loads_ns
    from hypotez.src.endpoints.advertisement.facebook.scenarios.switch_account import switch_account

    # ... (Инициализация драйвера и другие необходимые переменные) ...

    # Пример:
    driver: Driver = Driver(url='https://www.facebook.com/something')
    locator = j_loads_ns(Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json'))
    switch_account(driver)

    # ... (Дальнейшие действия после переключения аккаунта) ...