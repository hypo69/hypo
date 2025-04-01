# Модуль ide_experiments_fields.py

## Обзор

Модуль `ide_experiments_fields.py` предназначен для сбора и обработки полей товара с веб-страницы поставщика HB (hbdeadsea.co.il) и приведения их к формату, необходимому для системы PrestaShop. Модуль использует Selenium для взаимодействия с веб-страницей, извлечения данных и нормализации этих данных. Собранные данные затем используются для добавления или обновления информации о товаре в PrestaShop.

## Подробней

Этот модуль является частью процесса интеграции данных о товарах от поставщика HB в систему PrestaShop. Он автоматизирует сбор данных, которые в противном случае потребовалось бы вводить вручную. Модуль использует веб-драйвер для навигации по страницам товаров, извлечения информации о продуктах и преобразования этой информации в формат, который можно использовать для обновления базы данных PrestaShop.

## Функции

### `grab_product_page`

```python
def grab_product_page(supplier: Supplier, async_run: bool = True) -> ProductFields:
    """Собирает со страницы товара значения вебэлементов и приводит их к полям ProductFields.

    Args:
        supplier (Supplier): Класс поставщика. Веб-драйвер должен быть установлен на странице товара.
        async_run (bool, optional): Указывает, следует ли использовать асинхронный запуск. По умолчанию `True`.

    Returns:
        ProductFields: Объект, содержащий собранные и преобразованные поля товара.

    Как работает функция:
    1.  Инициализирует глобальные переменные `s` (supplier), `p` (product), `f` (product fields), `d` (driver) и `l` (locators).
    2.  Закрывает баннер на странице товара.
    3.  Прокручивает страницу товара для загрузки AJAX-контента.
    4.  Вызывает внутренние функции для извлечения и установки различных полей товара.

    Внутри функции происходят следующие действия и преобразования:
     Инициализация переменных
     |
     -- Закрытие баннера и прокрутка страницы
     |
     Извлечение и установка полей товара с помощью внутренних функций
    """
```

**Внутренние функции**:

#### `product_reference_and_volume_and_price_for_100`

```python
def product_reference_and_volume_and_price_for_100():
    """Вытаскивает 3 поля: volume, supplier_reference, цена за единицу товара.

    @todo Реализовать поле `цена за единицу товара`
    """
```

**Как работает функция**:

1.  Извлекает список веб-элементов, содержащих информацию об объеме, артикуле поставщика и цене за 100 мл.
2.  Перебирает веб-элементы и извлекает соответствующие значения, используя строковые операции и нормализацию.
3.  Заполняет поля `volume` и `supplier_reference` объекта `f` (ProductFields).
4.  Выводит в консоль цену за единицу товара (требуется дальнейшая реализация для сохранения этого значения в соответствующем поле).

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение веб-элементов
     |
     -- Перебор веб-элементов
     |
     Извлечение объема, артикула и цены
     |
     Заполнение полей объекта ProductFields

#### `set_references`

```python
def set_references(f: ProductFields, s: Supplier):
    """Устанавливает значения, касающиеся идентификаторов товара.

    Args:
        f (ProductFields): Объект для хранения полей продукта.
        s (Supplier): Объект поставщика, содержащий информацию о поставщике.
    """
```

**Как работает функция**:

1.  Устанавливает `id_supplier` из `s.supplier_id`.
2.  Формирует `reference` как комбинацию `s.supplier_id` и `f.supplier_reference`.
3.  Присваивает полученные значения полям объекта `f` (ProductFields).

**Внутри функции происходят следующие действия и преобразования**:

     Установка `id_supplier`
     |
     -- Формирование `reference`
     |
     Присвоение значений полям объекта `ProductFields`

### `field_additional_shipping_cost`

```python
def field_additional_shipping_cost():
    """
    стоимость доставки
    @details
    """
    return d.execute_locator(l["additional_shipping_cost"])
```

**Как работает функция**:

1.  Извлекает стоимость доставки, используя локатор `l["additional_shipping_cost"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение стоимости доставки
     |
     -- Возврат значения

### `field_delivery_in_stock`

```python
def field_delivery_in_stock():
    """
    Доставка, когда товар в наличии
    @details
    """
    return str(d.execute_locator(l["delivery_in_stock"]))
