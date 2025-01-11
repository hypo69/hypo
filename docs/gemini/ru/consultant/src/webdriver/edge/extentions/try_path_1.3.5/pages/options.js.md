## Анализ кода модуля options.js

**Качество кода**

-   Соответствие требованиям по оформлению кода: 7/10
    -   Плюсы:
        -   Код в целом структурирован и логичен.
        -   Используются `const` для неизменяемых значений.
        -   Есть обработка событий `load` и `click`.
        -   Используются асинхронные операции с `Promise`.
        -   Код содержит проверку валидности имен атрибутов и стилей.
    -   Минусы:
        -   Отсутствует документация кода (docstring)
        -   Используется стандартный `XMLHttpRequest` вместо `fetch`.
        -   Используется `try-catch` в `isValidAttrName` вместо `logger.error`.
        -   Переменные объявлены через `var`, что может привести к проблемам с областью видимости, рекомендуется использовать `let` и `const`
        -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`
        -   Не используется импорт `logger` из `src.logger.logger`
        -   В некоторых местах используется `message.textContent`, предпочтительнее использовать `logger.info` и `logger.error`.

**Рекомендации по улучшению**

1.  **Добавить описание модуля**:
    -   В начале файла необходимо добавить описание модуля с использованием docstring.
2.  **Документация кода**:
    -   Добавить документацию в формате RST для каждой функции и переменной.
3.  **Использование `fetch`**:
    -   Заменить `XMLHttpRequest` на `fetch` для более современного подхода к сетевым запросам.
4.  **Использовать `logger`**:
    -   Использовать `logger.error` вместо `try-catch` для обработки ошибок в `isValidAttrName`.
    -   Использовать `logger.info` и `logger.error` вместо `message.textContent` для вывода сообщений.
    -   Импортировать `logger` из `src.logger.logger`.
5.  **Использовать `let` и `const`**:
    -   Заменить `var` на `let` для переменных, которые могут изменяться, и `const` для констант.
6.  **Использовать `j_loads` или `j_loads_ns`**:
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` при чтении данных из файлов (если это необходимо).
7.  **Рефакторинг кода**:
    -   Упростить код, где это возможно, например, вынести повторяющиеся части в отдельные функции.
8.  **Обработка ошибок**:
    -   Улучшить обработку ошибок, используя `logger.error` и `return False`.
9.  **Улучшить сообщения**:
    -   Использовать более информативные сообщения об ошибках и успехе.

**Оптимизированный код**

