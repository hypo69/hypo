Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит тесты для модуля `AliAffiliatedProducts`, отвечающего за обработку продуктов с аффилиатными ссылками с AliExpress.  Он проверяет корректность методов `check_and_process_affiliate_products` и `process_affiliate_products`. Код использует фикстуры для имитации внешних зависимостей и проверки результатов.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:**  Код импортирует модули `pytest`, `patch`, `MagicMock` из `unittest.mock`, класс `AliAffiliatedProducts` и `SimpleNamespace` из соответствующих файлов.
2. **Определение фикстуры `ali_affiliated_products`:**  Создается фикстура, которая возвращает экземпляр класса `AliAffiliatedProducts` с предопределенными параметрами кампании, категории, языка и валюты.
3. **Тестирование `check_and_process_affiliate_products`:**  Функция `test_check_and_process_affiliate_products` использует `patch` для подмены метода `process_affiliate_products` и проверки, что он был вызван с правильными аргументами (списком ссылок на продукты).
4. **Тестирование `process_affiliate_products`:** Функция `test_process_affiliate_products` использует `patch` для подмены методов `retrieve_product_details`, `ensure_https`, `save_png_from_url`, `save_video_from_url`, `j_dumps`. Эти методы имитируют работу внешних сервисов и функций. Внутри метода `process_affiliate_products` ожидается, что будет вызвана функция `retrieve_product_details`, которая вернет список деталей продукта, а затем обработанные данные будут сохранены. 
5. **Проверка результатов:**  В обоих тестах проверяются возвращаемые значения (количество обработанных продуктов, значения свойств продукта).
6. **Запуск тестов:**  В блоке `if __name__ == "__main__":` используется `pytest.main()` для запуска всех тестов.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    from unittest.mock import patch, MagicMock
    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
    from types import SimpleNamespace

    # Sample data (replace with your actual values)
    campaign_name = "sample_campaign"
    category_name = "sample_category"
    language = "EN"
    currency = "USD"
    prod_urls = ["https://www.aliexpress.com/item/123.html", "https://www.aliexpress.com/item/456.html"]

    @pytest.fixture
    def ali_affiliated_products():
        return AliAffiliatedProducts(campaign_name, category_name, language, currency)

    def test_process_affiliate_products(ali_affiliated_products):
        # Пример того, как мокировать retrieve_product_details
        mock_product_details = [
            SimpleNamespace(product_id="789", promotion_link="promo_link2", product_main_image_url="image_url2", product_video_url="video_url2")
        ]
        with patch.object(ali_affiliated_products, 'retrieve_product_details', return_value=mock_product_details) as mock_retrieve:
            # ... (прочие patch, как в примере кода) ...
            processed_products = ali_affiliated_products.process_affiliate_products(prod_urls)
            assert len(processed_products) == 1  # Проверяем, что обработан один продукт
            assert processed_products[0].product_id == "789"  # Проверка значения product_id


    if __name__ == "__main__":
        pytest.main()