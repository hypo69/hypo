# Анализ кода модуля options.js

**Качество кода**
8
-   Плюсы
    -   Код хорошо структурирован и разбит на функции.
    -   Используется `browser.storage.sync.set` для сохранения данных.
    -   Присутствует обработка событий `load` и `click`.
    -   Используются Promise для асинхронных операций.
-   Минусы
    -   Отсутствует docstring для модуля, функций и переменных.
    -   Не используется `logger` для логирования ошибок.
    -   Не используются константы для повторяющихся значений.
    -   Используются магические строки, которые нужно вынести в константы.
    -   Отсутствует проверка на корректность значений `browser.runtime.sendMessage` и `browser.storage.sync.set` (нужно ловить и логировать ошибки).
    -   Не используется `async/await` для асинхронных операций.
    -   Не все переменные объявлены с `const` или `let`.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, функций и переменных.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить `var` на `const` или `let` там где это возможно.
4.  Использовать `async/await` для асинхронных операций.
5.  Вынести повторяющиеся значения в константы.
6.  Добавить обработку ошибок для `browser.runtime.sendMessage` и `browser.storage.sync.set`.
7.  Использовать более информативные сообщения об ошибках.
8.  Удалить неиспользуемые переменные `tx` и `fu`.
9.  Переименовать переменные `p` на более информативные.
10. Добавить комментарии для блоков кода.

**Оптимизированный код**

