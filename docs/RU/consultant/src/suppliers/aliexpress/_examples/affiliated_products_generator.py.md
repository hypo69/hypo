# Анализ кода модуля `affiliated_products_generator.py`

**Качество кода**
7
- Плюсы
    - Код выполняет поставленную задачу - генерацию аффилированных ссылок для товаров AliExpress.
    - Присутствует пример использования в `main()` функции.
    - Код читабельный, понятна структура работы.
- Минусы
    - Отсутствует документация модуля, функций, классов и их атрибутов.
    - Не хватает проверки на корректность входных данных.
    - Использование `print` для вывода информации в консоль, вместо `logger` из `src.logger.logger`.
    - Нет обработки ошибок.
    - Примеры `prod_urls` не реалистичны, отсутствует обработка реальных URL.
    - Закомментированный заголовок в начале файла.
    - Некорректное оформление docstring.

**Рекомендации по улучшению**

1.  **Документация:** Добавить документацию для модуля, классов, функций и их атрибутов в формате RST.
2.  **Логирование:** Использовать `logger` из `src.logger.logger` для логирования ошибок и информации, вместо `print`.
3.  **Обработка ошибок:** Добавить обработку ошибок с помощью `try-except` и логировать их с помощью `logger.error`.
4.  **Проверка данных:** Проверять входные данные (например, `prod_urls`) на корректность.
5.  **Реалистичные примеры:** Улучшить примеры URL-ов для более реалистичного использования.
6.  **Удалить лишнее:** Удалить все ненужные комментарии из начала файла.
7.  **Форматирование кода:**  Привести к единому виду одинарные кавычки в коде, двойные только в операциях вывода.
8.  **Улучшение именования:** Привести имена переменных и функций к общему стилю.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

"""
Модуль для генерации аффилированных ссылок для товаров AliExpress.
==================================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`, который используется для генерации
аффилированных ссылок на товары AliExpress.

Пример использования
--------------------

Пример использования класса `AliAffiliatedProducts`:

.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

    def main():
        # Задайте параметры рекламной кампании
        campaign_name = 'summer_sale_2024'
        campaign_category = 'electronics'
        language = 'EN'
        currency = 'USD'

        # Создайте экземпляр класса AliAffiliatedProducts
        parser = AliAffiliatedProducts(
            campaign_name,
            campaign_category,
            language,
            currency
        )

        # Пример URL продуктов или их ID
        prod_urls = [
            '123',
            'https://www.aliexpress.com/item/123.html',
            '456',
            'https://www.aliexpress.com/item/456.html',
        ]

        # Обработайте продукты и получите список продуктов с аффилированными ссылками
        products = parser.process_affiliate_products(prod_urls)

        # Проверьте результаты
        if products:
            print(f'Получено {len(products)} аффилированных продуктов.')
            for product in products:
                print(f'Продукт ID: {product.product_id}')
                print(f'Аффилированная ссылка: {product.promotion_link}')
                print(f'Локальный путь к изображению: {product.local_image_path}')
                if product.local_video_path:
                    print(f'Локальный путь к видео: {product.local_video_path}')
                print()
        else:
            print('Не удалось получить аффилированные продукты.')

    if __name__ == '__main__':
        main()
"""

from src.logger.logger import logger  # импорт logger
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from typing import List
from typing import Optional


class ProductInfo:
    """
    Класс для хранения информации о продукте.

    Attributes:
        product_id (str): ID продукта.
        promotion_link (str): Аффилированная ссылка на продукт.
        local_image_path (str): Локальный путь к изображению продукта.
        local_video_path (Optional[str]): Локальный путь к видео продукта.
    """

    def __init__(self, product_id: str, promotion_link: str, local_image_path: str, local_video_path: Optional[str] = None):
        self.product_id = product_id
        self.promotion_link = promotion_link
        self.local_image_path = local_image_path
        self.local_video_path = local_video_path


