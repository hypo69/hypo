# Анализ кода модуля `category.py`

**Качество кода**
7
-  Плюсы
    - Код хорошо структурирован и разделен на синхронную и асинхронную версии класса.
    - Используется `logger` для логирования ошибок.
    - Присутствует базовая документация к классам и методам.
-  Минусы
    - Не все функции и методы имеют подробную документацию в формате RST.
    - Отсутствуют doctests.
    - В асинхронном коде `category['categories'][0]['id_parent']` обращение по индексу без проверки наличия элементов.
    -  Использование `super()` в синхронном коде  `category = super().get`
    -  Использование `super()` в асинхронном коде `category = await super().read`

**Рекомендации по улучшению**

1.  **Документация:**
    *   Добавить подробное описание модуля в начале файла.
    *   Расширить документацию для всех функций и методов в формате RST.
    *   Добавить doctests для примеров использования.
2.  **Обработка ошибок:**
    *   В асинхронном методе `get_parent_categories_list` добавить проверку перед обращением по индексу `category['categories'][0]`, чтобы избежать ошибок `IndexError`.
3.  **Использование `super()`:**
    *  Использовать `self` вместо `super()` в синхронном классе `PrestaCategory` в методе `get_parent_categories_list` для вызова методов `get`.
    *  Использовать `self` вместо `super()` в асинхронном классе `PrestaCategoryAsync` в методе `get_parent_categories_list` для вызова методов `read`.
4.  **Форматирование**:
    *   Исправить форматирование в соответствии с `PEP8`.
    *   Убрать комментарии после `#` в строках где код не должен меняться.
5. **Импорты**
    - Добавить импорт `Path` из `pathlib`
    - Добавить `from src.logger.logger import logger`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с категориями в PrestaShop.
=========================================================================================

Этот модуль содержит классы :class:`PrestaCategory` и :class:`PrestaCategoryAsync`,
которые используются для управления категориями в PrestaShop.

Пример использования
--------------------

Пример использования класса `PrestaCategory`:

.. code-block:: python

    from src.endpoints.prestashop.category import PrestaCategory
    
    credentials = {
        'api_domain': 'your_api_domain',
        'api_key': 'your_api_key'
    }
    category_manager = PrestaCategory(credentials=credentials)
    parent_categories = category_manager.get_parent_categories_list(id_category=3)
    print(parent_categories)

Пример использования класса `PrestaCategoryAsync`:

.. code-block:: python

    import asyncio
    from src.endpoints.prestashop.category import PrestaCategoryAsync
    
    async def main():
        credentials = {
            'api_domain': 'your_api_domain',
            'api_key': 'your_api_key'
        }
        async_category_manager = PrestaCategoryAsync(credentials=credentials)
        parent_categories = await async_category_manager.get_parent_categories_list(id_category=3)
        print(parent_categories)

    if __name__ == "__main__":
        asyncio.run(main())
"""
from typing import List, Dict, Optional, Union
from types import SimpleNamespace
import asyncio
from pathlib import Path
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_dumps #  импорт не используется
from src.endpoints.prestashop.api import PrestaShop, PrestaShopAsync


class PrestaCategory(PrestaShop):
    """
    Класс для управления категориями в PrestaShop.

    Args:
        credentials (Optional[Union[dict, SimpleNamespace]]): Словарь или SimpleNamespace с учетными данными API.
        api_domain (Optional[str]): Домен API PrestaShop.
        api_key (Optional[str]): Ключ API PrestaShop.

    Raises:
        ValueError: Если не предоставлены `api_domain` или `api_key`.
    """

    def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
        """
        Инициализация экземпляра класса PrestaCategory.
        
        Args:
            credentials (Optional[Union[dict, SimpleNamespace]]): Словарь или SimpleNamespace с учетными данными API.
            api_domain (Optional[str]): Домен API PrestaShop.
            api_key (Optional[str]): Ключ API PrestaShop.
            
        Raises:
            ValueError: Если не предоставлены `api_domain` или `api_key`.
        """
        if credentials:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        if not api_domain or not api_key:
            raise ValueError('Both api_domain and api_key parameters are required.')

        super().__init__(api_domain, api_key)

    def get_parent_categories_list(self, id_category: Union[str, int], parent_categories_list: List[int] = []) -> List[int]:
        """
        Получает список родительских категорий для заданной категории.

        Args:
            id_category (Union[str, int]): Идентификатор категории.
            parent_categories_list (List[int]): Список родительских категорий (используется для рекурсии).

        Returns:
            List[int]: Список идентификаторов родительских категорий.
        """
        if not id_category:
            logger.error("Missing category ID.")
            return parent_categories_list

        category = self.get('categories', resource_id=id_category, display='full', io_format='JSON')
        if not category:
            logger.error("Issue with retrieving categories.")
            return
        
        _parent_category = int(category['id_parent'])
        parent_categories_list.append(_parent_category)

        if _parent_category <= 2:
            return parent_categories_list
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)


class PrestaCategoryAsync(PrestaShopAsync):
    """
    Асинхронный класс для управления категориями в PrestaShop.

    Args:
        credentials (Optional[Union[dict, SimpleNamespace]]): Словарь или SimpleNamespace с учетными данными API.
        api_domain (Optional[str]): Домен API PrestaShop.
        api_key (Optional[str]): Ключ API PrestaShop.

    Raises:
        ValueError: Если не предоставлены `api_domain` или `api_key`.
    """
    def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
        """
        Инициализация асинхронного экземпляра класса PrestaCategoryAsync.
        
        Args:
            credentials (Optional[Union[dict, SimpleNamespace]]): Словарь или SimpleNamespace с учетными данными API.
            api_domain (Optional[str]): Домен API PrestaShop.
            api_key (Optional[str]): Ключ API PrestaShop.
        
        Raises:
            ValueError: Если не предоставлены `api_domain` или `api_key`.
        """
        if credentials:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        if not api_domain or not api_key:
            raise ValueError('Both api_domain and api_key parameters are required.')

        super().__init__(api_domain, api_key)

    async def get_parent_categories_list(self, id_category: Union[str, int], parent_categories_list: List[int] = []) -> List[int]:
        """
        Асинхронно получает список родительских категорий для заданной категории.

        Args:
            id_category (Union[str, int]): Идентификатор категории.
            parent_categories_list (List[int]): Список родительских категорий (используется для рекурсии).

        Returns:
            List[int]: Список идентификаторов родительских категорий.
        """
        if not id_category:
            logger.error("Missing category ID.")
            return parent_categories_list
        
        category = await self.read('categories', resource_id=id_category, display='full', io_format='JSON')
        if not category:
            logger.error("Issue with retrieving categories.")
            return
        
        if not category.get('categories'):
             logger.error(f"Invalid category data structure: {category}")
             return parent_categories_list
        
        _parent_category = int(category['categories'][0]['id_parent'])
        parent_categories_list.append(_parent_category)

        if _parent_category <= 2: # корневая директория
            return parent_categories_list
        else:
            return await self.get_parent_categories_list(_parent_category, parent_categories_list)
```