# Документация для `morlevi_categories_laptops_hp.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
    - [HP 11.6 I3](#hp-116-i3)
    - [HP 11.6 I5](#hp-116-i5)
    - [HP 11.6 I7](#hp-116-i7)
    - [HP 11.6 I9](#hp-116-i9)
    - [HP 11.6 AMD](#hp-116-amd)
    - [HP 11.6 Celeron](#hp-116-celeron)
    - [HP 11.6 Pentium](#hp-116-pentium)
    - [HP 13.4 - 13.3 I3](#hp-134---133-i3)
    - [HP 13.4 - 13.3 I5](#hp-134---133-i5)
    - [HP 13.4 - 13.3 I7](#hp-134---133-i7)
    - [HP 13.4 - 13.3 I9](#hp-134---133-i9)
    - [HP 13.4 - 13.3 AMD](#hp-134---133-amd)
    - [HP 13.4 - 13.3 Celeron](#hp-134---133-celeron)
    - [HP 13.4 - 13.3 Pentium](#hp-134---133-pentium)
    - [HP 14 I3](#hp-14-i3)
    - [HP 14 I5](#hp-14-i5)
    - [HP 14 I7](#hp-14-i7)
    - [HP 14 I9](#hp-14-i9)
    - [HP 14 AMD RYZEN 7](#hp-14-amd-ryzen-7)
    - [HP 14 Celeron](#hp-14-celeron)
    - [HP 14 Pentium](#hp-14-pentium)
    - [HP 15 I3](#hp-15-i3)
    - [HP 15 I5](#hp-15-i5)
    - [HP 15 I7](#hp-15-i7)
    - [HP 15 I9](#hp-15-i9)
    - [HP 15 AMD RYZEN 5](#hp-15-amd-ryzen-5)
     - [HP 15 AMD RYZEN 7](#hp-15-amd-ryzen-7-1)
    - [HP 15 Celeron](#hp-15-celeron)
    - [HP 15 Pentium](#hp-15-pentium)
    - [HP 17.3 I3](#hp-173-i3)
    - [HP 17.3 I5](#hp-173-i5)
    - [HP 17.3 I7](#hp-173-i7)
    - [HP 17.3 I9](#hp-173-i9)
    - [HP 17.3 AMD](#hp-173-amd)
    - [HP 17.3 Celeron](#hp-173-celeron)
    - [HP 17.3 Pentium](#hp-173-pentium)


## Обзор

Данный JSON-файл содержит сценарии для категоризации ноутбуков HP по различным характеристикам (процессор, размер экрана) для последующего определения категорий в PrestaShop. Каждый сценарий определяет соответствие между конфигурацией ноутбука и категориями в магазине.

## Структура файла

Файл состоит из одного основного JSON-объекта, содержащего ключ `"scenarios"`, который является объектом, в котором ключами являются названия сценариев, а значениями - объекты, описывающие параметры сценария.

Каждый сценарий имеет следующую структуру:
- `brand` (string): Бренд ноутбука (в данном случае всегда "HP").
- `url` (null): URL, связанный со сценарием (не используется).
- `checkbox` (boolean): Флаг для использования в интерфейсе (не используется).
- `active` (boolean): Флаг, указывающий, активен ли сценарий.
- `condition` (string): Состояние товара (в данном случае "new").
- `presta_categories` (object): Объект, содержащий информацию о категориях PrestaShop.
  - `template` (object): Объект, определяющий соответствие между брендом и категориями. Ключом является бренд, а значением - массив категорий.

## Сценарии

### `HP 11.6 I3`
**Описание**: Сценарий для ноутбуков HP с диагональю 11.6 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I3", "11"]`

### `HP 11.6 I5`
**Описание**: Сценарий для ноутбуков HP с диагональю 11.6 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I5", "11"]`

### `HP 11.6 I7`
**Описание**: Сценарий для ноутбуков HP с диагональю 11.6 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I7", "11"]`

### `HP 11.6 I9`
**Описание**: Сценарий для ноутбуков HP с диагональю 11.6 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I9", "11"]`

### `HP 11.6 AMD`
**Описание**: Сценарий для ноутбуков HP с диагональю 11.6 дюймов и процессором AMD.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS AMD", "11"]`

### `HP 11.6 Celeron`
**Описание**: Сценарий для ноутбуков HP с диагональю 11.6 дюймов и процессором Intel Celeron.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "11"]`

### `HP 11.6 Pentium`
**Описание**: Сценарий для ноутбуков HP с диагональю 11.6 дюймов и процессором Intel Pentium.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "11"]`

### `HP 13.4 - 13.3 I3`
**Описание**: Сценарий для ноутбуков HP с диагональю 13.4 - 13.3 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I3", "13"]`

### `HP 13.4 - 13.3 I5`
**Описание**: Сценарий для ноутбуков HP с диагональю 13.4 - 13.3 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I5", "13"]`

### `HP 13.4 - 13.3 I7`
**Описание**: Сценарий для ноутбуков HP с диагональю 13.4 - 13.3 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I7", "13"]`

### `HP 13.4 - 13.3 I9`
**Описание**: Сценарий для ноутбуков HP с диагональю 13.4 - 13.3 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I9", "13"]`

### `HP 13.4 - 13.3 AMD`
**Описание**: Сценарий для ноутбуков HP с диагональю 13.4 - 13.3 дюймов и процессором AMD.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS AMD", "13"]`

### `HP 13.4 - 13.3 Celeron`
**Описание**: Сценарий для ноутбуков HP с диагональю 13.4 - 13.3 дюймов и процессором Intel Celeron.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "13"]`

### `HP 13.4 - 13.3 Pentium`
**Описание**: Сценарий для ноутбуков HP с диагональю 13.4 - 13.3 дюймов и процессором Intel Pentium.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "13"]`

### `HP 14 I3`
**Описание**: Сценарий для ноутбуков HP с диагональю 14 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I3", "14"]`

### `HP 14 I5`
**Описание**: Сценарий для ноутбуков HP с диагональю 14 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I5", "14"]`

### `HP 14 I7`
**Описание**: Сценарий для ноутбуков HP с диагональю 14 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I7", "14"]`

### `HP 14 I9`
**Описание**: Сценарий для ноутбуков HP с диагональю 14 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I9", "14"]`

### `HP 14 AMD RYZEN 7`
**Описание**: Сценарий для ноутбуков HP с диагональю 14 дюймов и процессором AMD Ryzen 7.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I7", "14"]`

### `HP 14 Celeron`
**Описание**: Сценарий для ноутбуков HP с диагональю 14 дюймов и процессором Intel Celeron.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "14"]`

### `HP 14 Pentium`
**Описание**: Сценарий для ноутбуков HP с диагональю 14 дюймов и процессором Intel Pentium.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "14"]`

### `HP 15 I3`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I3", "15"]`

### `HP 15 I5`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I5", "15"]`

### `HP 15 I7`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I7", "15"]`

### `HP 15 I9`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I9", "15"]`

### `HP 15 AMD RYZEN 5`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором AMD Ryzen 5.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `gigabyte`: `["LAPTOPS AMD RYZEN 5", "15"]`

### `HP 15 AMD RYZEN 7`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором AMD Ryzen 7.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS AMD RYZEN 7", "15"]`

### `HP 15 Celeron`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором Intel Celeron.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "15"]`

### `HP 15 Pentium`
**Описание**: Сценарий для ноутбуков HP с диагональю 15 дюймов и процессором Intel Pentium.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "15"]`

### `HP 17.3 I3`
**Описание**: Сценарий для ноутбуков HP с диагональю 17.3 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I3", "17"]`

### `HP 17.3 I5`
**Описание**: Сценарий для ноутбуков HP с диагональю 17.3 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I5", "17"]`

### `HP 17.3 I7`
**Описание**: Сценарий для ноутбуков HP с диагональю 17.3 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I7", "17"]`

### `HP 17.3 I9`
**Описание**: Сценарий для ноутбуков HP с диагональю 17.3 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL I9", "17"]`

### `HP 17.3 AMD`
**Описание**: Сценарий для ноутбуков HP с диагональю 17.3 дюймов и процессором AMD.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS AMD", "17"]`

### `HP 17.3 Celeron`
**Описание**: Сценарий для ноутбуков HP с диагональю 17.3 дюймов и процессором Intel Celeron.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "17"]`

### `HP 17.3 Pentium`
**Описание**: Сценарий для ноутбуков HP с диагональю 17.3 дюймов и процессором Intel Pentium.

**Параметры**:
- `brand`: `"HP"`
- `url`: `null`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`:
  - `template`:
    - `HP`: `["LAPTOPS INTEL CELERON", "17"]`