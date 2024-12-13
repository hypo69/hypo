# Документация для `hypotez/src/suppliers/ksp/scenarios/ksp_categories_motherboards_msi.json`

## Оглавление

1. [Обзор](#обзор)
2. [Структура файла](#структура-файла)
3. [Сценарии](#сценарии)
   - [MSI Intel-1200 H510](#msi-intel-1200-h510)
   - [MSI Intel-1200 B460](#msi-intel-1200-b460)
   - [MSI Intel-1200 B560](#msi-intel-1200-b560)
   - [MSI Intel-1200 Z590](#msi-intel-1200-z590)
   - [MSI Intel-1700 Z690](#msi-intel-1700-z690)
   - [MSI Intel-1700 B660](#msi-intel-1700-b660)
   - [MSI Intel-1700 H670](#msi-intel-1700-h670)
   - [MSI Intel-1700 H610](#msi-intel-1700-h610)
   - [MSI AMD AM4 B550](#msi-amd-am4-b550)
   - [MSI AMD AM4 A520](#msi-amd-am4-a520)

## Обзор

Этот файл содержит JSON-конфигурацию для сценариев обработки материнских плат MSI, полученных с сайта KSP. Каждый сценарий определяет параметры для конкретной модели материнской платы, включая URL, условия, правила ценообразования и соответствие категориям PrestaShop.

## Структура файла

Файл представляет собой JSON-объект со следующей структурой:

```json
{
  "scenarios": {
    "Название сценария 1": {
      "brand": "Бренд",
      "url": "URL страницы товара",
      "checkbox": false,
      "active": true,
      "condition":"Состояние товара",
      "presta_categories": {
        "template": { "имя шаблона": "Значение шаблона" }
      },
      "price_rule": 1
    },
    "Название сценария 2": {
      ...
    },
    ...
  }
}
```

Где:

-   `scenarios`: Объект, содержащий все сценарии.
-   `Название сценария`: Ключ, представляющий уникальное имя сценария для конкретной материнской платы.
-   `brand`: Строка, указывающая бренд (например, "MSI").
-   `url`: Строка, содержащая URL страницы товара на сайте KSP.
-   `checkbox`: Булево значение, определяющее состояние чекбокса (обычно `false`).
-   `active`: Булево значение, определяющее активность сценария (`true` для активных).
-   `condition`: Строка, указывающая состояние товара (например, "new").
-   `presta_categories`: Объект, содержащий настройки категорий PrestaShop.
    -   `template`: Объект, содержащий соответствия между внутренними именами и шаблонами категорий PrestaShop.
-   `price_rule`: Число, определяющее правило ценообразования.

## Сценарии

### `MSI Intel-1200 H510`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel H510 для сокета 1200.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..23877"`
-   `checkbox`: `false`
-   `active`: `true`
-  `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1200 H510"}`
-   `price_rule`: `1`

### `MSI Intel-1200 B460`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel B460 для сокета 1200.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..12539..13374"`
-   `checkbox`: `false`
-   `active`: `true`
-  `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1200 B460"}`
-   `price_rule`: `1`

### `MSI Intel-1200 B560`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel B560 для сокета 1200.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..12539..23315"`
-   `checkbox`: `false`
-   `active`: `true`
-  `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1200 B560"}`
-   `price_rule`: `1`

### `MSI Intel-1200 Z590`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel Z590 для сокета 1200.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..12539..21824"`
-   `checkbox`: `false`
-   `active`: `true`
-  `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1200 Z590"}`
-   `price_rule`: `1`

### `MSI Intel-1700 Z690`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel Z690 для сокета 1700.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..29757..29759"`
-   `checkbox`: `false`
-   `active`: `true`
-  `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1700 Z690"}`
-   `price_rule`: `1`

### `MSI Intel-1700 B660`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel B660 для сокета 1700.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..29757..31871"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1700 B660"}`
-   `price_rule`: `1`

### `MSI Intel-1700 H670`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel H670 для сокета 1700.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..29757..31871"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1700 H670"}`
-   `price_rule`: `1`

### `MSI Intel-1700 H610`

**Описание**: Сценарий для материнских плат MSI на чипсете Intel H610 для сокета 1700.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..52..29757..32570"`
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "INTEL 1700 H610"}`
-   `price_rule`: `1`

### `MSI AMD AM4 B550`

**Описание**: Сценарий для материнских плат MSI на чипсете AMD B550 для сокета AM4.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..202..3951..13789"`
-   `checkbox`: `false`
-   `active`: `true`
-  `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "AMD AM4 B550"}`
-   `price_rule`: `1`

### `MSI AMD AM4 A520`

**Описание**: Сценарий для материнских плат MSI на чипсете AMD A520 для сокета AM4.

**Параметры**:

-   `brand`: `"MSI"`
-   `url`: `"https://ksp.co.il/web/cat/47..3..202..3951..14715"`
-   `checkbox`: `false`
-   `active`: `true`
-  `condition`: `"new"`
-   `presta_categories`:
    -   `template`: `{"msi": "AMD AM4 A520"}`
-   `price_rule`: `1`