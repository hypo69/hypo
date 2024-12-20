# Документация для `store.json`

## Обзор

Файл `store.json` содержит локаторы элементов для страницы магазина поставщика Grand Advance. Он определяет структуру JSON, где ключи представляют собой названия элементов, а значения являются их CSS-селекторами.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)

## Структура JSON

Файл `store.json` представляет собой словарь (JSON-объект), где каждая запись имеет следующий формат:

```json
{
  "название_элемента": "css-селектор"
}
```

Где:
- `"название_элемента"`: Ключ, который является строковым идентификатором элемента на странице.
- `"css-селектор"`: Значение, которое является строкой, представляющей CSS-селектор для поиска данного элемента на странице.

### Примеры ключей и селекторов:

Примеры элементов, которые могут встречаться в этом файле:
- `"search_input"`: CSS-селектор для поля ввода поиска.
- `"search_button"`: CSS-селектор для кнопки поиска.
- `"product_cards"`: CSS-селектор для контейнера с карточками товаров.
- `"add_to_cart_button"`: CSS-селектор для кнопки "Добавить в корзину".
- `"product_name"`: CSS-селектор для названия товара.
- `"product_price"`: CSS-селектор для цены товара.
- `"cart_icon"`: CSS-селектор для иконки корзины.

### Назначение

Этот JSON-файл используется для централизованного хранения и доступа к локаторам элементов, что упрощает поддержку и изменение автоматизированных тестов и скриптов, работающих с сайтом поставщика Grand Advance.