## Анализ кода модуля `ali_campaign_editor.py`

**Качество кода**
8
-   Плюсы
    *   Код хорошо структурирован и разбит на методы.
    *   Используются `SimpleNamespace` для представления данных.
    *   Присутствует логирование ошибок с использованием `logger`.
    *   В целом, код соответствует PEP 8.
-   Минусы
    *   Не все методы имеют docstring.
    *   Используются стандартные блоки `try-except` для обработки ошибок, которые можно заменить на `logger.error`.
    *   Некоторые комментарии не соответствуют reStructuredText (RST) формату.
    *   Множественные `...` как точки остановки.
    *   Отсутствуют проверки типов данных.
    *   Не всегда последовательное использование `logger.debug`, `logger.warning`, `logger.error`, `logger.critical`, `logger.success`.
    *   Некоторые импорты не используются.

**Рекомендации по улучшению**

1.  **Документация**:
    *   Добавить docstring в формате RST для всех функций, методов и классов.
    *   Переписать комментарии в формате RST, включая описание параметров, возвращаемых значений и исключений.
    *   Добавить примеры использования в docstring.
2.  **Логирование**:
    *   Избегать избыточного использования `try-except`, вместо этого использовать `logger.error` с информацией об исключении.
    *   Использовать `logger.debug` для отладочной информации, `logger.warning` для предупреждений, `logger.error` для ошибок, `logger.critical` для критических ошибок и `logger.success` для сообщений об успешном выполнении операций.
