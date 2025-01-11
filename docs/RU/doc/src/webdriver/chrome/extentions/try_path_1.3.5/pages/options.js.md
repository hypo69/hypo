# Настройки расширения Try Xpath

## Обзор

Этот файл `options.js` отвечает за управление настройками расширения Try Xpath. Он позволяет пользователю настраивать атрибуты HTML, используемые для идентификации элементов, контекста, фокуса, фреймов, а также стили всплывающего окна.

## Оглавление

1. [Обзор](#обзор)
2. [Константы](#константы)
3. [Переменные](#переменные)
4. [Функции](#функции)
    - [`isValidAttrName`](#isvalidattrname)
    - [`isValidAttrNames`](#isvalidattrnames)
    - [`isValidStyleLength`](#isvalidstylelength)
    - [`loadDefaultCss`](#loaddefaultcss)
    - [`extractBodyStyles`](#extractbodystyles)
    - [`createPopupCss`](#createpopupcss)
5. [События](#события)

## Константы

### `defaultAttributes`

**Описание**: Объект, содержащий атрибуты по умолчанию для элементов, контекста, фокуса и фреймов.
```javascript
    const defaultAttributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };
```

### `defaultPopupBodyStyles`

**Описание**: Объект, содержащий стили по умолчанию для всплывающего окна.
```javascript
    const defaultPopupBodyStyles = {
        "width": "367px",
        "height": "auto"
    };
```

## Переменные

### `elementAttr`, `contextAttr`, `focusedAttr`, `ancestorAttr`, `frameAttr`, `frameAncestorAttr`, `style`, `popupBodyWidth`, `popupBodyHeight`, `message`, `testElement`
**Описание**: Глобальные переменные, используемые для хранения элементов DOM, значений атрибутов и стилей.
```javascript
    var elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;
```

## Функции

### `isValidAttrName`
```javascript
    function isValidAttrName(name) {
        try {
            testElement.setAttribute(name, "testValue");
        } catch (ex) {
            return false;
        }
        return true;
    };
```
**Описание**: Проверяет, является ли имя атрибута допустимым для установки на HTML-элемент.

**Параметры**:
- `name` (string): Имя атрибута для проверки.

**Возвращает**:
- `boolean`: `true`, если имя атрибута допустимо, иначе `false`.

### `isValidAttrNames`
```javascript
    function isValidAttrNames(names) {
        for (var p in names) {
            if (!isValidAttrName(names[p])) {
                return false;
            }
        }
        return true;
    };
```
**Описание**: Проверяет, являются ли все имена атрибутов в объекте допустимыми.

**Параметры**:
- `names` (object): Объект, содержащий имена атрибутов для проверки.

**Возвращает**:
- `boolean`: `true`, если все имена атрибутов допустимы, иначе `false`.

### `isValidStyleLength`
```javascript
   function isValidStyleLength(len) {
        return /^auto$|^[1-9]\\d*px$/.test(len);
    };
```
**Описание**: Проверяет, является ли строка допустимой длиной для CSS.

**Параметры**:
- `len` (string): Строка для проверки.

**Возвращает**:
- `boolean`: `true`, если строка является допустимой длиной, иначе `false`.

### `loadDefaultCss`
```javascript
    function loadDefaultCss() {
        return new Promise((resolve, reject) => {
            var req = new XMLHttpRequest();
            req.open("GET",
                     browser.runtime.getURL("/css/try_xpath_insert.css"));
            req.responseType = "text";
            req.onreadystatechange = function () {
                if (req.readyState === XMLHttpRequest.DONE) {
                    resolve(req.responseText);
                }
            };
            req.send();
        });
    };
```
**Описание**: Загружает CSS по умолчанию из файла `try_xpath_insert.css`.

**Возвращает**:
- `Promise<string>`: Promise, разрешающийся в текст CSS, или отклоняется с ошибкой.

### `extractBodyStyles`
```javascript
    function extractBodyStyles(css) {
        var styles = {};

        var res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            styles.width = res[1];
            styles.height = res[2];
        } else {
            styles.width = "";
            styles.height = "";
        }

        return styles;
    };
```
**Описание**: Извлекает стили ширины и высоты из CSS-строки.

**Параметры**:
- `css` (string): Строка, содержащая CSS-стили.

**Возвращает**:
- `object`: Объект со свойствами `width` и `height`.

### `createPopupCss`
```javascript
    function createPopupCss(bodyStyles) {
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };
```
**Описание**: Создаёт CSS-строку для всплывающего окна.

**Параметры**:
- `bodyStyles` (object): Объект, содержащий свойства `width` и `height`.

**Возвращает**:
- `string`: CSS-строка для всплывающего окна.

## События

### `window.addEventListener("load", ...)`

**Описание**: Обработчик события загрузки страницы.

1.  **Получение элементов DOM**
    - Находит и сохраняет ссылки на элементы ввода и другие элементы управления на странице.

2.  **Получение сохраненных параметров**
    - Отправляет сообщение расширению для получения сохраненных параметров, таких как атрибуты и стили.
    - Заполняет поля ввода значениями из сохраненных параметров.

3.  **Обработчик кнопки "save"**
    - Собирает значения атрибутов и стилей из полей ввода.
    - Проверяет корректность имен атрибутов и стилей.
    - Сохраняет новые значения атрибутов и стилей с помощью `browser.storage.sync.set`.
    - Выводит сообщение об успехе или неудаче.

4.  **Обработчик кнопки "show-default"**
    - Устанавливает значения атрибутов и стилей по умолчанию.
    - Загружает CSS по умолчанию и обновляет поле стиля.
    - Устанавливает размеры всплывающего окна по умолчанию.