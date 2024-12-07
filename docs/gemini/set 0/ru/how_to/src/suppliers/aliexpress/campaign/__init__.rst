Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот файл `hypotez/src/suppliers/aliexpress/campaign/__init__.py` является модулем инициализации для управления рекламными кампаниями AliExpress.  Он импортирует классы и функции, отвечающие за редактирование кампаний, обработку данных, генерацию отчетов и, возможно, интеграцию с Google Sheets (хотя эта часть закомментирована).  Модуль определяет константу `MODE`, которая, по всей видимости, задаёт режим работы (например, `'dev'` для разработки).


Шаги выполнения
-------------------------
1. Импортирует классы `AliCampaignEditor`, `CategoryHTMLGenerator`, `ProductHTMLGenerator`, `process_campaign`, `process_campaign_category`, `process_all_campaigns`.  
2. Определяет константу `MODE` с значением `'dev'`.  Это значение вероятно используется для управления различными режимами работы или настройки.
3.  Закомментированные строки (`#`)  указывает на функции и классы, которые потенциально использовались ранее, но сейчас отключены.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.campaign import AliCampaignEditor, process_campaign

    # Создаём объект редактора кампаний
    editor = AliCampaignEditor()

    # Обрабатываем определённую кампанию
    campaign_data = process_campaign(campaign_id=123)

    # Выводим данные кампании
    print(campaign_data)