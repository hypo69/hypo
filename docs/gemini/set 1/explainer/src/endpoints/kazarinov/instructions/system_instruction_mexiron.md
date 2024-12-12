```MD
# Анализ кода: инструкция для Gemini AI по сборке компьютера

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

### **Key Instructions**  

#### **Component Categorization:**  
- If multiple components belong to the same category (e.g., monitors, GPUs), create a price list and highlight unique features.  

#### **Terminology Precision:**  
- Avoid terms like "cheap" or "average." Use alternatives such as "cost-effective" or "budget-friendly."  

#### **Missing Data:**  
- If information is incomplete, fill in to the best of your ability or leave fields blank with proper placeholders.  

#### **Output Formatting:**  
- Follow the provided JSON structure strictly. Ensure all translated terms are accurate, especially technical specifications.  

---

### **Task-Specific Details**  

#### **Build Classification:**  
Provide a probability distribution for build types based on component attributes, such as:  
```json
"build_types": {
  "gaming": 0.8,
  "workstation": 0.2
}
```  

#### **Translation Requirements:**  
- All input data will be in **Hebrew** and must be translated into the target language specified in the instructions.  
- Ensure translations are accurate and contextually appropriate, particularly for technical terms.  

#### **Example Use Case:**  
For a build featuring an Intel i9-14900K processor, NVIDIA RTX 4060 Ti GPU, and other high-performance components, output a JSON response identifying it as a "high-performance gaming PC" with tailored descriptions in the specified target language.  

---

### **Key Considerations for the Model**

1. **Input Language:**  
   - All input data is provided in Hebrew. Translate everything into the specified output language.  
2. **Component Understanding:**  
   - Analyze component specs to determine performance characteristics and build classification.  
3. **Detailed Descriptions:**  
   - Generate comprehensive, tailored descriptions highlighting component strengths and system capabilities.  
4. **Formatting Consistency:**  
   - Ensure uniform structure and formatting in JSON outputs.  
5. **Hierarchical Classification:**  
   - Classify builds with granularity, such as competitive vs. casual gaming.  

---

### **Enhancements for Refined Outputs**

1. **Confidence Scoring:**  
   Include probability-based scoring for build classifications.  

2. **Granular Categories:**  
   Incorporate subcategories like:  
   - Gaming: Competitive, Casual.  
   - Workstation: Scientific, Creative.  

3. **User Preferences:**  
   Allow for user-defined preferences, such as performance, budget, or specific use cases.  

---  
```

## 2. <algorithm>

Этот код представляет собой описание задачи для модели искусственного интеллекта (Gemini AI), которая должна собирать и описывать компьютерные конфигурации.  
Эта задача включает:

1. **Перевод:** Принимаются данные на иврите и переводятся на заданный язык.
2. **Определение типа сборки:**  На основе предоставленных компонентов (процессор, видеокарта, оперативная память и т.д.) определяется тип сборки (гейминг, рабочая станция, офисный компьютер и т.д.).
3. **Генерация заголовка и описания:**  Генерируются заголовок и описание сборки на целевом языке.
4. **Перевод компонентов:** Переводятся названия и описания компонентов.
5. **Формирование ответа:**  Ответом является JSON, который содержит информацию о типах сборок, заголовке, описании и переведенных компонентах.


**Пример пошаговой блок-схемы (обобщенно):**

1. **Ввод данных (Hebrew JSON):** Получение JSON-данных о компонентах компьютера на иврите.
2. **Перевод:** Преобразование данных на заданный язык.
3. **Анализ компонентов:** Определение типа сборки (гейминг, рабочая станция, и т.д.) на основе характеристик компонентов.
4. **Генерация описания:** Создание описания сборки, включая заголовок и подробное описание.
5. **Перевод компонентов:** Перевод названий и описаний компонентов на целевой язык.
6. **Формирование JSON ответа:** Сборка JSON структуры с переведенными данными, включая типы сборок и параметры компонентов.
7. **Вывод:** Возврат сформированного JSON-ответа.


## 3. <mermaid>

```mermaid
graph TD
    A[Входные данные (Hebrew JSON)] --> B{Перевод на целевой язык};
    B --> C[Анализ компонентов];
    C --> D[Определение типа сборки];
    D --> E[Генерация описания];
    E --> F[Перевод компонентов];
    F --> G[Формирование JSON ответа];
    G --> H[Вывод JSON ответа];
```

**Объяснение диаграммы:**
Диаграмма показывает последовательность действий в программе. Начальный блок A – входные данные на иврите, которые переводятся на целевой язык. Затем происходит анализ компонентов для определения типа сборки. После этого генерируется описание сборки и переводятся имена компонентов. Наконец, всё собирается в JSON и выводится.
Подключаемых зависимостей нет, так как код описывает задачу для модели ИИ. Действия будут выполняться в рамках этой модели, а не в конкретных внешних системах.


## 4. <explanation>

**Импорты:** В данном коде нет импортов, так как это не исполняемый код, а описание задачи для модели ИИ. Импорты обычно встречались бы в python-скриптах для работы с языками, API и т.д.

**Классы:** Отсутствуют классы. Текст описывает взаимодействие модели с входными данными и формированием JSON-ответа.

**Функции:** Отсутствуют функции. Текст описывает вычислительный процесс, который будет выполняться моделью на основе входных данных.

**Переменные:** Входные данные представляют собой переменные, которые являются элементами JSON, описывающими компьютерные компоненты. Результаты модели - JSON-объекты.

**Возможные ошибки и улучшения:**

* **Неопределённость:**  Описание задачи достаточно абстрактно. Необходимо указать, каким образом модель будет определять тип сборки, какие ресурсы потребуются и как будет происходить перевод.
* **Сложность перевода:**  Перевод технических терминов может быть сложным и требующим сложной модели машинного перевода.
* **Обработка ошибок:** Не описаны способы обработки ошибок, если входные данные невалидны или не содержат необходимой информации.
* **Поддержка разных языков:** Описание не учитывает возможность поддержки различных входных языков.

**Взаимосвязи с другими частями проекта:**

Представленный код является описанием интерфейса с моделью и не содержит прямых зависимостей с другими частями проекта.  В реальном проекте для выполнения этой задачи потребуется интеграция с библиотеками машинного перевода (например, Google Translate API, или глубокими моделями машинного перевода), а также библиотекой для работы с JSON.