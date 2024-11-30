Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот файл содержит примеры использования модуля `executor` из пакета `src.scenario.executor`. Он демонстрирует, как запускать сценарии, обрабатывать файлы сценариев, взаимодействовать с API PrestaShop.  Примеры включают запуск списка файлов сценариев, одиночного файла, одиночного сценария, загрузки страницы продукта, добавления купона.  Файл предоставляет функции для выполнения различных задач:  запуск сценариев, работа с файлами сценариев, вставка данных, полученных со страниц продуктов, добавление купонов в PrestaShop.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:**  Код импортирует нужные модули, включая `run_scenario_files`, `run_scenario_file`, `run_scenarios`, `run_scenario`, `insert_grabbed_data`, `execute_PrestaShop_insert`, `execute_PrestaShop_insert_async`, `add_coupon` из модуля `src.scenario.executor`,  `j_loads` из `src.utils`, `ProductFields` из `src.product`, `PrestaShop` из `src.endpoints.PrestaShop`.
2. **Определение вспомогательных классов:** Вводятся классы `MockSupplier`, `MockRelatedModules`, `MockDriver`. Эти классы имитируют взаимодействия с внешними системами, такими как поставщик данных, модули, драйвер браузера, что позволяет тестировать и использовать код без необходимости подключения к реальным ресурсам.
3. **Определение функций-примеров:**  Код содержит несколько функций-примеров, демонстрирующих использование различных функций модуля `executor`.
   - `example_run_scenario_files`: Запуск списка файлов сценариев.
   - `example_run_scenario_file`: Запуск одного файла сценария.
   - `example_run_scenario`: Запуск одного сценария.
   - `example_insert_grabbed_data`: Вставка данных, полученных со страницы продукта, в PrestaShop.
   - `example_add_coupon`: Добавление купона в PrestaShop.
   - `example_execute_PrestaShop_insert_async`: Асинхронное выполнение вставки данных в PrestaShop.
   - `example_execute_PrestaShop_insert`: Синхронное выполнение вставки данных в PrestaShop.

4. **Вызов функций-примеров:** В блоке `if __name__ == "__main__":` выполняется вызов функций-примеров для демонстрации их работы.

Пример использования
-------------------------
.. code-block:: python

    # Пример использования функции example_run_scenario_files
    from hypotez.src.scenario._examples._example_executor import example_run_scenario_files
    example_run_scenario_files()

    # Пример использования функции example_add_coupon
    from hypotez.src.scenario._examples._example_executor import example_add_coupon
    example_add_coupon()