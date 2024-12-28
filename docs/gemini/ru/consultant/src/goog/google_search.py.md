# Анализ кода модуля `google_search`

**Качество кода**
8
-   Плюсы
    - Код хорошо структурирован и разбит на функции, что делает его читаемым.
    - Используются docstring для описания классов и методов.
    - Присутствуют проверки на наличие данных перед их использованием.
-   Минусы
    -  Отсутствует обработка ошибок.
    -  В коде есть некоторые места, которые можно улучшить с точки зрения читаемости и производительности.
    -  Некоторые docstring не полные и не соответствуют rst.

**Рекомендации по улучшению**

1. **Обработка ошибок**:
   - Необходимо добавить обработку исключений, возникающих при парсинге HTML, чтобы избежать сбоев программы.
   - Использовать `logger.error` для записи ошибок.
2. **Улучшение `docstring`**:
   - Дополнить описание модуля в начале файла и каждой функции в соответствии со стандартом reStructuredText (RST).
   - Добавить описание возвращаемых значений для каждой функции.
3. **Соответствие PEP 8**:
   - Проверить код на соответствие стандарту PEP 8 (например, использование 4 пробелов для отступов).
4. **Улучшение производительности**:
    - Использовать `get()` метод словаря для извлечения значений.
5. **Использовать `j_loads` или `j_loads_ns`**:
   - В этом файле не используются `j_loads` или `j_loads_ns`, но стоит отметить необходимость их использования в других файлах.
6. **Добавить импорты**:
  - Добавить `from src.logger.logger import logger` для логирования ошибок.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для парсинга результатов поиска Google.
=========================================================================================

Этот модуль содержит класс :class:`GoogleHtmlParser`, который используется для
парсинга HTML-страниц поисковой выдачи Google и извлечения структурированных данных.
Поддерживает как мобильную, так и десктопную версии.

Пример использования
--------------------

.. code-block:: python

    html_content = "<html>...</html>"  # Замените на реальный HTML-код
    parser = GoogleHtmlParser(html_content, user_agent='desktop')
    data = parser.get_data()
    print(data)
