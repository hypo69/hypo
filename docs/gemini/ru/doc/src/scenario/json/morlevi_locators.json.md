# Документация к файлу `morlevi_locators.json`

## Обзор

Файл `morlevi_locators.json` содержит JSON-структуру с определениями локаторов для веб-элементов, используемых в автоматизированных тестах или скриптах для взаимодействия с веб-сайтом. Эти локаторы используются для поиска и идентификации элементов на веб-странице с помощью различных методов, таких как XPath и CSS-селекторы.

## Оглавление

- [Структура файла](#структура-файла)
- [Раздел `pagination`](#раздел-pagination)
- [Раздел `close_pop_up_locator`](#раздел-close_pop_up_locator)
- [Раздел `store`](#раздел-store)
- [Раздел `product`](#раздел-product)
- [Раздел `product_fields_locators`](#раздел-product_fields_locators)
- [Раздел `laptop_description_fields_selectors`](#раздел-laptop_description_fields_selectors)
- [Раздел `stock_locator`](#раздел-stock_locator)
- [Раздел `login`](#раздел-login)

## Структура файла

Файл представляет собой JSON-объект, содержащий различные разделы, каждый из которых определяет локаторы для определенных элементов или групп элементов на веб-странице.

## Раздел `pagination`

### Описание

Раздел содержит локаторы для элементов пагинации на странице.

### `ul`

**Описание**: Локатор для элемента `ul`, содержащего пагинацию.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `null`.
- `by`: `"XPATH"`.
- `selector`: `"//ul[@class='pagination']"`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"click()"`.

### `a`

**Описание**: Локатор для элементов `a`, представляющих ссылки на страницы пагинации.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `null`.
- `by`: `"XPATH"`.
- `selector`: `"//ul[@class='pagination']//a[@class='page-link']"`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"click()"`.

## Раздел `close_pop_up_locator`

### Описание

Раздел содержит локатор для кнопки закрытия всплывающего окна.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `null`.
- `by`: `"XPATH"`.
- `selector`: `"//div[@class='modal-dialog']//button[@class='close']"`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"click()"`.

## Раздел `store`

### Описание

Раздел содержит локаторы для элементов, связанных с магазином, например, категорий товаров.

### `store categories`

**Описание**: Локатор для списка категорий магазина.

**Параметры**:
- `description`: `"Список катагероий магазина"`.
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `{"innerText": "href"}`.
- `by`: `"XPATH"`.
- `selector`: `"//li[@class='group-item']//a"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

## Раздел `product`

### Описание

Раздел содержит локаторы для элементов, связанных с информацией о товаре на странице.

### `link_to_product_locator`

**Описание**: Локатор для ссылки на страницу товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"href"`.
- `by`: `"XPATH"`.
- `selector`: `"//div[@class = 'product-thumb']/a"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `stock available`

**Описание**: Локатор для элемента, отображающего наличие товара на складе.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerText"`.
- `by`: `"XPATH"`.
- `selector`: `"//div[conatins(@class , 'stockMsg')]"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `product_name_locator`

**Описание**: Локатор для названия товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `"h1.d-inline-block"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `summary_locator`

**Описание**: Локатор для краткого описания товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `"h1.d-inline-block"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `description_locator`

**Описание**: Локатор для полного описания товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `".row.product-params.pt-2.pb-2.pt-sm-5.pb-sm-5"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `price_locator`

**Описание**: Локатор для цены товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"ID"`.
- `selector`: `"basicPrice"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `brand_locator`

**Описание**: Локатор для бренда товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `"text*='éöøï'"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `sku_locator`

**Описание**: Локатор для SKU товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerText"`.
- `by`: `"XPATH"`.
- `selector`: `"//div[contains(@class,'main-details')]//span[contains(@class,'sku-copy')]"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `brand_sku_locator`

**Описание**: Локатор для SKU бренда.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `"span.sku-copy"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `main_image_locator`

**Описание**: Локатор для главного изображения товара.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"href"`.
- `by`: `"ID"`.
- `selector`: `"mainpic"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `li_locator`

**Описание**: Локатор для элементов `li`.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"tag name"`.
- `selector`: `"li"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

## Раздел `product_fields_locators`

### Описание

Раздел предназначен для хранения локаторов дополнительных полей товаров, но в текущей версии пуст.

## Раздел `laptop_description_fields_selectors`

### Описание

Раздел содержит локаторы для полей описания ноутбуков.

### `screen`

**Описание**: Локатор для поля экрана ноутбука.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `"text*='âåãì îñê'"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `CPUTYPE`

**Описание**: Локатор для поля типа процессора.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `"text*='CPUTYPE'"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

### `cpu`

**Описание**: Локатор для поля процессора.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `"text='îòáã'"`
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

## Раздел `stock_locator`

### Описание

Раздел содержит локатор для элемента, отображающего информацию о наличии на складе.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `"innerHTML"`.
- `by`: `"css selector"`.
- `selector`: `".stockMsg"`.
- `logic for action[AND|OR|XOR|VALUE|null]`: `null`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `null`.

## Раздел `login`

### Описание

Раздел содержит локаторы и учетные данные для авторизации пользователя.

### `open_login_dialog_locator`

**Описание**: Локатор для кнопки открытия диалогового окна входа.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `null`.
- `by`: `"XPATH"`.
- `selector`: `"//a[contains(@data-modal,'User')]"`
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"click()"`.

### `email`

**Описание**: Email пользователя для входа.

**Значение**: `"sales@aluf.co.il"`.

### `email_locator`

**Описание**: Локатор для поля ввода email.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `null`.
- `by`: `"ID"`.
- `selector`: `"Email"`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"send_keys('sales@aluf.co.il')"`

### `password`

**Описание**: Пароль пользователя для входа.

**Значение**: `"9643766"`.

### `password_locator`

**Описание**: Локатор для поля ввода пароля.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `null`.
- `by`: `"ID"`.
- `selector`: `"Password"`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"send_keys('9643766')"`

### `loginbutton_locator`

**Описание**: Локатор для кнопки входа.

**Параметры**:
- `logic for attribue[AND|OR|XOR|VALUE|null]`: `null`.
- `attribute`: `null`.
- `by`: `"css selector"`.
- `selector`: `".btn.btn-primary.btn-lg.w-50.float-left.mr-2"`.
- `timeout`: `0`.
- `timeout_for_event`: `"presence_of_element_located"`.
- `event`: `"click()"`.