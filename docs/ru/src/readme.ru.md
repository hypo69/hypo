# Обзор модулей проекта `hypotez`

## Обзор

Этот документ содержит обзор различных модулей проекта `hypotez`, а также ссылки на их исходный код, документацию, тесты и примеры использования.

## Содержание

- [Модуль `bot`](#модуль-bot)
- [Модуль `scenario`](#модуль-scenario)
- [Модуль `suppliers`](#модуль-suppliers)
- [Модуль `templates`](#модуль-templates)
- [Модуль `translators`](#модуль-translators)
- [Модуль `utils`](#модуль-utils)
- [Модуль `webdriver`](#модуль-webdriver)
- [Глоссарий](#глоссарий)
  - [1. **webdriver**](#1-webdriver)
  - [2. **Supplier**](#2-supplier)
  - [3. **Product**](#3-product)
  - [4. **ai**](#4-ai)
- [Судебная информация](#судебная-информация)
- [Далее](#далее)

## Модуль `bot`

Модуль интерфейсов для `telegram` и `discord` ботов.

- [Исходный код модуля](https://github.com/hypo69/hypo/blob/master/src/bot/readme.ru.md)
- [Документация](https://github.com/hypo69/hypo/blob/master/docs/gemini/ru/doc/src/bot/readme.ru.md)
- [Тесты](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/bot)
- [Примеры](https://github.com/hypo69/hypo/blob/master/docs/examples/bot)

## Модуль `scenario`

Модуль для работы со сценариями, включая их генерацию и выполнение.

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

## Глоссарий

### 1. **webdriver**

- **`Driver`**: Объект, который управляет браузером (например, Chrome, Firefox) и выполняет такие действия, как навигация по веб-страницам, заполнение форм и т. д.
- **`Executor`**: Интерфейс или класс, который выполняет команды или скрипты в контексте веб-драйвера.
- **`Chrome`, `Firefox`, ...**: Конкретные браузеры, которыми можно управлять с помощью веб-драйвера.
- **`locator`**: Механизм для поиска элементов на веб-странице (например, по ID, CSS-селектору, XPath).

### 2. **Supplier**

- **list of suppliers (`Amazon`, `Aliexpress`, `Morlevi`, ...)**: Список компаний или платформ, которые предоставляют продукты или услуги.
- **`Graber`**: Инструмент или модуль, который автоматически собирает данные с веб-сайтов поставщиков (например, цены, доступность товаров).

### 3. **Product**

- **`Product`**: Объект, представляющий продукт или услугу, доступные на различных платформах.
- **`ProductFields`**: Поля или атрибуты, описывающие характеристики продукта (например, имя, цена, описание, изображения).

### 4. **ai**

- **`Model Prompt`**: Определяет, как модель должна обрабатывать входящую информацию и возвращать ответ. Он устанавливается при инициализации модели.
- **`Command Instruction`**: Небольшая команда или инструкция, отправляемая с каждым запросом.

## Судебная информация

1. Символ многоточия `...` указывает, где следует устанавливать точки останова при отладке кода.

## Далее

[Инициализация и настройка проекта](https://github.com/hypo69/hypo/blob/master/src/credentials.md)