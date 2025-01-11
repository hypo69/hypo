# Анализ кода модуля options.js

**Качество кода: 7/10**
 -  Плюсы
    - Код разбит на функции, что улучшает читаемость и организацию.
    - Используются константы для хранения значений по умолчанию, что облегчает их изменение и поддержку.
    - Присутствует валидация вводимых данных, что предотвращает ошибки.
    - Обработка асинхронных операций через `Promise` и `async/await`.
 -  Минусы
    - Отсутствует документация для функций и переменных, что усложняет понимание кода.
    - Используются глобальные переменные, что может привести к проблемам в будущем.
    - Избыточное использование `try-catch` в функции `isValidAttrName`, можно заменить проверкой через `if` и вызов `logger.error`.
    - Нет обработки ошибок при отправке сообщения `browser.runtime.sendMessage` в функции `load`.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Код не соответствует стандарту оформления docstring в Python.

**Рекомендации по улучшению**
1. Добавить документацию в формате RST для всех функций и переменных.
2. Заменить глобальные переменные на локальные, где это возможно.
3. Использовать `logger.error` для обработки ошибок вместо `try-catch` в `isValidAttrName`.
4. Добавить обработку ошибок при отправке сообщения `browser.runtime.sendMessage`.
5. Использовать `from src.logger.logger import logger` для логирования ошибок.
6. Удалить лишний код или комментарии (например, `alias`, `undefined`)
7. Переписать функцию `isValidAttrName` для исключения `try-catch` и использовать `logger.error`.
8. Переписать функцию `loadDefaultCss` для обработки ошибок с помощью `logger.error`.

**Оптимизированный код**
```python
"""
Модуль для настройки параметров расширения tryxpath.
=========================================================================================

Этот модуль отвечает за сохранение и загрузку настроек расширения,
таких как атрибуты элементов, стили CSS и размеры всплывающего окна.

Пример использования
--------------------

Пример использования:

.. code-block:: javascript

    // Загрузка и установка сохраненных настроек при загрузке страницы
    window.addEventListener("load", () => {
        // Инициализация элементов управления и загрузка настроек
    });

    // Сохранение настроек при нажатии кнопки "Сохранить"
    document.getElementById("save").addEventListener("click", () => {
       // Сохранение настроек в storage
    });
"""
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns
(function (window) {
    "use strict";

    # Удаляем alias так как он не используется
    # var tx = tryxpath;
    # var fu = tryxpath.functions;
    var document = window.document;

    # Константы для атрибутов и стилей по умолчанию
    const defaultAttributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    };

    const defaultPopupBodyStyles = {
        "width": "367px",
        "height": "auto"
    };

    # Переменные для элементов управления и значений
    var elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;

    def isValidAttrName(name):
        """
        Проверяет, является ли имя атрибута допустимым.

        Args:
            name (str): Имя атрибута для проверки.

        Returns:
            bool: True, если имя атрибута допустимо, False в противном случае.
        """
        # Код создает тестовый элемент и проверяет, можно ли установить атрибут с заданным именем
        testElement = document.createElement("div");
        if not hasattr(testElement, 'setAttribute'):
            logger.error(f'Элемент не имеет метода setAttribute')
            return False
        try:
            testElement.setAttribute(name, "testValue");
            return True;
        except Exception as e:
            logger.error(f"Недопустимое имя атрибута: {name}, {e}", exc_info=True)
            return False;


    def isValidAttrNames(names):
        """
        Проверяет, являются ли все имена атрибутов в объекте допустимыми.

        Args:
            names (dict): Объект, содержащий имена атрибутов для проверки.

        Returns:
            bool: True, если все имена атрибутов допустимы, False в противном случае.
        """
        # Код проверяет каждое имя атрибута на допустимость
        for p in names:
            if not isValidAttrName(names[p]):
                return False;
        return True;

    def isValidStyleLength(len):
        """
         Проверяет, является ли длина стиля допустимой.

        Args:
            len (str): Длина стиля для проверки.

        Returns:
            bool: True, если длина стиля допустима, False в противном случае.
        """
        # Код проверяет, соответствует ли длина стилю формату "auto" или "числоpx"
        return /^auto$|^[1-9]\d*px$/.test(len);

    def loadDefaultCss():
        """
        Загружает CSS по умолчанию из файла.

        Returns:
            Promise: Promise, который разрешается с текстом CSS или отклоняется с ошибкой.
        """
        # Код выполняет загрузку CSS из файла
        return new Promise((resolve, reject) => {
            var req = new XMLHttpRequest();
            req.open("GET",
                     browser.runtime.getURL("/css/try_xpath_insert.css"));
            req.responseType = "text";
            req.onreadystatechange = function () {
                if (req.readyState === XMLHttpRequest.DONE) {
                    if (req.status == 200) {
                        resolve(req.responseText);
                    } else {
                        logger.error(f'Не удалось загрузить CSS. Код ошибки: {req.status}')
                    }

                }
            };
            req.onerror = function(e){
                logger.error(f'Ошибка загрузки CSS: {e}')
                reject(e)
            }
            req.send();
        });

    def extractBodyStyles(css):
        """
        Извлекает ширину и высоту из CSS.

        Args:
            css (str): CSS, из которого нужно извлечь стили.

        Returns:
             dict: Объект, содержащий ширину и высоту.
        """
        # Код извлекает ширину и высоту из CSS
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

    def createPopupCss(bodyStyles):
         """
        Создает CSS для всплывающего окна.

        Args:
            bodyStyles (dict): Объект, содержащий ширину и высоту всплывающего окна.

        Returns:
            str: CSS для всплывающего окна.
        """
         # Код формирует CSS для всплывающего окна
        return "body{width:" + bodyStyles.width + ";height:"\
            + bodyStyles.height + ";}";

    window.addEventListener("load", () => {
    # Код получает ссылки на HTML-элементы
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

    # Код отправляет сообщение для получения настроек и устанавливает их значения
        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "loadOptions" }).then(res => {
            elementAttr.value = res.attributes.element;
            contextAttr.value = res.attributes.context;
            focusedAttr.value = res.attributes.focused;
            ancestorAttr.value = res.attributes.focusedAncestor;
            frameAttr.value = res.attributes.frame;
            frameAncestorAttr.value = res.attributes.frameAncestor;
            style.value = res.css;

            var bodyStyles = extractBodyStyles(res.popupCss);
            popupBodyWidth.value = bodyStyles.width;
            popupBodyHeight.value = bodyStyles.height;
        }).catch(err => logger.error(f'Ошибка при загрузке параметров: {err}', exc_info=True));

    # Код добавляет обработчик события "click" на кнопку "save"
        document.getElementById("save").addEventListener("click", () => {
            var styleValue = style.value;
            var attrs = Object.create(null);
            attrs.element = elementAttr.value;
            attrs.context = contextAttr.value;
            attrs.focused = focusedAttr.value;
            attrs.focusedAncestor = ancestorAttr.value;
            attrs.frame = frameAttr.value;
            attrs.frameAncestor = frameAncestorAttr.value;
            var bodyStyles = {};
            bodyStyles.width = popupBodyWidth.value;
            bodyStyles.height = popupBodyHeight.value;

            if (!isValidAttrNames(attrs)) {
                message.textContent = "There is a invalid attribute.";
                return;
            }
            if (!(isValidStyleLength(bodyStyles.width)
                  && isValidStyleLength(bodyStyles.height))) {
                message.textContent = "There is a invalid style.";
                return;
            }
        # Код сохраняет настройки в storage
            browser.storage.sync.set({
                "attributes": attrs,
                "css": styleValue,
                "popupCss": createPopupCss(bodyStyles)
            }).then(() => {
                message.textContent
                    = "Success. Please click the \\"Set style\\" button in "
                    + " the popup to apply new options.";
            }).catch(err => {
                message.textContent = "Failure. " + err.message;
            });
        });

    # Код добавляет обработчик события "click" на кнопку "show-default"
        document.getElementById("show-default").addEventListener(
            "click", () => {
                elementAttr.value = defaultAttributes.element;
                contextAttr.value = defaultAttributes.context;
                focusedAttr.value = defaultAttributes.focused;
                ancestorAttr.value = defaultAttributes.focusedAncestor;
                frameAttr.value = defaultAttributes.frame;
                frameAncestorAttr.value = defaultAttributes.frameAncestor;
                loadDefaultCss().then(css => {
                    style.value = css;
                }).catch(err => logger.error(f'Ошибка загрузки default CSS: {err}', exc_info=True));

                popupBodyWidth.value = defaultPopupBodyStyles.width;
                popupBodyHeight.value = defaultPopupBodyStyles.height;
            });
    });
    # Создаем тестовый элемент
    testElement = document.createElement("div");

})(window);
```