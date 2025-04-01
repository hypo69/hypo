# Модуль: `src.suppliers.aliexpress.campaign.html_generators`

## Обзор

Модуль `html_generators.py` предназначен для генерации HTML-контента рекламных кампаний, сфокусированных на товарах из AliExpress. Он включает в себя классы для создания HTML-страниц как для отдельных продуктов, так и для категорий товаров, а также для общей страницы кампании, которая объединяет все категории.

## Подробнее

Этот модуль предоставляет функциональность для автоматического создания HTML-страниц, которые могут быть использованы для представления товаров и категорий в рекламных кампаниях. Он использует данные о продуктах, такие как название, цена, изображения и ссылки для покупки, чтобы сгенерировать HTML-код, который затем сохраняется в файлы.

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс `ProductHTMLGenerator` предназначен для генерации HTML-страниц для отдельных товаров.

**Принцип работы**:
Класс предоставляет статический метод `set_product_html`, который принимает информацию о продукте и путь к категории, создает HTML-файл с детальным описанием продукта и сохраняет его в указанном месте. HTML включает название продукта, изображение, цену, оригинальную цену, категорию и ссылку для покупки.

**Методы**:

- `set_product_html(product: SimpleNamespace, category_path: str | Path)`

    ```python
    @staticmethod
    def set_product_html(product: SimpleNamespace, category_path: str | Path):
        """ Creates an HTML file for an individual product.
        
        @param product: The product details to include in the HTML.
        @param category_path: The path to save the HTML file.
        """
    ```

    **Назначение**: Создает HTML-файл для отдельного продукта.

    **Параметры**:
    - `product` (SimpleNamespace): Объект, содержащий детали продукта, такие как `product_id`, `product_title`, `local_image_path`, `target_sale_price`, `target_sale_price_currency`, `target_original_price`, `target_original_price_currency`, `second_level_category_name` и `promotion_link`.
    - `category_path` (str | Path): Путь к каталогу, в котором будет сохранен HTML-файл продукта.

    **Как работает функция**:
    1. Извлекает имя категории из `category_path`.
    2. Формирует путь к HTML-файлу продукта, используя `product.product_id`.
    3. Создает HTML-контент, включающий мета-теги, стили Bootstrap, заголовок с названием продукта, карточку продукта с изображением, ценами, категорией и ссылкой для покупки.
    4. Вызывает функцию `save_text_file` для сохранения HTML-контента в файл.

    **Примеры**:
    ```python
    from types import SimpleNamespace
    from pathlib import Path
    
    # Пример создания объекта product
    product = SimpleNamespace(
        product_id='12345',
        product_title='Example Product',
        local_image_path='/path/to/image.jpg',
        target_sale_price='19.99',
        target_sale_price_currency='USD',
        target_original_price='29.99',
        target_original_price_currency='USD',
        second_level_category_name='Category Name',
        promotion_link='https://example.com/product'
    )
    
    # Пример вызова set_product_html
    category_path = 'path/to/category'
    ProductHTMLGenerator.set_product_html(product, category_path)
    # Будет создан HTML-файл по пути path/to/category/html/12345.html
    ```

### `CategoryHTMLGenerator`

**Описание**: Класс `CategoryHTMLGenerator` предназначен для генерации HTML-страниц для категорий продуктов.

**Принцип работы**:
Класс предоставляет статический метод `set_category_html`, который принимает список продуктов и путь к категории, создает HTML-файл, отображающий список продуктов в данной категории, и сохраняет его в указанном месте. HTML включает название категории и карточки для каждого продукта с изображением, названием, ценами и ссылкой для покупки.

**Методы**:

- `set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path)`

    ```python
    @staticmethod
    def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
        """ Creates an HTML file for the category.
        
        @param products_list: List of products to include in the HTML.
        @param category_path: Path to save the HTML file.
        """
    ```

    **Назначение**: Создает HTML-файл для отображения списка продуктов в категории.

    **Параметры**:
    - `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов, содержащих детали продуктов, или один объект `SimpleNamespace` с деталями продукта.
    - `category_path` (str | Path): Путь к каталогу, в котором будет сохранен HTML-файл категории.

    **Как работает функция**:
    1. Преобразует `products_list` в список, если передан один объект `SimpleNamespace`.
    2. Извлекает имя категории из `category_path`.
    3. Формирует путь к HTML-файлу категории (`index.html`).
    4. Создает HTML-контент, включающий мета-теги, стили Bootstrap, заголовок с названием категории и сетку продуктов, отображающую каждый продукт в виде карточки с изображением, названием, ценами, категорией и ссылкой для покупки.
    5. Вызывает функцию `save_text_file` для сохранения HTML-контента в файл.

    **Примеры**:
    ```python
    from types import SimpleNamespace
    from pathlib import Path
    
    # Пример создания списка объектов product
    products_list = [
        SimpleNamespace(
            product_id='12345',
            product_title='Example Product 1',
            local_image_path='/path/to/image1.jpg',
            target_sale_price='19.99',
            target_sale_price_currency='USD',
            target_original_price='29.99',
            target_original_price_currency='USD',
            second_level_category_name='Category Name',
            promotion_link='https://example.com/product1'
        ),
        SimpleNamespace(
            product_id='67890',
            product_title='Example Product 2',
            local_image_path='/path/to/image2.jpg',
            target_sale_price='24.99',
            target_sale_price_currency='USD',
            target_original_price='34.99',
            target_original_price_currency='USD',
            second_level_category_name='Category Name',
            promotion_link='https://example.com/product2'
        )
    ]
    
    # Пример вызова set_category_html
    category_path = 'path/to/category'
    CategoryHTMLGenerator.set_category_html(products_list, category_path)
    # Будет создан HTML-файл по пути path/to/category/html/index.html
    ```

### `CampaignHTMLGenerator`

**Описание**: Класс `CampaignHTMLGenerator` предназначен для генерации HTML-страницы кампании, содержащей список категорий.

**Принцип работы**:
Класс предоставляет статический метод `set_campaign_html`, который принимает список категорий и путь к кампании, создает HTML-файл со списком категорий, представленных в виде ссылок, и сохраняет его в указанном месте. HTML включает заголовок кампании и список ссылок на HTML-страницы категорий.

**Методы**:

- `set_campaign_html(categories: list[str], campaign_path: str | Path)`

    ```python
    @staticmethod
    def set_campaign_html(categories: list[str], campaign_path: str | Path):
        """ Creates an HTML file for the campaign, listing all categories.
        
        @param categories: List of category names.
        @param campaign_path: Path to save the HTML file.
        """
    ```

    **Назначение**: Создает HTML-файл для кампании, отображающий список категорий.

    **Параметры**:
    - `categories` (list[str]): Список названий категорий.
    - `campaign_path` (str | Path): Путь к каталогу, в котором будет сохранен HTML-файл кампании.

    **Как работает функция**:
    1. Формирует путь к HTML-файлу кампании (`index.html`).
    2. Создает HTML-контент, включающий мета-теги, стили Bootstrap, заголовок кампании и список категорий, представленных в виде ссылок на HTML-страницы категорий.
    3. Вызывает функцию `save_text_file` для сохранения HTML-контента в файл.

    **Примеры**:
    ```python
    from pathlib import Path
    
    # Пример списка категорий
    categories = ['Category1', 'Category2', 'Category3']
    
    # Пример вызова set_campaign_html
    campaign_path = 'path/to/campaign'
    CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)
    # Будет создан HTML-файл по пути path/to/campaign/index.html
    ```