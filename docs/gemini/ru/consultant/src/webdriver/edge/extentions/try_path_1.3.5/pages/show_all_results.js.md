## Анализ кода модуля show_all_results.js

**Качество кода**
1.  **Соответствие требованиям по оформлению кода: 8**
    -   Плюсы
        - Код хорошо структурирован и читаем.
        - Присутствует обработка событий и взаимодействие с DOM.
        - Используются функции для разделения логики.
    -   Минусы
        - Отсутствуют docstring для функций и модуля.
        - Не используется `logger` для обработки ошибок.
        - Не все переменные объявлены с использованием `const` или `let`.

**Рекомендации по улучшению**

1.  **Добавить docstring**: Добавить документацию в формате reStructuredText (RST) для модуля и каждой функции, чтобы улучшить понимание кода.
2.  **Использовать `logger`**: Заменить `catch(fu.onError)` на использование `logger.error` для логирования ошибок.
3.  **Использовать `const` и `let`**: Заменить `var` на `const` или `let` там, где это уместно.
4.  **Улучшить читаемость**: Разбить длинные строки на несколько для лучшей читаемости.
5.  **Обработка ошибок**: Улучшить обработку ошибок, добавив более конкретные логи.
6.  **Переименование**: Привести имена переменных в соответствие с остальным кодом.

**Оптимизированный код**

