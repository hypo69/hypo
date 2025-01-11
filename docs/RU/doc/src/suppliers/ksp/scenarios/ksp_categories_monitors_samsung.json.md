# Документация для `ksp_categories_monitors_samsung.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [Описание сценариев](#описание-сценариев)
    - [Формат сценария](#формат-сценария)
    - [Примеры сценариев](#примеры-сценариев)

## Обзор

Файл `ksp_categories_monitors_samsung.json` содержит конфигурации сценариев для мониторов Samsung, предназначенные для парсинга и обработки данных. Каждый сценарий определяет, какую категорию мониторов Samsung следует обрабатывать, а также устанавливает соответствующие параметры для парсинга и сопоставления с категориями в PrestaShop.

## Структура файла

Файл представляет собой JSON-объект, имеющий корневой ключ `"scenarios"`, значением которого является объект, содержащий наборы сценариев. Каждый сценарий имеет уникальный ключ (размер диагонали монитора, например, "22", "23 - 24", и т.д.) и представляет собой объект со следующими полями:

- `"brand"`: Бренд производителя (в данном случае `"SAMSUNG"`).
- `"url"`: URL-адрес категории на сайте поставщика.
- `"checkbox"`: Логическое значение, определяющее использование чекбокса (в данном случае всегда `false`).
- `"active"`: Логическое значение, определяющее активность сценария (в данном случае всегда `true`).
- `"condition"`: Состояние товара (в данном случае всегда `"new"`).
- `"presta_categories"`: Объект, содержащий информацию о соответствии категорий PrestaShop.
    - `"template"`: Объект, ключом которого является бренд (в данном случае `"samsung"`), а значением - наименование категории в PrestaShop (например, `"PC MONITORS 21 - 22"`).

## Сценарии

### Описание сценариев

Каждый сценарий в файле представляет собой конфигурацию для парсинга конкретной категории мониторов Samsung на сайте поставщика KSP и сопоставления их с соответствующими категориями в PrestaShop. Сценарии различаются по размеру диагонали монитора и соответствующим URL-адресам на сайте KSP.

### Формат сценария

Каждый сценарий имеет следующую структуру:

```json
{
  "brand": "SAMSUNG",
  "url": "URL_категории_на_сайте_KSP",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": {
      "samsung": "Наименование_категории_в_PrestaShop"
    }
  }
}
```

### Примеры сценариев

#### Сценарий для мониторов 22 дюйма

```json
"22": {
  "brand": "SAMSUNG",
  "url": "https://ksp.co.il/web/cat/230..137..195",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": { "samsung": "PC MONITORS 21 - 22" }
  }
}
```

#### Сценарий для мониторов 23-24 дюйма

```json
"23 - 24": {
  "brand": "SAMSUNG",
  "url": "https://ksp.co.il/web/cat/230..137..2238..1649..198",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": { "samsung": "PC MONITORS 23 - 24" }
  }
}
```

#### Сценарий для мониторов 26-28 дюйма

```json
"26 - 28": {
  "brand": "SAMSUNG",
  "url": "https://ksp.co.il/web/cat/230..137..4831..199..4784..2037",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": { "samsung": "PC MONITORS 26 - 28" }
  }
}
```

#### Сценарий для мониторов 32-34 дюйма

```json
"32 - 34": {
  "brand": "SAMSUNG",
  "url": "https://ksp.co.il/web/cat/230..137..1948..200..2129",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": { "samsung": "PC MONITORS 32 - 34" }
  }
}
```

#### Сценарий для мониторов 44-46 дюйма

```json
"44 - 46": {
  "brand": "SAMSUNG",
  "url": "https://ksp.co.il/web/cat/230..137..3121",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": { "samsung": "PC MONITORS 44 - 46" }
  }
}
```

#### Сценарий для мониторов 48-50 дюйма

```json
"48 - 50": {
  "brand": "SAMSUNG",
  "url": "https://ksp.co.il/web/cat/230..137..30698",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": { "samsung": "PC MONITORS 48 - 50" }
  }
}
```

#### Сценарий для мониторов 52-54 дюйма

```json
"52 - 54": {
  "brand": "SAMSUNG",
  "url": "https://ksp.co.il/web/cat/230..137..43460",
  "checkbox": false,
  "active": true,
  "condition": "new",
  "presta_categories": {
    "template": { "samsung": "PC MONITORS 52 - 54" }
  }
}
```