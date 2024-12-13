# Документация для `morlevi_categories_psu_corsair.json`

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для парсинга блоков питания (PSU) бренда CORSAIR с сайта Morlevi. Каждый сценарий описывает конкретную модель блока питания, включая его мощность, URL для парсинга, и соответствующие категории PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
    - [Сценарии](#сценарии)
        - [CORSAIR 450W](#corsair-450w)
        - [CORSAIR 500W](#corsair-500w)
        - [CORSAIR 550W](#corsair-550w)
        - [CORSAIR 600W](#corsair-600w)
        - [CORSAIR 650W](#corsair-650w)
        - [CORSAIR 700W](#corsair-700w)
        - [CORSAIR 750W](#corsair-750w)
        - [CORSAIR 850W](#corsair-850w)
        - [CORSAIR 1000W](#corsair-1000w)
        - [CORSAIR 1200W](#corsair-1200w)
        - [CORSAIR 1600W](#corsair-1600w)

## Структура файла

Файл имеет следующую структуру:

```json
{
  "scenarios": {
    "Имя сценария 1": {
      "brand": "Бренд",
      "name": "Название модели",
      "url": "URL для парсинга",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "Список категорий PrestaShop"
    },
    "Имя сценария 2": {
      "brand": "Бренд",
      "name": "Название модели",
      "url": "URL для парсинга",
       "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "Список категорий PrestaShop"
    },
    ...
  }
}
```

### Сценарии

#### CORSAIR 450W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 450W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "450W" - название модели.
    - `url` (str): "--------------------------------------CORSAIR 450W-------------------------------------------" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
    - `presta_categories` (str): "158,511,188,580" - список категорий PrestaShop.

#### CORSAIR 500W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 500W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "500W" - название модели.
    - `url` (str): "https://www.morlevi.co.il/Cat/67?p_145=678&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
    - `presta_categories` (str): "158,511,189,580" - список категорий PrestaShop.

#### CORSAIR 550W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 550W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "550W" - название модели.
    - `url` (str): "---------------------------------CORSAIR 550W--------------------------------------" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
    - `presta_categories` (str): "151,158,511,190,580" - список категорий PrestaShop.

#### CORSAIR 600W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 600W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "600W" - название модели.
    - `url` (str): "--------------------------------------CORSAIR 600W-------------------------------------------" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,191,580" - список категорий PrestaShop.

#### CORSAIR 650W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 650W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "650W" - название модели.
    - `url` (str): "https://www.morlevi.co.il/Cat/67?p_145=637&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,192,580" - список категорий PrestaShop.

#### CORSAIR 700W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 700W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "700W" - название модели.
    - `url` (str): "--------------------------------------CORSAIR 700W-------------------------------------------" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,193,580" - список категорий PrestaShop.

#### CORSAIR 750W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 750W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "750W" - название модели.
    - `url` (str): "https://www.morlevi.co.il/Cat/67?p_145=670&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,194,580" - список категорий PrestaShop.

#### CORSAIR 850W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 850W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "850W" - название модели.
    - `url` (str): "https://www.morlevi.co.il/Cat/67?p_145=672&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,571,580" - список категорий PrestaShop.

#### CORSAIR 1000W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 1000W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "1000W" - название модели.
    - `url` (str): "https://www.morlevi.co.il/Cat/67?p_145=674&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,572,580" - список категорий PrestaShop.

#### CORSAIR 1200W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 1200W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "1200W" - название модели.
    - `url` (str): "https://www.morlevi.co.il/Cat/67?p_145=677&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,573,580" - список категорий PrestaShop.

#### CORSAIR 1600W
  **Описание**: Сценарий для парсинга блока питания CORSAIR мощностью 1600W.
  
  **Параметры**:
    - `brand` (str): "CORSAIR" - бренд производителя.
    - `name` (str): "1600W" - название модели.
    - `url` (str): "https://www.morlevi.co.il/Cat/67?p_145=676&sort=datafloat2%2Cprice&keyword=" - URL для парсинга.
    - `checkbox` (bool): `false` - состояние чекбокса.
    - `active` (bool): `true` - активность сценария.
    - `condition` (str): "new" - состояние товара.
     - `presta_categories` (str): "151,158,511,574,580" - список категорий PrestaShop.