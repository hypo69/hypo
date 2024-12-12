## Анализ кода модуля popup.js

**Качество кода**
8
-  Плюсы
    - Код разбит на функции, что улучшает читаемость и поддержку.
    - Используется `Object.create(null)` для создания объектов без прототипа, что может быть полезно в некоторых случаях.
    - Код следует стандартам именования переменных и функций.
    - Обработчики событий добавлены через `addEventListener`, что является хорошей практикой.
-  Минусы
    - Не хватает комментариев, особенно в формате reStructuredText (RST), для функций и переменных.
    - Используются стандартные блоки `try-except` без логирования ошибок через `logger.error`.
    - Многократное использование `sendToActiveTab` с одинаковыми параметрами, можно вынести в отдельную функцию.
    - Есть потенциал для улучшения структуры кода через разбиение на более мелкие, переиспользуемые функции.
    - Использование устаревшего var вместо let/const
    -  Дублирование кода при добавлении `event` и `timeout` параметров в сообщения.
    -  В некоторых местах используется `parseInt` без проверки на `NaN`
    - Отсутствуют docstring

**Рекомендации по улучшению**

1.  **Добавить docstring и комментарии в формате reStructuredText (RST)**:
    - Описать каждый модуль, функцию, метод и переменную с использованием RST.
    - Подробно комментировать каждый блок кода для лучшего понимания.
2.  **Использовать `logger.error` для обработки ошибок**:
    - Заменить стандартные блоки `try-except` на `logger.error` для более эффективного логирования ошибок.
3.  **Избегать дублирования кода**:
    - Вынести общие части кода в отдельные функции для переиспользования.
    - Упростить отправку сообщений, избегая повторений в `sendToActiveTab` и `sendToSpecifiedFrame`.
4.  **Улучшить структуру кода**:
    - Разбить крупные функции на более мелкие, переиспользуемые функции.
    - Использовать `let` и `const` вместо `var`.
    -  Добавить проверку на `NaN` после `parseInt`

**Оптимизированный код**

