# Модуль `graber`

## Обзор

Модуль `graber` предназначен для сбора информации о товарах с веб-страниц поставщиков. Он предоставляет базовый класс `Graber`, который использует веб-драйвер для извлечения целевых полей, таких как название, описание, спецификация, артикул и цена.

## Подробнее

Модуль предназначен для стандартизации процесса сбора данных о товарах с различных веб-сайтов поставщиков. Он использует локаторы, хранящиеся в JSON-файлах, для определения местоположения нужных элементов на странице. Это позволяет гибко настраивать процесс сбора данных для каждого поставщика. Для нестандартной обработки полей товара можно переопределить соответствующие функции в дочернем классе.

## Содержание

1.  [Класс `Context`](#класс-context)
2.  [Декоратор `close_pop_up`](#декоратор-close_pop_up)
3.  [Класс `Graber`](#класс-graber)
    *   [Метод `__init__`](#метод-__init__)
    *   [Метод `error`](#метод-error)
    *   [Метод `set_field_value`](#метод-set_field_value)
    *   [Метод `grab_page`](#метод-grab_page)
    *   [Метод `grab_page_async`](#метод-grab_page_async)
    *   [Метод `additional_shipping_cost`](#метод-additional_shipping_cost)
    *   [Метод `delivery_in_stock`](#метод-delivery_in_stock)
    *   [Метод `active`](#метод-active)
    *   [Метод `additional_delivery_times`](#метод-additional_delivery_times)
    *   [Метод `advanced_stock_management`](#метод-advanced_stock_management)
    *   [Метод `affiliate_short_link`](#метод-affiliate_short_link)
    *   [Метод `affiliate_summary`](#метод-affiliate_summary)
    *   [Метод `affiliate_summary_2`](#метод-affiliate_summary_2)
    *   [Метод `affiliate_text`](#метод-affiliate_text)
    *   [Метод `affiliate_image_large`](#метод-affiliate_image_large)
    *   [Метод `affiliate_image_medium`](#метод-affiliate_image_medium)
    *   [Метод `affiliate_image_small`](#метод-affiliate_image_small)
    *   [Метод `available_date`](#метод-available_date)
    *   [Метод `available_for_order`](#метод-available_for_order)
    *   [Метод `available_later`](#метод-available_later)
    *   [Метод `available_now`](#метод-available_now)
    *   [Метод `additional_categories`](#метод-additional_categories)
    *   [Метод `cache_default_attribute`](#метод-cache_default_attribute)
    *   [Метод `cache_has_attachments`](#метод-cache_has_attachments)
    *   [Метод `cache_is_pack`](#метод-cache_is_pack)
    *   [Метод `condition`](#метод-condition)
    *   [Метод `customizable`](#метод-customizable)
    *   [Метод `date_add`](#метод-date_add)
    *   [Метод `date_upd`](#метод-date_upd)
    *   [Метод `delivery_out_stock`](#метод-delivery_out_stock)
    *   [Метод `depth`](#метод-depth)
    *   [Метод `description`](#метод-description)
    *   [Метод `description_short`](#метод-description_short)
    *   [Метод `id_category_default`](#метод-id_category_default)
    *   [Метод `id_default_combination`](#метод-id_default_combination)
    *   [Метод `id_product`](#метод-id_product)
    *   [Метод `locale`](#метод-locale)
    *   [Метод `id_default_image`](#метод-id_default_image)
    *   [Метод `ean13`](#метод-ean13)
    *   [Метод `ecotax`](#метод-ecotax)
    *   [Метод `height`](#метод-height)
    *   [Метод `how_to_use`](#метод-how_to_use)
    *   [Метод `id_manufacturer`](#метод-id_manufacturer)
    *   [Метод `id_supplier`](#метод-id_supplier)
    *   [Метод `id_tax`](#метод-id_tax)
    *   [Метод `id_type_redirected`](#метод-id_type_redirected)
    *   [Метод `images_urls`](#метод-images_urls)
    *   [Метод `indexed`](#метод-indexed)
    *   [Метод `ingredients`](#метод-ingredients)
    *   [Метод `meta_description`](#метод-meta_description)
    *   [Метод `meta_keywords`](#метод-meta_keywords)
    *   [Метод `meta_title`](#метод-meta_title)
    *   [Метод `is_virtual`](#метод-is_virtual)
    *   [Метод `isbn`](#метод-isbn)
    *   [Метод `link_rewrite`](#метод-link_rewrite)
    *   [Метод `location`](#метод-location)
    *   [Метод `low_stock_alert`](#метод-low_stock_alert)
    *   [Метод `low_stock_threshold`](#метод-low_stock_threshold)
    *   [Метод `minimal_quantity`](#метод-minimal_quantity)
    *   [Метод `mpn`](#метод-mpn)
    *   [Метод `name`](#метод-name)
    *   [Метод `online_only`](#метод-online_only)
    *   [Метод `on_sale`](#метод-on_sale)
    *   [Метод `out_of_stock`](#метод-out_of_stock)
    *   [Метод `pack_stock_type`](#метод-pack_stock_type)
    *   [Метод `price`](#метод-price)
    *   [Метод `product_type`](#метод-product_type)
    *   [Метод `quantity`](#метод-quantity)
    *   [Метод `quantity_discount`](#метод-quantity_discount)
    *   [Метод `redirect_type`](#метод-redirect_type)
    *   [Метод `reference`](#метод-reference)
    *   [Метод `show_condition`](#метод-show_condition)
    *   [Метод `show_price`](#метод-show_price)
    *   [Метод `state`](#метод-state)
    *   [Метод `text_fields`](#метод-text_fields)
    *   [Метод `unit_price_ratio`](#метод-unit_price_ratio)
    *   [Метод `unity`](#метод-unity)
    *   [Метод `upc`](#метод-upc)
    *   [Метод `uploadable_files`](#метод-uploadable_files)
    *   [Метод `default_image_url`](#метод-default_image_url)
    *   [Метод `visibility`](#метод-visibility)
    *   [Метод `weight`](#метод-weight)
    *   [Метод `wholesale_price`](#метод-wholesale_price)
    *   [Метод `width`](#метод-width)
    *   [Метод `specification`](#метод-specification)
    *   [Метод `link`](#метод-link)
    *   [Метод `byer_protection`](#метод-byer_protection)
    *   [Метод `customer_reviews`](#метод-customer_reviews)
    *   [Метод `link_to_video`](#метод-link_to_video)
    *   [Метод `local_image_path`](#метод-local_image_path)
    *   [Метод `local_video_path`](#метод-local_video_path)

## Классы

### `Context`

```python
class Context:
    """
    Класс для хранения глобальных настроек.

    Attributes:
        driver (Optional['Driver']): Объект драйвера, используется для управления браузером или другим интерфейсом.
        locator_for_decorator (Optional[SimpleNamespace]): Если будет установлен - выполнится декоратор `@close_pop_up`.
            Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`.
        supplier_prefix (Optional[str]): Префикс поставщика.

    Example:
        >>> context = Context()
        >>> context.supplier_prefix = 'prefix'
        >>> print(context.supplier_prefix)
        prefix
    """

    # Аттрибуты класса
    driver: Optional['Driver'] = None
    locator_for_decorator: Optional[SimpleNamespace] = None  # <- Если будет установлен - выполнится декоратор `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`
    supplier_prefix: Optional[str] = None
```

**Описание**:

Класс `Context` предназначен для хранения глобальных настроек, используемых в процессе сбора данных. Он содержит атрибуты для хранения объекта драйвера, локатора для декоратора `@close_pop_up` и префикса поставщика.

**Как работает класс**:

Класс `Context` используется как хранилище глобальных параметров, которые могут быть доступны и изменены в различных частях программы. Это позволяет избежать передачи одних и тех же параметров между функциями и классами, упрощая код и повышая его читаемость.

## Декоратор

### `close_pop_up`

```python
def close_pop_up() -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.
    Функция `driver.execute_locator()` будет вызвана только если был указан `Context.locator_for_decorator` при инициализации экземляра класса.

    Args:
        value ('Driver'): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator:
                try:
                    await Context.driver.execute_locator(Context.locator_for_decorator)  # Await async pop-up close  
                    ... 
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', ex, False)

                finally:
                    Context.locator_for_decorator = None # Отмена после первого срабатывания

            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator
```

**Назначение**: Декоратор `close_pop_up` предназначен для закрытия всплывающих окон перед выполнением основной логики функции.

**Как работает декоратор**:

1.  Декоратор проверяет, установлен ли `Context.locator_for_decorator`. Если он установлен, это означает, что нужно закрыть всплывающее окно.
2.  Вызывается `Context.driver.execute_locator(Context.locator_for_decorator)` для выполнения локатора, который закроет всплывающее окно.
3.  После выполнения локатора `Context.locator_for_decorator` устанавливается в `None`, чтобы декоратор не срабатывал повторно.
4.  Основная логика функции выполняется после закрытия всплывающего окна.

## Классы

### `Graber`

```python
class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""

    def __init__(self, supplier_prefix: str, lang_index: int, driver: 'Driver'):
        """Инициализация класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика.
            lang_index (int): индекс языка.
            driver ('Driver'): Экземпляр класса Driver.
        """
        self.supplier_prefix = supplier_prefix
        self.locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
        self.driver = driver
        self.fields: ProductFields = ProductFields(lang_index)  # <- установка базового языка. Тип - `int`
        Context.driver = self.driver
        Context.supplier_prefix = None
        Context.locator_for_decorator = None
        """Если будет установлен локатор в Context.locator_for_decorator - выполнится декоратор `@close_pop_up`"""

    async def error(self, field: str):
        """Обработчик ошибок для полей."""
        logger.debug(f"Ошибка заполнения поля {field}")

    async def set_field_value(
        self,
        value: Any,
        locator_func: Callable[[], Any],
        field_name: str,
        default: Any = ''
    ) -> Any:
        """Универсальная функция для установки значений полей с обработкой ошибок.

        Args:
            value (Any): Значение для установки.
            locator_func (Callable[[], Any]): Функция для получения значения из локатора.
            field_name (str): Название поля.
            default (Any): Значение по умолчанию. По умолчанию пустая строка.

        Returns:
            Any: Установленное значение.
        """
        locator_result = await asyncio.to_thread(locator_func)
        if value:
            return value
        if locator_result:
            return locator_result
        await self.error(field_name)
        return default

    def grab_page(self, *args, **kwards) -> ProductFields:
        return asyncio.run(self.grab_page_async(*args, **kwards))

    async def grab_page_async(self, *args, **kwards) -> ProductFields:
        """Асинхронная функция для сбора полей продукта."""
        async def fetch_all_data(*args, **kwards):
            # Динамическое вызовы функций для каждого поля из args
            for filed_name in args:
                function = getattr(self, filed_name, None)
                if function:
                    await function(kwards.get(filed_name, ''))  # Просто вызываем с await, так как все функции асинхронные

        await fetch_all_data(*args, **kwards)
        return self.fields

    @close_pop_up()
    async def additional_shipping_cost(self, value: Optional[Any] = None):
        """Fetch and set additional shipping cost.
        Args:
        value (Any): это значение можно передать в словаре kwards чеез ключ {additional_shipping_cost = `value`} при определении класса
        если `value` был передан - его значение подставляется в поле `ProductFields.additional_shipping_cost`
        """
        try:
            # Получаем значение через execute_locator
            self.fields.additional_shipping_cost = normalize_string(value or await self.driver.execute_locator(self.locator.additional_shipping_cost) or '')
            if not self.fields.additional_shipping_cost:
                logger.error(f"Поле `additional_shipping_cost` не получиле значения")
                return

            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `additional_shipping_cost`", ex)
            ...
            return

    @close_pop_up()
    async def delivery_in_stock(self, value: Optional[Any] = None):
        """Fetch and set delivery in stock status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {delivery_in_stock = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.delivery_in_stock`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.delivery_in_stock = normalize_string(value or await self.driver.execute_locator(self.locator.delivery_in_stock) or '')
            if not self.fields.delivery_in_stock:
                logger.error(f"Поле `delivery_in_stock` не получиле значения")
                return
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `delivery_in_stock`", ex)
            ...
            return

    @close_pop_up()
    async def active(self, value: Optional[Any] = None):
        """Fetch and set active status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {active = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.active`.
        Принимаемое значениеЬ 1/0
        """
        try:
            # Получаем значение через execute_locator
            self.fields.active = normalize_int(value or await self.driver.execute_locator(self.locator.active) or 1)
            if not self.fields.active:
                return
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `active`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.active}")
            ...
            return

        # Записываем результат в поле `active` объекта `ProductFields`
        self.fields.active = value
        return True

    @close_pop_up()
    async def additional_delivery_times(self, value: Optional[Any] = None):
        """Fetch and set additional delivery times.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {additional_delivery_times = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.additional_delivery_times`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.additional_delivery_times) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `additional_delivery_times`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.additional_delivery_times}")
            ...
            return

        # Записываем результат в поле `additional_delivery_times` объекта `ProductFields`
        self.fields.additional_delivery_times = value
        return True

    @close_pop_up()
    async def advanced_stock_management(self, value: Optional[Any] = None):
        """Fetch and set advanced stock management status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {advanced_stock_management = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.advanced_stock_management`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.advanced_stock_management) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `advanced_stock_management`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.advanced_stock_management}")
            ...
            return

        # Записываем результат в поле `advanced_stock_management` объекта `ProductFields`
        self.fields.advanced_stock_management = value
        return True
    @close_pop_up()
    async def affiliate_short_link(self, value: Optional[Any] = None):
        """Fetch and set affiliate short link.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_short_link = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_short_link`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_short_link = value or await self.driver.execute_locator(self.locator.affiliate_short_link) or ''
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_short_link`", ex)
            ...
            return

    @close_pop_up()
    async def affiliate_summary(self, value: Optional[Any] = None):
        """Fetch and set affiliate summary.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_summary = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_summary = normalize_string(value or await self.driver.execute_locator(self.locator.affiliate_summary) or '')
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_summary`", ex)
            ...
            return

    @close_pop_up()
    async def affiliate_summary_2(self, value: Optional[Any] = None):
        """Fetch and set affiliate summary 2.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_summary_2 = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_summary_2`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.affiliate_summary_2) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_summary_2`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.affiliate_summary_2}")
            ...
            return

        # Записываем результат в поле `affiliate_summary_2` объекта `ProductFields`
        self.fields.affiliate_summary_2 = value
        return True

    @close_pop_up()
    async def affiliate_text(self, value: Optional[Any] = None):
        """Fetch and set affiliate text.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_text = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_text`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.affiliate_text) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_text`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.affiliate_text}")
            ...
            return

        # Записываем результат в поле `affiliate_text` объекта `ProductFields`
        self.fields.affiliate_text = value
        return True
    @close_pop_up()
    async def affiliate_image_large(self, value: Optional[Any] = None):
        """Fetch and set affiliate large image.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_image_large = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_large`.
        """
        try:
            # Получаем значение через execute_locator
            self.fields.affiliate_image_large = value or await self.driver.execute_locator(self.locator.affiliate_image_large) or ''
            return True
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_image_large`", ex)
            ...
            return

    @close_pop_up()
    async def affiliate_image_medium(self, value: Optional[Any] = None):
        """Fetch and set affiliate medium image.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_image_medium = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_medium`.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_medium) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_image_medium`", ex)
            ...
            return

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            ...
            return

        # Записываем результат в поле `affiliate_image_medium` объекта `ProductFields`
        self.fields.affiliate_image_medium = locator_result
        return True

    @close_pop_up()
    async def affiliate_image_small(self, value: Optional[Any] = None):
        """Fetch and set affiliate small image.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {affiliate_image_small = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.affiliate_image_small`.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.affiliate_image_small) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `affiliate_image_small`", ex)
            ...
            return

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            ...
            return

        # Записываем результат в поле `affiliate_image_small` объекта `ProductFields`
        self.fields.affiliate_image_small = locator_result
        return True

    @close_pop_up()
    async def available_date(self, value: Optional[Any] = None):
        """Fetch and set available date.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {available_date = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_date`.
        """
        try:
            # Получаем значение через execute_locator
            locator_result = value or await self.driver.execute_locator(self.locator.available_date) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_date`", ex)
            ...
            return

        # Проверка валидности `value`
        if not locator_result:
            logger.debug(f"Невалидный результат {locator_result=}")
            ...
            return

        # Записываем результат в поле `available_date` объекта `ProductFields`
        self.fields.available_date = locator_result
        return True
    @close_pop_up()
    async def available_for_order(self, value: Optional[Any] = None):
        """Fetch and set available for order status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {available_for_order = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_for_order`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_for_order) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_for_order`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_for_order}")
            ...
            return

        # Записываем результат в поле `available_for_order` объекта `ProductFields`
        self.fields.available_for_order = value
        return True

    @close_pop_up()
    async def available_later(self, value: Optional[Any] = None):
        """Fetch and set available later status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {available_later = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_later`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_later) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_later`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_later}")
            ...
            return

        # Записываем результат в поле `available_later` объекта `ProductFields`
        self.fields.available_later = value
        return True

    @close_pop_up()
    async def available_now(self, value: Optional[Any] = None):
        """Fetch and set available now status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {available_now = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.available_now`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.available_now) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `available_now`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.available_now}")
            ...
            return

        # Записываем результат в поле `available_now` объекта `ProductFields`
        self.fields.available_now = value
        return True

    @close_pop_up()
    async def additional_categories(self, value: str | list = None) -> dict:
        """Set additional categories.

        Это значение можно передать в словаре kwargs через ключ {additional_categories = `value`} при определении класса.
        Если `value` было передано, оно подставляется в поле `ProductFields.additional_categories`.

        Args:
        value (str | list, optional): Строка или список категорий. Если не передано, используется пустое значение.

        Returns:
        dict: Словарь с ID категорий.
        """
        self.fields.additional_categories = value or ''
        return {'additional_categories': self.fields.additional_categories}

    @close_pop_up()
    async def cache_default_attribute(self, value: Optional[Any] = None):
        """Fetch and set cache default attribute.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {cache_default_attribute = `value`} при определении класса.
        Если `value` был передан, его значение подставляется в поле `ProductFields.cache_default_attribute`.
        """
        try:
            # Получаем значение через execute_locator
            value = value or await self.driver.execute_locator(self.locator.cache_default_attribute) or ''
        except Exception as ex:
            logger.error(f"Ошибка получения значения в поле `cache_default_attribute`", ex)
            ...
            return

        # Проверка валидности `value`
        if not value:
            logger.debug(f"Невалидный результат {value=}\\nлокатор {self.locator.cache_default_attribute}")
            ...
            return

        # Записываем результат в поле `cache_default_attribute` объекта `ProductFields`
        self.fields.cache_default_attribute = value
        return True
    @close_pop_up()
    async def cache_has_attachments(self, value: Optional[Any] = None):
        """Fetch and set cache has attachments status.

        Args:
        value (Any): это значение можно передать в словаре kwargs через ключ {cache_has_attachments = `value`} при определении класса.
        Если `value