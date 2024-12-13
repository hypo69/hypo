# Документация для `morlevi_categories_minipc_gigabyte.json`

## Обзор

Данный файл содержит JSON-структуру, описывающую сценарии для парсинга категорий MiniPC бренда GIGABYTE с сайта Morlevi. Каждый сценарий содержит информацию о конкретной категории MiniPC, включая URL для парсинга, бренд, активность сценария и соответствующие категории PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [`scenarios` - Сценарии](#scenarios---сценарии)
    - [Описание полей сценария](#описание-полей-сценария)
4. [Примеры сценариев](#примеры-сценариев)

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "GIGABYTE MINIPC I3 8-9th GEN": {
      "brand": "GIGABYTE",
      "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=1895&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": "159,160"
    },
    // Другие сценарии...
  }
}
```

## `scenarios` - Сценарии

Раздел `scenarios` содержит объект, где каждый ключ является названием сценария для определенной категории MiniPC GIGABYTE. Значением каждого ключа является объект, описывающий настройки данного сценария.

### Описание полей сценария

Каждый сценарий имеет следующие поля:

-   `brand` (str): Название бренда, в данном случае всегда `"GIGABYTE"`.
-   `url` (str): URL-адрес страницы с категорией на сайте Morlevi. Может содержать placeholder`---------`, если URL не определен.
-   `checkbox` (bool): Флаг, указывающий на использование checkbox, в данном файле всегда `false`.
-   `active` (bool): Флаг, указывающий, активен ли данный сценарий.
-    `condition` (str):  Состояние товара , в данном файле всегда `"new"`.
-   `presta_categories` (str): Строка, содержащая ID категорий PrestaShop, разделенных запятой.

## Примеры сценариев

### GIGABYTE MINIPC I3 8-9th GEN
```json
"GIGABYTE MINIPC I3 8-9th GEN": {
      "brand": "GIGABYTE",
      "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=1895&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "159,160"
    }
```

**Описание**: Сценарий для парсинга MiniPC GIGABYTE с процессором Intel Core i3 8-го и 9-го поколений.

**Поля**:
- `brand`: `"GIGABYTE"`
- `url`: `"https://www.morlevi.co.il/Cat/127?p_315=2&p_189=1895&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"159,160"`

### GIGABYTE MINIPC I5 8-9th
```json
    "GIGABYTE MINIPC I5 8-9th": {
      "brand": "GIGABYTE",
      "url": "--------------------------GIGABYTE MINIPC I5 8-9th-------------------------",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "159,161"
    }
```
**Описание**: Сценарий для парсинга MiniPC GIGABYTE с процессором Intel Core i5 8-го и 9-го поколений. URL не указан, содержит placeholder.

**Поля**:
- `brand`: `"GIGABYTE"`
- `url`: `"--------------------------GIGABYTE MINIPC I5 8-9th-------------------------"`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"159,161"`