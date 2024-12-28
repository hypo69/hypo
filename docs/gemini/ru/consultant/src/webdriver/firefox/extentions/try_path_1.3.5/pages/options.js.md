# Анализ кода модуля `options.js`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разделен на функции, что способствует его читаемости и поддержке.
    - Используются константы для хранения значений по умолчанию, что улучшает консистентность.
    - Проверки на валидность атрибутов и стилей перед их сохранением предотвращают ошибки.
    - Применение `Promise` для асинхронных операций, таких как загрузка CSS, делает код более надежным.
    - Код использует `browser.runtime.sendMessage` и `browser.storage.sync.set` для взаимодействия с браузерными API, что соответствует стандартам разработки расширений.
- Минусы
    - Отсутствуют docstring для функций.
    - Отсутствуют явные импорты, которые необходимо добавить.
    - Использование `try...catch` для проверки атрибутов является не самым оптимальным решением, лучше использовать более явные проверки.
    - Глобальные переменные, такие как `elementAttr`, `contextAttr`, `focusedAttr`, объявлены в глобальной области видимости модуля, что не очень хорошо с точки зрения инкапсуляции.
    - Не все ошибки обрабатываются с использованием `logger.error`.

**Рекомендации по улучшению**

1.  Добавить docstring к каждой функции и модулю.
2.  Импортировать необходимые модули, в данном случае `from src.logger.logger import logger`.
3.  Избегать использования `try...catch` в функции `isValidAttrName`, проверку можно сделать более явной.
4.  Использовать `logger.error` для логирования ошибок вместо `fu.onError`.
5.  Сделать переменные `elementAttr`, `contextAttr` и т.д. локальными в функции обратного вызова события `load`, чтобы избежать их глобальной видимости.
6.  Переписать комментарии после `#` в соответствии с требованиями инструкции.

**Оптимизированный код**

