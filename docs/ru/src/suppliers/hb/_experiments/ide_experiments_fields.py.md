# src.suppliers.hb._experiments.ide_experiments_fields

## Обзор

Этот модуль содержит функции и классы, используемые для сбора и обработки данных о товарах с сайта поставщика HB (HBDeadsea). Он включает в себя функции для извлечения информации о товаре, такой как название, описание, цена, состав, и другие характеристики, а также для нормализации и подготовки этих данных для дальнейшей загрузки в PrestaShop.

## Подробней

Этот код является частью процесса автоматизации сбора данных о товарах с сайта HBDeadsea и их последующей загрузки в PrestaShop. Он использует Selenium для взаимодействия с веб-страницами, извлекает данные с помощью локаторов CSS и XPath, а затем нормализует эти данные, чтобы они соответствовали формату, требуемому для импорта в PrestaShop.
Этот файл содержит множество функций, каждая из которых отвечает за извлечение и обработку определенного поля продукта. Он также включает в себя функции для управления веб-драйвером, выполнения JavaScript и взаимодействия с API PrestaShop.

## Функции

### `grab_product_page`

```python
def grab_product_page(supplier: Supplier, async_run = True) -> ProductFields:
    """ Собираю со страницы товара значения вебэлементов и привожу их к полям ProductFields

    Args:
        supplier (Supplier): класс поставщика
         - вебдрайвер должен быть установлен на странице товара. 
        async_run (bool): Флаг, определяющий, следует ли запускать функцию асинхронно. По умолчанию `True`.

    Returns:
        ProductFields: Объект `ProductFields`, содержащий собранные и обработанные данные о товаре.

    Raises:
        Exception: Если возникает ошибка при выполнении локатора.
    """
```

**Описание**: Эта функция является основной функцией для сбора данных о товаре со страницы поставщика. Она принимает объект `Supplier` в качестве аргумента, который содержит информацию о поставщике, веб-драйвере и локаторах для элементов на странице товара.

**Как работает функция**:
1. Инициализирует глобальные переменные `s` (поставщик), `p` (продукт), `f` (поля продукта) и `l` (локаторы продукта).
2. Закрывает баннер на странице товара.
3. Прокручивает страницу для загрузки элементов, подгружаемых через AJAX.
4. Вызывает функции, специфичные для конкретного поставщика, для извлечения данных о товаре.
5. Устанавливает значения для различных полей объекта `ProductFields`, используя данные, полученные из веб-страницы.
6. Возвращает объект `ProductFields`, содержащий все собранные данные о товаре.

**Параметры**:
- `supplier` (Supplier): Объект класса `Supplier`, содержащий информацию о поставщике и веб-драйвере.
- `async_run` (bool, optional): Флаг, определяющий, следует ли запускать функцию асинхронно. По умолчанию `True`.

**Возвращает**:
- `ProductFields`: Объект `ProductFields`, содержащий собранные и обработанные данные о товаре.

**Примеры**:

```python
# Пример вызова функции grab_product_page
supplier = Supplier(supplier_prefix='hb')
driver = Driver()
supplier.driver = driver
product_fields = grab_product_page(supplier)
print(product_fields.name)
```

### `product_reference_and_volume_and_price_for_100`

```python
def product_reference_and_volume_and_price_for_100():
    """  Функция вытаскивает 3 поля:
    - volume,
    - supplier_reference,
    - цена за единицу товара 
    @todo Реализовать поле `цена за единицу товара`"""
```

**Описание**: Эта функция извлекает информацию об объеме продукта, артикуле поставщика и цене за единицу товара (за 100 мл).

**Как работает функция**:
1. Получает список веб-элементов, соответствующих локатору `product_reference_and_volume_and_price_for_100`.
2. Перебирает веб-элементы и извлекает информацию об объеме, цене за единицу товара и артикуле поставщика на основе текста каждого элемента.
3. Присваивает извлеченные значения соответствующим полям объекта `ProductFields`.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `f` (ProductFields), `s` (Supplier) и `d` (Driver).

**Возвращает**:
- Ничего явно не возвращает, но изменяет состояние глобального объекта `f` (ProductFields).

