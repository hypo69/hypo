# Анализ кода модуля `google_search`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на методы, каждый из которых выполняет свою задачу.
    - Используются информативные docstring для классов и методов, что облегчает понимание кода.
    - Код корректно обрабатывает различные структуры HTML, как для мобильной, так и для десктопной версии Google Search.
    - Присутствует логика для очистки и нормализации данных, полученных из HTML.
    - Код использует `lxml` для парсинга HTML, что является хорошей практикой.
-  Минусы
    -  Отсутствуют некоторые необходимые импорты.
    -  Не используются логирование ошибок.
    -  В некоторых местах логика извлечения данных из HTML может быть упрощена или сделана более надежной.
    -  Некоторые блоки `if-else` можно переписать с использованием более выразительных конструкций.
    -  Отсутствует обработка крайних случаев, например, когда элементы HTML не найдены.

**Рекомендации по улучшению**

1. **Добавить импорты:** Добавить необходимые импорты из `src.logger.logger`.
2. **Использовать логирование:** Заменить блоки try-except на логирование ошибок с помощью `logger.error`.
3. **Улучшить извлечение данных:** Пересмотреть xpath запросы для извлечения данных, чтобы они были более надежными.
4. **Улучшить обработку `if-else`:** Переписать некоторые блоки `if-else` с использованием более лаконичных конструкций.
5. **Добавить обработку крайних случаев:** Обработать случаи, когда элементы HTML не найдены, чтобы избежать ошибок.
6. **Добавить комментарии в стиле RST:** Добавить документацию в стиле RST ко всем функциям, методам и классам.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для парсинга HTML страниц поисковой выдачи Google.
=========================================================

Этот модуль содержит класс :class:`GoogleHtmlParser`, который используется для парсинга HTML-страниц поисковой выдачи Google.
Класс поддерживает парсинг как десктопной, так и мобильной версий HTML.

Пример использования
--------------------

Пример создания экземпляра класса `GoogleHtmlParser` и получения данных:

.. code-block:: python

    html_content = '<html>...</html>'
    parser = GoogleHtmlParser(html_content, user_agent='desktop')
    data = parser.get_data()
