# Документация для `kualastyle_categories_carpets.json`

## Обзор

Данный файл `kualastyle_categories_carpets.json` представляет собой JSON-конфигурацию, описывающую категорию "שטיחים" (ковры) для поставщика Kualastyle. Он содержит информацию о наличии подкатегорий и пустой объект для сценариев.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание полей](#описание-полей)

## Структура JSON

```json
{
  "category name on site": "שטיחים",
  "have subcategories": true,
  "scenarios": {}
}
```

## Описание полей

### `category name on site`
- **Описание**: Название категории на сайте поставщика.
- **Тип**: `string`
- **Значение**: `"שטיחים"` (Ковры).

### `have subcategories`
- **Описание**: Флаг, указывающий на наличие подкатегорий в данной категории.
- **Тип**: `boolean`
- **Значение**: `true` (означает, что категория имеет подкатегории).

### `scenarios`
- **Описание**: Объект, содержащий сценарии для данной категории. В текущей версии пустой.
- **Тип**: `object`
- **Значение**: `{}` (пустой объект, ожидается добавление сценариев).