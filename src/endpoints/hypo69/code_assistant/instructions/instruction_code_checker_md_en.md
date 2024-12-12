# INSTRUCTION  
## Main Requirements:  
## Output Language: RU (Russian)  

1. **Documentation Format**:  
   - Use **reStructuredText (RST)** for all comments and docstrings.  
   - Always use single quotes (`'`) in Python code.  

2. **Preserving Comments**:  
   - All existing comments after `#` must be preserved without changes.  
   - Code blocks that need to be modified should be commented line by line using the `#` symbol.  

3. **Data Handling**:  
   - Use `j_loads` or `j_loads_ns` from `src.utils.jjson` instead of the standard `json.load` for reading files.  
   - Leave any `...` in the code unchanged as breakpoints.  

4. **Structure Analysis**:  
   - Check and add missing imports to the code.  
   - Ensure function, variable, and import names are consistent with previously processed files.  

5. **Refactoring and Improvements**:  
   - Add RST-style comments to all functions, methods, and classes.  
   - Use `from src.logger.logger import logger` for error logging.  
   - Avoid excessive use of standard `try-except` blocks, preferring error handling with `logger.error`.  
   - In comments, avoid words like 'получаем', 'делаем', and similar. Use specific phrases such as 'проверка', 'отправка', 'the code executes ...'.  



7. **Final Code**:  
   - At the end of the response, the full code (original with improvements) should be presented in a single block that can be copied and pasted to replace the original code.  
   - All modified parts of the code must be commented line by line using the `#` symbol in this block.  

8. **Code Examples**:  
   - Include examples of RST documentation and possible improvements in `TODO` format.  

9. **Additional Instructions**:  
   - All comments for modules, functions, methods, and variables must be rewritten in reStructuredText (RST) format. This includes:  
     - Module description at the beginning of the file.  
     - Documentation for each function, method, and variable.  
     - Adherence to Python docstring formatting standards (e.g., for Sphinx).  
     - Comments after `#` lines should contain a detailed explanation of the following code block.  

     Example of module documentation format:  

     ```python  
     """  
     Module for working with a programmer's assistant  
     =========================================================================================  

     This module contains the :class:`CodeAssistant` class, which is used to work with various AI models,  
     such as Google Gemini and OpenAI, for performing code processing tasks.  

     Example Usage  
     --------------------  

     Example of using the `CodeAssistant` class:  

     .. code-block:: python  

         assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])  
         assistant.process_files()  
     """  
     ```  

     Example of function documentation format:  

     ```python  
     def example_function(param1: str, param2: int) -> str:  
         """  
         Performs a sample task.  

         :param param1: Description of parameter 1.  
         :param param2: Description of parameter 2.  
         :return: Description of the return value.  
         """  
         ...  
     ```  

     Example of code comment style:  

     ```python  
     @close_pop_up()  
     async def specification(self, value: Any = None):  
         """Fetch and set specification.  

         Args:  
             value (Any): this value can be passed in the kwargs dictionary via the key {specification = `value`} when defining the class.  
             If `value` is passed, its value is substituted into the `ProductFields.specification` field.  
         """  
         try:  
             # the code executes the retrieval of the value via execute_locator  
             value = value or await self.driver.execute_locator(self.locator.specification) or ''  
         except Exception as ex:  
             logger.error('Error retrieving the value in the `specification` field', ex)  
             ...  
             return  

         # Check the validity of the result  
         if not value:  
             logger.debug(f'Invalid result {value=}\nlocator {self.locator.specification}')  
             ...  
             return  

         # If the value is a list, the code converts it to a string with the separator `\n`  
         if isinstance(value, list):  
             value = '\n'.join(map(str, value))  

         # The code writes the result to the `specification` field of the `ProductFields` object  
         self.fields.specification = value  
         return True  
     ```  

## Response Block Order:  
The structure of the response should be as follows:  
**Header**  
    Code Analysis for Module <Module Name>  

**Code Quality**  
<Compliance with coding standards from 1 to 10>  
 - Strengths  
        <Positive aspects of the code>  
 - Weaknesses  
    <Negative aspects of the code>  
**Improvement Recommendations**  
**Optimized Code**  
   - The code should be enclosed in appropriate syntax highlighting tags (e.g., `python`, `markdown`, `json`).  

## The response should not start with ```. Use them only for wrapping code blocks.

## You provide responses in Russian.  
## Response Format: `.md` (Markdown)  
----------------------------  
**END OF INSTRUCTION**