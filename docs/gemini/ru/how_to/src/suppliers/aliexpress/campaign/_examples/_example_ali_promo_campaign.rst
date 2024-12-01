Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код создает объект AliPromoCampaign, представляющий рекламную кампанию на AliExpress. Он инициализирует объект с именем кампании, категорией, языком и валютой.  Код также извлекает и устанавливает значения для атрибутов кампании, категории и продуктов.  Важно отметить, что код использует классы из модулей `AliPromoCampaign`, `AliAffiliatedProducts`, и другие вспомогательные функции из `src.utils` и `src.logger`.

Шаги выполнения
-------------------------
1. **Импортирует необходимые модули:** Код импортирует классы и функции из различных модулей, включая `AliPromoCampaign`, `AliAffiliatedProducts`,  `get_filenames`, `get_directory_names`, `read_text_file`, `csv2dict`, `j_loads_ns`, `pprint`, `logger`, и `Path` из стандартной библиотеки Python.

2. **Определяет директорию кампаний:**  Получает путь к директории с рекламными кампаниями на Google Диске, используя `gs.path.google_drive`.

3. **Извлекает имена кампаний:**  Получает список имен каталогов (имен кампаний) в указанной директории с помощью функции `get_directory_names`.

4. **Назначает переменные для параметров кампании:**  Определяет переменные `campaign_name`, `category_name`, `language` и `currency` для настройки рекламной кампании.

5. **Создает экземпляр класса AliPromoCampaign:**  Создает экземпляр класса `AliPromoCampaign`, передавая в конструктор значения из переменных, заданные в шаге 4.  Важно, что этот код использует два разных способа инициализации объекта, демонстрируя гибкость.

6. **Получает атрибуты кампании:**  Получает ссылки на атрибуты `campaign`, `category` и `products` объекта `a`, созданного в шаге 5.

7. **(Альтернативный способ инициализации):**  Представлен альтернативный способ инициализации `AliPromoCampaign`,  при котором `category_name` передается как словарь, содержащий значения для разных языков. Также показано как инициализировать его с помощью параметров как строки.


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
    
    # ... (Импорт других модулей, как в исходном примере)
    
    campaigns_directory = Path(gs.path.google_drive, 'aliexpress', 'campaigns')
    campaign_names = get_directory_names(campaigns_directory)
    
    campaign_name = '280624_cleararanse'
    category_name = 'gaming_comuter_accessories'
    language = 'EN'
    currency = 'USD'
    
    # Использование первого способа инициализации
    a = AliPromoCampaign(campaign_name=campaign_name, category_name=category_name, language=language, currency=currency)
    
    # Или использование второго способа инициализации
    b = AliPromoCampaign(campaign_name, category_name, {'EN': 'USD'})

    # Или третий способ инициализации
    c = AliPromoCampaign(campaign_name, category_name, 'EN', 'USD') # Обратите внимание на круглые скобки
    
    # Доступ к атрибутам объекта
    print(a.campaign)
    print(b.category)
    print(c.products)