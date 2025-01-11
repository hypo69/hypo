# Документация для `morlevi_categories_cpu.json`

## Обзор

Этот файл содержит JSON-конфигурацию для определения сценариев категорий процессоров (CPU) для поставщика Morlevi. Каждый сценарий определяет бренд, URL, активность, состояние и шаблоны категорий PrestaShop для различных моделей CPU.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Описание сценариев](#описание-сценариев)

## Структура JSON

Файл представляет собой JSON-объект с одним ключевым полем `scenarios`, которое содержит словарь, где ключами являются названия сценариев, а значениями - объекты, описывающие каждый сценарий.

```json
{
  "scenarios": {
    "Имя сценария 1": {
      "brand": "Бренд процессора",
      "url": "URL страницы с процессорами",
      "checkbox": false,
      "active": true,
      "condition": "new",
       "presta_categories": {
        "template": {
          "cpu": "Шаблон категории процессора"
        }
      }
    },
    "Имя сценария 2": {
      // ... другие сценарии
    }
  }
}
```

## Описание сценариев

### `Intel  CELERON LGA1200 Gen 10`
   **Описание**: Сценарий для процессоров Intel Celeron LGA1200 10-го поколения.
   
   **Параметры**:
   - `brand`: "INTEL"
   - `url`: "https://www.morlevi.co.il/Cat/337?p_134=584&sort=datafloat2%2Cprice&keyword="
   - `checkbox`: `false`
   - `active`: `true`
   - `condition`: "new"
   - `presta_categories`:
        - `template`:
            - `cpu`: "INTEL CELERON LGA1200"
    
### `Intel  CELERON LGA1200 Gen 11`
   **Описание**: Сценарий для процессоров Intel Celeron LGA1200 11-го поколения.
    
   **Параметры**:
   - `brand`: "INTEL"
   - `url`: "https://www.morlevi.co.il/Cat/363?p_134=584&sort=datafloat2%2Cprice&keyword="
   - `checkbox`: `false`
   - `active`: `true`
   - `condition`: "new"
   - `presta_categories`:
        - `template`:
            - `cpu`: "INTEL CELERON LGA1200"

### `Intel  PENTIUM LGA1200 Gen 10`
   **Описание**: Сценарий для процессоров Intel Pentium LGA1200 10-го поколения.
   
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/337?p_134=585&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
             - `cpu`: "INTEL PENTIUM LGA1200"

### `I3 LGA1200`
   **Описание**: Сценарий для процессоров Intel Core i3 LGA1200.
   
   **Параметры**:
   - `brand`: "INTEL"
   - `url`: "https://www.morlevi.co.il/Cat/337?p_134=586&sort=datafloat2%2Cprice&keyword="
   - `checkbox`: `false`
   - `active`: `true`
   - `condition`: "new"
   - `presta_categories`:
        - `template`:
            - `cpu`: "I3 LGA1200"

### `I5 LGA1200`
   **Описание**: Сценарий для процессоров Intel Core i5 LGA1200.
   
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/399?p_134=587&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I5 LGA1200"

### `I5 LGA1200 11`
   **Описание**: Сценарий для процессоров Intel Core i5 LGA1200 11-го поколения.
    
   **Параметры**:
   - `brand`: "INTEL"
   - `url`: "https://www.morlevi.co.il/Cat/363?p_134=587&sort=datafloat2%2Cprice&keyword="
   - `checkbox`: `false`
   - `active`: `true`
   - `condition`: "new"
   - `presta_categories`:
        - `template`:
            - `cpu`: "I5 LGA1200"

### `I5 LGA1700 12`
   **Описание**: Сценарий для процессоров Intel Core i5 LGA1700 12-го поколения.
   
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/380?p_134=587&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I5 LGA1700"

### `I5 LGA1700 13`
   **Описание**: Сценарий для процессоров Intel Core i5 LGA1700 13-го поколения.
   
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/399"
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I5 LGA1700"
 
### `I7 LGA1200`
    **Описание**: Сценарий для процессоров Intel Core i7 LGA1200.
   
    **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/399?p_134=588&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I7 LGA1200"

### `I7 LGA1200 11`
   **Описание**: Сценарий для процессоров Intel Core i7 LGA1200 11-го поколения.
    
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/363?p_134=588&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I7 LGA1200"
  
### `I7 LGA1700 12`
   **Описание**: Сценарий для процессоров Intel Core i7 LGA1700 12-го поколения.
    
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/380?p_134=588&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I7 LGA1700"
 
### `I7 LGA1700 13`
    **Описание**: Сценарий для процессоров Intel Core i7 LGA1700 13-го поколения.
    
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/399"
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I7 LGA1700"
 
### `I9 LGA1200`
   **Описание**: Сценарий для процессоров Intel Core i9 LGA1200.
    
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/399?p_134=588&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I7 LGA1200"
  
### `I9 LGA1700 12`
   **Описание**: Сценарий для процессоров Intel Core i9 LGA1700 12-го поколения.
    
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/380"
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I9 LGA1700"

### `I9 LGA1700 13`
    **Описание**: Сценарий для процессоров Intel Core i9 LGA1700 13-го поколения.
   
   **Параметры**:
    - `brand`: "INTEL"
    - `url`: "https://www.morlevi.co.il/Cat/399?p_134=848&sort=datafloat2%2Cprice&keyword="
    - `checkbox`: `false`
    - `active`: `true`
    - `condition`: "new"
    - `presta_categories`:
        - `template`:
            - `cpu`: "I9 LGA1700"