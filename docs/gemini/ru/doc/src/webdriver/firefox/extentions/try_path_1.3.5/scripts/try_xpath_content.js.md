# try_xpath_content.js

## Обзор

Данный скрипт предназначен для работы с расширением Try xpath в браузере Firefox. Он отвечает за выполнение XPath запросов, подсветку элементов на странице и взаимодействие с всплывающим окном расширения. Скрипт обрабатывает сообщения от расширения, выполняет запросы, управляет стилями и отслеживает фокус элементов.

## Содержание

1.  [Переменные и константы](#Переменные-и-константы)
2.  [Функции](#Функции)
    *   [`setAttr`](#setAttr)
    *   [`setIndex`](#setIndex)
    *   [`isFocusable`](#isFocusable)
    *   [`focusItem`](#focusItem)
    *   [`setMainAttrs`](#setMainAttrs)
    *   [`restoreAttrs`](#restoreAttrs)
    *   [`resetPrev`](#resetPrev)
    *   [`makeTypeStr`](#makeTypeStr)
    *   [`updateCss`](#updateCss)
    *   [`getFrames`](#getFrames)
    *   [`parseFrameDesignation`](#parseFrameDesignation)
    *   [`traceBlankWindows`](#traceBlankWindows)
    *   [`handleCssChange`](#handleCssChange)
    *   [`findFrameByMessage`](#findFrameByMessage)
    *   [`setFocusFrameListener`](#setFocusFrameListener)
    *   [`initBlankWindow`](#initBlankWindow)
    *   [`findStyleParent`](#findStyleParent)
    *   [`updateStyleElement`](#updateStyleElement)
    *   [`updateAllStyleElements`](#updateAllStyleElements)
    *   [`removeStyleElement`](#removeStyleElement)
    *   [`removeAllStyleElements`](#removeAllStyleElements)
    *   [`createResultMessage`](#createResultMessage)
    *   [`genericListener`](#genericListener)
3.  [Обработчики сообщений](#Обработчики-сообщений)
    *   [`setContentInfo`](#setContentInfo)
    *   [`execute`](#execute)
    *   [`focusItem`](#focusItem-1)
    *   [`focusContextItem`](#focusContextItem)
    *   [`focusFrame`](#focusFrame)
    *   [`requestShowResultsInPopup`](#requestShowResultsInPopup)
    *   [`requestShowAllResults`](#requestShowAllResults)
    *   [`resetStyle`](#resetStyle)
    *   [`setStyle`](#setStyle)
    *   [`finishInsertCss`](#finishInsertCss)
    *   [`finishRemoveCss`](#finishRemoveCss)
4.  [Слушатели событий](#Слушатели-событий)
    *   [`browser.storage.onChanged`](#browserstorageonChanged)
    *   [`window.addEventListener("message")`](#windowaddEventListenermessage)
5.  [Инициализация](#Инициализация)

## Переменные и константы

- `tx`: Псевдоним для объекта `tryxpath`.
- `fu`: Псевдоним для объекта `tryxpath.functions`.
- `dummyItem`: Пустая строка, используемая как значение по умолчанию для элемента.
- `dummyItems`: Пустой массив, используемый как значение по умолчанию для массива элементов.
- `invalidExecutionId`: `NaN`, используется как недействительный идентификатор выполнения.
- `styleElementHeader`: Заголовок для стилей, добавляемых расширением.
- `attributes`: Объект, содержащий атрибуты данных для элементов.
- `prevMsg`: Предыдущее сообщение.
- `executionCount`: Счетчик выполнения.
- `inBlankWindow`: Флаг, указывающий на то, что текущее выполнение происходит в пустом окне.
- `currentDocument`: Текущий документ.
- `contextItem`: Элемент контекста.
- `currentItems`: Массив текущих элементов.
- `focusedItem`: Элемент в фокусе.
- `focusedAncestorItems`: Массив родительских элементов элемента в фокусе.
- `currentCss`: Текущий CSS.
- `insertedStyleElements`: Map, содержащий вставленные элементы `<style>`.
- `expiredCssSet`: Объект, содержащий устаревшие CSS.
- `originalAttributes`: Map, содержащий оригинальные атрибуты элементов.

## Функции

### `setAttr`
```javascript
    function setAttr(attr, value, item) {
        fu.saveAttrForItem(item, attr, originalAttributes);
        fu.setAttrToItem(attr, value, item);
    };
```
**Описание**: Устанавливает атрибут элемента. Сохраняет старое значение атрибута перед установкой нового.
 
**Параметры**:
- `attr` (string): Название атрибута.
- `value` (string): Значение атрибута.
- `item` (HTMLElement): HTML-элемент.
 
**Возвращает**:
- `void`: Ничего не возвращает.

### `setIndex`
```javascript
    function setIndex(attr, items) {
        fu.saveAttrForItems(items, attr, originalAttributes);
        fu.setIndexToItems(attr, items);
    };
```
**Описание**: Устанавливает атрибут с индексом для массива элементов.
Сохраняет старые значения атрибутов перед установкой новых.

**Параметры**:
- `attr` (string): Название атрибута.
- `items` (Array<HTMLElement>): Массив HTML-элементов.
 
**Возвращает**:
- `void`: Ничего не возвращает.

### `isFocusable`
```javascript
    function isFocusable(item) {
        if (!item) {
            return false;
        }
        if (fu.isNodeItem(item) || fu.isAttrItem(item)) {
            return true;
        }
        return false;
    };
```
**Описание**: Проверяет, является ли элемент фокусируемым.

**Параметры**:
- `item` (any): HTML-элемент или другой элемент, который нужно проверить.

**Возвращает**:
- `boolean`: Возвращает `true`, если элемент фокусируемый, и `false` в противном случае.

### `focusItem`
```javascript
    function focusItem(item) {
        fu.removeAttrFromItem(attributes.focused, focusedItem);
        fu.removeAttrFromItems(attributes.focusedAncestor,
                               focusedAncestorItems);
        
        if (!isFocusable(item)) {
            return;
        }

        if (fu.isElementItem(item)) {
            focusedItem = item;
        } else {
            focusedItem = fu.getParentElement(item);
        }

        focusedAncestorItems = fu.getAncestorElements(focusedItem);

        setAttr(attributes.focused, "true", focusedItem);
        setIndex(attributes.focusedAncestor, focusedAncestorItems);

        focusedItem.blur();
        focusedItem.focus();
        focusedItem.scrollIntoView();
    };
```
**Описание**: Устанавливает фокус на элементе, обновляет атрибуты и прокручивает элемент в видимую область.

**Параметры**:
- `item` (any): HTML-элемент или другой элемент, на который нужно установить фокус.

**Возвращает**:
- `void`: Ничего не возвращает.

### `setMainAttrs`
```javascript
    function setMainAttrs() {
        if (contextItem !== null) {
            setAttr(attributes.context, "true", contextItem);
        }
        setIndex(attributes.element, currentItems);
    };
```
**Описание**: Устанавливает атрибуты для контекста и текущих элементов.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `restoreAttrs`
```javascript
    function restoreAttrs() {
        fu.restoreItemAttrs(originalAttributes);
        originalAttributes = new Map();
    };
```
**Описание**: Восстанавливает исходные значения атрибутов элементов и очищает map `originalAttributes`.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `resetPrev`
```javascript
    function resetPrev() {
        restoreAttrs();

        contextItem = dummyItem;
        currentItems = dummyItems;
        focusedItem = dummyItem;
        focusedAncestorItems = dummyItems;

        prevMsg = createResultMessage();
        executionCount++;
    };
```
**Описание**: Сбрасывает все переменные и подготавливает к новому выполнению XPath запроса.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `makeTypeStr`
```javascript
    function makeTypeStr(resultType) {
        if ((typeof(resultType) === "number")
            && (resultType === resultType)) {
            return fu.getxpathResultStr(resultType) + "(" + resultType + ")";
        }
        return "";
    };
```
**Описание**: Формирует строку с типом результата XPath.

**Параметры**:
- `resultType` (number): Тип результата.

**Возвращает**:
- `string`: Строка с типом результата или пустая строка.

### `updateCss`
```javascript
    function updateCss() {
        if ((currentCss === null) || (Object.keys(expiredCssSet).length > 0)){
            browser.runtime.sendMessage({
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "updateCss",
                "expiredCssSet": expiredCssSet
            });
        }
    };
```
**Описание**: Отправляет сообщение для обновления CSS, если он отсутствует или если есть устаревшие стили.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `getFrames`
```javascript
    function getFrames(spec) {
        var inds = JSON.parse(spec);
        
        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return fu.getFrameAncestry(inds).reverse();
        } else {
            throw new Error("Invalid specification. [" + spec + "]");
        }
    };
```
**Описание**: Получает массив фреймов на основе спецификации.

**Параметры**:
- `spec` (string): JSON-строка с индексами фреймов.

**Возвращает**:
- `Array<HTMLIFrameElement>`: Массив HTML-элементов фреймов.

**Вызывает исключения**:
- `Error`: Если спецификация недействительна.

### `parseFrameDesignation`
```javascript
    function parseFrameDesignation(frameDesi) {
        var inds = JSON.parse(frameDesi);
        
        if (fu.isNumberArray(inds) && (inds.length > 0)) {
            return inds;
        } else {
            throw new Error("Invalid specification. [" + frameDesi + "]");
        }
    };
```
**Описание**: Парсит обозначение фрейма.

**Параметры**:
- `frameDesi` (string): JSON-строка с индексами фреймов.

**Возвращает**:
- `Array<number>`: Массив индексов фреймов.

**Вызывает исключения**:
- `Error`: Если обозначение фрейма недействительно.

### `traceBlankWindows`
```javascript
    function traceBlankWindows(desi, win) {
        win = win || window;
        var result = Object.create(null);

        result.windows = [];
        for (let i = 0; i < desi.length; i++) {
            let frameInd = desi[i];
            if ((frameInd <= -1) || (frameInd >= win.frames.length)) {
                result.failedWindow = null;
                result.success = false;
                return result;
            }
            win = win.frames[frameInd];
            if (!fu.isBlankWindow(win)) {
                result.failedWindow = win;
                result.success = false;
                return result;
            }
            result.windows.push(win);
        }

        result.success = true;
        return result;
    };
```
**Описание**: Проверяет, является ли цепочка фреймов пустой.

**Параметры**:
- `desi` (Array<number>): Массив индексов фреймов.
- `win` (Window): Начальное окно (по умолчанию `window`).

**Возвращает**:
- `object`: Объект с информацией об успехе и фреймах. Содержит свойства `success` (boolean) и `windows` (массив Window) и `failedWindow` (window)

### `handleCssChange`
```javascript
    function handleCssChange(newCss) {
        if (currentCss === null) {
            if (newCss in expiredCssSet) {
                currentCss = newCss;
                delete expiredCssSet[newCss];
            }
        } else if (newCss !== currentCss) {
            if (newCss in expiredCssSet) {
                currentCss = newCss;
                delete expiredCssSet[newCss];
            } else {
                expiredCssSet[currentCss] = true;
                currentCss = null;
            }
        }
        // If newCss and currentCss are the same string do nothing.
    };
```
**Описание**: Обрабатывает изменения CSS.

**Параметры**:
- `newCss` (string): Новый CSS.

**Возвращает**:
- `void`: Ничего не возвращает.

### `findFrameByMessage`
```javascript
    function findFrameByMessage(event, win) {
        var ind = event.data.frameIndex;
        var subWin;
        if (ind >= 0) {
            subWin = win.frames[ind];
        } else {
            subWin = event.source;
        }
        return fu.findFrameElement(subWin, win);
    };
```
**Описание**: Находит фрейм по сообщению.

**Параметры**:
- `event` (object): Объект события.
- `win` (Window): Текущее окно.

**Возвращает**:
- `HTMLIFrameElement`: HTML-элемент фрейма.

### `setFocusFrameListener`
```javascript
    function setFocusFrameListener(win, isBlankWindow) {
        var localUpdateCss;
        if (isBlankWindow) {
            localUpdateCss = updateStyleElement.bind(null, win.document);
        } else {
            localUpdateCss = updateCss;
        }

        win.addEventListener("message", (event) => {
            if (event.data
                && event.data.message === "tryxpath-focus-frame"
                && Number.isInteger(event.data.index)
                && Number.isInteger(event.data.frameIndex)) {

                let frame = findFrameByMessage(event, win);
                if (!frame) {
                    return;
                }

                let index = event.data.index;
                localUpdateCss();
                setAttr(attributes.frame, index, frame);
                setIndex(attributes.frameAncestor,
                         fu.getAncestorElements(frame));
                if (win === win.top) {
                    frame.blur();
                    frame.focus();
                    frame.scrollIntoView();
                } else {
                    win.parent.postMessage({
                        "message": "tryxpath-focus-frame",
                        "index": ++index,
                        "frameIndex": fu.findFrameIndex(win, win.parent)
                    }, "*");
                }
            }
        });
    };
```
**Описание**: Устанавливает слушателя сообщений для фреймов.

**Параметры**:
- `win` (Window): Окно, для которого устанавливается слушатель.
- `isBlankWindow` (boolean): Флаг, указывающий, является ли окно пустым.

**Возвращает**:
- `void`: Ничего не возвращает.

### `initBlankWindow`
```javascript
    function initBlankWindow(win) {
        if (!win.tryxpath) {
            win.tryxpath = Object.create(null);
        }

        if (win.tryxpath.isInitialized) {
            return;
        }
        win.tryxpath.isInitialized = true;

        setFocusFrameListener(win, true);
    };
```
**Описание**: Инициализирует пустое окно.

**Параметры**:
- `win` (Window): Окно для инициализации.

**Возвращает**:
- `void`: Ничего не возвращает.

### `findStyleParent`
```javascript
    function findStyleParent(doc) {
        return (doc.head || doc.body || null);
    };
```
**Описание**: Находит родительский элемент для добавления стилей.

**Параметры**:
- `doc` (Document): Документ.

**Возвращает**:
- `HTMLElement`: HTML-элемент head или body, или `null`.

### `updateStyleElement`
```javascript
    function updateStyleElement(doc) {
        var css = currentCss || "";
        css = styleElementHeader + css;

        var style = insertedStyleElements.get(doc);
        if (style) {
            style.textContent = css;
            return;
        }

        var parent = findStyleParent(doc);
        if (parent) {
            let newStyle = doc.createElement("style");
            newStyle.textContent = css;
            newStyle.setAttribute("type", "text/css");
            parent.appendChild(newStyle);
            insertedStyleElements.set(doc, newStyle);
        }
    };
```
**Описание**: Обновляет или добавляет элемент `<style>` в документ.

**Параметры**:
- `doc` (Document): Документ, в котором нужно обновить стили.

**Возвращает**:
- `void`: Ничего не возвращает.

### `updateAllStyleElements`
```javascript
    function updateAllStyleElements() {
        var css = currentCss || "";
        css = styleElementHeader + css;
        for (let [doc, elem] of insertedStyleElements) {
            elem.textContent = css;
        }
    };
```
**Описание**: Обновляет все элементы `<style>`.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `removeStyleElement`
```javascript
    function removeStyleElement(doc) {
        var elem = insertedStyleElements.get(doc);
        
        if (!elem) {
            return;
        }

        var parent = elem.parentNode;
        if (parent) {
            parent.removeChild(elem);
        }
        insertedStyleElements.delete(doc);
    };
```
**Описание**: Удаляет элемент `<style>` из документа.

**Параметры**:
- `doc` (Document): Документ, из которого нужно удалить стили.

**Возвращает**:
- `void`: Ничего не возвращает.

### `removeAllStyleElements`
```javascript
    function removeAllStyleElements() {
        for (let [doc, elem] of insertedStyleElements) {
            let parent = elem.parentNode;
            if (parent) {
                parent.removeChild(elem);
            }
        }
        insertedStyleElements.clear();
    };
```
**Описание**: Удаляет все элементы `<style>`.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `createResultMessage`
```javascript
    function createResultMessage() {
        return {
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "showResultsInPopup",
            "executionId": invalidExecutionId,
            "href": "",
            "title": "",
            "message": "There is no result.",
            "main": {
                "method": "evaluate",
                "expression": "",
                "specifiedResultType": "ANY_TYPE(0)",
                "resolver": "",
                "itemDetails": []
            }
        };        
    };
```
**Описание**: Создает объект сообщения результата по умолчанию.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `object`: Объект сообщения результата.

### `genericListener`
```javascript
    function genericListener(message, sender, sendResponse) {
        var listener = genericListener.listeners[message.event];
        if (listener) {
            return listener(message, sender, sendResponse);
        }
    };
    genericListener.listeners = Object.create(null);
    browser.runtime.onMessage.addListener(genericListener);
```
**Описание**: Общий слушатель сообщений от расширения.

**Параметры**:
- `message` (object): Объект сообщения.
- `sender` (object): Объект отправителя сообщения.
- `sendResponse` (function): Функция для отправки ответа.

**Возвращает**:
- `any`: Результат выполнения конкретного слушателя или `undefined`.

## Обработчики сообщений

### `setContentInfo`
```javascript
    genericListener.listeners.setContentInfo = function (message) {
        if (!message) {
            return;
        }

        if ("attributes" in message) {
            attributes = message.attributes;
        }
    };
```
**Описание**: Обработчик сообщения для установки информации о содержимом, включая атрибуты.

**Параметры**:
- `message` (object): Объект сообщения. Содержит атрибуты для установки.

**Возвращает**:
- `void`: Ничего не возвращает.

### `execute`
```javascript
    genericListener.listeners.execute = function(message, sender) {
        resetPrev();

        updateCss();

        var sendMsg = Object.create(null);
        var main = message.main;
        sendMsg.event = "showResultsInPopup";
        sendMsg.executionId = executionCount;
        sendMsg.href = window.location.href;
        sendMsg.title = window.document.title;
        sendMsg.frameDesignation = "";

        var mainType = fu.getxpathResultNum(main.resultType);
        sendMsg.main = Object.create(null);
        sendMsg.main.method = main.method;
        sendMsg.main.expression = main.expression;
        sendMsg.main.specifiedResultType = makeTypeStr(mainType);
        sendMsg.main.resultType = "";
        sendMsg.main.resolver = main.resolver || "";
        sendMsg.main.itemDetails = [];

        contextItem = document;
        currentDocument = document;

        if ("frameDesignation" in message) {
            sendMsg.frameDesignation = message.frameDesignation;

            try {
                let desi = parseFrameDesignation(message.frameDesignation);
                let res = traceBlankWindows(desi, window);
                if (!res.success) {
                    if (res.failedWindow === null) {
                        throw new Error(
                            "The specified frame does not exist.");
                    } else {
                        res.failedWindow.postMessage({
                            "message": "tryxpath-request-message-to-popup",
                            "messageId": 1
                        }, "*");
                        return;
                    }
                }
                contextItem = res.windows.pop().document;
            } catch (e) {
                sendMsg.message = "An error occurred when getting a frame. "
                    + e.message;
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }

            inBlankWindow = true;
            currentDocument = contextItem;
        }

        if (inBlankWindow) {
            removeStyleElement(currentDocument);
        }

        if (message.context) {
            let cont = message.context;
            let contType = fu.getxpathResultNum(cont.resultType);
            sendMsg.context = Object.create(null);
            sendMsg.context.method = cont.method;
            sendMsg.context.expression = cont.expression;
            sendMsg.context.specifiedResultType = makeTypeStr(contType);
            sendMsg.context.resolver = cont.resolver || "";
            sendMsg.context.itemDetail = null;

            let contRes;
            try {
                contRes = fu.execExpr(cont.expression, cont.method, {
                    "context": contextItem,
                    "resultType": contType,
                    "resolver": cont.resolver
                });
            } catch (ex) {
                sendMsg.message = "An error occurred when getting a context. "
                    + ex.message;
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }

            if (contRes.items.length === 0) {
                sendMsg.message = "A context is not found.";
                browser.runtime.sendMessage(sendMsg);
                prevMsg = sendMsg;
                return;
            }
            contextItem = contRes.items[0];

            sendMsg.context.resultType = makeTypeStr(contRes.resultType);
            sendMsg.context.itemDetail = fu.getItemDetail(contextItem);
        }

        var mainRes;
        try {
            mainRes = fu.execExpr(main.expression, main.method, {
                "context": contextItem,
                "resultType": mainType,
                "resolver": main.resolver
            });
        } catch (ex) {
            sendMsg.message = "An error occurred when getting nodes. "
                + ex.message;
            browser.runtime.sendMessage(sendMsg);
            prevMsg = sendMsg;
            return;
        }
        currentItems = mainRes.items;

        sendMsg.message = "Success.";
        sendMsg.main.resultType = makeTypeStr(mainRes.resultType);
        sendMsg.main.itemDetails = fu.getItemDetails(currentItems);
        browser.runtime.sendMessage(sendMsg);
        prevMsg = sendMsg;

        setMainAttrs();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
        return;
    }
```
**Описание**: Обработчик сообщения для выполнения XPath запроса.

**Параметры**:
- `message` (object): Объект сообщения, содержащий параметры выполнения XPath.
- `sender` (object): Объект отправителя сообщения.

**Возвращает**:
- `void`: Ничего не возвращает.

### `focusItem`
```javascript
    genericListener.listeners.focusItem = function(message) {
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(currentItems[message.index]);
        }
    };
```
**Описание**: Обработчик сообщения для установки фокуса на элементе.

**Параметры**:
- `message` (object): Объект сообщения, содержащий индекс элемента.

**Возвращает**:
- `void`: Ничего не возвращает.

### `focusContextItem`
```javascript
    genericListener.listeners.focusContextItem = function(message) {
        if (message.executionId === executionCount) {
            if (inBlankWindow) {
                updateStyleElement(currentDocument);
            }
            focusItem(contextItem);
        }
    };
```
**Описание**: Обработчик сообщения для установки фокуса на контекстный элемент.

**Параметры**:
- `message` (object): Объект сообщения, содержащий идентификатор выполнения.

**Возвращает**:
- `void`: Ничего не возвращает.

### `focusFrame`
```javascript
    genericListener.listeners.focusFrame = function(message) {
        var win = window;

        if ("frameDesignation" in message) {
            try {
                let desi = parseFrameDesignation(message.frameDesignation);
                let res = traceBlankWindows(desi, window);
                if (!res.success) {
                    let msg;
                    if (res.failedWindow === null) {
                        throw new Error(
                            "The specified frame does not exist.");
                    } else {
                        res.failedWindow.postMessage({
                            "message": "tryxpath-request-message-to-popup",
                            "messageId": 1
                        }, "*");
                        return;
                    }
                }
                win = res.windows.pop();
            } catch (e) {
                let sendMsg = createResultMessage();
                sendMsg.message = "An error occurred when focusing a frame. "
                    + e.message;
                browser.runtime.sendMessage(sendMsg);
                return;
            }
        }

        if (win !== win.top) {
            win.parent.postMessage({
                "message": "tryxpath-focus-frame",
                "index": 0,
                "frameIndex": fu.findFrameIndex(win, win.parent)
            }, "*");
        }
    };
```
**Описание**: Обработчик сообщения для установки фокуса на фрейм.

**Параметры**:
- `message` (object): Объект сообщения, содержащий обозначение фрейма.

**Возвращает**:
- `void`: Ничего не возвращает.

### `requestShowResultsInPopup`
```javascript
    genericListener.listeners.requestShowResultsInPopup = function () {
        if (prevMsg) {
            prevMsg.event = "showResultsInPopup";
            browser.runtime.sendMessage(prevMsg);
        }
    };
```
**Описание**: Обработчик сообщения для запроса показа результатов в popup.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `requestShowAllResults`
```javascript
    genericListener.listeners.requestShowAllResults = function () {
        if (prevMsg) {
            prevMsg.event = "showAllResults";
            browser.runtime.sendMessage(prevMsg);
        }
    }
```
**Описание**: Обработчик сообщения для запроса показа всех результатов.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `resetStyle`
```javascript
    genericListener.listeners.resetStyle = function () {
        restoreAttrs();
        removeAllStyleElements();
    };
```
**Описание**: Обработчик сообщения для сброса стилей.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `setStyle`
```javascript
    genericListener.listeners.setStyle = function () {
        restoreAttrs();
        updateCss();
        if (inBlankWindow) {
            updateStyleElement(currentDocument);
        }
        setMainAttrs();
    };
```
**Описание**: Обработчик сообщения для установки стилей.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Ничего не возвращает.

### `finishInsertCss`
```javascript
    genericListener.listeners.finishInsertCss = function (message) {
        var css = message.css;
        currentCss = css;
        delete expiredCssSet[css];

        updateAllStyleElements();
    };
```
**Описание**: Обработчик сообщения об окончании вставки CSS.

**Параметры**:
- `message` (object): Объект сообщения, содержащий CSS.

**Возвращает**:
- `void`: Ничего не возвращает.

### `finishRemoveCss`
```javascript
    genericListener.listeners.finishRemoveCss = function (message) {
        var css = message.css;
        if (css === currentCss) {
            currentCss = null;
        }
        delete expiredCssSet[css];
    };
```
**Описание**: Обработчик сообщения об окончании удаления CSS.

**Параметры**:
- `message` (object): Объект сообщения, содержащий CSS.

**Возвращает**:
- `void`: Ничего не возвращает.

## Слушатели событий

### `browser.storage.onChanged`
```javascript
    browser.storage.onChanged.addListener(changes => {
        if (changes.attributes && ("newValue" in changes.attributes)) {
            attributes = changes.attributes.newValue;
        }
        if (changes.css && ("newValue" in changes.css)) {
            handleCssChange(changes.css.newValue);
        }
    });
```
**Описание**: Слушатель изменений в хранилище браузера для атрибутов и CSS.

**Параметры**:
- `changes` (object): Объект, содержащий изменения в хранилище.

**Возвращает**:
- `void`: Ничего не возвращает.

### `window.addEventListener("message")`
```javascript
    window.addEventListener("message", event => {
        if (event.data
            && (event.data.message === "tryxpath-request-message-to-popup")) {

            let sendMsg;
            switch (event.data.messageId) {
            case 0:
                sendMsg = createResultMessage();
                sendMsg.message = "An error occurred when getting a frame. "
                    + "There is a frame having frameId.";
                browser.runtime.sendMessage(sendMsg);
                break;
            case 1:
                sendMsg = createResultMessage();
                sendMsg.message = "An error occurred when focusing a frame. "
                    + "There is a frame having frameId.";
                browser.runtime.sendMessage(sendMsg);
                break;
            default:
                break;
            }
        }
    });
```
**Описание**: Слушатель сообщений от других фреймов или окон.

**Параметры**:
- `event` (object): Объект события сообщения.

**Возвращает**:
- `void`: Ничего не возвращает.

## Инициализация
```javascript
    prevMsg = createResultMessage();
    setFocusFrameListener(window, false);

    browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "requestSetContentInfo" });
```
**Описание**: Начальная инициализация переменных и установка слушателей.