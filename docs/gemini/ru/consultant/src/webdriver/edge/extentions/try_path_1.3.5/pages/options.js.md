# Анализ кода модуля options.js

**Качество кода**
8
-   Плюсы
    -   Код достаточно хорошо структурирован и читаем.
    -   Используются константы для значений по умолчанию.
    -   Присутствует валидация введенных данных.
    -   Используется `browser.storage.sync.set` для сохранения настроек.
    -   Есть обработка ошибок при сохранении.
-   Минусы
    -   Отсутствует документация в формате reStructuredText (RST).
    -   Используется устаревший `XMLHttpRequest`, вместо `fetch`.
    -   Обработка ошибок через `fu.onError` не логирует ошибки.
    -   Нет обработки ошибок при загрузке настроек из storage.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Много `var` вместо `const` или `let`.

**Рекомендации по улучшению**
1.  Добавить документацию в формате reStructuredText (RST) для всех функций, переменных и модуля.
2.  Заменить `XMLHttpRequest` на `fetch` для загрузки CSS.
3.  Использовать `logger.error` для логирования ошибок вместо `fu.onError`.
4.  Добавить обработку ошибок при загрузке настроек из `browser.storage`.
5.  Использовать `const` вместо `var` для переменных, которые не меняются.
6.  Привести имена переменных и функций к единому стилю.
7.  Добавить try-catch в `window.addEventListener("load", () => { ... });` для отлова ошибок.

