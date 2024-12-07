Как использовать класс Firefox для работы с вебдрайвером
========================================================================================

Описание
-------------------------
Этот код определяет подкласс `webdriver.Firefox`, называемый `Firefox`. Он предоставляет расширенные возможности, такие как запуск Firefox в режиме киоска и настройку профиля Firefox для вебдрайвера.  Класс `Firefox` наследуется от `selenium.webdriver.Firefox` и добавляет функциональность для работы с профилем и настройками запуска браузера.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует необходимые библиотеки, такие как `pathlib`, `attr`, `os`, `selenium.webdriver`, `selenium.webdriver.firefox.options`, `selenium.webdriver.firefox.service`, `selenium.webdriver.firefox.firefox_profile`, `selenium.common.exceptions`, `gs`, `utils` и `logger`.  Эти импорты обеспечивают функционал для работы с путями, настройкой профилей, управления драйвером и логированием.
2. **Инициализация класса `Firefox`:**  Конструктор `__init__` принимает необязательный аргумент `user_agent` (словарь) для настройки пользовательского агента браузера. Если `user_agent` не предоставлен, используется случайный агент из библиотеки `fake_useragent`.
3. **Загрузка настроек:**  Загружаются настройки из файла `firefox.json` с помощью `j_loads_ns` и библиотеки `gs`, содержащие путь к geckodriver и профиль браузера.
4. **Настройка профиля:** Метод `_set_profile` создает объект `FirefoxProfile` с помощью указанного профиля.  Он определяет путь к профилю, учитывая возможные пути, содержащие переменную окружения `APPDATA`.
5. **Настройка параметров запуска:** Метод `_set_options` создает объект `Options` с настроенными параметрами запуска браузера (например, `headless`, параметры командной строки). Эти параметры задаются из настроек в `firefox.json`.
6. **Запуск браузера:** Используя загруженные настройки, запускается браузер Firefox с помощью родительского класса `super().__init__`.
7. **Обработка ошибок:**  Код содержит обработку исключений `WebDriverException` и общих ошибок `Exception` для перехвата возможных проблем при запуске браузера и последующей отладке.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.firefox import Firefox

    # Пример создания объекта Firefox с пользовательским агентом
    user_agent = {'user_agent': 'Mozilla/5.0'}
    driver = Firefox(user_agent=user_agent)

    #  ... дальнейшая работа с драйвером ...

    driver.quit()