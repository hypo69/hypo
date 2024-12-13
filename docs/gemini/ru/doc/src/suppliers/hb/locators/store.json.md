# Документация для `store.json`

## Обзор

Этот файл содержит JSON-структуру, представляющую локаторы для элементов на странице магазина поставщика HB. Он используется для определения путей к элементам пользовательского интерфейса при автоматизации тестирования или других задач, связанных с веб-скрейпингом.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [Поля](#поля)
    - [Пример использования](#пример-использования)

## Структура JSON

Файл `store.json` представляет собой JSON-объект, содержащий локаторы для различных элементов на странице магазина. Ключи объекта соответствуют именам элементов, а значения - это строки, представляющие собой XPath или CSS-селекторы для этих элементов.

### Поля

-   `product_item`: Локатор для отдельного элемента товара в списке.
-   `product_title`: Локатор для заголовка товара.
-   `product_price`: Локатор для цены товара.
-   `product_image`: Локатор для изображения товара.
-   `product_link`: Локатор для ссылки на страницу товара.
-   `next_page_button`: Локатор для кнопки "Следующая страница".
-   `pagination_item`: Локатор для элемента пагинации.
-   `active_pagination_item`: Локатор для активного элемента пагинации.
-   `sort_button`: Локатор для кнопки сортировки.
-   `sort_by_price_asc`: Локатор для варианта сортировки по цене по возрастанию.
-   `sort_by_price_desc`: Локатор для варианта сортировки по цене по убыванию.
-   `sort_by_name_asc`: Локатор для варианта сортировки по имени по возрастанию.
-   `sort_by_name_desc`: Локатор для варианта сортировки по имени по убыванию.
-   `product_card_button`: Локатор для кнопки добавления товара в корзину (или аналогичной кнопки) внутри карточки товара.
-   `search_input`: Локатор для поля ввода поиска.
-   `search_button`: Локатор для кнопки поиска.
-   `clear_search_button`: Локатор для кнопки очистки поля поиска.
-   `sort_by_popularity`: Локатор для варианта сортировки по популярности.
-   `breadcrumb`: Локатор для элемента breadcrumb.
-   `breadcrumb_item`: Локатор для элемента breadcrumb item.
-   `product_category`: Локатор для категории продукта.
-   `product_brand`: Локатор для бренда продукта.
-   `product_description`: Локатор для описания товара.
-   `product_parameters_table`: Локатор для таблицы параметров товара.
-   `product_parameter_name`: Локатор для имени параметра товара.
-   `product_parameter_value`: Локатор для значения параметра товара.
-  `product_available_status`: Локатор для статуса наличия товара.
-  `product_available_status_text`: Локатор для текстового значения статуса наличия товара.
- `product_card_availability`: Локатор для информации о наличии товара в карточке продукта.
- `product_add_to_wishlist_button`: Локатор для кнопки добавления товара в избранное
-  `product_not_available_status`: Локатор для статуса недоступности товара.

### Пример использования

```json
{
  "product_item": "//div[@class='product-item']",
  "product_title": ".//h2[@class='product-title']",
  "product_price": ".//span[@class='product-price']",
  "product_image": ".//img[@class='product-image']",
  "product_link": ".//a[@class='product-link']",
  "next_page_button": "//a[@class='next-page-button']",
  "pagination_item": "//ul[@class='pagination']/li",
  "active_pagination_item": "//ul[@class='pagination']/li[@class='active']",
  "sort_button": "//button[@class='sort-button']",
  "sort_by_price_asc": "//li[@data-sort='price-asc']",
  "sort_by_price_desc": "//li[@data-sort='price-desc']",
  "sort_by_name_asc": "//li[@data-sort='name-asc']",
  "sort_by_name_desc": "//li[@data-sort='name-desc']",
   "product_card_button": "//button[@class='add-to-cart-button']",
  "search_input": "//input[@id='search-input']",
  "search_button": "//button[@class='search-button']",
  "clear_search_button":"//button[@class='clear-search-button']",
   "sort_by_popularity": "//li[@data-sort='popularity']",
    "breadcrumb": "//ul[@class='breadcrumb']",
    "breadcrumb_item": "//ul[@class='breadcrumb']/li",
   "product_category": "//span[@class='product-category']",
   "product_brand": "//span[@class='product-brand']",
  "product_description": "//div[@class='product-description']",
   "product_parameters_table":"//table[@class='product-parameters-table']",
    "product_parameter_name":"//tr/td[1]",
    "product_parameter_value":"//tr/td[2]",
    "product_available_status": "//span[contains(@class, 'available')]",
    "product_available_status_text": "//span[contains(@class, 'available')]/text()",
  "product_card_availability":"//div[@class='product-availability']",
 "product_add_to_wishlist_button":"//button[@class='add-to-wishlist-button']",
 "product_not_available_status":"//span[contains(@class, 'not-available')]"
}
```