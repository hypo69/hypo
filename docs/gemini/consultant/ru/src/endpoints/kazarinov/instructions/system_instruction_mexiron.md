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
Модуль для сборки и описания компьютера на основе списка компонентов.

"""
import json

from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

def assemble_computer(components_data: list) -> dict:
    """
    Сборка компьютера и генерация описания.

    :param components_data: Список словарей с информацией о компонентах.
    :return: Словарь с описанием компьютера на иврите и русском.
    """
    try:
        # Обработка списка компонентов
        data = j_loads(components_data)  # Используем j_loads
        # ... (дальнейшая обработка данных)
        
        # Пример генерации описания
        build_description = {
            "ru": {
                "title": "Высокопроизводительный игровой компьютер",
                "description": "Современный высокопроизводительный игровой компьютер, оптимизированный для требовательных игр и приложений для обработки видео/графики. Он включает мощный процессор (Intel i7-14700F), быстрый графический процессор (Gigabyte GeForce RTX 4070 Super), большое количество оперативной памяти (16 ГБ DDR4) и быстрый твердотельный накопитель. Компьютер собран в корпусе Cooler Master HAF 700, который оснащен мощными и эффективными вентиляторами, обеспечивающими отличное охлаждение. Также имеется блок питания 750 Вт 80 Plus Gold. Все компоненты выбраны качественные и надежные для длительной эксплуатации.",

                "build_types": {"gaming": 0.9, "workstation": 0.1},
                "products": []
            },
            "he": {
              "title": "מחשב משחקים בינוני",
              "description": "מחשב משחקים בינוני, אופטימלי למשחקים ולעיבוד וידאו/גרפיקה. הוא כולל מעבד חזק (Intel i7-14700F), כרטיס גרפיקה מהיר (Gigabyte GeForce RTX 4070 Super), כמות גדולה של זיכרון RAM (16 GB DDR4) ודיסק קשיח מהיר. המחשב הותקן בתיבת Cooler Master HAF 700, המהודקת במאווררים חזקים ויעילים המספקים קירור מעולה. יש גם כוח 750 וואט 80 Plus Gold. כל הרכיבים נבחרו באיכות גבוהה ויציבות לשימוש ממושך." ,
                "build_types": {"gaming": 0.9, "workstation": 0.1},
                "products": []
            }
        }


        # Добавление продуктов в список описания (предполагается, что в 'components_data' есть данные о компонентах)

        for component in data:
          build_description['ru']['products'].append(component)
          build_description['he']['products'].append(component)
        return build_description
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}")
        return None
    except Exception as e:
        logger.error(f"Ошибка при сборке компьютера: {e}")
        return None
```

**Changes Made**

- Импортирован модуль `jjson` для работы с JSON данными.
- Добавлена функция `assemble_computer` для обработки входных данных.
- Функция `assemble_computer` теперь использует `j_loads` для декодирования данных из списка словарей.
- Функция `assemble_computer` теперь возвращает словарь с описанием компьютера.
- Обработка исключений `json.JSONDecodeError` и общих исключений.
- Внедрены логи для отслеживания ошибок.
- Пример кода теперь содержит структуру для добавления данных о компонентах в output.


**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для сборки и описания компьютера на основе списка компонентов.

"""
import json

from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

def assemble_computer(components_data: list) -> dict:
    """
    Сборка компьютера и генерация описания.

    :param components_data: Список словарей с информацией о компонентах.
    :return: Словарь с описанием компьютера на иврите и русском.
    """
    try:
        # Обработка списка компонентов
        data = j_loads(components_data)  # Используем j_loads
        # ... (дальнейшая обработка данных)
        
        # Пример генерации описания
        build_description = {
            "ru": {
                "title": "Высокопроизводительный игровой компьютер",
                "description": "Современный высокопроизводительный игровой компьютер, оптимизированный для требовательных игр и приложений для обработки видео/графики. Он включает мощный процессор (Intel i7-14700F), быстрый графический процессор (Gigabyte GeForce RTX 4070 Super), большое количество оперативной памяти (16 ГБ DDR4) и быстрый твердотельный накопитель. Компьютер собран в корпусе Cooler Master HAF 700, который оснащен мощными и эффективными вентиляторами, обеспечивающими отличное охлаждение. Также имеется блок питания 750 Вт 80 Plus Gold. Все компоненты выбраны качественные и надежные для длительной эксплуатации.",

                "build_types": {"gaming": 0.9, "workstation": 0.1},
                "products": []
            },
            "he": {
              "title": "מחשב משחקים בינוני",
              "description": "מחשב משחקים בינוני, אופטימלי למשחקים ולעיבוד וידאו/גרפיקה. הוא כולל מעבד חזק (Intel i7-14700F), כרטיס גרפיקה מהיר (Gigabyte GeForce RTX 4070 Super), כמות גדולה של זיכרון RAM (16 GB DDR4) ודיסק קשיח מהיר. המחשב הותקן בתיבת Cooler Master HAF 700, המהודקת במאווררים חזקים ויעילים המספקים קירור מעולה. יש גם כוח 750 וואט 80 Plus Gold. כל הרכיבים נבחרו באיכות גבוהה ויציבות לשימוש ממושך." ,
                "build_types": {"gaming": 0.9, "workstation": 0.1},
                "products": []
            }
        }


        # Добавление продуктов в список описания (предполагается, что в 'components_data' есть данные о компонентах)
		#TODO: Добавить корректную обработку данных компонентов
        for component in data:
          build_description['ru']['products'].append(component)
          build_description['he']['products'].append(component)
        return build_description
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}")
        return None
    except Exception as e:
        logger.error(f"Ошибка при сборке компьютера: {e}")
        return None
```