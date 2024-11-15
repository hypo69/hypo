```markdown
# Модуль `hypotez/src/suppliers/aliexpress/campaign/ttypes.py`

Этот модуль определяет типы данных для работы с кампаниями, категориями и продуктами на AliExpress. Он использует `TypedDict` для явного определения структуры данных и `SimpleNamespace` для хранения дополнительных, не типизированных данных.


## Типы данных

### `ProductType`

Представляет тип данных для описания продукта.

| Поле | Тип | Описание |
|---|---|---|
| `product_id` | `Optional[int]` | Идентификатор продукта. |
| `app_sale_price` | `Optional[float]` | Цена продукта на приложении. |
| `original_price` | `Optional[float]` | Исходная цена продукта. |
| `sale_price` | `Optional[float]` | Цена продукта со скидкой. |
| `discount` | `Optional[float]` | Скидка. |
| `product_main_image_url` | `Optional[str]` | URL основного изображения продукта. |
| `local_saved_image` | `Optional[str]` | Путь к сохранённому локальному изображению. |
| `product_small_image_urls` | `Optional[List[str]]` | Список URL малых изображений продукта. |
| `product_video_url` | `Optional[str]` | URL видео продукта. |
| `local_saved_video` | `Optional[str]` | Путь к сохранённому локальному видео. |
| `first_level_category_id` | `Optional[int]` | Идентификатор категории первого уровня. |
| `first_level_category_name` | `Optional[str]` | Название категории первого уровня. |
| `second_level_category_id` | `Optional[int]` | Идентификатор категории второго уровня. |
| `second_level_category_name` | `Optional[str]` | Название категории второго уровня. |
| `target_sale_price` | `Optional[float]` | Целевая цена со скидкой. |
| `target_sale_price_currency` | `Optional[str]` | Валюта целевой цены со скидкой. |
| `target_app_sale_price_currency` | `Optional[str]` | Валюта целевой цены на приложении. |
| `target_original_price_currency` | `Optional[str]` | Валюта исходной целевой цены. |
| `original_price_currency` | `Optional[str]` | Валюта исходной цены продукта. |
| `product_title` | `Optional[str]` | Название продукта. |
| `evaluate_rate` | `Optional[float]` | Рейтинг продукта. |
| `promotion_link` | `Optional[str]` | Ссылка на акцию. |
| `shop_url` | `Optional[str]` | Ссылка на магазин. |
| `shop_id` | `Optional[int]` | Идентификатор магазина. |
| `tags` | `Optional[List[str]]` | Список тегов продукта. |


### `CampaignType`

Представляет тип данных для описания кампании.

| Поле | Тип | Описание |
|---|---|---|
| `name` | `Optional[str]` | Название кампании. |
| `title` | `Optional[str]` | Заголовок кампании. |
| `language` | `Optional[str]` | Язык кампании. |
| `currency` | `Optional[str]` | Валюта кампании. |
| `category` | `SimpleNamespace` | Объект, содержащий данные о категории. |


### `CategoryType`

Представляет тип данных для описания категории.

| Поле | Тип | Описание |
|---|---|---|
| `name` | `Optional[str]` | Название категории. |
| `tags` | `Optional[List[str]]` | Список тегов категории. |
| `products` | `List[SimpleNamespace]` | Список продуктов в категории. |
| `products_count` | `int` | Количество продуктов в категории. |


## Переменная `types`

Содержит экземпляры `SimpleNamespace` для инициализации переменных, представляющих типы данных. Используется для хранения значений по умолчанию или начальных значений для последующего заполнения.


**Важно:**

* Использование `SimpleNamespace` для `category` в `CampaignType` и `products` в `CategoryType` означает, что эти поля могут содержать дополнительные данные, не охваченные этим определением.
* Тип данных `SimpleNamespace` позволяет хранить данные произвольного типа.


Этот документ предоставляет подробное описание типов данных, используемых в модуле, что повышает читаемость и понимание кода.
```