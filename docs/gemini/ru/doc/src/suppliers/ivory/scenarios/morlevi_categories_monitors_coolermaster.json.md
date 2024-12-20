# Документация для `morlevi_categories_monitors_coolermaster.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [COOLER MASTER 22](#cooler-master-22)
    - [COOLER MASTER 24-25](#cooler-master-24-25)
    - [COOLER MASTER 27-29](#cooler-master-27-29)
    - [COOLER MASTER 32](#cooler-master-32)
    - [COOLER MASTER 34](#cooler-master-34)
    - [COOLER MASTER 49](#cooler-master-49)

## Обзор

Этот файл содержит конфигурационные данные в формате JSON для определения сценариев парсинга категорий мониторов бренда COOLER MASTER с сайта morlevi.co.il. Он определяет различные сценарии на основе размера экрана монитора (22", 24-25", 27-29", 32", 34" и 49"), а также соответствующие параметры для каждого сценария.

## Структура файла

Файл представляет собой JSON-объект со следующим ключом:

- `scenarios` (object): Объект, содержащий вложенные объекты, каждый из которых описывает отдельный сценарий парсинга. Ключи этих вложенных объектов представляют собой название сценария, а значения - параметры для данного сценария.

## Сценарии

### `COOLER MASTER 22`

**Описание**: Сценарий для парсинга мониторов COOLER MASTER с диагональю 22".

**Параметры**:
- `brand` (str):  Бренд монитора, "COOLER MASTER".
- `url` (str):  URL-адрес для парсинга (в данном случае, указана пунктирная строка).
- `checkbox` (bool): Флаг для выбора (значение: false).
- `active` (bool): Флаг, указывающий на активность сценария (значение: true).
- `condition` (str):  Состояние товара (значение: "new").
- `presta_categories` (str):  Категории PrestaShop, к которым относится товар (значение: "127,128,981").

### `COOLER MASTER 24-25`

**Описание**: Сценарий для парсинга мониторов COOLER MASTER с диагональю 24-25".

**Параметры**:
- `brand` (str): Бренд монитора, "COOLER MASTER".
- `url` (str):  URL-адрес для парсинга с параметрами фильтрации.
- `checkbox` (bool): Флаг для выбора (значение: false).
- `active` (bool): Флаг, указывающий на активность сценария (значение: true).
- `condition` (str): Состояние товара (значение: "new").
- `presta_categories` (str):  Категории PrestaShop, к которым относится товар (значение: "127,129,981").

### `COOLER MASTER 27-29`

**Описание**: Сценарий для парсинга мониторов COOLER MASTER с диагональю 27-29".

**Параметры**:
- `brand` (str):  Бренд монитора, "COOLER MASTER".
- `url` (str):  URL-адрес для парсинга с параметрами фильтрации.
- `checkbox` (bool): Флаг для выбора (значение: false).
- `active` (bool): Флаг, указывающий на активность сценария (значение: true).
- `condition` (str): Состояние товара (значение: "new").
- `presta_categories` (str):  Категории PrestaShop, к которым относится товар (значение: "127,130,981").

### `COOLER MASTER 32`

**Описание**: Сценарий для парсинга мониторов COOLER MASTER с диагональю 32".

**Параметры**:
- `brand` (str):  Бренд монитора, "COOLER MASTER".
- `url` (str):  URL-адрес для парсинга с параметрами фильтрации.
- `checkbox` (bool): Флаг для выбора (значение: false).
- `active` (bool): Флаг, указывающий на активность сценария (значение: true).
- `condition` (str): Состояние товара (значение: "new").
- `presta_categories` (str):  Категории PrestaShop, к которым относится товар (значение: "127,131,981").

### `COOLER MASTER 34`

**Описание**: Сценарий для парсинга мониторов COOLER MASTER с диагональю 34".

**Параметры**:
- `brand` (str):  Бренд монитора, "COOLER MASTER".
- `url` (str):  URL-адрес для парсинга с параметрами фильтрации.
- `checkbox` (bool): Флаг для выбора (значение: false).
- `active` (bool): Флаг, указывающий на активность сценария (значение: true).
- `condition` (str): Состояние товара (значение: "new").
- `presta_categories` (str):  Категории PrestaShop, к которым относится товар (значение: "127,132,981").

### `COOLER MASTER 49`

**Описание**: Сценарий для парсинга мониторов COOLER MASTER с диагональю 49".

**Параметры**:
- `brand` (str): Бренд монитора, "COOLER MASTER".
- `url` (str):  URL-адрес для парсинга (в данном случае, указана пунктирная строка).
- `checkbox` (bool): Флаг для выбора (значение: false).
- `active` (bool): Флаг, указывающий на активность сценария (значение: true).
- `condition` (str): Состояние товара (значение: "new").
- `presta_categories` (str):  Категории PrestaShop, к которым относится товар (значение: "127,133,981").