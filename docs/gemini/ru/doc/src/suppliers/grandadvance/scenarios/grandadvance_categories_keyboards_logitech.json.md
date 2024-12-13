# Файл конфигурации категорий Logitech для Grand Advance

## Обзор

Этот файл содержит конфигурацию категорий товаров Logitech для парсера Grand Advance. Он определяет соответствие между названиями категорий товаров Logitech, URL-адресами их страниц на сайте Grand Advance и идентификаторами категорий PrestaShop.

## Оглавление

- [Обзор](#обзор)
- [Структура данных](#структура-данных)
- [Описание категорий](#описание-категорий)

## Структура данных

Файл представляет собой JSON-объект, где ключами являются названия категорий товаров Logitech, а значениями - объекты со следующими полями:

- `brand` (str): Бренд товара. В данном случае всегда "LOGITECH".
- `url` (str): URL-адрес страницы со списком товаров данной категории на сайте Grand Advance.
- `checkbox` (bool): Логическое значение, по умолчанию `false`.
- `active` (bool): Логическое значение, указывающее, активна ли категория. Всегда `true`.
- `condition` (str): Состояние товара, всегда `"new"`.
- `presta_categories` (str): Строка с идентификаторами категорий PrestaShop, разделенными запятыми.

## Описание категорий

### `LOGITECH WIRELESS KEYBOARD`

**Описание**: Беспроводные клавиатуры Logitech.

**Параметры**:
- `brand`: "LOGITECH".
- `url`: `https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manId=10`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"203,204,316"`

### `LOGITECH USB KEYBOARD`

**Описание**: USB клавиатуры Logitech.

**Параметры**:
- `brand`: "LOGITECH".
- `url`: `https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=589&manId=10`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"203,204,315"`

### `LOGITECH USB MOUSE`

**Описание**: USB мыши Logitech.

**Параметры**:
- `brand`: "LOGITECH".
- `url`: `https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manId=10`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"203,206,317"`

### `LOGITECH WIRELESS MOUSE`

**Описание**: Беспроводные мыши Logitech.

**Параметры**:
- `brand`: "LOGITECH".
- `url`: `https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=586&manId=10`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"203,206,318"`

### `LOGITECH USB KEYBOARD-MOUSE SET`

**Описание**: Комплекты USB клавиатура + мышь Logitech.

**Параметры**:
- `brand`: "LOGITECH".
- `url`: `https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=10`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"203,207,208"`

### `LOGITECH WIRELESS  KEYBOARD-MOUSE SET`

**Описание**: Беспроводные комплекты клавиатура + мышь Logitech.

**Параметры**:
- `brand`: "LOGITECH".
- `url`: `https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manId=10`
- `checkbox`: `false`
- `active`: `true`
- `condition`: `"new"`
- `presta_categories`: `"203,207,334"`