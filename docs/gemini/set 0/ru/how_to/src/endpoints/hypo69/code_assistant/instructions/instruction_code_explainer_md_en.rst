Как использовать этот блок кода
========================================================================================

Описание
-------------------------
Этот блок кода предоставляет шаблон для анализа кода и генерации документации. Он запрашивает код, а затем генерирует алгоритм, блок-схему в формате mermaid, объяснение импортов, классов, функций и переменных.  Он также анализирует возможные ошибки и предлагает улучшения, а также выявляет связи с другими частями проекта.

Шаги выполнения
-------------------------
1. **Анализ запроса**: Код анализирует полученный запрос, выделяя ключевые части: входной код, необходимую информацию (алгоритм, блок-схема, объяснение).
2. **Разбор входного кода**: Программа анализирует полученный код, определяет его структуру (классы, функции, переменные), ищет зависимости и импорты.
3. **Генерация алгоритма**: На основе анализа формируется пошаговый алгоритм работы кода,  с примерами для каждого логического блока.
4. **Создание блок-схемы (mermaid)**: Генерируется блок-схема (mermaid) для визуализации потока данных и зависимостей между функциями и классами.  Анализируются используемые импорты и их связь с другими частями проекта.
5. **Объяснение**:  Проводится подробное объяснение импортов (цель, связь с другими пакетами `src.`), классов (роль, атрибуты, методы, взаимодействие), функций (аргументы, возвращаемые значения, назначение, примеры), переменных (тип, использование).  Выявляются возможные ошибки и области для улучшения.
6. **Определение связей с другими частями проекта**: Программа устанавливает связи между анализируемым кодом и другими модулями проекта (если таковые имеются).


Пример использования
-------------------------
.. code-block:: markdown

    **INSTRUCTION**:  
    
    Analyze the provided code in detail and explain its functionality. The response should include three sections:  
    
    1. **<input code>**: Present the given code without modifications.  
    2. **<algorithm>**: Describe the workflow in a step-by-step block diagram format, include examples for each logical block, and illustrate data flow between functions, classes, or methods.  
    3. **<mermaid>**: Write a code for diagram in mermaid format, analyze and explain all the dependencies being imported while constructing the diagram.
    4. **<explanation>**: Provide detailed explanations of:  
       - **Imports**: Their purpose and relationship with other `src.` packages.  
       - **Classes**: Their role, attributes, methods, and interactions with other project components.  
       - **Functions**: Their arguments, return values, purpose, and examples.  
       - **Variables**: Their types and usage.  
       - Highlight potential errors or areas for improvement.  
    
    Additionally, construct a chain of relationships with other parts of the project (if applicable).  
    
    This ensures a comprehensive and structured analysis of the code.
    ## Response format: `.md` (markdown)
    **END INSTRUCTION**