# Документация для `visualdg_categories_laptops_lenovo_v_essentials.json`

## Обзор

Данный JSON-файл содержит конфигурационные данные для различных моделей ноутбуков Lenovo серии V ESSENTIALS. Каждая модель имеет свои характеристики, такие как процессор (i3, i5, i7, i9, AMD), размер экрана (13.3, 14, 15 дюймов), а также соответствующие URL и категории PrestaShop.

## Оглавление

- [Структура файла](#структура-файла)
- [Описание полей](#описание-полей)

## Структура файла

Файл имеет следующую структуру:

```json
{
  "scenarios": {
    "MODEL_NAME": {
      "brand": "BRAND_NAME",
      "template": "TEMPLATE_NAME",
      "url": "URL_LINK",
      "checkbox": BOOLEAN_VALUE,
      "active": BOOLEAN_VALUE,
      "condition": "CONDITION_VALUE",
      "presta_categories": "CATEGORY_IDS"
    },
    ...
  }
}
```

## Описание полей

### `scenarios`

Корневой объект, содержащий все сценарии (модели ноутбуков) в виде пар ключ-значение. Ключом является название модели, а значением - объект с параметрами.

### `MODEL_NAME`

Название модели ноутбука, например "LENOVO V ESSENTIALS 13.4 - 13.3 I3".

### `brand`

- **Описание**: Бренд ноутбука.
- **Тип**: `str`
- **Пример**: `"LENOVO"`

### `template`

- **Описание**: Шаблон модели.
- **Тип**: `str`
- **Пример**: `"V ESSENTIALS"`

### `url`

- **Описание**: URL-адрес, связанный с данной моделью.
- **Тип**: `str`
- **Пример**: `"https://www.visualdg.co.il/169443-%D7%A0%D7%99%D7%99%D7%93%D7%99-V-Essential-/253273/253294"`

### `checkbox`

- **Описание**: Флаг для отметки чекбокса (используется или нет).
- **Тип**: `bool`
- **Пример**: `false`

### `active`

- **Описание**: Флаг, указывающий, активен ли данный сценарий.
- **Тип**: `bool`
- **Пример**: `true`

### `condition`

- **Описание**: Состояние товара (новый, б/у).
- **Тип**: `str`
- **Пример**: `"new"`

### `presta_categories`

- **Описание**: Строка, содержащая ID категорий PrestaShop, к которым относится модель.
- **Тип**: `str`
- **Пример**: `"3,53,306,9,4,370"`