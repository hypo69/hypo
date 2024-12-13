# `try_xpath_background.js`

## Обзор

Данный файл является фоновым скриптом для расширения try_xpath. Он отвечает за обработку сообщений, управление стилями и состоянием всплывающего окна, а также за взаимодействие с хранилищем.

## Оглавление

1. [Обзор](#обзор)
2. [Глобальные переменные](#глобальные-переменные)
3. [Функции](#функции)
    - [`loadDefaultCss`](#loaddefaultcss)
    - [`genericListener`](#genericlistener)
    - [`genericListener.listeners.storePopupState`](#genericlistenerlistenersstorepopupstate)
    - [`genericListener.listeners.requestRestorePopupState`](#genericlistenerlistenersrequestrestorepopupstate)
    - [`genericListener.listeners.requestInsertStyleToPopup`](#genericlistenerlistenersrequestinsertstyletopopup)
    - [`genericListener.listeners.showAllResults`](#genericlistenerlistenersshowallresults)
    - [`genericListener.listeners.loadResults`](#genericlistenerlistenersloadresults)
    - [`genericListener.listeners.updateCss`](#genericlistenerlistenersupdatecss)
    - [`genericListener.listeners.loadOptions`](#genericlistenerlistenersloadoptions)
    - [`genericListener.listeners.requestSetContentInfo`](#genericlistenerlistenersrequestsetcontentinfo)
4. [События](#события)
    - [`browser.storage.onChanged`](#browserstorageonchanged)
    - [`browser.storage.sync.get`](#browserstoragesyncget)

## Глобальные переменные

- `tx`: Псевдоним для `tryxpath`.
- `fu`: Псевдоним для `tryxpath.functions`.
- `popupState`: Состояние всплывающего окна (может быть `null`).
- `popupCss`: CSS для всплывающего окна по умолчанию.
- `results`: Объект для хранения результатов.
- `css`: CSS для вставки в страницу.
- `attributes`: Объект, содержащий имена атрибутов для выделения элементов.

## Функции

### `loadDefaultCss`

**Описание**: Загружает CSS по умолчанию из файла `/css/try_xpath_insert.css`.

**Возвращает**:
- `Promise<string>`: Промис, который разрешается с текстом CSS.

### `genericListener`

**Описание**: Обработчик входящих сообщений от контентных скриптов.

**Параметры**:
- `message` (object): Объект сообщения.
- `sender` (object): Объект отправителя сообщения.
- `sendResponse` (function): Функция обратного вызова для отправки ответа.

**Возвращает**:
- `any`: Возвращает результат работы конкретного обработчика, если он найден.

### `genericListener.listeners.storePopupState`

**Описание**: Сохраняет состояние всплывающего окна.

**Параметры**:
- `message` (object): Объект сообщения, содержащий состояние всплывающего окна.

### `genericListener.listeners.requestRestorePopupState`

**Описание**: Отправляет запрос на восстановление состояния всплывающего окна.

### `genericListener.listeners.requestInsertStyleToPopup`

**Описание**: Отправляет запрос на вставку CSS во всплывающее окно.

### `genericListener.listeners.showAllResults`

**Описание**: Сохраняет результаты и открывает новую вкладку для отображения всех результатов.

**Параметры**:
- `message` (object): Объект сообщения, содержащий результаты.
- `sender` (object): Объект отправителя сообщения.

### `genericListener.listeners.loadResults`

**Описание**: Отправляет сохраненные результаты обратно контентному скрипту.

**Параметры**:
- `message` (object): Объект сообщения.
- `sender` (object): Объект отправителя сообщения.
- `sendResponse` (function): Функция обратного вызова для отправки ответа.

**Возвращает**:
- `boolean`: `true`, чтобы указать, что ответ будет отправлен асинхронно.

### `genericListener.listeners.updateCss`

**Описание**: Обновляет CSS на странице. Удаляет старый CSS и вставляет новый.

**Параметры**:
- `message` (object): Объект сообщения, содержащий `expiredCssSet`.
- `sender` (object): Объект отправителя сообщения.

### `genericListener.listeners.loadOptions`

**Описание**: Отправляет сохраненные параметры обратно контентному скрипту.

**Параметры**:
- `message` (object): Объект сообщения.
- `sender` (object): Объект отправителя сообщения.
- `sendResponse` (function): Функция обратного вызова для отправки ответа.

**Возвращает**:
- `boolean`: `true`, чтобы указать, что ответ будет отправлен асинхронно.

### `genericListener.listeners.requestSetContentInfo`

**Описание**: Отправляет запрос на обновление информации о контенте.

**Параметры**:
- `message` (object): Объект сообщения.
- `sender` (object): Объект отправителя сообщения.

## События

### `browser.storage.onChanged`

**Описание**: Обработчик события изменения в хранилище. Обновляет глобальные переменные `attributes`, `css` и `popupCss`, если они изменились в хранилище.

### `browser.storage.sync.get`

**Описание**: Загружает настройки из синхронизированного хранилища. Если CSS не был сохранен, загружает CSS по умолчанию. Обновляет глобальные переменные `attributes`, `css` и `popupCss` после загрузки.