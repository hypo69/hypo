Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот модуль предоставляет функции на JavaScript для взаимодействия с веб-страницей, расширяя возможности Selenium WebDriver. Он содержит методы для:  делания невидимых элементов DOM видимыми, получения метаданных (состояние загрузки документа, referrer, язык страницы), и управления фокусом браузера.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**: Модуль импортирует `header`, `gs`, `logger` из других частей проекта, а также `WebDriver` и `WebElement` из Selenium.
2. **Инициализация класса `JavaScript`**: Создается экземпляр класса `JavaScript`, принимая в качестве аргумента объект `WebDriver`. Это устанавливает соединение с браузером.
3. **Метод `unhide_DOM_element`**:  Переводит невидимый элемент DOM в видимое состояние, изменяя его свойства стиля (opacity, transform).
    - В качестве аргумента принимает `WebElement`.
    - Возвращает `True`, если выполнение скрипта прошло успешно, `False` - в противном случае.
4. **Свойство `ready_state`**: Возвращает текущее состояние загрузки документа ('loading' или 'complete').
5. **Метод `window_focus`**: Устанавливает фокус на окне браузера, переводит окно браузера на передний план.
6. **Метод `get_referrer`**: Возвращает URL referrer текущего документа.
7. **Метод `get_page_lang`**: Возвращает код языка текущей страницы.

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from hypotez.src.webdriver import js

    # ... (инициализация WebDriver)
    driver = webdriver.Chrome()

    # Пример использования функции unhide_DOM_element
    js_helper = js.JavaScript(driver)
    element = driver.find_element(By.ID, "myElement")  # Замените на ваш селектор
    success = js_helper.unhide_DOM_element(element)
    if success:
        print("Элемент успешно сделан видимым.")
    else:
        print("Ошибка при отображении элемента.")


    # Пример использования свойства ready_state
    ready_state = js_helper.ready_state
    print(f"Состояние загрузки документа: {ready_state}")


    # Пример использования get_referrer
    referrer = js_helper.get_referrer()
    print(f"Referrer: {referrer}")


    driver.quit()