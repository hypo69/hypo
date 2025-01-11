# Документация для `morlevi_categories_keyboards_microsoft.json`

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание полей](#описание-полей)

## Обзор

Этот JSON-файл содержит конфигурацию для категорий товаров, связанных с брендом "MICROSOFT" в контексте клавиатур и мышей. Файл определяет различные типы товаров Microsoft, их URL-адреса, а также соответствия категориям PrestaShop.

## Структура JSON

Файл представляет собой JSON-объект, содержащий один ключ `"scenarios"`, значением которого является объект, в котором ключами являются названия категорий товаров (например, "MICROSOFT WIRELESS KEYBOARD"), а значениями являются объекты с описанием этих категорий.

## Описание полей

Каждый объект в `"scenarios"` имеет следующие поля:

- `brand` (str): Название бренда товара, всегда "MICROSOFT".
- `url` (str): URL-адрес страницы категории товара на сайте поставщика.
- `checkbox` (bool): Логическое значение, указывающее на состояние чекбокса. (Всегда `false` в данном файле)
- `active` (bool): Логическое значение, указывающее на активность категории. (Всегда `true` в данном файле)
- `condition` (str): Состояние товара, всегда "new".
- `presta_categories` (str): Строка, представляющая список идентификаторов категорий PrestaShop, разделенных запятыми.

### Примеры категорий

#### `MICROSOFT WIRELESS KEYBOARD`
- **Описание**: Беспроводная клавиатура Microsoft.
- **url**:  "-----------------------------------------------MICROSOFT WIRELESS KEYBOARD----------------------------------------------"
- **presta_categories**: "203,204,316"

#### `MICROSOFT USB KEYBOARD`
- **Описание**: Проводная клавиатура Microsoft с USB-подключением.
- **url**: `https://www.morlevi.co.il/Cat/155?p_315=42&sort=datafloat2%2Cprice&keyword=`
- **presta_categories**: "203,204,315"

#### `MICROSOFT USB MOUSE`
- **Описание**: Проводная мышь Microsoft с USB-подключением.
- **url**:  "------------------------------------------------------MICROSOFT USB MOUSE------------------------------------------------"
- **presta_categories**: "203,206,317"

#### `MICROSOFT WIRELESS MOUSE`
- **Описание**: Беспроводная мышь Microsoft.
- **url**: `https://www.morlevi.co.il/Cat/109?p_315=42&sort=datafloat2%2Cprice&keyword=`
- **presta_categories**: "203,206,318"

#### `MICROSOFT USB KEYBOARD-MOUSE SET`
- **Описание**: Комплект из проводной клавиатуры и мыши Microsoft с USB-подключением.
- **url**: `https://www.morlevi.co.il/Cat/113?p_315=42&sort=datafloat2%2Cprice&keyword=`
- **presta_categories**: "203,207,208"

#### `MICROSOFT WIRELESS KEYBOARD-MOUSE SET`
- **Описание**: Комплект из беспроводной клавиатуры и мыши Microsoft.
- **url**: `https://www.morlevi.co.il/Cat/114?p_315=42&sort=datafloat2%2Cprice&keyword=`
- **presta_categories**: "203,207,334"