```python
"""
Модуль для управления настройками расширения TryXPath.
======================================================

Этот модуль отвечает за управление настройками расширения TryXPath, такими как атрибуты элементов, стили
и настройки CSS. Он обеспечивает взаимодействие с пользовательским интерфейсом страницы опций и сохранение
настроек в хранилище браузера.

Пример использования
--------------------

При открытии страницы опций этот модуль инициализирует поля ввода значениями из хранилища, а также
обрабатывает события сохранения и восстановления настроек по умолчанию.
"""
from src.logger.logger import logger

# Константы для атрибутов по умолчанию
DEFAULT_ATTRIBUTES = {
    "element": "data-tryxpath-element",
    "context": "data-tryxpath-context",
    "focused": "data-tryxpath-focused",
    "focusedAncestor": "data-tryxpath-focused-ancestor",
    "frame": "data-tryxpath-frame",
    "frameAncestor": "data-tryxpath-frame-ancestor"
}

# Константы для стилей по умолчанию
DEFAULT_POPUP_BODY_STYLES = {
    "width": "367px",
    "height": "auto"
}

# Объявление переменных
element_attr = None
context_attr = None
focused_attr = None
ancestor_attr = None
frame_attr = None
frame_ancestor_attr = None
style = None
popup_body_width = None
popup_body_height = None
message = None
test_element = None


def is_valid_attr_name(name: str) -> bool:
    """Проверяет, является ли имя атрибута допустимым.

    Args:
        name (str): Имя атрибута для проверки.

    Returns:
        bool: True, если имя атрибута допустимо, False в противном случае.
    """
    try:
        # Код пытается установить атрибут с заданным именем на тестовом элементе
        test_element.setAttribute(name, "testValue")
        return True
    except Exception as ex:
        # Логирует ошибку и возвращает False в случае ошибки
        logger.error(f'Недопустимое имя атрибута {name=}', ex)
        return False


def is_valid_attr_names(names: dict) -> bool:
    """Проверяет, являются ли все имена атрибутов в словаре допустимыми.

    Args:
        names (dict): Словарь с именами атрибутов для проверки.

    Returns:
        bool: True, если все имена атрибутов допустимы, False в противном случае.
    """
    for attr_name in names:
        # Код проверяет каждое имя атрибута через is_valid_attr_name
        if not is_valid_attr_name(names[attr_name]):
            return False
    return True


def is_valid_style_length(length: str) -> bool:
    """Проверяет, является ли длина стиля допустимой.

    Args:
        length (str): Длина стиля для проверки.

    Returns:
        bool: True, если длина стиля допустима, False в противном случае.
    """
    # Код проверяет, соответствует ли длина одному из допустимых форматов (auto или числоpx)
    return bool(/^auto$|^[1-9]\d*px$/.test(length))


async def load_default_css() -> str:
    """Загружает CSS по умолчанию из файла.

    Returns:
        str: CSS текст
    """
    try:
        # Код создает запрос к файлу
        req = XMLHttpRequest()
        req.open("GET", browser.runtime.getURL("/css/try_xpath_insert.css"))
        req.responseType = "text"
        # Код ожидает получения файла
        return await new Promise(function(resolve, reject) {
            req.onreadystatechange = function () {
                if (req.readyState === XMLHttpRequest.DONE) {
                    # Код возвращает содержимое файла
                    resolve(req.responseText)
                }
            }
            req.send()
        })
    except Exception as ex:
        # Логирует ошибку и возвращает пустую строку в случае ошибки
        logger.error('Ошибка загрузки default css', ex)
        return ''


def extract_body_styles(css: str) -> dict:
    """Извлекает стили ширины и высоты из CSS.

    Args:
        css (str): CSS текст для извлечения стилей.

    Returns:
        dict: Словарь с шириной и высотой.
    """
    styles = {}
    # Код извлекает значения ширины и высоты из css
    res = /width:(.+?);.*height:(.+?);/.exec(css)
    if res:
        styles["width"] = res[1]
        styles["height"] = res[2]
    else:
        styles["width"] = ""
        styles["height"] = ""
    return styles


def create_popup_css(body_styles: dict) -> str:
    """Создает CSS для всплывающего окна.

    Args:
        body_styles (dict): Словарь со стилями ширины и высоты.

    Returns:
        str: CSS текст.
    """
    # Код формирует css из полученных body_styles
    return f"body{{width:{body_styles['width']};height:{body_styles['height']};}}"


async def initialize_options():
    """Инициализирует страницу опций, устанавливает значения по умолчанию и загружает сохраненные настройки."""
    global element_attr, context_attr, focused_attr, ancestor_attr, frame_attr, frame_ancestor_attr, style, popup_body_width, popup_body_height, message
    # Код получает элементы страницы
    element_attr = document.getElementById("element-attribute")
    context_attr = document.getElementById("context-attribute")
    focused_attr = document.getElementById("focused-attribute")
    ancestor_attr = document.getElementById("ancestor-attribute")
    frame_attr = document.getElementById("frame-attribute")
    frame_ancestor_attr = document.getElementById(
        "frame-ancestor-attribute")
    style = document.getElementById("style")
    popup_body_width = document.getElementById("popup-body-width")
    popup_body_height = document.getElementById("popup-body-height")
    message = document.getElementById("message")
    # Код отправляет сообщение для получения сохраненных настроек
    try:
        res = await browser.runtime.sendMessage({"timeout": 0, "timeout_for_event": "presence_of_element_located",
                                            "event": "loadOptions"})
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
    except Exception as ex:
        # Код логирует ошибку
        logger.error("Ошибка при получении сохраненных настроек", ex)


async def save_options():
    """Сохраняет текущие настройки в хранилище."""
    # Код получает значения из полей ввода
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
    # Код проверяет валидность атрибутов
    if not is_valid_attr_names(attrs):
        message.textContent = "Недопустимый атрибут."
        return
    # Код проверяет валидность стилей
    if not (is_valid_style_length(body_styles["width"]) and is_valid_style_length(body_styles["height"])):
        message.textContent = "Недопустимый стиль."
        return
    try:
        # Код сохраняет настройки
        await browser.storage.sync.set({
            "attributes": attrs,
            "css": style_value,
            "popupCss": create_popup_css(body_styles)
        })
        message.textContent = "Успешно. Пожалуйста, нажмите кнопку \"Set style\" во всплывающем окне, чтобы применить новые параметры."
    except Exception as ex:
        # Код логирует ошибку
        logger.error("Ошибка при сохранении настроек", ex)
        message.textContent = f"Ошибка. {ex}"


async def show_default_options():
    """Устанавливает значения по умолчанию для всех настроек."""
    # Код устанавливает значения атрибутов по умолчанию
    element_attr.value = DEFAULT_ATTRIBUTES["element"]
    context_attr.value = DEFAULT_ATTRIBUTES["context"]
    focused_attr.value = DEFAULT_ATTRIBUTES["focused"]
    ancestor_attr.value = DEFAULT_ATTRIBUTES["focusedAncestor"]
    frame_attr.value = DEFAULT_ATTRIBUTES["frame"]
    frame_ancestor_attr.value = DEFAULT_ATTRIBUTES["frameAncestor"]
    try:
        # Код загружает css по умолчанию
        css = await load_default_css()
        style.value = css
    except Exception as ex:
         # Код логирует ошибку
        logger.error('Ошибка загрузки css по умолчанию', ex)
    # Код устанавливает значения стилей по умолчанию
    popup_body_width.value = DEFAULT_POPUP_BODY_STYLES["width"]
    popup_body_height.value = DEFAULT_POPUP_BODY_STYLES["height"]


window.addEventListener("load", async () => {
    # Код вызывает функцию инициализации
    await initialize_options()
    document.getElementById("save").addEventListener("click", async () => {
        # Код вызывает функцию сохранения
        await save_options()
    });
    document.getElementById("show-default").addEventListener(
        "click", async () => {
            # Код вызывает функцию установки значений по умолчанию
            await show_default_options()
        });
})
# Код создает тестовый элемент для проверок
test_element = document.createElement("div")