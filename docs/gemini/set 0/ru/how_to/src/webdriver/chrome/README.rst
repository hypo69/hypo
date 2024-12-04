Как использовать DevTools Protocol через WebDriver для Chrome
============================================================================================

Описание
-------------------------
Этот фрагмент кода демонстрирует, как использовать DevTools Protocol через WebDriver для Chrome, чтобы выполнять задачи, недоступные стандартными методами WebDriver.  Это позволяет, например, анализировать производительность, навигировать по страницам или управлять сетевыми запросами. Пример использует Selenium и WebDriver для Chrome.

Шаги выполнения
-------------------------
1. **Установка ChromeDriver:**  Убедитесь, что ChromeDriver установлен и доступен из текущей директории или укажите корректный путь к нему в переменной `service`.
2. **Настройка ChromeOptions:** Создайте объект `ChromeOptions` и добавьте аргумент `--remote-debugging-port=9222`. Этот аргумент активирует режим удаженной отладки, необходимый для взаимодействия с DevTools Protocol.
3. **Запуск Chrome:** Запустите Chrome с заданными параметрами, используя `webdriver.Chrome(service=service, options=chrome_options)`. Это инициализирует WebDriver для взаимодействия с Chrome.
4. **Получение сессии DevTools:** Используйте `driver.execute_cdp_cmd('Page.enable', {})`, чтобы получить сессию DevTools. Эта команда активирует определённые возможности DevTools для текущей сессии.
5. **Выполнение команд DevTools Protocol:** Используйте `driver.execute_cdp_cmd('Page.navigate', {'url': 'https://www.example.com'})`, чтобы выполнить команду DevTools Protocol. Замените `https://www.example.com` на необходимый URL. Эта команда перенаправляет браузер на заданный URL.
6. **Обработка ответа:** Обработайте ответ, возвращаемый командой DevTools Protocol, для анализа результата выполнения.
7. **Закрытие браузера:** Закройте браузер с помощью `driver.quit()`, чтобы освободить ресурсы.


Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options

    # Укажите путь к ChromeDriver
    service = Service('/path/to/chromedriver')

    # Настройка ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument('--remote-debugging-port=9222')

    # Запуск Chrome с заданными опциями
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Получение сессии DevTools
    dev_tools = driver.execute_cdp_cmd('Page.enable', {})

    # Выполнение команды DevTools Protocol
    response = driver.execute_cdp_cmd('Page.navigate', {'url': 'https://www.example.com'})
    print(response)

    # Закрытие браузера
    driver.quit()