```python
"""
Модуль для настройки расширения Try Xpath.
=========================================================================================

Этот модуль отвечает за управление настройками расширения, такими как атрибуты элементов, стили всплывающего окна и другие параметры.
Он обеспечивает сохранение, загрузку и применение настроек, а также позволяет сбрасывать настройки к значениям по умолчанию.

Пример использования
--------------------

.. code-block:: javascript

   // Загрузка настроек по умолчанию
   document.getElementById('show-default').click();

   // Сохранение пользовательских настроек
   document.getElementById('save').click();
"""
from src.logger.logger import logger # Импорт логгера

(function (window, undefined) {
    "use strict";

    # alias
    const tx = tryxpath;
    const fu = tryxpath.functions;

    const document = window.document;

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

    let elementAttr, contextAttr, focusedAttr, ancestorAttr, frameAttr,
        frameAncestorAttr, style, popupBodyWidth, popupBodyHeight, message,
        testElement;

    
    def isValidAttrName(name: str) -> bool:
        """
        Проверяет, является ли заданное имя допустимым именем атрибута HTML-элемента.

        Args:
            name (str): Имя атрибута для проверки.

        Returns:
            bool: True, если имя атрибута допустимо, False в противном случае.
        """
        try:
            # Код пытается установить атрибут с переданным именем на тестовый элемент
            testElement.setAttribute(name, "testValue");
            return True
        except Exception as e:
            # Если при установке атрибута возникает ошибка, возвращается False
            logger.error(f'Недопустимое имя атрибута {name}', e)
            return False
    

    def isValidAttrNames(names: dict) -> bool:
        """
        Проверяет, являются ли все заданные имена атрибутов допустимыми.

        Args:
            names (dict): Словарь с именами атрибутов для проверки.

        Returns:
            bool: True, если все имена атрибутов допустимы, False в противном случае.
        """
        for p in names:
            # Если хотя бы одно имя атрибута не является допустимым, функция возвращает False
            if not isValidAttrName(names[p]):
                return False
        return True
    

    def isValidStyleLength(len: str) -> bool:
        """
        Проверяет, является ли заданная длина допустимым значением длины CSS.

        Args:
            len (str): Длина для проверки.

        Returns:
            bool: True, если длина допустима, False в противном случае.
        """
        # Код проверяет, соответствует ли строка формату "auto" или "числоpx"
        return /^auto$|^[1-9]\\d*px$/.test(len);
    

    async def loadDefaultCss() -> str:
        """
        Асинхронно загружает содержимое CSS-файла по умолчанию.

        Returns:
            str: Содержимое CSS-файла.

        Raises:
             Exception: Если при загрузке файла возникает ошибка
        """
        try:
             # Код выполняет загрузку CSS файла
            const response = await fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
            # Код проверяет статус ответа
            if not response.ok:
               logger.error(f"Ошибка загрузки файла стилей, статус {response.status}")
               return ""
            return await response.text();
        except Exception as e:
            # Если во время выполнения возникает ошибка, возвращается пустая строка и логируется ошибка
           logger.error("Ошибка загрузки CSS", e);
           return ""
    

    def extractBodyStyles(css: str) -> dict:
        """
        Извлекает стили ширины и высоты из CSS-строки.

        Args:
            css (str): CSS-строка для анализа.

        Returns:
            dict: Словарь, содержащий ширину и высоту.
        """
        const styles = {};
        # Код выполняет извлечение ширины и высоты из строки
        const res = /width:(.+?);.*height:(.+?);/.exec(css);
        if (res) {
            styles.width = res[1];
            styles.height = res[2];
        } else {
            styles.width = "";
            styles.height = "";
        }

        return styles;
    

    def createPopupCss(bodyStyles: dict) -> str:
        """
        Создает CSS-строку для всплывающего окна на основе предоставленных стилей.

        Args:
            bodyStyles (dict): Словарь со стилями ширины и высоты.

        Returns:
            str: CSS-строка для всплывающего окна.
        """
        # Код формирует строку со стилями
        return "body{width:" + bodyStyles.width + ";height:"\
            + bodyStyles.height + ";}";
    

    window.addEventListener("load", () => {
        # Код находит HTML элементы по их id
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
            # Код устанавливает значения в поля ввода
            elementAttr.value = res.attributes.element;
            contextAttr.value = res.attributes.context;
            focusedAttr.value = res.attributes.focused;
            ancestorAttr.value = res.attributes.focusedAncestor;
            frameAttr.value = res.attributes.frame;
            frameAncestorAttr.value = res.attributes.frameAncestor;
            
            style.value = res.css;

            const bodyStyles = extractBodyStyles(res.popupCss);
            popupBodyWidth.value = bodyStyles.width;
            popupBodyHeight.value = bodyStyles.height;
        }).catch(fu.onError);

        document.getElementById("save").addEventListener("click", () => {
            # Код получает значения из полей ввода
            const styleValue = style.value;
            const attrs = Object.create(null);
            attrs.element = elementAttr.value;
            attrs.context = contextAttr.value;
            attrs.focused = focusedAttr.value;
            attrs.focusedAncestor = ancestorAttr.value;
            attrs.frame = frameAttr.value;
            attrs.frameAncestor = frameAncestorAttr.value;
            const bodyStyles = {};
            bodyStyles.width = popupBodyWidth.value;
            bodyStyles.height = popupBodyHeight.value;
            # Код проверяет валидность атрибутов
            if (!isValidAttrNames(attrs)) {
                logger.error("There is a invalid attribute.");
                return;
            }
            # Код проверяет валидность стилей
            if (!(isValidStyleLength(bodyStyles.width)
                  && isValidStyleLength(bodyStyles.height))) {
                logger.error("There is a invalid style.");
                return;
            }
            # Код сохраняет настройки
            browser.storage.sync.set({
                "attributes": attrs,
                "css": styleValue,
                "popupCss": createPopupCss(bodyStyles)
            }).then(() => {
                logger.info("Success. Please click the \\"Set style\\" button in "
                    + " the popup to apply new options.");
            }).catch(err => {
                logger.error(f"Failure. {err.message}");
            });
        });

        document.getElementById("show-default").addEventListener(
            "click", () => {
                # Код устанавливает значения по умолчанию
                elementAttr.value = defaultAttributes.element;
                contextAttr.value = defaultAttributes.context;
                focusedAttr.value = defaultAttributes.focused;
                ancestorAttr.value = defaultAttributes.focusedAncestor;
                frameAttr.value = defaultAttributes.frame;
                frameAncestorAttr.value = defaultAttributes.frameAncestor;
                
                loadDefaultCss().then(css => {
                    style.value = css;
                }).catch(fu.onError);
                
                popupBodyWidth.value = defaultPopupBodyStyles.width;
                popupBodyHeight.value = defaultPopupBodyStyles.height;
            });
    });

    testElement = document.createElement("div");

})(window);