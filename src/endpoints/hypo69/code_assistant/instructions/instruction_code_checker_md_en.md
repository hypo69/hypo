```markdown
### **Instruction: Code and Documentation Processing for the `hypotez` Project**

---

#### **Key Requirements**:

1. **Documentation Format**:
   - Use the `Markdown (.md)` standard.
   - Each file must start with a header and a brief description of its contents.

   Documentation examples: Module file header example:

        """
        Module for working with a programming assistant
        =================================================

        The module contains the :class:`CodeAssistant` class, which is used to interact with various AI models
        (e.g., Google Gemini and OpenAI) and perform code processing tasks.

        Usage Example
        ----------------------

        >>>assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
        >>>assistant.process_files()
        """

2. **Comment Preservation**:
   - All existing comments after `#` must remain unchanged.
   - In the event of code changes, add line-by-line comments using the `#` symbol.

3. **Data Processing**:
   - Each file must start with a header and a brief description of its contents.

   Documentation examples: Module file header example:

        """
        Module for working with a programming assistant
        =================================================

        The module contains the :class:`CodeAssistant` class, which is used to interact with various AI models
        (e.g., Google Gemini and OpenAI) and perform code processing tasks.

        Usage Example
        ----------------------

        >>>assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
        >>>assistant.process_files()
        """

   - For all classes and functions, use the following comment format:
     ```python
     def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
         """ Функция выполняет некоторое действия... <Тут Ты пишешь что именно делает функция>
         Args:
             param (str): Описание параметра `param`.
             param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

         Returns:
             dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

         Raises:
             SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
            ...
            <DO NOT output the function body. Only docstring>
         """
         def inner_function():
            """ Внутрняя функция Функция выполняет некоторое действия... <Тут Ты пишешь что именно делает функция>
                Args:
                    param (str): Описание параметра `param`.
                    param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

                Returns:
                    dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

                Raises:
                    SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

                ...
                    <DO NOT output the function body. Only docstring>

                """
     ```

     - All comments in the function and docstring must be in Russian in UTF-8 format.
     - If there are inner functions inside the function under consideration, consider each of them in detail separately.
   - Use `ex` instead of `e` in exception handling blocks.
   - For logging, use `logger` from my `src.logger` module. For example:
     ```python
     from src.logger import logger
     logger.info('Some information message')
     ...
     except SomeError as ex:
         logger.error('Some error message', ex, exc_info = True), where the error is passed as the second argument. exc_info determines whether to output service information.
    ```

    _ If the code uses a webdriver, know how to use it.
    inherit Driver, Chrome, Firexox, Playwright
    Next define like this
    # Creating a driver instance (example with Chrome)
    driver = Drivewr(Chrome)
    The Driver and Chrome, Firexox, Playwright modules already contain all the selenium settings.
    The main command that is used in the code: `driver.execute_locator(l:dict)`
    It returns the value of the web element by the locator.

    - Always use single quotes (`'`) in Python code. For example:
     ```python
     a = 'A1'
     b = ['a', 'b']
     c = {'key': 'value'}
     ```

   - All comments and docstrings must be in Russian in UTF-8 format. If the docstring is in English in the code, translate it into Russian.

4. **Structure Analysis**:
   - Check for the presence of all necessary imports.
   - Analyze the connection with other modules and classes of the `hypotez` project.

5. **Refactoring and Improvements**:
   - Add comments in the following format for all functions, methods, and classes:
        ```python
        def function_name(arg1: type, arg2: type) -> type:
            """
            Описание функции.

            Args:
                arg1 (type): Описание аргумента 1.
                arg2 (type): Описание аргумента 2.

            Returns:
                type: Описание возвращаемого значения.
            """
            ...
        ```

6. **Documentation Examples**:
   **Module Example**:
   ```python
   """
   Модуль для работы с ассистентом программиста
   =================================================

   Модуль содержит класс :class:`CodeAssistant`, который используется для взаимодействия с различными AI-моделями
   (например, Google Gemini и OpenAI) и выполнения задач обработки кода.

   Пример использования
   ----------------------

   >>>assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
   >>>assistant.process_files()
   """
   ```

   **Function Example**:
   ```python
   async def save_text_file(
       file_path: str | Path,
       data: str | list[str] | dict,
       mode: str = 'w'
   ) -> bool:
       """
       Асинхронно сохраняет данные в текстовый файл.
        Args:
            file_path (str | Path): Путь к файлу.
            data (str | list[str] | dict): Данные для записи.
            mode (str, optional): Режим записи. По умолчанию 'w'.
        Returns:
            bool: Результат сохранения файла.

        Example:
           >>> from pathlib import Path
           >>> file_path = Path('example.txt')
           >>> data = 'Пример текста'
           >>> result = await save_text_file(file_path, data)
           >>> print(result)
           True
       """
       ...
   ```

7. **Recommendations for Improvement**:
   - Follow PEP8 standards for formatting.
   - Avoid vague wording in comments, such as "getting" or "doing". Instead, use more precise descriptions: "checking", "sending", "executing".

---

#### **Response Structure**:

1. **Header**:
   - Code analysis of module `<module_name>`

2. **Code Quality**:
   - **Compliance with standards**: Rating from 1 to 10
   - **Pros**:
     - <Positive aspects of the code>
   - **Cons**:
     - <Negative aspects of the code>

3. **Recommendations for improvement**:
   - <Detailed advice and descriptions of necessary changes>

4. **Optimized code**:
   - The code you suggested

## Your behavior when analyzing the code:
- always look at the system instruction for processing the code of the `hypotez` project;
- analyze the location of the file in the project. This will help to understand its purpose and relationship with other files. You will find the location of the file in the very first line of code, starting with `## \file /...`;
- memorize the provided code and analyze its connection with other parts of the `hypotez` project;
```