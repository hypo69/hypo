Как использовать модуль `hypotez/src/scenario/__init__.py`
=========================================================================================

Описание
-------------------------
Модуль `hypotez/src/scenario/__init__.py` содержит функции для выполнения сценариев (scenarios) поставщиков (suppliers).  Он определяет логику для взаимодействия с поставщиком (например, AliExpress), драйвером и целевой системой (например, PrestaShop).  Модуль предоставляет функции для работы с файлами сценариев и сценариями в виде словарей.

Шаги выполнения
-------------------------
1. **Инициализация поставщика:** Создается объект `Supplier` с указанием имени поставщика (например, `'aliexpress'`):
   ```python
   s = Supplier('aliexpress')
   ```

2. **Выполнение сценариев из файла:**
   - Передача имени файла сценария функции `run_scenario_files` для выполнения сценариев, определённых в файле.
   ```python
   run_scenario_files(s, 'file1')
   ```
   - Передача списка имён файлов сценариев функции `run_scenario_files` для выполнения сценариев из каждого файла.
   ```python
   scenario_files = ['file1', 'file2']
   run_scenario_files(s, scenario_files)
   ```
3. **Выполнение сценариев из словаря:**
   - Передача словаря сценария функции `run_scenarios` для выполнения сценария, определённого в словаре.
   ```python
   scenario1 = {'key': 'value'}
   run_scenarios(s, scenario1)
   ```
   - Передача списка словарей сценариев функции `run_scenarios` для выполнения сценариев из каждого словаря.
   ```python
   list_of_scenarios = [scenario1, scenario2]
   run_scenarios(s, list_of_scenarios)
   ```

4. **Использование методов объекта `Supplier`:**

   - Можно вызвать метод `run()` объекта `Supplier`, что выполнит все ранее заданные сценарии:
   ```python
   s.run()
   ```
   - Аналогично, можно выполнить отдельные сценарии, передавая им имена файлов или словари сценариев:
   ```python
   s.run('file1')
   s.run(scenario1)
   s.run(scenario_files)
   s.run(list_of_scenarios)
   ```

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.scenario import Supplier, run_scenario_files
    # Предполагая, что Supplier и run_scenario_files определены в другом модуле


    # Инициализация поставщика
    s = Supplier('aliexpress')

    # Выполнение сценариев из файла
    run_scenario_files(s, 'scenario_file.json')

    # Выполнение сценариев из списка файлов
    scenario_files = ['scenario1.json', 'scenario2.json']
    run_scenario_files(s, scenario_files)

    #Пример сценария в формате JSON
    scenario_data = {
        "scenarios": {
            "example_scenario": {
                "url": "https://example.com",
                "name": "Example Scenario"
            }
        }
    }
    # Выполнение сценария из словаря
    run_scenarios(s, scenario_data)