# Обзор модулей проекта `hypotez`

## Обзор

Этот документ предоставляет обзор основных модулей программы `hypotez`. Он содержит информацию о назначении каждого модуля, ссылки на его исходный код, документацию, тесты и примеры использования.

## Подробнее

Проект `hypotez` состоит из нескольких модулей, каждый из которых выполняет определенную функцию. Понимание структуры этих модулей необходимо для разработки, тестирования и поддержки проекта.

## Модули

### `assistant`

Модуль для взаимодействия с классом `CodeAssistant`, который помогает в задачах обработки кода.

- **Ссылка на код модуля**: [assistant](https://github.com/hypo69/hypo/blob/master/src/assistant/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/assistant/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/assistant)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/assistant)

### `bot`

Модуль для логики бота, включая обработку сообщений и обработку команд бота.

- **Ссылка на код модуля**: [bot](https://github.com/hypo69/hypo/blob/master/src/bot/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/bot/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/bot)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/bot)

### `scenario`

Модуль для работы со сценариями, включая генерацию и выполнение сценариев.

- **Ссылка на код модуля**: [scenario](https://github.com/hypo69/hypo/blob/master/src/scenario/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/scenario/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/scenario)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/scenario)

### `suppliers`

Модуль для работы с поставщиками, включая управление их данными и отношениями.

- **Ссылка на код модуля**: [suppliers](https://github.com/hypo69/hypo/blob/master/src/suppliers/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/suppliers/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/suppliers)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/suppliers)

### `templates`

Модуль для работы с шаблонами, включая создание и управление шаблонами для различных целей.

- **Ссылка на код модуля**: [templates](https://github.com/hypo69/hypo/blob/master/src/templates/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/templates/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/templates)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/templates)

### `translators`

Модуль для работы с переводчиками и перевода текста.

- **Ссылка на код модуля**: [translators](https://github.com/hypo69/hypo/blob/master/src/translators/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/translators/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/translators)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/translators)

### `utils`

Модуль для вспомогательных утилит, упрощающих общие задачи.

- **Ссылка на код модуля**: [utils](https://github.com/hypo69/hypo/blob/master/src/utils/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/utils/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/utils)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/utils)

### `webdriver`

Модуль для работы с драйверами веб-браузеров и управления веб-элементами.

- **Ссылка на код модуля**: [webdriver](https://github.com/hypo69/hypo/blob/master/src/webdriver/readme.en.md)
- **Ссылка на документацию**: [documentation](https://github.com/hypo69/hypo/blob/master/docs/gemini/en/doc/src/webdriver/readme.en.md)
- **Ссылка на тесты**: [tests](https://github.com/hypo69/hypo/blob/master/pytest/gemini/src/webdriver)
- **Ссылка на примеры**: [examples](https://github.com/hypo69/hypo/blob/master/docs/examples/webdriver)

## Глоссарий

### 1. **webdriver**
   - **`Driver`**: Объект, который управляет браузером (например, Chrome, Firefox) и выполняет такие действия, как навигация по веб-страницам, заполнение форм и т.д.
   - **`Executor`**: Интерфейс или класс, который выполняет команды или скрипты в контексте веб-драйвера.
   - **`Chrome`, `Firefox`, ...**: Конкретные браузеры, которыми можно управлять с помощью веб-драйвера.
   - **`locator`**: Механизм для поиска элементов на веб-странице (например, по ID, CSS-селектору, XPath).

### 2. **`Supplier`**
   - **список поставщиков (`Amazon`, `Aliexpress`, `Morlevi`, ...)**: Список компаний или платформ, которые предоставляют продукты или услуги.
   - **`Graber`**: Инструмент или модуль, который автоматически собирает данные с веб-сайтов поставщиков (например, цены, доступность товаров).

### 3. **`Product`**
   - **`Product`**: Объект, представляющий продукт или услугу, которые могут быть доступны на различных платформах.
   - **`ProductFields`**: Поля или атрибуты, которые описывают характеристики продукта (например, имя, цена, описание, изображения).

### 4. **`ai`**
   - **`Model Prompt`**: Определяет, как модель должна обрабатывать входящую информацию и возвращать ответ. Он устанавливается при инициализации модели.
   - **`Command Instruction`**: Небольшая команда или инструкция, отправляемая с каждым запросом.

## Далее

[Инициализация и настройка проекта](https://github.com/hypo69/hypo/blob/master/src/credentials.md)