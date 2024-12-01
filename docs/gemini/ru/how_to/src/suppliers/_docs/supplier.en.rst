Как использовать класс Supplier
========================================================================================

Описание
-------------------------
Класс `Supplier` служит базовым классом для управления поставщиками данных в приложении. Он предоставляет фреймворк для взаимодействия с различными источниками данных, такими как Amazon, AliExpress, Walmart и другими. Этот класс обрабатывает инициализацию настроек, специфичных для поставщика, управляет сценариями сбора данных и предоставляет методы для входа и выполнения сценариев.

Шаги выполнения
-------------------------
1. **Инициализация объекта:** Создайте экземпляр класса `Supplier`, передав в конструктор `__init__` необходимые параметры, такие как префикс поставщика (`supplier_prefix`), локаль (`locale`) и драйвер веб-драйвера (`webdriver`). Пример:
   ```python
   supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
   ```

2. **Загрузка конфигурации:** Вызовите метод `_payload`, чтобы загрузить конфигурационные файлы, специфичные для поставщика (настройки, локеры). Этот метод также инициализирует веб-драйвер.
   ```python
   supplier._payload(webdriver='chrome')
   ```

3. **Вход (аутентификация):** Выполните вход на сайт поставщика, используя метод `login`.
   ```python
   supplier.login()
   ```

4. **Выполнение сценариев:** Используйте методы `run_scenario_files` или `run_scenarios`, чтобы запустить сценарии сбора данных.
   - `run_scenario_files` принимает список имен файлов со сценариями. Пример:
     ```python
     supplier.run_scenario_files(['example_scenario.json'])
     ```
   - `run_scenarios` принимает список словарей со сценариями, где каждый словарь описывает действия. Пример:
     ```python
     supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
     ```

Пример использования
-------------------------
.. code-block:: python

    from your_module import Supplier  # Замените 'your_module' на фактический модуль
    from selenium import webdriver # Если используете Selenium

    # Создаем экземпляр класса Supplier для AliExpress
    supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

    # Загружаем конфигурацию
    supplier._payload(webdriver=webdriver.Chrome())

    # Вход на сайт поставщика
    supplier.login()

    # Выполнение сценария из файла
    supplier.run_scenario_files(['example_scenario.json'])

    # Или выполнение определённых сценариев
    supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])