## \file /src/goog/google_search.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.goog 
	:platform: Windows, Unix
	:synopsis:

"""



from lxml import html


class GoogleHtmlParser:
    """Класс для парсинга HTML с Google Search.

    Парсит HTML страницы поисковой выдачи Google и преобразует её в словарь.
    Работает как с мобильной, так и с десктопной версией HTML.

    Атрибуты:
        tree (html.Element): Дерево документа, полученное через html.fromstring().
        user_agent (str): User agent, использованный для получения HTML Google Search.
    """

    def __init__(self, html_str: str, user_agent: str = 'desktop') -> None:
        """Инициализация парсера.

        Создает дерево документа из строки HTML.

        Args:
            html_str (str): HTML Google Search в виде строки.
            user_agent (str): User agent для получения HTML. Может быть 'mobile' или 'desktop'.

        Returns:
            None
        """
        self.tree = html.fromstring(html_str)
        if user_agent in ['mobile', 'desktop']:
            self.user_agent = user_agent
        else:
            self.user_agent = 'desktop'

    def _clean(self, content: str) -> str:
        """Очистка строки от лишних символов.

        Очищает строку от пробелов и лишних символов.

        Args:
            content (str): Строка для очистки.

        Returns:
            str: Очищенная строка.
        """
        if content:
            content = content.strip()
            content = ' '.join(content.split())
            return content
        return ''

    def _normalize_dict_key(self, content: str) -> str:
        """Нормализация строки для использования в качестве ключа словаря.

        Заменяет пробелы на подчеркивания, убирает двоеточия, приводит к нижнему регистру.

        Args:
            content (str): Строка для нормализации.

        Returns:
            str: Нормализованная строка.
        """
        content = str(content).replace(' ', '_').replace(':', '').lower().strip('_')
        return content

    def _get_estimated_results(self) -> int:
        """Получение количества результатов поиска.

        Возвращает количество найденных результатов для десктопной версии Google Search.

        Returns:
            int: Число результатов поиска.
        """
        estimated_results = 0
        estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()')
        if len(estimated_el) > 0:
            estimated_results = int(estimated_el[0].split()[1].replace(',', ''))
        return estimated_results

    def _get_organic(self) -> list:
        """Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        Returns:
            list: Список словарей с органическими результатами.
        """
        organic = []
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

            res = {
                'url': self._clean(g.xpath('.//@href[1]')[0]),
                'title': self._clean(g.xpath('.//h3/text()')[0]),
                'snippet': self._clean(snippet),
                'rich_snippet': self._clean(rich_snippet),
            }
            organic.append(res)
        return organic

    def _get_featured_snippet(self) -> dict | None:
        """Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        Returns:
            dict | None: Словарь с заголовком и URL или None.
        """
        fs = None
        snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]')
        if snippet_el:
            snippet_el = snippet_el[0]
            heading = snippet_el.xpath('.//h3/text()')
            url = snippet_el.xpath('.//a/@href')
            if heading and url:
                fs = {'title': heading[0], 'url': url[-1]}
        return fs

    def _get_knowledge_card(self) -> dict | None:
        """Получение карточки знаний.

        Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

        Returns:
            dict | None: Словарь с данными карточки знаний или None.
        """
        kc_el = self.tree.xpath('//div[contains(@class, "kp-wholepage")]')
        if kc_el:
            kc_el = kc_el[0]
            more_info = []
            for el in kc_el.xpath('.//div[contains(@data-attrid, ":/")]'):
                el_parts = el.xpath('.//span')
                if len(el_parts) == 2:
                    more_info.append({self._normalize_dict_key(el_parts[0].text_content()): el_parts[1].text_content()})
            return {
                'title': kc_el.xpath('.//h2/span')[0].text_content(),
                'subtitle': kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]')[0].text_content(),
                'description': kc_el.xpath('.//div[@class="kno-rdesc"]/span')[0].text_content(),
                'more_info': more_info
            }
        return None

    def _get_scrolling_sections(self) -> list:
        """Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        Returns:
            list: Список словарей с данными из виджетов.
        """
        sections = self.tree.xpath('//g-section-with-header')
        data = []
        for section in sections:
            title = section.xpath('.//h3')[0].text_content()
            section_data = []
            for data_section in section.xpath('.//g-inner-card'):
                data_title = data_section.xpath('.//div[@role="heading"]/text()')[0]
                data_url = data_section.xpath('.//a/@href')[0]
                section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)})
            data.append({'section_title': title, 'section_data': section_data})
        return data

    def get_data(self) -> dict:
        """Получение итоговых данных с поисковой страницы.

        Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

        Returns:
            dict: Словарь с данными поисковой страницы.
        """
        data = {}
        if self.user_agent == 'desktop':
            data = {
                'estimated_results': self._get_estimated_results(),
                'featured_snippet': self._get_featured_snippet(),
                'knowledge_card': self._get_knowledge_card(),
                'organic_results': self._get_organic(),
                'scrolling_widgets': self._get_scrolling_sections()
            }
        return data
