Как использовать класс Firefox
========================================================================================

Описание
-------------------------
Этот код определяет подкласс `webdriver.Firefox`, названный `Firefox`. Он предоставляет дополнительную функциональность, такую как запуск Firefox в режиме киоска и настройку профиля Firefox для WebDriver.  Код настраивает WebDriver Firefox, включая установку профиля, версии Firefox и geckodriver, а также пользовательского user-agent.  Он также инициализирует объекты для работы с JavaScript и исполнением локейтеров.

Шаги выполнения
-------------------------
1. **Импортирует необходимые библиотеки:** `os`, `Path`, `typing`, `selenium.webdriver`, `selenium.webdriver.firefox`, `selenium.webdriver.firefox.firefox_profile`, `selenium.common.exceptions`, `src.webdriver.executor`, `src.webdriver.js`, `fake_useragent`, `src`, `src.utils`, `src.logger`.  Это подключает нужные инструменты для работы с WebDriver, профилями, файлами, обработкой ошибок, JavaScript, user-agent и т.д.

2. **Определяет класс `Firefox`:** Наследуется от `webdriver.Firefox`, добавляя дополнительные атрибуты и методы.  Этот класс управляет настройками и запуском браузера Firefox.

3. **Инициализирует WebDriver:** Метод `__init__` принимает параметры для настройки профиля, версий Firefox и geckodriver, а также пользовательского user-agent.

4. **Настраивает `service`, `options` и `profile`:** Задает путь к geckodriver, двоичному файлу Firefox и директории профиля. Настраивает параметры `options` для браузера (например, аргументы командной строки). Устанавливает пользовательский user-agent.

5. **Запускает Firefox:** Использует `super().__init__(service=service, options=options)` для запуска браузера с настроенными параметрами.  Обрабатывает возможные исключения `WebDriverException` при старте браузера.

6. **Загружает `executors`:** Метод `_payload` загружает исполнители для locators и JavaScript, создавая объекты для последующего использования.

7. **Инициализирует дополнительные методы:**  Метод `_payload` создаёт и присваивает классу `Firefox` объекты, необходимые для работы с JavaScript (например, `get_page_lang`, `ready_state`) и локейтерами (например, `execute_locator`, `get_webelement_by_locator`).


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.webdriver.firefox.firefox import Firefox

    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"

    browser = Firefox(profile_name=profile_name, geckodriver_version=geckodriver_version, firefox_version=firefox_version)
    browser.get("https://www.example.com")
    browser.quit()