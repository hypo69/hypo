Как использовать этот блок кода
=========================================================================================\n

Описание
-------------------------
Этот модуль (`hypotez/src/webdriver/js.py`) предоставляет функции для взаимодействия с веб-страницей через JavaScript, расширяя возможности Selenium WebDriver.  Он позволяет делать невидимые элементы DOM видимыми, получать метаданные о странице (состояние загрузки, URL реферера, язык) и управлять фокусом браузера.


Шаги выполнения
-------------------------
1. **Импортирование модуля:**  Импортируйте класс `JavaScript` из файла `hypotez/src/webdriver/js.py`.
2. **Создание экземпляра:** Создайте экземпляр класса `JavaScript`, передав в конструктор объект `WebDriver` из Selenium.
3. **Использование методов:**  Вызовите нужные методы класса `JavaScript` для выполнения действий с веб-страницей через JavaScript.  Например:

    * `unhide_DOM_element(element)`: Сделает элемент `WebElement` видимым, изменяя его свойства стиля.
    * `ready_state`: Получит текущее состояние загрузки страницы (loading или complete).
    * `window_focus()`: Переведет фокус на окно браузера.
    * `get_referrer()`: Получит URL предыдущей страницы (referrer).
    * `get_page_lang()`: Получит язык страницы.


4. **Обработка ошибок:** Обратите внимание на использование блоков `try...except`, которые обрабатывают возможные исключения при выполнении JavaScript-кода.  Это важно, так как некоторые операции могут не удаться из-за разного поведения веб-страниц.  Модуль записывает сообщения об ошибках в лог.


Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from hypotez.src.webdriver.js import JavaScript

    # ... (Инициализация драйвера Selenium) ...

    driver = webdriver.Chrome()
    js_helper = JavaScript(driver)

    # Находим элемент, который нужно сделать видимым
    element = driver.find_element("xpath", "//some/xpath/to/your/element")

    # Делаем элемент видимым
    is_unhidden = js_helper.unhide_DOM_element(element)
    if is_unhidden:
        print("Элемент успешно сделан видимым")
    else:
        print("Не удалось сделать элемент видимым")

    # Получаем состояние загрузки
    ready_state = js_helper.ready_state
    print(f"Состояние загрузки: {ready_state}")

    # Переводим фокус на окно браузера
    js_helper.window_focus()

    # Получаем URL предыдущей страницы (referrer)
    referrer_url = js_helper.get_referrer()
    print(f"URL предыдущей страницы: {referrer_url}")

    # Получаем язык страницы
    page_lang = js_helper.get_page_lang()
    print(f"Язык страницы: {page_lang}")

    # ... (Закрытие драйвера) ...
    driver.quit()