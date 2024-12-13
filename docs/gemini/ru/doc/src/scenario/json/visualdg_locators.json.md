# Описание структуры JSON файла `visualdg_locators.json`

## Обзор

Файл `visualdg_locators.json` содержит JSON-структуру с локаторами элементов пользовательского интерфейса для автоматизации тестирования или парсинга веб-страниц. Этот файл определяет CSS-селекторы и атрибуты для различных элементов на веб-странице, таких как категории, товары, поля товаров, а также настройки для входа в систему и прокрутки.

## Оглавление

1.  [Раздел `category`](#category)
2.  [Раздел `product`](#product)
3.  [Раздел `product_fields_locators`](#product_fields_locators)
4.  [Раздел `stock_locator`](#stock_locator)
5.  [Раздел `not in stock`](#not-in-stock)
6.  [Раздел `login`](#login)
7.  [Раздел `infinity_scroll`](#infinity_scroll)
8.  [Раздел `checkboxes_for_categories`](#checkboxes_for_categories)

## `category`

### Описание

Этот раздел содержит локаторы для элементов, связанных с категориями на веб-странице.

### `pages_listing_locator`

#### Описание

Локатор для элемента, который содержит список категорий или страницу списка.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"pages_listing_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "infinity_scroll"
}
```

## `product`

### Описание

Этот раздел содержит локаторы для элементов, связанных с отображением товаров на веб-странице.

### `product_block_locator`

#### Описание

Локатор для блока, содержащего информацию о продукте.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"product_block_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "div[id^='item_id_']"
}
```

### `link_to_product_locator`

#### Описание

Локатор для ссылки на страницу товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"link_to_product_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "href",
  "by": "css selector",
  "selector": "div.layout_list_item.item a"
}
```

## `product_fields_locators`

### Описание

Этот раздел содержит локаторы для полей, отображающих информацию о товаре.

### `product_name_locator`

#### Описание

Локатор для элемента, содержащего название товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"product_name_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "div[id='item_current_title'] h1 span"
}
```

### `brand_locator`

#### Описание

Локатор для элемента, содержащего название бренда.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"brand_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": ".brands"
}
```

### `sku_locator`

#### Описание

Локатор для элемента, содержащего SKU товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"sku_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "div.code_item"
}
```

### `brand_sku_locator`

#### Описание

Локатор для элемента, содержащего SKU бренда.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"brand_sku_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "div.code_item"
}
```

### `summary_locator`

#### Описание

Локатор для элемента, содержащего краткое описание товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"summary_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "div[id='item_current_sub_title'] span"
}
```

### `description_locator`

#### Описание

Локатор для элемента, содержащего подробное описание товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"description_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "div.item_attributes"
}
```

### `images_locator`

#### Описание

Локатор для элемента, содержащего изображения товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"images_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "src",
  "by": "css selector",
  "selector": "div[id=item_show_carousel] img"
}
```

### `price_locator`

#### Описание

Локатор для элемента, содержащего цену товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"price_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "span.price_value"
}
```

## `stock_locator`

### Описание

Этот раздел содержит локатор для элемента, который указывает наличие товара на складе.

### `stock_locator`

#### Описание

Локатор для элемента, отображающего информацию о наличии товара.

#### Параметры

-   `logic for attribue[AND|OR|XOR|VALUE|null]` (null): Логика для атрибута. В данном случае не используется.
-   `attribute` (str): Атрибут элемента, который необходимо использовать.
-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"stock_locator": {
  "logic for attribue[AND|OR|XOR|VALUE|null]": null,
  "attribute": "innerHTML",
  "by": "css selector",
  "selector": "span[class='stock_text']"
}
```

## `not in stock`

### Описание

Этот раздел содержит список стилей, указывающих на отсутствие товара на складе.

### Описание

Список стилей, которые соответствуют статусу "нет в наличии".

#### Пример

```json
"not in stock": [
  "color:red",
  "color:#d19b00"
]
```

## `login`

### Описание

Этот раздел содержит данные и локаторы для входа в систему.

### `email`

#### Описание

E-mail для входа в систему.

#### Пример

```json
"email": "edik@aluf.co.il"
```

### `password`

#### Описание

Пароль для входа в систему.

#### Пример

```json
"password": "fbba0cadc8"
```

### `open_login_dialog_locator`

#### Описание

Локатор для элемента, открывающего диалог входа.

#### Параметры

-   `by` (str): Метод поиска элемента. В данном случае не заполнен.
-   `selector` (str): CSS-селектор для поиска элемента. В данном случае не заполнен.

#### Пример

```json
"open_login_dialog_locator": {
    "by": "------",
    "selector": "------"
  }
```

### `email_locator`

#### Описание

Локатор для поля ввода e-mail.

#### Параметры

-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"email_locator": {
  "by": "css selector",
  "selector": "input[id='customer_session_username']"
}
```

### `password_locator`

#### Описание

Локатор для поля ввода пароля.

#### Параметры

-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"password_locator": {
  "by": "css selector",
  "selector": "input[id='customer_session_password']"
}
```

### `loginbutton_locator`

#### Описание

Локатор для кнопки входа.

#### Параметры

-   `by` (str): Метод поиска элемента (например, `css selector`).
-   `selector` (str): CSS-селектор для поиска элемента.

#### Пример

```json
"loginbutton_locator": {
  "by": "css selector",
  "selector": "a[href='#customer']"
}
```

## `infinity_scroll`

### Описание

Этот раздел указывает, используется ли бесконечная прокрутка на странице.

### Описание

Логическое значение, указывающее, используется ли бесконечная прокрутка.

#### Пример

```json
"infinity_scroll": true
```

## `checkboxes_for_categories`

### Описание

Этот раздел указывает, используются ли чекбоксы для фильтрации категорий.

### Описание

Логическое значение, указывающее, используются ли чекбоксы для категорий.

#### Пример

```json
"checkboxes_for_categories": false
```