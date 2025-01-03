## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**1. Входные данные (Input Data):**
   - Получение JSON-массива с информацией о компьютерных компонентах. Каждый компонент содержит `product_id`, `product_title`, `product_description`, `specification` и `image_local_saved_path`.
   - Все входные данные представлены на иврите.

**Пример входных данных:**

```json
[
  {
    "product_id": "123",
    "product_title": "מעבד Intel Core i9-14900K",
    "product_description": "מעבד בעל ביצועים גבוהים",
    "specification": "8 ליבות, 16 threads",
    "image_local_saved_path": "/images/cpu.jpg"
  },
  {
    "product_id": "456",
    "product_title": "כרטיס מסך NVIDIA RTX 4060 Ti",
    "product_description": "כרטיס מסך גיימינג",
    "specification": "8GB GDDR6",
    "image_local_saved_path": "/images/gpu.jpg"
   }
]
```

**2. Обработка данных:**

   - **2.1. Перевод:** Перевести все текстовые поля (названия компонентов, описания, спецификации) из иврита на целевой язык (например, русский).
   
     *Пример: "מעבד Intel Core i9-14900K" -> "Процессор Intel Core i9-14900K"*
   - **2.2. Определение типа сборки (Build Type):**
      - Анализ компонентов для определения типа сборки (игровой, офисный, рабочая станция и т.д.).
      - Назначение вероятности для каждого типа сборки на основе характеристик компонентов.
        
         *Пример: Наличие i9-14900K и RTX 4060 Ti повышает вероятность "игровой" сборки.*
   - **2.3. Генерация заголовка и описания:** Создать заголовок и подробное описание сборки на целевом языке.
   
      *Пример: Заголовок: "Мощный игровой ПК", Описание: "Этот ПК собран для максимальной производительности в современных играх"*
   - **2.4. Поиск недостающей информации:** Если для компонента отсутствует спецификация или описание, выполнить поиск в интернете для их заполнения.
        
        *Пример: Если спецификация "כרטיס מסך NVIDIA RTX 4060 Ti" не полная, найти полную спецификацию в интернете.*
    - **2.5. Форматирование:**  Сформировать JSON-словарь в соответствии с требуемым форматом.

**3. Выходные данные (Output Data):**

   - Возвращение JSON-словаря, содержащего:
     - `language_code` - код языка.
     - `build_types` - словарь с вероятностями для каждого типа сборки.
     - `title` - сгенерированный заголовок сборки.
     - `description` - сгенерированное описание сборки.
     - `products` - массив словарей с информацией о каждом компоненте (с переведенными названиями, описаниями и спецификациями).

**Пример выходных данных:**
```json
{
  "ru": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "Мощный игровой ПК на базе Intel Core i9 и RTX 4060 Ti",
    "description": "Этот высокопроизводительный компьютер создан для максимальной производительности в современных играх и других требовательных задачах. Он оснащен мощным процессором и видеокартой.",
    "products": [
      {
        "product_id": "123",
        "product_title": "Процессор Intel Core i9-14900K",
        "product_description": "Высокопроизводительный процессор",
        "specification": "8 ядер, 16 потоков",
        "image_local_saved_path": "/images/cpu.jpg"
      },
      {
        "product_id": "456",
        "product_title": "Видеокарта NVIDIA RTX 4060 Ti",
        "product_description": "Игровая видеокарта",
        "specification": "8GB GDDR6",
        "image_local_saved_path": "/images/gpu.jpg"
      }
    ]
  }
}
```

## <mermaid>
```mermaid
flowchart TD
    A[Start: Input JSON Data (Hebrew)] --> B{Translate Data from Hebrew to Target Language};
    B --> C{Determine Build Type Based on Components};
    C --> D{Generate Title and Description in Target Language};
    D --> E{Translate Component Details in Target Language};
    E --> F{Search Internet for Missing Component Information if needed};
    F --> G{Format JSON Output};
    G --> H[Output JSON Data];
    
     style A fill:#f9f,stroke:#333,stroke-width:2px
     style H fill:#ccf,stroke:#333,stroke-width:2px

```
**Описание Mermaid-диаграммы:**

