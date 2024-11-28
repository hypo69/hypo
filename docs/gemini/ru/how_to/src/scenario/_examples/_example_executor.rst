Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот файл (`hypotez/src/scenario/_examples/_example_executor.py`) содержит примеры использования модуля `executor` из пакета `src.scenario.executor`.  Примеры демонстрируют, как запускать сценарии, работать с файлами сценариев, взаимодействовать с API PrestaShop, включая добавление купонов и синхронную/асинхронную загрузку данных.

Шаги выполнения
-------------------------
1. **Импорт необходимых модулей**:  Код импортирует нужные библиотеки, такие как `asyncio`, `pathlib`, функции для работы со сценариями (`run_scenario_files`, `run_scenario_file`, `run_scenarios`, `run_scenario`), для работы с PrestaShop (`execute_PrestaShop_insert`, `execute_PrestaShop_insert_async`, `add_coupon`) и другие вспомогательные функции.

2. **Определение вспомогательных классов**:  Создаются имитации классов `MockSupplier`, `MockRelatedModules`, `MockDriver`, которые имитируют работу с данными для тестирования. Это важно для изоляции тестирования и упрощения примеров без реального взаимодействия с системами.

3. **Определение функций-примеров**:  Файл содержит функции `example_run_scenario_files`, `example_run_scenario_file`, `example_run_scenario`, `example_insert_grabbed_data`, `example_add_coupon` и т.д., демонстрирующие различные способы использования функций из модуля `executor`.

4. **Заполнение данных для примеров**: В примерах используются примерные данные, такие как пути к сценариям, URL, данные продукта, настройки API.

5. **Вызов функций-примеров**: Основная часть кода (`if __name__ == "__main__":`) выполняет примеры запуска сценариев и добавления купонов, а также запуск асинхронных операций.

6. **Обработка результатов**: Примеры проверяют результат выполнения и выводят соответствующие сообщения (успех или неудачу).

7. **Асинхронные операции**: В примере `example_execute_PrestaShop_insert_async` показано использование `asyncio.run` для выполнения асинхронной операции.


Пример использования
-------------------------
.. code-block:: python

    # Пример запуска сценариев из списка файлов
    def example_run_scenario_files():
        supplier = MockSupplier()
        scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
        result = run_scenario_files(supplier, scenario_files)
        if result:
            print("Все сценарии выполнены успешно.")
        else:
            print("Некоторые сценарии не выполнены.")


    # Пример запуска асинхронного добавления данных в PrestaShop
    async def example_execute_PrestaShop_insert_async():
        product_fields = ProductFields(
            presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
            assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'],
                               'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'})
        await execute_PrestaShop_insert_async(product_fields)
        print("Данные продукта добавлены в PrestaShop асинхронно.")


    # Запуск примеров
    if __name__ == "__main__":
        example_run_scenario_files()
        # ... (Другие примеры) ...
        asyncio.run(example_execute_PrestaShop_insert_async())