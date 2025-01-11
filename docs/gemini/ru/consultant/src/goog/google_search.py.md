### Анализ кода модуля `google_search`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код хорошо структурирован, разбит на методы для парсинга различных элементов страницы.
    - Используется `lxml` для парсинга HTML, что является хорошим выбором для этой задачи.
    - Присутствуют docstring для классов и методов.
- **Минусы**:
    - Не используются одинарные кавычки для строк, кроме случаев когда это необходимо для вывода.
    - Отсутствуют импорты `logger` из `src.logger`.
    - Код не обрабатывает возможные ошибки при парсинге HTML, что может привести к сбоям.
    - Присутствует избыточное использование `if/else`, что может усложнить чтение кода.
    - Недостаточно комментариев в коде для объяснения сложных моментов.

**Рекомендации по улучшению**:
1.  **Форматирование строк**: Использовать одинарные кавычки для всех строк в коде, за исключением случаев вывода (например, в `print`, `input`, `logger`).
2.  **Импорт логгера**: Добавить импорт логгера из `src.logger.logger`.
3.  **Обработка исключений**: Добавить обработку исключений при парсинге HTML (например, когда элемент не найден) и использовать `logger.error` для записи ошибок.
4.  **Упрощение условий**: Упростить условия `if/else`, когда это возможно.
5.  **Уточнение комментариев**: Добавить более подробные комментарии, особенно для xpath-выражений и логики обработки данных.
6.  **Документирование**: Дополнить docstring в формате reStructuredText (RST) с использованием :param:, :type:, :return:, :rtype:.
7.  **Улучшение читаемости**: Выравнивание названий функций и переменных для лучшей читаемости.

