# Анализ кода модуля options.js

**Качество кода**
1.  Соответствие требованиям по оформлению кода: 7/10
    -   Плюсы:
        -   Код разбит на функции, что улучшает читаемость и повторное использование.
        -   Используются константы для атрибутов и стилей по умолчанию.
        -   Есть обработка событий `load` и `click`.
    -   Минусы:
        -   Отсутствуют docstring для функций и переменных.
        -   Не используется `j_loads` или `j_loads_ns`.
        -   Обработка ошибок не использует `logger.error`.
        -   Смешанный стиль именования переменных (camelCase и snake_case).
        -   Комментарии `#`  не соответствуют инструкции.
        -   Используется устаревший `XMLHttpRequest`, желательно заменить на `fetch`.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring для всех функций и переменных, используя reStructuredText (RST).
2.  **Импорты**: Нет необходимости в дополнительных импортах, так как используется глобальная переменная `browser`.
3.  **Обработка ошибок**: Заменить блоки `try-catch` на использование `logger.error` для логирования ошибок.
4.  **Стиль кода**: Привести к единому стилю именования переменных.
5. **AJAX** Заменить `XMLHttpRequest` на `fetch`.
6.  **Комментарии**: Переписать все комментарии в формате RST, объясняя каждый блок кода.
7.  **JSON**: Нет необходимости использовать `j_loads` или `j_loads_ns`, так как нет операций с JSON.

**Оптимизированный код**

