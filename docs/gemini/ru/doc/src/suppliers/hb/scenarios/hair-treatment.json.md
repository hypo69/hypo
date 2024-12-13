# Документация для `hypotez/src/suppliers/hb/scenarios/hair-treatment.json`

## Обзор

Файл `hair-treatment.json` содержит конфигурационные данные для сценариев обработки товаров из категории "Уход за волосами" для поставщика HB. Он определяет URL-адреса, названия, условия и категории PrestaShop для различных подкатегорий товаров, таких как "Дополнительные продукты", "Шампуни и кондиционеры", "Серия кератина" и "Маски для волос".

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [`scenarios`](#scenarios)
    - [`complementary-products`](#complementary-products)
    - [`hair-treatment`](#hair-treatment)
    - [`shampoo-conditioner`](#shampoo-conditioner)
    - [`cratin-series`](#cratin-series)
    - [`hair-masks`](#hair-masks)

## Структура JSON

### `scenarios`

Этот раздел содержит словарь, ключами которого являются названия сценариев обработки категорий товаров по уходу за волосами. Каждый сценарий является объектом со следующими ключами:

- `url` (str): URL-адрес категории на сайте поставщика.
- `name` (str): Название категории на иврите.
- `condition` (str | list): Условие для отбора товаров, например, `new`. Может быть строкой или списком строк.
- `presta_categories` (dict): Объект, определяющий соответствие между категориями поставщика и категориями PrestaShop. Содержит:
    - `default_category` (dict): Словарь, где ключ - идентификатор категории PrestaShop (обычно 11111), а значение - название категории PrestaShop (строка или число).
    - `additional_categories` (list): Список дополнительных категорий PrestaShop (может быть пустым).

### `complementary-products`

#### **Описание**:
Сценарий для обработки дополнительных товаров по уходу за волосами.

- **`url`**: `https://hbdeadsea.co.il/product-category/hair-treatment/complementary-products/`
- **`name`**: `מוצרי טיפוח משלימים`
- **`condition`**: `new`
- **`presta_categories`**:
    - **`default_category`**: `{"11111": "presta_category"}`
    - **`additional_categories`**: `[""]`

### `hair-treatment`

#### **Описание**:
Сценарий для обработки общей категории товаров по уходу за волосами.

- **`url`**: `https://hbdeadsea.co.il/product-category/hair-treatment/`
- **`name`**: `טיפוח השיער`
- **`condition`**: `["new"]`
- **`presta_categories`**:
    - **`default_category`**: `{"11111": "presta_category"}`
    - **`additional_categories`**: `[""]`

### `shampoo-conditioner`

#### **Описание**:
Сценарий для обработки шампуней и кондиционеров.

- **`url`**: `https://hbdeadsea.co.il/product-category/hair-treatment/shampoo-conditioner/`
- **`name`**: `שמפו ומרכך`
- **`condition`**: `new`
- **`presta_categories`**:
    - **`default_category`**: `{"11111": "presta_category"}`
    - **`additional_categories`**: `[""]`

### `cratin-series`

#### **Описание**:
Сценарий для обработки серии товаров с кератином.

- **`url`**: `https://hbdeadsea.co.il/product-category/hair-treatment/cratin-series/`
- **`name`**: `סדרת קרטין`
- **`condition`**: `new`
- **`presta_categories`**:
    - **`default_category`**: `11111`
    - **`additional_categories`**: `[""]`

### `hair-masks`

#### **Описание**:
Сценарий для обработки масок для волос.

- **`url`**: `https://hbdeadsea.co.il/product-category/hair-treatment/hair-masks/`
- **`name`**: `מסכות לשיער`
- **`condition`**: `new`
- **`presta_categories`**:
    - **`default_category`**: `11111`
    - **`additional_categories`**: `[""]`