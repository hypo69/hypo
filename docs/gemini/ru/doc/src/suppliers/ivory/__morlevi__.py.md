# Модуль `__morlevi__`

## Обзор

Модуль `__morlevi__.py` предназначен для автоматизации сбора данных о товарах с сайта поставщика "Morlevi". Он включает в себя функции для входа на сайт, сбора информации о товарах, включая их описание, цену, изображения и другие характеристики, а также для навигации по страницам категорий. Модуль использует библиотеки `requests`, `pandas` и `selenium` для взаимодействия с веб-сайтом.

## Содержание

1.  [Функции](#Функции)
    *   [`login`](#login)
    *   [`_login`](#_login)
    *   [`grab_product_page`](#grab_product_page)
    *   [`list_products_in_category_from_pagination`](#list_products_in_category_from_pagination)
    *   [`get_list_products_in_category`](#get_list_products_in_category)
    *    [`get_list_categories_from_site`](#get_list_categories_from_site)

## Функции

### `login`

**Описание**:
Функция выполняет вход на сайт поставщика. Она пытается сначала войти на сайт, а затем, в случае неудачи, пытается закрыть модальные окна и повторить вход.

**Параметры**:
- `supplier`: Объект поставщика, содержащий данные для входа и локаторы элементов.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешного входа, иначе `None`.

**Вызывает исключения**:
- `Exception`: В случае ошибки при попытке закрыть модальные окна или при логине.

### `_login`

**Описание**:
Вспомогательная функция, непосредственно выполняющая вход на сайт с использованием предоставленных локаторов.

**Параметры**:
- `_s`: Объект поставщика, содержащий локаторы и драйвер браузера.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешного входа, иначе `None`.

**Вызывает исключения**:
- `Exception`: В случае ошибки при попытке входа.

### `grab_product_page`

**Описание**:
Функция для сбора данных о товаре с текущей страницы. Она извлекает информацию, такую как идентификатор, артикул, заголовок, описание, цену, изображения и другие характеристики, и возвращает объект `Product` с собранными данными.

**Параметры**:
- `s`: Объект поставщика.

**Возвращает**:
- `Product`: Объект `Product` с информацией о товаре или None, если цена не найдена.

### `list_products_in_category_from_pagination`

**Описание**:
Функция собирает список ссылок на товары из текущей категории, переходя по страницам пагинации. Она находит все ссылки на товары и возвращает их в виде списка.

**Параметры**:
- `supplier`: Объект поставщика, содержащий драйвер браузера и локаторы.

**Возвращает**:
- `list`: Список ссылок на товары в текущей категории. Возвращает пустой список если нет товаров.

### `get_list_products_in_category`

**Описание**:
Функция вызывает `list_products_in_category_from_pagination`  и возвращает список товаров.
**Параметры**:
- `s`:Объект `Supplier`
- `scenario`:JSON
- `presath`:PrestaShopWebServiceDict

**Возвращает**:
- `None`:

### `get_list_categories_from_site`
**Описание**:
Функция  предназначена для сбора списка категорий с сайта поставщика.
**Параметры**:
- `s`:Объект `Supplier`
- `scenario_file`:JSON
- `brand`:str

**Возвращает**:
- `None`: