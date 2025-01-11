# Документация для `morlevi_categories_laptops_dell.json`

## Обзор

Данный файл содержит JSON-структуру, определяющую сценарии для категоризации ноутбуков Dell. В каждом сценарии заданы характеристики, такие как бренд, URL, активность, состояние и категории PrestaShop, а также соответствия этим категориям.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание сценариев](#описание-сценариев)
    - [DELL 11.6 I3](#dell-116-i3)
    - [DELL 11.6 I5](#dell-116-i5)
    - [DELL 11.6 I7](#dell-116-i7)
    - [DELL 11.6 I9](#dell-116-i9)
    - [DELL 11.6 AMD](#dell-116-amd)
    - [DELL 11.6 Celeron](#dell-116-celeron)
    - [DELL 11.6 Pentium](#dell-116-pentium)
    - [DELL 13.4 - 13.3 I3](#dell-134---133-i3)
    - [DELL 13.4 - 13.3 I5](#dell-134---133-i5)
    - [DELL 13.4 - 13.3 I7](#dell-134---133-i7)
    - [DELL 13.4 - 13.3 I9](#dell-134---133-i9)
    - [DELL 13.4 - 13.3 AMD](#dell-134---133-amd)
    - [DELL 13.4 - 13.3 Celeron](#dell-134---133-celeron)
    - [DELL 13.4 - 13.3 Pentium](#dell-134---133-pentium)
    - [DELL 14 I3](#dell-14-i3)
    - [DELL 14 I5](#dell-14-i5)
    - [DELL 14 I7](#dell-14-i7)
    - [DELL 14 I9](#dell-14-i9)
    - [DELL 14 AMD](#dell-14-amd)
    - [DELL 14 Celeron](#dell-14-celeron)
    - [DELL 14 Pentium](#dell-14-pentium)
    - [DELL 15 I3](#dell-15-i3)
    - [DELL 15 I5](#dell-15-i5)
    - [DELL 15 I7](#dell-15-i7)
    - [DELL 15 I9](#dell-15-i9)
    - [DELL 15 AMD](#dell-15-amd)
    - [DELL 15 Celeron](#dell-15-celeron)
    - [DELL 15 Pentium](#dell-15-pentium)
     - [DELL 17.3 I3](#dell-173-i3)
    - [DELL 17.3 I5](#dell-173-i5)
    - [DELL 17.3 I7](#dell-173-i7)
    - [DELL 17.3 I9](#dell-173-i9)
    - [DELL 17.3 AMD](#dell-173-amd)
    - [DELL 17.3 Celeron](#dell-173-celeron)
    - [DELL 17.3 Pentium](#dell-173-pentium)

## Структура JSON

Файл состоит из одного объекта JSON, содержащего ключ `"scenarios"`. Значением этого ключа является другой объект, где каждый ключ представляет собой название сценария, а значение – это объект, содержащий информацию о данном сценарии.

## Описание сценариев

Каждый сценарий имеет следующую структуру:
- `brand` (str): Бренд ноутбука, в данном случае всегда `"DELL"`.
- `url` (str | null): URL-адрес, связанный с категорией товаров, может быть `null`.
- `checkbox` (bool): Флаг, указывающий на наличие чекбокса (всегда `false`).
- `active` (bool): Флаг, указывающий активность сценария (всегда `true`).
- `condition` (str): Состояние товара (всегда `"new"`).
- `presta_categories` (object): Объект, определяющий соответствия категориям PrestaShop.
    - `template` (object): Объект, содержащий соответствия категориям для бренда `"dell"`.
        - `"dell"` (list): Список категорий PrestaShop, где первый элемент - процессор, второй размер экрана.

### DELL 11.6 I3

**Описание**: Сценарий для ноутбуков DELL с экраном 11.6 дюймов и процессором Intel I3.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: 
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I3", "11" ]`

### DELL 11.6 I5

**Описание**: Сценарий для ноутбуков DELL с экраном 11.6 дюймов и процессором Intel I5.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: 
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I5", "11" ]`

### DELL 11.6 I7

**Описание**: Сценарий для ноутбуков DELL с экраном 11.6 дюймов и процессором Intel I7.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I7", "11" ]`

### DELL 11.6 I9

**Описание**: Сценарий для ноутбуков DELL с экраном 11.6 дюймов и процессором Intel I9.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I9", "11" ]`

### DELL 11.6 AMD

**Описание**: Сценарий для ноутбуков DELL с экраном 11.6 дюймов и процессором AMD.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS AMD", "11" ]`

### DELL 11.6 Celeron

**Описание**: Сценарий для ноутбуков DELL с экраном 11.6 дюймов и процессором Celeron.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "11" ]`

### DELL 11.6 Pentium
**Описание**: Сценарий для ноутбуков DELL с экраном 11.6 дюймов и процессором Pentium.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "11" ]`

### DELL 13.4 - 13.3 I3

**Описание**: Сценарий для ноутбуков DELL с экраном 13.4 - 13.3 дюймов и процессором Intel I3.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I3", "13" ]`

### DELL 13.4 - 13.3 I5

**Описание**: Сценарий для ноутбуков DELL с экраном 13.4 - 13.3 дюймов и процессором Intel I5.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I5", "13" ]`

### DELL 13.4 - 13.3 I7

**Описание**: Сценарий для ноутбуков DELL с экраном 13.4 - 13.3 дюймов и процессором Intel I7.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I7", "13" ]`

### DELL 13.4 - 13.3 I9

**Описание**: Сценарий для ноутбуков DELL с экраном 13.4 - 13.3 дюймов и процессором Intel I9.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I9", "13" ]`

### DELL 13.4 - 13.3 AMD

**Описание**: Сценарий для ноутбуков DELL с экраном 13.4 - 13.3 дюймов и процессором AMD.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS AMD", "13" ]`

### DELL 13.4 - 13.3 Celeron

**Описание**: Сценарий для ноутбуков DELL с экраном 13.4 - 13.3 дюймов и процессором Celeron.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELRON", "13" ]`

### DELL 13.4 - 13.3 Pentium

**Описание**: Сценарий для ноутбуков DELL с экраном 13.4 - 13.3 дюймов и процессором Pentium.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "13" ]`

### DELL 14 I3

**Описание**: Сценарий для ноутбуков DELL с экраном 14 дюймов и процессором Intel I3.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I3", "14" ]`

### DELL 14 I5

**Описание**: Сценарий для ноутбуков DELL с экраном 14 дюймов и процессором Intel I5.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I5", "14" ]`

### DELL 14 I7

**Описание**: Сценарий для ноутбуков DELL с экраном 14 дюймов и процессором Intel I7.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I7", "14" ]`

### DELL 14 I9

**Описание**: Сценарий для ноутбуков DELL с экраном 14 дюймов и процессором Intel I9.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I9", "14" ]`

### DELL 14 AMD

**Описание**: Сценарий для ноутбуков DELL с экраном 14 дюймов и процессором AMD.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS AMD", "14" ]`

### DELL 14 Celeron

**Описание**: Сценарий для ноутбуков DELL с экраном 14 дюймов и процессором Celeron.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "14" ]`

### DELL 14 Pentium

**Описание**: Сценарий для ноутбуков DELL с экраном 14 дюймов и процессором Pentium.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "14" ]`

### DELL 15 I3

**Описание**: Сценарий для ноутбуков DELL с экраном 15 дюймов и процессором Intel I3.

**Поля**:
- `brand`: `"DELL"`
- `url`: `"https://www.morlevi.co.il/Cat/1?p_315=7&p_238=1145&p_387=3413&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I3", "15" ]`

### DELL 15 I5

**Описание**: Сценарий для ноутбуков DELL с экраном 15 дюймов и процессором Intel I5.

**Поля**:
- `brand`: `"DELL"`
- `url`: `"https://www.morlevi.co.il/Cat/1?p_315=7&p_238=1145&p_387=3414&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I5", "15" ]`

### DELL 15 I7

**Описание**: Сценарий для ноутбуков DELL с экраном 15 дюймов и процессором Intel I7.

**Поля**:
- `brand`: `"DELL"`
- `url`: `"https://www.morlevi.co.il/Cat/1?p_315=7&p_238=1145&p_387=3415&sort=datafloat2%2Cprice&keyword="`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I7", "15" ]`

### DELL 15 I9

**Описание**: Сценарий для ноутбуков DELL с экраном 15 дюймов и процессором Intel I9.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I9", "15" ]`

### DELL 15 AMD

**Описание**: Сценарий для ноутбуков DELL с экраном 15 дюймов и процессором AMD.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS AMD", "15" ]`

### DELL 15 Celeron

**Описание**: Сценарий для ноутбуков DELL с экраном 15 дюймов и процессором Celeron.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "15" ]`

### DELL 15 Pentium

**Описание**: Сценарий для ноутбуков DELL с экраном 15 дюймов и процессором Pentium.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "15" ]`

### DELL 17.3 I3

**Описание**: Сценарий для ноутбуков DELL с экраном 17.3 дюймов и процессором Intel I3.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I3", "17" ]`

### DELL 17.3 I5

**Описание**: Сценарий для ноутбуков DELL с экраном 17.3 дюймов и процессором Intel I5.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I5", "17" ]`

### DELL 17.3 I7

**Описание**: Сценарий для ноутбуков DELL с экраном 17.3 дюймов и процессором Intel I7.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I7", "17" ]`

### DELL 17.3 I9

**Описание**: Сценарий для ноутбуков DELL с экраном 17.3 дюймов и процессором Intel I9.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL I9", "17" ]`

### DELL 17.3 AMD

**Описание**: Сценарий для ноутбуков DELL с экраном 17.3 дюймов и процессором AMD.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS AMD", "17" ]`

### DELL 17.3 Celeron

**Описание**: Сценарий для ноутбуков DELL с экраном 17.3 дюймов и процессором Celeron.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "17" ]`

### DELL 17.3 Pentium

**Описание**: Сценарий для ноутбуков DELL с экраном 17.3 дюймов и процессором Pentium.

**Поля**:
- `brand`: `"DELL"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
    - `template`:
        - `dell`: `[ "LAPTOPS INTEL CELERON", "17" ]`