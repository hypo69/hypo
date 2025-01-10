# Анализ кода модуля `google_search`

**Качество кода**

9

-   **Плюсы**
    -   Код хорошо структурирован и разбит на логические функции, что облегчает понимание и поддержку.
    -   Присутствует подробная документация для класса и методов, что соответствует требованиям.
    -   Используется `lxml` для парсинга, что является хорошим выбором для работы с HTML.
    -   Функции очистки и нормализации данных (`_clean`, `_normalize_dict_key`) способствуют консистентности данных.
    -   Код обрабатывает как десктопную, так и мобильную версии HTML.
    -   Присутствуют проверки на наличие данных перед их извлечением.
-   **Минусы**
    -   Отсутствует обработка ошибок.
    -   Не используется `logger` для логирования ошибок.
    -   Используется `len(estimated_el) > 0` вместо более читаемого `if estimated_el:`.
    -   Не все возвращаемые значения проверены на `None`.
    -   Некоторые XPath-запросы могут быть упрощены.
    -   Не используется f-строки.

**Рекомендации по улучшению**

1.  **Добавить логирование ошибок**:
    -   Использовать `logger.error` для записи ошибок, возникающих при парсинге HTML.
    -   Включить информацию об исключениях, чтобы облегчить отладку.
2.  **Обработка ошибок**:
    -   Добавить обработку исключений в ключевых местах, где это может потребоваться, например, при выполнении запросов XPath.
3.  **Улучшение читаемости**:
    -   Использовать `if estimated_el:` вместо `if len(estimated_el) > 0`.
    -   Использовать f-строки для форматирования строк.
    -   Использовать более читаемые наименования переменных.
4.  **Упрощение XPath**:
    -   Упростить некоторые XPath запросы, где это возможно.
5.  **Проверка на `None`**:
    -   Проверять на `None` значения, возвращаемые из функций.
6.  **Добавить описание модуля**
7.  **Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.** (но в данном коде нет чтения файлов)
8.  **Соблюдать единый стиль кавычек**:
    -   Использовать одинарные кавычки (`'`) для строк в коде. Двойные только в операциях вывода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для парсинга HTML-страниц Google Search
=========================================================================================

Этот модуль содержит класс :class:`GoogleHtmlParser`, который используется для
парсинга HTML-страниц поисковой выдачи Google и преобразования их в словарь.

Класс поддерживает как мобильную, так и десктопную версии HTML.

Пример использования
--------------------

.. code-block:: python

    html_content = "<html>...</html>"
    parser = GoogleHtmlParser(html_content, user_agent='desktop')
    data = parser.get_data()
    print(data)
"""
from lxml import html
from src.logger import logger  # импортируем logger
class GoogleHtmlParser:
    """
    Класс для парсинга HTML с Google Search.

    Парсит HTML страницы поисковой выдачи Google и преобразует её в словарь.
    Работает как с мобильной, так и с десктопной версией HTML.

    :param html_str: HTML Google Search в виде строки.
    :type html_str: str
    :param user_agent: User agent для получения HTML. Может быть 'mobile' или 'desktop'.
    :type user_agent: str, optional
    :raises ValueError: Если user_agent не является 'mobile' или 'desktop'.
    :ivar tree: Дерево документа, полученное через html.fromstring().
    :vartype tree: html.Element
    :ivar user_agent: User agent, использованный для получения HTML Google Search.
    :vartype user_agent: str
    """

    def __init__(self, html_str: str, user_agent: str = 'desktop') -> None:
        """Инициализация парсера.

        Создает дерево документа из строки HTML.
        """
        self.tree = html.fromstring(html_str)
        if user_agent in ['mobile', 'desktop']:
            self.user_agent = user_agent
        else:
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
        try: # Обработка исключений при парсинге
            estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()')
            if estimated_el: # Проверка на наличие элементов
                estimated_results = int(estimated_el[0].split()[1].replace(',', ''))
        except Exception as e:
            logger.error(f'Ошибка при получении количества результатов поиска: {e}')
        return estimated_results

    def _get_organic(self) -> list:
        """
        Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        :return: Список словарей с органическими результатами.
        :rtype: list
        """
        organic = []
        for g in self.tree.xpath('//div[@class="g"]'):
            try:  # Обработка исключений внутри цикла
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
                    'snippet': self._clean(snippet) if snippet else '',
                    'rich_snippet': self._clean(rich_snippet) if rich_snippet else '',
                }
                organic.append(res)
            except Exception as e:
                logger.error(f'Ошибка при парсинге органических результатов: {e}')
                continue # Переход к следующей итерации цикла
        return organic

    def _get_featured_snippet(self) -> dict | None:
        """
        Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        :return: Словарь с заголовком и URL или None.
        :rtype: dict | None
        """
        fs = None
        try: # Обработка исключений при парсинге
            snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]')
            if snippet_el:
                snippet_el = snippet_el[0]
                heading = snippet_el.xpath('.//h3/text()')
                url = snippet_el.xpath('.//a/@href')
                if heading and url:
                    fs = {'title': heading[0], 'url': url[-1]}
        except Exception as e:
            logger.error(f'Ошибка при парсинге featured snippet: {e}')
        return fs

    def _get_knowledge_card(self) -> dict | None:
        """
        Получение карточки знаний.

        Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

        :return: Словарь с данными карточки знаний или None.
        :rtype: dict | None
        """
        kc_el = self.tree.xpath('//div[contains(@class, "kp-wholepage")]')
        if kc_el:
            try: # Обработка исключений при парсинге
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
            except Exception as e:
                 logger.error(f'Ошибка при парсинге карточки знаний: {e}')
        return None

    def _get_scrolling_sections(self) -> list:
        """
        Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        :return: Список словарей с данными из виджетов.
        :rtype: list
        """
        sections = self.tree.xpath('//g-section-with-header')
        data = []
        for section in sections:
            try: # Обработка исключений при парсинге
                title = section.xpath('.//h3')[0].text_content()
                section_data = []
                for data_section in section.xpath('.//g-inner-card'):
                    data_title = data_section.xpath('.//div[@role="heading"]/text()')[0]
                    data_url = data_section.xpath('.//a/@href')[0]
                    section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)})
                data.append({'section_title': title, 'section_data': section_data})
            except Exception as e:
                logger.error(f'Ошибка при парсинге скроллируемых виджетов: {e}')
                continue # Переход к следующей итерации цикла
        return data

    def get_data(self) -> dict:
        """
        Получение итоговых данных с поисковой страницы.

        Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

        :return: Словарь с данными поисковой страницы.
        :rtype: dict
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
```