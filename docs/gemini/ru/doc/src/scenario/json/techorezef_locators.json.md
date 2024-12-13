# Документация `techorezef_locators.json`

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [category](#category)
    - [product](#product)
    - [product_fields_locators](#product_fields_locators)
    - [stock_locator](#stock_locator)
    - [not in stock](#not-in-stock)
    - [login](#login)
    - [infinity_scroll](#infinity_scroll)
    - [checkboxes_for_categories](#checkboxes_for_categories)

## Обзор

Файл `techorezef_locators.json` содержит JSON-объект с локаторами элементов веб-страницы, используемые для автоматизации сбора данных с сайта. 
Этот файл включает в себя локаторы для категорий, продуктов, полей продукта, информации о наличии на складе, а также данные для входа в систему.
Файл предназначен для использования в скриптах, которые взаимодействуют с веб-страницами для извлечения и обработки данных.
   
## Структура JSON

### category

Содержит локатор для элемента, отвечающего за отображение списка страниц категорий.

- `pages_listing_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`:  "innerHTML"
    -   `by`:  "css selector"
    -   `selector`: "infinity_scroll"
    

### product

Содержит локаторы для элементов, относящихся к отображению информации о продукте.

- `product_block_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: "div[id^='item_id_']"

- `link_to_product_locator`
    -    `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`: "href"
    -   `by`: "css selector"
    -   `selector`: "div.layout_list_item.item a"
    

### product_fields_locators

Содержит локаторы для различных полей продукта.

- `product_name_locator`
    -    `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: "span[itemprop='name']"

- `brand_locator`
    -  `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: ".brands"

- `sku_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -    `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: "div.code_item"

- `brand_sku_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: "div.code_item"

- `summary_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -    `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: "div.item_current_sub_title span"

- `description_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -    `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: "div.item_attributes"

- `images_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`: "src"
    -   `by`: "css selector"
    -   `selector`: "div[id=item_show_carousel] img"

- `price_locator`
    -   `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
    -   `attribute`: "innerHTML"
    -   `by`: "css selector"
    -   `selector`: "span.price_value"

### stock_locator

Содержит локатор для элемента, отображающего информацию о наличии товара на складе.

-    `logic for attribue[AND|OR|XOR|VALUE|null]` : `null`
-   `attribute`: "innerHTML"
-   `by`: "css selector"
-   `selector`: "span.stock_text"

### not in stock

Список CSS-свойств для определения, что товар отсутствует на складе.

-   `color:red`
-   `color:#d19b00`

### login

Содержит данные и локаторы для входа в систему.

- `email`: "edik@aluf.co.il"
- `password`: "14170019"

- `open_login_dialog_locator`
    -  `by`: "css selector"
    -  `selector`: "a[id='login_button']"

- `email_locator`
    - `by`: "css selector"
    - `selector`: "input[name='username']"

- `password_locator`
    - `by`: "css selector"
    - `selector`: "input[name='password']"

- `loginbutton_locator`
    -  `by`: "css selector"
    -  `selector`: "input[id='login_button' type='submit']"

### infinity_scroll

Булево значение, указывающее, используется ли бесконечная прокрутка на сайте.
- `true`

### checkboxes_for_categories

Булево значение, указывающее, используются ли чекбоксы для выбора категорий.
- `false`