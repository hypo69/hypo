# `show_all_results.html`

## Обзор

Файл `show_all_results.html` представляет собой HTML-страницу, предназначенную для отображения результатов выполнения XPath-запросов в расширении Tryxpath. Она содержит элементы для вывода информации о контексте запроса, его результатах и способах экспорта данных.

## Оглавление

- [Обзор](#обзор)
- [Разметка HTML](#разметка-html)
    - [Заголовок](#заголовок)
    - [Раздел экспорта ссылок](#раздел-экспорта-ссылок)
    - [Раздел информации](#раздел-информации)
    - [Раздел контекстной информации](#раздел-контекстной-информации)
    - [Раздел основной информации](#раздел-основной-информации)
- [Используемые скрипты](#используемые-скрипты)
- [Используемые стили](#используемые-стили)

## Разметка HTML

### Заголовок

```html
<head>
    <meta charset="utf-8">
    <title>Tryxpath show all results</title>
    <script src="../scripts/try_xpath_functions.js"></script>
    <script src="show_all_results.js"></script>
    <link rel="stylesheet" href="show_all_results.css"/>
</head>
```

В заголовке страницы устанавливается кодировка `utf-8`, заголовок "Tryxpath show all results", подключаются скрипты `try_xpath_functions.js` и `show_all_results.js`, а также подключается таблица стилей `show_all_results.css`.

### Раздел экспорта ссылок

```html
<div>
  <h1>Export links</h1>
  <ul>
    <li><a id="export-text">Plain text</a></li>
    <li><a id="export-partly-converted">Some values are converted by JSON.stringify.</a></li>
  </ul>
</div>
```

Этот раздел предоставляет ссылки для экспорта данных в виде простого текста и частично преобразованного JSON.

### Раздел информации

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

Этот раздел отображает общую информацию, такую как сообщение, заголовок, URL и идентификатор фрейма.

### Раздел контекстной информации

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

Этот раздел предназначен для отображения контекстной информации о выполненном запросе, включая метод, выражение, указанный и фактический типы результата, а также используемый резолвер. Так же есть таблица для детальной информации.

### Раздел основной информации

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

Этот раздел отображает основную информацию о результате запроса, включая метод, выражение, указанный и фактический типы результата, используемый резолвер, а также количество найденных элементов. Так же есть таблица для детальной информации.

## Используемые скрипты

-   `../scripts/try_xpath_functions.js`: Содержит общие функции для работы с XPath.
-   `show_all_results.js`: Содержит скрипты, специфичные для страницы `show_all_results.html`, вероятно, для обработки и отображения полученных данных.

## Используемые стили

- `show_all_results.css`: Содержит стили оформления для страницы `show_all_results.html`.