**Примеры**:

```python
# Пример вызова функции product_reference_and_volume_and_price_for_100
product_reference_and_volume_and_price_for_100()
print(f.volume)
print(f.supplier_reference)
```

### `set_references`

```python
def set_references(f, s):
    """ все, что касается id товара """
```

**Описание**: Эта функция устанавливает значения для полей, связанных с идентификацией товара, таких как `id_supplier` и `reference`.

**Как работает функция**:
1. Устанавливает значение поля `id_supplier` равным `s.supplier_id` (идентификатор поставщика).
2. Формирует значение поля `reference` путем объединения `s.supplier_id` и `f.supplier_reference`.

**Параметры**:
- `f` (ProductFields): Объект `ProductFields`, поля которого необходимо установить.
- `s` (Supplier): Объект `Supplier`, содержащий информацию о поставщике.

**Возвращает**:
- Ничего явно не возвращает, но изменяет состояние объекта `f` (ProductFields).

**Примеры**:

```python
# Пример вызова функции set_references
set_references(f, s)
print(f.id_supplier)
print(f.reference)
```

### `field_additional_shipping_cost`

```python
def field_additional_shipping_cost():
    """  
    стоимость доставки
    @details
    """
    return d.execute_locator(l["additional_shipping_cost"])
```

**Описание**: Эта функция извлекает стоимость доставки товара.

**Как работает функция**:
1. Выполняет локатор `additional_shipping_cost` с помощью веб-драйвера `d`.
2. Возвращает результат выполнения локатора, который представляет собой стоимость доставки.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Стоимость доставки товара.

**Примеры**:

```python
# Пример вызова функции field_additional_shipping_cost
additional_shipping_cost = field_additional_shipping_cost()
print(additional_shipping_cost)
```

### `field_delivery_in_stock`

```python
def field_delivery_in_stock():
    """  
    Доставка, когда товар в наличии
    @details
    """
    return str(d.execute_locator(l["delivery_in_stock"]))
```

**Описание**: Эта функция извлекает информацию о доставке, когда товар есть в наличии.

**Как работает функция**:
1. Выполняет локатор `delivery_in_stock` с помощью веб-драйвера `d`.
2. Преобразует результат выполнения локатора в строку и возвращает ее.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Информация о доставке, когда товар есть в наличии.

**Примеры**:

```python
# Пример вызова функции field_delivery_in_stock
delivery_in_stock = field_delivery_in_stock()
print(delivery_in_stock)
```

### `field_active`

```python
def field_active():
    """  
    
    @details
    """
    return f.active    # <-  поставить в зависимость от delivery_out_stock
```

**Описание**: Эта функция возвращает значение активности товара.

**Как работает функция**:
1. Возвращает значение поля `f.active` (активность товара).

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Значение активности товара.

**Примеры**:

```python
# Пример вызова функции field_active
active = field_active()
print(active)
```

### `field_additional_delivery_times`

```python
def field_additional_delivery_times():
    """  
    
    @details
    """
    return d.execute_locator(l["additional_delivery_times"])
```

**Описание**: Эта функция извлекает информацию о дополнительном времени доставки.

**Как работает функция**:
1. Выполняет локатор `additional_delivery_times` с помощью веб-драйвера `d`.
2. Возвращает результат выполнения локатора, который представляет собой дополнительное время доставки.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Информация о дополнительном времени доставки.

**Примеры**:

```python
# Пример вызова функции field_additional_delivery_times
additional_delivery_times = field_additional_delivery_times()
print(additional_delivery_times)
```

### `field_advanced_stock_management`

```python
def field_advanced_stock_management():
    """  
    
    @details
    """
    return f.advanced_stock_management
```

**Описание**: Эта функция возвращает значение, указывающее, используется ли расширенное управление запасами.

**Как работает функция**:
1. Возвращает значение поля `f.advanced_stock_management`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Значение, указывающее, используется ли расширенное управление запасами.

**Примеры**:

```python
# Пример вызова функции field_advanced_stock_management
advanced_stock_management = field_advanced_stock_management()
print(advanced_stock_management)
```

### `field_affiliate_short_link`

