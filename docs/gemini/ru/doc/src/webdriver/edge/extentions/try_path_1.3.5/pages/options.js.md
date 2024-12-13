# Настройки расширения TryXPath

## Обзор

Этот файл `options.js` отвечает за логику страницы настроек расширения TryXPath. Он позволяет пользователю настраивать атрибуты HTML, используемые для идентификации элементов, а также CSS-стили всплывающего окна.

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
5. [Обработчики событий](#обработчики-событий)

## Константы

### `defaultAttributes`
   - **Описание**: Объект, содержащий значения атрибутов по умолчанию для элементов.
   - **Тип**: `Object`
   - **Свойства**:
     - `"element"`: `"data-tryxpath-element"`
     - `"context"`: `"data-tryxpath-context"`
     - `"focused"`: `"data-tryxpath-focused"`
     - `"focusedAncestor"`: `"data-tryxpath-focused-ancestor"`
     - `"frame"`: `"data-tryxpath-frame"`
     - `"frameAncestor"`: `"data-tryxpath-frame-ancestor"`

### `defaultPopupBodyStyles`
   - **Описание**: Объект, содержащий стили по умолчанию для тела всплывающего окна.
   - **Тип**: `Object`
   - **Свойства**:
     - `"width"`: `"367px"`
     - `"height"`: `"auto"`

## Переменные

### `elementAttr`
   - **Описание**: Ссылка на HTML-элемент ввода атрибута элемента.
   - **Тип**: `HTMLElement`

### `contextAttr`
   - **Описание**: Ссылка на HTML-элемент ввода атрибута контекста.
   - **Тип**: `HTMLElement`

### `focusedAttr`
   - **Описание**: Ссылка на HTML-элемент ввода атрибута фокусировки.
   - **Тип**: `HTMLElement`

### `ancestorAttr`
   - **Описание**: Ссылка на HTML-элемент ввода атрибута предка с фокусом.
   - **Тип**: `HTMLElement`

### `frameAttr`
   - **Описание**: Ссылка на HTML-элемент ввода атрибута фрейма.
   - **Тип**: `HTMLElement`

### `frameAncestorAttr`
   - **Описание**: Ссылка на HTML-элемент ввода атрибута предка фрейма.
   - **Тип**: `HTMLElement`

### `style`
   - **Описание**: Ссылка на HTML-элемент textarea для CSS.
   - **Тип**: `HTMLElement`

### `popupBodyWidth`
   - **Описание**: Ссылка на HTML-элемент ввода ширины всплывающего окна.
   - **Тип**: `HTMLElement`

### `popupBodyHeight`
   - **Описание**: Ссылка на HTML-элемент ввода высоты всплывающего окна.
   - **Тип**: `HTMLElement`

### `message`
   - **Описание**: Ссылка на HTML-элемент для отображения сообщений.
   - **Тип**: `HTMLElement`

### `testElement`
   - **Описание**: Тестовый элемент div, используемый для проверки допустимости имени атрибута.
   - **Тип**: `HTMLElement`

## Функции

### `isValidAttrName`

**Описание**: Проверяет, является ли предоставленное имя допустимым именем атрибута HTML-элемента.

**Параметры**:
   - `name` (str): Имя атрибута, которое нужно проверить.

**Возвращает**:
   - `boolean`: `true`, если имя атрибута допустимо, `false` в противном случае.

**Вызывает исключения**:
   -  `Error`: Возникает, если имя атрибута не является допустимым.

```javascript
 function isValidAttrName(name) {
        try {
            testElement.setAttribute(name, "testValue");
        } catch (e) {
            return false;
        }
        return true;
    };
```

### `isValidAttrNames`

**Описание**: Проверяет, являются ли все имена атрибутов в данном объекте допустимыми именами атрибутов HTML.

**Параметры**:
   - `names` (object): Объект, содержащий имена атрибутов для проверки.

**Возвращает**:
   - `boolean`: `true`, если все имена атрибутов допустимы, `false` в противном случае.
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
### `isValidStyleLength`
**Описание**: Проверяет, является ли предоставленная длина допустимой длиной CSS, которая должна быть либо "auto", либо в виде "XXXpx".

**Параметры**:
   - `len` (str): Длина CSS, которую нужно проверить.

**Возвращает**:
   - `boolean`: `true`, если длина допустима, `false` в противном случае.
```javascript
    function isValidStyleLength(len) {
        return /^auto$|^[1-9]\\d*px$/.test(len);
    };
```

### `loadDefaultCss`
**Описание**: Загружает CSS по умолчанию из файла `try_xpath_insert.css`.

**Возвращает**:
   - `Promise<string>`: Promise, который разрешается текстом CSS или отклоняется при ошибке.
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

### `extractBodyStyles`
**Описание**: Извлекает стили ширины и высоты из строки CSS.

**Параметры**:
   - `css` (str): Строка CSS, из которой нужно извлечь стили.

**Возвращает**:
   - `object`: Объект со свойствами `width` и `height`. Если стили не найдены, свойства будут пустыми строками.
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

### `createPopupCss`
**Описание**: Создает строку CSS для всплывающего окна на основе предоставленных стилей.

**Параметры**:
   - `bodyStyles` (object): Объект, содержащий свойства `width` и `height`.

**Возвращает**:
   - `string`: Строка CSS, которая устанавливает ширину и высоту тела всплывающего окна.
```javascript
    function createPopupCss(bodyStyles) {
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };
```

## Обработчики событий

### `window.addEventListener("load", ...)`
   - **Описание**: Обработчик события `load` окна.
   - **Действия**:
     1. Получает ссылки на элементы HTML из DOM.
     2. Отправляет сообщение фоновому скрипту для получения сохраненных параметров.
     3. Заполняет поля ввода параметрами из ответа.
     4. Добавляет обработчик события `click` для кнопки "Сохранить".
     5. Добавляет обработчик события `click` для кнопки "По умолчанию".

### `document.getElementById("save").addEventListener("click", ...)`
   - **Описание**: Обработчик события `click` для кнопки "Сохранить".
   - **Действия**:
     1. Получает значения из полей ввода.
     2. Проверяет допустимость имен атрибутов и стилей.
     3. Сохраняет значения в хранилище браузера.
     4. Выводит сообщение об успехе или ошибке.

### `document.getElementById("show-default").addEventListener("click", ...)`
   - **Описание**: Обработчик события `click` для кнопки "По умолчанию".
   - **Действия**:
     1. Устанавливает значения полей ввода атрибутов по умолчанию.
     2. Загружает и устанавливает CSS по умолчанию.
     3. Устанавливает значения полей ввода размеров всплывающего окна по умолчанию.