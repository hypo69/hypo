# Анализ кода модуля `language.py`

**Качество кода**
7
- Плюсы
    - Код содержит описание модуля и класса в формате docstring.
    - Используются аннотации типов.
    - Присутствует обработка ошибок при инициализации класса.
    - Класс наследует от `PrestaShop` и использует его API.
- Минусы
    -  Не все функции имеют docstring.
    -  Импорт `header` не используется, что является избыточным.
    -  Отсутствует обработка ошибок в методах добавления, удаления и обновления языка.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Стиль форматирования кода не соответствует PEP 8 (например, отступы, длина строк).
    -  Присутствует избыточный импорт `from .api import PrestaShop`.
    -  Использование `pprint` из `src.utils.printer` не соответствует принципу логирования.
     
**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring для всех методов, включая описание аргументов и возвращаемых значений.
2.  **Импорты:** Удалить неиспользуемый импорт `header` и дубликат `from .api import PrestaShop`.
3.  **Обработка ошибок:** Добавить обработку ошибок в методы `add_language_PrestaShop`, `delete_language_PrestaShop` и `update_language_PrestaShop`, используя `logger.error` для логирования ошибок.
4.  **Форматирование:** Привести код в соответствие со стандартом PEP 8.
5. **Использование `j_loads`:** Использовать `j_loads` или `j_loads_ns` вместо стандартного `json.load` для чтения файлов, если это требуется в других частях кода.
6. **Логирование:** Заменить `pprint` на `logger.debug` или `logger.info` для вывода информации.
7. **Комментарии:** Добавить комментарии к логике методов.
8. **Улучшить документацию:** Дополнить документацию примерами использования методов класса.

**Оптимизированный код**

```python
"""
Модуль для работы с языками в PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`PrestaLanguage`, который используется для управления языками в PrestaShop.
Модуль предоставляет методы для добавления, удаления, обновления и получения информации о языках.

Пример использования
--------------------

Пример использования класса `PrestaLanguage`:

.. code-block:: python

    from src.endpoints.prestashop.language import PrestaLanguage
    from types import SimpleNamespace

    credentials = SimpleNamespace(api_domain='your_domain', api_key='your_api_key')
    presta_language = PrestaLanguage(credentials=credentials)
    # или
    presta_language = PrestaLanguage(api_domain='your_domain', api_key='your_api_key')
    
    # Добавление нового языка
    presta_language.add_language_PrestaShop('English', 'en')

    # Удаление языка по ID
    presta_language.delete_language_PrestaShop(3)

    # Обновление языка по ID
    presta_language.update_language_PrestaShop(4, 'Updated Language Name')

    # Получение детальной информации о языке по ID
    language_details = presta_language.get_language_details_PrestaShop(5)
    print(language_details)
"""
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

from types import SimpleNamespace
from typing import Optional

# from .api import PrestaShop #Удален дубликат
from src import gs
# from src.utils.printer import pprint #Заменен на logger
from src.endpoints.prestashop.api import PrestaShop
# import header #Удален неиспользуемый импорт
from src.logger.logger import logger
from src.logger.exceptions import PrestaShopException

class PrestaLanguage(PrestaShop):
    """
    Класс, отвечающий за настройки языков магазина PrestaShop.

    Предоставляет методы для добавления, удаления, обновления и получения информации о языках PrestaShop.

    Args:
        credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        api_domain (Optional[str], optional): Домен API. Defaults to None.
        api_key (Optional[str], optional): Ключ API. Defaults to None.

    """
    
    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """
        Инициализация класса PrestaLanguage.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
            api_domain (Optional[str], optional): Домен API. Defaults to None.
            api_key (Optional[str], optional): Ключ API. Defaults to None.

        Raises:
            ValueError: Если не указаны `api_domain` и `api_key`.
        """
        # Проверяет, переданы ли учетные данные через словарь или SimpleNamespace
        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)
        
        # Проверяет, что оба параметра api_domain и api_key заданы
        if not api_domain or not api_key:
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
        
        super().__init__(api_domain, api_key, *args, **kwards)

    def add_language_PrestaShop(self, language_name: str, iso_code: str) -> None:
        """
        Добавляет новый язык в PrestaShop.

        Args:
            language_name (str): Название языка.
            iso_code (str): ISO-код языка.
        """
        try:
            #  Формирует данные для добавления языка
            data = {'language': {'name': language_name, 'iso_code': iso_code, 'active': 1}}
            #  Отправляет запрос на добавление языка
            response = self.add('languages', data)
            # Логирует успешное добавление языка
            logger.info(f'Язык {language_name} успешно добавлен в PrestaShop.')
        except Exception as e:
            #  Логирует ошибку при добавлении языка
            logger.error(f'Ошибка при добавлении языка {language_name} в PrestaShop: {e}')
            raise PrestaShopException(f'Ошибка при добавлении языка {language_name} в PrestaShop: {e}') from e

    def delete_language_PrestaShop(self, language_id: int) -> None:
        """
        Удаляет язык из PrestaShop по его ID.

        Args:
            language_id (int): ID языка, который нужно удалить.
        """
        try:
             #  Отправляет запрос на удаление языка
            self.delete('languages', language_id)
             # Логирует успешное удаление языка
            logger.info(f'Язык с ID {language_id} успешно удален из PrestaShop.')
        except Exception as e:
             #  Логирует ошибку при удалении языка
            logger.error(f'Ошибка при удалении языка с ID {language_id} из PrestaShop: {e}')
            raise PrestaShopException(f'Ошибка при удалении языка с ID {language_id} из PrestaShop: {e}') from e

    def update_language_PrestaShop(self, language_id: int, new_language_name: str) -> None:
        """
        Обновляет имя языка в PrestaShop по его ID.

        Args:
            language_id (int): ID языка, который нужно обновить.
            new_language_name (str): Новое имя языка.
        """
        try:
            #  Формирует данные для обновления языка
            data = {'language': {'name': new_language_name}}
            #  Отправляет запрос на обновление языка
            self.update('languages', language_id, data)
            # Логирует успешное обновление языка
            logger.info(f'Язык с ID {language_id} успешно обновлен в PrestaShop.')
        except Exception as e:
            #  Логирует ошибку при обновлении языка
            logger.error(f'Ошибка при обновлении языка с ID {language_id} в PrestaShop: {e}')
            raise PrestaShopException(f'Ошибка при обновлении языка с ID {language_id} в PrestaShop: {e}') from e

    def get_language_details_PrestaShop(self, language_id: int) -> dict:
        """
        Получает детальную информацию о языке из PrestaShop по его ID.

        Args:
            language_id (int): ID языка, информацию о котором нужно получить.

        Returns:
            dict: Детальная информация о языке.
        """
        try:
             #  Отправляет запрос на получение информации о языке
            response = self.get('languages', language_id)
            # Возвращает полученную информацию
            return response
        except Exception as e:
            #  Логирует ошибку при получении информации о языке
            logger.error(f'Ошибка при получении информации о языке с ID {language_id} из PrestaShop: {e}')
            raise PrestaShopException(f'Ошибка при получении информации о языке с ID {language_id} из PrestaShop: {e}') from e
```