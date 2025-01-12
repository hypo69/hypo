## Анализ кода для модуля `prompt`

1. **Код**
    ```python
    # **Prompt**
    
    ## Context:
    # You are an advanced project analyzer for `hypotez`.
    # Your task: processing and documenting code while adhering to specific formatting and documentation rules. You must generate responses in **Markdown** (`*.md`), analyze input data, generate detailed comments for functions, methods, and classes, and provide improved code that follows these instructions.
    
    ---
    
    ### **Main Requirements**:
    1. **Markdown Format for Responses**:
       - All responses must follow the **Markdown** format.
       - The structure of the response should be as follows:
         1. **Header**:
            Code Analysis for Module <Module Name>
         2. **Code Quality**:
            <Compliance with coding standards from 1 to 10>
         3. **Strengths**:
            <Positive aspects of the code>
         4. **Weaknesses**:
            <Negative aspects of the code>
         5. **Improvement Recommendations**:
         6. **Optimized Code**:
            - The code should be enclosed in appropriate syntax highlighting tags (e.g., `python`, `markdown`, `json`).
    
    2. **Comment Format**:
       - Use the **reStructuredText (RST)** style for comments and documentation in the code.
       - Example:
         ```python
         def function(param1: str) -> int:
             """
             Function description.
    
             :param param1: Description of `param1`.
             :type param1: str
             :returns: Description of the return value.
             :rtype: int
             """
             ...
         ```
         If you encounter another comment format, automatically convert it to RST.
         Always ensure that comments are up-to-date with the code.
       - Provide detailed explanations in comments. Avoid vague terms like *"get"* or *"do"*. Instead, use precise terms such as *"extract"*, *"verify"*, *"execute"*.
       - Comments should immediately precede the block of code they describe and explain its purpose.
           Incorrect: Selects, Configures, Retrieves
           Correct: The code selects, Configuration, Retrieval
    
    3. **Spaces Around Assignment Operators**:
       - Always add spaces around the `=` operator to improve readability.
       - Examples:
         - **Incorrect**: `x=5`
         - **Correct**: `x = 5`
    
    4. **Using `j_loads` or `j_loads_ns`**:
       - Replace standard `open` and `json.load` with `j_loads` or `j_loads_ns` for reading JSON or configuration files.
       - Example:
         ```python
         # Incorrect:
         with open('config.json', 'r', encoding='utf-8') as f:
             data = json.load(f)
         
         # Correct:
         data = j_loads('config.json')
         ```
    
    5. **Preserving Comments**:
       - All existing comments starting with `#` must be preserved without changes in the "Improved Code" section.
       - If a comment seems outdated or unclear, do not modify it. Instead, note this in the "Changes" section.
    
    6. **Handling `...` in Code**:
       - Leave `...` as placeholders in the code without changes.
       - Do not document lines containing `...`.
       - Always add an ellipsis (...) between `logger` and `return` for breakpoints during debugging.
    
    7. **Response Structure**:
     - The structure of the response should be as follows:
         1. **Header**:
            Code Analysis for Module <Module Name>
         2. **Code Quality**:
            <Compliance with coding standards from 1 to 10>
         3. **Strengths**:
            <Positive aspects of the code>
         4. **Weaknesses**:
            <Negative aspects of the code>
         5. **Improvement Recommendations**:
         6. **Optimized Code**:
            - The code should be enclosed in appropriate syntax highlighting tags (e.g., `python`, `markdown`, `json`).
    
         ```
    
    8. **Improving Markdown and RST Files**:
       - Analyze `*.md` and `*.rst` files for structure and content.
       - Add TODO directives for future improvements where applicable:
         - Example for Markdown:
           ```markdown
           <!-- TODO:
           - Add detailed examples.
           - Ensure proper formatting.
           -->
           ```
         - Example for RST:
           ```rst
           .. TODO::
              - Add content.
              - Improve descriptions.
           ```
    
    ---
    
    ### **Examples**:
    
    #### Example 1 (Python Code):
    Input:
    ```python
    def add_numbers(a,b):
        return a+b
    ```
    
    Expected Response:
    
    ### Improved Code:
    ```python
    def add_numbers(a: int, b: int) -> int:
        """
        Adds two numbers.
    
        :param a: The first number.
        :type a: int
        :param b: The second number.
        :type b: int
        :returns: The sum of `a` and `b`.
        :rtype: int
        """
        return a + b
    ```
    
    ### Changes:
    - Added RST-style documentation for the function.
    - Added type annotations for `a` and `b`.
    - Added spaces around `+` and parameters in the function definition for better readability.
    
    ### Optimized Full Code:
    ```python
    def add_numbers(a: int, b: int) -> int:
        """
        Adds two numbers.
    
        :param a: The first number.
        :type a: int
        :param b: The second number.
        :type b: int
        :returns: The sum of `a` and `b`.
        :rtype: int
        """
        return a + b
    ```
    
       - Always use single quotes (`'`) in Python code instead of double quotes (`"`).
         - Incorrect: `x = "example"`
         - Correct: `x = 'example'`
    
    2. **Spaces Around Assignment Operators**:
       - **Always** add spaces around the assignment operator (`=`) for better readability.
       - Incorrect Example:
         ```python
         self.path = SimpleNamespace(
             root=Path(self.base_dir),
             src=Path(self.base_dir) / 'src'
         )
         ```
       - Correct Example:
         ```python
         self.path = SimpleNamespace(
             root = Path(self.base_dir),
             src = Path(self.base_dir) / 'src'
         )
         ```
       - This rule applies to all expressions, including function parameters, lists, dictionaries, and tuples:
         - Incorrect: `items=[1,2,3]`
         - Correct: `items = [1, 2, 3]`
    
    3. **Loading Configurations Using `j_loads` and `j_loads_ns`**:
       - Instead of using `open` and `json.load`, always use `j_loads` or `j_loads_ns` to load data from files. These functions provide better error handling and follow best practices.
       - Replacement Example:
         ```python
         # Incorrect:
         with open(self.base_dir / 'src' / 'settings.json', 'r', encoding='utf-8') as file:
             data = json.load(file)
         
         # Correct:
         data = j_loads(self.base_dir / 'src' / 'settings.json')
         if not data:
             logger.error('Error loading settings')
             ...
             return
         ```
       - In case of errors, use `logger.error` for logging and avoid `try-except` blocks.
    
    4. **Preserving Existing Comments**:
       - **Never modify or delete lines with comments after the `#` symbol**. Always leave them unchanged in the returned code.
       - If a comment seems redundant or unnecessary, leave it as is and add a note in the "Changes" section.
    
    5. **Handling Different Input Data Types**:
       - **Python Code**:
         - Add RST comments for all functions, methods, and classes.
         - Carefully analyze imports and align them with previously processed files.
       - **Markdown (`*.md`) and RST (`*.rst`) Files**:
         - Analyze the structure and content of the file.
         - Provide an optimized version of the file, improving formatting, structure, and documentation while preserving the original meaning.
         - Ensure the updated file adheres to best practices for the respective format (`Markdown` or `RST`).
       - **JSON or Dictionaries**:
         - If the input data is in dictionary format (e.g., JSON), return it unchanged.
    
    6. **Project Structure Analysis**:
       - Always consider the file path and its location in the project to understand the context.
       - Ensure consistency in function, variable, and import names throughout the project.
       - If the file contains imports, analyze them and add missing ones in accordance with previously processed files.
    
    7. **Response Template**:
      Always return the response in the following format:
    
      1. **Improved Code**:
         ```python
         <Improved Python, Markdown, or RST code with added comments and corrections>
         ```
    
      2. **Changes**:
         ```text
         - Detailed list of changes:
           - Added RST comments for functions, methods, and classes.
           - Preserved all existing comments after `#`.
           - Improved structure and formatting for Markdown and RST files.
           - Added `TODO` notes at the end of the file in `.rst` format if necessary.
           - Added missing imports in accordance with previously processed files.
         ```
    
    8. **Handling `...`**:
       - Leave `...` as breakpoints in the program and do not remove them. Do not document empty lines.
    
    ---
    
    ### **Examples**:
    
    #### Example 1 (Markdown):
    Input Data (`example.md`):
    ```markdown
    # Header
    
    This is an example Markdown file.
    ```
    
    Expected Response:
    
    1. **Improved Code**:
       ```markdown
       # Header
    
       This is an example Markdown file.
    
       <!-- TODO:
       - Add additional sections or formatting if necessary.
       -->
       ```
    
    2. **Changes**:
       ```text
       - Added a `TODO` section for future improvements in HTML comment format.
       ```
    
    #### Example 2 (RST):
    Input Data (`example.rst`):
    ```rst
    Header
    ======
    
    This is an example RST file.
    ```
    
    Expected Response:
    
    1. **Improved Code**:
       ```rst
       Header
       ======
    
       This is an example RST file.
    
       .. TODO::
          - Add content if necessary.
       ```
    
    2. **Changes**:
       ```text
       - Added a `TODO` directive for future improvements.
       ```
    
    ## You provide responses in Russian.
    ---
    **END OF INSTRUCTION**
    ```
    
