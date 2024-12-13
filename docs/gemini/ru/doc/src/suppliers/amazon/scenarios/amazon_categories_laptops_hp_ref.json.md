# Документация для `amazon_categories_laptops_hp_ref.json`

## Обзор

Данный файл содержит JSON-конфигурацию для сценариев парсинга категорий ноутбуков HP с сайта Amazon. Каждый сценарий определяет условия для поиска ноутбуков определенной модели (например, HP с процессором Intel Celeron, i3, i5, i7 или AMD Ryzen) и размера экрана, а также связывает их с категориями в PrestaShop.

## Оглавление

1. [Сценарии](#Сценарии)
    - [LAPTOPS HP INTEL CELERON 11](#LAPTOPS-HP-INTEL-CELERON-11)
    - [LAPTOPS HP INTEL CELERON 13](#LAPTOPS-HP-INTEL-CELERON-13)
    - [LAPTOPS HP INTEL CELERON 14](#LAPTOPS-HP-INTEL-CELERON-14)
    - [LAPTOPS HP INTEL CELERON 15](#LAPTOPS-HP-INTEL-CELERON-15)
    - [LAPTOPS HP INTEL CELERON 17](#LAPTOPS-HP-INTEL-CELERON-17)
    - [LAPTOPS HP INTEL I3 11](#LAPTOPS-HP-INTEL-I3-11)
    - [LAPTOPS HP INTEL I3 13](#LAPTOPS-HP-INTEL-I3-13)
    - [LAPTOPS HP INTEL I3 14](#LAPTOPS-HP-INTEL-I3-14)
    - [LAPTOPS HP INTEL I3 15](#LAPTOPS-HP-INTEL-I3-15)
    - [LAPTOPS HP INTEL I3 17](#LAPTOPS-HP-INTEL-I3-17)
    - [LAPTOPS HP INTEL I5 11](#LAPTOPS-HP-INTEL-I5-11)
    - [LAPTOPS HP INTEL I5 13](#LAPTOPS-HP-INTEL-I5-13)
    - [LAPTOPS HP INTEL I5 14](#LAPTOPS-HP-INTEL-I5-14)
    - [LAPTOPS HP INTEL I5 15](#LAPTOPS-HP-INTEL-I5-15)
    - [LAPTOPS HP INTEL I5 17](#LAPTOPS-HP-INTEL-I5-17)
    - [LAPTOPS HP INTEL I7 11](#LAPTOPS-HP-INTEL-I7-11)
    - [LAPTOPS HP INTEL I7 13](#LAPTOPS-HP-INTEL-I7-13)
    - [LAPTOPS HP INTEL I7 14](#LAPTOPS-HP-INTEL-I7-14)
     - [LAPTOPS HP INTEL I7 15](#LAPTOPS-HP-INTEL-I7-15)
    - [LAPTOPS HP INTEL I7 17](#LAPTOPS-HP-INTEL-I7-17)
    - [LAPTOPS HP AMD RYZEN 3 14](#LAPTOPS-HP-AMD-RYZEN-3-14)
    - [LAPTOPS HP AMD RYZEN 3 17](#LAPTOPS-HP-AMD-RYZEN-3-17)
    - [LAPTOPS HP AMD RYZEN 5 13](#LAPTOPS-HP-AMD-RYZEN-5-13)
    - [LAPTOPS HP AMD RYZEN 5 14](#LAPTOPS-HP-AMD-RYZEN-5-14)
    - [LAPTOPS HP AMD RYZEN 5 15](#LAPTOPS-HP-AMD-RYZEN-5-15)
    - [LAPTOPS HP AMD RYZEN 5 17](#LAPTOPS-HP-AMD-RYZEN-5-17)
    - [LAPTOPS HP AMD RYZEN 7 13](#LAPTOPS-HP-AMD-RYZEN-7-13)
    - [LAPTOPS HP AMD RYZEN 7 14](#LAPTOPS-HP-AMD-RYZEN-7-14)
    - [LAPTOPS HP AMD RYZEN 7 15](#LAPTOPS-HP-AMD-RYZEN-7-15)
    - [LAPTOPS HP AMD RYZEN 7 17](#LAPTOPS-HP-AMD-RYZEN-7-17)
    - [LAPTOPS HP AMD ATHLON 14](#LAPTOPS-HP-AMD-ATHLON-14)
    - [LAPTOPS HP AMD ATHLON 15](#LAPTOPS-HP-AMD-ATHLON-15)
    - [LAPTOPS HP AMD ATHLON 17](#LAPTOPS-HP-AMD-ATHLON-17)

## Сценарии

### LAPTOPS HP INTEL CELERON 11

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel Celeron и диагональю экрана 11 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL CELERON", "11"]`.

### LAPTOPS HP INTEL CELERON 13

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel Celeron и диагональю экрана 13 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL CELERON", "13"]`.

### LAPTOPS HP INTEL CELERON 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel Celeron и диагональю экрана 14 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL CELERON", "14"]`.

### LAPTOPS HP INTEL CELERON 15

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel Celeron и диагональю экрана 15 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL CELERON", "15"]`.

### LAPTOPS HP INTEL CELERON 17

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel Celeron и диагональю экрана 17 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL CELERON", "17"]`.

### LAPTOPS HP INTEL I3 11

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i3 и диагональю экрана 11 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I3", "11"]`.

### LAPTOPS HP INTEL I3 13

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i3 и диагональю экрана 13 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I3", "13"]`.

### LAPTOPS HP INTEL I3 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i3 и диагональю экрана 14 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I3", "14"]`.

### LAPTOPS HP INTEL I3 15

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i3 и диагональю экрана 15 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I3", "15"]`.

### LAPTOPS HP INTEL I3 17

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i3 и диагональю экрана 17 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I3", "17"]`.
  
### LAPTOPS HP INTEL I5 11

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i5 и диагональю экрана 11 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I5", "11"]`.

### LAPTOPS HP INTEL I5 13

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i5 и диагональю экрана 13 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I5", "11"]`.

### LAPTOPS HP INTEL I5 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i5 и диагональю экрана 14 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I5", "14"]`.

### LAPTOPS HP INTEL I5 15

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i5 и диагональю экрана 15 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I5", "15"]`.

### LAPTOPS HP INTEL I5 17

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i5 и диагональю экрана 17 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I5", "17"]`.
  
### LAPTOPS HP INTEL I7 11

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i7 и диагональю экрана 11 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I7", "11"]`.

### LAPTOPS HP INTEL I7 13

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i7 и диагональю экрана 13 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I7", "13"]`.

### LAPTOPS HP INTEL I7 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i7 и диагональю экрана 14 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I7", "14"]`.
  
### LAPTOPS HP INTEL I7 15

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i7 и диагональю экрана 15 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I7", "15"]`.

### LAPTOPS HP INTEL I7 17

**Описание**: Сценарий для парсинга ноутбуков HP с процессором Intel i7 и диагональю экрана 17 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS INTEL I7", "17"]`.

### LAPTOPS HP AMD RYZEN 3 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 3 и диагональю экрана 14 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 3", "14"]`.

### LAPTOPS HP AMD RYZEN 3 17

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 3 и диагональю экрана 17 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 3", "17"]`.

### LAPTOPS HP AMD RYZEN 5 13

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 5 и диагональю экрана 13 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 5", "13"]`.

### LAPTOPS HP AMD RYZEN 5 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 5 и диагональю экрана 14 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 5", "14"]`.

### LAPTOPS HP AMD RYZEN 5 15

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 5 и диагональю экрана 15 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 5", "15"]`.

### LAPTOPS HP AMD RYZEN 5 17

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 5 и диагональю экрана 17 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 5", "17"]`.

### LAPTOPS HP AMD RYZEN 7 13

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 7 и диагональю экрана 13 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 7", "13"]`.

### LAPTOPS HP AMD RYZEN 7 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 7 и диагональю экрана 14 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 7", "14"]`.

### LAPTOPS HP AMD RYZEN 7 15

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 7 и диагональю экрана 15 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 7", "15"]`.

### LAPTOPS HP AMD RYZEN 7 17

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Ryzen 7 и диагональю экрана 17 дюймов.

**Параметры**:
- `brand` (str): Бренд ноутбука (`HP`).
- `url` (str): URL для поиска ноутбуков на Amazon.
- `active` (bool): Флаг, указывающий, активен ли сценарий.
- `condition` (str): Состояние товара (`new`).
- `presta_categories` (dict): Категории PrestaShop, куда будут отнесены товары.
- `checkbox` (bool): Флаг для использования в интерфейсе (здесь всегда `false`).
- `price_rule` (int): Правило ценообразования.

**Presta Categories**
- `template`:
  - `hp`: Список категорий PrestaShop, к которым будет привязан товар: `["LAPTOPS AMD RYZEN 7", "17"]`.

### LAPTOPS HP AMD ATHLON 14

**Описание**: Сценарий для парсинга ноутбуков HP с процессором AMD Athlon и диагональю экрана 14 дюймов.

**Парамет