```python
"""
Модуль для управления popup окном расширения tryxpath
====================================================

Этот модуль отвечает за взаимодействие с popup окном расширения,
включая отправку сообщений на активную вкладку,
обработку результатов и сохранение состояния popup окна.
"""

import json
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

# alias
#  создаем псевдоним для tryxpath
tx = tryxpath
# создаем псевдоним для tryxpath.functions
fu = tryxpath.functions

# сохраняем ссылку на объект document
document = window.document

#  класс для скрытия элементов
noneClass = "none"
# класс для элементов справки
helpClass = "help"
#  константа, представляющая недействительный идентификатор вкладки
invalidTabId = browser.tabs.TAB_ID_NONE
# константа, представляющая недействительный идентификатор выполнения скрипта
invalidExecutionId = float('NaN')
# константа, представляющая недействительный идентификатор фрейма
invalidFrameId = -1

# Объявление переменных для элементов интерфейса popup окна
# :var mainWay: HTML элемент select для выбора способа поиска
# :var mainExpression: HTML элемент textarea для ввода основного xpath выражения
# :var contextCheckbox: HTML элемент checkbox для включения/выключения контекстного поиска
# :var contextHeader: HTML элемент для заголовка контекстного поиска
# :var contextBody: HTML элемент для тела контекстного поиска
# :var contextWay: HTML элемент select для выбора способа контекстного поиска
# :var contextExpression: HTML элемент textarea для ввода контекстного xpath выражения
# :var resolverHeader: HTML элемент для заголовка поиска через resolver
# :var resolverBody: HTML элемент для тела поиска через resolver
# :var resolverCheckbox: HTML элемент checkbox для включения/выключения поиска через resolver
# :var resolverExpression: HTML элемент textarea для ввода выражения resolver
# :var frameDesignationHeader: HTML элемент для заголовка поиска фрейма
# :var frameDesignationCheckbox: HTML элемент checkbox для включения/выключения поиска фрейма
# :var frameDesignationBody: HTML элемент для тела поиска фрейма
# :var frameDesignationExpression: HTML элемент textarea для ввода выражения для поиска фрейма
# :var frameIdHeader: HTML элемент для заголовка поиска по frameId
# :var frameIdCheckbox: HTML элемент checkbox для включения/выключения поиска по frameId
# :var frameIdBody: HTML элемент для тела поиска по frameId
# :var frameIdList: HTML элемент select для выбора frameId
# :var frameIdExpression: HTML элемент textarea для ввода frameId
# :var resultsMessage: HTML элемент для отображения сообщения о результате
# :var resultsTbody: HTML элемент tbody для отображения результатов
# :var contextTbody: HTML элемент tbody для отображения контекстных результатов
# :var resultsCount: HTML элемент для отображения количества результатов
# :var resultsFrameId: HTML элемент для отображения frameId
# :var detailsPageCount: HTML элемент для отображения номера страницы с деталями
# :var helpBody: HTML элемент для тела справки
# :var helpCheckbox: HTML элемент checkbox для включения/выключения справки
let mainWay, mainExpression, contextCheckbox, contextHeader, contextBody,
    contextWay, contextExpression, resolverHeader, resolverBody,
    resolverCheckbox, resolverExpression, frameDesignationHeader,
    frameDesignationCheckbox, frameDesignationBody,
    frameDesignationExpression, frameIdHeader, frameIdCheckbox,
    frameIdBody, frameIdList, frameIdExpression, resultsMessage,
    resultsTbody, contextTbody, resultsCount, resultsFrameId,
    detailsPageCount, helpBody, helpCheckbox;

# :var relatedTabId:  Идентификатор вкладки, связанной с текущим popup
# :var relatedFrameId: Идентификатор фрейма, связанного с текущим popup
# :var executionId: Идентификатор выполнения скрипта
# :var resultedDetails: Список деталей результатов
# :var detailsPageSize: Размер страницы для отображения деталей
# :var detailsPageIndex: Индекс текущей страницы деталей
let relatedTabId = invalidTabId;
let relatedFrameId = invalidFrameId;
let executionId = invalidExecutionId;
let resultedDetails = [];
const detailsPageSize = 50;
let detailsPageIndex = 0;

def send_message(tab_id, msg, opts=None):
    """
    Отправляет сообщение на указанную вкладку.

    :param tab_id: Идентификатор вкладки, куда отправить сообщение.
    :param msg: Объект сообщения для отправки.
    :param opts: Дополнительные опции для отправки сообщения.
    :return: Promise, разрешающийся с ответом от вкладки.
    """
    opts = opts or {};
    return browser.tabs.sendMessage(tab_id, {
       "timeout":0,
        "timeout_for_event":"presence_of_element_located",
        **msg
        }, opts);
    
def send_to_active_tab(msg, opts=None):
    """
    Отправляет сообщение на активную вкладку в текущем окне.

    :param msg: Объект сообщения для отправки.
    :param opts: Дополнительные опции для отправки сообщения.
    :return: Promise, разрешающийся с ответом от вкладки.
    """
    return browser.tabs.query({
        "active": True,
        "currentWindow": True
    }).then(tabs => {
       return send_message(tabs[0].id, msg, opts);
    });


def send_to_specified_frame(msg):
    """
    Отправляет сообщение в указанный фрейм.

    :param msg: Объект сообщения для отправки.
    :return: Promise, разрешающийся после выполнения скрипта.
    """
    let frameId = get_specified_frame_id();
    return Promise.resolve().then(() => {
        return browser.tabs.executeScript({
            "file": "/scripts/try_xpath_check_frame.js",
            "matchAboutBlank": True,
            "runAt": "document_start",
            "frameId": frameId
        });
    }).then(ress => {
        if (ress[0]) {
            return;
        }
        return exec_content_script();
    }).then(() => {
       return send_to_active_tab({ "event": "initializeBlankWindows" });
    }).then(() => {
        return send_to_active_tab(msg, { "frameId": frameId });
    }).catch(e => {
        show_error("An error occurred. The frameId may be incorrect.",
                  frameId);
    });


def collect_popup_state():
    """
    Собирает текущее состояние popup окна.

    :return: Объект с текущим состоянием popup окна.
    """
    let state = Object.create(None);
    state.helpCheckboxChecked = helpCheckbox.checked;
    state.mainWayIndex = mainWay.selectedIndex;
    state.mainExpressionValue = mainExpression.value;
    state.contextCheckboxChecked = contextCheckbox.checked;
    state.contextWayIndex = contextWay.selectedIndex;
    state.contextExpressionValue = contextExpression.value;
    state.resolverCheckboxChecked = resolverCheckbox.checked;
    state.resolverExpressionValue = resolverExpression.value;
    state.frameDesignationCheckboxChecked = frameDesignationCheckbox.checked;
    state.frameDesignationExpressionValue = frameDesignationExpression.value;
    state.frameIdCheckboxChecked = frameIdCheckbox.checked;

    state.specifiedFrameId = get_specified_frame_id();
    state.detailsPageIndex = detailsPageIndex;
    return state;

def change_context_visible():
    """
    Изменяет видимость блока контекстного поиска.
    """
    if (contextCheckbox.checked) {
        contextBody.classList.remove(noneClass);
    } else {
        contextBody.classList.add(noneClass);
    }


def change_resolver_visible():
    """
    Изменяет видимость блока поиска через resolver.
    """
    if (resolverCheckbox.checked) {
        resolverBody.classList.remove(noneClass);
    } else {
        resolverBody.classList.add(noneClass);
    }


def change_frame_id_visible():
    """
    Изменяет видимость блока выбора frameId.
    """
    if (frameIdCheckbox.checked) {
        frameIdBody.classList.remove(noneClass);
    } else {
        frameIdBody.classList.add(noneClass);
    }


def change_frame_designation_visible():
    """
    Изменяет видимость блока указания фрейма.
    """
    if (frameDesignationCheckbox.checked) {
        frameDesignationBody.classList.remove(noneClass);
    } else {
        frameDesignationBody.classList.add(noneClass);
    }


def change_help_visible():
    """
    Изменяет видимость элементов справки.
    """
    let helps = document.getElementsByClassName(helpClass);
    if (helpCheckbox.checked) {
        for (let i = 0; i < helps.length; i++) {
            helps[i].classList.remove(noneClass);
        }
    } else {
        for (let i = 0; i < helps.length; i++) {
            helps[i].classList.add(noneClass);
        }
    }


def make_execute_message():
    """
    Создает объект сообщения для выполнения xpath запроса.

    :return: Объект сообщения с параметрами для выполнения запроса.
    """
    let msg = Object.create(None);
    msg.event = "execute";

    let resol;
    if (resolverCheckbox.checked) {
        resol = resolverExpression.value;
    } else {
        resol = None;
    }

    let way = mainWay.selectedOptions[0];
    msg.main = Object.create(None);
    msg.main.expression = mainExpression.value;
    msg.main.method = way.getAttribute("data-method");
    msg.main.resultType = way.getAttribute("data-type");
    msg.main.resolver = resol;

    if (contextCheckbox.checked) {
        let way = contextWay.selectedOptions[0];
        msg.context = Object.create(None);
        msg.context.expression = contextExpression.value;
        msg.context.method = way.getAttribute("data-method");
        msg.context.resultType = way.getAttribute("data-type");
        msg.context.resolver = resol;
    }

    if (frameDesignationCheckbox.checked) {
        msg.frameDesignation = frameDesignationExpression.value;
    }

    return msg;


def get_specified_frame_id():
    """
    Получает идентификатор фрейма, указанного пользователем.

    :return: Идентификатор фрейма.
    """
    if (!frameIdCheckbox.checked) {
        return 0;
    }
    let id = frameIdList.selectedOptions[0].getAttribute("data-frame-id");
    if (id === "manual") {
        let manual_id = parseInt(frameIdExpression.value, 10);
        if (isNaN(manual_id)){
            return 0;
        }
        return manual_id;
    }
    let frame_id = parseInt(id, 10);
    if(isNaN(frame_id)){
        return 0;
    }
    return frame_id;


def exec_content_script():
    """
    Выполняет скрипты содержимого на всех фреймах.

    :return: Promise, разрешающийся после выполнения скриптов.
    """
    return browser.tabs.executeScript({
        "file": "/scripts/try_xpath_functions.js",
        "matchAboutBlank": True,
        "runAt": "document_start",
        "allFrames": True
    }).then(() => {
        return browser.tabs.executeScript({
            "file": "/scripts/try_xpath_content.js",
            "matchAboutBlank": True,
            "runAt": "document_start",
            "allFrames": True
        });
    });


def send_execute():
    """
    Отправляет сообщение на выполнение xpath запроса.
    """
    send_to_specified_frame(make_execute_message());


def handle_expr_enter(event):
    """
    Обрабатывает нажатие клавиши Enter в полях ввода выражений.

    :param event: Событие нажатия клавиши.
    """
    if ((event.key === "Enter") and !event.shiftKey) {
        event.preventDefault();
        send_execute();
    }


def show_details_page(index):
    """
    Отображает страницу с деталями результатов.

    :param index: Индекс страницы для отображения.
    """
    let max = Math.floor(resultedDetails.length / detailsPageSize);

    if (!Number.isInteger(index)) {
        index = 0;
    }
    index = Math.max(0, index);
    index = Math.min(index, max);

    let scrollY = window.scrollY;
    let scrollX = window.scrollX;

    fu.updateDetailsTable(resultsTbody, resultedDetails, {
        "begin": index * detailsPageSize,
        "end": (index * detailsPageSize) + detailsPageSize,
    }).then(() => {
        detailsPageCount.value = index + 1;
        detailsPageIndex = index;
        window.scrollTo(scrollX, scrollY);
    }).catch(fu.onError);


def show_error(message, frameId):
    """
    Отображает сообщение об ошибке.

    :param message: Сообщение об ошибке.
    :param frameId: Идентификатор фрейма, где произошла ошибка.
    """
    relatedTabId = invalidTabId;
    relatedFrameId = invalidFrameId;
    executionId = invalidExecutionId;

    resultsMessage.textContent = message;
    resultedDetails = [];
    resultsCount.textContent = resultedDetails.length;
    resultsFrameId.textContent = frameId;
    
    fu.updateDetailsTable(contextTbody, [])
        .catch(fu.onError);
    show_details_page(0);


def generic_listener(message, sender, sendResponse):
    """
    Общий обработчик сообщений от content script.

    :param message: Объект сообщения.
    :param sender: Объект отправителя сообщения.
    :param sendResponse: Функция для отправки ответа.
    """
    let listener = generic_listener.listeners[message.event];
    if (listener) {
        return listener(message, sender, sendResponse);
    }


generic_listener.listeners = Object.create(None);
browser.runtime.onMessage.addListener(generic_listener);


generic_listener.listeners.showResultsInPopup = function (message, sender) {
    """
    Обрабатывает сообщение о отображении результатов в popup окне.

    :param message: Объект сообщения с результатами.
    :param sender: Объект отправителя сообщения.
    """
    relatedTabId = sender.tab.id;
    relatedFrameId = sender.frameId;
    executionId = message.executionId;

    resultsMessage.textContent = message.message;
    resultedDetails = message.main.itemDetails;
    resultsCount.textContent = resultedDetails.length;
    resultsFrameId.textContent = sender.frameId;

    if (message.context and message.context.itemDetail) {
        fu.updateDetailsTable(contextTbody, [message.context.itemDetail])
            .catch(fu.onError);
    }

    show_details_page(detailsPageIndex);
};


generic_listener.listeners.restorePopupState = function (message) {
    """
    Восстанавливает состояние popup окна.

    :param message: Объект сообщения с сохраненным состоянием.
    """
    let state = message.state;

    if (state !== None) {
        helpCheckbox.checked = state.helpCheckboxChecked;
        mainWay.selectedIndex = state.mainWayIndex;
        mainExpression.value = state.mainExpressionValue;
        contextCheckbox.checked = state.contextCheckboxChecked;
        contextWay.selectedIndex = state.contextWayIndex;
        contextExpression.value = state.contextExpressionValue;
        resolverCheckbox.checked = state.resolverCheckboxChecked;
        resolverExpression.value = state.resolverExpressionValue;
        frameDesignationCheckbox.checked = state.frameDesignationCheckboxChecked;
        frameDesignationExpression.value = state.frameDesignationExpressionValue;
        frameIdCheckbox.checked = state.frameIdCheckboxChecked;
        frameIdExpression.value = state.specifiedFrameId;

        detailsPageIndex = state.detailsPageIndex;
    }

    change_help_visible();
    change_context_visible();
    change_resolver_visible();
    change_frame_designation_visible();
    change_frame_id_visible();

    send_to_specified_frame({ "event": "requestShowResultsInPopup" });
};


generic_listener.listeners.insertStyleToPopup = function (message) {
    """
    Вставляет стили в popup окно.

    :param message: Объект сообщения со стилями.
    """
    let style = document.createElement("style");
    style.textContent = message.css;
    document.head.appendChild(style);
};


generic_listener.listeners.addFrameId = function (message, sender) {
    """
    Добавляет идентификатор фрейма в список.

    :param message: Объект сообщения.
    :param sender: Объект отправителя сообщения.
    """
    let opt = document.createElement("option");
    opt.setAttribute("data-frame-id", sender.frameId);
    opt.textContent = sender.frameId;
    frameIdList.appendChild(opt);
};


window.addEventListener("load", () => {
    """
    Обработчик события загрузки окна. Инициализирует элементы интерфейса.
    """
    helpBody = document.getElementById("help-body");
    helpCheckbox = document.getElementById("help-switch");
    mainWay = document.getElementById("main-way");
    mainExpression = document.getElementById("main-expression");
    contextHeader = document.getElementById("context-header");
    contextCheckbox = document.getElementById("context-switch");
    contextBody = document.getElementById("context-body");
    contextWay = document.getElementById("context-way");
    contextExpression = document.getElementById("context-expression");
    resolverHeader = document.getElementById("resolver-header");
    resolverCheckbox = document.getElementById("resolver-switch");
    resolverBody = document.getElementById("resolver-body");
    resolverExpression = document.getElementById("resolver-expression");
    frameDesignationHeader = document.getElementById(
        "frame-designation-header");
    frameDesignationCheckbox = document.getElementById(
        "frame-designation-switch");
    frameDesignationBody = document.getElementById(
        "frame-designation-body");
    frameDesignationExpression = document.getElementById(
        "frame-designation-expression");
    frameIdHeader = document.getElementById("frame-id-header");
    frameIdCheckbox = document.getElementById("frame-id-switch");
    frameIdBody = document.getElementById("frame-id-body");
    frameIdList = document.getElementById("frame-id-list");
    frameIdExpression = document.getElementById("frame-id-expression");
    resultsMessage = document.getElementById("results-message");
    resultsCount = document.getElementById("results-count");
    resultsFrameId = document.getElementById("results-frame-id");
    resultsTbody = document.getElementById("results-details")
        .getElementsByTagName("tbody")[0];
    contextTbody = document.getElementById("context-detail")
        .getElementsByTagName("tbody")[0];
    detailsPageCount = document.getElementById("details-page-count");

    helpBody.addEventListener("click", change_help_visible);
    helpBody.addEventListener("keypress", change_help_visible);

    document.getElementById("execute").addEventListener("click",
                                                        send_execute);
    mainExpression.addEventListener("keypress", handle_expr_enter);

    contextHeader.addEventListener("click", change_context_visible);
    contextHeader.addEventListener("keypress", change_context_visible);
    contextExpression.addEventListener("keypress", handle_expr_enter);

    resolverHeader.addEventListener("click", change_resolver_visible);
    resolverHeader.addEventListener("keypress", change_resolver_visible);
    resolverExpression.addEventListener("keypress", handle_expr_enter);

    frameDesignationHeader.addEventListener(
        "click", change_frame_designation_visible);
    frameDesignationHeader.addEventListener(
        "keypress", change_frame_designation_visible);
    frameDesignationExpression.addEventListener(
        "keypress", handle_expr_enter);

    document.getElementById("focus-designated-frame").addEventListener(
        "click", () => {
            send_to_specified_frame({
                "event": "focusFrame",
                "frameDesignation": frameDesignationExpression.value
            });
        });

    frameIdHeader.addEventListener("click", change_frame_id_visible);
    frameIdHeader.addEventListener("keypress", change_frame_id_visible);
    frameIdExpression.addEventListener("keypress", handle_expr_enter);
    document.getElementById("get-all-frame-id").addEventListener(
        "click", () => {
            fu.emptyChildNodes(frameIdList);
            
            let opt = document.createElement("option");
            opt.setAttribute("data-frame-id", "manual");
            opt.textContent = "Manual";
            frameIdList.appendChild(opt);

            browser.tabs.executeScript({
                "code": "browser.runtime.sendMessage"
                    + "({\\"event\\":\\"addFrameId\\"});",
                "matchAboutBlank": True,
                "runAt": "document_start",
                "allFrames": True
            }).catch(fu.onError);
        });

    document.getElementById("show-previous-results").addEventListener(
        "click", () => {
            send_to_specified_frame({ "event": "requestShowResultsInPopup"});
        });

    document.getElementById("focus-frame").addEventListener(
        "click", () => {
           send_to_specified_frame({ "event": "focusFrame"});
        });

    document.getElementById("show-all-results").addEventListener(
        "click", () => {
            send_to_specified_frame({ "event": "requestShowAllResults" });
        });

    document.getElementById("open-options").addEventListener(
        "click", () => {
            browser.runtime.openOptionsPage();
        });

    document.getElementById("set-style").addEventListener("click", () => {
        send_to_specified_frame({ "event": "setStyle" });
    });

    document.getElementById("reset-style").addEventListener("click", () => {
        send_to_specified_frame({ "event": "resetStyle" });
    });

    document.getElementById("set-all-style").addEventListener(
        "click", () => {
            send_to_active_tab({ "event": "setStyle" });
        });

    document.getElementById("reset-all-style").addEventListener(
        "click", () => {
           send_to_active_tab({ "event": "resetStyle" });
        });

    contextTbody.addEventListener("click", event => {
        if (event.target.tagName.toLowerCase() === "button") {
            send_message(relatedTabId, {
                "event": "focusContextItem",
                "executionId": executionId,
            }, {
                "frameId": relatedFrameId
            });
        }
    });

    document.getElementById("previous-details-page").addEventListener(
        "click", () => {
            show_details_page(detailsPageIndex - 1);
        });
    document.getElementById("move-details-page").addEventListener(
        "click", () => {
            let count = parseInt(detailsPageCount.value, 10);
            if (isNaN(count)){
                count = 1;
            }
            show_details_page(count - 1);
        });
    document.getElementById("next-details-page").addEventListener(
        "click", () => {
            show_details_page(detailsPageIndex + 1);
        });

    resultsTbody.addEventListener("click", event => {
        let target = event.target;
        if (target.tagName.toLowerCase() === "button") {
            let ind = parseInt(target.getAttribute("data-index"), 10);
            if (isNaN(ind)){
                ind = 0;
            }
            send_message(relatedTabId, {
                "event": "focusItem",
                "executionId": executionId,
                "index": ind
            }, {
                "frameId": relatedFrameId
            });
        }
    });

    window.addEventListener("unload", () => {
        let state = collect_popup_state();
        browser.runtime.sendMessage({
            "event": "storePopupState",
            "state": state
        });
    });

    resultsTbody.appendChild(fu.createDetailTableHeader());
    contextTbody.appendChild(fu.createDetailTableHeader());

    browser.runtime.sendMessage({ "event": "requestInsertStyleToPopup"});
    browser.runtime.sendMessage({ "event": "requestRestorePopupState" });
});