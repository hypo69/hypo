# Документация для `kualastyle_categories_photos.json`

## Обзор

Файл `kualastyle_categories_photos.json` содержит JSON-структуру, описывающую категорию товаров "תמונות" (Фотографии) для поставщика Kualastyle. Указывает на то, что у этой категории нет подкатегорий и пока нет сценариев.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)

## Структура JSON

### Описание структуры

Файл имеет следующую структуру:

```json
{
  "category name on site": "תמונות",
  "have subcategories": false,
  "scenarios": {}
}
```

### Поля JSON

- `category name on site` (string): Название категории на сайте поставщика. В данном случае `"תמונות"` (Фотографии).
- `have subcategories` (boolean): Указывает, имеет ли категория подкатегории. Значение `false` означает, что подкатегорий нет.
- `scenarios` (object): Объект, содержащий сценарии для данной категории. В данном случае пустой объект `{}`, что означает отсутствие сценариев.