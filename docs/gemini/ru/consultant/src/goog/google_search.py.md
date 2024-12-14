# Анализ кода модуля `google_search`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, разбит на методы, каждый из которых выполняет определенную задачу.
    - Используется `lxml` для парсинга HTML, что является хорошей практикой.
    - Есть docstring для классов и методов, что облегчает понимание кода.
    - Код обрабатывает как мобильную, так и десктопную версии Google Search.
    - Присутствует логика для очистки и нормализации данных.

- Минусы
    - Отсутствует импорт `from src.logger.logger import logger` для логирования ошибок.
    - Используются `if/else` конструкции для проверок, которые можно заменить более лаконичными выражениями.
    - Нет обработки исключений в методах, где это может быть полезно.
    - Не везде используется `self._clean` для очистки данных, что может привести к несогласованности в данных.
    - Нет четкой обработки случаев, когда элементы не найдены в HTML (например, `[0]` после `xpath`).

**Рекомендации по улучшению**

1.  **Добавить логирование ошибок:**
    -   Использовать `from src.logger.logger import logger` для логирования возможных ошибок в методах парсинга.
    -   Заменить `try-except` на логирование ошибок через `logger.error` для более контролируемого процесса.

2.  **Улучшить обработку `xpath`:**
    -   Проверять, что `xpath` возвращает не пустой список, перед тем как обращаться к его элементам по индексу.
    -   Использовать `xpath(...).get()` вместо `xpath(...)[0]`, для обработки случаев, когда элемент не найден.

3.  **Улучшить читаемость и лаконичность кода:**
    -   Использовать более лаконичные выражения, где это возможно (например, тернарный оператор вместо if/else).
    -   По возможности, избегать вложенных `if/else` конструкций.

4.  **Документация:**
    -   Переписать docstring в формате reStructuredText (RST).
    -   Добавить примеры использования класса.

5. **Обработка исключений**
    - Добавить обработку исключений в методах, где это необходимо для избежания ошибок.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для парсинга HTML страниц Google Search
====================================================

Этот модуль содержит класс :class:`GoogleHtmlParser`, который используется для парсинга HTML страниц
поисковой выдачи Google и преобразования ее в словарь. Работает как с мобильной, так и с десктопной версией HTML.

Пример использования
--------------------

Пример использования класса `GoogleHtmlParser`:

.. code-block:: python

    html_str = "<html>...</html>" # HTML Google Search
    parser = GoogleHtmlParser(html_str, user_agent='desktop')
    data = parser.get_data()
