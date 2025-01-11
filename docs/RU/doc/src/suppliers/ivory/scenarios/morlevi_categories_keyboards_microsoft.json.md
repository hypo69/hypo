# Документация для `morlevi_categories_keyboards_microsoft.json`

## Обзор

Данный файл содержит JSON-конфигурацию для определения соответствия между категориями товаров Microsoft и категориями PrestaShop для поставщика Morlevi. Он определяет сценарии для различных типов клавиатур и мышей Microsoft, указывая бренды, URL-адреса, настройки активации, состояния товаров и соответствующие категории PrestaShop.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
  - [Сценарии](#сценарии)
    - [MICROSOFT WIRELESS KEYBOARD](#microsoft-wireless-keyboard)
    - [MICROSOFT USB KEYBOARD](#microsoft-usb-keyboard)
    - [MICROSOFT USB MOUSE](#microsoft-usb-mouse)
    - [MICROSOFT WIRELESS MOUSE](#microsoft-wireless-mouse)
    - [MICROSOFT USB KEYBOARD-MOUSE SET](#microsoft-usb-keyboard-mouse-set)
    - [MICROSOFT WIRELESS KEYBOARD-MOUSE SET](#microsoft-wireless-keyboard-mouse-set)

## Структура JSON

### Сценарии

JSON-объект содержит ключ `"scenarios"`, который является словарем, где ключи представляют собой названия сценариев, а значения - детализированные настройки для каждого сценария.

#### `MICROSOFT WIRELESS KEYBOARD`

**Описание**: Настройки для беспроводной клавиатуры Microsoft.

**Параметры**:
- `"brand"` (str): `"MICROSOFT"`.
- `"url"` (str): `"-----------------------------------------------MICROSOFT WIRELESS KEYBOARD----------------------------------------------"`.
- `"checkbox"` (bool): `false`.
- `"active"` (bool): `true`.
- `"condition"` (str): `"new"`.
- `"presta_categories"` (str): `"203,204,316"`.

#### `MICROSOFT USB KEYBOARD`

**Описание**: Настройки для USB клавиатуры Microsoft.

**Параметры**:
- `"brand"` (str): `"MICROSOFT"`.
- `"url"` (str): `"https://www.morlevi.co.il/Cat/155?p_315=42&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"` (bool): `false`.
- `"active"` (bool): `true`.
- `"condition"` (str): `"new"`.
- `"presta_categories"` (str): `"203,204,315"`.

#### `MICROSOFT USB MOUSE`

**Описание**: Настройки для USB мыши Microsoft.

**Параметры**:
- `"brand"` (str): `"MICROSOFT"`.
- `"url"` (str): `"------------------------------------------------------MICROSOFT USB MOUSE------------------------------------------------"`.
- `"checkbox"` (bool): `false`.
- `"active"` (bool): `true`.
- `"condition"` (str): `"new"`.
- `"presta_categories"` (str): `"203,206,317"`.

#### `MICROSOFT WIRELESS MOUSE`

**Описание**: Настройки для беспроводной мыши Microsoft.

**Параметры**:
- `"brand"` (str): `"MICROSOFT"`.
- `"url"` (str): `"https://www.morlevi.co.il/Cat/109?p_315=42&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"` (bool): `false`.
- `"active"` (bool): `true`.
- `"condition"` (str): `"new"`.
- `"presta_categories"` (str): `"203,206,318"`.

#### `MICROSOFT USB KEYBOARD-MOUSE SET`

**Описание**: Настройки для набора USB клавиатура-мышь Microsoft.

**Параметры**:
- `"brand"` (str): `"MICROSOFT"`.
- `"url"` (str): `"https://www.morlevi.co.il/Cat/113?p_315=42&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"` (bool): `false`.
- `"active"` (bool): `true`.
- `"condition"` (str): `"new"`.
- `"presta_categories"` (str): `"203,207,208"`.

#### `MICROSOFT WIRELESS KEYBOARD-MOUSE SET`

**Описание**: Настройки для набора беспроводная клавиатура-мышь Microsoft.

**Параметры**:
- `"brand"` (str): `"MICROSOFT"`.
- `"url"` (str): `"https://www.morlevi.co.il/Cat/114?p_315=42&sort=datafloat2%2Cprice&keyword="`.
- `"checkbox"` (bool): `false`.
- `"active"` (bool): `true`.
- `"condition"` (str): `"new"`.
- `"presta_categories"` (str): `"203,207,334"`.