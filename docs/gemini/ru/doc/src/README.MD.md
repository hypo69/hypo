# Обзор модулей проекта

## Обзор

Этот документ предоставляет обзор основных модулей программы.

## Содержание

- [assistant](#assistant)
- [bot](#bot)
- [scenario](#scenario)
- [suppliers](#suppliers)
- [templates](#templates)
- [translators](#translators)
- [utils](#utils)
- [webdriver](#webdriver)
- [Глоссарий](#Глоссарий)

## assistant

Модуль для взаимодействия с классом `CodeAssistant`, который помогает в обработке задач с кодом.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/assistant/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/assistant/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/assistant)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/assistant)

## bot

Модуль для логики бота, включая обработку сообщений и команд бота.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/bot/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/bot/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/bot)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/bot)

## scenario

Модуль для работы со сценариями, включая генерацию и выполнение сценариев.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/scenario/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/scenario/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/scenario)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/scenario)

## suppliers

Модуль для работы с поставщиками, включая управление их данными и взаимоотношениями.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/suppliers/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/suppliers/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/suppliers)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/suppliers)

## templates

Модуль для работы с шаблонами, включая создание и управление шаблонами для различных целей.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/templates/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/templates/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/templates)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/templates)

## translators

Модуль для работы с переводчиками и переводом текста.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/translators/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/translators/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/translators)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/translators)

## utils

Модуль для вспомогательных утилит, упрощающих выполнение общих задач.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/utils/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/utils/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/utils)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/utils)

## webdriver

Модуль для работы с драйверами веб-браузера и управления веб-элементами.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/webdriver/readme.en.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/webdriver/readme.en.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/webdriver)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/webdriver)

---

## Глоссарий

### 1. **webdriver**
   - **`Driver`**: Объект, который управляет браузером (например, Chrome, Firefox) и выполняет такие действия, как навигация по веб-страницам, заполнение форм и т. д.
   - **`Executor`**: Интерфейс или класс, который выполняет команды или скрипты в контексте веб-драйвера.
   - **`Chrome`, `Firefox`, ...**: Конкретные браузеры, которыми можно управлять с помощью веб-драйвера.
   - **`locator`**: Механизм для поиска элементов на веб-странице (например, по ID, CSS-селектору, XPath).

### 2. **`Supplier`**
   - **Список поставщиков (`Amazon`, `Aliexpress`, `Morlevi`, ...)**: Список компаний или платформ, которые предоставляют товары или услуги.
   - **`Graber`**: Инструмент или модуль, который автоматически собирает данные с веб-сайтов поставщиков (например, цены, наличие товаров).

### 3. **`Product`**
   - **`Product`**: Объект, представляющий товар или услугу, которые могут быть доступны на различных платформах.
   - **`ProductFields`**: Поля или атрибуты, которые описывают характеристики продукта (например, название, цена, описание, изображения).

### 4. **`ai`**
    - **`Model Prompt`**: Определяет, как модель должна обрабатывать входящую информацию и возвращать ответ. Устанавливается при инициализации модели.
    - **`Command Instruction`**: Небольшая команда или инструкция, отправляемая с каждым запросом.
    
## Далее
[Инициализация и настройка проекта](https://github.com/hypo69/hypo/blob/master/src/credentials.md)