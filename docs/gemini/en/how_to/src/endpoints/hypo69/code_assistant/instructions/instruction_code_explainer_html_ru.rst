How to Use This Code Analysis Prompt
========================================================================================

Description
-------------------------
This prompt is designed to generate a detailed analysis of provided code, explaining its logic, structure, and potential improvements. It focuses on understanding the code's functionality by breaking it down into steps, identifying data flows, and explaining the role of each component.  It aims for a comprehensive understanding, including imports, classes, functions, variables, and their interconnections within a larger project context.

Execution steps
-------------------------
1. **Input Code:** The prompt expects the code to be provided within a code block (e.g., ````python`).  The code is analyzed without modification.  The input is precisely what you want analyzed.

2. **Algorithm Description:** A step-by-step explanation of the code's algorithm is generated in the form of an algorithm diagram/flowchart that visually depicts data flow between functions and classes.  This is intended as a visual overview of the code's logic.

3. **Detailed Explanation:** A detailed explanation follows, including:
    * **Imports:** A description of each import statement, its purpose, and its relationship to other modules within the project.
    * **Classes:** A description of each class, its purpose, attributes, and methods.  Relationships with other parts of the code are highlighted.
    * **Functions:**  Explanations of each function, including its purpose, arguments, and return values.
    * **Variables:** Descriptions of each variable, including its type and use.
    * **Relationships with other parts of the project:**  Connections to other files, modules, or classes within the project.
    * **Potential errors or improvements:**  The analysis should point out any potential issues or areas where the code could be improved.

4. **Output Format:**  The analysis is presented in a structured format as required by the summary and includes these sections in the output: `<input code>`, `<algorithm>`, `<explanation>`.

Usage example
-------------------------
.. code-block:: markdown
    ```
    **Резюме для промпта:**

    ### Основные требования:
    1. **Анализ кода**:\n
       - Предоставьте исходный код без изменений.\n
       - Опишите алгоритм работы кода в виде пошаговой блок-схемы, показывая перемещение данных между функциями или классами.\n
       - Объясните работу кода, включая импорты, классы, функции, переменные и их связи с другими частями проекта.\n
       - Укажите потенциальные ошибки или улучшения, если они есть.\n

    2. **Формат ответа**:
       - **<input code>**: Исходный код без изменений.\n
       - **<algorithm>**: Пошаговое описание алгоритма работы кода с примерами.\n
       - **<explanation>**: Детальное объяснение кода, включая:\n
         - Импорты: их назначение и связи с другими модулями.\n
         - Классы: их назначение, атрибуты и методы, связи с другими компонентами.\n
         - Функции: описание назначения, аргументов и возвращаемых значений.\n
         - Переменные: описание типов и использования.\n
         - Связь с другими частями проекта и потенциальные ошибки или улучшения.\n

    ### Пример вызова:
    Представлен код, который анализируется и объясняется в соответствии с инструкциями.\n

    ---
    ```