# <input code>

```
# command instruction for model:
**"Analyze computer components from JSON, classify build type (e.g., gaming, workstation), 
provide titles and descriptions in Hebrew and Russian, translate component details, 
and return structured JSON output. Maintain correct formatting, include confidence scores, 
and follow detailed guidelines for descriptions and component handling."**

## response text encoding: `UTF-8`

### **Template Response:**
```json
{
  "he": {
    "title": "מחשב גיימינג בעל ביצועים גבוהים",
    "description": "מחשב מודרני למשחקים ותוכנות תובעניים. כולל מעבד Intel i7-14700F, כרטיס מסך Gigabyte RTX 4070, זיכרון RAM DDR4 בנפח 16GB ו-SSD Kingston בנפח 4TB.",
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "products": [
      {
        "product_id": "<leave as is form input data>",
        "product_title": "<product name in hebrew generated by you>",
        "product_description": "<description for product in hebrew generated by you>",
        "specification": "<specifiacetion for product in hebrew generated by you>",
        "image_local_saved_path": "<leave as is from input data>"
      },
            {
        "product_id": "<leave as is form input data>",
        "product_title": "<your product name in hebrew>",
        "product_description": "<description for product in hebrew generated by you>",
        "product_specification": "<specifiacetion for product in hebrew generated by you>",
        "image_local_saved_path": "<leave as is from input data>"
      }
    ]
  }
},
{
  "ru": {
    "title": "Высокопроизводительный игровой компьютер",
    "description": "Современный компьютер для требовательных игр и приложений. Включает Intel i7-14700F, Gigabyte RTX 4070, DDR4 RAM 16GB и SSD Kingston 4TB.",
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "products": [
      {
        "product_id": "<leave as is form input data>",
        "product_title": "<product name in russian generated by you>",
        "product_description": "<description for product in russian generated by you>",
        "product_specification": "<specifiacetion for product in russian generated by you>",
        "image_local_saved_path": "<leave as is from input data>"
      },
            {
        "product_id": "<leave as is form input data>",
        "product_title": "<your product name in russian>",
        "product_description": "<description for product in russian generated by you>",
        "product_specification": "<specifiacetion for product in russian generated by you>",
        "image_local_saved_path": "<leave as is from input data>"
      }
    ]
  }
}
```
### формат ответа должен полностью соответствовать шаблону
## end command
```

# <algorithm>

Этот код представляет собой шаблон для инструкции модели. Он не содержит выполняемого кода, а описывает ожидаемый формат ответа модели на запрос о характеристиках компьютера. Алгоритм работы модели основан на анализе данных о компонентах компьютера, полученных в формате JSON.  

**Шаг 1:** Модель получает JSON-данные о компонентах компьютера.
**Шаг 2:** Модель анализирует данные, чтобы определить тип сборки (например, "gaming", "workstation").
**Шаг 3:** Модель генерирует заголовки и описания на иврите и русском языке, используя предоставленные данные и свои внутренние знания.
**Шаг 4:** Модель возвращает структурированный JSON-ответ в формате, который указан в шаблоне. Этот ответ включает в себя заголовок и описание на обоих языках, категории (gaming и workstation) и информацию о каждом продукте (ID, название, описание и спецификация). Вероятность того или иного типа сборки указывается в виде оценки от 0 до 1. 

Пример: Если входные данные JSON содержат информацию о графическом процессоре, процессоре, оперативной памяти и жестком диске, модель на основе этой информации может классифицировать компьютер как игровой компьютер с высокой вероятностью (например, 0.9).


# <mermaid>

```mermaid
graph TD
    A[Input JSON Data] --> B{Analysis};
    B --> C[Classification];
    C --> D[Hebrew Generation];
    C --> E[Russian Generation];
    D --> F[Output (Hebrew)];
    E --> G[Output (Russian)];
    F -- Hebrew Output --> H[JSON Response];
    G -- Russian Output --> H;

```

**Диаграмма** показывает, что входные JSON-данные анализируются, на основе анализа определяется тип сборки компьютера и на основании этого генерируются заголовки и описания на русском и иврите. В итоге формируется итоговый JSON-ответ, содержащий информацию на обоих языках.

# <explanation>

**Импорты:**

В данном примере нет импортируемых библиотек. Код представляет собой описание инструкции, а не выполняемый код.

**Классы:**

Нет определенных классов.

**Функции:**

Нет определенных функций. Код представляет собой шаблон для ответа модели, поэтому нет функций для выполнения конкретных действий.

**Переменные:**

Нет определенных переменных.

**Возможные ошибки или улучшения:**

* Отсутствие примера реализации: Шаблон не реализован, он определяет только структуру ответа.  Необходимо реализовать алгоритм анализа JSON-данных, определения типов сборки, генерации текстов на двух языках и формирование выходного JSON-объекта.
* Сложность задачи:  Точное и качественное перевод и описание компонентов компьютера требует больших вычислительных ресурсов и модели, хорошо обученной на текстах о компьютерах.


**Цепочка взаимосвязей:**

Код функционирует как шаблон ответа для модели, которая обрабатывает входные данные в JSON формате. Это значит, что модель (возможно, большая языковая модель) должна быть обучена, чтобы выполнять предписанные операции.