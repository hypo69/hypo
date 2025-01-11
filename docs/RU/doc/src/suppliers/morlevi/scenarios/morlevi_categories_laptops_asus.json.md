# Документация для `morlevi_categories_laptops_asus.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Описание разделов](#описание-разделов)
    - [Asus laptops](#asus-laptops)
    - [scenarios](#scenarios)
        - [ASUS 11.6 I3](#asus-116-i3)
        - [ASUS 11.6 I5](#asus-116-i5)
        - [ASUS 11.6 I7](#asus-116-i7)
        - [ASUS 11.6 I9](#asus-116-i9)
        - [ASUS 11.6 AMD](#asus-116-amd)
        - [ASUS 11.6 Celeron](#asus-116-celeron)
        - [ASUS 11.6 Pentium](#asus-116-pentium)
        - [ASUS 13.4 - 13.3 I3](#asus-134---133-i3)
        - [ASUS 13.4 - 13.3 I5](#asus-134---133-i5)
        - [ASUS 13.4 - 13.3 I7](#asus-134---133-i7)
        - [ASUS 13.4 - 13.3 I9](#asus-134---133-i9)
        - [ASUS 13.4 - 13.3 AMD](#asus-134---133-amd)
        - [ASUS 13.4 - 13.3 Celeron](#asus-134---133-celeron)
        - [ASUS 13.4 - 13.3 Pentium](#asus-134---133-pentium)
        - [ASUS 14 I3](#asus-14-i3)
        - [ASUS 14 I5](#asus-14-i5)
        - [ASUS 14 I7](#asus-14-i7)
        - [ASUS 14 I9](#asus-14-i9)
        - [ASUS 14 AMD RYZEN 7](#asus-14-amd-ryzen-7)
         - [ASUS 14 Celeron](#asus-14-celeron)
        - [ASUS 14 Pentium](#asus-14-pentium)
        - [ASUS 15 I3](#asus-15-i3)
        - [ASUS 15 I5](#asus-15-i5)
        - [ASUS 15 I7](#asus-15-i7)
        - [ASUS 15 I9](#asus-15-i9)
        - [ASUS 15 AMD RYZEN 7](#asus-15-amd-ryzen-7)
        - [ASUS 15 Celeron](#asus-15-celeron)
        - [ASUS 15 Pentium](#asus-15-pentium)
        - [ASUS 17.3 I3](#asus-173-i3)
        - [ASUS 17.3 I5](#asus-173-i5)
        - [ASUS 17.3 I7](#asus-173-i7)
        - [ASUS 17.3 I9](#asus-173-i9)
        - [ASUS 17.3 AMD](#asus-173-amd)
        - [ASUS 17.3 Celeron](#asus-173-celeron)
        - [ASUS 17.3 Pentium](#asus-173-pentium)

## Обзор

Файл `morlevi_categories_laptops_asus.json` содержит конфигурацию для определения категорий ноутбуков ASUS на сайте Morlevi. Он включает в себя URL для получения данных и сценарии для сопоставления моделей ноутбуков с категориями PrestaShop.

## Структура файла
Файл имеет следующую структуру:

- **`Asus laptops`**: Содержит URL для получения списка ноутбуков ASUS.
- **`scenarios`**: Содержит набор сценариев для разных моделей ноутбуков ASUS, каждый из которых имеет следующую структуру:
  - **`brand`**: Бренд ноутбука (всегда "ASUS" в данном файле).
  - **`url`**: URL для фильтрации товаров на сайте. Может быть `null`.
  - **`checkbox`**: Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false` в данном файле.
  - **`active`**: Флаг, который указывает, активен ли сценарий. Всегда `true` в данном файле.
  - **`condition`**: Условие товара (всегда "new" в данном файле).
  - **`presta_categories`**: Сопоставление с категориями PrestaShop.
    - **`template`**: Шаблон категорий.
      - **`asus`**: Массив категорий PrestaShop, где первый элемент — это основная категория, а второй — размер экрана.

## Описание разделов

### `Asus laptops`
Содержит общую информацию о ноутбуках ASUS, включая URL для получения данных.

**Поля:**
*   `url` (str): URL для получения списка ноутбуков ASUS.

### `scenarios`
Содержит набор сценариев для разных моделей ноутбуков ASUS.

#### `ASUS 11.6 I3`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i3 и экраном 11.6 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I3", "11"]`

#### `ASUS 11.6 I5`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i5 и экраном 11.6 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I5", "11"]`

#### `ASUS 11.6 I7`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i7 и экраном 11.6 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I7", "11"]`

#### `ASUS 11.6 I9`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i9 и экраном 11.6 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I9", "11"]`

#### `ASUS 11.6 AMD`
**Описание**: Сценарий для ноутбуков ASUS с процессором AMD и экраном 11.6 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS AMD", "11"]`

#### `ASUS 11.6 Celeron`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Celeron и экраном 11.6 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "11"]`

#### `ASUS 11.6 Pentium`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Pentium и экраном 11.6 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "11"]`

#### `ASUS 13.4 - 13.3 I3`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i3 и экраном от 13.3 до 13.4 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I3", "13"]`

#### `ASUS 13.4 - 13.3 I5`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i5 и экраном от 13.3 до 13.4 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I5", "13"]`

#### `ASUS 13.4 - 13.3 I7`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i7 и экраном от 13.3 до 13.4 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I7", "13"]`

#### `ASUS 13.4 - 13.3 I9`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i9 и экраном от 13.3 до 13.4 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I9", "13"]`

#### `ASUS 13.4 - 13.3 AMD`
**Описание**: Сценарий для ноутбуков ASUS с процессором AMD и экраном от 13.3 до 13.4 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS AMD", "13"]`

#### `ASUS 13.4 - 13.3 Celeron`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Celeron и экраном от 13.3 до 13.4 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "13"]`

#### `ASUS 13.4 - 13.3 Pentium`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Pentium и экраном от 13.3 до 13.4 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "13"]`

#### `ASUS 14 I3`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i3 и экраном 14 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I3", "14"]`

#### `ASUS 14 I5`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i5 и экраном 14 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I5", "14"]`

#### `ASUS 14 I7`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i7 и экраном 14 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I7", "14"]`

#### `ASUS 14 I9`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i9 и экраном 14 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I9", "14"]`
#### `ASUS 14 AMD RYZEN 7`
**Описание**: Сценарий для ноутбуков ASUS с процессором AMD Ryzen 7 и экраном 14 дюймов.

**Поля:**
*   `brand` (str): Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    * `template` (dict): Шаблон категорий.
        * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I7", "14"]`

#### `ASUS 14 Celeron`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Celeron и экраном 14 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "14"]`
#### `ASUS 14 Pentium`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Pentium и экраном 14 дюймов.

**Поля:**
*   `brand` (str): Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    * `template` (dict): Шаблон категорий.
        * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "14"]`

#### `ASUS 15 I3`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i3 и экраном 15 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I3", "15"]`

#### `ASUS 15 I5`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i5 и экраном 15 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I5", "15"]`

#### `ASUS 15 I7`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i7 и экраном 15 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I7", "15"]`

#### `ASUS 15 I9`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i9 и экраном 15 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I9", "15"]`

#### `ASUS 15 AMD RYZEN 7`
**Описание**: Сценарий для ноутбуков ASUS с процессором AMD Ryzen 7 и экраном 15 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str): URL для фильтрации товаров на сайте.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS AMD RYZEN 7", "15"]`

#### `ASUS 15 Celeron`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Celeron и экраном 15 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "15"]`

#### `ASUS 15 Pentium`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Pentium и экраном 15 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL CELERON", "15"]`

#### `ASUS 17.3 I3`
**Описание**: Сценарий для ноутбуков ASUS с процессором Intel Core i3 и экраном 17.3 дюймов.

**Поля:**
*   `brand` (str):  Бренд ноутбука (всегда "ASUS").
*   `url` (str | null): URL для фильтрации товаров на сайте. Может быть `null`.
*   `checkbox` (bool): Флаг, который указывает, нужно ли использовать чекбокс. Всегда `false`.
*   `active` (bool): Флаг, который указывает, активен ли сценарий. Всегда `true`.
*   `condition` (str): Условие товара (всегда "new").
*   `presta_categories` (dict): Сопоставление с категориями PrestaShop.
    *  `template` (dict): Шаблон категорий.
       * `asus` (list): Массив категорий PrestaShop: `["LAPTOPS INTEL I3", "17"]`