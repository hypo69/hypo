# Документация для `visualdg_categories_laptops_lenovo_yoga.json`

## Обзор

Файл `visualdg_categories_laptops_lenovo_yoga.json` содержит JSON-структуру, описывающую сценарии для категорий ноутбуков Lenovo Yoga. Каждый сценарий включает информацию о бренде, шаблоне, URL-адресе, активности, состоянии и соответствующих категориях PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Описание сценариев](#описание-сценариев)

## Структура JSON

JSON-файл содержит один корневой объект с ключом `"scenarios"`, значением которого является объект, содержащий сценарии для ноутбуков Lenovo Yoga. Каждый сценарий представлен в виде объекта, ключом которого является название сценария (например, `"LENOVO YOGA 13.4 - 13.3 I3"`).

## Описание сценариев

Каждый сценарий имеет следующие атрибуты:

- `"brand"` (строка): Бренд ноутбука, всегда `"LENOVO"` в данном файле.
- `"template"` (строка): Шаблон ноутбука, всегда `"YOGA"` в данном файле.
- `"url"` (строка): URL-адрес, связанный с данным сценарием. Может быть как реальным URL, так и строкой-заглушкой.
- `"checkbox"` (логическое значение): Флаг, указывающий на наличие чекбокса. Всегда `false` в данном файле.
- `"active"` (логическое значение): Флаг, указывающий на активность сценария. Всегда `true` в данном файле.
- `"condition"` (строка): Состояние товара, всегда `"new"` в данном файле.
- `"presta_categories"` (строка): Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

### Примеры сценариев:

#### LENOVO YOGA 13.4 - 13.3 I3

```json
"LENOVO YOGA 13.4 - 13.3 I3": {
  "brand": "LENOVO",
  "template": "YOGA",
  "url": "-----------------YOGA 13.4 - 13.3 I3-------------r ",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": "3,53,306,9,4,370,839"
}
```

**Описание**: Сценарий для ноутбука Lenovo Yoga с процессором Intel Core i3 и диагональю экрана 13.3-13.4 дюйма.

**Параметры**:

- `brand`: "LENOVO"
- `template`: "YOGA"
- `url`: "-----------------YOGA 13.4 - 13.3 I3-------------r "
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "3,53,306,9,4,370,839"

#### LENOVO YOGA 13.4 - 13.3 I5

```json
"LENOVO YOGA 13.4 - 13.3 I5": {
  "brand": "LENOVO",
  "template": "YOGA",
  "url": "https://www.visualdg.co.il/172330--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-Yoga/253273/253294",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": "3,53,306,9,5,371,839"
}
```

**Описание**: Сценарий для ноутбука Lenovo Yoga с процессором Intel Core i5 и диагональю экрана 13.3-13.4 дюйма.

**Параметры**:

- `brand`: "LENOVO"
- `template`: "YOGA"
- `url`: "https://www.visualdg.co.il/172330--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-Yoga/253273/253294"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "3,53,306,9,5,371,839"

#### LENOVO YOGA 13.4 - 13.3 I7

```json
"LENOVO YOGA 13.4 - 13.3 I7": {
  "brand": "LENOVO",
  "template": "YOGA",
  "url": "https://www.visualdg.co.il/172330--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-Yoga/253274/253294",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": "3,53,306,9,6,372,839"
}
```

**Описание**: Сценарий для ноутбука Lenovo Yoga с процессором Intel Core i7 и диагональю экрана 13.3-13.4 дюйма.

**Параметры**:

- `brand`: "LENOVO"
- `template`: "YOGA"
- `url`: "https://www.visualdg.co.il/172330--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-Yoga/253274/253294"
- `checkbox`: false
- `active`: true
- `condition`: "new"
- `presta_categories`: "3,53,306,9,6,372,839"
#### LENOVO YOGA 15 AMD

```json
"LENOVO YOGA 15 AMD": {
    "brand": "LENOVO",
    "template": "YOGA",
    "url": "----------------LENOVO YOGA 15 AMD------------- ",
    "checkbox": false,
    "active": true,
    "condition":"new",
    "presta_categories": "3,53,105,11,234,388,839"
}
```

**Описание**: Сценарий для ноутбука Lenovo Yoga с процессором AMD и диагональю экрана 15 дюймов.

**Параметры**:

-   `brand`: "LENOVO"
-   `template`: "YOGA"
-   `url`: "----------------LENOVO YOGA 15 AMD------------- "
-   `checkbox`: false
-   `active`: true
-   `condition`: "new"
-   `presta_categories`: "3,53,105,11,234,388,839"

Аналогично описаны остальные сценарии в файле.

Этот файл предназначен для хранения и использования в качестве конфигурации для автоматизированных задач, связанных с продуктами Lenovo Yoga в интернет-магазине PrestaShop.