```python
"""
Модуль для управления опциями расширения TryXPath.
=========================================================================================

Этот модуль отвечает за настройку атрибутов, стилей и сохранения их в хранилище браузера.
Также включает в себя функциональность для сброса настроек к значениям по умолчанию.
"""
from src.logger.logger import logger # Импортируем logger

(function (window, undefined) {
    "use strict";

    # alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

    # Константы с атрибутами по умолчанию
    const defaultAttributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };

    # Константы со стилями всплывающего окна по умолчанию
    const defaultPopupBodyStyles = {
        "width": "367px",
        "height": "auto"
    };

    # Объявление переменных
    var elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;

    /**
     * Проверяет, является ли имя атрибута валидным.
     *
     * :param name: Имя атрибута для проверки.
     * :type name: str
     * :return: Возвращает True, если имя атрибута валидно, иначе False.
     * :rtype: bool
     */
    function isValidAttrName(name) {
        try {
            # Код пытается установить атрибут на тестовый элемент.
            testElement.setAttribute(name, "testValue");
        } catch (e) {
            # Если возникает ошибка, возвращается False, т.к. атрибут невалидный.
            return false;
        }
        # Если ошибок не было, возвращается True.
        return true;
    };

    /**
     * Проверяет, являются ли имена атрибутов в объекте валидными.
     *
     * :param names: Объект с именами атрибутов для проверки.
     * :type names: dict
     * :return: Возвращает True, если все имена атрибутов валидны, иначе False.
     * :rtype: bool
     */
    function isValidAttrNames(names) {
        for (var p in names) {
            # Код проверяет каждый атрибут с помощью функции isValidAttrName.
            if (!isValidAttrName(names[p])) {
                # Если хотя бы один атрибут невалидный, возвращается False.
                return false;
            }
        }
        # Если все атрибуты валидны, возвращается True.
        return true;
    };

    /**
     * Проверяет, является ли длина стиля CSS валидной.
     *
     * :param len: Длина стиля CSS для проверки.
     * :type len: str
     * :return: Возвращает True, если длина стиля валидна, иначе False.
     * :rtype: bool
     */
    function isValidStyleLength(len) {
        # Код проверяет длину стиля на соответствие формату 'auto' или 'XXXpx'.
        return /^auto$|^[1-9]\\d*px$/.test(len);
    };

    /**
     * Загружает CSS по умолчанию из файла.
     *
     * :return: Promise, который разрешается с текстом CSS или отклоняется с ошибкой.
     * :rtype: Promise
     */
    function loadDefaultCss() {
        return new Promise((resolve, reject) => {
            # Код создаёт запрос GET для получения CSS файла.
            fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
            .then(response => {
                if (!response.ok) {
                    # Если запрос не успешен, вызывается reject.
                    reject(new Error(`HTTP error! status: ${response.status}`));
                }
                return response.text();
            })
            .then(text => {
                # Если запрос успешен, вызывается resolve с текстом CSS.
                resolve(text);
            })
            .catch(error => {
                # Код обрабатывает ошибки, возникшие во время fetch.
                logger.error('Ошибка при загрузке CSS по умолчанию', error);
                reject(error);
            });
        });
    };

    /**
     * Извлекает стили ширины и высоты из CSS.
     *
     * :param css: CSS строка, из которой нужно извлечь стили.
     * :type css: str
     * :return: Объект со стилями ширины и высоты.
     * :rtype: dict
     */
    function extractBodyStyles(css) {
        var styles = {};

        # Код ищет ширину и высоту с помощью регулярного выражения.
        var res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            # Код сохраняет ширину и высоту, если найдено.
            styles.width = res[1];
            styles.height = res[2];
        } else {
            # Код устанавливает пустые значения, если не найдено.
            styles.width = "";
            styles.height = "";
        }

        return styles;
    };

    /**
     * Создает CSS для всплывающего окна на основе стилей.
     *
     * :param bodyStyles: Объект со стилями ширины и высоты.
     * :type bodyStyles: dict
     * :return: Строка CSS для всплывающего окна.
     * :rtype: str
     */
    function createPopupCss(bodyStyles) {
        # Код создаёт строку CSS, используя ширину и высоту.
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };

    # Код устанавливает слушателя события load на window.
    window.addEventListener("load", () => {
        # Код получает элементы DOM по их ID.
        elementAttr = document.getElementById("element-attribute");
        contextAttr = document.getElementById("context-attribute");
        focusedAttr = document.getElementById("focused-attribute");
        ancestorAttr = document.getElementById("ancestor-attribute");
        frameAttr = document.getElementById("frame-attribute");
        frameAncestorAttr = document.getElementById(
            "frame-ancestor-attribute");
        style = document.getElementById("style");
        popupBodyWidth = document.getElementById("popup-body-width");
        popupBodyHeight = document.getElementById("popup-body-height");

        message = document.getElementById("message");

        # Код отправляет сообщение в runtime для получения настроек.
        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "loadOptions" }).then(res => {
            # Код устанавливает значения полей на основе полученных данных.
            elementAttr.value = res.attributes.element;
            contextAttr.value = res.attributes.context;
            focusedAttr.value = res.attributes.focused;
            ancestorAttr.value = res.attributes.focusedAncestor;
            frameAttr.value = res.attributes.frame;
            frameAncestorAttr.value = res.attributes.frameAncestor;
            
            style.value = res.css;

            # Код извлекает стили тела всплывающего окна.
            var bodyStyles = extractBodyStyles(res.popupCss);
            popupBodyWidth.value = bodyStyles.width;
            popupBodyHeight.value = bodyStyles.height;
        }).catch(fu.onError);

         # Код устанавливает слушателя события click на кнопку "save".
        document.getElementById("save").addEventListener("click", () => {
            var styleValue = style.value;
            var attrs = Object.create(null);
            # Код собирает значения атрибутов из полей ввода.
            attrs.element = elementAttr.value;
            attrs.context = contextAttr.value;
            attrs.focused = focusedAttr.value;
            attrs.focusedAncestor = ancestorAttr.value;
            attrs.frame = frameAttr.value;
            attrs.frameAncestor = frameAncestorAttr.value;
            var bodyStyles = {};
            bodyStyles.width = popupBodyWidth.value;
            bodyStyles.height = popupBodyHeight.value;

            # Код проверяет валидность атрибутов и стилей.
            if (!isValidAttrNames(attrs)) {
                message.textContent = "There is a invalid attribute.";
                return;
            }
            if (!(isValidStyleLength(bodyStyles.width)
                  && isValidStyleLength(bodyStyles.height))) {
                message.textContent = "There is a invalid style.";
                return;
            }

            # Код сохраняет настройки в storage.
            browser.storage.sync.set({
                "attributes": attrs,
                "css": styleValue,
                "popupCss": createPopupCss(bodyStyles)
            }).then(() => {
                # Код выводит сообщение об успехе.
                message.textContent
                    = "Success. Please click the \\"Set style\\" button in "
                    + " the popup to apply new options.";
            }).catch(err => {
                # Код выводит сообщение об ошибке.
                message.textContent = "Failure. " + err.message;
                logger.error('Ошибка при сохранении настроек', err);
            });
        });

        # Код устанавливает слушателя события click на кнопку "show-default".
        document.getElementById("show-default").addEventListener(
            "click", () => {
                # Код устанавливает значения атрибутов по умолчанию.
                elementAttr.value = defaultAttributes.element;
                contextAttr.value = defaultAttributes.context;
                focusedAttr.value = defaultAttributes.focused;
                ancestorAttr.value = defaultAttributes.focusedAncestor;
                frameAttr.value = defaultAttributes.frame;
                frameAncestorAttr.value = defaultAttributes.frameAncestor;
                
                # Код загружает стили CSS по умолчанию.
                loadDefaultCss().then(css => {
                    style.value = css;
                }).catch(fu.onError);

                # Код устанавливает стили всплывающего окна по умолчанию.
                popupBodyWidth.value = defaultPopupBodyStyles.width;
                popupBodyHeight.value = defaultPopupBodyStyles.height;
            });
    });
    # Код создаёт тестовый элемент div.
    testElement = document.createElement("div");

})(window);
```