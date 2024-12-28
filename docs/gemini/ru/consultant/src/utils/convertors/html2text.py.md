## Анализ кода модуля html2text

**Качество кода: 7/10**
 -  Плюсы
    - Код выполняет поставленную задачу по преобразованию HTML в Markdown.
    - Присутствует обработка различных HTML-тегов и стилей.
    - Поддержка Google Docs.
    - Присутствует возможность настройки ширины вывода и символа для списка.
 -  Минусы
    - Отсутствуют docstring для модуля и функций.
    - Используется устаревший `optparse` вместо `argparse`.
    - Обработка ошибок не всегда явная и не использует `logger`.
    - Сложная логика обработки стилей.
    - Много глобальных переменных.
    - Неоднородность форматирования.

**Рекомендации по улучшению**

1. **Документация:** Добавить docstring к модулю и всем функциям, используя reStructuredText.
2. **Импорты:** Проверить и добавить отсутствующие импорты, например, `from src.logger.logger import logger`.
3. **Обработка ошибок:** Использовать `logger.error` вместо стандартных `try-except` для логирования ошибок.
4. **Рефакторинг:** Упростить и разбить на более мелкие функции логику обработки стилей и тегов.
5. **Глобальные переменные:** Минимизировать использование глобальных переменных, передавать их как аргументы в функции.
6. **argparse:** Заменить `optparse` на `argparse`.
7. **Форматирование:** Привести код к единому стилю, соблюдая PEP8.
8. **Комментарии:** Добавить подробные комментарии для сложных частей кода в формате RST.
9. **Unicode:** Использовать явное кодирование UTF-8, убрав лишние `try-except` блоки для Python 2 и 3.
10. **Обработка файлов:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для преобразования HTML в Markdown.
=========================================

Этот модуль содержит функции и класс для преобразования HTML-документов в
эквивалентный текст в формате Markdown.

Модуль поддерживает:

-   Различные HTML-теги (заголовки, параграфы, списки, ссылки, изображения).
-   Стили Google Docs.
-   Настройку ширины вывода и символа для списка.

Пример использования
--------------------

.. code-block:: python

    from src.utils.convertors.html2text import html2text

    html_text = "<h1>Заголовок</h1><p>Текст</p>"
    markdown_text = html2text(html_text)
    print(markdown_text)
