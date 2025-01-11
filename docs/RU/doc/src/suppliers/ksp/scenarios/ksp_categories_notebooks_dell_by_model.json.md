# Документация для `ksp_categories_notebooks_dell_by_model.json`

## Обзор

Файл `ksp_categories_notebooks_dell_by_model.json` содержит JSON-структуру, описывающую сценарии для сопоставления моделей ноутбуков Dell с категориями в PrestaShop. Каждый сценарий включает информацию о бренде, URL-адресе, состоянии, а также категориях PrestaShop, к которым относится модель.

## Содержание

1. [Структура JSON](#структура-json)
2. [Сценарии](#сценарии)
    - [Описание сценариев](#описание-сценариев)
    - [Пример сценария](#пример-сценария)
3. [Поля сценария](#поля-сценария)

## Структура JSON

JSON-файл имеет следующую структуру:

```json
{
  "scenarios": {
    "model_name_1": {
      "brand": "brand_name",
      "url": "url_of_product",
      "checkbox": boolean,
      "active": boolean,
      "condition": "condition_of_product",
      "presta_categories": {
        "template": {
          "brand": [ "category_1", "category_2" ]
        }
      }
    },
    "model_name_2": {
      "brand": "brand_name",
      "url": "url_of_product",
       "checkbox": boolean,
      "active": boolean,
      "condition": "condition_of_product",
      "presta_categories": {
        "template": {
          "brand": [ "category_1", "category_2" ]
        }
      }
    },
     ...
   }
}
```

## Сценарии

### Описание сценариев

Сценарии представляют собой наборы правил для сопоставления конкретных моделей ноутбуков Dell с их соответствующими категориями в PrestaShop. Каждый сценарий идентифицируется по имени модели.

### Пример сценария

```json
 "Vostro 13 5000 5301 Intel Core i5 - G": {
      "brand": "DELL",
      "url": "https://ksp.co.il/web/cat/271..132..33047..5394",
      "checkbox": false,
      "active": true,
      "condition": "new",
      "presta_categories": {
        "template": {
          "dell": [ "LAPTOPS INTEL I3", "13" ]
        }
      }
    }
```

В этом примере:
- **`Vostro 13 5000 5301 Intel Core i5 - G`** - это название модели ноутбука Dell.
- **`brand`**:  `DELL` - указывает, что это ноутбук бренда Dell.
- **`url`**: `https://ksp.co.il/web/cat/271..132..33047..5394` - URL-адрес товара.
-  **`checkbox`**: `false` - определяет, что чекбокс не выбран.
- **`active`**: `true` - указывает, что сценарий активен.
- **`condition`**: `new` - указывает, что товар является новым.
- **`presta_categories`**:  Содержит информацию о категориях PrestaShop.
   - **`template`**: содержит шаблон категорий для бренда Dell.
      - **`dell`**: `[ "LAPTOPS INTEL I3", "13" ]` - Массив категорий PrestaShop, к которым относится данная модель.

## Поля сценария

*   **`model_name`**: Ключ (название модели) идентифицирует конкретный сценарий.
*   **`brand`** (`str`): Бренд ноутбука.
*   **`url`** (`str`): URL-адрес страницы товара.
*   **`checkbox`** (`bool`):  Определяет, выбран ли чекбокс.
*   **`active`** (`bool`): Флаг, определяющий активность сценария. `true`, если сценарий активен, `false` в противном случае.
*   **`condition`** (`str`): Состояние товара (например, "new").
*   **`presta_categories`** (`dict`): Словарь, содержащий категории PrestaShop.
    *   **`template`** (`dict`): Шаблон для категорий.
        *   **`brand`** (`list`): Список категорий PrestaShop, к которым относится модель.

---