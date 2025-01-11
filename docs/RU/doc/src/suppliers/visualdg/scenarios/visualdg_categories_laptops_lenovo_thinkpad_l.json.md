# Документация для `visualdg_categories_laptops_lenovo_thinkpad_l.json`

## Обзор

Данный файл содержит JSON-конфигурацию сценариев для ноутбуков Lenovo ThinkPad L, предназначенную для использования в рамках проекта VisualDG. Каждый сценарий описывает конкретную модель ноутбука, включая его процессор (Intel i3, i5, i7, i9 или AMD), URL для получения информации, состояние (новый), а также категории PrestaShop.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
3.  [Описание сценариев](#описание-сценариев)
    -   [LENOVO THINKPAD L 13.4 - 13.3 I3](#lenovo-thinkpad-l-134---133-i3)
    -   [LENOVO THINKPAD L 13.4 - 13.3 I5](#lenovo-thinkpad-l-134---133-i5)
    -   [LENOVO THINKPAD L 13.4 - 13.3 I7](#lenovo-thinkpad-l-134---133-i7)
    -   [LENOVO THINKPAD L 13.4 - 13.3 I9](#lenovo-thinkpad-l-134---133-i9)
    -   [LENOVO THINKPAD L 13.4 - 13.3 AMD](#lenovo-thinkpad-l-134---133-amd)
    -   [LENOVO THINKPAD L 14 I3](#lenovo-thinkpad-l-14-i3)
    -   [LENOVO THINKPAD L 14 I5](#lenovo-thinkpad-l-14-i5)
    -   [LENOVO THINKPAD L 14 I7](#lenovo-thinkpad-l-14-i7)
    -   [LENOVO THINKPAD L 14 I9](#lenovo-thinkpad-l-14-i9)
    -   [LENOVO THINKPAD L 14 AMD](#lenovo-thinkpad-l-14-amd)
    -   [LENOVO THINKPAD L 15 I3](#lenovo-thinkpad-l-15-i3)
    -   [LENOVO THINKPAD L 15 I5](#lenovo-thinkpad-l-15-i5)
    -   [LENOVO THINKPAD L 15 I7](#lenovo-thinkpad-l-15-i7)
    -   [LENOVO THINKPAD L 15 I9](#lenovo-thinkpad-l-15-i9)
    -   [LENOVO THINKPAD L 15 AMD](#lenovo-thinkpad-l-15-amd)

## Структура JSON

Файл содержит корневой объект JSON с одним ключом `scenarios`, значением которого является объект, содержащий сценарии. Каждый сценарий представлен как ключ-значение, где ключ - это название сценария, а значение - объект со следующими полями:
-   `brand`: Строка, представляющая бренд ноутбука (в данном случае всегда "LENOVO").
-   `template`: Строка, представляющая шаблон модели (в данном случае всегда "THINKPAD L").
-   `url`: Строка, представляющая URL для получения информации о ноутбуке.
-   `checkbox`: Булево значение, указывающее на состояние чекбокса (всегда `false` в данном файле).
-   `active`: Булево значение, указывающее, активен ли сценарий (всегда `true` в данном файле).
-   `condition`: Строка, представляющая состояние ноутбука (всегда "new" в данном файле).
-   `presta_categories`: Строка, представляющая категории PrestaShop в виде списка ID, разделенных запятыми.

## Описание сценариев

### LENOVO THINKPAD L 13.4 - 13.3 I3

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 13.4 - 13.3 дюйма и процессором Intel i3.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "-----------------LENOVO 13.4 - 13.3 I3-------------r "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,306,9,4,370,838"

### LENOVO THINKPAD L 13.4 - 13.3 I5

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 13.4 - 13.3 дюйма и процессором Intel i5.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253273/253294"
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,306,9,5,371,838"

### LENOVO THINKPAD L 13.4 - 13.3 I7

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 13.4 - 13.3 дюйма и процессором Intel i7.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253274/253294"
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,306,9,6,372,838"

### LENOVO THINKPAD L 13.4 - 13.3 I9

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 13.4 - 13.3 дюйма и процессором Intel i9.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "----------------LENOVO THINKPAD L 13.4 - 13.3 I9------------- "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,306,9,7,373,838"

### LENOVO THINKPAD L 13.4 - 13.3 AMD

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 13.4 - 13.3 дюйма и процессором AMD.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "--------------LENOVO THINKPAD L 13.4 - 13.3 AMD--------------- "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,306,9,234,347,838"

### LENOVO THINKPAD L 14 I3

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 14 дюймов и процессором Intel i3.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "------------------------LENOVO THINKPAD L 14 I3----------------------"
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,104,10,4,377,838"

### LENOVO THINKPAD L 14 I5

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 14 дюймов и процессором Intel i5.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253273/253295"
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,104,10,5,378,838"

### LENOVO THINKPAD L 14 I7

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 14 дюймов и процессором Intel i7.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253274/253295"
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,104,10,6,379,838"

### LENOVO THINKPAD L 14 I9

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 14 дюймов и процессором Intel i9.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "----------------LENOVO THINKPAD L 14 I9------------- "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,104,10,7,380,838"

### LENOVO THINKPAD L 14 AMD

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 14 дюймов и процессором AMD.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "----------------LENOVO THINKPAD L 14 AMD------------- "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,104,10,234,381,838"

### LENOVO THINKPAD L 15 I3

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 15 дюймов и процессором Intel i3.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "----------------LENOVO THINKPAD L 15 I3------------- "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-  `presta_categories`: "3,53,105,11,4,384,838"

### LENOVO THINKPAD L 15 I5

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 15 дюймов и процессором Intel i5.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253273/253296"
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-  `presta_categories`: "3,53,105,11,5,385,838"

### LENOVO THINKPAD L 15 I7

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 15 дюймов и процессором Intel i7.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "-----------------THINKPAD L 15 I7----------------"
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-  `presta_categories`: "3,53,105,11,6,386,838"

### LENOVO THINKPAD L 15 I9

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 15 дюймов и процессором Intel i9.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "----------------LENOVO THINKPAD L 15 I9------------- "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-  `presta_categories`: "3,53,105,11,7,387,838"

### LENOVO THINKPAD L 15 AMD

**Описание**: Сценарий для ноутбука Lenovo ThinkPad L с диагональю 15 дюймов и процессором AMD.

**Параметры**:
-   `brand`: "LENOVO"
-   `template`: "THINKPAD L"
-   `url`: "----------------LENOVO THINKPAD L 15 AMD------------- "
-   `checkbox`: `false`
-   `active`: `true`
-   `condition`: "new"
-   `presta_categories`: "3,53,105,11,234,388,838"