-   **Start: Input JSON Data (Hebrew)**: Начало процесса, представляющее получение JSON данных на иврите. Это точка входа для процесса.
-   **Translate Data from Hebrew to Target Language**: Блок, отвечающий за перевод всей текстовой информации из иврита на целевой язык.
-   **Determine Build Type Based on Components**: Блок, анализирующий характеристики компонентов для определения типа сборки компьютера.
-   **Generate Title and Description in Target Language**: Блок, генерирующий заголовок и описание сборки на целевом языке.
-   **Translate Component Details in Target Language**: Блок, отвечающий за перевод названий, описаний и спецификаций компонентов на целевой язык.
-   **Search Internet for Missing Component Information if needed**: Блок, выполняющий поиск в интернете дополнительной информации о компонентах в случае ее отсутствия во входных данных.
-  **Format JSON Output**: Блок, отвечающий за форматирование выходных данных в требуемый JSON-формат.
-   **Output JSON Data**: Конец процесса, представляющий вывод готового JSON-словаря.

## <объяснение>

### **Объяснение процесса**

Данная инструкция предназначена для модели Gemini AI, специализирующейся на сборке компьютеров. Основная задача - принимать данные о компьютерных компонентах на иврите, переводить их на целевой язык, анализировать эти компоненты и генерировать описание готовой сборки в формате JSON.

**Входные данные:**

Входные данные представляют собой JSON-массив, где каждый элемент - это словарь с информацией о компьютерном компоненте. Основные ключи:
  - `"product_id"`: идентификатор продукта (не изменяется).
  - `"product_title"`: название компонента (требуется перевод).
  - `"product_description"`: описание компонента (требуется перевод).
  - `"specification"`: технические характеристики компонента (требуется перевод).
  - `"image_local_saved_path"`: путь к изображению компонента (не изменяется).

**Обработка данных:**

1.  **Перевод**: Все текстовые поля из входного JSON на иврите переводятся на целевой язык, указанный в инструкции. Это ключевой шаг, позволяющий модели работать с ивритоязычными данными.

2.  **Определение типа сборки**: На основании анализа характеристик компонентов определяется тип сборки компьютера (игровой, офисный, рабочая станция и т.д.). Например, наличие мощной видеокарты и процессора указывает на игровой ПК. Для каждого типа сборки назначается вероятность.

3.  **Генерация заголовка и описания**: Создается заголовок и описание сборки, которые обобщают информацию о назначении компьютера и его ключевых компонентах.

4.  **Поиск недостающей информации**: Если в данных не хватает описаний или технических характеристик компонента, модель выполняет поиск недостающей информации в интернете. Это позволяет создать более полные выходные данные.

5.  **Форматирование вывода**: Выходные данные формируются в виде JSON-словаря с требуемой структурой:
    -   `"language_code"`: Код языка, на который был выполнен перевод.
    -   `"build_types"`: Распределение вероятностей для разных типов сборки (например, `"gaming": 0.8, "workstation": 0.2`).
    -   `"title"`: Заголовок сборки на целевом языке.
    -   `"description"`: Описание сборки на целевом языке.
    -   `"products"`: Список компонентов, включающий их переведенные названия, описания, спецификации и неизмененные идентификаторы и пути к изображениям.

**Выходные данные:**

Выходные данные предоставляются в формате JSON, содержащем все необходимые детали о сборке на целевом языке.

**Ключевые моменты:**

*   **Перевод:** Все данные из иврита должны быть аккуратно переведены, особенно технические термины.
*   **Классификация:** Правильное определение типа сборки на основе компонентов.
*   **Детализация:** Описание должно быть подробным и информативным.
*   **Форматирование:** Строгое соблюдение JSON-структуры.
*   **Поиск информации:** Модель должна уметь дополнять отсутствующую информацию из внешних источников.

**Потенциальные улучшения:**

*   **Улучшенная классификация:** Ввести подкатегории для сборок (например, "игровой: соревновательный", "игровой: казуальный").
*   **Учет пользовательских предпочтений:** Добавить возможность учитывать пользовательские запросы, например, по бюджету или специфическим задачам.
*  **Оценка достоверности**: Добавление оценки достоверности для информации, найденной в интернете.

**Взаимосвязи с другими частями проекта:**

Данная инструкция может быть интегрирована в систему, которая:

*   Получает данные о компонентах из разных источников.
*   Обрабатывает различные языковые вводы.
*   Хранит и отображает результаты сборки для пользователей.

**Использование в проекте:**

Эта инструкция предназначена для использования с моделью Gemini AI для автоматизации процесса сборки и описания компьютерных систем. Она обеспечивает четкое понимание процесса и формализованный результат.