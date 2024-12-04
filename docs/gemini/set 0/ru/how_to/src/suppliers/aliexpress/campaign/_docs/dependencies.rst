Как использовать зависимости модуля AliExpress Campaign
============================================================================================

Описание
-------------------------
Этот документ описывает зависимости модуля AliExpress Campaign, используемые для управления рекламными кампаниями. Он объясняет, как модуль использует внешние библиотеки и другие модули, а также предоставляет примеры.

Шаги выполнения
-------------------------
1. **Модуль `ali_promo_campaign.py`:** Этот модуль управляет рекламными кампаниями AliExpress.  Он зависит от модуля `AliCampaignGoogleSheet` из `src.suppliers.aliexpress`. Это означает, что для корректной работы `ali_promo_campaign.py` требуется доступ к функциям и данным, предоставляемым `AliCampaignGoogleSheet`.

2. **Модуль `gsheet.py`:**  Этот модуль отвечает за взаимодействие с Google Sheets.  Он зависит от библиотек `gspread`, `pandas` и `src.settings.gs`.  `gspread` используется для работы с Google Sheets API, `pandas` для обработки данных, а `src.settings.gs` содержит настройки для доступа к Google Sheets.

3. **Связь между модулями:** `ali_promo_campaign.py` использует функциональность `gsheet.py` для получения и работы с данными о рекламных кампаниях из Google Sheets.


Пример использования
-------------------------
.. code-block:: python

    # Пример использования из ali_promo_campaign.py
    from src.suppliers.aliexpress import AliCampaignGoogleSheet

    # ... (другие импорты) ...

    # Инициализация AliCampaignGoogleSheet
    google_sheets_handler = AliCampaignGoogleSheet(spreadsheet_id='YOUR_SPREADSHEET_ID', sheet_name='CAMPAIGNS')

    # Получение данных о кампаниях
    campaigns_data = google_sheets_handler.get_campaign_data()

    # Обработка полученных данных (например, создание, редактирование или удаление кампаний)
    # ...

    # Пример работы с pandas (если используется)
    import pandas as pd
    campaigns_df = pd.DataFrame(campaigns_data)
    campaigns_df['campaign_cost'] = campaigns_df['cost'].astype(float) * 2 # Умножает стоимость на 2
    # ... (дальнейшая работа с данными) ...