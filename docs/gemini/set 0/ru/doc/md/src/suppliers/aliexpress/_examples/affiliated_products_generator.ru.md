# Модуль `affiliated_products_generator` (генератор аффилированных продуктов AliExpress)

## Обзор

Этот модуль предоставляет инструменты для генерации аффилированных ссылок для продуктов AliExpress.  Он позволяет собирать данные о продуктах, создавать аффилированные ссылки и сохранять связанные изображения и видео.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс `AliAffiliatedProducts` отвечает за обработку данных о продуктах AliExpress и генерацию аффилированных ссылок.  Он обрабатывает список URL или ID продуктов, создаёт аффилированные ссылки и сохраняет связанные изображения/видео на локальный диск.

**Методы**:

- `process_affiliate_products(prod_urls: list[str | int]) -> list[Product] | None`:
    **Описание**: Обрабатывает список URL или ID продуктов, создаёт аффилированные ссылки, сохраняет изображения и видео на локальный диск. Возвращает список объектов `Product`, содержащих информацию об обработанном продукте, или `None` в случае ошибки.

    **Параметры**:
    - `prod_urls` (list[str | int]): Список URL или ID продуктов AliExpress для обработки.

    **Возвращает**:
    - list[Product] | None: Список объектов `Product` с аффилированными ссылками, изображениями и видео, или `None` при ошибках.

    **Вызывает исключения**:
    - `ValueError`: Если введен неправильный тип данных в `prod_urls`.
    - `RequestException`: При возникновении проблем с запросом к API AliExpress.
    - `IOError`: При ошибках при работе с файлами.
    - `Exception`:  Для других неопределённых ошибок.


## Пример использования (файл `пример_использования.py`)

### Пример использования `AliAffiliatedProducts`

Этот пример демонстрирует, как использовать класс `AliAffiliatedProducts` для получения аффилированных ссылок и сохранения информации о продуктах. Он включает создание экземпляра класса, обработку списка URL/ID, получение и вывод результатов.

```python
# пример_использования.py
# ... (код из input_code)
```

**Описание примера**:

Код показывает процесс:

1.  Создание экземпляра `AliAffiliatedProducts` с параметрами кампании.
2.  Подготовка списка URL/ID продуктов.
3.  Вызов `process_affiliate_products` для получения списка обработанных продуктов.
4.  Проверка результата и вывод информации о каждом обработанном продукте.


## Класс `Product`

**Описание**: Внутренний класс, хранящий информацию о продукте, включая его аффилированную ссылку, ID продукта, локальный путь к сохранённому изображению, и пути к видео (если есть).

**Атрибуты**:

- `product_id`: ID продукта.
- `promotion_link`: Аффилированная ссылка.
- `local_saved_image`: Путь к сохранённому изображению.
- `local_saved_video`: Путь к сохранённому видео (если есть).


**Примечания**:  Для полного понимания работы модуля, необходимо изучить реализацию класса `AliAffiliatedProducts` и методов, которые он использует (например, методы для получения аффилированных ссылок, загрузки изображений и т.д.).  Эти реализации не приведены в данном файле.