```

**Как работает функция**:

1.  Извлекает информацию о доставке, когда товар в наличии, используя локатор `l["delivery_in_stock"]` и метод `execute_locator` объекта `d` (driver).
2.  Преобразует извлеченное значение в строку.
3.  Возвращает полученную строку.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение информации о доставке
     |
     -- Преобразование в строку
     |
     Возврат строки

### `field_active`

```python
def field_active():
    """

    @details
    """
    return f.active  # <-  поставить в зависимость от delivery_out_stock
```

**Как работает функция**:

1.  Возвращает значение `f.active`.
2.  В комментарии указано, что значение должно зависеть от `delivery_out_stock`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.active`

### `field_additional_delivery_times`

```python
def field_additional_delivery_times():
    """

    @details
    """
    return d.execute_locator(l["additional_delivery_times"])
```

**Как работает функция**:

1.  Извлекает дополнительное время доставки, используя локатор `l["additional_delivery_times"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение времени доставки
     |
     -- Возврат значения

### `field_additional_shipping_cost`

```python
def field_additional_shipping_cost():
    """

    @details
    """
    return d.execute_locator(l["additional_shipping_cost"])
```

**Как работает функция**:

1.  Извлекает дополнительную стоимость доставки, используя локатор `l["additional_shipping_cost"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение стоимости доставки
     |
     -- Возврат значения

### `field_advanced_stock_management`

```python
def field_advanced_stock_management():
    """

    @details
    """
    return f.advanced_stock_management
```

**Как работает функция**:

1.  Возвращает значение `f.advanced_stock_management`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.advanced_stock_management`

### `field_affiliate_short_link`

```python
def field_affiliate_short_link():
    """

    @details
    """
    return d.current_url
```

**Как работает функция**:

1.  Возвращает текущий URL из объекта `d` (driver).

**Внутри функции происходят следующие действия и преобразования**:

     Возврат текущего URL

### `field_affiliate_summary`

```python
def field_affiliate_summary():
    """

    @details
    """
    return f.affiliate_summary
```

**Как работает функция**:

1.  Возвращает значение `f.affiliate_summary`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.affiliate_summary`

### `field_affiliate_summary_2`

```python
def field_affiliate_summary_2():
    """

    @details
    """
    return f.affiliate_summary_2
```

**Как работает функция**:

1.  Возвращает значение `f.affiliate_summary_2`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.affiliate_summary_2`

### `field_affiliate_text`

```python
def field_affiliate_text():
    """

    @details
    """
    return f.affiliate_text
```

**Как работает функция**:

1.  Возвращает значение `f.affiliate_text`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.affiliate_text`

### `field_affiliate_image_large`

```python
def field_affiliate_image_large():
    """

    @details
    """
    ...
```

**Как работает функция**:

1.  Функция не имеет реализации (содержит только `...`).

**Внутри функции происходят следующие действия и преобразования**:

     Нет действий

### `field_affiliate_image_medium`

```python
def field_affiliate_image_medium():
    """

    @details
    """
    ...
```

**Как работает функция**:

1.  Функция не имеет реализации (содержит только `...`).

**Внутри функции происходят следующие действия и преобразования**:

     Нет действий

### `field_affiliate_image_small`

```python
def field_affiliate_image_small():
    """

    @details
    """
    return d.execute_locator(l["affiliate_image_small"])
```

**Как работает функция**:

1.  Извлекает изображение маленького размера для аффилиатов, используя локатор `l["affiliate_image_small"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение изображения
     |
     -- Возврат значения

### `field_available_date`

```python
def field_available_date():
    """

    @details
    """
    return f.available_date
```

**Как работает функция**:

1.  Возвращает значение `f.available_date`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.available_date`

### `field_available_for_order`

```python
def field_available_for_order():
    """Если вернулся вебэлемент, это флаг, что товара нет в наличии, а вернулся <p>המלאי אזל
    """
    available_for_order = d.execute_locator(l["available_for_order"])
    ...
    if available_for_order is None:
        f.available_for_order = 1
    else:
        f.available_for_order = 0
        f.active = 0
    ...
```

**Как работает функция**:

1.  Извлекает информацию о доступности товара для заказа, используя локатор `l["available_for_order"]` и метод `execute_locator` объекта `d` (driver).
2.  Если веб-элемент не найден (`None`), устанавливает `f.available_for_order` в 1 (товар доступен).
3.  Если веб-элемент найден, устанавливает `f.available_for_order` в 0 и `f.active` в 0 (товар не доступен).

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение информации о доступности
     |
     -- Проверка наличия веб-элемента
     |
     Установка значений полей в зависимости от доступности

### `field_available_later`

```python
def field_available_later():
    """

    @details
    """
    return f.available_later
```

**Как работает функция**:

1.  Возвращает значение `f.available_later`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.available_later`

### `field_available_now`

```python
def field_available_now():
    """

    @details
    """
    return f.available_now
```

**Как работает функция**:

1.  Возвращает значение `f.available_now`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.available_now`

### `field_category_ids`

```python
def field_category_ids():
    """

    @details
    """
    return f.category_ids
```

**Как работает функция**:

1.  Возвращает значение `f.category_ids`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.category_ids`

### `field_category_ids_append`

```python
def field_category_ids_append():
    """

    @details
    """
    # return f.category_ids_append
    ...
```

**Как работает функция**:

1.  Функция не имеет реализации (содержит только `...`).
2.  Закомментирована строка `return f.category_ids_append`.

**Внутри функции происходят следующие действия и преобразования**:

     Нет действий

### `field_cache_default_attribute`

```python
def field_cache_default_attribute():
    """

    @details
    """
    return f.cache_default_attribute
```

**Как работает функция**:

1.  Возвращает значение `f.cache_default_attribute`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.cache_default_attribute`

### `field_cache_has_attachments`

```python
def field_cache_has_attachments():
    """

    @details
    """
    return f.cache_has_attachments
```

**Как работает функция**:

1.  Возвращает значение `f.cache_has_attachments`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.cache_has_attachments`

### `field_cache_is_pack`

```python
def field_cache_is_pack():
    """

    @details
    """
    return f.cache_is_pack
```

**Как работает функция**:

1.  Возвращает значение `f.cache_is_pack`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.cache_is_pack`

### `field_condition`

```python
def field_condition():
    """

    @details
    """
    return d.execute_locator(l.condition)
```

**Как работает функция**:

1.  Извлекает условие товара, используя локатор `l.condition` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение условия товара
     |
     -- Возврат значения

### `field_customizable`

```python
def field_customizable():
    """

    @details
    """
    return f.customizable
```

**Как работает функция**:

1.  Возвращает значение `f.customizable`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.customizable`

### `field_date_add`

```python
def field_date_add():
    """

    @details
    """
    return f.date_add
```

**Как работает функция**:

1.  Возвращает значение `f.date_add`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.date_add`

### `field_date_upd`

```python
def field_date_upd():
    """

    @details
    """
    return f.date_upd
```

**Как работает функция**:

1.  Возвращает значение `f.date_upd`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.date_upd`

### `field_delivery_in_stock`

```python
def field_delivery_in_stock():
    """
    Доставка, когда товар в наличии
    @details
    """
    return d.execute_locator(l["delivery_in_stock"])
```

**Как работает функция**:

1.  Извлекает информацию о доставке, когда товар в наличии, используя локатор `l["delivery_in_stock"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение информации о доставке
     |
     -- Возврат значения

### `field_delivery_out_stock`

```python
def field_delivery_out_stock():
    """
    Заметка о доставке, когда товара нет в наличии
    """
    return f.delivery_out_stock
```

**Как работает функция**:

1.  Возвращает значение `f.delivery_out_stock`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.delivery_out_stock`

### `field_depth`

```python
def field_depth():
    """
    @details
    """
    return d.execute_locator(l["depth"])
```

**Как работает функция**:

1.  Извлекает глубину товара, используя локатор `l["depth"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение глубины товара
     |
     -- Возврат значения

### `field_description`

```python
def field_description():
    """поле полного описания товара
    @details
    """
    return d.execute_locator(l["description"])[0].text
```

**Как работает функция**:

1.  Извлекает полное описание товара, используя локатор `l["description"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает текст первого элемента из списка найденных веб-элементов.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение описания товара
     |
     -- Возврат текста описания

### `field_id_category_default`

```python
def field_id_category_default():
    """Главная категория товара. Берется из сценария
    """
    return s.current_scenario["presta_categories"]["default_category"]
```

**Как работает функция**:

1.  Возвращает идентификатор главной категории товара из сценария `s.current_scenario`.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение идентификатора категории
     |
     -- Возврат идентификатора

### `field_ean13`

```python
def field_ean13():
    """

    @details
    """
    return d.execute_locator(l["ean13"])
```

**Как работает функция**:

1.  Извлекает EAN13 код товара, используя локатор `l["ean13"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение EAN13 кода
     |
     -- Возврат значения

### `field_ecotax`

```python
def field_ecotax():
    """

    @details
    """
    return f.ecotax
```

**Как работает функция**:

1.  Возвращает значение `f.ecotax`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.ecotax`

### `field_height`

```python
def field_height():
    """

    @details
    """
    return d.execute_locator(l["height"])
```

**Как работает функция**:

1.  Извлекает высоту товара, используя локатор `l["height"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение высоты товара
     |
     -- Возврат значения

### `field_how_to_use`

```python
def field_how_to_use():
    """

    @details
    """
    return d.execute_locator(l["how_to_use"])[0].text
```

**Как работает функция**:

1.  Извлекает инструкцию по использованию товара, используя локатор `l["how_to_use"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает текст первого элемента из списка найденных веб-элементов.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение инструкции
     |
     -- Возврат текста инструкции

### `field_id_category_default`

```python
def field_id_category_default():
    """

    @details
    """
    return s.current_scenario["presta_categories"]["default_category"]
```

**Как работает функция**:

1.  Возвращает идентификатор главной категории товара из сценария `s.current_scenario`.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение идентификатора категории
     |
     -- Возврат идентификатора

### `field_id_default_combination`

```python
def field_id_default_combination():
    """

    @details
    """
    return f.id_default_combination
```

**Как работает функция**:

1.  Возвращает значение `f.id_default_combination`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.id_default_combination`

### `field_id_default_image`

```python
def field_id_default_image():
    """

    @details
    """
    return f.id_default_image
```

**Как работает функция**:

1.  Возвращает значение `f.id_default_image`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.id_default_image`

### `field_id_lang`

```python
def field_id_lang():
    """

    @details
    """
    return f.id_lang
```

**Как работает функция**:

1.  Возвращает значение `f.id_lang`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.id_lang`

### `field_id_manufacturer`

```python
def field_id_manufacturer():
    """ID бренда. Может быть и названием бренда - престашоп сам разберется"""

    return d.execute_locator(l["id_manufacturer"])
```

**Как работает функция**:

1.  Извлекает идентификатор производителя, используя локатор `l["id_manufacturer"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение идентификатора производителя
     |
     -- Возврат значения

### `field_id_product`

```python
def field_id_product():
    """

    @details
    """
    return f.id_product
```

**Как работает функция**:

1.  Возвращает значение `f.id_product`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.id_product`

### `field_id_shop_default`

```python
def field_id_shop_default():
    """

    @details
    """
    return f.id_shop_default
```

**Как работает функция**:

1.  Возвращает значение `f.id_shop_default`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.id_shop_default`

### `field_id_supplier`

```python
def field_id_supplier():
    """

    @details
    """
    return d.execute_locator(l["id_supplier"])
```

**Как работает функция**:

1.  Извлекает идентификатор поставщика, используя локатор `l["id_supplier"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение идентификатора поставщика
     |
     -- Возврат значения

### `field_id_tax`

```python
def field_id_tax():
    """

    @details
    """
    return f.id_tax
```

**Как работает функция**:

1.  Возвращает значение `f.id_tax`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.id_tax`

### `field_id_type_redirected`

```python
def field_id_type_redirected():
    """

    @details
    """
    return f.id_type_redirected
```

**Как работает функция**:

1.  Возвращает значение `f.id_type_redirected`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.id_type_redirected`

### `field_images_urls`

```python
def field_images_urls():
    """
    Вначале я загружу дефолтную картинку
    @details
    """
    return d.execute_locator(l["additional_images_urls"])
```

**Как работает функция**:

1.  Извлекает список URL дополнительных изображений товара, используя локатор `l["additional_images_urls"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченный список.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение списка URL изображений
     |
     -- Возврат списка

### `field_indexed`

```python
def field_indexed():
    """

    @details
    """
    return f.indexed
```

**Как работает функция**:

1.  Возвращает значение `f.indexed`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.indexed`

### `field_ingredients`

```python
def field_ingredients():
    """Состав. Забираю с сайта HTML с картинками ингридиентов"""

    return d.execute_locator(l["ingredients"])[0].text
```

**Как работает функция**:

1.  Извлекает состав товара, используя локатор `l["ingredients"]` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает текст первого элемента из списка найденных веб-элементов.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение состава товара
     |
     -- Возврат текста состава

### `field_meta_description`

```python
def field_meta_description():
    """

    @details
    """
    d.execute_locator(l['meta_description'])
    ...
```

**Как работает функция**:

1.  Извлекает мета-описание товара, используя локатор `l['meta_description']` и метод `execute_locator` объекта `d` (driver).
2.  Функция не возвращает значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение мета-описания

### `field_meta_keywords`

```python
def field_meta_keywords():
    """

    @details
    """
    return d.execute_locator(l['meta_keywords'])
```

**Как работает функция**:

1.  Извлекает мета-ключевые слова товара, используя локатор `l['meta_keywords']` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченные ключевые слова.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение мета-ключевых слов
     |
     -- Возврат ключевых слов

### `field_meta_title`

```python
def field_meta_title():
    """

    @details
    """
    return d.execute_locator(l['meta_title'])
```

**Как работает функция**:

1.  Извлекает мета-заголовок товара, используя локатор `l['meta_title']` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченный заголовок.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение мета-заголовка
     |
     -- Возврат заголовка

### `field_is_virtual`

```python
def field_is_virtual():
    """

    @details
    """
    return f.is_virtual
```

**Как работает функция**:

1.  Возвращает значение `f.is_virtual`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.is_virtual`

### `field_isbn`

```python
def field_isbn():
    """

    @details
    """
    return f.isbn
```

**Как работает функция**:

1.  Возвращает значение `f.isbn`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.isbn`

### `field_link_rewrite`

```python
def field_link_rewrite(product_name: str) -> str:
    """Создается из переменной `product_name` которая содержит значение локатора l["name"]
    """
    return StringNormalizer.normalize_link_rewrite(product_name)
```

**Как работает функция**:

1.  Нормализует предоставленное имя продукта для создания понятного URL, используя функцию `StringNormalizer.normalize_link_rewrite`.
2.  Возвращает нормализованный URL.

**Внутри функции происходят следующие действия и преобразования**:

     Нормализация имени продукта
     |
     -- Возврат нормализованного URL

### `field_location`

```python
def field_location():
    """

    @details
    """
    return f.location
```

**Как работает функция**:

1.  Возвращает значение `f.location`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.location`

### `field_low_stock_alert`

```python
def field_low_stock_alert():
    """

    @details
    """
    return f.low_stock_alert
```

**Как работает функция**:

1.  Возвращает значение `f.low_stock_alert`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.low_stock_alert`

### `field_low_stock_threshold`

```python
def field_low_stock_threshold():
    """

    @details
    """
    return f.low_stock_threshold
```

**Как работает функция**:

1.  Возвращает значение `f.low_stock_threshold`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.low_stock_threshold`

### `field_meta_description`

```python
def field_meta_description():
    """

    @details
    """
    ...
```

**Как работает функция**:

1.  Функция не имеет реализации (содержит только `...`).

**Внутри функции происходят следующие действия и преобразования**:

     Нет действий

### `field_meta_keywords`

```python
def field_meta_keywords():
    """

    @details
    """
    return f.meta_keywords
```

**Как работает функция**:

1.  Возвращает значение `f.meta_keywords`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.meta_keywords`

### `field_meta_title`

```python
def field_meta_title():
    """

    @details
    """
    return f.meta_title
```

**Как работает функция**:

1.  Возвращает значение `f.meta_title`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.meta_title`

### `field_minimal_quantity`

```python
def field_minimal_quantity():
    """

    @details
    """
    return f.minimal_quantity
```

**Как работает функция**:

1.  Возвращает значение `f.minimal_quantity`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.minimal_quantity`

### `field_mpn`

```python
def field_mpn():
    """

    @details
    """
    return f.mpn
```

**Как работает функция**:

1.  Возвращает значение `f.mpn`.

**Внутри функции происходят следующие действия и преобразования**:

     Возврат значения `f.mpn`

### `field_name`

```python
def field_name(name: str):
    """Название товара
    Очищаю поля от лишних параметров, которые не проходят в престашоп
    """
    return StringNormalizer.normalize_product_name(name)
```

**Как работает функция**:

1.  Нормализует предоставленное имя продукта, используя функцию `StringNormalizer.normalize_product_name`.
2.  Возвращает нормализованное имя.

**Внутри функции происходят следующие действия и преобразования**:

     Нормализация имени продукта
     |
     -- Возврат нормализованного имени

### `field_online_only`

```python
def field_online_only():
    """товар только в интернет магазине

    @details
    """
    return d.execute_locator(l['online_only'])
```

**Как работает функция**:

1.  Извлекает информацию о том, доступен ли товар только в интернет-магазине, используя локатор `l['online_only']` и метод `execute_locator` объекта `d` (driver).
2.  Возвращает извлеченное значение.

**Внутри функции происходят следующие действия и преобразования**:

     Извлечение информации о доступности
     |
     -- Возврат значения

### `