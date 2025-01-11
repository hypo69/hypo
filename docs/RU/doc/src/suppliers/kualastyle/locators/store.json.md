# Описание файла `store.json`

## Обзор

Файл `store.json` содержит JSON-структуру с локаторами элементов для страницы магазина Kualastyle. Эти локаторы используются для автоматизации тестирования и сбора данных. Файл организован в виде словаря, где ключи представляют собой осмысленные названия элементов страницы, а значения – это словари, содержащие информацию о локаторах.

## Содержание

- [Структура файла](#структура-файла)
- [Пример локаторов](#пример-локаторов)

## Структура файла

Файл представляет собой JSON-объект, содержащий единственный словарь. Ключами этого словаря являются строковые идентификаторы элементов страницы магазина Kualastyle. Каждое значение ключа является еще одним словарем, содержащим следующие поля:

-   `locator_type`: Тип локатора (например, "xpath", "css").
-   `locator`: Строка, представляющая локатор элемента.

## Пример локаторов

```json
{
    "filter_by_color_button": {
      "locator_type": "xpath",
      "locator": "//div[@class = 'filter-options__item' and descendant::span[text() = 'Цвет']]"
    },
    "first_color_in_filter": {
      "locator_type": "xpath",
      "locator": "//div[@class = 'filter-options__item' and descendant::span[text() = 'Цвет']]/following-sibling::div//label[1]"
    },
    "show_products_button": {
      "locator_type": "xpath",
      "locator": "//button[contains(text(), 'Показать')]"
    },
    "product_card": {
      "locator_type": "xpath",
      "locator": "//div[@class = 'product-card']"
    },
    "product_name_in_card": {
        "locator_type": "xpath",
        "locator": ".//a[@class = 'product-card__title']"
    },
     "product_price_in_card": {
        "locator_type": "xpath",
        "locator": ".//span[@class = 'product-card__price']"
     },
    "product_card_link": {
        "locator_type": "xpath",
        "locator": ".//a[@class = 'product-card__img-link']"
    },
    "product_cards_in_page": {
      "locator_type": "xpath",
      "locator": "//div[@class = 'product-card']"
    },
    "filter_block_title": {
      "locator_type": "xpath",
      "locator": "//div[@class = 'filter__title']"
    }
  }
```

### `filter_by_color_button`

**Описание**: Локатор кнопки фильтрации по цвету.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение кнопки.

### `first_color_in_filter`

**Описание**: Локатор первого варианта цвета в фильтре.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение элемента.

### `show_products_button`

**Описание**: Локатор кнопки для отображения отфильтрованных продуктов.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение кнопки.

### `product_card`

**Описание**: Локатор для карточки товара.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение карточки товара.

### `product_name_in_card`

**Описание**: Локатор для названия товара внутри карточки.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение названия товара.

### `product_price_in_card`

**Описание**: Локатор для цены товара внутри карточки.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение цены товара.

### `product_card_link`

**Описание**: Локатор для ссылки на страницу товара в карточке.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение ссылки.

### `product_cards_in_page`

**Описание**: Локатор для всех карточек товаров на странице.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение всех карточек.

### `filter_block_title`

**Описание**: Локатор для заголовка блока фильтрации.

**Параметры**:
-   `locator_type` (str): Тип локатора ("xpath").
-   `locator` (str): Строка XPath, определяющая расположение заголовка блока.