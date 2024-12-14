## Анализ кода модуля `gspreadsheet.py`

**Качество кода**
8
-  Плюсы
    - Код в целом структурирован и выполняет свою основную задачу: взаимодействие с Google Sheets API.
    - Используется класс `GSpreadsheet` для инкапсуляции логики работы с таблицами.
    - Присутствуют docstring для классов и методов, хотя они требуют доработки.
    -  Импорт необходимых библиотек.
-  Минусы
    -  Много дублирующихся комментариев и лишних docstring.
    -  Отсутствует использование `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не все комментарии соответствуют стандарту reStructuredText (RST).
    -  Не используется логгирование ошибок.
    -  Имена переменных и методов не всегда соответствуют соглашениям (например, `gsh`, `s_id`, `sh_title`).
    -  Использование `print` вместо логирования.
    -  Отсутствуют проверки на корректность id или title при открытии spreadsheet.

**Рекомендации по улучшению**

1.  **Удалить лишние комментарии и docstring**: Оставить только осмысленные docstring в формате reStructuredText (RST).
2.  **Использовать `j_loads` для загрузки JSON**: Заменить `json.loads` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Добавить логирование**: Использовать `logger.error` для записи ошибок вместо `print`.
4.  **Стандартизировать имена**: Привести имена переменных и функций к более понятному и общепринятому виду.
5.  **Обработка ошибок**: Добавить try-except блоки там, где это необходимо.
6.  **Улучшить документацию**: Добавить более подробное описание классов и методов в docstring.
7.  **Удалить лишний код**: Убрать закомментированный код, который не используется.
8.  **Проверки на корректность** Добавить проверки входных параметров, таких как id и title, на корректность.
9.  **Использовать `from src.logger.logger import logger`**: для логирования ошибок.
10. **Удалить лишнии импорты** : Удалить не используемые импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль предоставляет класс :class:`GSpreadsheet`, который используется для взаимодействия
с Google Sheets API. Он позволяет открывать, создавать и получать доступ к таблицам.

Пример использования
--------------------

Пример использования класса `GSpreadsheet`:

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.gspreadsheet import GSpreadsheet

    spreadsheet = GSpreadsheet(s_id='your_spreadsheet_id')
    # Или
    spreadsheet = GSpreadsheet(s_title='Your Spreadsheet Title')
    data = spreadsheet.get_all_spreadsheets_for_current_account()
"""
from src.global_settingspread import Spreadsheet, service_account
import gspread
from typing import List, Type, Union
from src.utils.jjson import j_loads
from src.logger.logger import logger



class GSpreadsheet(Spreadsheet):
    """
    Класс для работы с Google Sheets.

    :param s_id: ID таблицы Google Sheets.
    :type s_id: str, optional
    :param s_title: Название таблицы Google Sheets.
    :type s_title: str, optional
    :raises ValueError: Если не передан id или title
    """
    gsh: Spreadsheet = None
    gclient = gspread.client
    
    def __init__(self, s_id: str = None, s_title: str = None, *args, **kwargs):
        """
        Инициализация класса GSpreadsheet.
        
        :param s_id: ID таблицы Google Sheets.
        :type s_id: str, optional
        :param s_title: Название таблицы Google Sheets.
        :type s_title: str, optional
        """
        secret_file = 'goog/onela-hypotez-1aafa5e5d1b5.json'
        try:
            self.gclient = service_account(filename=secret_file)
        except Exception as ex:
             logger.error(f'Ошибка при инициализации gclient {ex=}')
             raise
        if s_id:
            self.gsh = self.get_by_id(s_id)
        elif s_title:
             self.gsh = self.get_by_title(s_title)
        else:
            logger.error('Не указан id или title таблицы')
            raise ValueError('Не указан id или title таблицы')


    def get_project_spreadsheets_dict(self) -> dict:
        """
        Получение словаря с настройками таблиц.

        :return: Словарь с настройками таблиц.
        :rtype: dict
        """
        try:
            # Используем j_loads для загрузки JSON
            return j_loads('goog/spreadsheets.json')
        except Exception as ex:
            logger.error(f'Ошибка загрузки файла настроек {ex=}')
            return {}


    def get_by_title(self, sh_title: str = 'New Spreadsheet'):
        """
        Открытие или создание таблицы по названию.
        
        :param sh_title: Название таблицы.
        :type sh_title: str
        """
        try:
            if not sh_title:
               logger.error('Не указано название таблицы')
               raise ValueError('Не указано название таблицы')
            all_spreadsheets = self.gclient.openall()
            if sh_title not in [sh.title for sh in all_spreadsheets]:
                # Код создает новую таблицу
                self.gclient.create(sh_title)
                self.gclient.share('d07708766@gmail.com', perm_type='user', role='writer')
                logger.info(f'Создана новая таблица {sh_title=}')
            else:
                # Код открывает существующую таблицу
                 self.gsh = self.gclient.open(sh_title)
                 logger.info(f'Таблица {sh_title} уже существует')
        except Exception as ex:
             logger.error(f'Ошибка при создании/открытии таблицы {ex=}')
             raise
    
    def get_by_id(self, sh_id: str) -> Spreadsheet:
        """
        Открытие таблицы по ID.

        :param sh_id: ID таблицы Google Sheets.
        :type sh_id: str
        :return: Объект Spreadsheet.
        :rtype: Spreadsheet
        :raises ValueError: Если id не передан
        """
        if not sh_id:
             logger.error('Не указан id таблицы')
             raise ValueError('Не указан id таблицы')
        try:
            # Код открывает таблицу по ID
            return self.gclient.open_by_key(sh_id)
        except Exception as ex:
            logger.error(f'Ошибка открытия таблицы по id {sh_id=} {ex=}')
            raise


    def get_all_spreadsheets_for_current_account(self):
        """
        Получение всех таблиц для текущего аккаунта.

        :return: Список всех таблиц.
        :rtype: list
        """
        try:
             # Код открывает все таблицы аккаунта
            return self.gclient.openall()
        except Exception as ex:
            logger.error(f'Ошибка получения списка таблиц {ex=}')
            return []