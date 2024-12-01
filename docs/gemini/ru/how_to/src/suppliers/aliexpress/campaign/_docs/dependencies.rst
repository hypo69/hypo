Как использовать зависимости модуля AliExpress кампаний
==============================================================================================

Описание
-------------------------
Данный документ описывает зависимости модуля AliExpress кампаний. Он предоставляет информацию о внешних модулях и файлах, необходимых для корректной работы модуля.  Это помогает разработчикам понять, какие библиотеки и ресурсы им нужны для интеграции или расширения функциональности.

Шаги выполнения
-------------------------
1. **Установка зависимостей**:
    Модуль `gsheet.py` использует библиотеки `gspread`, `pandas` и файл `src.settings.gs`.  Необходимо установить их, используя менеджер пакетов (например, `pip`):
    ```bash
    pip install gspread pandas
    ```
    Убедитесь, что файл `src.settings.gs` доступен в указанном пути.
2. **Импорты**:
    Для использования зависимостей, таких как `AliCampaignGoogleSheet` из `src.suppliers.aliexpress`, необходимо импортировать необходимые модули в ваш код:
    ```python
    from src.suppliers.aliexpress import AliCampaignGoogleSheet
    ```
3. **Использование**:
    После установки и импорта зависимостей, можно использовать функциональность, предоставляемую `AliCampaignGoogleSheet` в `ali_promo_campaign.py` или в других модулях.
    Пример, как использовать этот класс:
    ```python
    # Внутри ali_promo_campaign.py
    from src.suppliers.aliexpress import AliCampaignGoogleSheet

    # ... (другие импорты и инициализации) ...

    campaign_data = AliCampaignGoogleSheet().get_campaign_data()
    # Далее работа с данными из campaign_data
    ```
4. **Конфигурация:**
    Убедитесь, что `src.settings.gs` содержит корректные настройки для доступа к Google Sheets.  Некорректные настройки могут привести к ошибкам в работе модуля.

Пример использования
-------------------------
.. code-block:: python

    # Пример, показывающий импорт и использование AliCampaignGoogleSheet
    from src.suppliers.aliexpress import AliCampaignGoogleSheet

    # Предположим, что у вас есть объект gs_client, полученный из модуля gspread
    gs_client = # ... ваш код для создания объекта gspread
    gs_sheet = AliCampaignGoogleSheet(gs_client)  # Инициализация с объектом gs_client

    campaign_data = gs_sheet.get_campaign_data()

    if campaign_data:
        print("Данные кампании получены успешно:", campaign_data)
    else:
        print("Ошибка при получении данных кампании.")