# `background.js`

## Обзор

Этот файл является фоновым скриптом для расширения Firefox. Он слушает события нажатия на иконку расширения и выполняет скрипт `contentScript.js` в активной вкладке.

## Оглавление

- [Обзор](#обзор)
- [События](#события)
    - [`browser.browserAction.onClicked`](#browserbrowseractiononclicked)

## События

### `browser.browserAction.onClicked`

**Описание**:
   Этот обработчик событий срабатывает, когда пользователь нажимает на иконку расширения в браузере. Он выполняет `contentScript.js` в активной вкладке.

**Параметры**:
   - `tab` (object): Объект, представляющий вкладку, в которой произошло событие нажатия на иконку расширения.

**Пример использования**
```javascript
browser.browserAction.onClicked.addListener((tab) => {
    browser.scripting.executeScript({
        target: { tabId: tab.id },
        files: ["contentScript.js"],
    });
});
```