```python
def field_affiliate_short_link():
    """  
    
    @details
    """
    return d.current_url
```

**Описание**: Эта функция возвращает текущий URL веб-драйвера, который используется в качестве короткой партнерской ссылки.

**Как работает функция**:
1. Возвращает значение `d.current_url` (текущий URL веб-драйвера).

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `d` (Driver).

**Возвращает**:
- Текущий URL веб-драйвера.

**Примеры**:

```python
# Пример вызова функции field_affiliate_short_link
affiliate_short_link = field_affiliate_short_link()
print(affiliate_short_link)
```

### `field_affiliate_summary`

```python
def field_affiliate_summary():
    """  
    
    @details
    """
    return f.affiliate_summary
```

**Описание**: Эта функция возвращает краткое описание партнерской программы.

**Как работает функция**:
1. Возвращает значение поля `f.affiliate_summary`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Краткое описание партнерской программы.

**Примеры**:

```python
# Пример вызова функции field_affiliate_summary
affiliate_summary = field_affiliate_summary()
print(affiliate_summary)
```

### `field_affiliate_summary_2`

```python
def field_affiliate_summary_2():
    """  
    
    @details
    """
    return f.affiliate_summary_2
```

**Описание**: Эта функция возвращает дополнительное краткое описание партнерской программы.

**Как работает функция**:
1. Возвращает значение поля `f.affiliate_summary_2`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Дополнительное краткое описание партнерской программы.

**Примеры**:

```python
# Пример вызова функции field_affiliate_summary_2
affiliate_summary_2 = field_affiliate_summary_2()
print(affiliate_summary_2)
```

### `field_affiliate_text`

```python
def field_affiliate_text():
    """  
    
    @details
    """
    return f.affiliate_text
```

**Описание**: Эта функция возвращает текст партнерской программы.

**Как работает функция**:
1. Возвращает значение поля `f.affiliate_text`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Текст партнерской программы.

**Примеры**:

```python
# Пример вызова функции field_affiliate_text
affiliate_text = field_affiliate_text()
print(affiliate_text)
```

### `field_affiliate_image_large`

```python
def field_affiliate_image_large():
    """  
    
    @details
    """
```

**Описание**: Эта функция должна была возвращать большую картинку для партнерской программы, но в текущем коде она не реализована.

**Как работает функция**:
1. В текущем коде отсутствует реализация функции.

**Параметры**:
- Нет явных параметров.

**Возвращает**:
- Отсутствует возвращаемое значение, так как функция не реализована.

**Примеры**:
- Невозможно привести пример, так как функция не реализована.

### `field_affiliate_image_medium`

```python
def field_affiliate_image_medium():
    """  
    
    @details
    """
```

**Описание**: Эта функция должна была возвращать среднюю картинку для партнерской программы, но в текущем коде она не реализована.

**Как работает функция**:
1. В текущем коде отсутствует реализация функции.

**Параметры**:
- Нет явных параметров.

**Возвращает**:
- Отсутствует возвращаемое значение, так как функция не реализована.

**Примеры**:
- Невозможно привести пример, так как функция не реализована.

### `field_affiliate_image_small`

```python
def field_affiliate_image_small():
    """  
    
    @details
    """
    return d.execute_locator(l["affiliate_image_small"])
```

**Описание**: Эта функция извлекает маленькое изображение партнерской программы.

**Как работает функция**:
1. Выполняет локатор `affiliate_image_small` с помощью веб-драйвера `d`.
2. Возвращает результат выполнения локатора, который представляет собой маленькое изображение партнерской программы.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Маленькое изображение партнерской программы.

**Примеры**:

```python
# Пример вызова функции field_affiliate_image_small
affiliate_image_small = field_affiliate_image_small()
print(affiliate_image_small)
```

### `field_available_date`

```python
def field_available_date():
    """  
    
    @details
    """
    return f.available_date
```

**Описание**: Эта функция возвращает дату доступности товара.

**Как работает функция**:
1. Возвращает значение поля `f.available_date`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Дата доступности товара.

**Примеры**:

```python
# Пример вызова функции field_available_date
available_date = field_available_date()
print(available_date)
```

### `field_available_for_order`

