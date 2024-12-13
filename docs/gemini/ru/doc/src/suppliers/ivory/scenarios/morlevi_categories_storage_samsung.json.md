# Документация для `morlevi_categories_storage_samsung.json`

## Обзор

Файл `morlevi_categories_storage_samsung.json` содержит конфигурацию для сбора данных о категориях товаров Samsung из магазина Morlevi. Он определяет URL-адреса, параметры фильтрации и категории PrestaShop для различных SSD-накопителей Samsung.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [Сценарии](#сценарии)
    - [`SAMSUNG NVME GEN4 512GB`](#samsung-nvme-gen4-512gb)
    - [`SAMSUNG NVME GEN4 1TB`](#samsung-nvme-gen4-1tb)
    - [`SAMSUNG NVME GEN4 2TB`](#samsung-nvme-gen4-2tb)
    - [`SAMSUNG SATA 3 256GB`](#samsung-sata-3-256gb)
    - [`SAMSUNG SATA 3 512GB`](#samsung-sata-3-512gb)
    - [`SAMSUNG SATA 3 1TB`](#samsung-sata-3-1tb)
    - [`SAMSUNG SATA 3 2TB`](#samsung-sata-3-2tb)
    - [`SAMSUNG SATA 3 4TB`](#samsung-sata-3-4tb)
    - [`SAMSUNG SSD NVME PCIE 256GB`](#samsung-ssd-nvme-pcie-256gb)
    - [`SAMSUNG SSD NVME PCIE 512GB`](#samsung-ssd-nvme-pcie-512gb)
    - [`SAMSUNG SSD NVME PCIE 1TB`](#samsung-ssd-nvme-pcie-1tb)
    - [`SAMSUNG SSD NVME PCIE 2TB`](#samsung-ssd-nvme-pcie-2tb)

## Структура файла

Файл представляет собой JSON-объект, содержащий один ключ `scenarios`, значением которого является словарь. Каждый ключ в этом словаре представляет собой конкретный сценарий для определенного товара Samsung.

## Сценарии

### `SAMSUNG NVME GEN4 512GB`

**Описание**: Сценарий для SSD SAMSUNG NVME GEN4 объемом 512GB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/314?p_315=28&p_175=826&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`: 
        - `samsung`: `SSD NVME GEN4 512GB` - Соответствующая категория в PrestaShop.

### `SAMSUNG NVME GEN4 1TB`

**Описание**: Сценарий для SSD SAMSUNG NVME GEN4 объемом 1TB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/314?p_315=28&p_175=829&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SSD NVME GEN4 1TB` - Соответствующая категория в PrestaShop.

### `SAMSUNG NVME GEN4 2TB`

**Описание**: Сценарий для SSD SAMSUNG NVME GEN4 объемом 2TB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/314?p_315=28&p_175=831&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SSD NVME GEN4 2TB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SATA 3 256GB`

**Описание**: Сценарий для SSD SAMSUNG SATA 3 объемом 256GB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/50?p_315=28&p_175=823&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SATA 3 256GB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SATA 3 512GB`

**Описание**: Сценарий для SSD SAMSUNG SATA 3 объемом 512GB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/50?p_315=28&p_175=826&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SATA 3 521GB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SATA 3 1TB`

**Описание**: Сценарий для SSD SAMSUNG SATA 3 объемом 1TB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/50?p_315=28&p_175=829&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SATA 3 1TB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SATA 3 2TB`

**Описание**: Сценарий для SSD SAMSUNG SATA 3 объемом 2TB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/50?p_315=28&p_175=831&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SATA 3 2TB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SATA 3 4TB`

**Описание**: Сценарий для SSD SAMSUNG SATA 3 объемом 4TB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/50?p_315=28&p_175=3576&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SATA 3 4TB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SSD NVME PCIE 256GB`

**Описание**: Сценарий для SSD SAMSUNG NVME PCIE объемом 256GB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/50?p_315=28&p_175=3576&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SSD NVME PCIE 256GB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SSD NVME PCIE 512GB`

**Описание**: Сценарий для SSD SAMSUNG NVME PCIE объемом 512GB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/51?p_315=28&p_175=826&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SSD NVME PCIE 512GB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SSD NVME PCIE 1TB`

**Описание**: Сценарий для SSD SAMSUNG NVME PCIE объемом 1TB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/51?p_315=28&p_175=829&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SSD NVME PCIE 1TB` - Соответствующая категория в PrestaShop.

### `SAMSUNG SSD NVME PCIE 2TB`

**Описание**: Сценарий для SSD SAMSUNG NVME PCIE объемом 2TB.

**Поля**:
- `brand`: `SAMSUNG` - Бренд товара.
- `url`: `https://www.morlevi.co.il/Cat/51?p_315=28&p_175=831&sort=datafloat2%2Cprice&keyword=` - URL для сбора данных.
- `checkbox`: `false` - Флаг для чекбокса (не используется).
- `active`: `true` - Флаг активности сценария.
- `condition`: `new` - Состояние товара.
- `presta_categories`:
    - `template`:
        - `samsung`: `SSD NVME PCIE 2TB` - Соответствующая категория в PrestaShop.