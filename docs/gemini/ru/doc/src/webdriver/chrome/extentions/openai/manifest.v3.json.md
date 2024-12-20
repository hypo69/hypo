# Документация для `manifest.v3.json`

## Обзор

Файл `manifest.v3.json` представляет собой манифест расширения для браузера Chrome, который определяет метаданные и настройки расширения "OpenAI Model Interface". Манифест включает информацию о названии расширения, его версии, описании, разрешениях, скриптах, используемых в фоновом режиме, а также о действиях, связанных с кнопкой расширения и иконками. Он также включает политику безопасности содержимого.

## Содержание

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [Основные поля](#основные-поля)
    - [Разрешения](#разрешения)
    - [Фоновый скрипт](#фоновый-скрипт)
    - [Действие браузера](#действие-браузера)
    - [Иконки](#иконки)
    - [Политика безопасности содержимого](#политика-безопасности-содержимого)
- [Пример использования](#пример-использования)

## Структура JSON

### Основные поля

- `manifest_version` (integer): Версия манифеста, указывающая на используемую спецификацию (в данном случае 3).
- `name` (string): Название расширения, которое будет отображаться в интерфейсе браузера ("OpenAI Model Interface").
- `version` (string): Версия расширения (в данном случае "1.0").
- `description` (string): Описание расширения, которое кратко поясняет его назначение ("Interface for interacting with OpenAI model").

### Разрешения

- `permissions` (array of strings): Список разрешений, которые расширение запрашивает у браузера.
    - `activeTab`: Разрешение, позволяющее расширению взаимодействовать с текущей активной вкладкой.

### Фоновый скрипт

- `background` (object): Объект, определяющий настройки фонового скрипта.
    - `scripts` (array of strings): Список скриптов, которые должны быть запущены в фоновом режиме.
        - `"scripts/background.js"`:  Путь к фоновому JavaScript-файлу.
    - `persistent` (boolean): Указывает, является ли фоновый скрипт постоянно работающим (в данном случае `false`, то есть не постоянно работающий).

### Действие браузера

- `browser_action` (object): Объект, определяющий настройки для действия расширения, связанного с кнопкой в панели инструментов браузера.
    - `default_popup` (string): Путь к HTML-файлу, который будет отображаться в виде всплывающего окна при нажатии на кнопку расширения (`"index.html"`).
    - `default_icon` (object): Объект, определяющий пути к иконкам расширения различных размеров.
        - `"16"` (string): Путь к иконке размером 16x16 пикселей (`"icons/16.png"`).
        - `"48"` (string): Путь к иконке размером 48x48 пикселей (`"icons/48.png"`).
        - `"128"` (string): Путь к иконке размером 128x128 пикселей (`"icons/128.png"`).

### Иконки

- `icons` (object): Объект, определяющий пути к иконкам расширения различных размеров.
    - `"16"` (string): Путь к иконке размером 16x16 пикселей (`"icons/16.png"`).
    - `"48"` (string): Путь к иконке размером 48x48 пикселей (`"icons/48.png"`).
    - `"128"` (string): Путь к иконке размером 128x128 пикселей (`"icons/128.png"`).

### Политика безопасности содержимого

- `content_security_policy` (string):  Определяет политику безопасности содержимого для расширения.
    - `"script-src 'self'; object-src 'self';"`:  Разрешает загрузку скриптов и объектов только из собственного источника.

## Пример использования

Этот манифест используется для установки расширения в браузер Chrome.  Расширение предоставляет интерфейс для взаимодействия с моделью OpenAI через всплывающее окно, которое открывается при нажатии на иконку расширения. Фоновый скрипт `background.js` может обрабатывать различные события, связанные с работой расширения и взаимодействием с API OpenAI. Разрешение `activeTab` позволяет расширению работать с текущей вкладкой браузера. Иконки в различных разрешениях используются для отображения расширения в разных контекстах браузера.