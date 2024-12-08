```MD
# Анализ кода: Инструкции для Gemini AI по сборке компьютера

## 1. <input code>

```
## **Prompt for Gemini AI: Assembling a Computer**

### **Prompt Description**

#### **Role:**  
Computer Builder Assistant  

#### **Task:**  
You will receive input data in **Hebrew**. This data will contain information about computer components in JSON format. Your responsibilities include:  

1. **Translate all provided data** from Hebrew into the target language specified in the instructions.  
2. **Determine the build type** (e.g., gaming, office, workstation, etc.) based on the components.  
3. **Generate a descriptive title and detailed description** of the build in the target language.  
4. **Translate all component names and descriptions** into the target language.  
5. **Return the response** as a JSON dictionary in the exact structure specified in the command instructions.  
6. **Ensure correct formatting** of all quotation marks and JSON structure.  

---

In this prompt, the words `product` and `component` are synonyms  
and refer to a component for assembling a computer.

---

### **Input Format:** JSON  

**Example Input:**
```json
[
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description or specs>",
    "specification": "<specs>",
    "image_local_saved_path": "<leave as is>"
  },
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description or specs>",
    "specification": "<specs>",
    "image_local_saved_path": "<leave as is>"
  },
  <other components>
]
```

---

### **Output Format:** JSON  

You must return the JSON dictionary as specified in the command instructions. Below is a **template** for generating output in a single language.  

**Example Output:**
```json
{
  "language_code": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "Your generated build title in the target language",
    "description": "Your generated build description in the target language",
    "products": [
      {
        "product_id": "<leave as is from input data>",
        "product_title": "Translated product name in the target language",
        "product_description": "Translated product description in the target language. If you cannot create a specification, leave this field empty.",
        "specification": "Translated specification in the target language. If you cannot create a specification, leave this field empty.",
        "image_local_saved_path": "<leave as is from input data>"
      },
      <other components>
    ]
  }
}
```

---

... (rest of the prompt)
```

## 2. <algorithm>

**Пошаговая блок-схема:**

1. **Получение входных данных:** Принимает JSON массив с описанием компонентов компьютера (на иврите).
2. **Перевод:** Преобразует все данные с иврита на целевой язык.
3. **Анализ компонентов:** Определяет тип сборки (гейминг, рабочая станция и т.д.) на основе характеристик компонентов.
4. **Генерация заголовка и описания:** Создает заголовок и подробное описание сборки на целевом языке.
5. **Перевод компонентов:** Переводит названия и описания компонентов на целевой язык.
6. **Формирование JSON:** Формирует JSON ответ в заданном формате, включая вероятности типов сборок.
7. **Возврат результата:** Возвращает сформированный JSON ответ.


**Примеры:**

* **Вход:** JSON данные о компонентах на иврите.
* **Перевод:** JSON данные о компонентах на английском.
* **Анализ:** На основе компонентов определяется тип сборки - гейминг.
* **Генерация:** Заголовок "Высокопроизводительный игровой ПК", описание с характеристиками компонентов.
* **Вывод:** JSON в формате `UTF-8`.


## 3. <mermaid>

```mermaid
graph TD
    A[Ввод JSON (иврит)] --> B{Перевод на целевой язык};
    B --> C[Анализ компонентов];
    C --> D[Определение типа сборки];
    D --> E[Генерация заголовка и описания];
    E --> F[Перевод компонентов];
    F --> G[Формирование JSON];
    G --> H[Возврат JSON (UTF-8)];
```

**Объяснение зависимостей:**

Диаграмма показывает последовательность шагов. Зависимость между шагами заключается в том, что результат одного шага используется на следующем. Например, переведенные данные используются для анализа компонентов, а анализ для определения типа сборки.

## 4. <explanation>

**Импорты:**  Нет импортов, так как это не код программы, а инструкция. Инструкция описывает, как должен работать AI, и как он должен получать и обрабатывать данные.


**Классы:** Нет классов, это структура документации.


**Функции:**  Нет функций, нет фрагментов кода.  Это описание процесса работы программы.


**Переменные:** Нет переменных. Входные данные и вывод представляются в виде данных JSON.


**Возможные ошибки или области для улучшений:**

* **Не определен язык перевода:** Не указан язык, на который нужно переводить.
* **Не указан способ анализа компонентов:** Не указаны алгоритмы для определения типа сборки.
* **Не определено, как обрабатываются ошибки:**  Что делать с неполными данными или с неразрешимыми проблемами.


**Цепочка взаимосвязей с другими частями проекта:**

Инструкция описывает интерфейс для Gemini AI.  Взаимосвязь с другими частями проекта (например, с обработкой JSON или с инструментами перевода) неясна, так как инструкция сама по себе является описанием требований.