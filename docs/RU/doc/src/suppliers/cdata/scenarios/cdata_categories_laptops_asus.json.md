# Документация для `cdata_categories_laptops_asus.json`

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для категоризации ноутбуков ASUS. Каждый сценарий определяет бренд, URL, состояние чекбокса, активность, состояние товара и категории PrestaShop, к которым должен принадлежать товар.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [scenarios](#scenarios)
- [Сценарии](#сценарии)
  - [ASUS 11.6 I3](#asus-116-i3)
  - [ASUS 14 I3 AsusPro](#asus-14-i3-asuspro)
  - [ASUS 11.6 I5](#asus-116-i5)
  - [ASUS 11.6 I7](#asus-116-i7)
  - [ASUS 11.6 I9](#asus-116-i9)
  - [ASUS 11.6 AMD](#asus-116-amd)
  - [ASUS 11.6 Celeron E203/L203](#asus-116-celeron-e203l203)
  - [ASUS 11.6 Celeron E210/E410](#asus-116-celeron-e210e410)
  - [ASUS 11.6 Celeron ChromeBook Flip](#asus-116-celeron-chromebook-flip)
  - [ASUS 11.6 Pentium](#asus-116-pentium)
  - [ASUS 13.4 - 13.3 I3](#asus-134---133-i3)
  - [ASUS 13.4 - 13.3 I5 VivoBook](#asus-134---133-i5-vivobook)
  - [ASUS 13.4 - 13.3 I5 ZenBook](#asus-134---133-i5-zenbook)
  - [ASUS 13.4 - 13.3 I5 ZenBook Flip](#asus-134---133-i5-zenbook-flip)
  - [ASUS 13.4 - 13.3 I7 ZenBook](#asus-134---133-i7-zenbook)
  - [ASUS 13.4 - 13.3 I7 ZenBook Flip](#asus-134---133-i7-zenbook-flip)
  - [ASUS 13.4 - 13.3 I9](#asus-134---133-i9)
  - [ASUS 13.4 - 13.3 AMD](#asus-134---133-amd)
  - [ASUS 13.4 - 13.3 Celeron](#asus-134---133-celeron)
  - [ASUS 13.4 - 13.3 Pentium](#asus-134---133-pentium)
  - [ASUS 14 I5 AsusPro](#asus-14-i5-asuspro)
  - [ASUS 14 I5 VivoBook](#asus-14-i5-vivobook)
  - [ASUS 14 I5 ZenBook](#asus-14-i5-zenbook)
  - [ASUS 14 I5 ZenBook Flip](#asus-14-i5-zenbook-flip)
  - [ASUS 14 I7 X409](#asus-14-i7-x409)
  - [ASUS 14 I7 AsusPro](#asus-14-i7-asuspro)
  - [ASUS 14 I7 VivoBook](#asus-14-i7-vivobook)
  - [ASUS 14 I7 ZenBook](#asus-14-i7-zenbook)
  - [ASUS 14 I7 ZenBook Pro Duo](#asus-14-i7-zenbook-pro-duo)
  - [ASUS 14 I9](#asus-14-i9)
  - [ASUS 14 AMD](#asus-14-amd)
  - [ASUS 14 Celeron](#asus-14-celeron)
  - [ASUS 14 Pentium](#asus-14-pentium)
  - [ASUS 15 I3 X509](#asus-15-i3-x509)
  - [ASUS 15 I5 X509](#asus-15-i5-x509)
  - [ASUS 15 I5 ASUSPro](#asus-15-i5-asuspro)
  - [ASUS 15 I5 VivoBook](#asus-15-i5-vivobook)
  - [ASUS 15 I7 X509](#asus-15-i7-x509)
  - [ASUS 15 I7 ASUSPro](#asus-15-i7-asuspro)
  - [ASUS 15 I7 VivoBook](#asus-15-i7-vivobook)
  - [ASUS 15 I7 ZenBook](#asus-15-i7-zenbook)
  - [ASUS 15 I7 ZenBook Pro Duo](#asus-15-i7-zenbook-pro-duo)
  - [ASUS 15 I7 Asus Gaming](#asus-15-i7-asus-gaming)
  - [ASUS 15 I9 Gaming](#asus-15-i9-gaming)
  - [ASUS 15 I9 ZenBook Pro Duo](#asus-15-i9-zenbook-pro-duo)
  - [ASUS 15 AMD Gaming](#asus-15-amd-gaming)
  - [ASUS 15 Celeron](#asus-15-celeron)
  - [ASUS 15 Pentium X543](#asus-15-pentium-x543)
  - [ASUS 17.3 I3](#asus-173-i3)
  - [ASUS 17.3 I5](#asus-173-i5)
  - [ASUS 17.3 I7 Gaming](#asus-173-i7-gaming)
  - [ASUS 17.3 I9](#asus-173-i9)
  - [ASUS 17.3 AMD](#asus-173-amd)
  - [ASUS 17.3 Celeron](#asus-173-celeron)
  - [ASUS 17.3 Pentium](#asus-173-pentium)

## Структура JSON

### `scenarios`

Объект, содержащий сценарии категоризации. Каждый ключ в этом объекте представляет собой название сценария, а значение — объект с данными сценария.

## Сценарии

### `ASUS 11.6 I3`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором Intel Core i3.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-----------ASUS 11.6 I3-------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "2,3,4,989,309,358,48".

### `ASUS 14 I3 AsusPro`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i3 серии AsusPro.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6447!-#!227!#-!4633!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,4,433,654".

### `ASUS 11.6 I5`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором Intel Core i5.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-----------ASUS 11.6 I5-------------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "2,3,234,989,309,361,48".

### `ASUS 11.6 I7`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором Intel Core i7.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "--------------ASUS 11.6 I7-----------------".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,8,6".

### `ASUS 11.6 I9`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором Intel Core i9.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-------------ASUS 11.6 I9---------------- ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,8,7".

### `ASUS 11.6 AMD`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором AMD.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-------------ASUS 11.6 AMD---------------- ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,8,248,361".

### `ASUS 11.6 Celeron E203/L203`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором Celeron E203/L203.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6176!-#!227!#-!4655!-#!225!#-!4869".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,233,359,615".

### `ASUS 11.6 Celeron E210/E410`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором Celeron E210/E410.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6432!-#!227!#-!4655!-#!225!#-!4869".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,233,359,616".

### `ASUS 11.6 Celeron ChromeBook Flip`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов Celeron ChromeBook Flip.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6463!-#!227!#-!4655!-#!225!#-!4869".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,233,359,617".

### `ASUS 11.6 Pentium`

**Описание**: Сценарий для ноутбуков ASUS 11.6 дюймов с процессором Pentium.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-----------------ASUS 11.6 Pentium------------ ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,8,232,360".

### `ASUS 13.4 - 13.3 I3`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Intel Core i3.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-------------------ASUS 13.4 - 13.3 I3-----------r ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "2,3,4,990,48".

### `ASUS 13.4 - 13.3 I5 VivoBook`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Intel Core i5 серии VivoBook.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235!#-!6221!-#!227m!#-!4634!-#!225!#-!4877".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,5,427,618,49".

### `ASUS 13.4 - 13.3 I5 ZenBook`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Intel Core i5 серии ZenBook.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!4812!-#!227!#-!4634!-#!225!#-!4877".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,5,427,618,619,49".

### `ASUS 13.4 - 13.3 I5 ZenBook Flip`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Intel Core i5 серии ZenBook Flip.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6376!-#!227!#-!4634!-#!225!#-!4877".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,5,427,618,620,49".

### `ASUS 13.4 - 13.3 I7 ZenBook`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Intel Core i7 серии ZenBook.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!4812!-#!227!#-!4635!-#!225!#-!4877".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,6,619,49".

### `ASUS 13.4 - 13.3 I7 ZenBook Flip`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Intel Core i7 серии ZenBook Flip.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6376!-#!227!#-!4635!-#!225!#-!4877".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,6,620,49".

### `ASUS 13.4 - 13.3 I9`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Intel Core i9.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "------------ASUS 13.4 - 13.3 I9----------------- ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,7,449".

### `ASUS 13.4 - 13.3 AMD`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором AMD.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "----------------ASUS 13.4 - 13.3 AMD------------------ ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,248,454".

### `ASUS 13.4 - 13.3 Celeron`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Celeron.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-----------------ASUS 13.4 - 13.3 Celeron---------------- ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,233,431,54".

### `ASUS 13.4 - 13.3 Pentium`

**Описание**: Сценарий для ноутбуков ASUS 13.4 - 13.3 дюймов с процессором Pentium.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "-----------------ASUS 13.4 - 13.3 Pentium ------------ ".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,9,232,432,54".

### `ASUS 14 I5 AsusPro`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i5 серии AsusPro.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235!#-!6447!-#!227m!#-!4634!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,5,434,649,54".

### `ASUS 14 I5 VivoBook`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i5 серии VivoBook.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6221!-#!227!#-!4634!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,5,434,626,49".

### `ASUS 14 I5 ZenBook`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i5 серии ZenBook.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!4812!-#!227!#-!4634!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,5,434,62,49".

### `ASUS 14 I5 ZenBook Flip`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i5 серии ZenBook Flip.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6376!-#!227!#-!4634!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,5,434,625,49".

### `ASUS 14 I7 X409`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i7 модели X409.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6203!-#!227!#-!4635!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,6,435,654".

### `ASUS 14 I7 AsusPro`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i7 серии AsusPro.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6447!-#!227!#-!4635!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,6,435,649,54".

### `ASUS 14 I7 VivoBook`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i7 серии VivoBook.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%97%D7%A9%D7%91%D7%99%D7%9D-%D7%A0%D7%99%D7%99%D7%93%D7%99%D7%9D-ASUS#/specFilters=235m!#-!6221!-#!227!#-!4635!-#!225!#-!4662".
- `checkbox` (bool): `false`.
- `active` (bool): `true`.
- `condition` (str): "new".
- `presta_categories` (str): "3,48,10,6,435,626,49".

### `ASUS 14 I7 ZenBook`

**Описание**: Сценарий для ноутбуков ASUS 14 дюймов с процессором Intel Core i7 серии ZenBook.

**Параметры**:
- `brand` (str): "ASUS".
- `url` (str): "https://reseller.c-data.co.il/%D7%9E%D7%97%D7%A9%D7%95%D7%91-%D7%9E%D7%9