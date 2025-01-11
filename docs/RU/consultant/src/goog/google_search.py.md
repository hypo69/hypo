## Анализ кода модуля google_search

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на отдельные методы, каждый из которых выполняет свою задачу.
    - Используются `docstring` для документирования классов и методов.
    - Есть обработка и очистка текста от лишних символов.
    - Код корректно обрабатывает десктопную версию Google Search.
    - Используется `lxml` для парсинга HTML, что является хорошей практикой.
-  Минусы
    - Отсутствует импорт `from src.logger.logger import logger`.
    - Не везде используются одинарные кавычки для строк.
    - Не все строки документации оформлены согласно RST.
    - Нет обработки ошибок, что может привести к сбоям при неожиданной структуре HTML.
    - Присутствует избыточное использование `if len(element) > 0` для проверки существования элемента, что может быть заменено на более лаконичные конструкции.
    -  Необходимо добавить описание модуля в начале файла.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Импортировать `logger` из `src.logger.logger`.
3.  Использовать одинарные кавычки для строковых литералов в коде.
4.  Дополнить `docstring` в формате RST для всех методов и класса.
5.  Заменить конструкции `if len(element) > 0` на более лаконичные проверки.
6.  Добавить обработку исключений с использованием `logger.error` для более стабильной работы.
7.  Улучшить читаемость кода, например, вынести xpath запросы в константы.
8.  Использовать более конкретные имена переменных.
9.  Добавить тип возвращаемых значений для функций с аннотациями.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
# file: src/goog/google_search.py

#! venv/bin/python/python3.12

"""
Модуль для парсинга HTML страниц поисковой выдачи Google.
=========================================================================================

Этот модуль содержит класс :class:`GoogleHtmlParser`, который используется для
парсинга HTML-страниц поисковой выдачи Google и преобразования их в словарь.
Поддерживает как мобильную, так и десктопную версии HTML.

Пример использования
--------------------

Пример использования класса `GoogleHtmlParser`:

.. code-block:: python

    parser = GoogleHtmlParser(html_str='<html>...</html>', user_agent='desktop')
    data = parser.get_data()
"""
from lxml import html
from src.logger.logger import logger


class GoogleHtmlParser:
    """
    Класс для парсинга HTML с Google Search.

    Парсит HTML страницы поисковой выдачи Google и преобразует её в словарь.
    Работает как с мобильной, так и с десктопной версией HTML.

    :param html_str: HTML Google Search в виде строки.
    :type html_str: str
    :param user_agent: User agent для получения HTML. Может быть 'mobile' или 'desktop'.
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
        :raises ValueError: Если `user_agent` не является 'mobile' или 'desktop'.
        """
        self.tree = html.fromstring(html_str)
        if user_agent in ['mobile', 'desktop']:
            self.user_agent = user_agent
        else:
            self.user_agent = 'desktop'
            logger.error(f'Неверный user_agent: {user_agent}. Установлен "desktop"')

    def _clean(self, content: str) -> str:
        """
        Очистка строки от лишних символов.

        Удаляет пробелы в начале и конце строки, а также заменяет множественные пробелы на одинарные.

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
        # xpath запрос для получения количества результатов
        estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()')
        if estimated_el:
            try:
                estimated_results = int(estimated_el[0].split()[1].replace(',', ''))
            except (ValueError, IndexError) as e:
                logger.error(f'Ошибка при извлечении количества результатов: {e}')
        return estimated_results

    def _get_organic(self) -> list[dict]:
        """
        Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        :return: Список словарей с органическими результатами.
        :rtype: list[dict]
        """
        organic = []
        # xpath запрос для получения всех блоков с органическими результатами
        for g in self.tree.xpath('//div[@class="g"]'):
            # xpath запрос для получения сниппетов
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
                # xpath запрос для получения URL и заголовка
                res = {
                    'url': self._clean(g.xpath('.//@href[1]')[0]),
                    'title': self._clean(g.xpath('.//h3/text()')[0]),
                    'snippet': self._clean(snippet),
                    'rich_snippet': self._clean(rich_snippet),
                }
                organic.append(res)
            except IndexError as e:
                logger.error(f'Ошибка при извлечении данных из органического результата: {e}')
                continue
        return organic

    def _get_featured_snippet(self) -> dict | None:
        """
        Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        :return: Словарь с заголовком и URL или None.
        :rtype: dict | None
        """
        fs = None
        # xpath запрос для получения блока с featured snippet
        snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]')
        if snippet_el:
            snippet_el = snippet_el[0]
            # xpath запрос для получения заголовка и URL
            heading = snippet_el.xpath('.//h3/text()')
            url = snippet_el.xpath('.//a/@href')
            if heading and url:
                fs = {'title': heading[0], 'url': url[-1]}
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
            kc_el = kc_el[0]
            more_info = []
            # xpath запрос для получения дополнительной информации
            for el in kc_el.xpath('.//div[contains(@data-attrid, ":/")]'):
                el_parts = el.xpath('.//span')
                if len(el_parts) == 2:
                    more_info.append({self._normalize_dict_key(el_parts[0].text_content()): el_parts[1].text_content()})
            try:
                # xpath запрос для получения заголовка, подзаголовка и описания
                return {
                    'title': kc_el.xpath('.//h2/span')[0].text_content(),
                    'subtitle': kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]')[0].text_content(),
                    'description': kc_el.xpath('.//div[@class="kno-rdesc"]/span')[0].text_content(),
                    'more_info': more_info
                }
            except IndexError as e:
                logger.error(f'Ошибка при извлечении данных из карточки знаний: {e}')

        return None

    def _get_scrolling_sections(self) -> list[dict]:
        """
        Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        :return: Список словарей с данными из виджетов.
        :rtype: list[dict]
        """
        sections = self.tree.xpath('//g-section-with-header')
        data = []
        for section in sections:
            # xpath запрос для получения заголовка секции
            try:
                 title = section.xpath('.//h3')[0].text_content()
            except IndexError as e:
                logger.error(f'Ошибка при получении заголовка секции: {e}')
                continue
            section_data = []
            # xpath запрос для получения данных из секции
            for data_section in section.xpath('.//g-inner-card'):
                try:
                    data_title = data_section.xpath('.//div[@role="heading"]/text()')[0]
                    data_url = data_section.xpath('.//a/@href')[0]
                    section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)})
                except IndexError as e:
                    logger.error(f'Ошибка при извлечении данных из скроллируемой секции: {e}')
                    continue
            data.append({'section_title': title, 'section_data': section_data})
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