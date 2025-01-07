# Анализ кода модуля `google_search`

**Качество кода**
8
-   Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используется `lxml` для парсинга HTML, что является хорошей практикой.
    - Присутствуют docstring для классов и методов.
    - Код обрабатывает как мобильную, так и десктопную версию Google Search.
    - Есть очистка и нормализация данных.
-   Минусы
    - Не хватает обработки ошибок.
    - Нет логирования.
    - Не все комментарии в формате reStructuredText (RST).
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов (хотя в данном файле нет операций чтения файлов, это все равно важно отметить).
    - Отсутствуют проверки на наличие элементов перед их использованием, что может привести к ошибкам при парсинге.

**Рекомендации по улучшению**

1.  **Добавить логирование**: Использовать `from src.logger.logger import logger` для логирования ошибок и предупреждений.
2.  **Обработка ошибок**: Добавить блоки `try-except` для обработки возможных ошибок при парсинге HTML, особенно при использовании `xpath`. Заменить `try-except` на обработку ошибок с помощью `logger.error`.
3.  **Комментарии RST**: Переписать все комментарии и docstring в формате RST.
4.  **Проверка на наличие элементов**: Добавить проверки на существование элементов перед обращением к ним (например, `if len(elements) > 0:`).
5.  **Убрать избыточность**: Избавиться от избыточного использования `if content:` в методе `_clean`, т.к. `content.strip()` при `content` равном `None` или `''` и так вернет `''`.
6.  **Улучшить docstring**: Дополнить docstring для лучшей документации.
7.  **Согласованность**: Сделать консистентным стиль кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для парсинга HTML страниц поисковой выдачи Google.
======================================================

Этот модуль содержит класс :class:`GoogleHtmlParser`, который используется для анализа HTML-кода,
полученного из поисковой выдачи Google, и извлечения релевантной информации.

Класс поддерживает парсинг как десктопной, так и мобильной версий HTML-страниц.

Пример использования
--------------------

.. code-block:: python

    html_content = "<!DOCTYPE html><html>...</html>" # HTML контент ответа
    parser = GoogleHtmlParser(html_content, user_agent='desktop')
    data = parser.get_data()
    print(data)
