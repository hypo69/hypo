# Локаторы для продукта

## Обзор

Данный файл `product.json` содержит JSON-объект, описывающий локаторы для различных атрибутов продукта на веб-странице. Локаторы используются для извлечения или взаимодействия с элементами страницы во время автоматизированного сбора данных.

## Оглавление

1. [Описание структуры](#описание-структуры)
2. [Локаторы](#локаторы)

## Описание структуры

JSON-объект представляет собой словарь, где ключи являются именами полей продукта, а значения - это словари с параметрами локаторов. Каждый локатор имеет следующие параметры:

-   `attribute` (str | null): Атрибут элемента, который нужно извлечь (например, `innerText`, `value`). Может быть `null`, если нужен сам элемент.
-   `by` (str | null): Метод поиска элемента (`XPATH`, `VALUE`, `CSS` и т.д.). Может быть `null`, если не требуется поиск.
-   `selector` (str | null): Строка селектора для поиска элемента. Может быть `null`, если не требуется поиск.
-   `if_list` (str): Указывает, что делать, если найдено несколько элементов (`first`, `all`).
-   `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом.
-   `mandatory` (bool): Указывает, является ли локатор обязательным.
-  `timeout` (int): Время ожидания в секундах.
-  `timeout_for_event` (str): Тип ожидания события (например, `presence_of_element_located`).
-  `event` (str | null): Событие, которое нужно выполнить. (например, `screenshot()`, `click()`, `wait(click(),2,after)`)
-   `locator_description` (str | null): Описание локатора.
-   `logic for attribue[AND|OR|XOR|VALUE|null]` (list | null): Логика обработки нескольких атрибутов, если есть.
-   `logic for action[AND|OR|XOR|VALUE|null]` (list | null): Логика выполнения нескольких действий, если есть.

## Локаторы

### `id`
    
**Описание**: Локатор для `id` продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `id_manufacturer`

**Описание**: Локатор для `id` производителя продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `id_supplier`

**Описание**: Локатор для `id` поставщика продукта.

**Параметры**:
- `attribute` (int):  `2778` - Атрибут равен 2778.
- `by` (str): `VALUE` - Использовать метод поиска по значению.
- `selector` (null): Селектор не задан.
- `if_list` (str): `first` - возвращается первый элемент из списка найденных.
- `use_mouse` (bool): `false` - не использовать мышь.
- `mandatory` (bool): `true` - локатор обязательный.
- `timeout` (int): `0` - таймаут не задан.
- `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
- `event` (null): Событие не задано.

### `id_category_default`

**Описание**: Локатор для `id` категории продукта по умолчанию.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `new`

**Описание**: Локатор для отметки нового продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `cache_default_attribute`

**Описание**: Локатор для кэшированного атрибута по умолчанию.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `id_default_image`

**Описание**: Локатор для `id` изображения продукта по умолчанию.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `id_default_combination`

**Описание**: Локатор для `id` комбинации продукта по умолчанию.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `id_tax`

**Описание**: Локатор для `id` налога на продукт.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `position_in_category`

**Описание**: Локатор для позиции продукта в категории.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `type`

**Описание**: Локатор для типа продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `id_shop_default`

**Описание**: Локатор для `id` магазина продукта по умолчанию.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `reference`

**Описание**: Локатор для артикула продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `supplier_reference`

**Описание**: Локатор для артикула поставщика продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `location`

**Описание**: Локатор для расположения продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `width`

**Описание**: Локатор для ширины продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `height`

**Описание**: Локатор для высоты продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `depth`

**Описание**: Локатор для глубины продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `weight`

**Описание**: Локатор для веса продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `quantity_discount`

**Описание**: Локатор для скидки за количество продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `ean13`

**Описание**: Локатор для штрих-кода EAN13.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `isbn`

**Описание**: Локатор для штрих-кода ISBN.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `upc`

**Описание**: Локатор для штрих-кода UPC.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `mpn`

**Описание**: Локатор для MPN продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `cache_is_pack`

**Описание**: Локатор для кэшированной отметки, что продукт является набором.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `cache_has_attachments`

**Описание**: Локатор для кэшированной отметки наличия вложений у продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `is_virtual`

**Описание**: Локатор для отметки, что продукт является виртуальным.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `state`

**Описание**: Локатор для состояния продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `additional_delivery_times`

**Описание**: Локатор для дополнительных сроков доставки.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `delivery_in_stock`

**Описание**: Локатор для срока доставки при наличии на складе.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `delivery_out_stock`

**Описание**: Локатор для срока доставки при отсутствии на складе.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `product_type`

**Описание**: Локатор для типа продукта.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `on_sale`

**Описание**: Локатор для отметки о том, что продукт продается со скидкой.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `online_only`

**Описание**: Локатор для отметки, что продукт продается только онлайн.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `ecotax`

**Описание**: Локатор для экологического налога.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `minimal_quantity`

**Описание**: Локатор для минимального количества продукта для заказа.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `low_stock_threshold`

**Описание**: Локатор для порога низкого уровня запасов.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.
 -  `timeout_for_event` (str): `presence_of_element_located` - ожидает появление элемента.
 -  `event` (null): Событие не задано.

### `low_stock_alert`

**Описание**: Локатор для оповещения о низком уровне запасов.

**Параметры**:
 -   `attribute` (null): Атрибут не задан.
 -   `by` (null): Метод поиска не задан.
 -   `selector` (null): Селектор не задан.
 -   `if_list` (str): `first` - возвращается первый элемент из списка найденных.
 -   `use_mouse` (bool): `false` - не использовать мышь.
 -   `mandatory` (bool): `true` - локатор обязательный.
 -   `timeout` (int): `0` - таймаут не задан.