3.  **Обработка данных**:
    *   Использовать `j_loads` и `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
    *   Удалить или заменить все `...` на конкретные действия или комментарии.
4.  **Структура**:
    *   Удалить неиспользуемые импорты.
    *   Уточнить типы для переменных, где это возможно.
5.  **Рефакторинг**:
    *   Упростить логику там, где это возможно, делая код более читаемым.
    *   Добавить проверки типов и валидацию входных данных.
6.  **Комментарии**:
     *  Добавить пояснения к каждому блоку кода, что он делает.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для управления рекламными кампаниями AliExpress.
=======================================================

Этот модуль предоставляет класс :class:`AliCampaignEditor` для управления рекламными кампаниями AliExpress,
включая создание, обновление и удаление продуктов и категорий.

Пример использования
--------------------

Пример создания экземпляра класса `AliCampaignEditor`:

.. code-block:: python

    editor = AliCampaignEditor(campaign_name="Летняя Распродажа", language="RU", currency="RUB")

"""
MODE = 'dev'

import re
import shutil
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional, Any

# избыточный импорт header
# from header import header
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https
from src.utils.jjson import j_loads_ns, j_loads, j_dumps
# избыточный импорт csv2dict
# from src.utils.convertors.csv import csv2dict
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.logger.logger import logger


class AliCampaignEditor(AliPromoCampaign):
    """
    Класс для редактирования рекламных кампаний.

    Предоставляет методы для управления продуктами, категориями и параметрами кампании.
    """

    def __init__(self,
                 campaign_name: str,
                 language: Optional[str | dict] = None,
                 currency: Optional[str] = None):
        """
        Инициализация редактора рекламной кампании.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык кампании. Может быть строкой или словарем.
        :type language: Optional[str | dict]
        :param currency: Валюта кампании.
        :type currency: Optional[str]
        :raises ValueError: Если не предоставлено ни `campaign_name`, ни `campaign_file`.

        :Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
        """
        super().__init__(campaign_name=campaign_name, language=language, currency=currency)
        # self.google_sheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency, campaign_editor=self)

    def delete_product(self, product_id: str, exc_info: bool = False):
        """
        Удаление товара, у которого нет партнерской ссылки.

        :param product_id: Идентификатор товара для удаления.
        :type product_id: str
        :param exc_info: Включать ли информацию об исключении в логи. По умолчанию False.
        :type exc_info: bool

        :Example:
           >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
           >>> editor.delete_product("12345")
        """
        _product_id = extract_prod_ids(product_id) # Извлечение числового ID из product_id
        product_path = self.category_path / 'sources.txt' # определение пути к файлу списка товаров
        prepared_product_path = self.category_path / '_sources.txt' # определение пути к временному файлу списка товаров

        products_list = read_text_file(product_path) # чтение списка товаров из файла
        if products_list:
            for record in products_list: # итерация по списку товаров
                if _product_id: # если ID был извлечен
                    record_id = extract_prod_ids(record) # извлекаем ID из записи
                    if record_id == str(product_id): # если ID записи совпадает с ID товара
                        products_list.remove(record) # удаляем запись из списка
                        save_text_file((products_list, '\n'), prepared_product_path) # сохраняем обновленный список во временный файл
                        break
                else: # если ID не был извлечен
                    if record == str(product_id): # если запись совпадает с ID товара
                        products_list.remove(record) # удаляем запись из списка
                        save_text_file((products_list, '\n'), product_path) # сохраняем обновленный список в файл списка товаров
        else: # если список товаров пуст
            product_path = self.category_path / 'sources' / f'{product_id}.html' # формируем путь к файлу товара
            try:
                product_path.rename(self.category_path / 'sources' / f'{product_id}_.html') # переименовываем файл товара
                logger.success(f"Product file {product_path=} renamed successfully.") # логируем успешное переименование
            except FileNotFoundError as ex: # если файл товара не найден
                logger.error(f"Product file {product_path=} not found.", exc_info=exc_info) # логируем ошибку
            except Exception as ex: # если произошла другая ошибка
                logger.critical(f"An error occurred while deleting the product file {product_path}.", ex) # логируем критическую ошибку


    def update_product(self, category_name: str, lang: str, product: dict):
        """
        Обновление информации о товаре в категории.

        :param category_name: Название категории, в которой нужно обновить товар.
        :type category_name: str
        :param lang: Язык кампании.
        :type lang: str
        :param product: Словарь с информацией о товаре.
        :type product: dict

        :Example:
           >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
           >>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
        """
        self.dump_category_products_files(category_name, lang, product)  # Обновление файлов товаров категории


    def update_campaign(self):
        """
        Обновление свойств кампании, таких как описание или теги.
        """
        #  Код обновления параметров кампании, например description, tags
        ...

    def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
        """
        Обновление категории в JSON файле.

        :param json_path: Путь к JSON файлу.
        :type json_path: Path
        :param category: Объект категории для обновления.
        :type category: SimpleNamespace
        :return: True, если обновление прошло успешно, иначе False.
        :rtype: bool

        :Example:
            >>> category = SimpleNamespace(name="New Category", description="Updated description")
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> result = editor.update_category(Path("category.json"), category)
            >>> print(result)  # True, если успешно
        """
        try:
            data = j_loads(json_path)  # Загрузка данных из JSON файла
            data['category'] = category.__dict__  # Преобразование SimpleNamespace в словарь
            j_dumps(data, json_path)  # Сохранение обновленных данных в JSON файл
            return True
        except Exception as ex:
            logger.error(f"Failed to update category {json_path}: {ex}")  # Логирование ошибки
            return False

    def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
        """
        Возвращает объект SimpleNamespace для заданной категории.

        :param category_name: Название категории для получения.
        :type category_name: str
        :return: Объект SimpleNamespace, представляющий категорию, или None, если категория не найдена.
        :rtype: Optional[SimpleNamespace]

        :Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> category = editor.get_category("Electronics")
            >>> print(category)  # SimpleNamespace или None
        """
        try:
            if hasattr(self.campaign.category, category_name): # Проверяет наличие категории в кампании
                return getattr(self.campaign.category, category_name) # Возвращает объект категории
            else:
                logger.warning(f"Category {category_name} not found in the campaign.") # Логирует предупреждение, если категория не найдена
                return # возвращает None
        except Exception as ex:
             logger.error(f"Error retrieving category {category_name}.", ex, exc_info=True) # Логирует ошибку получения категории
             return # возвращает None


    @property
    def list_categories(self) -> Optional[List[str]]:
        """
        Получение списка категорий в текущей кампании.

        :return: Список названий категорий или None, если категории не найдены.
        :rtype: Optional[List[str]]

        :Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> categories = editor.list_categories
            >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
        """
        try:
            # Проверяет, есть ли у кампании атрибут category и является ли он SimpleNamespace
            if hasattr(self.campaign, 'category') and isinstance(self.campaign.category, SimpleNamespace):
                return list(vars(self.campaign.category).keys()) # Возвращает список названий категорий
            else:
                logger.warning("No categories found in the campaign.") # Логирует предупреждение, если категории не найдены
                return # возвращает None
        except Exception as ex:
            logger.error(f"Error retrieving categories list: {ex}") # Логирует ошибку получения списка категорий
            return # возвращает None


    def get_category_products(self, category_name: str) -> Optional[List[SimpleNamespace]]:
        """
        Чтение данных о товарах из JSON файлов для конкретной категории.

        :param category_name: Имя категории.
        :type category_name: str
        :return: Список объектов SimpleNamespace, представляющих товары, или None, если нет товаров.
        :rtype: Optional[List[SimpleNamespace]]

        :Example:
            >>> products = campaign.get_category_products("Electronics")
            >>> print(len(products))
            15
        """
        category_path = (
            self.base_path
            / "category"
            / category_name
            / f"{self.language}_{self.currency}"
        ) # Формирует путь к директории категории
        json_filenames = get_filenames(category_path, extensions="json") # получает список файлов json в директории
        products = [] # инициализирует список товаров

        if json_filenames:
            for json_filename in json_filenames: # итерируется по списку файлов
                product_data = j_loads_ns(category_path / json_filename) # загружает данные из файла
                product = SimpleNamespace(**vars(product_data)) # формирует объект SimpleNamespace
                products.append(product) # добавляет товар в список
            return products # возвращает список товаров
        else:
            logger.error( # логирует ошибку, если нет файлов
                f"No JSON files found for {category_name=} at {category_path=}.\nStart prepare category"
            )
            self.process_category_products(category_name) # вызывает метод подготовки товаров категории
            return # возвращает None