"""

from lxml import html
from typing import List, Dict, Optional
from src.logger.logger import logger # импорт модуля логгера

MODE = 'dev'


class GoogleHtmlParser:
    """
    Класс для парсинга HTML с Google Search.

    Парсит HTML страницы поисковой выдачи Google и преобразует её в словарь.
    Работает как с мобильной, так и с десктопной версией HTML.

    :param html_str: HTML Google Search в виде строки.
    :param user_agent: User agent для получения HTML. Может быть 'mobile' или 'desktop'.
    :type html_str: str
    :type user_agent: str
    :ivar tree: Дерево документа, полученное через html.fromstring().
    :vartype tree: lxml.html.HtmlElement
    :ivar user_agent: User agent, использованный для получения HTML Google Search.
    :vartype user_agent: str
    """
    def __init__(self, html_str: str, user_agent: str = 'desktop') -> None:
        """
        Инициализация парсера.

        Создает дерево документа из строки HTML.

        :param html_str: HTML Google Search в виде строки.
        :param user_agent: User agent для получения HTML. Может быть 'mobile' или 'desktop'.
        :type html_str: str
        :type user_agent: str
        """
        try:
            # Код создает дерево документа из HTML строки
            self.tree = html.fromstring(html_str)
            # Код проверяет user_agent и устанавливает значение
            if user_agent in ['mobile', 'desktop']:
                self.user_agent = user_agent
            else:
                self.user_agent = 'desktop'
        except Exception as e:
            logger.error(f'Ошибка при инициализации парсера: {e}')
            self.tree = None
            self.user_agent = 'desktop'

    def _clean(self, content: str) -> str:
        """
        Очистка строки от лишних символов.

        Очищает строку от пробелов и лишних символов.

        :param content: Строка для очистки.
        :type content: str
        :return: Очищенная строка.
        :rtype: str
        """
        if content:
            # Код удаляет лишние пробелы и возвращает строку
            content = content.strip()
            content = ' '.join(content.split())
            return content
        return ''

    def _normalize_dict_key(self, content: str) -> str:
        """
        Нормализация строки для использования в качестве ключа словаря.

        Заменяет пробелы на подчеркивания, убирает двоеточия, приводит к нижнему регистру.

        :param content: Строка для нормализации.
        :type content: str
        :return: Нормализованная строка.
        :rtype: str
        """
        # Код нормализует строку для использования в качестве ключа словаря
        content = str(content).replace(' ', '_').replace(':', '').lower().strip('_')
        return content

    def _get_estimated_results(self) -> int:
        """
        Получение количества результатов поиска.

        Возвращает количество найденных результатов для десктопной версии Google Search.

        :return: Число результатов поиска.
        :rtype: int
        """
        estimated_results = 0
        # Код извлекает текст элемента с id="result-stats"
        estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()')
        if estimated_el:
            try:
                 # Код извлекает количество результатов из текста
                 estimated_results = int(estimated_el[0].split()[1].replace(',', ''))
            except (IndexError, ValueError) as e:
                 logger.error(f'Ошибка при извлечении количества результатов: {e}')
                 return 0
        return estimated_results

    def _get_organic(self) -> List[Dict[str, Optional[str]]]:
        """
        Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        :return: Список словарей с органическими результатами.
        :rtype: list
        """
        organic = []
        # Код итерируется по каждому элементу с классом 'g'
        for g in self.tree.xpath('//div[@class="g"]'):
            snippets = g.xpath('.//div/div/div[2]/div')
            snippet, rich_snippet = None, None
            if len(snippets) == 1:
                snippet = snippets[0].text_content()
            elif len(snippets) > 1:
                if snippets[1].xpath('.//g-review-stars'):
                    rich_snippet = snippets[1].text_content()
                    snippet = snippets[0].text_content()
                else:
                    snippet = snippets[1].text_content()
                    rich_snippet = snippets[0].text_content()
            try:
                # Код формирует словарь с данными органического результата
                res = {
                    'url': self._clean(g.xpath('.//@href[1]')[0]) if g.xpath('.//@href[1]') else None, # добавлена проверка на наличие элемента
                    'title': self._clean(g.xpath('.//h3/text()')[0]) if g.xpath('.//h3/text()') else None,  # добавлена проверка на наличие элемента
                    'snippet': self._clean(snippet),
                    'rich_snippet': self._clean(rich_snippet),
                }
            except IndexError as e:
                logger.error(f'Ошибка при извлечении органических результатов: {e}')
                continue
            organic.append(res)
        return organic

    def _get_featured_snippet(self) -> Optional[Dict[str, str]]:
        """
        Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        :return: Словарь с заголовком и URL или None.
        :rtype: dict | None
        """
        fs = None
        # Код ищет элемент с классом, содержащим "kp-blk"
        snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]')
        if snippet_el:
            snippet_el = snippet_el[0]
            # Код извлекает заголовок и URL featured snippet
            heading = snippet_el.xpath('.//h3/text()')
            url = snippet_el.xpath('.//a/@href')
            if heading and url:
                fs = {'title': heading[0], 'url': url[-1]}
        return fs

    def _get_knowledge_card(self) -> Optional[Dict[str, any]]:
        """
        Получение карточки знаний.

        Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

        :return: Словарь с данными карточки знаний или None.
        :rtype: dict | None
        """
        kc_el = self.tree.xpath('//div[contains(@class, "kp-wholepage")]')
        if kc_el:
            kc_el = kc_el[0]
            more_info = []
            # Код извлекает данные из элементов с атрибутом data-attrid, содержащим ":/"
            for el in kc_el.xpath('.//div[contains(@data-attrid, ":/")]'):
                el_parts = el.xpath('.//span')
                if len(el_parts) == 2:
                    more_info.append({self._normalize_dict_key(el_parts[0].text_content()): el_parts[1].text_content()})
            try:
                # Код формирует словарь с данными карточки знаний
                return {
                    'title': kc_el.xpath('.//h2/span')[0].text_content() if kc_el.xpath('.//h2/span') else None,  # добавлена проверка на наличие элемента
                    'subtitle': kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]')[0].text_content() if kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]') else None,  # добавлена проверка на наличие элемента
                    'description': kc_el.xpath('.//div[@class="kno-rdesc"]/span')[0].text_content() if kc_el.xpath('.//div[@class="kno-rdesc"]/span') else None,  # добавлена проверка на наличие элемента
                    'more_info': more_info
                }
            except IndexError as e:
               logger.error(f'Ошибка при извлечении данных карточки знаний: {e}')
               return None
        return None

    def _get_scrolling_sections(self) -> List[Dict[str, any]]:
        """
        Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        :return: Список словарей с данными из виджетов.
        :rtype: list
        """
        sections = self.tree.xpath('//g-section-with-header')
        data = []
        # Код итерируется по всем секциям
        for section in sections:
            try:
                # Код извлекает заголовок секции
                title = section.xpath('.//h3')[0].text_content()
            except IndexError:
                logger.error(f'Ошибка при извлечении заголовка секции')
                continue
            section_data = []
            # Код итерируется по данным в секции
            for data_section in section.xpath('.//g-inner-card'):
                try:
                    # Код извлекает заголовок и URL элемента секции
                    data_title = data_section.xpath('.//div[@role="heading"]/text()')[0]
                    data_url = data_section.xpath('.//a/@href')[0]
                    section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)})
                except IndexError:
                    logger.error(f'Ошибка при извлечении данных из секции')
                    continue
            data.append({'section_title': title, 'section_data': section_data})
        return data

    def get_data(self) -> Dict[str, any]:
        """
        Получение итоговых данных с поисковой страницы.

        Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

        :return: Словарь с данными поисковой страницы.
        :rtype: dict
        """
        data = {}
        # Код проверяет user_agent и собирает данные
        if self.user_agent == 'desktop':
            data = {
                'estimated_results': self._get_estimated_results(),
                'featured_snippet': self._get_featured_snippet(),
                'knowledge_card': self._get_knowledge_card(),
                'organic_results': self._get_organic(),
                'scrolling_widgets': self._get_scrolling_sections()
            }
        return data
```