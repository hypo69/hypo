```python
## \file hypotez/src/endpoints/advertisement/facebook/start_sergey.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.advertisement.facebook """

"""Отправка рекламных объявлений в группы фейсбук."""
import header
import random
import time
import copy
from pathlib import Path

from __init__ import gs
from src.utils.file import get_directory_names, get_filenames
from src.webdriver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.logger import logger
from src.utils.date_time import interval

# Определение групп и категорий
group_file_paths_ru: list[str] = ["sergey_pages.json"]
adv_file_paths_ru: list[str] = ["ru_ils.json"]
group_file_paths_he: list[str] = ["sergey_pages.json"]
adv_file_paths_he: list[str] = ["he_ils.json"]
group_categories_to_adv = ['sales', 'biz']

def run_campaign(driver: Driver, promoter_name: str, campaigns: list, group_file_paths: list, language: str, currency: str) -> None:
    """Запускает рекламную кампанию в Facebook.

    Args:
        driver (Driver): Экземпляр драйвера для взаимодействия с браузером.
        promoter_name (str): Имя рекламодателя.
        campaigns (list): Список названий кампаний.
        group_file_paths (list): Список путей к файлам с группами.
        language (str): Язык рекламной кампании (например, "RU", "HE").
        currency (str): Валюта рекламной кампании (например, "ILS").

    Raises:
        Exception: Если возникла ошибка при запуске кампании.
    """

    try:
        promoter = FacebookPromoter(driver, promoter=promoter_name)
        promoter.run_campaigns(
            campaigns=campaigns,
            group_file_paths=group_file_paths,
            group_categories_to_adv=group_categories_to_adv,
            language=language,
            currency=currency,
            no_video=False
        )
    except Exception as e:
        logger.error(f"Ошибка при запуске кампании: {e}")
        raise


def campaign_cycle(driver: Driver) -> bool:
    """Цикл для управления запуском кампаний для разных языков и валют.

    Args:
        driver (Driver): Экземпляр драйвера.

    Returns:
        bool: True, если цикл завершен успешно, иначе False.
    """

    file_paths_ru = copy.copy(group_file_paths_ru)
    file_paths_ru.extend(adv_file_paths_ru)  # <- promo in groups
    file_paths_he = copy.copy(group_file_paths_he)
    file_paths_he.extend(adv_file_paths_he)

    language_currency_pairs = [{"language": "RU", "currency": "ILS"}, {"language": "HE", "currency": "ILS"}]

    for pair in language_currency_pairs:
        language = pair['language']
        currency = pair['currency']
        
        group_file_paths = file_paths_ru if language == "RU" else file_paths_he

        # Загрузка кампаний из папки кампаний (вместо жестко заданных списков)
        campaigns_dir = gs.path.google_drive / 'aliexpress' / 'campaigns'
        campaigns = get_directory_names(campaigns_dir) if campaigns_dir.exists() else []

        if not campaigns:
            logger.warning("Папка с кампаниями не найдена. Проверьте путь.")
            continue


        # Правильный способ загрузки кампаний
        for campaign in campaigns:
            if language == "RU" and not campaign.endswith("_ru"):
              continue  # Skip campaign if language doesn't match
            if language == "HE" and not campaign.endswith("_he"):
              continue  # Skip campaign if language doesn't match

            try:
                run_campaign(driver, 'kazarinov', [campaign], group_file_paths, language, currency)
            except Exception as e:
                logger.error(f"Ошибка при запуске кампании {campaign}: {e}")

    return True


def main():
    """Основная функция для запуска рекламных кампаний."""
    try:
        driver = Driver(Chrome)
        driver.get_url(r"https://facebook.com")

        while True:
            if interval():
                print("Good night!")
                time.sleep(1000)  # Задержка 1000 секунд (16.67 минут)

            if campaign_cycle(driver):
              logger.debug(f"campaign cycle finished at {time.strftime('%H:%M:%S')}")
            else:
              logger.error("Ошибка при выполнении цикла кампаний.")
              
            logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}")
            sleep_time = random.randint(300, 3600)  # Случайное время от 5 до 60 минут
            print(f"sleeping {sleep_time} sec")
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")

if __name__ == "__main__":
    main()
```

**Основные улучшения:**

* **Обработка ошибок:** Добавлена обработка исключений (`try...except`) в `run_campaign` и `campaign_cycle`, чтобы программа не прекращала работу при возникновении ошибок.  Теперь она логгирует ошибку и продолжает работу.
* **Динамическое получение кампаний:**  Код теперь динамически загружает названия кампаний из директории `gs.path.google_drive / 'aliexpress' / 'campaigns'`.  Это намного гибче, чем хранить список кампаний в коде.
* **Проверка наличия директории:** Добавлена проверка `if campaigns_dir.exists()`.  Это предотвращает ошибку, если директория с кампаниями не существует.
* **Проверка языка кампаний:** Добавлены проверки `if language == "RU" and not campaign.endswith("_ru")` и `if language == "HE" and not campaign.endswith("_he")` для правильной обработки кампаний.
* **Более разумная задержка:** Задержка теперь случайная от 5 до 60 минут, что более реалистично и предотвращает частые переходы.
* **Яснее логирование:** Логгирование стало более информативным, включая конкретные ошибки и уведомления о завершении цикла.
* **Типизация:** Добавлена типизация для `run_campaign` и `campaign_cycle` для повышения читабельности и предотвращения ошибок.
* **Обновление импорта:** Обновлён импорт модуля `gs`, так как он подразумевается как глобальный, доступный из внешнего контекста.


**Рекомендации:**

* **Проверка путей:**  Убедитесь, что переменная `gs.path.google_drive` корректно указывает на папку с кампаниями.
* **Файлы JSON:**  В коде предполагается, что файлы `sergey_pages.json` и `ru_ils.json` содержат структуру данных, необходимую для запуска кампании.  Важно проверить их структуру и корректность.
* **FacebookPromoter:**  Посмотрите код класса `FacebookPromoter` на предмет потенциальных проблем (например, обработка ошибок, логирование, использование driver).

**Критически важное замечание:** Этот код предполагает, что `gs.path.google_drive` определен где-то в вашем проекте. Если `gs` — это нестандартная библиотека, убедитесь, что она корректно импортируется.  Если `gs` — просто переменная, определяющая путь к Google Drive, добавьте соответствующую инициализацию.