```markdown
# Модуль `hypotez/src/suppliers/aliexpress/campaign/ttypes.py`

Файл: `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\campaign\ttypes.py`

Этот модуль определяет типы данных для работы с рекламными кампаниями на AliExpress. Он использует аннотации типов Python для лучшей читаемости и поддержки статического анализа.

## Определения типов

### `ProductType`

Тип данных для описания продукта.

| Поле | Тип | Описание |
|---|---|---|
| `product_id` | `Optional[int]` | ID продукта. |
| `app_sale_price` | `Optional[float]` | Цена продукта на приложении. |
| `original_price` | `Optional[float]` | Исходная цена продукта. |
| `sale_price` | `Optional[float]` | Цена продажи продукта. |
| `discount` | `Optional[float]` | Скидка на продукт. |
| `product_main_image_url` | `Optional[str]` | URL основного изображения продукта. |
| `local_saved_image` | `Optional[str]` | Путь к сохраненному изображению продукта на локальном диске. |
| `product_small_image_urls` | `Optional[List[str]]` | Список URL изображений малого размера. |
| `product_video_url` | `Optional[str]` | URL видео продукта. |
| `local_saved_video` | `Optional[str]` | Путь к сохраненному видео продукта. |
| `first_level_category_id` | `Optional[int]` | ID категории первого уровня. |
| `first_level_category_name` | `Optional[str]` | Название категории первого уровня. |
| `second_level_category_id` | `Optional[int]` | ID категории второго уровня. |
| `second_level_category_name` | `Optional[str]` | Название категории второго уровня. |
| `target_sale_price` | `Optional[float]` | Целевая цена продажи. |
| `target_sale_price_currency` | `Optional[str]` | Валюта целевой цены продажи. |
| `target_app_sale_price_currency` | `Optional[str]` | Валюта целевой цены на приложении. |
| `target_original_price_currency` | `Optional[str]` | Валюта целевой исходной цены. |
| `original_price_currency` | `Optional[str]` | Валюта исходной цены. |
| `product_title` | `Optional[str]` | Название продукта. |
| `evaluate_rate` | `Optional[float]` | Рейтинг оценки продукта. |
| `promotion_link` | `Optional[str]` | Ссылка на акцию. |
| `shop_url` | `Optional[str]` | Ссылка на магазин. |
| `shop_id` | `Optional[int]` | ID магазина. |
| `tags` | `Optional[List[str]]` | Список тегов продукта. |


### `CampaignType`

Тип данных для описания рекламной кампании.

| Поле | Тип | Описание |
|---|---|---|
| `name` | `Optional[str]` | Название кампании. |
| `title` | `Optional[str]` | Заголовок кампании. |
| `language` | `Optional[str]` | Язык кампании. |
| `currency` | `Optional[str]` | Валюта кампании. |
| `category` | `SimpleNamespace` | Объект типа `SimpleNamespace`, представляющий категорию кампании.  **Важно:**  Этот тип требует дальнейшей детализации. |


### `CategoryType`

Тип данных для описания категории.

| Поле | Тип | Описание |
|---|---|---|
| `name` | `Optional[str]` | Название категории. |
| `tags` | `Optional[List[str]]` | Список тегов категории. |
| `products` | `List[SimpleNamespace]` | Список продуктов в категории. **Важно:**  Этот тип требует дальнейшей детализации. |
| `products_count` | `int` | Количество продуктов в категории. |


## Переменная `types`

Переменная `types` содержит экземпляры `SimpleNamespace` для каждого типа.  Она предоставляет удобный способ доступа к данным. Однако `SimpleNamespace`  не обеспечивает валидацию данных и не рекомендует к использованию в случаях, когда необходимы сложные типы данных.

**Рекомендация:** Замените `SimpleNamespace` на более конкретные типы данных (например, `TypedDict`) в `CampaignType` и `CategoryType` для лучшей поддержки типов.


**Примечание:**  В коде присутствуют повторяющиеся объявления для `campaign` и `category`, что нелогично.  Лучше использовать единственный `SimpleNamespace` или `TypedDict`.  Из-за этого есть рекомендации по улучшению типов.


Этот документ предоставляет описание типов данных.  Для более глубокого понимания логики работы с данными рекомендуется изучить контекст использования этих типов в программе.
```