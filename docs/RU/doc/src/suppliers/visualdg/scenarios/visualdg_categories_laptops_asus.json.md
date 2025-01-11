# Документация для `visualdg_categories_laptops_asus.json`

## Обзор

Данный файл `visualdg_categories_laptops_asus.json` содержит конфигурации сценариев для ноутбуков ASUS, используемых для определения категорий товаров и их параметров. Каждый сценарий представляет собой определенную модель ноутбука ASUS с различными характеристиками, такими как размер экрана и тип процессора.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [Описание сценариев](#описание-сценариев)
    - [ASUS 11.6 I3](#asus-116-i3)
    - [ASUS 11.6 I5](#asus-116-i5)
    - [ASUS 11.6 I7](#asus-116-i7)
    - [ASUS 11.6 I9](#asus-116-i9)
    - [ASUS 11.6 AMD](#asus-116-amd)
    - [ASUS 11.6 Pentium - Celeron](#asus-116-pentium---celeron)
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
    - [ASUS 14 AMD](#asus-14-amd)
    - [ASUS 14 Celeron](#asus-14-celeron)
    - [ASUS 14 Pentium](#asus-14-pentium)
    - [ASUS 15 I3](#asus-15-i3)
    - [ASUS 15 I5](#asus-15-i5)
    - [ASUS 15 I7](#asus-15-i7)
    - [ASUS 15 I9](#asus-15-i9)
    - [ASUS 15 AMD](#asus-15-amd)
    - [ASUS 15 Celeron](#asus-15-celeron)
    - [ASUS 15 Pentium](#asus-15-pentium)
    - [ASUS 17.3 I3](#asus-173-i3)
    - [ASUS 17.3 I5](#asus-173-i5)
    - [ASUS 17.3 I7](#asus-173-i7)
    - [ASUS 17.3 I9](#asus-173-i9)
    - [ASUS 17.3 AMD](#asus-173-amd)
    - [ASUS 17.3 Celeron](#asus-173-celeron)
    - [ASUS 17.3 Pentium](#asus-173-pentium)

## Структура файла

Файл представляет собой JSON-объект, содержащий единственный ключ `"scenarios"`. Значение этого ключа - другой JSON-объект, где каждый ключ является названием сценария (модели ноутбука ASUS), а значение - объект, описывающий параметры этого сценария.

Каждый сценарий включает следующие ключи:

- `"brand"`: Строка, указывающая на бренд ноутбука (всегда `"ASUS"`).
- `"url"`: Строка, содержащая URL-адрес, связанный с моделью.
- `"checkbox"`: Логическое значение, определяющее состояние чекбокса (всегда `false`).
- `"active"`: Логическое значение, указывающее, активен ли сценарий (всегда `true`).
- `"condition"`: Строка, указывающая на состояние товара (всегда `"new"`).
- `"presta_categories"`: Строка, содержащая идентификаторы категорий PrestaShop, разделенные запятыми.

## Описание сценариев

### ASUS 11.6 I3

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"--------------------------------ASUS 11.6 I3 ----------------------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"2,3,4,989,309,358,48"`.

### ASUS 11.6 I5

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"-----------ASUS 11.6 I5-------------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"2,3,234,989,309,361,48"`.

### ASUS 11.6 I7

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"--------------ASUS 11.6 I7-----------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,8,6"`.

### ASUS 11.6 I9

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 11.6 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"-------------ASUS 11.6 I9---------------- "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,8,7"`.

### ASUS 11.6 AMD

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 11.6 дюймов и процессором AMD.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"-------------ASUS 11.6 AMD---------------- "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"2,3,4,989,309,361,48"`.

### ASUS 11.6 Pentium - Celeron

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 11.6 дюймов и процессором Pentium или Celeron.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253279/253293"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"2,3,233,989,309,359,48"`.

### ASUS 11.6 Pentium

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 11.6 дюймов и процессором Pentium.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253280/253293"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"2,3,233,989,309,359,48"`.

### ASUS 13.4 - 13.3 I3

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 13.4 или 13.3 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"-------------------ASUS 13.4 - 13.3 I3-----------r "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"2,3,4,990,48"`.

### ASUS 13.4 - 13.3 I5

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 13.4 или 13.3 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253273/253294"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,8,54,5,358"`.

### ASUS 13.4 - 13.3 I7

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 13.4 или 13.3 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253274/253294"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,8,54,4,358,993"`.

### ASUS 13.4 - 13.3 I9

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 13.4 или 13.3 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"------------ASUS 13.4 - 13.3 I9----------------- "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,8,54,4,358,990"`.

### ASUS 13.4 - 13.3 AMD

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 13.4 или 13.3 дюймов и процессором AMD.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"----------------ASUS 13.4 - 13.3 AMD------------------ "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,9,248,430"`.

### ASUS 13.4 - 13.3 Celeron

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 13.4 или 13.3 дюймов и процессором Celeron.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"-----------------ASUS 13.4 - 13.3 Celeron---------------- "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,9,233,431"`.

### ASUS 13.4 - 13.3 Pentium

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 13.4 или 13.3 дюймов и процессором Pentium.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"-----------------ASUS 13.4 - 13.3 Pentium ------------ "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,9,232,432"`.

### ASUS 14 I3

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 14 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253272/253295"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,8,54,4,358,991"`.

### ASUS 14 I5

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 14 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253273/253295?"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,10,5,434"`.

### ASUS 14 I7

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 14 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253273/253295"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,10,6,435"`.

### ASUS 14 I9

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 14 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253273/253295"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,10,7,436"`.

### ASUS 14 AMD

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 14 дюймов и процессором AMD.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253281"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,10,248,437"`.

### ASUS 14 Celeron

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 14 дюймов и процессором Celeron.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253280/253295"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,10,233,438"`.

### ASUS 14 Pentium

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 14 дюймов и процессором Pentium.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253279/253295"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,10,232,439"`.

### ASUS 15 I3

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 15 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253272/253296"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,8,54,4,358,992"`.

### ASUS 15 I5

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 15 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253273/253296"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,11,5,441"`.

### ASUS 15 I7

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 15 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253274/253296"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,11,6,442"`.

### ASUS 15 I9

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 15 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/253278/253296"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,11,7,443"`.

### ASUS 15 AMD

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 15 дюймов и процессором AMD.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253281/253296"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,11,248,444"`.

### ASUS 15 Celeron

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 15 дюймов и процессором Celeron.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253280/253296"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,11,233,445"`.

### ASUS 15 Pentium

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 15 дюймов и процессором Pentium.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253279/253296"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,11,232,446"`.

### ASUS 17.3 I3

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 17.3 дюймов и процессором Intel Core i3.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"---------------ASUS 17.3 I3------------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,12,4,447"`.

### ASUS 17.3 I5

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 17.3 дюймов и процессором Intel Core i5.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"--------------ASUS 17.3 I5--------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,12,5,448"`.

### ASUS 17.3 I7

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 17.3 дюймов и процессором Intel Core i7.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253274/253297"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,12,6,449"`.

### ASUS 17.3 I9

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 17.3 дюймов и процессором Intel Core i9.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"https://www.visualdg.co.il/169419-%D7%A0%D7%99%D7%99%D7%93%D7%99-ASUS/243216-Asus/253278/253297"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,12,7,450"`.

### ASUS 17.3 AMD

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 17.3 дюймов и процессором AMD.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"------------------------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,12,248,451"`.

### ASUS 17.3 Celeron

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 17.3 дюймов и процессором Celeron.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"----------------------------- "`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,12,233,452"`.

### ASUS 17.3 Pentium

**Описание**: Конфигурация для ноутбука ASUS с диагональю экрана 17.3 дюймов и процессором Pentium.

**Параметры**:
- `brand` (str): `"ASUS"`.
- `url` (str): `"---------------------------------"`.
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): `"new"`.
- `presta_categories` (str): `"3,48,12,232,453"`.