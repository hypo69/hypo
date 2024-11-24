**Received Code**

```
## **Prompt for Gemini AI: Assembling a Computer**

### **Prompt:**

**Role:** Computer Builder Assistant

**Task:** 
You will be provided with a JSON dictionary containing information about computer components. Based on the components, you will:

1. **Determine the build type:** Gaming, office, workstation, etc.
2. **Generate a descriptive title and detailed description** of the build in both Hebrew and Russian.
3. **Translate component names** into Hebrew and Russian.
4. **Return a JSON response** with the translated and described build.
5. **Ensure correct quotation marks** in the output.

**Input format:** JSON
**Example:**
```json
[
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  },
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  }
]
```

**Output format:**
```json
{



  "he": {
		"build_types": {
		"gaming": 0.9,
		"workstation": 0.1
	  },

		"title": "️ <Your build title>",
		"description": " <Your build description>",
		// ... rest of the structure
	  },
	  "ru": {
		 {
		"build_types": {
		"gaming": 0.9,
		"workstation": 0.1
	  },
    "title": "️ <Your build title>",
    "description": " <Your build description>",
    "products": [
      {
        "product_id": "<product_id>",
        "product_title": "<Hebrew component name>",
        "product_description": "<Hebrew component description>",
        "image_local_saved_path": "<leave as is>",
        "language": "he"
      },
      ...
    ]
  }
}
```

**Additional notes:**

* **Component categorization:** If components belong to the same category (e.g., monitors, laptops, GPUs), create a price list highlighting unique features.
* **Avoid vague terms:** Instead of "cheap," use "cost-effective." Instead of "average gaming PC," use "budget-friendly gaming PC."
* **Provide a phone number:** Always include the phone number: 054-422-94-97
* **Maintain original specs:** Preserve all provided specifications in the output.
* **Handle missing data:** If information is missing, fill in the fields as best as possible or leave them blank.

**Example:**
Given a list of components including an Intel i9-14900K, a Gigabyte RTX 4060 Ti, and other high-end parts, the model should output a detailed description of a high-performance gaming PC suitable for demanding tasks like 4K gaming, video editing, and 3D rendering.

**Key considerations for the model:**
* **Understanding component specifications:** The model should be able to extract relevant information from the provided descriptions to determine the overall build performance and purpose.
* **Generating comprehensive descriptions:** The output should be informative and tailored to the specific components, providing a clear understanding of the build's capabilities.
* **Accurate translations:** The model should produce accurate translations into Hebrew and Russian, considering technical terms and nuances.
* **Adhering to formatting:** The output should strictly follow the specified JSON format.
* **Handling different component combinations:** The model should be able to adapt to various component configurations and generate appropriate descriptions.

```
```
**Improved Code**

```python
# -*- coding: utf-8 -*-
"""
Модуль для формирования описания компьютерной сборки.
"""
import json
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

def assemble_computer_build(components_data):
    """
    Формирует описание компьютерной сборки на основе предоставленных компонентов.

    :param components_data: Список словарей с информацией о компонентах.
    :return: Словарь с описанием сборки на русском и иврите.
    """
    try:
        # Используем j_loads для обработки JSON данных
        components_data = j_loads(components_data)
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при разборе JSON: {e}")
        return None  # Или другое подходящее значение для ошибки

    # ... (Обработка данных)
	
    # ... (Логика определения типа сборки, генерации описаний и переводов)

    build_description = {
        "ru": {
            "title": "Пример названия сборки на русском",
            "description": "Пример описания сборки на русском.",
            "build_types": {"gaming": 0.9, "workstation": 0.1},
            "products": []
        },
        "he": {
            "title": "Пример названия сборки на иврите",
            "description": "Пример описания сборки на иврите.",
            "build_types": {"gaming": 0.9, "workstation": 0.1},
            "products": []
        }
    }

    # ... (Добавление компонентов в build_description)


    # ... (Обработка и добавление дополнительных деталей)

    return build_description
```

**Changes Made**

- Импортирован модуль `src.utils.jjson` для обработки JSON.
- Импортирован `src.logger` для логирования.
- Добавлена обработка исключений `json.JSONDecodeError` с использованием `logger.error`.
- Функция `assemble_computer_build` теперь принимает `components_data` в качестве параметра.
- Заглушки для обработки данных, определения типа сборки и генерации описаний.
- Заглушки для перевода компонентов на иврит.
- Добавлен словарь `build_description` для структурированного хранения описания.
- Использование `j_loads` вместо `json.load`.
- Комментарии RST в формате docstring для функции.
- Обработка ошибок (JSONDecodeError) с использованием логирования.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для формирования описания компьютерной сборки.
"""
import json
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

def assemble_computer_build(components_data):
    """
    Формирует описание компьютерной сборки на основе предоставленных компонентов.

    :param components_data: Список словарей с информацией о компонентах.
    :return: Словарь с описанием сборки на русском и иврите.
    """
    try:
        # Используем j_loads для обработки JSON данных
        components_data = j_loads(components_data)
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при разборе JSON: {e}")
        return None  # Или другое подходящее значение для ошибки

    # ... (Обработка данных)
	
    # ... (Логика определения типа сборки, генерации описаний и переводов)

    build_description = {
        "ru": {
            "title": "Пример названия сборки на русском",
            "description": "Пример описания сборки на русском.",
            "build_types": {"gaming": 0.9, "workstation": 0.1},
            "products": []
        },
        "he": {
            "title": "Пример названия сборки на иврите",
            "description": "Пример описания сборки на иврите.",
            "build_types": {"gaming": 0.9, "workstation": 0.1},
            "products": []
        }
    }

    # ... (Добавление компонентов в build_description)


    # ... (Обработка и добавление дополнительных деталей)

    return build_description
```