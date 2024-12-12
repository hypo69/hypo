# Анализ кода модуля options.js

**Качество кода**

7/10
- Плюсы
    - Код достаточно хорошо структурирован и разделен на функции.
    - Используются константы для атрибутов и стилей по умолчанию.
    - Есть обработка событий для кнопок "Сохранить" и "Показать по умолчанию".
- Минусы
    - Отсутствует описание модуля и функций в формате reStructuredText (RST).
    - Присутствует избыточное использование `try-catch`, которое можно заменить на `logger.error`.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов, хотя в инструкции это указано.
    - Некоторые переменные объявлены через `var` вместо `const` или `let`.
    - Нет обработки ошибок при получении стилей из `extractBodyStyles`.

**Рекомендации по улучшению**

1.  Добавить описание модуля и функций в формате reStructuredText (RST).
2.  Заменить `try-catch` на `logger.error` для обработки ошибок.
3.  Использовать `const` и `let` вместо `var` там, где это возможно.
4.  Добавить импорт `logger` из `src.logger.logger`.
5.  Использовать `j_loads` или `j_loads_ns` если потребуется чтение файлов.
6.  Добавить обработку ошибок в функции `extractBodyStyles`, если это необходимо.
7.  Добавить более подробные комментарии к коду, особенно к сложным частям.
8.  Переименовать `fu` в более понятное имя (например, `utils`).

**Оптимизированный код**