```python
"""
Модуль для управления настройками расширения TryXPath.
=========================================================================================

Этот модуль отвечает за настройку атрибутов, стилей и других параметров расширения,
которые используются для работы с XPath и отображения элементов на странице.

Модуль позволяет пользователю настраивать:
    - Атрибуты элементов, используемые для идентификации.
    - Стили всплывающего окна.

Пример использования
--------------------

.. code-block:: javascript

    // Взаимодействие с элементами DOM и настройками расширения через этот модуль.
    // window.addEventListener("load", () => { ... });

"""

from src.logger.logger import logger # Импорт модуля для логирования

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

    var testElement;

    /**
     * Проверяет, является ли имя атрибута допустимым.
     *
     * :param name: Имя атрибута для проверки.
     * :return: True, если имя атрибута допустимо, иначе False.
     */
    function isValidAttrName(name) {
        # Код проверяет, является ли имя атрибута допустимым, устанавливая его для тестового элемента.
        if (!name || typeof name !== 'string') {
            return false;
        }
        try {
            testElement.setAttribute(name, "testValue");
            testElement.removeAttribute(name);
        } catch (e) {
            # Если установка атрибута вызывает исключение, имя атрибута считается недействительным.
            return false;
        }
        # Если установка и удаление атрибута прошли успешно, имя атрибута допустимо.
        return true;
    };
    
    /**
     * Проверяет, являются ли все имена атрибутов в объекте допустимыми.
     *
     * :param names: Объект, содержащий имена атрибутов для проверки.
     * :return: True, если все имена атрибутов допустимы, иначе False.
     */
    function isValidAttrNames(names) {
        # Код итерируется по всем именам атрибутов в объекте.
        for (var p in names) {
            # Код проверяет каждое имя атрибута с помощью `isValidAttrName`.
            if (!isValidAttrName(names[p])) {
                # Если хотя бы одно имя атрибута недействительно, функция возвращает False.
                return false;
            }
        }
        # Если все имена атрибутов допустимы, функция возвращает True.
        return true;
    };

    /**
     * Проверяет, является ли длина стиля допустимой.
     *
     * :param len: Длина стиля для проверки.
     * :return: True, если длина стиля допустима, иначе False.
     */
    function isValidStyleLength(len) {
        # Код проверяет длину стиля на соответствие формату "auto" или "числоpx".
        return /^auto$|^[1-9]\\d*px$/.test(len);
    };
    
    /**
     * Загружает CSS по умолчанию.
     *
     * :return: Promise, который разрешается с текстом CSS.
     */
    function loadDefaultCss() {
        # Код возвращает Promise, который выполняет запрос на получение CSS файла.
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

    /**
     * Извлекает стили из CSS.
     *
     * :param css: Строка CSS.
     * :return: Объект со стилями ширины и высоты.
     */
    function extractBodyStyles(css) {
        var styles = {};
        # Код извлекает значения ширины и высоты из CSS с использованием регулярного выражения.
        var res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            # Если значения найдены, код присваивает их в объект `styles`.
            styles.width = res[1];
            styles.height = res[2];
        } else {
            # Если значения не найдены, код устанавливает пустые строки для ширины и высоты.
            styles.width = "";
            styles.height = "";
        }

        return styles;
    };

    /**
     * Создает CSS для всплывающего окна.
     *
     * :param bodyStyles: Объект со стилями ширины и высоты.
     * :return: Строка CSS для всплывающего окна.
     */
    function createPopupCss(bodyStyles) {
        # Код создает CSS строку для всплывающего окна с использованием переданных стилей.
        return "body{width:" + bodyStyles.width + ";height:"
            + bodyStyles.height + ";}";
    };

    window.addEventListener("load", () => {
        # Код объявляет локальные переменные для элементов DOM.
        var elementAttr = document.getElementById("element-attribute");
        var contextAttr = document.getElementById("context-attribute");
        var focusedAttr = document.getElementById("focused-attribute");
        var ancestorAttr = document.getElementById("ancestor-attribute");
        var frameAttr = document.getElementById("frame-attribute");
        var frameAncestorAttr = document.getElementById(
            "frame-ancestor-attribute");
        var style = document.getElementById("style");
        var popupBodyWidth = document.getElementById("popup-body-width");
        var popupBodyHeight = document.getElementById("popup-body-height");

        var message = document.getElementById("message");
        
        # Код отправляет сообщение расширению для получения сохраненных настроек.
        browser.runtime.sendMessage({ "timeout":0,"timeout_for_event":"presence_of_element_located","event": "loadOptions" }).then(res => {
            # Код устанавливает значения полей ввода из полученных настроек.
            elementAttr.value = res.attributes.element;
            contextAttr.value = res.attributes.context;
            focusedAttr.value = res.attributes.focused;
            ancestorAttr.value = res.attributes.focusedAncestor;
            frameAttr.value = res.attributes.frame;
            frameAncestorAttr.value = res.attributes.frameAncestor;
            
            style.value = res.css;
            # Код извлекает и устанавливает стили для всплывающего окна.
            var bodyStyles = extractBodyStyles(res.popupCss);
            popupBodyWidth.value = bodyStyles.width;
            popupBodyHeight.value = bodyStyles.height;
        }).catch(error => {
                # Логирование ошибки при загрузке опций
                logger.error('Ошибка при загрузке опций', error);
            });
        # Код добавляет обработчик события клика на кнопку "save".
        document.getElementById("save").addEventListener("click", () => {
            var styleValue = style.value;
            var attrs = Object.create(null);
            # Код извлекает значения атрибутов из полей ввода.
            attrs.element = elementAttr.value;
            attrs.context = contextAttr.value;
            attrs.focused = focusedAttr.value;
            attrs.focusedAncestor = ancestorAttr.value;
            attrs.frame = frameAttr.value;
            attrs.frameAncestor = frameAncestorAttr.value;
            var bodyStyles = {};
            bodyStyles.width = popupBodyWidth.value;
            bodyStyles.height = popupBodyHeight.value;
            
            # Код проверяет корректность введенных атрибутов.
            if (!isValidAttrNames(attrs)) {
                message.textContent = "There is a invalid attribute.";
                return;
            }
            # Код проверяет корректность введенных стилей.
            if (!(isValidStyleLength(bodyStyles.width)
                  && isValidStyleLength(bodyStyles.height))) {
                message.textContent = "There is a invalid style.";
                return;
            }
            # Код сохраняет введенные настройки в хранилище браузера.
            browser.storage.sync.set({
                "attributes": attrs,
                "css": styleValue,
                "popupCss": createPopupCss(bodyStyles)
            }).then(() => {
                message.textContent
                    = "Success. Please click the \\"Set style\\" button in "
                    + " the popup to apply new options.";
            }).catch(err => {
                #  Логирование ошибки при сохранении настроек
                 logger.error('Ошибка при сохранении настроек', err);
                message.textContent = "Failure. " + err.message;
            });
        });
        # Код добавляет обработчик события клика на кнопку "show-default".
        document.getElementById("show-default").addEventListener(
            "click", () => {
                # Код устанавливает значения по умолчанию для атрибутов.
                elementAttr.value = defaultAttributes.element;
                contextAttr.value = defaultAttributes.context;
                focusedAttr.value = defaultAttributes.focused;
                ancestorAttr.value = defaultAttributes.focusedAncestor;
                frameAttr.value = defaultAttributes.frame;
                frameAncestorAttr.value = defaultAttributes.frameAncestor;
                
                # Код загружает CSS по умолчанию и устанавливает его значение.
                loadDefaultCss().then(css => {
                    style.value = css;
                }).catch(error => {
                        # Логирование ошибки при загрузке CSS
                        logger.error('Ошибка при загрузке CSS', error);
                    });
                # Код устанавливает значения по умолчанию для стилей всплывающего окна.
                popupBodyWidth.value = defaultPopupBodyStyles.width;
                popupBodyHeight.value = defaultPopupBodyStyles.height;
            });
    });
    # Создание тестового элемента, который необходим для проверки валидности атрибутов.
    testElement = document.createElement("div");

})(window);
```