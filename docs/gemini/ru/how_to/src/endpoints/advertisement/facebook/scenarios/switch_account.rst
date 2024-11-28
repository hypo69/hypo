Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Функция `switch_account` предназначена для переключения между учетными записями в Facebook.  Она ищет и нажимает кнопку "Переключить" на странице, если такая кнопка присутствует.

Шаги выполнения
-------------------------
1. Функция `switch_account` принимает объект `driver` типа `Driver` в качестве аргумента. Объект `driver` представляет собой драйвер браузера, используемый для взаимодействия с веб-сайтом.

2. Функция `driver.execute_locator(locator.switch_to_account_button)` выполняет поиск элемента на странице, соответствующего локатору `locator.switch_to_account_button`. Локатор загружен из файла `post_message.json` в папке `locators`.

3. Если элемент с указанным локатором найден, функция выполняет клик по нему, тем самым переключаясь между учетными записями.  Если элемент не найден, никакой операции не выполняется.

Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from types import SimpleNamespace
    from src import gs
    from src.webdriver import Driver
    from src.utils import j_loads_ns
    from hypotez.src.endpoints.advertisement.facebook.scenarios.switch_account import switch_account  # Импортируем функцию

    # Пример создания объекта Driver (замените на ваш способ создания драйвера)
    driver = Driver()
    driver.get("адрес_страницы_facebook")  #  Загрузить страницу, где есть кнопка "Переключить"
    locator: SimpleNamespace = j_loads_ns(
        Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
    )

    switch_account(driver)