"""


from lxml import html
from typing import Dict, List, Optional
from src.logger.logger import logger


class GoogleHtmlParser:
    """
    Класс для парсинга HTML с Google Search.

    Парсит HTML страницы поисковой выдачи Google и преобразует её в словарь.
    Работает как с мобильной, так и с десктопной версией HTML.

    :param html_str: HTML Google Search в виде строки.
    :type html_str: str
    :param user_agent: User agent для получения HTML. Может быть \'mobile\' или \'desktop\'. По умолчанию 'desktop'.
    :type user_agent: str
    :ivar tree: Дерево документа, полученное через html.fromstring().
    :vartype tree: html.Element
    :ivar user_agent: User agent, использованный для получения HTML Google Search.
    :vartype user_agent: str
    """

    def __init__(self, html_str: str, user_agent: str = 'desktop') -> None:
        """
        Инициализация парсера.

        Создает дерево документа из строки HTML.

        :param html_str: HTML Google Search в виде строки.
        :type html_str: str
        :param user_agent: User agent для получения HTML. Может быть 'mobile' или 'desktop'.
        :type user_agent: str
        :return: None
        :rtype: None
        """
        try:
            # код инициализирует дерево документа из HTML строки
            self.tree = html.fromstring(html_str)
            # код проверяет user_agent и устанавливает значение по умолчанию
            if user_agent in ['mobile', 'desktop']:
                self.user_agent = user_agent
            else:
                self.user_agent = 'desktop'
        except Exception as e:
            # Логируем ошибку при инициализации
            logger.error(f'Ошибка при инициализации GoogleHtmlParser: {e}')
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
            # код удаляет лишние пробелы и символы из строки
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
        # код заменяет пробелы, удаляет двоеточия и приводит к нижнему регистру
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
        try:
            # код получает элемент с количеством результатов поиска
            estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()')
            if estimated_el:
                # код извлекает и форматирует число результатов поиска
                estimated_results = int(estimated_el[0].split()[1].replace(',', ''))
        except Exception as e:
            # Логируем ошибку при получении количества результатов
             logger.error(f'Ошибка при получении количества результатов поиска: {e}')
        return estimated_results

    def _get_organic(self) -> List[Dict]:
        """
        Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        :return: Список словарей с органическими результатами.
        :rtype: list[dict]
        """
        organic = []
        try:
            # цикл по всем элементам, содержащим органические результаты
            for g in self.tree.xpath('//div[@class="g"]'):
                # код извлекает сниппеты
                snippets = g.xpath('.//div/div/div[2]/div')
                snippet, rich_snippet = None, None
                if len(snippets) == 1:
                    snippet = snippets[0].text_content()
                elif len(snippets) > 1:
                    # код определяет тип сниппета
                    if snippets[1].xpath('.//g-review-stars'):
                        rich_snippet = snippets[1].text_content()
                        snippet = snippets[0].text_content()
                    else:
                        snippet = snippets[1].text_content()
                        rich_snippet = snippets[0].text_content()
                # код создает словарь с данными органического результата
                res = {
                    'url': self._clean(g.xpath('.//@href[1]')[0]),
                    'title': self._clean(g.xpath('.//h3/text()')[0]),
                    'snippet': self._clean(snippet),
                    'rich_snippet': self._clean(rich_snippet),
                }
                organic.append(res)
        except Exception as e:
            # Логируем ошибку при получении органических результатов
            logger.error(f'Ошибка при получении органических результатов: {e}')
        return organic

    def _get_featured_snippet(self) -> Optional[Dict]:
        """
        Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        :return: Словарь с заголовком и URL или None.
        :rtype: dict | None
        """
        fs = None
        try:
            # код ищет элемент featured snippet
            snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]')
            if snippet_el:
                snippet_el = snippet_el[0]
                heading = snippet_el.xpath('.//h3/text()')
                url = snippet_el.xpath('.//a/@href')
                if heading and url:
                    fs = {'title': heading[0], 'url': url[-1]}
        except Exception as e:
            # Логируем ошибку при получении featured snippet
            logger.error(f'Ошибка при получении featured snippet: {e}')
        return fs

    def _get_knowledge_card(self) -> Optional[Dict]:
        """
        Получение карточки знаний.

        Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

        :return: Словарь с данными карточки знаний или None.
        :rtype: dict | None
        """
        kc_data = None
        try:
            # код ищет элемент карточки знаний
            kc_el = self.tree.xpath('//div[contains(@class, "kp-wholepage")]')
            if kc_el:
                kc_el = kc_el[0]
                more_info = []
                # код извлекает дополнительную информацию
                for el in kc_el.xpath('.//div[contains(@data-attrid, ":/")]'):
                    el_parts = el.xpath('.//span')
                    if len(el_parts) == 2:
                        more_info.append({self._normalize_dict_key(el_parts[0].text_content()): el_parts[1].text_content()})
                # код формирует и возвращает словарь с данными карточки знаний
                kc_data = {
                    'title': kc_el.xpath('.//h2/span')[0].text_content(),
                    'subtitle': kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]')[0].text_content(),
                    'description': kc_el.xpath('.//div[@class="kno-rdesc"]/span')[0].text_content(),
                    'more_info': more_info
                }
        except Exception as e:
            # Логируем ошибку при получении карточки знаний
            logger.error(f'Ошибка при получении карточки знаний: {e}')
        return kc_data

    def _get_scrolling_sections(self) -> List[Dict]:
        """
        Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        :return: Список словарей с данными из виджетов.
        :rtype: list[dict]
        """
        sections_data = []
        try:
            # код ищет элементы секций скроллинга
            sections = self.tree.xpath('//g-section-with-header')
            for section in sections:
                # код извлекает заголовок секции
                title = section.xpath('.//h3')[0].text_content()
                section_data = []
                for data_section in section.xpath('.//g-inner-card'):
                    # код извлекает данные из каждой карточки в секции
                    data_title = data_section.xpath('.//div[@role="heading"]/text()')[0]
                    data_url = data_section.xpath('.//a/@href')[0]
                    section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)})
                sections_data.append({'section_title': title, 'section_data': section_data})
        except Exception as e:
            # Логируем ошибку при получении данных из скроллируемых секций
            logger.error(f'Ошибка при получении данных из скроллируемых секций: {e}')
        return sections_data

    def get_data(self) -> Dict:
        """
        Получение итоговых данных с поисковой страницы.

        Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

        :return: Словарь с данными поисковой страницы.
        :rtype: dict
        """
        data = {}
        # код проверяет user_agent и собирает соответствующие данные
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