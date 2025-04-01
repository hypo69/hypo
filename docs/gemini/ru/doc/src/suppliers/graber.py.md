# Модуль `graber.py`

## Обзор

Модуль `graber.py` является частью проекта `hypotez` и предназначен для сбора информации о товарах с веб-страниц поставщиков. Он содержит базовый класс `Graber`, который использует веб-драйвер для извлечения целевых полей, таких как название, описание, спецификация, артикул и цена, с HTML-страниц. Локаторы для этих полей хранятся в JSON-файлах в директории `locators` каждого поставщика. Модуль также включает функциональность для обработки всплывающих окон и нормализации данных.

## Подробнее

Модуль предоставляет гибкий способ сбора данных о товарах, позволяя переопределять функции для нестандартной обработки полей. Он также использует декоратор `@close_pop_up` для автоматического закрытия всплывающих окон перед выполнением основной логики функций.

## Содержание

1.  [Классы](#классы)
    *   [Context](#context)
    *   [Graber](#graber)
2.  [Функции](#функции)
    *   [close_pop_up](#close_pop_up)

## Классы

### `Context`

**Описание**: Класс для хранения глобальных настроек, таких как драйвер, локатор для декоратора и префикс поставщика.

**Атрибуты**:

*   `driver` (Optional['Driver']): Объект драйвера для управления браузером.
*   `locator_for_decorator` (Optional[SimpleNamespace]): Локатор для выполнения декоратором `@close_pop_up`.
*   `supplier_prefix` (Optional[str]): Префикс поставщика.

### `Graber`

**Описание**: Базовый класс для сбора данных со страницы товара для всех поставщиков.

**Принцип работы**:

Класс `Graber` инициализируется с префиксом поставщика, индексом языка и драйвером. Он загружает локаторы из JSON-файла, устанавливает драйвер в контексте и предоставляет методы для извлечения и нормализации данных о товаре.

**Методы**:

*   `__init__(supplier_prefix: str, lang_index: int, driver: 'Driver')`: Инициализирует класс Graber.
*   `error(field: str)`: Обработчик ошибок для полей.
*   `set_field_value(value: Any, locator_func: Callable[[], Any], field_name: str, default: Any = '')`: Универсальная функция для установки значений полей с обработкой ошибок.
*   `grab_page(*args, **kwards) -> ProductFields`: Запускает асинхронную функцию для сбора полей продукта.
*   `grab_page_async(*args, **kwards) -> ProductFields`: Асинхронная функция для сбора полей продукта.
*   `additional_shipping_cost(value: Optional[Any] = None)`: Извлекает и устанавливает дополнительную стоимость доставки.
*   `delivery_in_stock(value: Optional[Any] = None)`: Извлекает и устанавливает статус доставки в наличии.
*   `active(value: Optional[Any] = None)`: Извлекает и устанавливает статус активности.
*   `additional_delivery_times(value: Optional[Any] = None)`: Извлекает и устанавливает дополнительное время доставки.
*   `advanced_stock_management(value: Optional[Any] = None)`: Извлекает и устанавливает статус расширенного управления запасами.
*   `affiliate_short_link(value: Optional[Any] = None)`: Извлекает и устанавливает короткую партнерскую ссылку.
*   `affiliate_summary(value: Optional[Any] = None)`: Извлекает и устанавливает партнерский обзор.
*   `affiliate_summary_2(value: Optional[Any] = None)`: Извлекает и устанавливает второй партнерский обзор.
*   `affiliate_text(value: Optional[Any] = None)`: Извлекает и устанавливает партнерский текст.
*   `affiliate_image_large(value: Optional[Any] = None)`: Извлекает и устанавливает большое партнерское изображение.
*   `affiliate_image_medium(value: Optional[Any] = None)`: Извлекает и устанавливает среднее партнерское изображение.
*   `affiliate_image_small(value: Optional[Any] = None)`: Извлекает и устанавливает маленькое партнерское изображение.
*   `available_date(value: Optional[Any] = None)`: Извлекает и устанавливает дату доступности.
*   `available_for_order(value: Optional[Any] = None)`: Извлекает и устанавливает статус доступности для заказа.
*   `available_later(value: Optional[Any] = None)`: Извлекает и устанавливает статус "доступно позже".
*   `available_now(value: Optional[Any] = None)`: Извлекает и устанавливает статус "доступно сейчас".
*   `additional_categories(value: str | list = None) -> dict`: Устанавливает дополнительные категории.
*   `cache_default_attribute(value: Optional[Any] = None)`: Извлекает и устанавливает кэшированный атрибут по умолчанию.
*   `cache_has_attachments(value: Optional[Any] = None)`: Извлекает и устанавливает статус наличия вложений в кэше.
*   `cache_is_pack(value: Optional[Any] = None)`: Извлекает и устанавливает статус "является ли набором" в кэше.
*   `condition(value: Optional[Any] = None)`: Извлекает и устанавливает состояние продукта.
*   `customizable(value: Optional[Any] = None)`: Извлекает и устанавливает статус настраиваемости.
*   `date_add(value: Optional[str | datetime.date] = None)`: Извлекает и устанавливает дату добавления.
*   `date_upd(value: Optional[Any] = None)`: Извлекает и устанавливает дату обновления.
*   `delivery_out_stock(value: Optional[Any] = None)`: Извлекает и устанавливает статус доставки при отсутствии на складе.
*   `depth(value: Optional[Any] = None)`: Извлекает и устанавливает глубину.
*   `description(value: Optional[Any] = None)`: Извлекает и устанавливает описание.
*   `description_short(value: Optional[Any] = None)`: Извлекает и устанавливает краткое описание.
*   `id_category_default(value: Optional[Any] = None)`: Извлекает и устанавливает ID категории по умолчанию.
*   `id_default_combination(value: Optional[Any] = None)`: Извлекает и устанавливает ID комбинации по умолчанию.
*   `id_product(value: Optional[Any] = None)`: Извлекает и устанавливает ID продукта.
*   `locale(value: Optional[Any] = None)`: Извлекает и устанавливает локаль.
*   `id_default_image(value: Optional[Any] = None)`: Извлекает и устанавливает ID изображения по умолчанию.
*   `ean13(value: Optional[Any] = None)`: Извлекает и устанавливает код EAN13.
*   `ecotax(value: Optional[Any] = None)`: Извлекает и устанавливает ecotax.
*   `height(value: Optional[Any] = None)`: Извлекает и устанавливает высоту.
*   `how_to_use(value: Optional[Any] = None)`: Извлекает и устанавливает информацию о том, как использовать.
*   `id_manufacturer(value: Optional[Any] = None)`: Извлекает и устанавливает ID производителя.
*   `id_supplier(value: Optional[Any] = None)`: Извлекает и устанавливает ID поставщика.
*   `id_tax(value: Optional[Any] = None)`: Извлекает и устанавливает ID налога.
*   `id_type_redirected(value: Optional[Any] = None)`: Извлекает и устанавливает ID типа переадресации.
*   `images_urls(value: Optional[Any] = None)`: Извлекает и устанавливает URL изображений.
*   `indexed(value: Optional[Any] = None)`: Извлекает и устанавливает статус индексации.
*   `ingredients(value: Optional[Any] = None)`: Извлекает и устанавливает ингредиенты.
*   `meta_description(value: Optional[Any] = None)`: Извлекает и устанавливает мета-описание.
*   `meta_keywords(value: Optional[Any] = None)`: Извлекает и устанавливает мета-ключевые слова.
*   `meta_title(value: Optional[Any] = None)`: Извлекает и устанавливает мета-заголовок.
*   `is_virtual(value: Optional[Any] = None)`: Извлекает и устанавливает виртуальный статус.
*   `isbn(value: Optional[Any] = None)`: Извлекает и устанавливает ISBN.
*   `link_rewrite(value: Optional[Any] = None)`: Извлекает и устанавливает перезапись ссылки.
*   `location(value: Optional[Any] = None)`: Извлекает и устанавливает местоположение.
*   `low_stock_alert(value: Optional[Any] = None)`: Извлекает и устанавливает оповещение о низком уровне запасов.
*   `low_stock_threshold(value: Optional[Any] = None)`: Извлекает и устанавливает порог низкого уровня запасов.
*   `minimal_quantity(value: Optional[Any] = None)`: Извлекает и устанавливает минимальное количество.
*   `mpn(value: Optional[Any] = None)`: Извлекает и устанавливает MPN (Manufacturer Part Number).
*   `name(value: Optional[Any] = None)`: Извлекает и устанавливает название продукта.
*   `online_only(value: Optional[Any] = None)`: Извлекает и устанавливает статус "только онлайн".
*   `on_sale(value: Optional[Any] = None)`: Извлекает и устанавливает статус "в продаже".
*   `out_of_stock(value: Optional[Any] = None)`: Извлекает и устанавливает статус "нет в наличии".
*   `pack_stock_type(value: Optional[Any] = None)`: Извлекает и устанавливает тип запаса упаковки.
*   `price(value: Optional[Any] = None)`: Извлекает и устанавливает цену.
*   `product_type(value: Optional[Any] = None)`: Извлекает и устанавливает тип продукта.
*   `quantity(value: Optional[Any] = None)`: Извлекает и устанавливает количество.
*   `quantity_discount(value: Optional[Any] = None)`: Извлекает и устанавливает скидку за количество.
*   `redirect_type(value: Optional[Any] = None)`: Извлекает и устанавливает тип переадресации.
*   `reference(value: Optional[Any] = None)`: Извлекает и устанавливает ссылку.
*   `show_condition(value: Optional[int] = None)`: Извлекает и устанавливает отображение состояния.
*   `show_price(value: Optional[int] = None)`: Извлекает и устанавливает отображение цены.
*   `state(value: Optional[Any] = None)`: Извлекает и устанавливает состояние.
*   `text_fields(value: Optional[Any] = None)`: Извлекает и устанавливает текстовые поля.
*   `unit_price_ratio(value: Optional[Any] = None)`: Извлекает и устанавливает отношение цены за единицу.
*   `unity(value: Optional[str] = None)`: Извлекает и устанавливает единство.
*   `upc(value: Optional[str] = None)`: Извлекает и устанавливает UPC.
*   `uploadable_files(value: Optional[Any] = None)`: Извлекает и устанавливает загружаемые файлы.
*   `default_image_url(value: Optional[Any] = None)`: Извлекает и устанавливает URL изображения по умолчанию.
*   `visibility(value: Optional[str] = None)`: Извлекает и устанавливает видимость.
*   `weight(value: Optional[float] = None)`: Извлекает и устанавливает вес.
*   `wholesale_price(value: Optional[float] = None)`: Извлекает и устанавливает оптовую цену.
*   `width(value: Optional[float] = None)`: Извлекает и устанавливает ширину.
    *   `specification(value: Optional[str|list] = None)`: Извлекает и устанавливает спецификацию.
*   `link(value: Optional[str] = None)`: Извлекает и устанавливает ссылку.
*   `byer_protection(value: Optional[str|list] = None)`: Извлекает и устанавливает защиту покупателя.
*   `customer_reviews(value: Optional[Any] = None)`: Извлекает и устанавливает отзывы клиентов.
*   `link_to_video(value: Optional[Any] = None)`: Извлекает и устанавливает ссылку на видео.
*   `local_image_path(value: Optional[str] = None)`: Извлекает и сохраняет изображение локально.
*   `local_video_path(value: Optional[Any] = None)`: Извлекает и сохраняет видео локально.

## Функции

### `close_pop_up`

**Описание**: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Как работает функция**:

1.  Определяет декоратор `decorator`, который принимает функцию `func` в качестве аргумента.
2.  Внутри декоратора определяется обертка `wrapper`, которая выполняется перед вызовом основной функции.
3.  Проверяет, установлен ли `Context.locator_for_decorator`. Если установлен, пытается выполнить локатор для закрытия всплывающего окна.
4.  После выполнения локатора или в случае ошибки, сбрасывает `Context.locator_for_decorator`.
5.  Вызывает основную функцию `func` и возвращает результат.

**Параметры**:

*   `value` ('Driver'): Дополнительное значение для декоратора.

**Возвращает**:

*   `Callable`: Декоратор, оборачивающий функцию.

**Примеры**:

```python
@close_pop_up()
async def some_function(param: str) -> None:
    ...
```

ASCII Flowchart:

```
    A: Проверка Context.locator_for_decorator
    |
    B: Выполнение Context.driver.execute_locator(Context.locator_for_decorator)
    |
    C: Сброс Context.locator_for_decorator
    |
    D: Вызов func(*args, **kwargs)