# Документация для `cdata_categories_keyboards.json`

## Обзор

Этот файл содержит JSON-объект, описывающий сценарии для категорий клавиатур и мышей. Каждый сценарий включает информацию о бренде, URL, чекбоксе, активности, состоянии и категориях PrestaShop.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Сценарии](#сценарии)
   - [MICROSOFT WIRELESS KEYBOARD](#microsoft-wireless-keyboard)
   - [MICROSOFT USB KEYBOARD](#microsoft-usb-keyboard)
   - [MICROSOFT USB MOUSE](#microsoft-usb-mouse)
   - [MICROSOFT WIRELESS MOUSE](#microsoft-wireless-mouse)
   - [MICROSOFT USB KEYBOARD-MOUSE SET](#microsoft-usb-keyboard-mouse-set)
   - [MICROSOFT WIRELESS KEYBOARD-MOUSE SET](#microsoft-wireless-keyboard-mouse-set)
   - [ASUS WIRELESS KEYBOARD](#asus-wireless-keyboard)
   - [ASUS USB KEYBOARD](#asus-usb-keyboard)
   - [ASUS USB MOUSE](#asus-usb-mouse)
   - [ASUS WIRELESS MOUSE](#asus-wireless-mouse)
   - [ASUS USB KEYBOARD-MOUSE SET](#asus-usb-keyboard-mouse-set)
   - [ASUS WIRELESS SET](#asus-wireless-set)

## Структура JSON

JSON-объект состоит из одного ключа `scenarios`, значением которого является словарь. Каждый ключ словаря представляет собой название сценария, а значение - словарь с деталями этого сценария.

## Сценарии

### `MICROSOFT WIRELESS KEYBOARD`

**Описание**: Сценарий для беспроводной клавиатуры Microsoft.

**Параметры**:
- `brand` (str): Значение `"MICROSOFT"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,204,316"`.

### `MICROSOFT USB KEYBOARD`

**Описание**: Сценарий для USB-клавиатуры Microsoft.

**Параметры**:
- `brand` (str): Значение `"MICROSOFT"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,204,315"`.

### `MICROSOFT USB MOUSE`

**Описание**: Сценарий для USB-мыши Microsoft.

**Параметры**:
- `brand` (str): Значение `"MICROSOFT"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,206,317"`.

### `MICROSOFT WIRELESS MOUSE`

**Описание**: Сценарий для беспроводной мыши Microsoft.

**Параметры**:
- `brand` (str): Значение `"MICROSOFT"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,206,318"`.

### `MICROSOFT USB KEYBOARD-MOUSE SET`

**Описание**: Сценарий для набора USB-клавиатуры и мыши Microsoft.

**Параметры**:
- `brand` (str): Значение `"MICROSOFT"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,207,208"`.

### `MICROSOFT WIRELESS KEYBOARD-MOUSE SET`

**Описание**: Сценарий для набора беспроводной клавиатуры и мыши Microsoft.

**Параметры**:
- `brand` (str): Значение `"MICROSOFT"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,207,334"`.

### `ASUS WIRELESS KEYBOARD`

**Описание**: Сценарий для беспроводной клавиатуры ASUS.

**Параметры**:
- `brand` (str): Значение `"ASUS"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,204,316"`.

### `ASUS USB KEYBOARD`

**Описание**: Сценарий для USB-клавиатуры ASUS.

**Параметры**:
- `brand` (str): Значение `"ASUS"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,204,315"`.

### `ASUS USB MOUSE`

**Описание**: Сценарий для USB-мыши ASUS.

**Параметры**:
- `brand` (str): Значение `"ASUS"`.
- `url` (str): Заполнитель.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,206,317"`.

### `ASUS WIRELESS MOUSE`

**Описание**: Сценарий для беспроводной мыши ASUS.

**Параметры**:
- `brand` (str): Значение `"ASUS"`.
- `url` (str): Заполнитель.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,206,318"`.

### `ASUS USB KEYBOARD-MOUSE SET`

**Описание**: Сценарий для набора USB-клавиатуры и мыши ASUS.

**Параметры**:
- `brand` (str): Значение `"ASUS"`.
- `url` (str): Заполнитель.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,207,208"`.

### `ASUS WIRELESS SET`

**Описание**: Сценарий для беспроводного набора ASUS.

**Параметры**:
- `brand` (str): Значение `"ASUS"`.
- `url` (str): URL-адрес товара на сайте C-Data.
- `checkbox` (bool): Значение `false`.
- `active` (bool): Значение `true`.
- `condition` (str): Значение `"new"`.
- `presta_categories` (str): Значение `"203,207,334"`.