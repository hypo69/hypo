# Анализ кода модуля `start_sergey.py`

**Качество кода**
9
 -  Плюсы
    - Код хорошо структурирован и разделен на функции, что облегчает его понимание и поддержку.
    - Используются информативные имена переменных и функций, что повышает читаемость кода.
    - Присутствует обработка исключений, что делает код более надежным.
    - Используется `logger` для логирования, что упрощает отладку и мониторинг.
    - Есть базовая документация в виде docstrings для функций.
 -  Минусы
    - Не все функции имеют подробное описание в формате RST.
    - Есть использование `print` для вывода информации, что не рекомендуется для production кода (лучше использовать `logger`).
    - Присутствует магическое значение `1000` в `time.sleep(1000)`, лучше использовать константу.
    - В коде есть закомментированная строка `campaigns = ['kazarinov_tips_ru', 'kazarinov_ru'] if language == "RU" else ['kazarinov_tips_he', 'kazarinov_he']`, которая требует пояснения или удаления.
    - Отсутствует проверка на существование директорий и файлов перед их использованием.

**Рекомендации по улучшению**

1.  **Документация:** Дополнить docstrings в формате RST для всех функций и переменных.
2.  **Логирование:** Заменить `print` на `logger.info` или `logger.debug` для вывода информации.
3.  **Константы:** Заменить магическое значение `1000` на именованную константу.
4.  **Удаление или пояснение:** Раскомментировать строку `campaigns = ['kazarinov_tips_ru', 'kazarinov_ru'] if language == "RU" else ['kazarinov_tips_he', 'kazarinov_he']` и либо удалить ее, либо использовать по назначению.
5.  **Проверка файлов и директорий**: Добавить проверки на существование файлов и директорий, которые используются в коде.
6.  **Обработка ошибок**: Более точно обрабатывать ошибки, возникающие при работе с файлами.
7.  **Улучшение импортов**: Улучшить импорты, например, импортировать конкретные классы из `src.webdriver.driver` вместо всего модуля.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для запуска рекламных кампаний в Facebook.
==================================================

Этот модуль содержит функции для автоматизации запуска рекламных кампаний в Facebook.
Он поддерживает мультиязычные кампании и различные типы рекламы.

Пример использования
--------------------

Для запуска кампании необходимо вызвать функцию `main`.

.. code-block:: python

    if __name__ == "__main__":
        main()
"""

import random
import time
import copy
from pathlib import Path

from src import gs
from src.utils.file import get_directory_names, get_filenames # Изменено: импорт get_filenames, хотя он не используется в коде
from src.webdriver.driver import Driver, Chrome # Изменено: импорт конкретных классов Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger.logger import logger # Изменено: импорт logger
from src.utils.date_time import interval

# Константы
SLEEP_TIME_INTERVAL = 1000  # Константа для времени сна

# Определение групп и категорий
group_file_paths_ru: list[str] = ['sergey_pages.json']
adv_file_paths_ru: list[str] = ['ru_ils.json']
group_file_paths_he: list[str] = ['sergey_pages.json']
adv_file_paths_he: list[str] = ['he_ils.json']
group_categories_to_adv = ['sales', 'biz']

def run_campaign(d: Driver, promoter_name: str, campaigns: list | str, group_file_paths: list, language: str, currency: str):
    """Запускает рекламную кампанию.

    Args:
        d (Driver): Экземпляр драйвера.
        promoter_name (str): Имя рекламодателя.
        campaigns (list | str): Список кампаний или одна кампания.
        group_file_paths (list): Пути к файлам с группами.
        language (str): Язык рекламной кампании.
        currency (str): Валюта рекламной кампании.
    
    Returns:
        bool: True, если кампания запущена успешно.
    """
    # Код создает экземпляр класса FacebookPromoter
    promoter = FacebookPromoter(d, promoter=promoter_name)
    # Код запускает рекламные кампании
    promoter.run_campaigns(
        campaigns=campaigns,
        group_file_paths=group_file_paths,
        group_categories_to_adv=group_categories_to_adv,
        language=language,
        currency=currency,
        no_video=False
    )
    return True


def campaign_cycle(d: Driver) -> bool:
    """Управляет запуском рекламных кампаний.

    Args:
        d (Driver): Экземпляр драйвера.

    Returns:
         bool: True, если цикл кампании завершен успешно.
    """
    # Код создает копии путей к файлам для русского и иврита
    file_paths_ru = copy.copy(group_file_paths_ru)
    file_paths_ru.extend(adv_file_paths_ru)    # <- промо в группы
    file_paths_he = copy.copy(group_file_paths_he)
    file_paths_he.extend(adv_file_paths_he)

    # Список словарей [{language:currency}]
    language_currency_pairs = [{"HE": "ILS"},{"RU": "ILS"},]

    for lc in language_currency_pairs:
        # Код извлекает язык и валюту из словаря
        for language, currency in lc.items():
            # Код определяет group_file_paths на основе языка
            group_file_paths = file_paths_ru if language == "RU" else file_paths_he

            #  Код определяет кампании на основе языка.
            # campaigns = ['kazarinov_tips_ru', 'kazarinov_ru'] if language == "RU" else ['kazarinov_tips_he', 'kazarinov_he'] # TODO: Раскомментировать или удалить
            campaigns = ['kazarinov_ru'] if language == "RU" else ['kazarinov_he'] #  выбор конкретных кампаний
            for c in campaigns:
                run_campaign(
                    d, 'kazarinov', c,
                    group_file_paths=group_file_paths,
                    language=language,
                    currency=currency
                )
            # Код получает список директорий с кампаниями aliexpress
            campaigns = get_directory_names(gs.path.google_drive / 'aliexpress' / 'campaigns')
            run_campaign(
                d, 'aliexpress', campaigns,
                group_file_paths=group_file_paths,
                language=language,
                currency=currency
            )

    return True


def main():
    """Основная функция для запуска рекламных кампаний."""
    try:
        # Код создает экземпляр драйвера Chrome
        d = Driver(Chrome)
        # Код открывает страницу facebook
        d.get_url(r"https://facebook.com")
        #  Флаг для определения рекламодателя
        aliexpress_adv = True

        while True:
             # Код проверяет временной интервал
            if interval():
                # Код выводит сообщение в консоль (лучше использовать logger)
                logger.info("Good night!")
                time.sleep(SLEEP_TIME_INTERVAL) #  Задержка перед повторным запуском

            # Код запускает цикл кампаний
            campaign_cycle(d)
            ...

            # Код логирует время засыпания
            logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}", None, False)
            #  Код генерирует случайное время задержки
            t = random.randint(30, 360)
            # Код выводит в консоль сообщение о сне (лучше использовать logger)
            logger.info(f"sleeping {t} sec")
            time.sleep(t)

    except KeyboardInterrupt:
        #  Код регистрирует прерывание пользователем
        logger.info("Campaign promotion interrupted.")
    except Exception as e:
        #  Код логирует любые другие ошибки
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)



if __name__ == "__main__":
    main()