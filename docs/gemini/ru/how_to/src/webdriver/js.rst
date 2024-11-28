Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет класс `JavaScript`, который расширяет возможности Selenium WebDriver, добавляя функции для взаимодействия с веб-страницей через JavaScript.  Он позволяет делать невидимые элементы DOM видимыми, получать метаданные страницы (состояние загрузки, referrer, язык) и управлять фокусом браузера.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек**: Код импортирует нужные модули: `header`, `gs`, `logger` из `src`, `WebDriver` и `WebElement` из `selenium.webdriver`.

2. **Класс `JavaScript`**: Определяется класс `JavaScript`, предоставляющий методы для взаимодействия с веб-страницей через JavaScript.

3. **Конструктор `__init__`**: В конструкторе инициализируется `self.driver` - экземпляр `WebDriver` для выполнения JavaScript-кода.

4. **`unhide_DOM_element`**: Этот метод делает невидимый элемент DOM видимым, изменяя его свойства стиля (opacity, transform). Он использует `driver.execute_script` для выполнения JavaScript-кода.  Возвращает `True` при успешном выполнении и `False` в случае ошибки.

5. **`ready_state`**:  Свойство, возвращающее текущее состояние загрузки документа. Использует `driver.execute_script` для получения значения `document.readyState`. Возвращает `'loading'` или `'complete'`.

6. **`window_focus`**: Метод, устанавливающий фокус на окно браузера через JavaScript.  Использует `driver.execute_script('window.focus();')`.

7. **`get_referrer`**: Метод для получения URL referrer текущей страницы. Возвращает ссылку referrer или пустую строку, если она недоступна.

8. **`get_page_lang`**: Метод, возвращающий язык текущей страницы, используя `document.documentElement.lang`. Возвращает язык или пустую строку.

9. **Обработка ошибок**:  Все методы содержат обработку исключений (`try...except`) для логгирования ошибок при взаимодействии с JavaScript.  Это важно для надежности кода.

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from hypotez.src.webdriver import js

    # ... (создание драйвера и навигация по странице) ...

    driver = webdriver.Chrome()
    driver.get("https://example.com")

    js_helper = js.JavaScript(driver)

    # Находим элемент, который нужно сделать видимым
    element_to_unhide = driver.find_element("xpath", "//some/element")

    # Делаем элемент видимым
    if js_helper.unhide_DOM_element(element_to_unhide):
        print("Элемент успешно сделан видимым")
    else:
        print("Не удалось сделать элемент видимым")


    # Получаем состояние загрузки документа
    document_ready_state = js_helper.ready_state
    print(f"Состояние загрузки документа: {document_ready_state}")

    # Устанавливаем фокус на окно браузера
    js_helper.window_focus()

    # ... (дополнительные операции с веб-страницей) ...

    driver.quit()