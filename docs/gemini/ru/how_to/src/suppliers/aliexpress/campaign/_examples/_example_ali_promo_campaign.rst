Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код создает объект рекламной кампании AliExpress. Он устанавливает имя кампании, категорию, язык и валюту. Код также инициирует загрузку данных о продуктах, необходимых для кампании.

Шаги выполнения
-------------------------
1. Импортируются необходимые библиотеки и модули, включая `AliPromoCampaign`, `AliAffiliatedProducts`, функции для работы с файлами и каталогами, и логгирование.
2. Определяется директория кампаний на Google Диск и получаются имена кампаний в этой директории.
3. Устанавливаются значения для имени кампании (`campaign_name`), категории (`category_name`), языка (`language`) и валюты (`currency`).
4. Создается объект `SimpleNamespace` `a` с использованием класса `AliPromoCampaign`, передавая в него имя кампании, категорию, язык и валюту.
5. Из объекта `a` извлекаются атрибуты `campaign`, `category` и `products`, которые содержат соответствующую информацию.
6. Код демонстрирует два способа инициализации класса `AliPromoCampaign`:  с использованием словаря и с использованием строк.

Пример использования
-------------------------
.. code-block:: python

    import header
    from pathlib import Path
    from types import SimpleNamespace
    from src import gs
    from src.suppliers.aliexpress import AliPromoCampaign
    from src.suppliers.aliexpress import AliAffiliatedProducts
    from src.utils import get_filenames, get_directory_names, read_text_file, csv2dict
    from src.utils import j_loads_ns
    from src.utils import pprint
    from src.logger import logger

    campaigns_directory = Path(gs.path.google_drive, 'aliexpress', 'campaigns')
    campaign_names = get_directory_names(campaigns_directory)

    campaign_name = '280624_cleararanse'
    category_name = 'gaming_comuter_accessories'
    language = 'EN'
    currency = 'USD'

    a = AliPromoCampaign(campaign_name=campaign_name,
                         category_name=category_name,
                         language=language,
                         currency=currency)

    campaign = a.campaign
    category = a.category
    products = a.category.products

    # Пример с использованием словаря для инициализации
    a_dict = AliPromoCampaign(campaign_name, category_name, {'EN': 'USD'})

    # Пример с использованием строк для инициализации
    a_string = AliPromoCampaign(campaign_name, category_name, 'EN', 'USD')