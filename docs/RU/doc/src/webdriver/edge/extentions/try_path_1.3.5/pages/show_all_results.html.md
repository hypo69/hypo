# `show_all_results.html`

## Обзор

Файл `show_all_results.html` представляет собой HTML-страницу, предназначенную для отображения результатов выполнения XPath-запросов в расширении браузера. Эта страница отображает различные параметры запроса, контекст и результаты.

## Оглавление

1.  [Заголовок](#заголовок)
2.  [Разделы HTML](#разделы-html)
    *   [Экспорт ссылок](#экспорт-ссылок)
    *   [Информация](#информация)
    *   [Контекстная информация](#контекстная-информация)
    *   [Основная информация](#основная-информация)
3.  [Внешние ресурсы](#внешние-ресурсы)

## Заголовок

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Tryxpath show all results</title>
    <script src="../scripts/try_xpath_functions.js"></script>
    <script src="show_all_results.js"></script>
    <link rel="stylesheet" href="show_all_results.css"/>
  </head>
```

## Разделы HTML

### Экспорт ссылок

```html
    <div>
      <h1>Export links</h1>
      <ul>
        <li><a id="export-text">Plain text</a></li>
        <li><a id="export-partly-converted">Some values are converted by JSON.stringify.</a></li>
      </ul>
    </div>
```
Этот раздел предоставляет ссылки для экспорта результатов:
- **Plain text**: Экспортирует результаты в виде простого текста.
- **Some values are converted by JSON.stringify.**: Экспортирует результаты, преобразованные с использованием JSON.stringify.

### Информация

```html
    <div>
      <h1>Information</h1>
      <table>
        <tbody>
          <tr><th>Message</th><td id="message"></td></tr>
          <tr><th>Title</th><td id="title"></td></tr>
          <tr><th>URL</th><td id="url"></td></tr>
          <tr><th>frameId</th><td id="frame-id"</td></tr>
        </tbody>
      </table>
    </div>
```

В этом разделе отображается основная информация о контексте запроса, включая:
- **Message**: Сообщение, связанное с результатом запроса.
- **Title**: Заголовок страницы.
- **URL**: URL страницы, на которой был выполнен запрос.
- **frameId**: ID фрейма, в котором был выполнен запрос.

### Контекстная информация

```html
    <div id="context-area">
      <h1>Context information</h1>
      <table>
        <tbody>
          <tr><th>Method</th><td id="context-method"></td></tr>
          <tr><th>Expression</th><td id="context-expression"></td></tr>
          <tr><th>Specified resultType</th><td id="context-specified-result-type"></td></tr>
          <tr><th>resultType</th><td id="context-result-type"></td></tr>
          <tr><th>Resolver</th><td id="context-resolver"></td></tr>
        </tbody>
      </table>
      <h1>Context detail</h1>
      <table id="context-detail">
        <tbody>
        </tbody>
      </table>
    </div>
```

В этом разделе отображается информация о контексте запроса:
- **Method**: Метод XPath, использованный в запросе.
- **Expression**: XPath-выражение.
- **Specified resultType**: Указанный тип результата запроса.
- **resultType**: Фактический тип результата запроса.
- **Resolver**: Разрешитель, использованный для выполнения запроса.
- **Context detail**: Детали контекста в виде таблицы.

### Основная информация

```html
    <div>
      <h1>Main information</h1>
      <table>
        <tbody>
          <tr><th>Method</th><td id="main-method"></td></tr>
          <tr><th>Expression</th><td id="main-expression"></td></tr>
          <tr><th>Specified resultType</th><td id="main-specified-result-type"></td></tr>
          <tr><th>resultType</th><td id="main-result-type"></td></tr>
          <tr><th>Resolver</th><td id="main-resolver"></td></tr>
          <tr><th>Count</th><td id="main-count"></td><tr>
        </tbody>
      </table>
      <h1>Main details</h1>
      <table id="main-details">
        <tbody>
        </tbody>
      </table>
    </div>
```
В этом разделе отображается основная информация о результате запроса:
- **Method**: Метод, использованный в основном запросе.
- **Expression**: Основное XPath-выражение.
- **Specified resultType**: Указанный тип результата основного запроса.
- **resultType**: Фактический тип результата основного запроса.
- **Resolver**: Разрешитель, использованный для выполнения основного запроса.
- **Count**: Количество найденных элементов.
- **Main details**: Детали результата в виде таблицы.

## Внешние ресурсы

Страница подключает следующие внешние ресурсы:

-   `../scripts/try_xpath_functions.js`:  JavaScript-файл с функциями, необходимыми для работы расширения.
-   `show_all_results.js`:  JavaScript-файл, содержащий логику для этой конкретной страницы.
-   `show_all_results.css`: Файл CSS, определяющий стили страницы.