```python
"""
Модуль для настройки параметров расширения TryXPath.
===========================================================================

Этот модуль отвечает за управление настройками расширения TryXPath,
включая атрибуты элементов, стили CSS и другие параметры. Пользователи
могут сохранять свои настройки, а также восстанавливать значения по умолчанию.

Пример использования
--------------------

.. code-block:: javascript

    // Этот код выполняется при загрузке страницы параметров
    // и позволяет пользователю взаимодействовать с элементами
    // управления для настройки расширения.
"""
import logging

from src.logger.logger import logger

(function (window, undefined) {
    "use strict";

    # alias
    # Код создает алиас `tx` для доступа к функциональности `tryxpath`.
    const tx = tryxpath;
    # Код создает алиас `utils` для доступа к функциям `tryxpath`.
    const utils = tryxpath.functions;

    const document = window.document;

    # Объект с атрибутами по умолчанию для элементов.
    const defaultAttributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };

    # Объект со стилями по умолчанию для всплывающего окна.
    const defaultPopupBodyStyles = {
        "width": "367px",
        "height": "auto"
    };

    let elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;

    /**
     * Проверяет, является ли переданное имя допустимым именем атрибута HTML элемента.
     *
     * :param name: Имя атрибута для проверки.
     * :return: `True`, если имя атрибута допустимо, `False` в противном случае.
     */
    function isValidAttrName(name) {
        try {
            # Код пытается установить атрибут с заданным именем для проверки его валидности.
            testElement.setAttribute(name, "testValue");
        } catch (e) {
            # Если при установке атрибута возникает ошибка, имя считается недопустимым.
            return false;
        }
        # Если атрибут успешно установлен, имя считается допустимым.
        return true;
    };

     /**
      * Проверяет, являются ли все имена атрибутов в переданном объекте допустимыми.
      *
      * :param names: Объект, содержащий имена атрибутов для проверки.
      * :return: `True`, если все имена атрибутов допустимы, `False` в противном случае.
      */
    function isValidAttrNames(names) {
        for (let p in names) {
            # Код проверяет каждое имя атрибута с помощью функции isValidAttrName.
            if (!isValidAttrName(names[p])) {
                return false;
            }
        }
        return true;
    };

    /**
     * Проверяет, является ли переданная длина строки допустимой для стилей CSS (`auto` или `Npx`).
     *
     * :param len: Строка, представляющая длину для проверки.
     * :return: `True`, если длина строки допустима, `False` в противном случае.
     */
    function isValidStyleLength(len) {
        # Код использует регулярное выражение для проверки допустимости длины.
        return /^auto$|^[1-9]\\d*px$/.test(len);
    };

    /**
     * Загружает CSS-файл по умолчанию для расширения.
     *
     * :return: Promise, который разрешается с текстом CSS-файла.
     */
    function loadDefaultCss() {
        return new Promise((resolve, reject) => {
            const req = new XMLHttpRequest();
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

    /**
     * Извлекает стили ширины и высоты из CSS-строки.
     *
     * :param css: Строка, содержащая CSS-стили.
     * :return: Объект со стилями ширины и высоты, или пустые строки, если не найдены.
     */
    function extractBodyStyles(css) {
        const styles = {};

        # Код извлекает значения ширины и высоты из CSS-строки с помощью регулярного выражения.
        const res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            styles.width = res[1];
            styles.height = res[2];
        } else {
            # Если регулярное выражение не находит совпадений, то присваивает пустые строки.
             styles.width = "";
             styles.height = "";
        }

        return styles;
    };

     /**
      * Создаёт CSS-строку для всплывающего окна на основе переданных стилей.
      *
      * :param bodyStyles: Объект, содержащий стили ширины и высоты.
      * :return: Строка, содержащая CSS для всплывающего окна.
      */
    function createPopupCss(bodyStyles) {
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };

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

        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "loadOptions" }).then(res => {
            # Код устанавливает значения атрибутов элементов управления из полученных данных.
            elementAttr.value = res.attributes.element;
            contextAttr.value = res.attributes.context;
            focusedAttr.value = res.attributes.focused;
            ancestorAttr.value = res.attributes.focusedAncestor;
            frameAttr.value = res.attributes.frame;
            frameAncestorAttr.value = res.attributes.frameAncestor;
            
            style.value = res.css;

            # Код извлекает и устанавливает стили ширины и высоты всплывающего окна.
            const bodyStyles = extractBodyStyles(res.popupCss);
            popupBodyWidth.value = bodyStyles.width;
            popupBodyHeight.value = bodyStyles.height;
        }).catch(utils.onError);

        document.getElementById("save").addEventListener("click", () => {
             # Код получает текущее значение CSS из элемента управления.
            const styleValue = style.value;
            const attrs = Object.create(null);
            # Код получает текущие значения атрибутов из элементов управления.
            attrs.element = elementAttr.value;
            attrs.context = contextAttr.value;
            attrs.focused = focusedAttr.value;
            attrs.focusedAncestor = ancestorAttr.value;
            attrs.frame = frameAttr.value;
            attrs.frameAncestor = frameAncestorAttr.value;
            const bodyStyles = {};
            # Код получает текущие значения ширины и высоты всплывающего окна.
            bodyStyles.width = popupBodyWidth.value;
            bodyStyles.height = popupBodyHeight.value;

            # Код проверяет валидность имен атрибутов.
            if (!isValidAttrNames(attrs)) {
                message.textContent = "There is a invalid attribute.";
                return;
            }
            # Код проверяет валидность стилей ширины и высоты.
            if (!(isValidStyleLength(bodyStyles.width)
                  && isValidStyleLength(bodyStyles.height))) {
                message.textContent = "There is a invalid style.";
                return;
            }

            # Код сохраняет параметры расширения в хранилище.
            browser.storage.sync.set({
                "attributes": attrs,
                "css": styleValue,
                "popupCss": createPopupCss(bodyStyles)
            }).then(() => {
                 # Код выводит сообщение об успешном сохранении.
                message.textContent
                    = "Success. Please click the \\"Set style\\" button in "
                    + " the popup to apply new options.";
            }).catch(err => {
                 # Код выводит сообщение об ошибке сохранения.
                message.textContent = "Failure. " + err.message;
                logger.error("Ошибка сохранения настроек", err)
            });
        });

        document.getElementById("show-default").addEventListener(
            "click", () => {
                 # Код устанавливает значения атрибутов по умолчанию.
                elementAttr.value = defaultAttributes.element;
                contextAttr.value = defaultAttributes.context;
                focusedAttr.value = defaultAttributes.focused;
                ancestorAttr.value = defaultAttributes.focusedAncestor;
                frameAttr.value = defaultAttributes.frame;
                frameAncestorAttr.value = defaultAttributes.frameAncestor;
                
                # Код загружает CSS по умолчанию и устанавливает его.
                loadDefaultCss().then(css => {
                    style.value = css;
                }).catch(utils.onError);

                # Код устанавливает стили ширины и высоты всплывающего окна по умолчанию.
                popupBodyWidth.value = defaultPopupBodyStyles.width;
                popupBodyHeight.value = defaultPopupBodyStyles.height;
            });
    });

    # Код создает тестовый элемент div для проверки валидности атрибутов.
    testElement = document.createElement("div");

})(window);