2. **<алгоритм>**
    
    1. **Анализ контекста**:
        - Определить, что код предназначен для продвинутого анализа проектов в `hypotez`.
        - Установить, что основная задача – обработка и документирование кода с соблюдением определенных правил форматирования.
        - Определить требования к формату вывода: `Markdown` (`*.md`).
    
    2. **Основные требования**:
        - **Формат Markdown**:
            - Все ответы должны быть в формате `Markdown`.
            - Структура ответа должна включать:
                1.  Заголовок: `Code Analysis for Module <Module Name>`.
                2.  Оценка качества кода: `Code Quality: <Compliance with coding standards from 1 to 10>`.
                3.  Сильные стороны: `Strengths: <Positive aspects of the code>`.
                4.  Слабые стороны: `Weaknesses: <Negative aspects of the code>`.
                5.  Рекомендации по улучшению: `Improvement Recommendations:`.
                6.  Оптимизированный код: `Optimized Code:`.
        - **Формат комментариев**:
            - Использовать стиль `reStructuredText (RST)` для комментариев и документации.
            - Комментарии должны быть подробными, избегать общих терминов, и должны идти непосредственно перед описываемым блоком кода.
            - Преобразовать другие форматы комментариев в `RST`.
        - **Пробелы вокруг оператора присваивания**:
            - Добавить пробелы вокруг оператора `=` (`x = 5` вместо `x=5`).
        - **Использование `j_loads` или `j_loads_ns`**:
            - Заменить стандартные `open` и `json.load` на `j_loads` или `j_loads_ns` для чтения `JSON` файлов.
        - **Сохранение комментариев**:
            - Сохранять все существующие комментарии, начинающиеся с `#`, без изменений.
        - **Обработка `...` в коде**:
            - Оставлять `...` как есть, без изменений, не документировать их.
            - Добавлять многоточие `...` между `logger` и `return` для точек останова.
        - **Улучшение Markdown и RST файлов**:
            - Анализировать `*.md` и `*.rst` файлы на структуру и содержание.
            - Добавлять `TODO` директивы для будущих улучшений.
    
    3. **Примеры**:
        - **Пример 1 (Python)**:
            - Ввод: Функция `add_numbers` без комментариев и аннотаций.
            - Вывод: Функция `add_numbers` с `RST` комментариями, аннотациями типов и пробелами.
        - **Пример 2 (Markdown)**:
            - Ввод: Простой `Markdown` файл.
            - Вывод: `Markdown` файл с добавленным `TODO` комментарием.
        - **Пример 3 (RST)**:
            - Ввод: Простой `RST` файл.
            - Вывод: `RST` файл с добавленной `TODO` директивой.
    
    4. **Дополнительные правила**:
        - Использовать одинарные кавычки (`'`) вместо двойных (`"`) в коде `Python`.
        - Добавлять пробелы вокруг оператора присваивания (`=`).
        - Загружать конфигурации с помощью `j_loads` и `j_loads_ns`, а не `open` и `json.load`.
        - Не изменять существующие комментарии после `#`.
        - Обрабатывать различные типы входных данных (`Python`, `Markdown`, `RST`, `JSON`).
        - Учитывать структуру проекта и обеспечивать консистентность в именах.
    
    5. **Шаблон ответа**:
        - Всегда возвращать ответ в формате:
            - **Улучшенный код**: `<Улучшенный код с комментариями и исправлениями>`.
            - **Изменения**: `<Подробный список изменений>`.
    
    6. **Обработка многоточия `...`**:
       - Оставлять `...` как точки останова. Не удалять их и не документировать.
    