**Оптимизированный код**
```python
"""
Модуль для управления настройками расширения tryxpath
=====================================================

Этот модуль отвечает за загрузку, сохранение и отображение настроек расширения,
таких как атрибуты элементов, стили popup окна и другие параметры.
Он также обеспечивает взаимодействие с пользовательским интерфейсом страницы настроек.
"""

from src.logger.logger import logger
# Использовать j_loads и j_loads_ns из src.utils.jjson не требуется в данном контексте.


def is_valid_attr_name(name: str) -> bool:
    """
    Проверяет, является ли переданное имя допустимым именем атрибута.

    :param name: Имя атрибута для проверки.
    :return: True, если имя атрибута допустимо, иначе False.
    """
    try:
        test_element = document.createElement("div")
        test_element.setAttribute(name, "testValue")
        return True
    except Exception as ex:
        logger.error(f'Недопустимое имя атрибута: {name}', ex)
        return False

def is_valid_attr_names(names: dict) -> bool:
    """
    Проверяет, является ли набор имен допустимыми именами атрибутов.

    :param names: Словарь с именами атрибутов для проверки.
    :return: True, если все имена атрибутов допустимы, иначе False.
    """
    for name in names:
        if not is_valid_attr_name(names[name]):
            return False
    return True

def is_valid_style_length(length: str) -> bool:
    """
    Проверяет, является ли переданная длина допустимой длиной для CSS.

    :param length: Длина CSS для проверки.
    :return: True, если длина допустима, иначе False.
    """
    return bool(/^auto$|^[1-9]\d*px$/.test(length))

async def load_default_css() -> str:
    """
    Загружает CSS по умолчанию из файла.

    :return: Текст CSS по умолчанию.
    """
    try:
        response = await fetch(browser.runtime.getURL("/css/try_xpath_insert.css"))
        if not response.ok:
             logger.error(f'Ошибка загрузки CSS: {response.status} - {response.statusText}')
             return ''
        css_text = await response.text()
        return css_text
    except Exception as ex:
        logger.error('Ошибка при загрузке CSS', ex)
        return ''


def extract_body_styles(css: str) -> dict:
    """
    Извлекает стили для body из CSS.

    :param css: CSS текст, из которого нужно извлечь стили.
    :return: Словарь со стилями ширины и высоты.
    """
    styles = {}
    res = /width:(.+?);.*height:(.+?);/.exec(css)
    if res:
        styles["width"] = res[1]
        styles["height"] = res[2]
    else:
        styles["width"] = ""
        styles["height"] = ""
    return styles

def create_popup_css(body_styles: dict) -> str:
    """
    Создает CSS для popup окна.

    :param body_styles: Словарь со стилями ширины и высоты.
    :return: CSS текст для popup окна.
    """
    return f"body{{width:{body_styles['width']};height:{body_styles['height']};}}"

def main():
    """
    Основная функция для инициализации и управления страницей настроек.
    """
    element_attr = document.getElementById("element-attribute")
    context_attr = document.getElementById("context-attribute")
    focused_attr = document.getElementById("focused-attribute")
    ancestor_attr = document.getElementById("ancestor-attribute")
    frame_attr = document.getElementById("frame-attribute")
    frame_ancestor_attr = document.getElementById("frame-ancestor-attribute")
    style = document.getElementById("style")
    popup_body_width = document.getElementById("popup-body-width")
    popup_body_height = document.getElementById("popup-body-height")
    message = document.getElementById("message")
    try:
        browser.runtime.sendMessage({"timeout": 0, "timeout_for_event": "presence_of_element_located",
                                    "event": "loadOptions"}).then(res => {
            if not res:
                logger.error('Не удалось загрузить настройки')
                return
            element_attr.value = res.attributes.element
            context_attr.value = res.attributes.context
            focused_attr.value = res.attributes.focused
            ancestor_attr.value = res.attributes.focusedAncestor
            frame_attr.value = res.attributes.frame
            frame_ancestor_attr.value = res.attributes.frameAncestor
            style.value = res.css
            body_styles = extract_body_styles(res.popupCss)
            popup_body_width.value = body_styles["width"]
            popup_body_height.value = body_styles["height"]
            }).catch(ex => {
                logger.error('Ошибка при получении настроек', ex)
                message.textContent = "Failure. " + ex.message
            })


        document.getElementById("save").addEventListener("click", () => {
            style_value = style.value
            attrs = {}
            attrs["element"] = element_attr.value
            attrs["context"] = context_attr.value
            attrs["focused"] = focused_attr.value
            attrs["focusedAncestor"] = ancestor_attr.value
            attrs["frame"] = frame_attr.value
            attrs["frameAncestor"] = frame_ancestor_attr.value
            body_styles = {}
            body_styles["width"] = popup_body_width.value
            body_styles["height"] = popup_body_height.value

            if not is_valid_attr_names(attrs):
                message.textContent = "There is a invalid attribute."
                return

            if not (is_valid_style_length(body_styles["width"])
                    and is_valid_style_length(body_styles["height"])):
                message.textContent = "There is a invalid style."
                return

            browser.storage.sync.set({
                "attributes": attrs,
                "css": style_value,
                "popupCss": create_popup_css(body_styles)
            }).then(() => {
                message.textContent = "Success. Please click the \\"Set style\\" button in " \
                                    + " the popup to apply new options."
            }).catch(err => {
                logger.error('Ошибка при сохранении настроек', err)
                message.textContent = "Failure. " + err.message
            })
        })

        document.getElementById("show-default").addEventListener("click", async () => {
            element_attr.value = default_attributes["element"]
            context_attr.value = default_attributes["context"]
            focused_attr.value = default_attributes["focused"]
            ancestor_attr.value = default_attributes["focusedAncestor"]
            frame_attr.value = default_attributes["frame"]
            frame_ancestor_attr.value = default_attributes["frameAncestor"]

            try:
                css = await load_default_css()
                style.value = css
            except Exception as ex:
                logger.error('Ошибка при загрузке CSS по умолчанию', ex)

            popup_body_width.value = default_popup_body_styles["width"]
            popup_body_height.value = default_popup_body_styles["height"]
        })
    except Exception as ex:
        logger.error('Ошибка при инициализации страницы', ex)

    test_element = document.createElement("div")

    window.addEventListener("load", main);

    const default_attributes = {
        "element": "data-tryxpath-element",
        "context": "data-tryxpath-context",
        "focused": "data-tryxpath-focused",
        "focusedAncestor": "data-tryxpath-focused-ancestor",
        "frame": "data-tryxpath-frame",
        "frameAncestor": "data-tryxpath-frame-ancestor"
    }

    const default_popup_body_styles = {
        "width": "367px",
        "height": "auto"
    }

})(window);
```