```python
def field_available_for_order():
    """  Если вернулся вебэлемент, это флаг, что товара нет в наличии, а вернулся <p>המלאי אזל
    """
    available_for_order = d.execute_locator(l["available_for_order"])
    if available_for_order is None:
        f.available_for_order = 1
    else:
        f.available_for_order = 0
        f.active = 0
```

**Описание**: Эта функция определяет, доступен ли товар для заказа.

**Как работает функция**:
1. Выполняет локатор `available_for_order` с помощью веб-драйвера `d`.
2. Если локатор возвращает `None`, это означает, что товар доступен для заказа, и устанавливает `f.available_for_order = 1`.
3. В противном случае устанавливает `f.available_for_order = 0` и `f.active = 0`, что означает, что товар недоступен для заказа и деактивирован.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver), `l` (локаторы продукта) и `f` (ProductFields).

**Возвращает**:
- Ничего явно не возвращает, но изменяет состояние объекта `f` (ProductFields).

**Примеры**:

```python
# Пример вызова функции field_available_for_order
field_available_for_order()
print(f.available_for_order)
print(f.active)
```

### `field_available_later`

```python
def field_available_later():
    """  
    
    @details
    """
    return f.available_later
```

**Описание**: Эта функция возвращает текст сообщения о доступности товара позже.

**Как работает функция**:
1. Возвращает значение поля `f.available_later`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Текст сообщения о доступности товара позже.

**Примеры**:

```python
# Пример вызова функции field_available_later
available_later = field_available_later()
print(available_later)
```

### `field_available_now`

```python
def field_available_now():
    """  
    
    @details
    """
    return f.available_now
```

**Описание**: Эта функция возвращает текст сообщения о доступности товара сейчас.

**Как работает функция**:
1. Возвращает значение поля `f.available_now`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Текст сообщения о доступности товара сейчас.

**Примеры**:

```python
# Пример вызова функции field_available_now
available_now = field_available_now()
print(available_now)
```

### `field_category_ids`

```python
def field_category_ids():
    """  
    
    @details
    """
    return f.category_ids
```

**Описание**: Эта функция возвращает идентификаторы категорий товара.

**Как работает функция**:
1. Возвращает значение поля `f.category_ids`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Идентификаторы категорий товара.

**Примеры**:

```python
# Пример вызова функции field_category_ids
category_ids = field_category_ids()
print(category_ids)
```

### `field_category_ids_append`

```python
def field_category_ids_append():
    """  
    
    @details
    """
    #return f.category_ids_append
```

**Описание**: Эта функция должна была возвращать идентификаторы категорий товара для добавления, но в текущем коде она не реализована.

**Как работает функция**:
1. В текущем коде отсутствует реализация функции.

**Параметры**:
- Нет явных параметров.

**Возвращает**:
- Отсутствует возвращаемое значение, так как функция не реализована.

**Примеры**:
- Невозможно привести пример, так как функция не реализована.

### `field_cache_default_attribute`

```python
def field_cache_default_attribute():
    """  
    
    @details
    """
    return f.cache_default_attribute
```

**Описание**: Эта функция возвращает идентификатор атрибута по умолчанию для кэширования.

**Как работает функция**:
1. Возвращает значение поля `f.cache_default_attribute`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Идентификатор атрибута по умолчанию для кэширования.

**Примеры**:

```python
# Пример вызова функции field_cache_default_attribute
cache_default_attribute = field_cache_default_attribute()
print(cache_default_attribute)
```

### `field_cache_has_attachments`

```python
def field_cache_has_attachments():
    """  
    
    @details
    """
    return f.cache_has_attachments
```

**Описание**: Эта функция возвращает флаг, указывающий, есть ли у товара вложения для кэширования.

**Как работает функция**:
1. Возвращает значение поля `f.cache_has_attachments`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Флаг, указывающий, есть ли у товара вложения для кэширования.

**Примеры**:

```python
# Пример вызова функции field_cache_has_attachments
cache_has_attachments = field_cache_has_attachments()
print(cache_has_attachments)
```

### `field_cache_is_pack`

```python
def field_cache_is_pack():
    """  
    
    @details
    """
    return f.cache_is_pack
```

