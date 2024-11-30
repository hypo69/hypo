Как использовать модуль `src.scenario` для автоматизации взаимодействия с поставщиками
=====================================================================================

Описание
-------------------------
Модуль `src.scenario` автоматизирует взаимодействие с поставщиками, используя сценарии, описанные в JSON-файлах.  Он предназначен для извлечения и обработки данных о продуктах с веб-сайтов поставщиков и синхронизации этой информации с базой данных вашей системы (например, PrestaShop).

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `Supplier`, передав в качестве аргумента название поставщика (например, 'aliexpress').

2. **Запуск сценариев:**
    - **Запуск из списка файлов:** Передайте список путей к JSON-файлам со сценариями функции `run_scenario_files`.
      ```python
      scenario_files = [Path("path/to/scenario1.json"), Path("path/to/scenario2.json")]
      s = Supplier('aliexpress')
      s.run_scenario_files(scenario_files)
      ```
    - **Запуск из одного файла:** Передайте путь к JSON-файлу функции `run_scenario_file`.
      ```python
      scenario_file = Path("path/to/scenario.json")
      s = Supplier('aliexpress')
      s.run_scenario_file(scenario_file)
      ```
    - **Запуск одиночного сценария:** Передайте словарь со сценарием напрямую функции `run_scenarios` или `run`.
      ```python
      scenario = {'url': 'http://example.com/category1', 'name': 'CategoryName'}
      s = Supplier('aliexpress')
      s.run_scenarios([scenario])
      ```
    - **Запуск списка сценариев:** Передайте список словарей со сценариями функции `run_scenarios`.

3. **Обработка сценариев:**  Модуль последовательно обрабатывает каждый сценарий, извлекая данные о продуктах с указанных веб-страниц и сохраняя их в базе данных PrestaShop, используя информацию о категориях из сценария.

4. **Логирование:** Модуль ведёт журнал выполнения сценариев, фиксируя детали выполнения и результаты, что позволяет отслеживать успех и идентифицировать ошибки.  Вы можете просмотреть журнал, используя функцию `dump_journal`.


Пример использования
-------------------------
.. code-block:: python

    from pathlib import Path
    from your_module import Supplier  # Замените 'your_module' на фактическое имя модуля

    # Создаем экземпляр класса Supplier
    s = Supplier('aliexpress')

    # Путь к файлу со сценарием
    scenario_file = Path("path/to/scenario.json")

    # Запуск сценария из файла
    s.run_scenario_file(scenario_file)


    # Запуск списка сценариев
    scenarios = [
        {'url': 'https://hbdeadsea.co.il/product-category/facial/moisture-face/', 'name': 'Moisturizing'},
        {'url': 'https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/', 'name': 'Feet and Hands'},
    ]
    s.run_scenarios(scenarios)

    # Вывод журнала
    s.dump_journal(s.journal)