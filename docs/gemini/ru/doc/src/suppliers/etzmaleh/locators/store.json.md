# Описание локаторов магазина ETZ Maleh

## Обзор

Файл `store.json` содержит JSON-структуру, описывающую локаторы элементов пользовательского интерфейса для магазина ETZ Maleh. Эти локаторы используются для автоматизации тестирования и взаимодействия с веб-сайтом магазина.

## Содержание

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [Примеры](#примеры)

## Структура файла

Файл представляет собой JSON-объект, содержащий следующие ключи:

- `general_search`: Локаторы, связанные с общим поиском.
- `product_card`: Локаторы, связанные с карточками продуктов.
- `product_page`: Локаторы, связанные со страницами отдельных продуктов.
- `cart`: Локаторы, связанные с корзиной.

### Общие локаторы поиска

-   `input`: Локатор для поля ввода поиска.
-  `result`: Локатор для результатов поиска.

### Локаторы карточки продукта

- `product`: Локатор для контейнера карточки продукта.
- `title`: Локатор для заголовка продукта.
- `price`: Локатор для цены продукта.
- `add_to_cart_button`: Локатор для кнопки добавления товара в корзину.
- `product_image`: Локатор для изображения товара.

### Локаторы страницы продукта

- `title`: Локатор для заголовка продукта на странице продукта.
- `price`: Локатор для цены продукта на странице продукта.
- `add_to_cart_button`: Локатор для кнопки добавления товара в корзину на странице продукта.
- `description`: Локатор для описания продукта на странице продукта.
- `gallery`: Локатор для галереи изображений продукта.
- `breadcrumb`: Локатор для хлебных крошек на странице продукта.

### Локаторы корзины

-   `cart_item`: Локатор для элемента корзины.
-  `total`: Локатор для общей суммы корзины.
-  `checkout_button`: Локатор для кнопки оформления заказа.
-  `delete_button`: Локатор для кнопки удаления элемента из корзины.

## Примеры

```json
{
  "general_search": {
    "input": {
      "by": "css",
      "value": "#search"
    },
        "result": {
      "by": "css",
      "value": ".products-list"
    }
  },
  "product_card": {
    "product": {
      "by": "css",
      "value": ".product"
    },
    "title": {
      "by": "css",
      "value": ".product-title"
    },
    "price": {
      "by": "css",
      "value": ".product-price"
    },
    "add_to_cart_button": {
      "by": "css",
      "value": ".add-to-cart"
    },
    "product_image": {
     "by": "css",
     "value": ".product-image img"
    }
  },
  "product_page": {
     "title": {
      "by": "css",
      "value": ".product-details h1"
    },
    "price": {
      "by": "css",
      "value": ".product-price"
    },
    "add_to_cart_button": {
      "by": "css",
      "value": ".add-to-cart"
    },
    "description": {
      "by": "css",
      "value": ".product-description"
    },
    "gallery":{
     "by": "css",
     "value": ".product-gallery"
    },
        "breadcrumb": {
      "by": "css",
      "value": ".breadcrumb"
    }
  },
  "cart": {
      "cart_item": {
      "by": "css",
      "value": ".cart-item"
    },
     "total": {
      "by": "css",
      "value": ".cart-total"
    },
    "checkout_button":{
      "by": "css",
      "value": ".checkout-button"
    },
       "delete_button": {
      "by": "css",
      "value": ".delete-item"
    }
  }
}