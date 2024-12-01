Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот документ описывает, как запустить и выполнить тесты, расположенные в файле `test_driver_executor.py`.  Данные тесты проверяют функциональность классов `Driver` и `ExecuteLocator`, а также взаимодействие между ними. Документ содержит инструкции по установке зависимостей, настройке WebDriver, запуску тестов, а также описание каждого теста и ожидаемого результата.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
   - Убедитесь, что на вашем компьютере установлены необходимые библиотеки. Выполните команду в терминале:

     .. code-block:: bash
        pip install -r requirements.txt

   - Эта команда устанавливает все зависимости, перечисленные в файле `requirements.txt`, включая `pytest` и `selenium`.

2. **Настройка WebDriver:**
   - Тесты используют Chrome WebDriver. Убедитесь, что у вас установлен ChromeDriver.
   - Найдите и запишите путь к исполняемому файлу `chromedriver` в вашем проекте.
   - В файле `test_driver_executor.py` замените `/path/to/chromedriver` на фактический путь к вашему файлу `chromedriver`:

     .. code-block:: python
        from selenium.webdriver.chrome.service import Service
        service = Service(executable_path="/path/to/chromedriver")

3. **Запуск тестов:**
   - Откройте терминал и перейдите в директорию проекта.
   - Используйте команду `pytest` для запуска тестов:

     .. code-block:: bash
        pytest src/webdriver/_pytest/test_driver_executor.py

   - Эта команда выполнит все тесты, определенные в файле `test_driver_executor.py`.


4. **Просмотр отчета:**
   - После запуска тестов вы увидите результат в терминале. Для получения более подробной информации (в том числе прохождения и проваленных тестов), используйте флаги командной строки:

     - Для текстового отчета:

       .. code-block:: bash
         pytest src/webdriver/_pytest/test_driver_executor.py -v

     - Для HTML отчета (установив сначала `pytest-html`):

       .. code-block:: bash
         pip install pytest-html
         pytest src/webdriver/_pytest/test_driver_executor.py --html=report.html

     HTML отчет будет сохранен в файле `report.html`.


Пример использования
-------------------------
.. code-block:: python

    # Пример кода из файла test_driver_executor.py (фрагмент)
    # (Подразумевается, что необходимые импорты и setup уже выполнены)

    def test_navigate_to_page(driver):
        driver.get("http://example.com")
        assert driver.current_url == "http://example.com"