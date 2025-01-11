# grandadvance_categories_keyboards_microsoft.json

## Обзор

Файл содержит JSON-объект, описывающий категории товаров "MICROSOFT" для клавиатур и мышей с настройками для импорта в Prestashop. Каждая запись определяет бренд, URL, активность, состояние и категории PrestaShop для конкретного продукта.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Описание полей](#описание-полей)

## Структура JSON

Файл представляет собой JSON-объект, где ключами являются названия категорий товаров MICROSOFT (например, "MICROSOFT WIRELESS KEYBOARD"), а значениями являются объекты, содержащие информацию о каждом продукте.

```json
{
  "MICROSOFT WIRELESS KEYBOARD": {
    "brand": "MICROSOFT",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manId=14",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,204,316"
  },
  "MICROSOFT USB KEYBOARD": {
    "brand": "MICROSOFT",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=589&manId=14",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,204,315"
  },
  "MICROSOFT USB MOUSE": {
    "brand": "MICROSOFT",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manId=14",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,206,317"
  },
  "MICROSOFT WIRELESS MOUSE": {
    "brand": "MICROSOFT",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=586&manId=14",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,206,318"
  },
  "MICROSOFT USB KEYBOARD-MOUSE SET": {
    "brand": "MICROSOFT",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=14",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,207,208"
  },
  "MICROSOFT WIRELESS  KEYBOARD-MOUSE SET": {
    "brand": "MICROSOFT",
    "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=14",
    "checkbox": false,
    "active": true,
     "condition":"new",
    "presta_categories": "203,207,334"
  }
}
```

## Описание полей

- **`brand`**:
  - **Описание**: Название бренда товара.
  - **Тип**: `str`
  - **Пример**: `"MICROSOFT"`

- **`url`**:
  - **Описание**: URL-адрес страницы товара на сайте поставщика.
  - **Тип**: `str`
  - **Пример**: `"https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manId=14"`

-  **`checkbox`**:
    -   **Описание**: Флаг, указывающий, выбран ли товар (в данном случае всегда `false`).
    -   **Тип**: `bool`
    -   **Пример**: `false`

- **`active`**:
  - **Описание**: Флаг, указывающий, активен ли товар.
  - **Тип**: `bool`
  - **Пример**: `true`

-   **`condition`**:
    -   **Описание**: Состояние товара.
    -   **Тип**: `str`
    -   **Пример**: `"new"`

- **`presta_categories`**:
  - **Описание**:  Список идентификаторов категорий PrestaShop, к которым относится товар.
  - **Тип**: `str`
  - **Пример**: `"203,204,316"`