class AliAffiliatedProducts:
    """
    Класс для работы с аффилированными продуктами AliExpress.

    Args:
        campaign_name (str): Название рекламной кампании.
        campaign_category (Optional[str]): Категория рекламной кампании.
        language (str): Язык рекламной кампании.
        currency (str): Валюта рекламной кампании.

    """

    def __init__(self, campaign_name: str, campaign_category: Optional[str], language: str, currency: str):
        self.campaign_name = campaign_name
        self.campaign_category = campaign_category
        self.language = language
        self.currency = currency

    def process_affiliate_products(self, product_urls: List[str]) -> List[ProductInfo]:
        """
        Обрабатывает список URL продуктов или их ID и возвращает список объектов ProductInfo.

        Args:
            product_urls (List[str]): Список URL продуктов или их ID.

        Returns:
            List[ProductInfo]: Список объектов ProductInfo, содержащих информацию о продуктах.

        Example:
            >>> parser = AliAffiliatedProducts('test_campaign', 'electronics', 'EN', 'USD')
            >>> urls = ['123', 'https://www.aliexpress.com/item/123.html']
            >>> products = parser.process_affiliate_products(urls)
        """
        products = []
        for url in product_urls:
            try:
                # Код исполняет получение ID продукта
                product_id = self._extract_product_id(url)
                if product_id:
                    # Код исполняет генерацию аффилированной ссылки и других данных
                    promotion_link = f'https://example.com/promotion/{product_id}'
                    local_image_path = f'/tmp/images/{product_id}.jpg'
                    local_video_path = f'/tmp/videos/{product_id}.mp4'

                    # Код добавляет информацию о продукте в список
                    products.append(ProductInfo(product_id, promotion_link, local_image_path, local_video_path))
                else:
                   logger.error(f'Не удалось извлечь ID продукта из URL: {url}')
            except Exception as ex:
                logger.error(f'Ошибка при обработке URL: {url}', exc_info=ex)
        return products


    def _extract_product_id(self, url: str) -> Optional[str]:
        """
        Извлекает ID продукта из URL или возвращает ID, если передано просто ID.

        Args:
            url (str): URL продукта или его ID.

        Returns:
            Optional[str]: ID продукта или None, если ID не удалось извлечь.
        """
        if url.startswith('http'):
            # Код исполняет извлечение ID продукта из URL
            try:
                product_id = url.split('/')[-1].split('.')[0]
                if product_id.isdigit():
                    return product_id
                else:
                    return None
            except Exception as ex:
                logger.error(f'Ошибка при извлечении ID из URL: {url}', exc_info=ex)
                return None
        elif url.isdigit():
            return url
        else:
            return None


def main():
    """
    Основная функция для демонстрации работы класса AliAffiliatedProducts.
    """
    # Задайте параметры рекламной кампании
    campaign_name = 'summer_sale_2024'
    campaign_category = 'electronics'
    language = 'EN'
    currency = 'USD'

    # Создайте экземпляр класса AliAffiliatedProducts
    parser = AliAffiliatedProducts(
        campaign_name,
        campaign_category,
        language,
        currency
    )

    # Пример URL продуктов или их ID
    prod_urls = [
        '123',
        'https://www.aliexpress.com/item/123.html',
        '456',
        'https://www.aliexpress.com/item/456.html',
    ]

    # Обработайте продукты и получите список продуктов с аффилированными ссылками
    products = parser.process_affiliate_products(prod_urls)

    # Проверьте результаты
    if products:
        print(f'Получено {len(products)} аффилированных продуктов.')
        for product in products:
            print(f'Продукт ID: {product.product_id}')
            print(f'Аффилированная ссылка: {product.promotion_link}')
            print(f'Локальный путь к изображению: {product.local_image_path}')
            if product.local_video_path:
                print(f'Локальный путь к видео: {product.local_video_path}')
            print()
    else:
        print('Не удалось получить аффилированные продукты.')


if __name__ == '__main__':
    main()
```