"""

MODE = 'dev'

from lxml import html
from src.logger.logger import logger  #  Импорт логгера


class GoogleHtmlParser:
    """
    Класс для парсинга HTML с Google Search.

    Парсит HTML страницы поисковой выдачи Google и преобразует её в словарь.
    Работает как с мобильной, так и с десктопной версией HTML.

    :param html_str: HTML Google Search в виде строки.
    :param user_agent: User agent для получения HTML. Может быть 'mobile' или 'desktop'.
    :ivar tree: Дерево документа, полученное через html.fromstring().
    :ivar user_agent: User agent, использованный для получения HTML Google Search.
    """

    def __init__(self, html_str: str, user_agent: str = 'desktop') -> None:
        """
        Инициализация парсера.

        Создает дерево документа из строки HTML.

        :param html_str: HTML Google Search в виде строки.
        :param user_agent: User agent для получения HTML. Может быть 'mobile' или 'desktop'.
        """
        self.tree = html.fromstring(html_str)
        self.user_agent = user_agent if user_agent in ['mobile', 'desktop'] else 'desktop'
        #  Устанавливаем user_agent в зависимости от переданного значения или по умолчанию 'desktop'

    def _clean(self, content: str) -> str:
        """
        Очистка строки от лишних символов.

        Очищает строку от пробелов и лишних символов.

        :param content: Строка для очистки.
        :return: Очищенная строка.
        """
        if not content:
            return ''
        content = content.strip()
        content = ' '.join(content.split())
        return content
        #  Если строка не пуста, удаляем лишние пробелы и возвращаем очищенную строку

    def _normalize_dict_key(self, content: str) -> str:
        """
        Нормализация строки для использования в качестве ключа словаря.

        Заменяет пробелы на подчеркивания, убирает двоеточия, приводит к нижнему регистру.

        :param content: Строка для нормализации.
        :return: Нормализованная строка.
        """
        return str(content).replace(' ', '_').replace(':', '').lower().strip('_')
        #  Нормализуем строку для использования в качестве ключа словаря

    def _get_estimated_results(self) -> int:
        """
        Получение количества результатов поиска.

        Возвращает количество найденных результатов для десктопной версии Google Search.

        :return: Число результатов поиска.
        """
        try:
            estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()')
            #  Выполняем xpath запрос для получения элементов с количеством результатов
            if estimated_el:
                #  Проверяем, что список не пустой
                return int(estimated_el[0].split()[1].replace(',', ''))
                #  Извлекаем и форматируем количество результатов
            return 0
            #  Возвращаем 0, если не удалось найти количество результатов
        except Exception as ex:
            logger.error('Ошибка получения количества результатов поиска', ex)
            #  Логируем ошибку
            return 0
        #  Возвращаем 0 в случае ошибки

    def _get_organic(self) -> list:
        """
        Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        :return: Список словарей с органическими результатами.
        """
        organic = []
        for g in self.tree.xpath('//div[@class="g"]'):
            #  Проходимся по всем элементам органических результатов
            snippets = g.xpath('.//div/div/div[2]/div')
            #  Выполняем xpath запрос для получения сниппетов
            snippet, rich_snippet = None, None
            if len(snippets) == 1:
                 snippet = snippets[0].text_content()
                 #  Извлекаем текст сниппета, если он один
            elif len(snippets) > 1:
                #  Проверяем, что список сниппетов больше одного
                if snippets[1].xpath('.//g-review-stars'):
                    rich_snippet = snippets[1].text_content()
                    snippet = snippets[0].text_content()
                    #  Извлекаем текст rich сниппета и сниппета
                else:
                    snippet = snippets[1].text_content()
                    rich_snippet = snippets[0].text_content()
                     #  Извлекаем текст сниппета и rich сниппета
            res = {
                'url': self._clean(g.xpath('.//@href[1]')[0] if g.xpath('.//@href[1]') else ''),
                'title': self._clean(g.xpath('.//h3/text()')[0] if g.xpath('.//h3/text()') else ''),
                'snippet': self._clean(snippet) if snippet else '',
                'rich_snippet': self._clean(rich_snippet) if rich_snippet else '',
            }
            #  Собираем данные и очищаем их
            organic.append(res)
            #  Добавляем результат в список
        return organic
        #  Возвращаем список органических результатов

    def _get_featured_snippet(self) -> dict | None:
        """
        Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        :return: Словарь с заголовком и URL или None.
        """
        try:
            snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]')
            #  Выполняем xpath запрос для получения featured snippet
            if not snippet_el:
                 return None
                 #  Если featured snippet не найден, возвращаем None
            snippet_el = snippet_el[0]
            heading = snippet_el.xpath('.//h3/text()')
            url = snippet_el.xpath('.//a/@href')
            #  Выполняем xpath запрос для получения заголовка и URL
            if heading and url:
                 #  Проверяем, что заголовок и URL существуют
                 return {'title': heading[0], 'url': url[-1]}
                 #  Возвращаем словарь с заголовком и URL
            return None
        except Exception as ex:
            logger.error('Ошибка получения featured snippet', ex)
            #  Логируем ошибку
            return None
         #  Возвращаем None в случае ошибки

    def _get_knowledge_card(self) -> dict | None:
        """
        Получение карточки знаний.

        Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

        :return: Словарь с данными карточки знаний или None.
        """
        try:
            kc_el = self.tree.xpath('//div[contains(@class, "kp-wholepage")]')
             #  Выполняем xpath запрос для получения карточки знаний
            if not kc_el:
                return None
                #  Если карточка знаний не найдена, возвращаем None
            kc_el = kc_el[0]
            more_info = []
            for el in kc_el.xpath('.//div[contains(@data-attrid, ":/")]'):
                #  Проходимся по всем элементам с дополнительной информацией
                el_parts = el.xpath('.//span')
                if len(el_parts) == 2:
                    more_info.append({self._normalize_dict_key(el_parts[0].text_content()): el_parts[1].text_content()})
                    #  Собираем дополнительную информацию
            return {
                'title': kc_el.xpath('.//h2/span')[0].text_content() if kc_el.xpath('.//h2/span') else '',
                'subtitle': kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]')[0].text_content() if kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]') else '',
                'description': kc_el.xpath('.//div[@class="kno-rdesc"]/span')[0].text_content() if kc_el.xpath('.//div[@class="kno-rdesc"]/span') else '',
                'more_info': more_info
            }
            #  Возвращаем данные карточки знаний
        except Exception as ex:
            logger.error('Ошибка получения карточки знаний', ex)
            #  Логируем ошибку
            return None
        #  Возвращаем None в случае ошибки

    def _get_scrolling_sections(self) -> list:
        """
        Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        :return: Список словарей с данными из виджетов.
        """
        data = []
        for section in self.tree.xpath('//g-section-with-header'):
             #  Проходимся по всем скроллируемым секциям
            title = section.xpath('.//h3')[0].text_content() if section.xpath('.//h3') else ''
             #  Извлекаем заголовок секции
            section_data = []
            for data_section in section.xpath('.//g-inner-card'):
                 #  Проходимся по всем элементам данных в секции
                data_title = data_section.xpath('.//div[@role="heading"]/text()')[0] if data_section.xpath('.//div[@role="heading"]/text()') else ''
                data_url = data_section.xpath('.//a/@href')[0] if data_section.xpath('.//a/@href') else ''
                #  Извлекаем заголовок и URL элемента данных
                section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)})
                #  Добавляем данные в список
            data.append({'section_title': title, 'section_data': section_data})
            #  Добавляем секцию в список
        return data
        #  Возвращаем список данных из виджетов

    def get_data(self) -> dict:
        """
        Получение итоговых данных с поисковой страницы.

        Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

        :return: Словарь с данными поисковой страницы.
        """
        if self.user_agent == 'desktop':
            return {
                'estimated_results': self._get_estimated_results(),
                'featured_snippet': self._get_featured_snippet(),
                'knowledge_card': self._get_knowledge_card(),
                'organic_results': self._get_organic(),
                'scrolling_widgets': self._get_scrolling_sections()
            }
            #  Возвращаем словарь с данными для десктопной версии
        return {}
        #  Возвращаем пустой словарь, если user_agent не desktop
```