```python
"""
Модуль для отображения результатов XPath на странице.
======================================================

Этот модуль обрабатывает результаты выполнения XPath запросов и отображает их на странице результатов.
Также обеспечивает функциональность экспорта результатов в текстовый файл и возможность
фокусировки на элементах, найденных по XPath запросу, на исходной странице.

Пример использования
--------------------

Этот модуль используется внутри расширения браузера для отображения результатов поиска элементов.
Он получает данные от фонового скрипта и динамически обновляет HTML страницу.
"""
import json # импортируем модуль для работы с json

from src.logger.logger import logger # импортируем логгер для обработки ошибок
# from src.utils.jjson import j_loads, j_loads_ns # todo: не используется

# алиасы
tx = tryxpath # todo: не используется
fu = tryxpath.functions # todo: не используется

def show_all_results(results: dict) -> None:
    """
    Отображает все результаты XPath запроса на странице.

    :param results: Объект, содержащий результаты выполнения XPath запроса.
    :type results: dict
    """
    try:
        document = window.document
        document.getElementById("message").textContent = results["message"] # Записываем сообщение в соответствующий элемент
        document.getElementById("title").textContent = results["title"] # Записываем заголовок
        document.getElementById("url").textContent = results["href"] # Записываем url
        document.getElementById("frame-id").textContent = results["frameId"] # Записываем frame id

        if results["context"]: # Проверка наличия контекста
            cont = results["context"] # сохраняем контекст
            document.getElementById("context-method").textContent = cont["method"] # записываем метод контекста
            document.getElementById("context-expression").textContent = cont["expression"] # записываем выражение контекста
            document.getElementById("context-specified-result-type").textContent = cont["specifiedResultType"] # записываем тип результата
            document.getElementById("context-result-type").textContent = cont["resultType"] # записываем тип результата контекста
            document.getElementById("context-resolver").textContent = cont["resolver"] # записываем резолвер контекста
            cont_tbody = document.getElementById("context-detail").getElementsByTagName("tbody")[0] # получаем таблицу контекста
            if cont["itemDetail"]: # проверяем детали контекста
                fu.updateDetailsTable(cont_tbody, [cont["itemDetail"]], { # обновляем таблицу деталей
                    "headerValues": ["Type", "Name", "Value", "textContent"],
                    "detailKeys": ["type", "name", "value", "textContent"]
                }).catch(lambda ex: logger.error("Ошибка обновления таблицы деталей контекста", exc_info=ex)) # обработка ошибок при обновлении таблицы
        else: # если контекста нет, удаляем область контекста
            area = document.getElementById("context-area") # получаем область контекста
            area.parentNode.removeChild(area) # удаляем область контекста

        main = results["main"] # сохраняем основные результаты
        document.getElementById("main-method").textContent = main["method"] # записываем метод
        document.getElementById("main-expression").textContent = main["expression"] # записываем выражение
        document.getElementById("main-specified-result-type").textContent = main["specifiedResultType"] # записываем тип результата
        document.getElementById("main-result-type").textContent = main["resultType"] # записываем тип результата
        document.getElementById("main-resolver").textContent = main["resolver"] # записываем резолвер
        document.getElementById("main-count").textContent = len(main["itemDetails"]) # записываем количество элементов
        main_tbody = document.getElementById("main-details").getElementsByTagName("tbody")[0] # получаем таблицу основных результатов
        fu.updateDetailsTable(main_tbody, main["itemDetails"], { # обновляем таблицу основных результатов
            "headerValues": ["Type", "Name", "Value", "textContent"],
            "detailKeys": ["type", "name", "value", "textContent"]
        }).catch(lambda ex: logger.error("Ошибка обновления таблицы основных результатов", exc_info=ex)) # обрабатываем ошибки при обновлении
    except Exception as ex: # обрабатываем общие ошибки
        logger.error("Ошибка при отображении результатов", exc_info=ex)

def make_text_download_url(text: str) -> str:
    """
    Создает URL для скачивания текста.

    :param text: Текст для скачивания.
    :type text: str
    :return: URL для скачивания.
    :rtype: str
    """
    try:
        return URL.createObjectURL(new Blob([text], { "type": "text/plain"})) # возвращаем url для скачивания
    except Exception as ex: # обрабатываем общие ошибки
        logger.error("Ошибка при создании URL для скачивания", exc_info=ex)

def make_info_text(results: dict) -> str:
    """
    Создает текстовое представление результатов XPath запроса.

    :param results: Объект, содержащий результаты выполнения XPath запроса.
    :type results: dict
    :return: Текстовое представление результатов.
    :rtype: str
    """
    try:
        cont = results["context"] # сохраняем контекст
        main = results["main"] # сохраняем основные результаты
        text = f"[Information]\n" # начало текстового представления
        text += f"Message:     {results['message']}\n" # добавляем сообщение
        text += f"Title:       {results['title']}\n" # добавляем заголовок
        text += f"URL:         {results['href']}\n" # добавляем url
        text += f"frameId:     {results['frameId']}\n\n" # добавляем frame id

        if cont: # проверяем наличие контекста
             text += "[Context information]\n" # начало информации о контексте
             text += f"Method:                  {cont['method']}\n" # добавляем метод контекста
             text += f"Expression:              {cont['expression']}\n" # добавляем выражение контекста
             text += f"Specified resultType:    {cont['specifiedResultType']}\n" # добавляем тип результата
             text += f"resultType:              {cont['resultType']}\n" # добавляем тип результата
             text += f"Resolver:                {cont['resolver']}\n\n" # добавляем резолвер

             text += "[Context detail]\n" # начало информации о деталях контекста
             text += f"{', '.join(['Type', 'Name', 'Value', 'textContent'])}\n" # добавляем заголовки таблицы
             text += f"{fu.makeDetailText(cont['itemDetail'], ['type', 'name', 'value', 'textContent'], ', ')}\n" # добавляем детали контекста
        text += "[Main information]\n" # начало информации об основных результатах
        text += f"Method:                  {main['method']}\n" # добавляем метод
        text += f"Expression:              {main['expression']}\n" # добавляем выражение
        text += f"Specified resultType:    {main['specifiedResultType']}\n" # добавляем тип результата
        text += f"resultType:              {main['resultType']}\n" # добавляем тип результата
        text += f"Resolver:                {main['resolver']}\n" # добавляем резолвер
        text += f"Count:                   {len(main['itemDetails'])}\n\n" # добавляем количество элементов

        text += "[Main details]\n" # начало информации о деталях основных результатов
        text += f"{', '.join(['Index', 'Type', 'Name', 'Value', 'textContent'])}\n" # добавляем заголовки таблицы
        text += '\n'.join( # добавляем детали
            fu.makeDetailText(detail, ["index", "type", "name", "value", "textContent"], ", ", {
                "index": lambda val: ind # создаем лямбда для получения индекса
            }) for ind, detail in enumerate(main["itemDetails"]) # итерируемся по деталям и их индексам
        )
        return text # возвращаем текст
    except Exception as ex: # обрабатываем общие ошибки
        logger.error("Ошибка при создании текстового представления результатов", exc_info=ex)

def make_converted_info_text(results: dict) -> str:
    """
    Создает текстовое представление результатов XPath запроса с JSON преобразованием.

    :param results: Объект, содержащий результаты выполнения XPath запроса.
    :type results: dict
    :return: Текстовое представление результатов с JSON преобразованием.
    :rtype: str
    """
    try:
        cont = results["context"] # сохраняем контекст
        main = results["main"] # сохраняем основные результаты
        text = f"[Information]\n" # начало текстового представления
        text += f"Message:     {results['message']}\n" # добавляем сообщение
        text += f"Title:       {results['title']}\n" # добавляем заголовок
        text += f"URL:         {results['href']}\n" # добавляем url
        text += f"frameId:     {results['frameId']}\n\n" # добавляем frame id

        if cont: # проверяем наличие контекста
            text += "[Context information]\n" # начало информации о контексте
            text += f"Method:                  {cont['method']}\n" # добавляем метод контекста
            text += f"Expression(JSON):        {json.dumps(cont['expression'])}\n" # добавляем выражение контекста
            text += f"Specified resultType:    {cont['specifiedResultType']}\n" # добавляем тип результата
            text += f"resultType:              {cont['resultType']}\n" # добавляем тип результата
            text += f"Resolver:                {cont['resolver']}\n\n" # добавляем резолвер

            text += "[Context detail]\n" # начало информации о деталях контекста
            text += "Type, Name, Value(JSON), textContent(JSON)\n" # добавляем заголовки таблицы
            text += f"{fu.makeDetailText(cont['itemDetail'], ['type', 'name', 'value', 'textContent'], ', ', {\n" # добавляем детали контекста
            text += "    'value': json.dumps,\n" # преобразовываем value в json
            text += "    'textContent': json.dumps\n" # преобразовываем textContent в json
            text += "})}\n"
        text += "[Main information]\n" # начало информации об основных результатах
        text += f"Method:                  {main['method']}\n" # добавляем метод
        text += f"Expression(JSON):        {json.dumps(main['expression'])}\n" # добавляем выражение
        text += f"Specified resultType:    {main['specifiedResultType']}\n" # добавляем тип результата
        text += f"resultType:              {main['resultType']}\n" # добавляем тип результата
        text += f"Resolver:                {main['resolver']}\n" # добавляем резолвер
        text += f"Count:                   {len(main['itemDetails'])}\n\n" # добавляем количество элементов
        text += "[Main details]\n" # начало информации о деталях основных результатов
        text += "Index, Type, Name, Value(JSON), textContent(JSON)\n" # добавляем заголовки таблицы
        text += '\n'.join( # добавляем детали
            fu.makeDetailText(detail, ["index", "type", "name", "value", "textContent"], ", ", {
                "index": lambda val: ind, # создаем лямбда для получения индекса
                "value": json.dumps, # преобразовываем value в json
                "textContent": json.dumps # преобразовываем textContent в json
            }) for ind, detail in enumerate(main["itemDetails"]) # итерируемся по деталям и их индексам
        )
        return text # возвращаем текст
    except Exception as ex: # обрабатываем общие ошибки
        logger.error("Ошибка при создании текстового представления результатов с JSON", exc_info=ex)
# Глобальные переменные
related_tab_id = None # id связанной вкладки
related_frame_id = None # id связанного фрейма
execution_id = None # id выполнения

window.addEventListener("load", lambda:  # Добавляем слушатель события загрузки страницы
    browser.runtime.sendMessage({"event":"loadResults"}).then(results => { # отправляем сообщение фоновому скрипту
        if results: # проверяем наличие результатов
            related_tab_id = results["tabId"] # сохраняем id вкладки
            related_frame_id = results["frameId"] # сохраняем id фрейма
            execution_id = results["executionId"] # сохраняем id выполнения

            expo_text = document.getElementById("export-text") # получаем элемент для экспорта текста
            expo_text.setAttribute( # устанавливаем атрибуты для экспорта
                "download", f"tryxpath-{results['title']}.txt") # устанавливаем имя файла
            expo_text.href =  make_text_download_url(make_info_text(results)) # устанавливаем url для скачивания

            expo_part_conv = document.getElementById("export-partly-converted") # получаем элемент для экспорта частично конвертированного текста
            expo_part_conv.setAttribute( # устанавливаем атрибуты для экспорта
                "download", f"tryxpath-converted-{results['title']}.txt") # устанавливаем имя файла
            expo_part_conv.href =  make_text_download_url(
                make_converted_info_text(results)) # устанавливаем url для скачивания

            show_all_results(results) # отображаем результаты
    }).catch(lambda ex: logger.error("Ошибка при получении результатов из фонового скрипта", exc_info=ex)) # обрабатываем ошибки при получении результатов

    cont_detail = document.getElementById("context-detail") # получаем элемент детали контекста
    cont_detail.addEventListener("click", lambda event:  # Добавляем слушатель события клика
        (lambda target:  # Создаем лямбда функцию
            target.tagName.lower() == "button" and # проверяем, что кликнули на кнопку
            browser.tabs.sendMessage(related_tab_id, { # отправляем сообщение фоновой странице
                "timeout": 0,"timeout_for_event":"presence_of_element_located","event": "focusContextItem",
                "executionId": execution_id
            }, {
                "frameId": related_frame_id
            })
        )(event.target)
    ) # вызываем лямбда-функцию и обрабатываем событие

    main_details = document.getElementById("main-details") # получаем элемент основных деталей
    main_details.addEventListener("click", lambda event: # Добавляем слушатель события клика
         (lambda target: # Создаем лямбда функцию
             target.tagName.lower() == "button" and  # проверяем, что кликнули на кнопку
            (lambda ind: browser.tabs.sendMessage(related_tab_id, { # отправляем сообщение фоновой странице
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "focusItem",
                "executionId": execution_id,
                "index": ind
            }, {
                "frameId": related_frame_id
            }))(int(target.getAttribute("data-index"), 10)) # получаем индекс из атрибута
        )(event.target)
    ) # вызываем лямбда-функцию и обрабатываем событие
)