Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Функция `login(d: Driver) -> bool` предназначена для авторизации пользователя на Facebook. Она принимает экземпляр класса `Driver` для взаимодействия с веб-элементами и использует данные из файла конфигурации для заполнения полей логина и пароля, а затем нажимает кнопку входа. Функция возвращает `True`, если авторизация прошла успешно, и `False` в противном случае.  Она обрабатывает возможные исключения, связанные с ошибками ввода данных и нажатия кнопок.

Шаги выполнения
-------------------------
1. **Загрузка локаторов:** Функция загружает локаторы (данные о расположении элементов на странице Facebook) из файла `login.json`.  Путь к файлу определяется переменной `gs.path.src`.
2. **Проверка локаторов:** Проверяет, что локаторы были успешно загружены. Если нет, выводит сообщение об ошибке в лог.
3. **Получение учетных данных:** Извлекает данные для авторизации (`username` и `password`) из переменной `gs.facebook_credentials`.
4. **Ввод логина:** Используя метод `d.send_key_to_webelement`, заполняет поле логина на странице Facebook указанными учетными данными.  Обрабатывает возможные исключения при заполнении.
5. **Ожидание (логин):** Продолжает выполнение с небольшим задержкой `d.wait(1.3)`, давая время браузеру обновить страницу.
6. **Ввод пароля:** Используя метод `d.send_key_to_webelement`, заполняет поле пароля на странице Facebook указанными учетными данными.  Обрабатывает возможные исключения при заполнении.
7. **Ожидание (пароль):** Продолжает выполнение с задержкой `d.wait(0.5)`.
8. **Нажатие кнопки входа:** Используя метод `d.execute_locator`, нажимает кнопку входа.  Обрабатывает возможные исключения при нажатии.
9. **Возврат результата:** Возвращает `True`, если все шаги выполнены без ошибок, `False` - если произошла ошибка на любом этапе.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver import Driver
    from hypotez.src.endpoints.advertisement.facebook.scenarios.login import login

    # Создаем экземпляр драйвера (например, для Chrome)
    driver = Driver(browser_type='chrome')

    # Авторизуем пользователя
    is_logged_in = login(driver)

    if is_logged_in:
        print("Успешная авторизация!")
    else:
        print("Ошибка авторизации.")

    # Закрываем браузер
    driver.quit()