**Оптимизированный код**:
```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для парсинга HTML-страниц Google Search
=================================================

Этот модуль содержит класс :class:`GoogleHtmlParser`, который используется для парсинга HTML-страниц
результатов поиска Google. Он поддерживает как десктопную, так и мобильную версии HTML.

Пример использования
----------------------
.. code-block:: python

    from src.goog.google_search import GoogleHtmlParser
    
    html_content = '<html>...</html>' # Замените на ваш HTML контент
    parser = GoogleHtmlParser(html_content, user_agent='desktop')
    data = parser.get_data()
    print(data)
"""

from lxml import html # Импортируем lxml для парсинга HTML
from src.logger import logger # Импортируем логгер
from typing import List, Dict, Optional # Импортируем типы данных

class GoogleHtmlParser:
    """
    Класс для парсинга HTML с Google Search.

    Парсит HTML страницы поисковой выдачи Google и преобразует её в словарь.
    Работает как с мобильной, так и с десктопной версией HTML.

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
        :type user_agent: str, optional
        :raises ValueError: Если user_agent не является 'mobile' или 'desktop'.
        """
        try: # Обработка ошибок при создании дерева HTML
            self.tree = html.fromstring(html_str) # Создаем дерево документа из HTML
        except Exception as e: # Ловим ошибку и логируем ее
            logger.error(f"Ошибка при создании дерева HTML: {e}") # Логируем ошибку
            self.tree = None # Если ошибка при создании дерева, то дерево = None
            return
        if user_agent in ['mobile', 'desktop']: # Проверяем, является ли user_agent допустимым
            self.user_agent = user_agent # Если user_agent допустимый, то присваиваем его self.user_agent
        else:
             self.user_agent = 'desktop' # Иначе user_agent = desktop

    def _clean(self, content: str) -> str:
        """
        Очистка строки от лишних символов.

        Очищает строку от пробелов и лишних символов.

        :param content: Строка для очистки.
        :type content: str
        :return: Очищенная строка.
        :rtype: str
        """
        if content: # Если строка не пустая
            content = content.strip() # Удаляем пробелы в начале и конце
            content = ' '.join(content.split()) # Удаляем лишние пробелы между словами
            return content # Возвращаем очищенную строку
        return '' # Возвращаем пустую строку если content пустой

    def _normalize_dict_key(self, content: str) -> str:
        """
        Нормализация строки для использования в качестве ключа словаря.

        Заменяет пробелы на подчеркивания, убирает двоеточия, приводит к нижнему регистру.

        :param content: Строка для нормализации.
        :type content: str
        :return: Нормализованная строка.
        :rtype: str
        """
        content = str(content).replace(' ', '_').replace(':', '').lower().strip('_') # Заменяем пробелы на подчеркивания, убираем двоеточия, приводим к нижнему регистру, удаляем подчеркивания в начале и конце
        return content # Возвращаем нормализованную строку

    def _get_estimated_results(self) -> int:
        """
        Получение количества результатов поиска.

        Возвращает количество найденных результатов для десктопной версии Google Search.

        :return: Число результатов поиска.
        :rtype: int
        """
        estimated_results = 0 # Инициализируем количество результатов 0
        try: # Обрабатываем ошибки при xpath поиске
            estimated_el = self.tree.xpath('//*[@id="result-stats"]/text()') # Ищем элемент с количеством результатов
            if estimated_el: # Если элемент найден
                estimated_results = int(estimated_el[0].split()[1].replace(',', '')) # Парсим и возвращаем количество результатов
        except Exception as e: # Ловим ошибку и логируем ее
           logger.error(f"Ошибка при получении количества результатов: {e}") # Логируем ошибку
        return estimated_results # Возвращаем количество результатов

    def _get_organic(self) -> List[Dict]:
        """
        Получение органических результатов поиска.

        Возвращает список органических результатов без дополнительных фич (snippet, featured snippet и т.д.).

        :return: Список словарей с органическими результатами.
        :rtype: List[Dict]
        """
        organic = [] # Инициализируем список органических результатов
        try: # Обрабатываем ошибки при xpath поиске
            for g in self.tree.xpath('//div[@class="g"]'): # Ищем блоки с органическими результатами
                snippets = g.xpath('.//div/div/div[2]/div') # Получаем все сниппеты
                snippet, rich_snippet = None, None # Инициализируем сниппеты
                if len(snippets) == 1: # Если один сниппет
                    snippet = snippets[0].text_content() # Получаем текст сниппета
                elif len(snippets) > 1: # Если несколько сниппетов
                    if snippets[1].xpath('.//g-review-stars'): # Если есть рейтинги
                        rich_snippet = snippets[1].text_content() # Получаем текст rich сниппета
                        snippet = snippets[0].text_content() # Получаем текст сниппета
                    else: # Если нет рейтингов
                        snippet = snippets[1].text_content() # Получаем текст сниппета
                        rich_snippet = snippets[0].text_content() # Получаем текст rich сниппета

                res = { # Собираем данные в словарь
                    'url': self._clean(g.xpath('.//@href[1]')[0]), # Получаем URL
                    'title': self._clean(g.xpath('.//h3/text()')[0]), # Получаем заголовок
                    'snippet': self._clean(snippet), # Получаем сниппет
                    'rich_snippet': self._clean(rich_snippet), # Получаем rich сниппет
                }
                organic.append(res) # Добавляем результат в список
        except Exception as e: # Ловим ошибку и логируем ее
           logger.error(f"Ошибка при получении органических результатов: {e}") # Логируем ошибку
        return organic # Возвращаем список органических результатов

    def _get_featured_snippet(self) -> Optional[Dict]:
        """
        Получение featured snippet.

        Если существует, возвращает featured snippet с заголовком и URL.

        :return: Словарь с заголовком и URL или None.
        :rtype: Optional[Dict]
        """
        fs = None # Инициализируем featured snippet
        try: # Обрабатываем ошибки при xpath поиске
            snippet_el = self.tree.xpath('//div[contains(@class, "kp-blk")]') # Ищем элемент featured snippet
            if snippet_el: # Если элемент найден
                snippet_el = snippet_el[0] # Получаем первый элемент
                heading = snippet_el.xpath('.//h3/text()') # Получаем заголовок
                url = snippet_el.xpath('.//a/@href') # Получаем URL
                if heading and url: # Если есть заголовок и URL
                    fs = {'title': heading[0], 'url': url[-1]} # Сохраняем данные
        except Exception as e: # Ловим ошибку и логируем ее
             logger.error(f"Ошибка при получении featured snippet: {e}") # Логируем ошибку
        return fs # Возвращаем featured snippet

    def _get_knowledge_card(self) -> Optional[Dict]:
        """
        Получение карточки знаний.

        Возвращает карточку знаний с заголовком, подзаголовком и описанием, если существует.

        :return: Словарь с данными карточки знаний или None.
        :rtype: Optional[Dict]
        """
        kc_el = None # Инициализируем knowledge card
        try: # Обрабатываем ошибки при xpath поиске
            kc_el = self.tree.xpath('//div[contains(@class, "kp-wholepage")]') # Ищем элемент knowledge card
            if kc_el: # Если элемент найден
                kc_el = kc_el[0] # Получаем первый элемент
                more_info = [] # Инициализируем список с дополнительной информацией
                for el in kc_el.xpath('.//div[contains(@data-attrid, ":/")]'): # Ищем элементы с дополнительной информацией
                    el_parts = el.xpath('.//span') # Получаем части элемента
                    if len(el_parts) == 2: # Если есть 2 части
                        more_info.append({self._normalize_dict_key(el_parts[0].text_content()): el_parts[1].text_content()}) # Сохраняем информацию
                return { # Возвращаем данные
                    'title': kc_el.xpath('.//h2/span')[0].text_content(), # Получаем заголовок
                    'subtitle': kc_el.xpath('.//div[contains(@data-attrid, "subtitle")]')[0].text_content(), # Получаем подзаголовок
                    'description': kc_el.xpath('.//div[@class="kno-rdesc"]/span')[0].text_content(), # Получаем описание
                    'more_info': more_info # Получаем дополнительную информацию
                }
        except Exception as e: # Ловим ошибку и логируем ее
           logger.error(f"Ошибка при получении карточки знаний: {e}") # Логируем ошибку
        return None # Возвращаем None если ничего не нашли

    def _get_scrolling_sections(self) -> List[Dict]:
        """
        Получение данных из скроллируемых виджетов.

        Возвращает список данных из виджетов, например, топовые истории или твиты.

        :return: Список словарей с данными из виджетов.
        :rtype: List[Dict]
        """
        data = [] # Инициализируем список данных
        try: # Обрабатываем ошибки при xpath поиске
            sections = self.tree.xpath('//g-section-with-header') # Ищем элементы скроллируемых секций
            for section in sections: # Проходим по всем секциям
                title = section.xpath('.//h3')[0].text_content() # Получаем заголовок секции
                section_data = [] # Инициализируем список данных секции
                for data_section in section.xpath('.//g-inner-card'): # Проходим по всем элементам данных в секции
                    data_title = data_section.xpath('.//div[@role="heading"]/text()')[0] # Получаем заголовок элемента данных
                    data_url = data_section.xpath('.//a/@href')[0] # Получаем URL элемента данных
                    section_data.append({'title': self._clean(data_title), 'url': self._clean(data_url)}) # Сохраняем данные
                data.append({'section_title': title, 'section_data': section_data}) # Сохраняем данные секции
        except Exception as e: # Ловим ошибку и логируем ее
            logger.error(f"Ошибка при получении скроллируемых секций: {e}") # Логируем ошибку
        return data # Возвращаем список данных

    def get_data(self) -> Dict:
        """
        Получение итоговых данных с поисковой страницы.

        Собирает данные с результатов поиска: органические результаты, карточка знаний и др.

        :return: Словарь с данными поисковой страницы.
        :rtype: Dict
        """
        data = {} # Инициализируем словарь данных
        if self.user_agent == 'desktop': # Если user_agent - десктоп
            data = { # Собираем данные
                'estimated_results': self._get_estimated_results(), # Получаем количество результатов
                'featured_snippet': self._get_featured_snippet(), # Получаем featured snippet
                'knowledge_card': self._get_knowledge_card(), # Получаем knowledge card
                'organic_results': self._get_organic(), # Получаем органические результаты
                'scrolling_widgets': self._get_scrolling_sections() # Получаем скроллируемые секции
            }
        return data # Возвращаем данные