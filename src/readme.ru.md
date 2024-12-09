```rst
.. :module: src
```

<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.RU.MD'>[Root ↑]</A>
</TD>


<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>English</A>
</TD>
</TABLE>



# Модули проекта

## Обзор

Данный документ предоставляет обзор различных модулей проекта, включая ссылки на исходный код, документацию, тесты и примеры.

## Модуль `assistant`

Модуль для взаимодействия с классом `CodeAssistant`. Назначение класса: обучение модели коду проекта

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/code_assistant/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/out/ru/doc/src/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/assistant)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/assistant)


## Модуль `bot`

Модуль для логики бота, включая обработку сообщений и управление командами бота.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/bot/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/bot/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/bot)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/bot)


## Модуль `scenario`

Модуль для работы со сценариями, включая генерацию и выполнение сценариев.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/scenario/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/scenario/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/scenario)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/scenario)


## Модуль `suppliers`

Модуль для работы с поставщиками, включая управление их данными и отношениями.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/suppliers/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/suppliers/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/suppliers)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/suppliers)


## Модуль `templates`

Модуль для работы с шаблонами, включая создание и управление шаблонами для различных целей.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/templates/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/templates/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/templates)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/templates)


## Модуль `translators`

Модуль для работы с переводчиками и переводом текста.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/translators/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/translators/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/translators)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/translators)


## Модуль `utils`

Модуль для вспомогательных утилит, упрощающих выполнение общих задач.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/utils/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/utils/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/utils)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/utils)


## Модуль `webdriver`

Модуль для работы с драйверами веб-браузера и управления веб-элементами.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/webdriver/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/webdriver/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/webdriver)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/webdriver)

---

Глоссарий
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
[Project Initialization and Setup](https://github.com/hypo69/hypo/blob/master/src/credentials.md)