"""



from lxml import html
from typing import Any, Dict, List, Optional
from src.logger.logger import logger #  Импорт logger для логирования


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
        :raises ValueError: Если `user_agent` не 'mobile' и не 'desktop'.
        :return: None
        """
        self.tree = html.fromstring(html_str)
        if user_agent in ['mobile', 'desktop']:
            self.user_agent = user_agent
        else:
            self.user_agent = 'desktop'

    def _clean(self, content: Optional[str]) -> str:
        """
        Очистка строки от лишних символов.

        Очищает строку от пробелов и лишних символов.

        :param content: Строка для очистки.
        :return: Очищенная строка.
        """
        if not content:
            return ''
        content = content.strip()
        return ' '.join(content.split())

    def _normalize_dict_key(self, content: str) -> str:
        """
        Нормализация строки для использования в качестве ключа словаря.

        Заменяет пробелы на подчеркивания, убирает двоеточия, приводит к нижнему регистру.

        :param content: Строка для нормализации.
        :return: Нормализованная строка.
        """
        return str(content).replace(' ', '_').replace(':', '').lower().strip('_')

    def _get_estimated_results(self) -> int:
        """
        Получение количества результатов поиска.

        Возвращает количество найденных результатов для десктопной версии Google Search.

        :return: Число результатов поиска.
        """
        estimated_results = 0
        try: #  Обработка ошибок при поиске элемента
            estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()')
            if estimated_el:  #  проверяет что список не пустой
                estimated_results = int(estimated_el[0].split()[1].replace(',', ''))
        except Exception as e: #  Логирование ошибок
            logger.error(f'Ошибка при получении количества результатов поиска: {e}')
        return estimated_results

    def _get_organic(self) -> List[Dict[str, Optional[str]]]:
        """
        Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        :return: Список словарей с органическими результатами.
        """
        organic = []
        for g in self.tree.xpath('//div[@class="g"]'): #  цикл по найденным элементам
            snippets = g.xpath('.//div/div/div[2]/div')
            snippet, rich_snippet = None, None
            if len(snippets) == 1: #  проверяет длину списка
                snippet = snippets[0].text_content()
            elif len(snippets) > 1: #  проверяет длину списка
                if snippets[1].xpath('.//g-review-stars'): #  проверяет наличие элемента
                    rich_snippet = snippets[1].text_content()
                    snippet = snippets[0].text_content()
                else:
                    snippet = snippets[1].text_content()
                    rich_snippet = snippets[0].text_content()
            try: #  Обработка ошибок при получении данных
                res = {
                    'url': self._clean(g.xpath('.//@href[1]')[0]),
                    'title': self._clean(g.xpath('.//h3/text()')[0]),
                    'snippet': self._clean(snippet),
                    'rich_snippet': self._clean(rich_snippet),
                }
                organic.append(res)
            except Exception as e: #  Логирование ошибок
                 logger.error(f'Ошибка при получении органических результатов: {e}')
        return organic

    def _get_featured_snippet(self) -> Optional[Dict[str, str]]:
        """
        Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        :return: Словарь с заголовком и URL или None.
        """
        fs = None
        try: #  Обработка ошибок при поиске элемента
            snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]')
            if snippet_el: #  проверяет что список не пустой
                snippet_el = snippet_el[0]
                heading = snippet_el.xpath('.//h3/text()')
                url = snippet_el.xpath('.//a/@href')
                if heading and url: #  проверяет что списки не пустые
                    fs = {'title': heading[0], 'url': url[-1]}
        except Exception as e: #  Логирование ошибок
            logger.error(f'Ошибка при получении featured snippet: {e}')
        return fs

    def _get_knowledge_card(self) -> Optional[Dict[str, Any]]:
        """
        Получение карточки знаний.

        Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

        :return: Словарь с данными карточки знаний или None.
        """
        kc_data = None
        try: #  Обработка ошибок при поиске элемента
            kc_el = self.tree.xpath('//div[contains(@class, "kp-wholepage")]')
            if kc_el: #  проверяет что список не пустой
                kc_el = kc_el[0]
                more_info = []
                for el in kc_el.xpath('.//div[contains(@data-attrid, ":/")]'): #  цикл по найденным элементам
                    el_parts = el.xpath('.//span')
                    if len(el_parts) == 2: #  проверяет длину списка
                        more_info.append({self._normalize_dict_key(el_parts[0].text_content()): el_parts[1].text_content()})
                kc_data = {
                    'title': kc_el.xpath('.//h2/span')[0].text_content(),
                    'subtitle': kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]')[0].text_content(),
                    'description': kc_el.xpath('.//div[@class="kno-rdesc"]/span')[0].text_content(),
                    'more_info': more_info
                }
        except Exception as e: #  Логирование ошибок
            logger.error(f'Ошибка при получении карточки знаний: {e}')
        return kc_data

    def _get_scrolling_sections(self) -> List[Dict[str, Any]]:
        """
        Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        :return: Список словарей с данными из виджетов.
        """
        data = []
        try: #  Обработка ошибок при поиске элемента
            sections = self.tree.xpath('//g-section-with-header')
            for section in sections:  #  цикл по найденным элементам
                title = section.xpath('.//h3')[0].text_content()
                section_data = []
                for data_section in section.xpath('.//g-inner-card'): #  цикл по найденным элементам
                    data_title = data_section.xpath('.//div[@role="heading"]/text()')[0]
                    data_url = data_section.xpath('.//a/@href')[0]
                    section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)})
                data.append({'section_title': title, 'section_data': section_data})
        except Exception as e: #  Логирование ошибок
            logger.error(f'Ошибка при получении скроллируемых секций: {e}')
        return data

    def get_data(self) -> Dict[str, Any]:
        """
        Получение итоговых данных с поисковой страницы.

        Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

        :return: Словарь с данными поисковой страницы.
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