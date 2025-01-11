# Описание локаторов для магазина AliExpress

## Обзор

Этот файл содержит JSON-объект, представляющий локаторы для элементов интерфейса магазина AliExpress. Локаторы используются для автоматизации взаимодействия с веб-страницей AliExpress, например, для тестирования или сбора данных.

## Оглавление

- [Обзор](#обзор)
- [Локаторы](#локаторы)
  - [product_page_locators](#product_page_locators)
  - [search_page_locators](#search_page_locators)
  - [modal_locators](#modal_locators)
  - [common_locators](#common_locators)

## Локаторы

### `product_page_locators`

**Описание**: Локаторы для элементов на странице продукта.

```json
{
    "add_to_cart_button": "//button[contains(text(),'В корзину') or contains(text(),'Add to cart')]",
    "buy_now_button": "//button[contains(text(),'Купить сейчас') or contains(text(),'Buy now')]",
    "item_price": "//div[@class='product-price-current']//span[@class='price-value']",
    "item_title": "//h1[@class='product-title-text']",
    "item_rating": "//div[@class='product-rating-sum']//span[@class='star-sum-text']"
}
```
**Элементы**:
- `add_to_cart_button`: Локатор для кнопки "В корзину".
- `buy_now_button`: Локатор для кнопки "Купить сейчас".
- `item_price`: Локатор для элемента с ценой товара.
- `item_title`: Локатор для заголовка товара.
- `item_rating`: Локатор для рейтинга товара.

### `search_page_locators`
**Описание**: Локаторы для элементов на странице результатов поиска.

```json
{
    "search_input": "//input[@id='search-words']",
    "search_button": "//input[@class='search-button']",
     "item_link": "//a[@class='item-title']"
}
```

**Элементы**:
- `search_input`: Локатор для поля ввода поискового запроса.
- `search_button`: Локатор для кнопки поиска.
- `item_link`: Локатор для ссылки на товар в результатах поиска.

### `modal_locators`

**Описание**: Локаторы для элементов модальных окон.

```json
{
    "close_modal_button": "//div[@class='ui-window-close']"
}
```

**Элементы**:
- `close_modal_button`: Локатор для кнопки закрытия модального окна.

### `common_locators`

**Описание**: Локаторы для общих элементов, присутствующих на разных страницах.

```json
{
 "cookie_modal_close_button": "//button[@class='btn-close']"
}
```
**Элементы**:
- `cookie_modal_close_button`: Локатор для кнопки закрытия модального окна с cookie.