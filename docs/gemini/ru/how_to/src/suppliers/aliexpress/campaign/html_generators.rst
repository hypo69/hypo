Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит классы для генерации HTML-страниц, предназначенных для отображения рекламных кампаний на сайте.  Классы `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator` генерируют HTML-файлы для отдельных товаров, категорий товаров и всей рекламной кампании соответственно.  Код использует библиотеку `html` для экранирования пользовательского ввода, `pathlib` для работы с путями к файлам, `SimpleNamespace` для структурирования данных о товарах и функцию `save_text_file` для сохранения сгенерированного HTML в файлы.  Он использует Bootstrap для стилей и шаблона веб-страницы.

Шаги выполнения
-------------------------
1. **Создание HTML для продукта:**  Класс `ProductHTMLGenerator` принимает объект `product` (содержащий информацию о товаре) и путь к папке категории (`category_path`). Он формирует HTML-код, содержащий информацию о товаре (название, цена, изображение, ссылка на покупку), используя данные из объекта `product`. Затем, он сохраняет сгенерированный HTML-контент в файл с именем, соответствующим идентификатору продукта (`product.product_id.html`), в подпапке `html` указанной категории.

2. **Создание HTML для категории:** Класс `CategoryHTMLGenerator` принимает список товаров (`products_list`) и путь к папке категории (`category_path`).  Он формирует HTML-код, содержащий информацию обо всех товарах в категории.  Вместо одиночного объекта `product`, этот класс может обрабатывать список `products_list` (или одиночный объект, если он передается как таковой).  HTML-страница содержит список товаров с картинками, заголовками, ценами и кнопками "Купить".  Все это сохраняется в файл `index.html` в указанной категории.

3. **Создание HTML для всей кампании:** Класс `CampaignHTMLGenerator` принимает список имен категорий (`categories`) и путь к папке кампании (`campaign_path`). Этот класс формирует HTML-код для главной страницы кампании.  Он создает список ссылок на все категории товаров, позволяя пользователю быстро перейти к интересующей категории. Результат сохраняется в файл `index.html` в папке кампании.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator
    from pathlib import Path
    from types import SimpleNamespace
    
    # Пример данных о продукте
    product_data = SimpleNamespace(
        product_id=123,
        product_title="Example Product",
        local_saved_image="images/example.jpg",
        target_sale_price=10.99,
        target_sale_price_currency="USD",
        target_original_price=15.99,
        target_original_price_currency="USD",
        second_level_category_name="Electronics",
        promotion_link="https://example.com/product123"
    )
    
    # Путь к папке категории
    category_path = Path("./category1")
    
    # Генерация HTML для продукта
    ProductHTMLGenerator.set_product_html(product_data, category_path)


    # Пример списка продуктов для категории
    products_list = [product_data, product_data]  # Список из нескольких продуктов
    CategoryHTMLGenerator.set_category_html(products_list, category_path)


    # Пример списка категорий
    categories = ["category1", "category2"]
    campaign_path = Path("./campaign")
    CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)