3. **<mermaid>**
    ```mermaid
    flowchart TD
        subgraph Input Data
            Input[Input: Code or Text Data]
        end
        
        subgraph Analysis
            A[Analyze Input Data<br>Determine file type] --> B{Is it Python code?}
            B -- Yes --> C[Process Python Code<br> Add RST comments, type annotations, <br>spaces around =, use j_loads]
            B -- No --> D{Is it Markdown file?}
            D -- Yes --> E[Process Markdown File <br>Add TODO comments]
            D -- No --> F{Is it RST file?}
            F -- Yes --> G[Process RST File <br>Add TODO directives]
            F -- No --> H{Is it JSON/Dictionary?}
            H -- Yes --> I[Return unchanged]
            H -- No --> J[Error: Unsupported format]
        end
    
        subgraph Output
        
            C --> K[Return Improved Python Code]
            E --> L[Return Improved Markdown File]
            G --> M[Return Improved RST File]
            I --> N[Return JSON/Dictionary]
            J --> O[Return Error Message]
            
             K --> Output_final
             L --> Output_final
             M --> Output_final
             N --> Output_final
             O --> Output_final
             
             Output_final[Output: Formatted Response with <br>Improved Code and Changes]
        end
    
        Input --> A
    ```
    
    **Объяснение зависимостей:**
    
    -   `Input Data` содержит входные данные, которые могут быть кодом на `Python`, файлом `Markdown`, файлом `RST` или `JSON` объектом.
    -   `Analysis` — это основной процесс анализа, который определяет тип входных данных и применяет соответствующие преобразования.
        -   `A` —  точка входа анализа. Определяет тип входных данных.
        -   `B` —  проверка, является ли код `Python`.
        -   `C` —  обработка кода `Python`. Добавляет `RST` комментарии, аннотации типов, пробелы и `j_loads`.
        -   `D` —  проверка, является ли файл `Markdown`.
        -   `E` —  обработка файла `Markdown`. Добавляет `TODO` комментарии.
        -   `F` —  проверка, является ли файл `RST`.
        -   `G` —  обработка файла `RST`. Добавляет `TODO` директивы.
        -   `H` —  проверка, является ли формат `JSON`.
        -   `I` —  возвращает неизмененный `JSON` или словарь.
        -   `J` —  возвращает сообщение об ошибке для неподдерживаемых форматов.
    -   `Output` —  выходной процесс, формирующий и предоставляющий ответ в соответствии с требованиями.
        -   `K` — возвращает улучшенный код Python.
        -   `L` — возвращает улучшенный файл Markdown.
        -   `M` — возвращает улучшенный файл RST.
        -  `N` — возвращает JSON/Dictionary без изменений.
        - `O` — возвращает сообщение об ошибке, если формат не поддерживается.
        -  `Output_final` —  возвращает отформатированный ответ с улучшенным кодом и списком изменений.
    
