```rst
.. :module: src
```
[Русский](https://github.com/hypo69/hypo/blob/master/src/readme.ru.md)

[Root ↑](https://github.com/hypo69/hypo/blob/master/readme.ru.md)

This document provides an overview of main progam modules

## assistant  
Module for interacting with the `CodeAssistant` class, which helps with processing code tasks.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/assistant/readme.en.md) - Source code for the `assistant` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/assistant/readme.en.md) - Documentation for the `assistant` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/assistant) - Tests for the `assistant` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/assistant) - Examples of using the `assistant` module.

## bot  
Module for the bot logic, including message processing and handling bot commands.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/bot/readme.en.md) - Source code for the `bot` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/bot/readme.en.md) - Documentation for the `bot` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/bot) - Tests for the `bot` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/bot) - Examples of using the `bot` module.

## scenario  
Module for working with scenarios, including scenario generation and execution.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/scenario/readme.en.md) - Source code for the `scenario` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/scenario/readme.en.md) - Documentation for the `scenario` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/scenario) - Tests for the `scenario` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/scenario) - Examples of using the `scenario` module.

## suppliers  
Module for working with suppliers, including managing their data and relationships.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/suppliers/readme.en.md) - Source code for the `suppliers` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/suppliers/readme.en.md) - Documentation for the `suppliers` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/suppliers) - Tests for the `suppliers` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/suppliers) - Examples of using the `suppliers` module.

## templates  
Module for working with templates, including creating and managing templates for various purposes.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/templates/readme.en.md) - Source code for the `templates` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/templates/readme.en.md) - Documentation for the `templates` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/templates) - Tests for the `templates` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/templates) - Examples of using the `templates` module.

## translators  
Module for working with translators and text translation.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/translators/readme.en.md) - Source code for the `translators` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/translators/readme.en.md) - Documentation for the `translators` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/translators) - Tests for the `translators` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/translators) - Examples of using the `translators` module.

## utils  
Module for auxiliary utilities, simplifying common tasks.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/utils/readme.en.md) - Source code for the `utils` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/utils/readme.en.md) - Documentation for the `utils` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/utils) - Tests for the `utils` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/utils) - Examples of using the `utils` module.

## webdriver  
Module for working with web browser drivers and managing web elements.

- [Module code](https://github.com/hypo69/hypo/blob/master/src/webdriver/readme.en.md) - Source code for the `webdriver` module.
- [Documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/webdriver/readme.en.md) - Documentation for the `webdriver` module.
- [Tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/webdriver) - Tests for the `webdriver` module.
- [Examples](https://github.com/hypo69/hypo/blob/master/docs/examples/webdriver) - Examples of using the `webdriver` module.

Glossary
=========

### 1. **webdriver**
   - **`Driver`**: An object that controls the browser (e.g., Chrome, Firefox) and performs actions such as navigating web pages, filling out forms, etc.
   - **`Executor`**: An interface or class that executes commands or scripts within the context of the web driver.
   - **`Chrome`, `Firefox`, ...**: Specific browsers that can be controlled using the web driver.
   - **`locator`**: A mechanism for finding elements on a web page (e.g., by ID, CSS selector, XPath).

### 2. **`Supplier`**
   - **list of suppliers (`Amazon`, `Aliexpress`, `Morlevi`, ...)**: A list of companies or platforms that provide products or services.
   - **`Graber`**: A tool or module that automatically collects data from supplier websites (e.g., prices, product availability).

### 3. **`Product`**
   - **`Product`**: An object representing a product or service that can be available on various platforms.
   - **`ProductFields`**: Fields or attributes that describe the characteristics of a product (e.g., name, price, description, images).

### 4. **`ai`**
	- **`Model Prompt`**: Specifies how the model should process incoming information and return a response. It is set during model initialization.
	- **`Command Instruction`**: A small command or instruction sent with each request.
Next
=====
[Project Initialization and Setup]((https://github.com/hypo69/hypo/blob/master/src/credentials.md)