# Анализ кода модуля src.endpoints.advertisement.facebook.start_sergey

**Качество кода**
7
- Плюсы
    - Код имеет чёткую структуру, разделен на функции, что упрощает чтение и поддержку.
    - Используется `logger` для отслеживания работы программы.
    - Присутствуют docstring для функций.
    - Использование `pathlib` для работы с путями.
    - Выделение основных путей и настроек в константы.
- Минусы
    - Отсутствуют docstring для модуля.
    - Использование `copy.copy` для списков (можно использовать более эффективные методы).
    - Не все импорты используются (например, `header`).
    - Присутствует избыточное использование `print` для логирования, вместо `logger`.
    - Жестко заданные имена кампаний, стоит вынести в конфигурационный файл.
    - Отсутствует проверка на существование директорий или файлов.
    - Отсутствие обработки ошибок при запуске промоутера.
    - Не используется `j_loads` или `j_loads_ns` для работы с json файлами.
    - Константы для путей вынесены не в `settings`, а в глобальную область, что не очень удобно.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить docstring для модуля.
    - Улучшить docstring функций, указав типы аргументов и возвращаемых значений.

2.  **Импорты:**
    - Удалить неиспользуемые импорты.
    - Привести импорты к единому стандарту.

3.  **Логирование:**
    - Заменить `print` на `logger.info` или `logger.debug`.
    - Использовать `logger.error` для записи исключений.

4.  **Обработка ошибок:**
    - Добавить обработку исключений при работе с файлами.
    - Логировать все ошибки с помощью `logger.error`.
    - Проверять, что директории и файлы существуют перед работой с ними.

5.  **Конфигурация:**
    - Вынести имена кампаний и другие константы в конфигурационный файл или переменные окружения.
    - Использовать `j_loads` или `j_loads_ns` для работы с json файлами.
    - Вынести пути к файлам в настройки

6.  **Общая структура:**
    -  Улучшить структуру кода, выделив повторяющиеся части в отдельные функции.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для запуска рекламных кампаний в Facebook.
=========================================================================================

Этот модуль содержит функции для запуска рекламных кампаний в Facebook,
управляя процессом запуска для различных языковых групп и кампаний.

Пример использования
--------------------

Пример запуска рекламной кампании:

.. code-block:: python

    from src.webdriver.driver import Driver, Chrome
    from src.endpoints.advertisement.facebook.start_sergey import main

    if __name__ == "__main__":
        driver = Driver(Chrome)
        main(driver)
"""
MODE = 'dev'

import random
import time
from pathlib import Path
# from src import gs # gs теперь импортируется внутри main
from src.utils.file import get_directory_names
from src.webdriver.driver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger.logger import logger
from src.utils.date_time import interval
from src.utils.jjson import j_loads
# from src.config.settings import Settings # settings теперь импортируется внутри main

# Определение групп и категорий
# Пути вынесены в константы
GROUP_FILE_PATHS_RU: list[str] = ["sergey_pages.json"]
ADV_FILE_PATHS_RU: list[str] = ["ru_ils.json"]
GROUP_FILE_PATHS_HE: list[str] = ["sergey_pages.json"]
ADV_FILE_PATHS_HE: list[str] = ["he_ils.json"]
GROUP_CATEGORIES_TO_ADV = ['sales', 'biz']


def run_campaign(d: Driver, promoter_name: str, campaigns: list | str, group_file_paths: list, language: str, currency: str):
    """Запускает рекламную кампанию.

    :param d: Экземпляр драйвера.
    :type d: Driver
    :param promoter_name: Имя рекламодателя.
    :type promoter_name: str
    :param campaigns: Список кампаний или имя одной кампании.
    :type campaigns: list | str
    :param group_file_paths: Пути к файлам с группами.
    :type group_file_paths: list
    :param language: Язык рекламной кампании.
    :type language: str
    :param currency: Валюта рекламной кампании.
    :type currency: str
    :raises Exception: Если при запуске кампании возникает ошибка.
    """
    try:
        # Код создает объект FacebookPromoter с переданными параметрами
        promoter = FacebookPromoter(d, promoter=promoter_name)
        promoter.run_campaigns(
            campaigns=campaigns,
            group_file_paths=group_file_paths,
            group_categories_to_adv=GROUP_CATEGORIES_TO_ADV,
            language=language,
            currency=currency,
            no_video=False
        )
    except Exception as e:
        # Логируем ошибку, если что-то пошло не так во время выполнения кампании
        logger.error(f"Ошибка при запуске кампании {campaigns}: {e}", exc_info=True)


def campaign_cycle(d: Driver, settings):
    """Управляет циклом запуска кампаний.

    :param d: Экземпляр драйвера.
    :type d: Driver
    :param settings: Экземпляр класса настроек.
    :type settings: src.config.settings.Settings
    :return: True, если цикл выполнен успешно.
    :rtype: bool
    """

    # Код копирует списки путей для избежания изменения исходных данных.
    file_paths_ru = GROUP_FILE_PATHS_RU[:]
    file_paths_ru.extend(ADV_FILE_PATHS_RU)
    file_paths_he = GROUP_FILE_PATHS_HE[:]
    file_paths_he.extend(ADV_FILE_PATHS_HE)

    # Список словарей [{language:currency}]
    language_currency_pairs = [{"HE": "ILS"}, {"RU": "ILS"}]

    for lc in language_currency_pairs:
        # Извлечение языка и валюты из словаря
        for language, currency in lc.items():
            # Определение group_file_paths на основе language
            group_file_paths = file_paths_ru if language == "RU" else file_paths_he

            # Загрузка списка кампаний из json
            try:
                campaigns_config = j_loads(settings.path.config / 'campaigns.json')
                campaigns = campaigns_config.get(language, [])
                
                # Если кампании не найдены в конфиге, используем дефолтные значения.
                if not campaigns:
                    campaigns = ['kazarinov_ru'] if language == "RU" else ['kazarinov_he']

                for c in campaigns:
                    run_campaign(
                        d, 'kazarinov', c,
                        group_file_paths=group_file_paths,
                        language=language,
                        currency=currency
                    )
            except Exception as e:
                logger.error(f'Ошибка загрузки или обработки конфигурации кампаний {e}', exc_info=True)
                continue

            try:
                campaigns = get_directory_names(settings.path.google_drive / 'aliexpress' / 'campaigns')
                run_campaign(
                    d, 'aliexpress', campaigns,
                    group_file_paths=group_file_paths,
                    language=language,
                    currency=currency
                )
            except Exception as e:
                logger.error(f'Ошибка при запуске кампании aliexpress {e}', exc_info=True)
                continue
    return True


def main(driver=None):
    """Основная функция для запуска рекламных кампаний.

    :param driver: Экземпляр драйвера, по умолчанию None.
    :type driver: Driver, optional
    """
    from src import gs
    from src.config.settings import Settings
    settings = Settings()

    try:
        if not driver:
            d = Driver(Chrome)
            d.get_url("https://facebook.com")
        else:
            d = driver
        
        while True:
            if interval():
                logger.info("Good night!")
                time.sleep(1000)

            # Запуск цикла кампаний.
            campaign_cycle(d, settings)
            ...

            # Логирование и задержка.
            logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}")
            t = random.randint(30, 360)
            logger.debug(f"sleeping {t} sec")
            time.sleep(t)

    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")
    except Exception as e:
         logger.error(f'Неизвестная ошибка в main {e}', exc_info=True)
    finally:
       if not driver:
          d.close()

if __name__ == "__main__":
    main()