"""
#  Импортируем необходимые модули из стандартной библиотеки Python
import html.entities as htmlentitydefs
import urllib.parse as urlparse
import html.parser as HTMLParser
import urllib.request as urllib
import re
import sys
import codecs
import argparse
from textwrap import wrap

#  Импортируем модуль для логирования
from src.logger.logger import logger
#  Импортируем функции для работы с json
# from src.utils.jjson import j_loads, j_loads_ns #TODO не используется

#  Константы для работы модуля


__version__ = "3.1"
__author__ = "Aaron Swartz (me@aaronsw.com)"
__copyright__ = "(C) 2004-2008 Aaron Swartz. GNU GPL 3."
__contributors__ = ["Martin \'Joey\' Schulze", "Ricardo Reyes", "Kevin Jay North"]

#  Флаг для использования Unicode символов вместо ASCII
UNICODE_SNOB = 0
#  Флаг для размещения ссылок после каждого параграфа
LINKS_EACH_PARAGRAPH = 0
#  Ширина строки для переноса текста
BODY_WIDTH = 78
#  Флаг для пропуска внутренних ссылок
SKIP_INTERNAL_LINKS = True
#  Флаг для использования встроенных ссылок вместо сносок
INLINE_LINKS = True
#  Отступ для вложенных списков в Google Docs
GOOGLE_LIST_INDENT = 36
#  Флаг для игнорирования ссылок
IGNORE_ANCHORS = False
#  Флаг для игнорирования изображений
IGNORE_IMAGES = False

#  Словарь для замены HTML-сущностей на Unicode символы
unifiable = {
    'rsquo': "'", 'lsquo': "'", 'rdquo': '"', 'ldquo': '"',
    'copy': '(C)', 'mdash': '--', 'nbsp': ' ', 'rarr': '->', 'larr': '<-', 'middot': '*',
    'ndash': '-', 'oelig': 'oe', 'aelig': 'ae',
    'agrave': 'a', 'aacute': 'a', 'acirc': 'a', 'atilde': 'a', 'auml': 'a', 'aring': 'a',
    'egrave': 'e', 'eacute': 'e', 'ecirc': 'e', 'euml': 'e',
    'igrave': 'i', 'iacute': 'i', 'icirc': 'i', 'iuml': 'i',
    'ograve': 'o', 'oacute': 'o', 'ocirc': 'o', 'otilde': 'o', 'ouml': 'o',
    'ugrave': 'u', 'uacute': 'u', 'ucirc': 'u', 'uuml': 'u',
    'lrm': '', 'rlm': ''
}
unifiable_n = {name2cp(k): unifiable[k] for k in unifiable.keys()}

def has_key(x, y):
    """
    Проверяет наличие ключа в словаре или атрибута в объекте.

    :param x: Словарь или объект для проверки.
    :param y: Ключ или атрибут для поиска.
    :return: True, если ключ или атрибут присутствует, иначе False.
    """
    if hasattr(x, 'has_key'):
        return x.has_key(y)
    else:
        return y in x

def name2cp(k):
    """
    Преобразует имя HTML-сущности в кодовую точку Unicode.

    :param k: Имя HTML-сущности.
    :return: Кодовая точка Unicode.
    """
    if k == 'apos':
        return ord("'")
    if hasattr(htmlentitydefs, "name2codepoint"):
        return htmlentitydefs.name2codepoint[k]
    else:
        k = htmlentitydefs.entitydefs[k]
        if k.startswith("&#") and k.endswith(";"):
            return int(k[2:-1])
        return ord(codecs.latin_1_decode(k)[0])

def charref(name):
    """
    Преобразует числовую ссылку на символ в символ Unicode.

    :param name: Числовая ссылка на символ (например, '123' или 'x41').
    :return: Символ Unicode.
    """
    if name[0] in ['x', 'X']:
        c = int(name[1:], 16)
    else:
        c = int(name)
    if not UNICODE_SNOB and c in unifiable_n:
        return unifiable_n[c]
    else:
        try:
            return chr(c)
        except ValueError as ex:
            logger.error(f'Не удалось преобразовать числовую ссылку в символ {name=}', ex)
            return ''

def entityref(c):
    """
    Преобразует именованную ссылку на символ в символ Unicode.

    :param c: Именованная ссылка на символ (например, 'amp').
    :return: Символ Unicode.
    """
    if not UNICODE_SNOB and c in unifiable:
        return unifiable[c]
    try:
      name2cp(c)
    except KeyError as ex:
       logger.error(f'Неизвестная HTML-сущность: {c=}', ex)
       return "&" + c + ';'
    try:
       return chr(name2cp(c))
    except ValueError as ex:
        logger.error(f'Не удалось преобразовать именованную ссылку в символ {c=}', ex)
        return ''

def replaceEntities(s):
    """
    Заменяет HTML-сущности на соответствующие символы.

    :param s: Строка с HTML-сущностью.
    :return: Строка с замененным символом.
    """
    s = s.group(1)
    if s[0] == "#":
        return charref(s[1:])
    else:
        return entityref(s)

r_unescape = re.compile(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));")

def unescape(s):
    """
    Заменяет все HTML-сущности в строке на соответствующие символы.

    :param s: Строка с HTML-сущностями.
    :return: Строка с замененными символами.
    """
    return r_unescape.sub(replaceEntities, s)

def onlywhite(line):
    """
    Проверяет, состоит ли строка только из пробельных символов.

    :param line: Строка для проверки.
    :return: True, если строка состоит только из пробельных символов, иначе False.
    """
    for c in line:
        if c != ' ' and c != '\t':
            return False
    return True

def optwrap(text):
    """
    Переносит длинные параграфы в тексте.

    :param text: Текст для переноса.
    :return: Текст с перенесенными строками.
    """
    if not BODY_WIDTH:
        return text

    result = ''
    newlines = 0
    for para in text.split("\n"):
        if len(para) > 0:
            if para[0] != ' ' and para[0] != '-' and para[0] != '*':
                for line in wrap(para, BODY_WIDTH):
                    result += line + "\n"
                result += "\n"
                newlines = 2
            else:
                if not onlywhite(para):
                    result += para + "\n"
                    newlines = 1
        else:
            if newlines < 2:
                result += "\n"
                newlines += 1
    return result

def hn(tag):
    """
    Определяет уровень заголовка по тегу.

    :param tag: HTML-тег (например, 'h1', 'h2').
    :return: Уровень заголовка (1-9) или 0, если тег не является заголовком.
    """
    if tag[0] == 'h' and len(tag) == 2:
        try:
            n = int(tag[1])
            if 1 <= n <= 9:
                return n
        except ValueError:
            return 0
    return 0

def dumb_property_dict(style):
    """
    Разбирает строку CSS-стилей в словарь атрибутов.

    :param style: Строка CSS-стилей.
    :return: Словарь, где ключи - это имена атрибутов, а значения - значения атрибутов.
    """
    return dict(
        (x.strip(), y.strip())
        for x, y in [z.split(':', 1) for z in style.split(';') if ':' in z]
    )

def dumb_css_parser(data):
    """
    Разбирает CSS-данные в словарь селекторов и их атрибутов.

    :param data: Строка CSS-данных.
    :return: Словарь, где ключи - это CSS-селекторы, а значения - словари атрибутов.
    """
    import_index = data.find('@import')
    while import_index != -1:
        data = data[:import_index] + data[data.find(';', import_index) + 1:]
        import_index = data.find('@import')
    elements = [x.split('{') for x in data.split('}') if '{' in x.strip()]
    return dict((a.strip(), dumb_property_dict(b)) for a, b in elements)

def element_style(attrs, style_def, parent_style):
    """
    Определяет окончательные стили элемента.

    :param attrs: Словарь атрибутов HTML-тега.
    :param style_def: Словарь CSS-стилей.
    :param parent_style: Словарь стилей родительского элемента.
    :return: Словарь стилей элемента.
    """
    style = parent_style.copy()
    if 'class' in attrs:
        for css_class in attrs['class'].split():
            if '.' + css_class in style_def:
                css_style = style_def['.' + css_class]
                style.update(css_style)
    if 'style' in attrs:
        immediate_style = dumb_property_dict(attrs['style'])
        style.update(immediate_style)
    return style

def google_list_style(style):
    """
    Определяет тип списка (упорядоченный или неупорядоченный) по стилю Google Docs.

    :param style: Словарь стилей элемента.
    :return: 'ul' для неупорядоченного списка, 'ol' для упорядоченного списка.
    """
    if 'list-style-type' in style:
        list_style = style['list-style-type']
        if list_style in ['disc', 'circle', 'square', 'none']:
            return 'ul'
    return 'ol'

def google_nest_count(style):
    """
    Рассчитывает уровень вложенности списка Google Docs.

    :param style: Словарь стилей элемента.
    :return: Уровень вложенности списка.
    """
    nest_count = 0
    if 'margin-left' in style:
        try:
            nest_count = int(style['margin-left'][:-2]) / GOOGLE_LIST_INDENT
        except ValueError as ex:
            logger.error(f'Не удалось рассчитать уровень вложенности {style=}', ex)
    return int(nest_count)

def google_has_height(style):
    """
    Проверяет, задана ли высота элемента явно в стилях Google Docs.

    :param style: Словарь стилей элемента.
    :return: True, если высота задана, иначе False.
    """
    return 'height' in style

def google_text_emphasis(style):
    """
    Определяет модификаторы выделения текста элемента Google Docs.

    :param style: Словарь стилей элемента.
    :return: Список модификаторов выделения текста (например, ['line-through', 'italic', 'bold']).
    """
    emphasis = []
    if 'text-decoration' in style:
        emphasis.append(style['text-decoration'])
    if 'font-style' in style:
        emphasis.append(style['font-style'])
    if 'font-weight' in style:
        emphasis.append(style['font-weight'])
    return emphasis

def google_fixed_width_font(style):
    """
    Проверяет, используется ли моноширинный шрифт в стилях Google Docs.

    :param style: Словарь стилей элемента.
    :return: True, если используется моноширинный шрифт, иначе False.
    """
    font_family = style.get('font-family', '')
    return font_family in ['Courier New', 'Consolas']

def list_numbering_start(attrs):
    """
    Извлекает начальный номер списка из атрибутов элемента.

    :param attrs: Словарь атрибутов HTML-тега.
    :return: Начальный номер списка (начинается с 0) или 0, если атрибут 'start' отсутствует.
    """
    if 'start' in attrs:
        try:
            return int(attrs['start']) - 1
        except ValueError as ex:
            logger.error(f'Неверный атрибут start {attrs=}', ex)
            return 0
    else:
        return 0

class _html2text(HTMLParser.HTMLParser):
    """
    Класс для преобразования HTML в Markdown.

    :param out: Функция для вывода текста.
    :param baseurl: Базовый URL для ссылок.
    """
    def __init__(self, out=None, baseurl=''):
        """
        Инициализирует объект класса _html2text.

        :param out: Функция для вывода текста.
        :param baseurl: Базовый URL для ссылок.
        """
        HTMLParser.HTMLParser.__init__(self)
        self.out = out if out else self.outtextf
        self.outtextlist = []
        self.outtext = ''
        self.quiet = 0
        self.p_p = 0
        self.outcount = 0
        self.start = 1
        self.space = 0
        self.a = []
        self.astack = []
        self.acount = 0
        self.list = []
        self.blockquote = 0
        self.pre = 0
        self.startpre = 0
        self.code = False
        self.br_toggle = ''
        self.lastWasNL = False
        self.lastWasList = False
        self.style = 0
        self.style_def = {}
        self.tag_stack = []
        self.emphasis = 0
        self.drop_white_space = 0
        self.inheader = False
        self.abbr_title = None
        self.abbr_data = None
        self.abbr_list = {}
        self.baseurl = baseurl

        if options.google_doc:
            del unifiable_n[name2cp('nbsp')]
            unifiable['nbsp'] = '&nbsp_place_holder;'

    def feed(self, data):
        """
        Обрабатывает HTML-данные.

        :param data: HTML-данные.
        """
        data = data.replace("</' + \'script>", "</ignore>")
        HTMLParser.HTMLParser.feed(self, data)

    def outtextf(self, s):
        """
        Добавляет текст в список для последующего вывода.

        :param s: Строка текста для добавления.
        """
        self.outtextlist.append(s)
        if s:
            self.lastWasNL = s[-1] == '\n'

    def close(self):
        """
        Завершает разбор HTML и возвращает текст.

        :return: Текст в формате Markdown.
        """
        HTMLParser.HTMLParser.close(self)
        self.pbr()
        self.o('', 0, 'end')
        self.outtext = "".join(self.outtextlist)
        if options.google_doc:
            self.outtext = self.outtext.replace('&nbsp_place_holder;', ' ')
        return self.outtext

    def handle_charref(self, c):
        """
        Обрабатывает числовые ссылки на символы.

        :param c: Числовая ссылка на символ.
        """
        self.o(charref(c), 1)

    def handle_entityref(self, c):
        """
        Обрабатывает именованные ссылки на символы.

        :param c: Именованная ссылка на символ.
        """
        self.o(entityref(c), 1)

    def handle_starttag(self, tag, attrs):
        """
        Обрабатывает начальный HTML-тег.

        :param tag: Имя HTML-тега.
        :param attrs: Словарь атрибутов HTML-тега.
        """
        self.handle_tag(tag, attrs, 1)

    def handle_endtag(self, tag):
        """
        Обрабатывает конечный HTML-тег.

        :param tag: Имя HTML-тега.
        """
        self.handle_tag(tag, None, 0)

    def previousIndex(self, attrs):
        """
        Возвращает индекс ссылки в списке ссылок, если она есть.

        :param attrs: Словарь атрибутов HTML-тега.
        :return: Индекс ссылки в списке или None, если ссылка не найдена.
        """
        if not has_key(attrs, 'href'):
            return None
        for i, a in enumerate(self.a):
            match = False
            if has_key(a, 'href') and a['href'] == attrs['href']:
                if has_key(a, 'title') or has_key(attrs, 'title'):
                    if (has_key(a, 'title') and has_key(attrs, 'title') and
                            a['title'] == attrs['title']):
                        match = True
                else:
                    match = True
            if match:
                return i
        return None

    def drop_last(self, n_letters):
        """
        Удаляет последние n символов из вывода, если не в режиме quiet.

        :param n_letters: Количество символов для удаления.
        """
        if not self.quiet:
           self.outtext = self.outtext[:-n_letters]

    def handle_emphasis(self, start, tag_style, parent_style):
        """
        Обрабатывает выделение текста.

        :param start: Флаг, указывающий, является ли тег открывающим.
        :param tag_style: Словарь стилей текущего тега.
        :param parent_style: Словарь стилей родительского тега.
        """
        tag_emphasis = google_text_emphasis(tag_style)
        parent_emphasis = google_text_emphasis(parent_style)

        strikethrough = 'line-through' in tag_emphasis and options.hide_strikethrough
        bold = 'bold' in tag_emphasis and not 'bold' in parent_emphasis
        italic = 'italic' in tag_emphasis and not 'italic' in parent_emphasis
        fixed = google_fixed_width_font(tag_style) and not google_fixed_width_font(
            parent_style) and not self.pre

        if start:
            if bold or italic or fixed:
                self.emphasis += 1
            if strikethrough:
                self.quiet += 1
            if italic:
                self.o("_")
                self.drop_white_space += 1
            if bold:
                self.o("**")
                self.drop_white_space += 1
            if fixed:
                self.o('`')
                self.drop_white_space += 1
                self.code = True
        else:
            if bold or italic or fixed:
                self.emphasis -= 1
                self.space = 0
                self.outtext = self.outtext.rstrip()
            if fixed:
                if self.drop_white_space:
                   self.drop_last(1)
                   self.drop_white_space -= 1
                else:
                    self.o('`')
                self.code = False
            if bold:
                if self.drop_white_space:
                    self.drop_last(2)
                    self.drop_white_space -= 1
                else:
                    self.o("**")
            if italic:
                if self.drop_white_space:
                    self.drop_last(1)
                    self.drop_white_space -= 1
                else:
                    self.o("_")
            if (bold or italic) and not self.emphasis:
                self.o(" ")
            if strikethrough:
                self.quiet -= 1

    def handle_tag(self, tag, attrs, start):
        """
        Обрабатывает HTML-тег.

        :param tag: Имя HTML-тега.
        :param attrs: Словарь атрибутов HTML-тега.
        :param start: Флаг, указывающий, является ли тег открывающим.
        """
        if attrs is None:
            attrs = {}
        else:
            attrs = dict(attrs)

        if options.google_doc:
            parent_style = {}
            if start:
                if self.tag_stack:
                    parent_style = self.tag_stack[-1][2]
                tag_style = element_style(attrs, self.style_def, parent_style)
                self.tag_stack.append((tag, attrs, tag_style))
            else:
                if self.tag_stack:
                    _, attrs, tag_style = self.tag_stack.pop()
                    if self.tag_stack:
                        parent_style = self.tag_stack[-1][2]

        if hn(tag):
            self.p()
            if start:
                self.inheader = True
                self.o(hn(tag) * "#" + ' ')
            else:
                self.inheader = False
                return

        if tag in ['p', 'div']:
            if options.google_doc:
                if start and google_has_height(tag_style):
                    self.p()
                else:
                    self.soft_br()
            else:
                self.p()

        if tag == "br" and start:
            self.o("  \n")

        if tag == "hr" and start:
            self.p()
            self.o("* * *")
            self.p()

        if tag in ["head", "style", 'script']:
            if start:
                self.quiet += 1
            else:
                self.quiet -= 1

        if tag == "style":
            if start:
                self.style += 1
            else:
                self.style -= 1

        if tag in ["body"]:
            self.quiet = 0

        if tag == "blockquote":
            if start:
                self.p()
                self.o('> ', 0, 1)
                self.start = 1
                self.blockquote += 1
            else:
                self.blockquote -= 1
                self.p()

        if tag in ['em', 'i', 'u']:
            self.o("_")
        if tag in ['strong', 'b']:
            self.o("**")
        if tag in ['del', 'strike']:
             if start:
                self.o("<"+tag+">")
             else:
                self.o("</"+tag+">")
        if options.google_doc:
            if not self.inheader:
                self.handle_emphasis(start, tag_style, parent_style)

        if tag == "code" and not self.pre:
            self.o('`')
        if tag == "abbr":
            if start:
                self.abbr_title = None
                self.abbr_data = ''
                if has_key(attrs, 'title'):
                    self.abbr_title = attrs['title']
            else:
                if self.abbr_title:
                    self.abbr_list[self.abbr_data] = self.abbr_title
                    self.abbr_title = None
                self.abbr_data = ''

        if tag == "a" and not IGNORE_ANCHORS:
            if start:
                if has_key(attrs, 'href') and not (
                        SKIP_INTERNAL_LINKS and attrs['href'].startswith('#')):
                    self.astack.append(attrs)
                    self.o("[")
                else:
                    self.astack.append(None)
            else:
                if self.astack:
                    a = self.astack.pop()
                    if a:
                        if INLINE_LINKS:
                            self.o("](" + a['href'] + ")")
                        else:
                            i = self.previousIndex(a)
                            if i is not None:
                                a = self.a[i]
                            else:
                                self.acount += 1
                                a['count'] = self.acount
                                a['outcount'] = self.outcount
                                self.a.append(a)
                            self.o("][" + str(a['count']) + "]")

        if tag == "img" and start and not IGNORE_IMAGES:
            if has_key(attrs, 'src'):
                attrs['href'] = attrs['src']
                alt = attrs.get('alt', '')
                if INLINE_LINKS:
                    self.o("![")
                    self.o(alt)
                    self.o("](" + attrs['href'] + ")")
                else:
                    i = self.previousIndex(attrs)
                    if i is not None:
                        attrs = self.a[i]
                    else:
                        self.acount += 1
                        attrs['count'] = self.acount
                        attrs['outcount'] = self.outcount
                        self.a.append(attrs)
                    self.o("![")
                    self.o(alt)
                    self.o("][" + str(attrs['count']) + "]")

        if tag == 'dl' and start:
            self.p()
        if tag == 'dt' and not start:
            self.pbr()
        if tag == 'dd' and start:
            self.o('    ')
        if tag == 'dd' and not start:
            self.pbr()

        if tag in ["ol", "ul"]:
            if (not self.list) and (not self.lastWasList):
                self.p()
            if start:
                if options.google_doc:
                    list_style = google_list_style(tag_style)
                else:
                    list_style = tag
                numbering_start = list_numbering_start(attrs)
                self.list.append({'name': list_style, 'num': numbering_start})
            else:
                if self.list:
                    self.list.pop()
            self.lastWasList = True
        else:
            self.lastWasList = False

        if tag == 'li':
            self.pbr()
            if start:
                if self.list:
                    li = self.list[-1]
                else:
                    li = {'name': 'ul', 'num': 0}
                if options.google_doc:
                    nest_count = google_nest_count(tag_style)
                else:
                    nest_count = len(self.list)
                self.o("  " * nest_count)
                if li['name'] == "ul":
                    self.o(options.ul_item_mark + " ")
                elif li['name'] == "ol":
                    li['num'] += 1
                    self.o(str(li['num']) + ". ")
                self.start = 1

        if tag in ["table", "tr"] and start:
            self.p()
        if tag == 'td':
            self.pbr()

        if tag == "pre":
            if start:
                self.startpre = 1
                self.pre = 1
            else:
                self.pre = 0
            self.p()

    def pbr(self):
        """
        Устанавливает флаг для добавления одного переноса строки.
        """
        if self.p_p == 0:
            self.p_p = 1

    def p(self):
        """
        Устанавливает флаг для добавления двух переносов строки.
        """
        self.p_p = 2

    def soft_br(self):
        """
        Устанавливает флаг для добавления мягкого переноса строки.
        """
        self.pbr()
        self.br_toggle = '  '

    def o(self, data, puredata=0, force=0):
        """
        Выводит данные с учетом форматирования.

        :param data: Данные для вывода.
        :param puredata: Флаг, указывающий на необходимость очистки пробелов.
        :param force: Флаг для принудительного вывода данных.
        """
        if self.abbr_data is not None:
            self.abbr_data += data

        if not self.quiet:
            if options.google_doc:
                lstripped_data = data.lstrip()
                if self.drop_white_space and not (self.pre or self.code):
                   data = lstripped_data
                if lstripped_data != '':
                   self.drop_white_space = 0
            if puredata and not self.pre:
                data = re.sub(r'\s+', ' ', data)
                if data and data[0] == ' ':
                    self.space = 1
                    data = data[1:]
            if not data and not force:
                return

            if self.startpre:
                self.startpre = 0

            bq = (">" * self.blockquote)
            if not (force and data and data[0] == ">") and self.blockquote:
                bq += " "

            if self.pre:
                bq += "    "
                data = data.replace("\n", "\n" + bq)

            if self.start:
                self.space = 0
                self.p_p = 0
                self.start = 0

            if force == 'end':
                self.p_p = 0
                self.out("\n")
                self.space = 0

            if self.p_p:
                self.out((self.br_toggle + '\n' + bq) * self.p_p)
                self.space = 0
                self.br_toggle = ''

            if self.space:
                if not self.lastWasNL:
                    self.out(' ')
                self.space = 0

            if self.a and ((self.p_p == 2 and LINKS_EACH_PARAGRAPH) or force == "end"):
                if force == "end":
                    self.out("\n")

                newa = []
                for link in self.a:
                    if self.outcount > link['outcount']:
                        self.out("   [" + str(link['count']) + "]: " +
                                 urlparse.urljoin(self.baseurl, link['href']))