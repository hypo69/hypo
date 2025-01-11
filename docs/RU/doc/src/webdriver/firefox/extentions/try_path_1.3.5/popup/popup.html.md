# Модуль: `src.webdriver.firefox.extentions.try_path_1.3.5.popup`

## Обзор

Данный HTML-файл представляет собой пользовательский интерфейс расширения для браузера Firefox, предназначенного для тестирования XPath-выражений и CSS-селекторов на веб-страницах. Расширение позволяет пользователю вводить XPath-выражения и CSS-селекторы, задавать контекст для их выполнения, а также определять пространство имен и фреймы, в которых эти выражения будут выполняться. Результаты выполнения запросов отображаются в нижней части страницы.

## Оглавление

1. [Обзор](#обзор)
2. [Основные элементы](#основные-элементы)
3. [Раздел "Main"](#раздел-main)
4. [Раздел "Context"](#раздел-context)
5. [Раздел "namespaceResolver"](#раздел-namespaceresolver)
6. [Раздел "Frame without id"](#раздел-frame-without-id)
7. [Раздел "frameId"](#раздел-frameid)
8. [Раздел "Results"](#раздел-results)

## Основные элементы

Файл содержит следующие основные элементы:

-   `<!DOCTYPE html>`: Объявление типа документа.
-   `<html>`: Корневой элемент HTML-страницы.
-   `<head>`: Содержит метаданные, ссылки на CSS и JavaScript.
    -   `<meta charset="utf-8">`: Установка кодировки UTF-8.
    -   `<link rel="stylesheet" href="popup.css"/>`: Подключение файла стилей `popup.css`.
    -   `<script src="../scripts/try_xpath_functions.js"></script>`: Подключение скрипта с функциями для работы с XPath.
    -   `<script src="popup.js"></script>`: Подключение скрипта `popup.js`, содержащего логику работы интерфейса.
-   `<body>`: Содержит видимое содержимое HTML-страницы.

## Раздел "Main"

Этот раздел предназначен для ввода и настройки основных параметров XPath-выражений и CSS-селекторов.

-   **Way:**
    -   Выпадающий список `<select id="main-way">` позволяет выбрать метод выполнения запроса (XPath с различными типами результатов, querySelector, querySelectorAll).
-   **Expression:**
    -   Многострочное текстовое поле `<textarea id="main-expression">` для ввода XPath-выражения или CSS-селектора.
-   **Help:**
    -   Текстовое сообщение с подсказкой по вводу многострочного выражения.

## Раздел "Context"

Этот раздел позволяет задать контекстный элемент для выполнения запроса.

-   **Way:**
    -   Выпадающий список `<select id="context-way">` позволяет выбрать метод выполнения запроса (XPath с различными типами результатов, querySelector, querySelectorAll).
-   **Expression:**
    -   Многострочное текстовое поле `<textarea id="context-expression">` для ввода XPath-выражения или CSS-селектора.
-   **Help:**
    -   Текстовое сообщение с пояснением использования контекста.

## Раздел "namespaceResolver"

Этот раздел позволяет настроить функцию namespaceResolver для работы с пространствами имен в XPath.

-   **Resolver:**
    -   Текстовое поле `<input type="text" id="resolver-expression">` для ввода JSON-представления пространства имен.
-   **Help:**
    -   Текстовое сообщение с примером использования resolver.

## Раздел "Frame without id"

Этот раздел позволяет указать фрейм без id, в котором будет выполняться запрос.

-   **Frame:**
    -   Текстовое поле `<input type="text" id="frame-designation-expression">` для ввода индексов фреймов (например, `[1, 0]`).
-   **Focus frame:**
    -   Кнопка `<button id="focus-designated-frame">` для переключения фокуса на указанный фрейм.
-   **Help:**
    -   Текстовое сообщение с пояснением о способе задания фреймов без ID.

## Раздел "frameId"

Этот раздел позволяет указать фрейм по его id, в котором будет выполняться запрос.

-   **Get all frameId:**
    -   Кнопка `<button id="get-all-frame-id">` для получения списка всех frameId.
    -   Выпадающий список `<select id="frame-id-list">` для выбора frameId.
-   **frameId:**
    -   Текстовое поле `<input type="text" id="frame-id-expression">` для ввода frameId.
-   **Focus frame:**
    -   Кнопка `<button id="focus-frame">` для переключения фокуса на указанный фрейм.
-   **Show previous results:**
    -   Кнопка `<button id="show-previous-results">` для отображения предыдущих результатов.
-   **Help:**
    -   Текстовое сообщение с пояснением о порядке работы с frameId.

## Раздел "Results"

Этот раздел предназначен для отображения результатов выполнения запросов.

-   **Message:**
    -   Элемент `<span>` с id `results-message` для вывода сообщений.
-   **Count:**
    -   Элемент `<span>` с id `results-count` для вывода количества результатов.
-   **frameId:**
    -   Элемент `<span>` с id `results-frame-id` для вывода frameId.
-   **Buttons:**
    -   Кнопки `<button>` для управления отображением результатов и настройками.
    -   `Show all results`, `Open options`, `Set style`, `Reset style`, `Set style(all frames)`, `Reset style(all frame)`.
-   **Context detail:**
    -   Таблица `<table id="context-detail">` для отображения подробностей о контексте.
-   **Details:**
    -   Элементы управления для навигации по деталям результатов:
        -   `<button id="previous-details-page">&lt;</button>`
        -   `<button id="move-details-page">Move</button>`
        -   `<input type="text" id="details-page-count">`
        -   `<button id="next-details-page">&gt;</button>`
    -   Таблица `<table id="results-details">` для отображения деталей результатов.