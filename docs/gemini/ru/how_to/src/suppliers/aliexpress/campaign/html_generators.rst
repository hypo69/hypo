Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит классы для генерации HTML-страниц рекламных кампаний.  Он позволяет создавать отдельные HTML-страницы для продуктов, категорий продуктов и общей страницы кампании.  Код генерирует HTML-структуру с использованием Bootstrap, включая заголовки, изображения, цены, ссылки на страницы продуктов и категории.  Он использует библиотеки `pathlib`, `html`, `SimpleNamespace` и `save_text_file` для работы с путями, HTML-экранированием, данными продуктов и сохранением сгенерированных файлов.

Шаги выполнения
-------------------------
1. **Инициализация:**  Создаются классы `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator`.  Эти классы содержат статические методы для генерации HTML.

2. **Генерация HTML для продукта:** Метод `set_product_html` принимает объект `product` (представленный как `SimpleNamespace`) и путь к категории `category_path`.  Он формирует путь к файлу `html` для конкретного продукта `product.product_id.html`.  Затем формирует HTML-код, включающий название продукта, изображение, цену, оригинальную цену, категорию и ссылку покупки, используя методы `html.escape` для экранирования специальных символов.  В конечном итоге он сохраняет сгенерированный HTML-контент в указанный файл.

3. **Генерация HTML для категории:** Метод `set_category_html` принимает список продуктов `products_list` и путь к категории `category_path`. Он создаёт HTML-страницу с разметкой для вывода всех продуктов в категории.  Код итерирует по списку `products_list` и генерирует HTML для каждого продукта, включая изображение, название, цену, оригинальную цену и категорию.  Сохраняет полученный HTML-код в файл `index.html` в данной категории.

4. **Генерация HTML для кампании:** Метод `set_campaign_html` принимает список категорий `categories` и путь к кампании `campaign_path`.  Генерирует главную страницу кампании, которая выводит список категорий и ссылки на них.  Для каждой категории генерируется ссылка на её HTML-страницу `category/index.html`. Сохраняет сгенерированный HTML-код в файл `index.html` кампании.

5. **Обработка данных:** Код использует `SimpleNamespace` для представления данных продукта, что позволяет обращаться к атрибутам продукта (например, `product.product_title`, `product.local_saved_image` и т.д.) удобным способом.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator
    from pathlib import Path
    from types import SimpleNamespace
    
    # Пример данных продукта (замените на ваши данные)
    product_data = SimpleNamespace(
        product_id=123,
        product_title="Example Product",
        local_saved_image=Path("images/example.jpg"),
        target_sale_price=10.99,
        target_sale_price_currency="USD",
        target_original_price=15.99,
        target_original_price_currency="USD",
        second_level_category_name="Electronics",
        promotion_link="https://example.com/product"
    )

    # Пример использования для генерации HTML страницы продукта
    ProductHTMLGenerator.set_product_html(product_data, "categories/electronics")

    # Пример для генерации HTML страницы категории (если есть список продуктов)
    categories_products = [product_data, product_data] # Замените на реальный список продуктов
    CategoryHTMLGenerator.set_category_html(categories_products, "categories/electronics")

    # Пример для генерации HTML страницы кампании
    categories = ["Electronics", "Clothing"]
    CampaignHTMLGenerator.set_campaign_html(categories, "campaign")