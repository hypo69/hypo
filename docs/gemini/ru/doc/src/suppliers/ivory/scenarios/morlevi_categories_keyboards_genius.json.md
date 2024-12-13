# Документация для `morlevi_categories_keyboards_genius.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [scenarios](#scenarios)
    - [Описание сценариев](#описание-сценариев)
3. [Примеры](#примеры)

## Обзор

Данный файл `morlevi_categories_keyboards_genius.json` содержит JSON-структуру, описывающую сценарии для категорий товаров (клавиатуры и мыши) бренда "GENIUS" с сайта morlevi.co.il. Файл предназначен для конфигурации процесса сбора и обработки данных о товарах.

## Структура JSON

### `scenarios`
Объект `scenarios` является основным контейнером, содержащим наборы сценариев. Каждый ключ в `scenarios` представляет собой название сценария.

### Описание сценариев

Каждый сценарий представляет собой объект со следующими ключами:

- **`brand`** (str): Бренд товара. В данном файле всегда `"GENIUS"`.
- **`url`** (str): URL-адрес страницы на сайте morlevi.co.il, откуда необходимо собирать данные. 
- **`checkbox`** (bool): Флаг, указывающий, нужно ли использовать чекбокс. Всегда `false`.
- **`active`** (bool): Флаг, указывающий, активен ли сценарий. Всегда `true`.
- **`condition`** (str): Состояние товара. Всегда `"new"`.
- **`presta_categories`** (str):  Строка, содержащая ID категорий в PrestaShop, разделенные запятыми.

## Примеры

Примеры сценариев, описанных в данном файле:

```json
{
  "scenarios": {
    "GENIUS WIRELESS KEYBOARD": {
      "brand": "GENIUS",
      "url": "-----------------------------------------------GENIUS WIRELESS KEYBOARD----------------------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,204,316"
    },
    "GENIUS USB KEYBOARD": {
      "brand": "GENIUS",
      "url": "https://www.morlevi.co.il/Cat/155?p_315=43&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,204,315"
    },
    "GENIUS USB MOUSE": {
      "brand": "GENIUS",
      "url": "https://www.morlevi.co.il/Cat/108?p_315=43&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,206,317"
    },
    "GENIUS WIRELESS MOUSE": {
      "brand": "GENIUS",
      "url": "https://www.morlevi.co.il/Cat/109?p_315=43&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "203,206,318"
    },
    "GENIUS USB KEYBOARD-MOUSE SET": {
      "brand": "GENIUS",
      "url": "https://www.morlevi.co.il/Cat/113?p_315=43&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
       "presta_categories": "203,207,208"
    },
    "GENIUS WIRELESS  KEYBOARD-MOUSE SET": {
      "brand": "GENIUS",
      "url": "https://www.morlevi.co.il/Cat/114?p_315=43&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "203,207,334"
    }
  }
}
```