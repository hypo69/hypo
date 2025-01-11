# Документация для `morlevi_categories_laptops_asus.json`

## Обзор

Этот JSON-файл содержит конфигурацию для сценариев с категориями ноутбуков ASUS, предназначенных для веб-сайта Morlevi. Он определяет URL-адреса для фильтрации товаров, а также категории PrestaShop, к которым они относятся, на основе процессора и размера экрана.

## Оглавление

1. [Структура файла](#структура-файла)
2. [Раздел `Asus laptops`](#раздел-asus-laptops)
3. [Раздел `scenarios`](#раздел-scenarios)
   - [Сценарий `ASUS 11.6 I3`](#сценарий-asus-116-i3)
   - [Сценарий `ASUS 11.6 I5`](#сценарий-asus-116-i5)
   - [Сценарий `ASUS 11.6 I7`](#сценарий-asus-116-i7)
   - [Сценарий `ASUS 11.6 I9`](#сценарий-asus-116-i9)
   - [Сценарий `ASUS 11.6 AMD`](#сценарий-asus-116-amd)
   - [Сценарий `ASUS 11.6 Celeron`](#сценарий-asus-116-celeron)
   - [Сценарий `ASUS 11.6 Pentium`](#сценарий-asus-116-pentium)
   - [Сценарий `ASUS 13.4 - 13.3 I3`](#сценарий-asus-134---133-i3)
   - [Сценарий `ASUS 13.4 - 13.3 I5`](#сценарий-asus-134---133-i5)
   - [Сценарий `ASUS 13.4 - 13.3 I7`](#сценарий-asus-134---133-i7)
   - [Сценарий `ASUS 13.4 - 13.3 I9`](#сценарий-asus-134---133-i9)
   - [Сценарий `ASUS 13.4 - 13.3 AMD`](#сценарий-asus-134---133-amd)
   - [Сценарий `ASUS 13.4 - 13.3 Celeron`](#сценарий-asus-134---133-celeron)
   - [Сценарий `ASUS 13.4 - 13.3 Pentium`](#сценарий-asus-134---133-pentium)
   - [Сценарий `ASUS 14 I3`](#сценарий-asus-14-i3)
   - [Сценарий `ASUS 14 I5`](#сценарий-asus-14-i5)
   - [Сценарий `ASUS 14 I7`](#сценарий-asus-14-i7)
    - [Сценарий `ASUS 14 I9`](#сценарий-asus-14-i9)
   -  [Сценарий `ASUS 14 AMD RYZEN 7`](#сценарий-asus-14-amd-ryzen-7)
   - [Сценарий `ASUS 14 Celeron`](#сценарий-asus-14-celeron)
   - [Сценарий `ASUS 14 Pentium`](#сценарий-asus-14-pentium)
   - [Сценарий `ASUS 15 I3`](#сценарий-asus-15-i3)
   - [Сценарий `ASUS 15 I5`](#сценарий-asus-15-i5)
   - [Сценарий `ASUS 15 I7`](#сценарий-asus-15-i7)
    - [Сценарий `ASUS 15 I9`](#сценарий-asus-15-i9)
   - [Сценарий `ASUS 15 AMD RYZEN 7`](#сценарий-asus-15-amd-ryzen-7)
   - [Сценарий `ASUS 15 Celeron`](#сценарий-asus-15-celeron)
    - [Сценарий `ASUS 15 Pentium`](#сценарий-asus-15-pentium)
   -  [Сценарий `ASUS 17.3 I3`](#сценарий-asus-173-i3)
   - [Сценарий `ASUS 17.3 I5`](#сценарий-asus-173-i5)
   - [Сценарий `ASUS 17.3 I7`](#сценарий-asus-173-i7)
   -  [Сценарий `ASUS 17.3 I9`](#сценарий-asus-173-i9)
   - [Сценарий `ASUS 17.3 AMD`](#сценарий-asus-173-amd)
   - [Сценарий `ASUS 17.3 Celeron`](#сценарий-asus-173-celeron)
   -  [Сценарий `ASUS 17.3 Pentium`](#сценарий-asus-173-pentium)


## Структура файла
Файл представлен в формате JSON и содержит два основных раздела:
- `Asus laptops`: Содержит общие URL для фильтрации ноутбуков Asus.
- `scenarios`: Содержит набор сценариев, каждый из которых определяет характеристики ноутбуков Asus и их сопоставление с категориями PrestaShop.

## Раздел `Asus laptops`

Этот раздел содержит URL-адрес для фильтрации товаров.
- `url` (str): URL для фильтрации ноутбуков Asus на сайте Morlevi.

```json
"Asus laptops": {
    "url": "https://www.morlevi.co.il/Cat/1?p_315=5&sort=datafloat2%2Cprice&keyword="
  },
```

## Раздел `scenarios`

Этот раздел содержит набор сценариев для различных моделей ноутбуков ASUS. Каждый сценарий определяет уникальную комбинацию характеристик и категорий PrestaShop.

### Сценарий `ASUS 11.6 I3`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i3.

**Свойства**:

- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I3"` - Категория для ноутбуков с процессором Intel Core i3.
            - `"11"` - Размер экрана 11 дюймов.
```json
   "ASUS 11.6 I3": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I3", "11" ]
        }
      }
    },
```

### Сценарий `ASUS 11.6 I5`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i5.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I5"` - Категория для ноутбуков с процессором Intel Core i5.
            - `"11"` - Размер экрана 11 дюймов.
```json
    "ASUS 11.6 I5": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I5", "11" ]
        }
      }
    },
```

### Сценарий `ASUS 11.6 I7`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i7.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I7"` - Категория для ноутбуков с процессором Intel Core i7.
            - `"11"` - Размер экрана 11 дюймов.

```json
    "ASUS 11.6 I7": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I7", "11" ]
        }
      }
    },
```

### Сценарий `ASUS 11.6 I9`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i9.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I9"` - Категория для ноутбуков с процессором Intel Core i9.
            - `"11"` - Размер экрана 11 дюймов.
```json
    "ASUS 11.6 I9": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I9", "11" ]
        }
      }
    },
```
### Сценарий `ASUS 11.6 AMD`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 11.6 дюймов и процессором AMD.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS AMD"` - Категория для ноутбуков с процессором AMD.
            - `"11"` - Размер экрана 11 дюймов.
```json
    "ASUS 11.6 AMD": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS AMD", "11" ]
        }
      }
    },
```

### Сценарий `ASUS 11.6 Celeron`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 11.6 дюймов и процессором Intel Celeron.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (str): URL для фильтрации ноутбуков с процессором Intel Celeron на сайте Morlevi.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL CELERON"` - Категория для ноутбуков с процессором Intel Celeron.
            - `"11"` - Размер экрана 11 дюймов.
```json
    "ASUS 11.6 Celeron": {
      "brand": "ASUS",
      "url": "https://www.morlevi.co.il/Cat/69?p_238=1142&p_387=3416&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL CELERON", "11" ]
        }
      }
    },
```

### Сценарий `ASUS 11.6 Pentium`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 11.6 дюймов и процессором Intel Pentium.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL CELERON"` - Категория для ноутбуков с процессором Intel Pentium (объединена с Celeron).
            - `"11"` - Размер экрана 11 дюймов.
```json
  "ASUS 11.6 Pentium": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL CELERON", "11" ]
        }
      }
    },
```

### Сценарий `ASUS 13.4 - 13.3 I3`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i3.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I3"` - Категория для ноутбуков с процессором Intel Core i3.
            - `"13"` - Размер экрана от 13.3 до 13.4 дюймов.
```json
   "ASUS 13.4 - 13.3 I3": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I3", "13" ]
        }
      }
    },
```

### Сценарий `ASUS 13.4 - 13.3 I5`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i5.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (str): URL для фильтрации ноутбуков с процессором Intel Core i5 на сайте Morlevi.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I5"` - Категория для ноутбуков с процессором Intel Core i5.
            - `"13"` - Размер экрана от 13.3 до 13.4 дюймов.
```json
    "ASUS 13.4 - 13.3 I5": {
      "brand": "ASUS",
      "url": "https://www.morlevi.co.il/Cat/69?p_238=1143&p_387=3414&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I5", "13" ]
        }
      }
    },
```

### Сценарий `ASUS 13.4 - 13.3 I7`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i7.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (str): URL для фильтрации ноутбуков с процессором Intel Core i7 на сайте Morlevi.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I7"` - Категория для ноутбуков с процессором Intel Core i7.
            - `"13"` - Размер экрана от 13.3 до 13.4 дюймов.
```json
  "ASUS 13.4 - 13.3 I7": {
      "brand": "ASUS",
      "url": "https://www.morlevi.co.il/Cat/69?p_238=1143&p_387=3415&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I7", "13" ]
        }
      }
    },
```

### Сценарий `ASUS 13.4 - 13.3 I9`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Core i9.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I9"` - Категория для ноутбуков с процессором Intel Core i9.
            - `"13"` - Размер экрана от 13.3 до 13.4 дюймов.
```json
    "ASUS 13.4 - 13.3 I9": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I9", "13" ]
        }
      }
    },
```
### Сценарий `ASUS 13.4 - 13.3 AMD`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана от 13.3 до 13.4 дюймов и процессором AMD.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS AMD"` - Категория для ноутбуков с процессором AMD.
            - `"13"` - Размер экрана от 13.3 до 13.4 дюймов.
```json
   "ASUS 13.4 - 13.3 AMD": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS AMD", "13" ]
        }
      }
    },
```

### Сценарий `ASUS 13.4 - 13.3 Celeron`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Celeron.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL CELERON"` - Категория для ноутбуков с процессором Intel Celeron.
            - `"13"` - Размер экрана от 13.3 до 13.4 дюймов.
```json
    "ASUS 13.4 - 13.3 Celeron": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL CELERON", "13" ]
        }
      }
    },
```

### Сценарий `ASUS 13.4 - 13.3 Pentium`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана от 13.3 до 13.4 дюймов и процессором Intel Pentium.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL CELERON"` - Категория для ноутбуков с процессором Intel Pentium (объединена с Celeron).
            - `"13"` - Размер экрана от 13.3 до 13.4 дюймов.
```json
 "ASUS 13.4 - 13.3 Pentium": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL CELERON", "13" ]
        }
      }
    },
```

### Сценарий `ASUS 14 I3`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 14 дюймов и процессором Intel Core i3.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (str): URL для фильтрации ноутбуков с процессором Intel Core i3 на сайте Morlevi.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I3"` - Категория для ноутбуков с процессором Intel Core i3.
            - `"14"` - Размер экрана 14 дюймов.
```json
    "ASUS 14 I3": {
      "brand": "ASUS",
      "url": "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3413&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I3", "14" ]
        }
      }
    },
```

### Сценарий `ASUS 14 I5`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 14 дюймов и процессором Intel Core i5.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (str): URL для фильтрации ноутбуков с процессором Intel Core i5 на сайте Morlevi.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I5"` - Категория для ноутбуков с процессором Intel Core i5.
            - `"14"` - Размер экрана 14 дюймов.
```json
 "ASUS 14 I5": {
      "brand": "ASUS",
      "url": "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3414&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I5", "14" ]
        }
      }
    },
```

### Сценарий `ASUS 14 I7`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 14 дюймов и процессором Intel Core i7.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (str): URL для фильтрации ноутбуков с процессором Intel Core i7 на сайте Morlevi.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I7"` - Категория для ноутбуков с процессором Intel Core i7.
            - `"14"` - Размер экрана 14 дюймов.
```json
    "ASUS 14 I7": {
      "brand": "ASUS",
      "url": "https://www.morlevi.co.il/Cat/69?p_238=1144&p_387=3415&sort=datafloat2%2Cprice&keyword=",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I7", "14" ]
        }
      }
    },
```
### Сценарий `ASUS 14 I9`

**Описание**: Конфигурация для ноутбуков ASUS с диагональю экрана 14 дюймов и процессором Intel Core i9.

**Свойства**:
- `brand` (str): "ASUS" - бренд ноутбука.
- `url` (null): URL-адрес не указан, так как категория на сайте выбирается через фильтр.
- `checkbox` (bool): `false` - чекбокс не используется.
- `active` (bool): `true` - сценарий активен.
- `condition` (str): "new" - условие - новый товар.
- `presta_categories` (dict): Категории PrestaShop.
    - `template` (dict): Шаблон для категорий.
        - `asus` (list): Список категорий PrestaShop.
            - `"LAPTOPS INTEL I9"` - Категория для ноутбуков с процессором Intel Core i9.
            - `"14"` - Размер экрана 14 дюймов.
```json
   "ASUS 14 I9": {
      "brand": "ASUS",
      "url": null,
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "asus": [ "LAPTOPS INTEL I9", "14" ]
        }
      }
    },
```
### Сценарий `AS