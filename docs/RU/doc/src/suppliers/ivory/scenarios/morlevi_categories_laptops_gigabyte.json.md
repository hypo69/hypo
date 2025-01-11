# Документация для `morlevi_categories_laptops_gigabyte.json`

## Обзор

Этот файл содержит JSON-конфигурацию сценариев для сопоставления категорий ноутбуков GIGABYTE в магазине Morlevi с категориями в PrestaShop. Каждый сценарий определяет условия для ноутбуков GIGABYTE на основе размера экрана и типа процессора, а также связывает их с определенными категориями в PrestaShop.

## Оглавление

1. [Сценарии](#сценарии)
    - [Описание структуры](#описание-структуры)
    - [Примеры сценариев](#примеры-сценариев)

## Сценарии

### Описание структуры

JSON-файл содержит корневой объект с ключом `"scenarios"`. Значением этого ключа является объект, где каждый ключ представляет собой название сценария (например, `"GIGABYTE 11.6 I3"`). Каждый сценарий имеет следующую структуру:

-   `brand` (str): Бренд ноутбука, всегда `"GIGABYTE"`.
-   `url` (str | null): URL для фильтрации товаров на сайте Morlevi, если применимо, иначе `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе (всегда `false`).
-   `active` (bool): Флаг активации сценария (всегда `true`).
-   `condition` (str): Состояние товара (всегда `"new"`).
-   `presta_categories` (dict): Объект, определяющий категории PrestaShop. Содержит ключ `"template"` со вложенным объектом, где ключ `"gigabyte"` содержит список категорий PrestaShop, к которым относится ноутбук.

### Примеры сценариев

#### GIGABYTE 11.6 I3

```json
"GIGABYTE 11.6 I3": {
    "brand": "GIGABYTE",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
        "template": {
            "gigabyte": [
                "LAPTOPS INTEL I3",
                "11"
            ]
        }
    }
}
```

Ноутбук GIGABYTE с диагональю экрана 11.6 дюймов и процессором Intel i3 будет отнесен к категориям `"LAPTOPS INTEL I3"` и `"11"` в PrestaShop.

#### GIGABYTE 15 I5

```json
"GIGABYTE 15 I5": {
    "brand": "GIGABYTE",
    "url": "https://www.morlevi.co.il/Cat/358?p_315=2&p_238=1145&p_387=3414&sort=datafloat2%2Cprice&keyword=",
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
        "template": {
            "gigabyte": [
                "LAPTOPS INTEL I5",
                "15"
            ]
        }
    }
}
```

Ноутбук GIGABYTE с диагональю экрана 15 дюймов и процессором Intel i5 будет отнесен к категориям `"LAPTOPS INTEL I5"` и `"15"` в PrestaShop. Также предоставляется URL для фильтрации товаров на сайте Morlevi.

#### GIGABYTE 17.3 AMD

```json
"GIGABYTE 17.3 AMD": {
    "brand": "GIGABYTE",
    "url": null,
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": {
        "template": {
            "gigabyte": [
                "LAPTOPS AMD",
                "17"
            ]
        }
    }
}
```

Ноутбук GIGABYTE с диагональю экрана 17.3 дюйма и процессором AMD будет отнесен к категориям `"LAPTOPS AMD"` и `"17"` в PrestaShop.

## Заключение

Этот JSON-файл является важным элементом для интеграции данных между Morlevi и PrestaShop, обеспечивая правильное сопоставление категорий ноутбуков GIGABYTE. Документация поможет разработчикам понять структуру и назначение файла, а также упростит процесс его модификации и обновления.