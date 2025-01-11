# Документация для `ksp_locators.json`

## Обзор

Файл `ksp_locators.json` содержит JSON-объект, определяющий локаторы для различных элементов веб-страницы. Эти локаторы используются для автоматизации тестирования и взаимодействия с элементами страницы. Структура файла включает в себя локаторы для выбора языка, категорий, баннеров, а также локаторы для элементов на странице продукта.

## Оглавление

1. [Языки](#languages)
2. [Бесконечная прокрутка](#infinity_scroll)
3. [Чекбоксы для категорий](#checkboxes_for_categories)
4. [Категория](#category)
    - [Локатор списка страниц](#pages_listing_locator)
5. [Топ-баннер](#top_banner_locator)
6. [Продукт](#product)
    - [Локатор ссылки на продукт](#link_to_product_locator)
    - [Локатор блока продукта](#product_block_locator)
    - [Локатор SKU](#sku_locator)
    - [Локатор названия продукта](#product_name_locator)
    - [Локатор цены](#price_locator)
    - [Локатор доставки продукта](#product_delivery_locator)
    - [Локатор главного изображения](#main_image_locator)
    - [Локатор краткого описания](#summary_locator)
    - [Локатор описания](#description_locator)
    - [Локатор спецификации](#specification_locator)
    - [Локатор отзывов покупателей](#customer_reviews_locator)
    - [Локатор атрибутов продукта](#product_attributes_locator)
        - [Локатор цвета](#color)
        - [Локатор памяти телефона](#phone_memory)
        - [Локатор доставки](#delivery)

## Языки

Секция `languages` содержит локаторы для переключения языков на сайте. Каждый язык представлен в виде объекта с ключом, соответствующим коду языка.
Например, для иврита ("he"):

- **attribute**: "sendKeys(Keys.RETURN)" - Атрибут, который будет использоваться.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//li[@data-value='he']" - XPATH-селектор для элемента.
- **timeout**: 0 - Тайм-аут ожидания элемента.
- **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
- **event**: null - Событие, которое будет выполнено

## Бесконечная прокрутка

Поле `infinity_scroll` указывает, используется ли на странице бесконечная прокрутка.

- **infinity_scroll**: `true` - Указывает на то, что на странице есть бесконечная прокрутка.

## Чекбоксы для категорий

Поле `checkboxes_for_categories` указывает, используются ли чекбоксы для фильтрации категорий.

- **checkboxes_for_categories**: `false` - Указывает, что чекбоксы не используются.

## Категория

Секция `category` содержит локаторы для элементов, связанных с категорией.

### `pages_listing_locator`

**Описание**: Локатор для списка страниц.

- **attribute**: "innerHTML" - Атрибут элемента, который будет использован.
- **by**: "css selector" - Тип локатора.
- **selector**: "infinity_scroll" - CSS-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

## Топ-баннер

### `top_banner_locator`

**Описание**: Локатор для верхнего баннера на странице.

-   **attribute**: `{"src" : null}` - Атрибут элемента, который будет использован.
-   **by**: "XPATH" - Тип локатора.
-   **selector**: "//ul[contains(@class , 'slider animated')]//img" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

## Продукт

Секция `product` содержит локаторы для элементов на странице продукта.

### `link_to_product_locator`

**Описание**: Локатор для ссылки на страницу продукта.

- **attribute**: "href" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//a[contains(@class,'MuiTypography') and contains(@href , 'web/item')]" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `product_block_locator`

**Описание**: Локатор для блока продукта.

- **attribute**: "innerHTML" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//*[@id='product-page-root']" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `sku_locator`

**Описание**: Локатор для SKU (артикула) продукта.

- **attribute**: "innerText" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//*[contains(@data-id, 'product-')]/span" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `product_name_locator`

**Описание**: Локатор для названия продукта.

- **attribute**: "innerText" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **replaced by driver.title**: `null` - Указывает, что значение будет заменено на `driver.title`
- **selector**: "//*[@id='product-page-root']//h1//span" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `price_locator`

**Описание**: Локатор для цены продукта.

- **attribute**: "innerText" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//*[@id='product-page-root']//div[@aria-label]//div[text()]" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `product_delivery_locator`

**Описание**: Локатор для информации о доставке продукта.

-   **attribute**: `null` - Атрибут элемента, который будет использован.
-   **by**: "XPATH" - Тип локатора.
- **selector**: "//h2[contains(@aria-label ,'אפשרויות איסוף ומשלו')]//following::ul//li[contains(@aria-label ,'משלוח')]" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `main_image_locator`

**Описание**: Локатор для главного изображения продукта.

-   **attribute**: `null` - Атрибут элемента, который будет использован.
-   **by**: "XPATH" - Тип локатора.
-   **selector**: "//li[contains(@class ,'slide selected')]//div//img" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: "screenshot()" - Событие, которое будет выполнено

### `summary_locator`

**Описание**: Локатор для краткого описания продукта.

- **attribute**: "innerHTML" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//p[contains(text(),'תיאור קצר')]//following-sibling::p[1]" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `description_locator`

**Описание**: Локатор для полного описания продукта.

- **attribute**: "innerText" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//div[contains(@id , 'review-section')]" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `specification_locator`

**Описание**: Локатор для спецификации продукта.

-   **attribute**: `null` - Атрибут элемента, который будет использован.
-   **by**: "XPATH" - Тип локатора.
-   **selector**: "//div[contains(@id , 'review-section')]" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

### `customer_reviews_locator`

**Описание**: Локатор для отзывов покупателей. В данный момент равен `null`.

-   **customer_reviews_locator**: `null` - Локатор отсутствует.

### `product_attributes_locator`

**Описание**: Локатор для атрибутов продукта.

- **attribute**: "innerHTML" - Атрибут элемента, который будет использован.
- **by**: "XPATH" - Тип локатора.
- **selector**: "//*[@id='product-page-root']//div[@aria-label]//following-sibling::div/p[1]" - XPATH-селектор для элемента.
-  **timeout**: 0 - Тайм-аут ожидания элемента.
-  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
-   **event**: null - Событие, которое будет выполнено

    #### `color`

     **Описание**: Локатор для выбора цвета.
     -    **attribute**: `null` - Атрибут элемента, который будет использован.
     -   **by**: "XPATH" - Тип локатора.
     -   **selector**: "//h3[contains(@aria-label , 'בחירת צבע')]/following-sibling::*" - XPATH-селектор для элемента.
      -  **timeout**: 0 - Тайм-аут ожидания элемента.
     -  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
     -   **event**: null - Событие, которое будет выполнено

    #### `phone_memory`

    **Описание**: Локатор для выбора памяти телефона.
     -    **attribute**: `null` - Атрибут элемента, который будет использован.
     -   **by**: "XPATH" - Тип локатора.
     -   **selector**: "//h3[contains(@aria-label , 'בחירת נפח')]/following-sibling::*" - XPATH-селектор для элемента.
      -  **timeout**: 0 - Тайм-аут ожидания элемента.
     -  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
     -   **event**: null - Событие, которое будет выполнено

    #### `delivery`

    **Описание**: Локатор для выбора доставки.
     -    **attribute**: `null` - Атрибут элемента, который будет использован.
     -   **by**: "XPATH" - Тип локатора.
     -   **selector**: "//h3[contains(@aria-label , 'אפשרויות איסוף ומשלוח')]/following-sibling::*" - XPATH-селектор для элемента.
      -  **timeout**: 0 - Тайм-аут ожидания элемента.
     -  **timeout_for_event**: "presence_of_element_located" - Событие, которое нужно ожидать.
     -   **event**: null - Событие, которое будет выполнено