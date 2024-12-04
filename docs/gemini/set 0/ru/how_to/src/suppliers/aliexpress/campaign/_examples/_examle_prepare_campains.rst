Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный код предоставляет примеры использования функций из модуля `prepare_campaigns`.  Он демонстрирует, как обработать одну категорию кампании, конкретную кампанию или все кампании, используя различные параметры.  Также он определяет директорию кампаний и список поддерживаемых языков с валютами.

Шаги выполнения
-------------------------
1. **Импортирует необходимые функции:**  Код импортирует все функции из модуля `prepare_campaigns`  в начале файла, что позволяет использовать их в последующих примерах.

2. **Обрабатывает одну категорию кампании:**  Вызывает функцию `process_campaign_category` с параметрами, задающими название категории ("SummerSale", "Electronics"), язык ("EN") и валюту ("USD"). Параметр `force=True` указывает на принудительное обновление данных.

3. **Обрабатывает конкретную кампанию:**  Вызывает функцию `process_campaign` для обработки кампании "WinterSale" с указанием списка категорий ("Clothing", "Toys"), языка ("EN"), валюты ("USD"), и параметром `force=False`, указывающим, что обновление данных не должно быть принудительным.

4. **Обрабатывает все кампании:** Вызывает функцию `process_all_campaigns` с указанием языка ("EN") и валюты ("USD").  Параметр `force=True` указывает на принудительное обновление данных для всех кампаний.

5. **Определяет директорию и список языков:** Определяет путь к директории кампаний, используя переменную `gs.path.google_drive`, и сохраняет её в `campaigns_directory`.  Создаёт словарь `languages`, сопоставляющий языки с соответствующими валютами.  Эта информация вероятно будет использоваться для выбора параметров при обработке кампаний.


Пример использования
-------------------------
.. code-block:: python

    import os  # Добавьте эту строку, если переменная gs.path не определена.
    from pathlib import Path

    # Замените 'your_google_drive_path' на реальный путь
    gs = type('gs', (), {'path': type('path', (), {'google_drive': 'your_google_drive_path'})()})  # Предположите, что gs.path - это путь к гугл драйву.



    from ..prepare_campaigns import * # предполагая что prepare_campaigns - это путь к вашему модулю


    # Example 1: Process a Single Campaign Category
    process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)

    # Example 2: Process a Specific Campaign
    process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)

    # Example 3: Process All Campaigns
    process_all_campaigns(language="EN", currency="USD", force=True)

    # Определение пути к директории кампаний (важно: заменив 'your_google_drive_path' на реальный путь к вашей папке на гугл диске!)
    campaigns_directory = Path(gs.path.google_drive, 'aliexpress', 'campaigns')
    campaign_names = get_directory_names(campaigns_directory)

    # Список языков и валют
    languages = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}