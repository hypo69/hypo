# Локаторы магазина Wallashop

## Обзор

Файл `store.json` содержит JSON-объект с локаторами для элементов пользовательского интерфейса (UI) магазина Wallashop. Эти локаторы используются для автоматизации тестирования и взаимодействия с элементами на веб-странице магазина.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [Общие локаторы](#общие-локаторы)
  - [Локаторы для элементов главной страницы](#локаторы-для-элементов-главной-страницы)
    - [Меню](#меню)
    - [Слайдер](#слайдер)
    - [Модальное окно](#модальное-окно)
  - [Локаторы для элементов страниц категорий](#локаторы-для-элементов-страниц-категорий)
    - [Фильтры](#фильтры)
    - [Список товаров](#список-товаров)
  - [Локаторы для элементов страницы товара](#локаторы-для-элементов-страницы-товара)
  - [Локаторы для корзины](#локаторы-для-корзины)

## Структура JSON

Файл `store.json` представляет собой JSON-объект со структурой, организованной по разделам, каждый из которых содержит локаторы для различных частей пользовательского интерфейса магазина Wallashop.

### Общие локаторы

Общие локаторы, которые используются на разных страницах сайта, например, загрузчики, поля поиска и т.д.

```json
{
  "common": {
    "loader": "//div[@class='loader-wrapper']",
    "search_field": "//input[@placeholder='Найти товар']",
    "search_button": "//button[@class='search-button']",
    "close_modal_button": "//button[@class='modal-close-button']"
  },
  "home_page": {
    "menu": {
      "category_button": "//button[@class='category-menu-button']",
       "sub_category_link": "//a[contains(@href, '/category/') and contains(@class, 'sub-menu-item')]",
      "sub_category_button": "//a[contains(@href, '/category/') and contains(@class, 'sub-menu-item')]/div"
    },
    "slider": {
         "next_slide_button": "//button[@class='slider-next']",
         "previous_slide_button": "//button[@class='slider-prev']",
         "current_slide": "//div[@class='slider-dot slider-dot--active']"
      },
    "modal":{
        "modal_window": "//div[@class='modal']"
       }
  },
  "category_page": {
      "filters":{
          "filter_block": "//div[@class='filter']",
          "filter_header": "//div[@class='filter-header']",
           "filter_checkbox": "//input[@type='checkbox']",
           "filter_checkbox_label": "//label",
           "filter_show_button":"//button[@class='filter-show-button']",
          "filter_hide_button":"//button[@class='filter-hide-button']"
      },
    "products":{
         "product_card": "//div[@class='product-card']",
         "product_name": "//div[@class='product-card-name']",
         "product_price": "//div[@class='product-card-price']"
    }
  },
  "product_page": {
       "product_title": "//h1[@class='product-title']",
       "product_price": "//div[@class='product-price']",
       "add_to_cart_button":"//button[text()='В корзину']",
       "product_quantity_field": "//input[@type='number']"
  },
 "cart":{
      "cart_item": "//div[@class='cart-item']",
      "cart_item_name": "//div[@class='cart-item-name']",
      "cart_item_price": "//div[@class='cart-item-price']",
       "cart_item_remove_button": "//button[@class='cart-item-remove']",
       "cart_total_price": "//div[@class='cart-total-price']",
       "cart_checkout_button": "//button[@class='cart-checkout-button']"
    }
}
```

### Локаторы для элементов главной страницы

Включают локаторы для меню категорий, слайдера и модального окна.

#### Меню

Содержит локаторы для кнопок категорий и подкатегорий.

- `category_button`: Локатор для кнопки вызова меню категорий.
- `sub_category_link`: Локатор для ссылок на подкатегории.
- `sub_category_button`: Локатор для кнопок подкатегорий.

#### Слайдер

Содержит локаторы для управления слайдером.

- `next_slide_button`: Локатор для кнопки перехода к следующему слайду.
- `previous_slide_button`: Локатор для кнопки перехода к предыдущему слайду.
- `current_slide`: Локатор для текущего активного слайда.

#### Модальное окно

Содержит локаторы для модальных окон.

- `modal_window`: Локатор для модального окна.

### Локаторы для элементов страниц категорий

Включают локаторы для фильтров товаров и списка товаров.

#### Фильтры

Содержит локаторы для блоков фильтров, заголовков, чекбоксов и кнопок фильтров.

- `filter_block`: Локатор для блока фильтра.
- `filter_header`: Локатор для заголовка фильтра.
- `filter_checkbox`: Локатор для чекбокса фильтра.
- `filter_checkbox_label`: Локатор для надписи чекбокса фильтра.
- `filter_show_button`: Локатор для кнопки показа фильтров.
- `filter_hide_button`: Локатор для кнопки скрытия фильтров.

#### Список товаров

Содержит локаторы для карточек товаров.

- `product_card`: Локатор для карточки товара.
- `product_name`: Локатор для названия товара.
- `product_price`: Локатор для цены товара.

### Локаторы для элементов страницы товара

Содержит локаторы для элементов на странице товара.

- `product_title`: Локатор для заголовка товара.
- `product_price`: Локатор для цены товара.
- `add_to_cart_button`: Локатор для кнопки добавления товара в корзину.
- `product_quantity_field`: Локатор для поля ввода количества товара.

### Локаторы для корзины

Содержит локаторы для элементов корзины.

- `cart_item`: Локатор для элемента корзины.
- `cart_item_name`: Локатор для названия товара в корзине.
- `cart_item_price`: Локатор для цены товара в корзине.
- `cart_item_remove_button`: Локатор для кнопки удаления товара из корзины.
- `cart_total_price`: Локатор для общей цены товаров в корзине.
- `cart_checkout_button`: Локатор для кнопки оформления заказа.