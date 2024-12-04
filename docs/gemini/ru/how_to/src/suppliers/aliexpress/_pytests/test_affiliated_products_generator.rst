Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит тесты для класса `AliAffiliatedProducts`, отвечающего за обработку продуктов с аффилированными ссылками на AliExpress.  Тесты проверяют корректность вызовов методов `check_and_process_affiliate_products` и `process_affiliate_products`.  Код использует `pytest`, `unittest.mock` для мокирования внешних зависимостей и проверки ожидаемого поведения.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:** Модуль `pytest` для запуска тестов, `unittest.mock` для мокирования функций, класс `AliAffiliatedProducts` и вспомогательные классы.

2. **Определение данных для тестов:**
   - `campaign_name`, `category_name`, `language`, `currency`: Переменные для хранения данных кампании.
   - `prod_urls`: Список URL адресов продуктов AliExpress.
   - `mock_product_details`: Список объектов `SimpleNamespace`, имитирующих детали продуктов.  Важное примечание: это мок, а не реальные данные.

3. **Создание фикстуры `ali_affiliated_products`:**  Фикстура, которая создает экземпляр класса `AliAffiliatedProducts` с указанными параметрами кампании.

4. **Тест `test_check_and_process_affiliate_products`:**
   - Использует `patch` для мокирования метода `process_affiliate_products`.
   - Вызывает `check_and_process_affiliate_products` с входными `prod_urls`.
   - Проверяет, что метод `process_affiliate_products` был вызван один раз с теми же `prod_urls`.

5. **Тест `test_process_affiliate_products`:**
   - Использует `patch` для мокирования функций `retrieve_product_details`, `ensure_https`, `save_png_from_url`, `save_video_from_url`, `j_dumps`.
   - `retrieve_product_details` возвращает `mock_product_details`.
   - `ensure_https` возвращает `prod_urls` (это мок, предполагается, что функция возвращает то же самое, что и на вход).
   - `save_png_from_url`, `save_video_from_url`, `j_dumps` -  мокируются, что они работают без ошибок.
   - Вызывает `process_affiliate_products` с `prod_urls`.
   - Проверяет, что количество обработанных продуктов равно 1.
   - Проверяет, что `product_id` первого обработанного продукта соответствует ожидаемому значению.

6. **Запуск тестов:** Код содержит блок `if __name__ == "__main__":`, который запускает тесты с помощью `pytest.main()`.

Пример использования
-------------------------
.. code-block:: python

    # (Этот код не является примером использования тестируемого кода,
    # а демонстрирует как можно использовать созданные фикстуры и методы.)
    import pytest
    from unittest.mock import MagicMock  # Импортируем необходимый класс
    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    @pytest.fixture
    def ali_affiliated_products(campaign_name, category_name, language, currency):
        # ... (код фикстуры)
        return AliAffiliatedProducts(campaign_name, category_name, language, currency)

    def test_something(ali_affiliated_products):
        product_urls = ["https://example.com/product1", "https://example.com/product2"]

        mock_result = MagicMock()  # Создаем мок для результата метода
        with patch.object(ali_affiliated_products, "process_affiliate_products", return_value = mock_result):
            result = ali_affiliated_products.check_and_process_affiliate_products(product_urls)
        
        # Проверка результатов
        assert result == mock_result