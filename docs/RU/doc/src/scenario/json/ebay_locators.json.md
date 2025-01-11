# Документация для `ebay_locators.json`

## Обзор

Данный файл `ebay_locators.json` содержит JSON-структуру, определяющую локаторы элементов веб-страницы eBay для автоматизации действий. Локаторы сгруппированы по логическим секциям, таким как "login", "pagination" и "product". Каждый локатор содержит параметры для его поиска и взаимодействия с элементом на странице.

## Оглавление

- [Обзор](#обзор)
- [Раздел "login"](#раздел-login)
  - [Локатор "open_login"](#локатор-open_login)
  - [Локатор "user_id"](#локатор-user_id)
  - [Локатор "button_continue_login"](#локатор-button_continue_login)
  - [Локатор "password"](#локатор-password)
  - [Локатор "button_login"](#локатор-button_login)
- [Раздел "pagination"](#раздел-pagination)
  - [Локатор "->"](#локатор--)
- [Раздел "product"](#раздел-product)
    - [Локатор "product_block_locator"](#локатор-product_block_locator)
    - [Локатор "link_to_product_locator"](#локатор-link_to_product_locator)
    - [Локатор "product_name_locator"](#локатор-product_name_locator)
    - [Локатор "brand_locator"](#локатор-brand_locator)
    - [Локатор "sku_locator"](#локатор-sku_locator)
    - [Локатор "brand_sku_locator"](#локатор-brand_sku_locator)
    - [Локатор "summary_locator"](#локатор-summary_locator)
    - [Локатор "description_locator"](#локатор-description_locator)
    - [Локатор "images_locator"](#локатор-images_locator)
    - [Локатор "main_image_locator"](#локатор-main_image_locator)
    - [Локатор "price_locator"](#локатор-price_locator)
    - [Локатор "qty_locator"](#локатор-qty_locator)
    - [Локатор "condition_locator"](#локатор-condition_locator)

## Раздел "login"

### Локатор "open_login"

**Описание**: Локатор для кнопки "Sign in" для открытия формы входа.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//a[. = 'Sign in']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `if_list`: `"first"`
- `use_mouse`: `false`

### Локатор "user_id"

**Описание**: Локатор для поля ввода "User ID".

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//input[@id = 'userid']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"send_keys('one.last.bit@gmail.com')"`
- `if_list`: `"first"`
- `use_mouse`: `false`

### Локатор "button_continue_login"

**Описание**: Локатор для кнопки "Continue" на странице логина.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//button[@id = 'signin-continue-btn']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `if_list`: `"first"`
- `use_mouse`: `false`

### Локатор "password"

**Описание**: Локатор для поля ввода пароля.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//input[@id = '...']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"send_keys('bG4I8y_oiOh9')"`
- `if_list`: `"first"`
- `use_mouse`: `false`

### Локатор "button_login"

**Описание**: Локатор для кнопки "Sign in" для завершения входа.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//button[@id = 'sgnBt']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `if_list`: `"first"`
- `use_mouse`: `false`

## Раздел "pagination"

### Локатор "->"

**Описание**: Локатор для кнопки "Next page" для пагинации.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//a[contains(@class,'pagination__next')]"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"click()"`
- `if_list`: `"first"`
- `use_mouse`: `false`

## Раздел "product"

### Локатор "product_block_locator"

**Описание**: Локатор для блока с информацией о продукте.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerHTML"`
- `by`: `"css selector"`
- `selector`: `"div.boxItem-wrap"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`
- `if_list`: `"first"`
- `use_mouse`: `false`

### Локатор "link_to_product_locator"

**Описание**: Локатор для ссылки на страницу продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"href"`
- `by`: `"XPATH"`
- `selector`: `"//div[@id='srp-river-results']//a[@class='s-item__link' and not(@aria-hidden='true')]"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "product_name_locator"

**Описание**: Локатор для имени продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerText"`
- `by`: `"XPATH"`
- `selector`: `"//h1[contains(@class,'mainTitle')]"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "brand_locator"

**Описание**: Локатор для бренда продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerHTML"`
- `by`: `"css selector"`
- `selector`: `".brands"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "sku_locator"

**Описание**: Локатор для артикула продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerHTML"`
- `by`: `"css selector"`
- `selector`: `"div[class=sku] span[itemprop='sku']"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "brand_sku_locator"

**Описание**: Локатор для артикула продукта (дубликат).

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerHTML"`
- `by`: `"css selector"`
- `selector`: `"div[class=sku] span[itemprop='sku']"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "summary_locator"

**Описание**: Локатор для краткого описания продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerHTML"`
- `by`: `"XPATH"`
- `selector`: `"//div[@class=product-name]//h1[itemprop()='name']"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "description_locator"

**Описание**: Локатор для полного описания продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerHTML"`
- `by`: `"XPATH"`
- `selector`: `"//div[contains(@class, 'x-about-this-item')]"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "images_locator"

**Описание**: Локатор для изображений продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"src"`
- `by`: `"XPATH"`
- `selector`: `"//div[contains(@class,'ux-image-carousel-item')]//img"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "main_image_locator"

**Описание**: Локатор для основного изображения продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `null`
- `by`: `"XPATH"`
- `selector`: `"//div[@class='ux-image-carousel-item active image']"`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `"screenshot()"`
- `if_list`: `"first"`
- `use_mouse`: `false`

### Локатор "price_locator"

**Описание**: Локатор для цены продукта.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerText"`
- `by`: `"XPATH"`
- `selector`: `"//span[@class = 'x-price-approx__price']"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "qty_locator"

**Описание**: Локатор для количества продукта.

**Параметры**:
- `by`: `"XPATH"`
- `selector`: `"//span[@id = 'qtySubTxt']"`
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerText"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`

### Локатор "condition_locator"

**Описание**: Локатор для состояния продукта.

**Параметры**:
- `by`: `"XPATH"`
- `selector`: `"//div[@class='d-item-condition-text']//following-sibling::span[@class = 'ux-textspans']"`
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`
- `attribute`: `"innerText"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`
- `timeout`: `0`
- `timeout_for_event`: `"presence_of_element_located"`
- `event`: `null`