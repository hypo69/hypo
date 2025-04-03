# Модуль для генерации HTML контента рекламной кампании
=================================================

Модуль содержит классы для генерации HTML-страниц: `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator`.
Эти классы позволяют создавать HTML-файлы для отдельных продуктов, категорий продуктов и общие страницы кампании, соответственно.

## Обзор

Модуль предназначен для автоматического создания HTML-страниц на основе данных о товарах и категориях. Он использует строковые шаблоны и метод `save_text_file` из модуля `src.utils.file` для сохранения сгенерированного HTML-контента в файлы.

## Подробней

Модуль предоставляет три класса для генерации HTML-страниц разного уровня:

- `ProductHTMLGenerator`: Создает HTML-страницу для отдельного товара, отображая его название, изображение, цену и категорию.
- `CategoryHTMLGenerator`: Создает HTML-страницу для категории товаров, отображая список товаров с их основной информацией.
- `CampaignHTMLGenerator`: Создает общую HTML-страницу кампании, содержащую список категорий товаров.

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML-страницы отдельного товара.

**Принцип работы**: Класс `ProductHTMLGenerator` предоставляет статический метод `set_product_html`, который принимает объект `SimpleNamespace` с данными о продукте и путь к каталогу, в котором нужно сохранить HTML-файл. Метод создает HTML-контент, используя строковые шаблоны, и сохраняет его в файл с именем `product_id.html` в подкаталоге `html` указанного каталога.

**Методы**:

- `set_product_html(product: SimpleNamespace, category_path: str | Path)`: Создает HTML-файл для отдельного продукта.

    **Параметры**:
    - `product` (SimpleNamespace): Объект `SimpleNamespace`, содержащий данные о продукте.
    - `category_path` (str | Path): Путь к каталогу, в котором нужно сохранить HTML-файл.

    **Как работает функция**:
    1. **Извлечение имени категории**: Извлекается имя категории из пути `category_path`.
    2. **Определение пути к HTML-файлу**: Формируется путь к HTML-файлу, который будет создан в подкаталоге `html` каталога `category_path`. Имя файла формируется на основе `product.product_id`.
    3. **Создание HTML-контента**: Создается HTML-контент с использованием f-строк, в который подставляются данные из объекта `product`.
    4. **Сохранение HTML-контента в файл**: Используется функция `save_text_file` для сохранения HTML-контента в файл по указанному пути.

    **Пример**:

    ```python
    from types import SimpleNamespace
    from pathlib import Path

    product_data = SimpleNamespace(
        product_id="12345",
        product_title="Example Product",
        local_image_path="images/example.jpg",
        target_sale_price=100,
        target_sale_price_currency="USD",
        target_original_price=120,
        target_original_price_currency="USD",
        second_level_category_name="Example Category",
        promotion_link="https://example.com"
    )
    category_path = "path/to/category"
    ProductHTMLGenerator.set_product_html(product_data, category_path)
    ```

    **Flowchart**:

    ```
    Получение данных о продукте и пути к категории
    │
    └──> Определение пути к HTML-файлу
    │
    └──> Создание HTML-контента с данными о продукте
    │
    └──> Сохранение HTML-контента в файл
    ```

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML-страницы категории товаров.

**Принцип работы**: Класс `CategoryHTMLGenerator` предоставляет статический метод `set_category_html`, который принимает список объектов `SimpleNamespace` с данными о продуктах в категории и путь к каталогу категории. Метод создает HTML-контент, формируя HTML-код для каждого продукта в списке, и сохраняет его в файл `index.html` в подкаталоге `html` указанного каталога.

**Методы**:

- `set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path)`: Создает HTML-файл для категории товаров.

    **Параметры**:
    - `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов `SimpleNamespace`, содержащих данные о продуктах в категории.
    - `category_path` (str | Path): Путь к каталогу категории.

    **Как работает функция**:

    1. **Обработка входных данных**: Преобразует входные данные `products_list` в список, если передан один объект `SimpleNamespace`.
    2. **Извлечение имени категории**: Извлекается имя категории из пути `category_path`.
    3. **Определение пути к HTML-файлу**: Формируется путь к HTML-файлу `index.html`, который будет создан в подкаталоге `html` каталога `category_path`.
    4. **Создание HTML-контента**: Создается HTML-контент, который включает в себя HTML-код для каждого продукта в списке.
    5. **Сохранение HTML-контента в файл**: Используется функция `save_text_file` для сохранения HTML-контента в файл по указанному пути.

    **Пример**:

    ```python
    from types import SimpleNamespace
    from pathlib import Path

    product_data_1 = SimpleNamespace(
        product_id="12345",
        product_title="Example Product 1",
        local_image_path="images/example1.jpg",
        target_sale_price=100,
        target_sale_price_currency="USD",
        target_original_price=120,
        target_original_price_currency="USD",
        second_level_category_name="Example Category",
        promotion_link="https://example.com/1"
    )
    product_data_2 = SimpleNamespace(
        product_id="67890",
        product_title="Example Product 2",
        local_image_path="images/example2.jpg",
        target_sale_price=150,
        target_sale_price_currency="USD",
        target_original_price=170,
        target_original_price_currency="USD",
        second_level_category_name="Example Category",
        promotion_link="https://example.com/2"
    )
    products_list = [product_data_1, product_data_2]
    category_path = "path/to/category"
    CategoryHTMLGenerator.set_category_html(products_list, category_path)
    ```

    **Flowchart**:

    ```
    Получение списка продуктов и пути к категории
    │
    └──> Преобразование в список, если передан один продукт
    │
    └──> Определение пути к HTML-файлу (index.html)
    │
    └──> Создание HTML-контента для каждого продукта
    │
    └──> Сохранение HTML-контента в файл
    ```

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML-страницы кампании, содержащей список категорий.

**Принцип работы**: Класс `CampaignHTMLGenerator` предоставляет статический метод `set_campaign_html`, который принимает список имен категорий и путь к каталогу кампании. Метод создает HTML-контент, формируя список ссылок на страницы категорий, и сохраняет его в файл `index.html` в указанном каталоге кампании.

**Методы**:

- `set_campaign_html(categories: list[str], campaign_path: str | Path)`: Создает HTML-файл для кампании, перечисляя все категории.

    **Параметры**:
    - `categories` (list[str]): Список имен категорий.
    - `campaign_path` (str | Path): Путь к каталогу кампании.

    **Как работает функция**:

    1. **Определение пути к HTML-файлу**: Формируется путь к HTML-файлу `index.html` в каталоге кампании.
    2. **Создание HTML-контента**: Создается HTML-контент, который включает в себя список ссылок на страницы категорий.
    3. **Сохранение HTML-контента в файл**: Используется функция `save_text_file` для сохранения HTML-контента в файл по указанному пути.

    **Пример**:

    ```python
    from pathlib import Path

    categories = ["category1", "category2", "category3"]
    campaign_path = "path/to/campaign"
    CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)
    ```

    **Flowchart**:

    ```
    Получение списка категорий и пути к кампании
    │
    └──> Определение пути к HTML-файлу (index.html)
    │
    └──> Создание HTML-контента со списком категорий
    │
    └──> Сохранение HTML-контента в файл
    ```

## Функции

В данном модуле нет отдельных функций, только статические методы внутри классов.