# Документация для `cdata_categories_laptops_dell.json`

## Оглавление

1. [Обзор](#обзор)
2. [Содержимое файла](#содержимое-файла)
    - [Структура JSON](#структура-json)
    - [Описание сценариев](#описание-сценариев)

## Обзор

Данный файл `cdata_categories_laptops_dell.json` содержит JSON-структуру, описывающую сценарии для категорий ноутбуков DELL. Каждый сценарий представляет собой определенную модель ноутбука DELL с указанием его характеристик и параметров для интеграции с PrestaShop.

## Содержимое файла

### Структура JSON

Файл имеет следующую структуру:

```json
{
  "scenarios": {
    "Модель ноутбука 1": {
      "brand": "DELL",
      "url": "URL_для_парсинга",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": "строка_категорий_presta"
    },
   "Модель ноутбука 2": {
      "brand": "DELL",
      "url": "URL_для_парсинга",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": "строка_категорий_presta"
    },
    ...
  }
}
```

- `scenarios`: Объект, содержащий все сценарии. Ключами являются названия моделей ноутбуков DELL.
    - `brand`: Строка, представляющая бренд ноутбука (всегда "DELL").
    - `url`: Строка, содержащая URL-адрес, с которого нужно парсить данные для конкретной модели ноутбука.
    - `checkbox`: Логическое значение, которое всегда установлено в `false`. Похоже, что это поле не используется в текущей реализации.
    - `active`: Логическое значение, указывающее, активен ли сценарий (всегда `true`).
    - `condition`: Строка, представляющая состояние товара (всегда "new").
    - `presta_categories`: Строка, содержащая ID категорий PrestaShop, к которым относится данный товар, разделенные запятыми.

### Описание сценариев

Файл содержит множество сценариев, каждый из которых описывает определенную модель ноутбука DELL. Сценарии сгруппированы по размеру экрана и типу процессора:
- `DELL 11.6 I3`, `DELL 11.6 I5`, `DELL 11.6 I7`, `DELL 11.6 I9`, `DELL 11.6 AMD`, `DELL 11.6 Celeron`, `DELL 11.6 Pentium`: Сценарии для ноутбуков DELL с диагональю экрана 11.6 дюймов.
- `DELL 13.3 I3`, `DELL 13.3 I5 Inspiron 7000`, `DELL 13.3 I5 XPS13`, `DELL 13.3 I7 Inspiron 7000`, `DELL 13.3 I7 Latitude 7000`, `DELL 13.3 I7 XPS`, `DELL 13.3 I9`, `DELL 13.3 AMD`, `DELL 13.3 Celeron`, `DELL 13.3 Pentium`: Сценарии для ноутбуков DELL с диагональю экрана 13.3 дюймов.
- `DELL 14 I3`, `DELL 14 I5 Inspiron 5000`, `DELL 14 I5 Latitude 3000`, `DELL 14 I5 Latitude 5000`, `DELL 14 I5 Latitude 7000`, `DELL 14 I7 Inspiron 5000`, `DELL 14 I7 Latitude 3000`, `DELL 14 I7 Latitude 5000`, `DELL 14 I7 Latitude 7000`, `DELL 14 I9`, `DELL 14 AMD`, `DELL 14 Celeron`, `DELL 14 Pentium`: Сценарии для ноутбуков DELL с диагональю экрана 14 дюймов.
- `DELL 15 I3`, `DELL 15 I5.6 Inspiron 5000`, `DELL 15 I5 Vostro 3000`, `DELL 15 I5 Vostro 5000`, `DELL 15 I5 Latitude 3000`, `DELL 15 I5 Latitude 5000`, `DELL 15.0 I7 Latitude 9000`, `DELL 15.6 I7 Inspiron 5000`, `DELL 15.6 I7 Inspiron G5500`, `DELL 15 I7 Vostro 3000`, `DELL 15 I7 Vostro 5000`, `DELL 15 I7 Latitude 3000`, `DELL 15 I7 Latitude 5000`, `DELL 15 I7 XPS`, `DELL 15 I7 Precision 3000`, `DELL 15 I7 Precision 5000`, `DELL 15 I7 Precision 7000`, `DELL 15 I9 Precision 5000`, `DELL 15 I9 Precision 7000`: Сценарии для ноутбуков DELL с диагональю экрана 15 дюймов.
- `DELL 17.3 I3`, `DELL 17.3 I5 Inspiron 3000`, `DELL 17.3 I7 Inspiron 3000`, `DELL 17.3 I7 XPS`, `DELL 17.3 I7 Precision 7000`, `DELL 17.3 I9 Precision 7000`, `DELL 17.3 AMD`, `DELL 17.3 Celeron`, `DELL 17.3 Pentium`: Сценарии для ноутбуков DELL с диагональю экрана 17.3 дюймов.

Каждый сценарий содержит:
   -   Название модели, которое служит ключом объекта.
   -  Бренд (`brand`), всегда "DELL".
   - URL-адрес для парсинга данных (`url`).
   - Флаг `checkbox`, который всегда установлен в `false`.
   - Флаг `active`, который всегда установлен в `true`.
   - Состояние товара (`condition`), всегда "new".
   - Список ID категорий PrestaShop (`presta_categories`), к которым относится товар.

Этот файл используется для автоматизации процесса добавления товаров в интернет-магазин на базе PrestaShop путем парсинга данных с указанных URL-адресов и присвоения их соответствующим категориям.