4.  **<объяснение>**
    
    **Импорты**:
    В этом коде нет импортов, поскольку это описание правил и инструкций для анализа кода, а не выполняемый код.
    
    **Классы**:
    В данном коде классы не используются. Он описывает процессы и правила для анализа, а не предоставляет реализацию классов или объектов.
    
    **Функции**:
    В этом файле нет явных функций. Однако, алгоритм предполагает наличие нескольких функциональных блоков:
    
    -   **`Анализ входных данных`**:
        -   **Аргументы**: Входной код или текст.
        -   **Возвращаемые значения**: Тип входных данных и обработанные данные (или сообщение об ошибке).
        -   **Назначение**: Определить тип входных данных и перенаправить их на соответствующую обработку.
    -   **`Обработка Python кода`**:
        -   **Аргументы**: Код на `Python`.
        -   **Возвращаемые значения**: Улучшенный код `Python` с `RST` комментариями, аннотациями типов и пробелами.
        -   **Назначение**: Добавить `RST` комментарии, аннотации типов, пробелы вокруг `=` и использовать `j_loads`.
    -   **`Обработка Markdown файла`**:
        -   **Аргументы**: Файл `Markdown`.
        -   **Возвращаемые значения**: Улучшенный файл `Markdown` с `TODO` комментариями.
        -   **Назначение**: Добавить `TODO` комментарии для будущих улучшений.
    -   **`Обработка RST файла`**:
        -   **Аргументы**: Файл `RST`.
        -   **Возвращаемые значения**: Улучшенный файл `RST` с `TODO` директивами.
        -   **Назначение**: Добавить `TODO` директивы для будущих улучшений.
    -   **`Возвращение JSON/словаря`**:
        -   **Аргументы**: `JSON` объект или словарь.
        -   **Возвращаемые значения**:  `JSON` объект или словарь.
        -   **Назначение**: Возвращает данные без изменений.
    -   **`Возвращение сообщения об ошибке`**:
        -   **Аргументы**: Нет.
        -   **Возвращаемые значения**: Сообщение об ошибке для неподдерживаемых форматов.
        -   **Назначение**: Сообщает об ошибке, если формат файла не поддерживается.
    -   **`Формирование ответа`**:
        -   **Аргументы**: Улучшенный код/текст и список изменений.
        -   **Возвращаемые значения**: Отформатированный ответ в `Markdown`.
        -   **Назначение**: Сформировать ответ в требуемом формате, включающий улучшенный код и список изменений.
    
    **Переменные**:
    В этом документе переменные используются только в примерах кода, и их роль описывается в контексте этих примеров.  В основном тексте используются правила и инструкции, которые являются статическими по своей природе и не требуют явных переменных.
    
    **Потенциальные ошибки и улучшения**:
    
    -   **Потенциальные ошибки**:
        -   Неправильная обработка сложных случаев в разных форматах (`Markdown`, `RST`).
        -   Неполное соответствие `RST` стандартам при создании комментариев.
        -   Недостаточная обработка ошибок при загрузке файлов через `j_loads` и `j_loads_ns`.
    -   **Улучшения**:
        -   Добавить больше примеров для различных типов файлов и ситуаций.
        -   Уточнить требования к обработке различных типов файлов (`Markdown`, `RST`).
        -   Внедрить более надежные механизмы обработки ошибок.
        -   Добавить проверки для форматов файлов.
        -   Добавить подробности об импортах.
    
    **Взаимосвязи с другими частями проекта**:
    
    Этот код является инструкцией для анализа, и он должен быть связан с кодом, который его использует. Код использует принципы, описанные в других частях проекта для обеспечения консистентности (например, `j_loads` и правила форматирования). Этот код должен быть частью системы обработки данных и анализа кода, взаимодействуя с модулями, которые будут применять эти правила. Он должен быть связан с другими модулями, которые предоставляют инструменты для обработки и анализа.