**Описание**: Эта функция возвращает флаг, указывающий, является ли товар комплектом для кэширования.

**Как работает функция**:
1. Возвращает значение поля `f.cache_is_pack`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Флаг, указывающий, является ли товар комплектом для кэширования.

**Примеры**:

```python
# Пример вызова функции field_cache_is_pack
cache_is_pack = field_cache_is_pack()
print(cache_is_pack)
```

### `field_condition`

```python
def field_condition():
    """  
    
    @details
    """
    return d.execute_locator(l.condition)
```

**Описание**: Эта функция извлекает условие (состояние) товара.

**Как работает функция**:
1. Выполняет локатор `condition` с помощью веб-драйвера `d`.
2. Возвращает результат выполнения локатора, который представляет собой условие товара.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Условие (состояние) товара.

**Примеры**:

```python
# Пример вызова функции field_condition
condition = field_condition()
print(condition)
```

### `field_customizable`

```python
def field_customizable():
    """  
    
    @details
    """
    return f.customizable
```

**Описание**: Эта функция возвращает флаг, указывающий, настраиваемый ли товар.

**Как работает функция**:
1. Возвращает значение поля `f.customizable`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Флаг, указывающий, настраиваемый ли товар.

**Примеры**:

```python
# Пример вызова функции field_customizable
customizable = field_customizable()
print(customizable)
```

### `field_date_add`

```python
def field_date_add():
    """  
    
    @details
    """
    return f.date_add
```

**Описание**: Эта функция возвращает дату добавления товара.

**Как работает функция**:
1. Возвращает значение поля `f.date_add`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Дата добавления товара.

**Примеры**:

```python
# Пример вызова функции field_date_add
date_add = field_date_add()
print(date_add)
```

### `field_date_upd`

```python
def field_date_upd():
    """  
    
    @details
    """
    return f.date_upd
```

**Описание**: Эта функция возвращает дату обновления товара.

**Как работает функция**:
1. Возвращает значение поля `f.date_upd`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Дата обновления товара.

**Примеры**:

```python
# Пример вызова функции field_date_upd
date_upd = field_date_upd()
print(date_upd)
```

### `field_delivery_out_stock`

```python
def field_delivery_out_stock():
    """  
    Заметка о доставке, когда товара нет в наличии
    """
    return f.delivery_out_stock
```

**Описание**: Эта функция возвращает заметку о доставке, когда товара нет в наличии.

**Как работает функция**:
1. Возвращает значение поля `f.delivery_out_stock`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Заметка о доставке, когда товара нет в наличии.

**Примеры**:

```python
# Пример вызова функции field_delivery_out_stock
delivery_out_stock = field_delivery_out_stock()
print(delivery_out_stock)
```

### `field_depth`

```python
def field_depth():
    """  
    @details
    """
    return d.execute_locator ( l ["depth"] )
```

**Описание**: Эта функция извлекает глубину товара.

**Как работает функция**:
1. Выполняет локатор `depth` с помощью веб-драйвера `d`.
2. Возвращает результат выполнения локатора, который представляет собой глубину товара.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Глубина товара.

**Примеры**:

```python
# Пример вызова функции field_depth
depth = field_depth()
print(depth)
```

### `field_description`

```python
def field_description():
    """  поле полного описания товара 
    @details
    """
    return d.execute_locator (l["description"] )[0].text
```

**Описание**: Эта функция извлекает полное описание товара.

**Как работает функция**:
1. Выполняет локатор `description` с помощью веб-драйвера `d`.
2. Возвращает текст первого элемента, найденного по локатору, который представляет собой полное описание товара.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Полное описание товара.

**Примеры**:

```python
# Пример вызова функции field_description
description = field_description()
print(description)
```

### `field_id_category_default`

```python
def field_id_category_default():
    """  Главная категория товара. Берется из сценария """
    return s.current_scenario["presta_categories"]["default_category"]
```

**Описание**: Эта функция возвращает идентификатор главной категории товара, взятый из сценария.

**Как работает функция**:
1. Возвращает значение `s.current_scenario["presta_categories"]["default_category"]`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `s` (Supplier).

