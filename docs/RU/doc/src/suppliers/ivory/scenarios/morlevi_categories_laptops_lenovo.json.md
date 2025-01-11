# Документация для `morlevi_categories_laptops_lenovo.json`

## Обзор

Файл `morlevi_categories_laptops_lenovo.json` содержит конфигурацию сценариев для определения категорий ноутбуков Lenovo на основе их характеристик, таких как размер экрана и процессор. Каждый сценарий определяет соответствие между моделью ноутбука и категориями в PrestaShop, а также включает URL для поиска товаров на сайте Morlevi.

## Оглавление

1.  [Сценарии](#сценарии)
    -   [LENOVO 11.6 I3](#lenovo-116-i3)
    -   [LENOVO 11.6 I5](#lenovo-116-i5)
    -   [LENOVO 11.6 I7](#lenovo-116-i7)
    -   [LENOVO 11.6 I9](#lenovo-116-i9)
    -   [LENOVO 11.6 AMD](#lenovo-116-amd)
    -   [LENOVO 11.6 Celeron](#lenovo-116-celeron)
    -   [LENOVO 11.6 Pentium](#lenovo-116-pentium)
    -  [LENOVO 13.4 - 13.3 I3](#lenovo-134---133-i3)
    -   [LENOVO 13.4 - 13.3 I5](#lenovo-134---133-i5)
    -   [LENOVO 13.4 - 13.3 I7](#lenovo-134---133-i7)
    -   [LENOVO 13.4 - 13.3 I9](#lenovo-134---133-i9)
    -  [LENOVO 13.4 - 13.3 AMD](#lenovo-134---133-amd)
    -   [LENOVO 13.4 - 13.3 Celeron](#lenovo-134---133-celeron)
    -   [LENOVO 13.4 - 13.3 Pentium](#lenovo-134---133-pentium)
    -   [LENOVO 14 I3](#lenovo-14-i3)
    -   [LENOVO 14 I5](#lenovo-14-i5)
    -  [LENOVO 14 I7](#lenovo-14-i7)
    -   [LENOVO 14 I9](#lenovo-14-i9)
    -   [LENOVO 14 AMD RYZEN 7](#lenovo-14-amd-ryzen-7)
    -  [LENOVO 14 Celeron](#lenovo-14-celeron)
    -   [LENOVO 14 Pentium](#lenovo-14-pentium)
    -   [LENOVO 15 I3](#lenovo-15-i3)
    -   [LENOVO 15 I5](#lenovo-15-i5)
    -   [LENOVO 15 I7](#lenovo-15-i7)
    -   [LENOVO 15 I9](#lenovo-15-i9)
    -  [LENOVO 15 AMD RYZEN 5](#lenovo-15-amd-ryzen-5)
    -   [LENOVO 15 AMD RYZEN 7](#lenovo-15-amd-ryzen-7)
    -  [LENOVO 15 Celeron](#lenovo-15-celeron)
    -   [LENOVO 15 Pentium](#lenovo-15-pentium)
    -   [LENOVO 17.3 I3](#lenovo-173-i3)
    -   [LENOVO 17.3 I5](#lenovo-173-i5)
    -  [LENOVO 17.3 I7](#lenovo-173-i7)
    -   [LENOVO 17.3 I9](#lenovo-173-i9)
    -   [LENOVO 17.3 AMD](#lenovo-173-amd)
    -   [LENOVO 17.3 Celeron](#lenovo-173-celeron)
    -  [LENOVO 17.3 Pentium](#lenovo-173-pentium)

## Сценарии

### LENOVO 11.6 I3
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 11.6 дюймов и процессором Intel Core i3.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I3", "11" ]

### LENOVO 11.6 I5
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 11.6 дюймов и процессором Intel Core i5.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I5", "11" ]

### LENOVO 11.6 I7
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 11.6 дюймов и процессором Intel Core i7.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I7", "11" ]

### LENOVO 11.6 I9
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 11.6 дюймов и процессором Intel Core i9.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I9", "11" ]

### LENOVO 11.6 AMD
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 11.6 дюймов и процессором AMD.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS AMD", "11" ]

### LENOVO 11.6 Celeron
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 11.6 дюймов и процессором Intel Celeron.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "11" ]

### LENOVO 11.6 Pentium
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 11.6 дюймов и процессором Intel Pentium.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "11" ]
### LENOVO 13.4 - 13.3 I3
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i3.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I3", "13" ]

### LENOVO 13.4 - 13.3 I5
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i5.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I5", "13" ]

### LENOVO 13.4 - 13.3 I7
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i7.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I7", "13" ]
### LENOVO 13.4 - 13.3 I9
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i9.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I9", "13" ]
### LENOVO 13.4 - 13.3 AMD
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана от 13.3 до 13.4 дюймов и процессором AMD.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS AMD", "13" ]

### LENOVO 13.4 - 13.3 Celeron
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Celeron.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "13" ]

### LENOVO 13.4 - 13.3 Pentium
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Pentium.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "13" ]
### LENOVO 14 I3
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 14 дюймов и процессором Intel Core i3.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I3", "14" ]

### LENOVO 14 I5
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 14 дюймов и процессором Intel Core i5.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I5", "14" ]

### LENOVO 14 I7
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 14 дюймов и процессором Intel Core i7.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I7", "14" ]

### LENOVO 14 I9
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 14 дюймов и процессором Intel Core i9.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I9", "14" ]

### LENOVO 14 AMD RYZEN 7
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 14 дюймов и процессором AMD Ryzen 7.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I7", "14" ]

### LENOVO 14 Celeron
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 14 дюймов и процессором Intel Celeron.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "14" ]
### LENOVO 14 Pentium
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 14 дюймов и процессором Intel Pentium.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "14" ]
### LENOVO 15 I3
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором Intel Core i3.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I3", "15" ]

### LENOVO 15 I5
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором Intel Core i5.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I5", "15" ]
### LENOVO 15 I7
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором Intel Core i7.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I7", "15" ]
### LENOVO 15 I9
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором Intel Core i9.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I9", "15" ]
### LENOVO 15 AMD RYZEN 5
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором AMD Ryzen 5.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `gigabyte`: [ "LAPTOPS AMD RYZEN 5", "15" ]
### LENOVO 15 AMD RYZEN 7
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором AMD Ryzen 7.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS AMD RYZEN 7", "15" ]
### LENOVO 15 Celeron
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором Intel Celeron.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "15" ]
### LENOVO 15 Pentium
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 15 дюймов и процессором Intel Pentium.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "15" ]

### LENOVO 17.3 I3
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 17.3 дюймов и процессором Intel Core i3.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I3", "17" ]

### LENOVO 17.3 I5
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 17.3 дюймов и процессором Intel Core i5.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I5", "17" ]

### LENOVO 17.3 I7
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 17.3 дюймов и процессором Intel Core i7.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-   `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I7", "17" ]

### LENOVO 17.3 I9
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 17.3 дюймов и процессором Intel Core i9.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL I9", "17" ]

### LENOVO 17.3 AMD
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 17.3 дюймов и процессором AMD.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров. По умолчанию `null`.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS AMD", "17" ]

### LENOVO 17.3 Celeron
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 17.3 дюймов и процессором Intel Celeron.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "17" ]
### LENOVO 17.3 Pentium
**Описание**: Сценарий для ноутбуков Lenovo с диагональю экрана 17.3 дюймов и процессором Intel Pentium.

**Параметры**:
-   `brand` (str): Бренд ноутбука.
-    `url` (str, optional): URL для поиска товаров.
-   `checkbox` (bool): Флаг для использования в интерфейсе.
-   `active` (bool): Флаг активности сценария.
-   `condition` (str): Состояние товара ("new").
-   `presta_categories` (dict): Категории для PrestaShop.

**PrestaShop Категории**:
-   `template`:
    -   `LENOVO`: [ "LAPTOPS INTEL CELERON", "17" ]