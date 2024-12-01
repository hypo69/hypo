Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит набор тестов для класса `AliPromoCampaign`, предназначенного для работы с кампаниями на AliExpress. Тесты проверяют различные методы класса, такие как инициализация кампании, получение данных о продуктах, создание пространств имен для продуктов, категорий и кампании, обработку продуктов, загрузку данных о продуктах, сохранение данных о продуктах и вывод списка названий продуктов кампании.  Тесты используют фреймворк `pytest` и `mocking` для проверки работы методов в различных сценариях (например, с пустым набором файлов JSON или с наличием данных).

Шаги выполнения
-------------------------
1. **Импорт необходимых библиотек:** Код импортирует необходимые библиотеки, включая `pytest`, `pathlib`, `types`, класс `AliPromoCampaign`, функции `j_dumps`, `j_loads_ns`, `save_text_file`, и модуль `gs` из проекта.
2. **Определение фикстуры `campaign`:**  Создается фикстура `campaign`, которая возвращает экземпляр класса `AliPromoCampaign` с заданными параметрами (имя кампании, категория, язык и валюта). Это позволяет использовать один и тот же экземпляр кампании во всех тестах.
3. **Определение тестов:** Код содержит различные тесты для проверки методов класса `AliPromoCampaign`.
    - `test_initialize_campaign`: Проверяет корректную инициализацию данных кампании.
    - `test_get_category_products_no_json_files`: Проверяет метод `get_category_products` в случае отсутствия файлов JSON.
    - `test_get_category_products_with_json_files`: Проверяет метод `get_category_products` в случае наличия файлов JSON.
    - `test_create_product_namespace`, `test_create_category_namespace`, `test_create_campaign_namespace`: Проверяют корректное создание пространств имен для продуктов, категорий и кампании.
    - `test_prepare_products`: Проверяет, что метод `prepare_products` вызывает метод `process_affiliate_products`.
    - `test_fetch_product_data`: Проверяет корректную загрузку данных о продуктах.
    - `test_save_product`: Проверяет корректное сохранение данных о продуктах.
    - `test_list_campaign_products`: Проверяет корректный вывод списка названий продуктов кампании.
4. **Мокинг:** В тестах используется `mocking` для имитации поведения внешних функций, таких как `get_filenames`, `j_loads_ns` и `fetch_product_data`. Это позволяет проверить внутреннюю логику класса `AliPromoCampaign`, изолировав его от внешних зависимостей.
5. **Проверка результатов:**  Каждый тест проверяет, соответствуют ли полученные результаты ожидаемым значениям с помощью `assert`.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    from pathlib import Path
    from types import SimpleNamespace
    from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
    from src.utils import j_dumps, j_loads_ns
    # ... (другие импорты)


    # ... (определение фикстуры campaign, как в примере кода)


    def test_example_using_campaign(campaign):
        # Пример использования метода get_category_products
        products = campaign.get_category_products(force=True)
        assert len(products) == 0  # Проверяем, что список продуктов пуст, если нет JSON файлов