**Возвращает**:
- Идентификатор главной категории товара.

**Примеры**:

```python
# Пример вызова функции field_id_category_default
id_category_default = field_id_category_default()
print(id_category_default)
```

### `field_ean13`

```python
def field_ean13():
    """  
    
    @details
    """
    return d.execute_locator ( l ["ean13"] )
```

**Описание**: Эта функция извлекает EAN13 код товара.

**Как работает функция**:
1. Выполняет локатор `ean13` с помощью веб-драйвера `d`.
2. Возвращает результат выполнения локатора, который представляет собой EAN13 код товара.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- EAN13 код товара.

**Примеры**:

```python
# Пример вызова функции field_ean13
ean13 = field_ean13()
print(ean13)
```

### `field_ecotax`

```python
def field_ecotax():
    """  
    
    @details
    """
    return f.ecotax
```

**Описание**: Эта функция возвращает ecotax товара.

**Как работает функция**:
1. Возвращает значение поля `f.ecotax`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- Ecotax товара.

**Примеры**:

```python
# Пример вызова функции field_ecotax
ecotax = field_ecotax()
print(ecotax)
```

### `field_height`

```python
def field_height():
    """  
    
    @details
    """
    return d.execute_locator ( l ["height"] )
```

**Описание**: Эта функция извлекает высоту товара.

**Как работает функция**:
1. Выполняет локатор `height` с помощью веб-драйвера `d`.
2. Возвращает результат выполнения локатора, который представляет собой высоту товара.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Высота товара.

**Примеры**:

```python
# Пример вызова функции field_height
height = field_height()
print(height)
```

### `field_how_to_use`

```python
def field_how_to_use():
    """  
    
    @details
    """
    return d.execute_locator ( l ["how_to_use"] ) [0].text
```

**Описание**: Эта функция извлекает инструкцию о том, как использовать товар.

**Как работает функция**:
1. Выполняет локатор `how_to_use` с помощью веб-драйвера `d`.
2. Возвращает текст первого элемента, найденного по локатору, который представляет собой инструкцию о том, как использовать товар.

**Параметры**:
- Нет явных параметров, но использует глобальные переменные `d` (Driver) и `l` (локаторы продукта).

**Возвращает**:
- Инструкция о том, как использовать товар.

**Примеры**:

```python
# Пример вызова функции field_how_to_use
how_to_use = field_how_to_use()
print(how_to_use)
```

### `field_id_default_combination`

```python
def field_id_default_combination():
    """  
    
    @details
    """
    return f.id_default_combination
```

**Описание**: Эта функция возвращает ID комбинации по умолчанию.

**Как работает функция**:
1. Возвращает значение поля `f.id_default_combination`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- ID комбинации по умолчанию.

**Примеры**:

```python
# Пример вызова функции field_id_default_combination
id_default_combination = field_id_default_combination()
print(id_default_combination)
```

### `field_id_default_image`

```python
def field_id_default_image():
    """  
    
    @details
    """
    return f.id_default_image
```

**Описание**: Эта функция возвращает ID изображения по умолчанию.

**Как работает функция**:
1. Возвращает значение поля `f.id_default_image`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- ID изображения по умолчанию.

**Примеры**:

```python
# Пример вызова функции field_id_default_image
id_default_image = field_id_default_image()
print(id_default_image)
```

### `field_id_lang`

```python
def field_id_lang():
    """  
    
    @details
    """
    return f.id_lang
```

**Описание**: Эта функция возвращает ID языка.

**Как работает функция**:
1. Возвращает значение поля `f.id_lang`.

**Параметры**:
- Нет явных параметров, но использует глобальную переменную `f` (ProductFields).

**Возвращает**:
- ID языка.

**Примеры**:

```python
# Пример вызова функции field_id_lang
id_lang = field_id_lang()
print(id_lang)
```

### `field_id_manufacturer`

```python
def field_id_manufacturer():
    """  ID бренда. Может быть и названием бренда - престашоп сам разберется """
    return d.execute_locator(l["id_manufacturer"])
```

**Описание**: Эта функция возвращает ID производителя товара.

**Как работает функция**: