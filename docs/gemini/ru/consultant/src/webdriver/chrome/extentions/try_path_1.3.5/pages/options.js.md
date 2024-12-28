# Анализ кода модуля options.js

**Качество кода**
7
 -  Плюсы
    - Код достаточно хорошо структурирован и разбит на функции.
    - Используется `browser.storage.sync.set` для сохранения настроек.
    - Присутствует обработка событий `load` и `click`.
 -  Минусы
    - Отсутствуют docstring для функций и переменных.
    - Используется стандартный `XMLHttpRequest` вместо `fetch`.
    - Нет логирования ошибок с использованием `logger`.
    - Присутствует избыточное использование `try-catch`.

**Рекомендации по улучшению**
1.  Добавить docstring для всех функций и переменных, используя reStructuredText (RST) формат.
2.  Заменить `XMLHttpRequest` на `fetch` для загрузки CSS.
3.  Добавить логирование ошибок с использованием `logger.error`.
4.  Убрать избыточное использование `try-catch` блоков.
5.  Использовать `async/await` для асинхронных операций, где это возможно.
6.  Переименовать переменные и функции для лучшей читаемости и соответствия общему стилю.

**Оптимизированный код**
```python
"""
Модуль для управления настройками расширения TryXPath.
=========================================================================================

Этот модуль предоставляет интерфейс для настройки атрибутов, стилей и размеров всплывающего окна
расширения TryXPath.

"""
import json
from src.logger.logger import logger #  Импорт модуля логирования
# from src.utils.jjson import j_loads, j_loads_ns

(function (window, undefined) {
    "use strict";

    # alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    var document = window.document;

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

    var elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;

    /**
     * Проверяет, является ли переданное имя допустимым именем атрибута.
     *
     * :param name: Имя атрибута для проверки.
     * :type name: str
     * :return: `true`, если имя атрибута допустимо, `false` в противном случае.
     * :rtype: bool
     */
    function isValidAttrName(name) {
        try {
            # код пытается установить атрибут с переданным именем, чтобы проверить его валидность
            testElement.setAttribute(name, "testValue");
        } catch (e) {
            # в случае ошибки (невалидное имя атрибута) функция вернет `false`
            return false;
        }
        # если установка атрибута прошла успешно, возвращается `true`
        return true;
    };

    /**
     * Проверяет, являются ли все имена атрибутов в переданном объекте допустимыми.
     *
     * :param names: Объект, содержащий имена атрибутов для проверки.
     * :type names: dict
     * :return: `true`, если все имена атрибутов допустимы, `false` в противном случае.
     * :rtype: bool
     */
    function isValidAttrNames(names) {
        # код перебирает все имена атрибутов в объекте
        for (var p in names) {
            # для каждого имени проверяется его валидность
            if (!isValidAttrName(names[p])) {
                # если хотя бы одно имя невалидно, возвращается `false`
                return false;
            }
        }
        # если все имена валидны, возвращается `true`
        return true;
    };

    /**
     * Проверяет, является ли переданная длина CSS-стиля допустимой.
     *
     * :param len: Длина CSS-стиля для проверки.
     * :type len: str
     * :return: `true`, если длина допустима (`auto` или `XXXpx`), `false` в противном случае.
     * :rtype: bool
     */
    function isValidStyleLength(len) {
        # код проверяет, соответствует ли переданная длина одному из допустимых форматов
        return /^auto$|^[1-9]\\d*px$/.test(len);
    };

    /**
     * Загружает CSS по умолчанию из файла.
     *
     * :return: Promise, который разрешается с текстом CSS или отклоняется с ошибкой.
     * :rtype: Promise<str>
     */
    async function loadDefaultCss() {
        #  Код загружает CSS по умолчанию
        try{
            const response = await fetch(browser.runtime.getURL("/css/try_xpath_insert.css"));
            if (!response.ok) {
                # Если запрос не удался, код генерирует ошибку
                throw new Error(`HTTP error! status: ${response.status}`);
            }
           #  Код возвращает текст ответа
            return await response.text();
        } catch (error) {
            #  Код логирует ошибку при загрузке CSS
            logger.error('Ошибка загрузки CSS по умолчанию', error);
            throw error;
        }
    };

    /**
     * Извлекает стили ширины и высоты из CSS.
     *
     * :param css: CSS, из которого нужно извлечь стили.
     * :type css: str
     * :return: Объект со стилями ширины и высоты.
     * :rtype: dict
     */
    function extractBodyStyles(css) {
        var styles = {};
        # Код ищет значения ширины и высоты в CSS
        var res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            # Если значения найдены, код сохраняет их в объект `styles`
            styles.width = res[1];
            styles.height = res[2];
        } else {
            # Если значения не найдены, код устанавливает пустые строки
            styles.width = "";
            styles.height = "";
        }
        # Код возвращает объект со стилями
        return styles;
    };

    /**
     * Создает CSS для всплывающего окна с заданными стилями тела.
     *
     * :param bodyStyles: Объект со стилями ширины и высоты.
     * :type bodyStyles: dict
     * :return: CSS для всплывающего окна.
     * :rtype: str
     */
    function createPopupCss(bodyStyles) {
        # Код возвращает строку с CSS для всплывающего окна
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };

    window.addEventListener("load", async () => {
        #  Код получает DOM элементы
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
        #  Код отправляет сообщение для получения настроек
        try {
            const res = await browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "loadOptions" });
            #  Код устанавливает значения из полученных настроек
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
        } catch (error) {
            #  Код логирует ошибку при загрузке настроек
            logger.error('Ошибка при загрузке настроек', error);
        }

        document.getElementById("save").addEventListener("click", async () => {
            var styleValue = style.value;
            var attrs = Object.create(null);
            #  Код получает значения атрибутов из DOM элементов
            attrs.element = elementAttr.value;
            attrs.context = contextAttr.value;
            attrs.focused = focusedAttr.value;
            attrs.focusedAncestor = ancestorAttr.value;
            attrs.frame = frameAttr.value;
            attrs.frameAncestor = frameAncestorAttr.value;
            var bodyStyles = {};
            bodyStyles.width = popupBodyWidth.value;
            bodyStyles.height = popupBodyHeight.value;
            # Проверка валидности атрибутов
            if (!isValidAttrNames(attrs)) {
                message.textContent = "There is a invalid attribute.";
                return;
            }
            # Проверка валидности стилей
            if (!(isValidStyleLength(bodyStyles.width)
                  && isValidStyleLength(bodyStyles.height))) {
                message.textContent = "There is a invalid style.";
                return;
            }
            #  Код сохраняет настройки
            try {
               await browser.storage.sync.set({
                    "attributes": attrs,
                    "css": styleValue,
                    "popupCss": createPopupCss(bodyStyles)
                });
                #  Код выводит сообщение об успешном сохранении
                message.textContent
                    = "Success. Please click the \\"Set style\\" button in "
                    + " the popup to apply new options.";
            } catch (err) {
                #  Код выводит сообщение об ошибке
                message.textContent = "Failure. " + err.message;
                #  Код логирует ошибку при сохранении настроек
                logger.error('Ошибка при сохранении настроек', err)
            }

        });

        document.getElementById("show-default").addEventListener(
            "click", async () => {
                #  Код устанавливает значения атрибутов по умолчанию
                elementAttr.value = defaultAttributes.element;
                contextAttr.value = defaultAttributes.context;
                focusedAttr.value = defaultAttributes.focused;
                ancestorAttr.value = defaultAttributes.focusedAncestor;
                frameAttr.value = defaultAttributes.frame;
                frameAncestorAttr.value = defaultAttributes.frameAncestor;
                
                #  Код загружает CSS по умолчанию и устанавливает его
                try {
                    const css = await loadDefaultCss();
                    style.value = css;
                }
                catch(error) {
                     #  Код логирует ошибку при загрузке CSS по умолчанию
                    logger.error('Ошибка при загрузке CSS по умолчанию', error);
                }
                # Код устанавливает размеры окна по умолчанию
                popupBodyWidth.value = defaultPopupBodyStyles.width;
                popupBodyHeight.value = defaultPopupBodyStyles.height;
            });
    });

    testElement = document.createElement("div");

})(window);