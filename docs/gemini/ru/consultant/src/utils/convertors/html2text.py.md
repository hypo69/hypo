# Анализ кода модуля `html2text.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки, что облегчает понимание и модификацию.
    - Присутствуют комментарии, объясняющие назначение отдельных частей кода.
    - Реализована поддержка различных видов форматирования HTML в Markdown, включая заголовки, списки, ссылки и изображения.
    - Есть возможность настройки параметров конвертации, таких как ширина строки и стиль списка.
- Минусы
    - Не все комментарии оформлены в соответствии с reStructuredText.
    - Используется  `try-except` без логирования ошибок.
    - Некоторые места кода не соответствуют стандарту PEP8 (например, длинные строки, использование `has_key` вместо `in`).
    - Использование `sys.stdout.write` и `sys.stdout.buffer.write` для вывода в консоль можно заменить на более универсальный подход.
    - Использование `if hasattr(x, 'has_key'): return x.has_key(y)` вместо `if y in x`

**Рекомендации по улучшению**

1.  **Документация:**
    -   Переписать все комментарии и docstring в формате reStructuredText (RST), включая описание модуля, функций, методов и переменных.
    -   Добавить примеры использования функций и классов в docstring.
2.  **Логирование:**
    -   Использовать `from src.logger.logger import logger` для логирования ошибок вместо стандартных `try-except`.
    -   Добавить логирование для критических операций, таких как чтение файлов и обработка данных.
3.  **Обработка данных:**
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
4.  **Рефакторинг:**
    -   Заменить устаревший метод `has_key` на оператор `in`.
    -   Убрать избыточные проверки на `True` и `False`.
    -   Разбить длинные функции на более мелкие и управляемые блоки.
    -   Переименовать переменные и функции в соответствии с PEP8 (например, `file_` -> `file_path`).
    -   Избавиться от избыточного использования `if/else`, где можно использовать тернарные операторы или другие более краткие выражения.
    -  Убрать избыточное использование `try/except NameError` в блоках `charref` и `entityref`.
    -  Убрать устаревший коментарий  `#attrs = fixattrs(attrs)`
    - Использовать `os.path.join` для конкатенации путей.
    - Использовать более унифицированный подход для вывода данных, например, с помощью функции `print`.

**Оптимизированный код**

```python
"""
Модуль для конвертации HTML в Markdown
=========================================================================================

Этот модуль преобразует HTML-документы в Markdown-форматированный текст.
Поддерживает различные HTML-теги, включая заголовки, списки, ссылки и изображения.
Также позволяет настраивать параметры конвертации, такие как ширина строки и стиль списка.

Пример использования
--------------------

.. code-block:: python

    from src.utils.convertors.html2text import html2text
    
    html_text = "<h1>Заголовок</h1><p>Параграф с <b>жирным</b> текстом.</p>"
    markdown_text = html2text(html_text)
    print(markdown_text)

"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import html.entities as htmlentitydefs
import urllib.parse as urlparse
import html.parser as HTMLParser
import urllib.request as urllib
import optparse
import re
import sys
import codecs
import os
from textwrap import wrap
from src.logger.logger import logger #  импортируем logger
from typing import Any

# Use Unicode characters instead of their ascii psuedo-replacements
UNICODE_SNOB = 0

# Put the links after each paragraph instead of at the end.
LINKS_EACH_PARAGRAPH = 0

# Wrap long lines at position. 0 for no wrapping. (Requires Python 2.3.)
BODY_WIDTH = 78

# Don't show internal links (href="#local-anchor") -- corresponding link targets
# won't be visible in the plain text file anyway.
SKIP_INTERNAL_LINKS = True

# Use inline, rather than reference, formatting for images and links
INLINE_LINKS = True

# Number of pixels Google indents nested lists
GOOGLE_LIST_INDENT = 36

IGNORE_ANCHORS = False
IGNORE_IMAGES = False

MODE = 'dev'

### Entity Nonsense ###

def name2cp(k: str) -> int:
    """
    Преобразует имя HTML-сущности в кодовую точку Unicode.

    :param k: Имя HTML-сущности.
    :return: Кодовая точка Unicode.
    :raises KeyError: Если имя сущности не найдено.
    """
    if k == 'apos':
        return ord("'")
    if hasattr(htmlentitydefs, "name2codepoint"):  # requires Python 2.3
        return htmlentitydefs.name2codepoint[k]
    else:
        k = htmlentitydefs.entitydefs[k]
        if k.startswith("&#") and k.endswith(";"):
            return int(k[2:-1])  # not in latin-1
        return ord(codecs.latin_1_decode(k)[0])


unifiable = {'rsquo': "'", 'lsquo': "'", 'rdquo': '"', 'ldquo': '"',
             'copy': '(C)', 'mdash': '--', 'nbsp': ' ', 'rarr': '->', 'larr': '<-', 'middot': '*',
             'ndash': '-', 'oelig': 'oe', 'aelig': 'ae',
             'agrave': 'a', 'aacute': 'a', 'acirc': 'a', 'atilde': 'a', 'auml': 'a', 'aring': 'a',
             'egrave': 'e', 'eacute': 'e', 'ecirc': 'e', 'euml': 'e',
             'igrave': 'i', 'iacute': 'i', 'icirc': 'i', 'iuml': 'i',
             'ograve': 'o', 'oacute': 'o', 'ocirc': 'o', 'otilde': 'o', 'ouml': 'o',
             'ugrave': 'u', 'uacute': 'u', 'ucirc': 'u', 'uuml': 'u',
             'lrm': '', 'rlm': ''}

unifiable_n = {name2cp(k): v for k, v in unifiable.items()}


def charref(name: str) -> str:
    """
    Преобразует числовую ссылку на символ в символ Unicode.

    :param name: Числовая ссылка (например, "x20" или "160").
    :return: Символ Unicode.
    """
    if name[0] in ['x', 'X']:
        c = int(name[1:], 16)
    else:
        c = int(name)

    if not UNICODE_SNOB and c in unifiable_n:
        return unifiable_n[c]
    else:
        return chr(c)


def entityref(c: str) -> str:
    """
    Преобразует именованную ссылку на сущность в символ Unicode.

    :param c: Имя сущности.
    :return: Символ Unicode или исходная ссылка, если сущность не найдена.
    """
    if not UNICODE_SNOB and c in unifiable:
        return unifiable[c]
    try:
        return chr(name2cp(c))
    except KeyError:
         return "&" + c + ';'

def replaceEntities(s: re.Match) -> str:
    """
    Заменяет HTML-сущности на соответствующие символы.

    :param s: Объект re.Match, содержащий найденную сущность.
    :return: Символ Unicode, соответствующий сущности.
    """
    s = s.group(1)
    if s[0] == "#":
        return charref(s[1:])
    else:
        return entityref(s)


r_unescape = re.compile(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));")


def unescape(s: str) -> str:
    """
    Удаляет HTML-сущности из строки.

    :param s: Строка, содержащая HTML-сущности.
    :return: Строка без HTML-сущностей.
    """
    return r_unescape.sub(replaceEntities, s)

### End Entity Nonsense ###


def onlywhite(line: str) -> bool:
    """
    Проверяет, состоит ли строка только из пробельных символов.

    :param line: Строка для проверки.
    :return: True, если строка состоит только из пробельных символов, иначе False.
    """
    for c in line:
        if c != ' ' and c != '\t':
            return False
    return True


def optwrap(text: str) -> str:
    """
    Выполняет перенос строк в тексте.

    :param text: Текст для переноса.
    :return: Текст с переносом строк.
    """
    if not BODY_WIDTH:
        return text

    assert wrap, "Requires Python 2.3."
    result = ''
    newlines = 0
    for para in text.split("\n"):
        if para:
            if para[0] not in [' ', '-', '*']:
                for line in wrap(para, BODY_WIDTH):
                    result += line + "\n"
                result += "\n"
                newlines = 2
            elif not onlywhite(para):
                result += para + "\n"
                newlines = 1
        elif newlines < 2:
            result += "\n"
            newlines += 1
    return result


def hn(tag: str) -> int:
    """
    Определяет уровень заголовка по тегу.

    :param tag: HTML-тег (например, "h1", "h2").
    :return: Уровень заголовка (1-9) или 0, если тег не является заголовком.
    """
    if tag.startswith('h') and len(tag) == 2:
        try:
            n = int(tag[1])
            if 1 <= n <= 9:
                return n
        except ValueError:
            return 0
    return 0


def dumb_property_dict(style: str) -> dict:
    """
    Создает словарь CSS-свойств из строки.

    :param style: Строка CSS-стилей.
    :return: Словарь CSS-свойств.
    """
    return dict(
        (x.strip(), y.strip())
        for x, y in (z.split(':', 1) for z in style.split(';') if ':' in z)
    )


def dumb_css_parser(data: str) -> dict:
    """
    Разбирает CSS-стили и возвращает словарь селекторов.

    :param data: Строка CSS-стилей.
    :return: Словарь CSS-селекторов, где каждый селектор содержит словарь свойств.
    """
    # remove @import sentences
    import_index = data.find('@import')
    while import_index != -1:
        data = data[:import_index] + data[data.find(';', import_index) + 1:]
        import_index = data.find('@import')

    # parse the css. reverted from dictionary compehension in order to support older pythons
    elements = [x.split('{') for x in data.split('}') if '{' in x.strip()]
    elements = dict((a.strip(), dumb_property_dict(b)) for a, b in elements)

    return elements

def element_style(attrs: dict, style_def: dict, parent_style: dict) -> dict:
    """
    Определяет стиль элемента на основе CSS.

    :param attrs: Словарь атрибутов HTML-элемента.
    :param style_def: Словарь определений стилей.
    :param parent_style: Словарь стилей родительского элемента.
    :return: Словарь окончательных стилей элемента.
    """
    style = parent_style.copy()
    if 'class' in attrs:
        for css_class in attrs['class'].split():
            css_style = style_def.get('.' + css_class, {})
            style.update(css_style)
    if 'style' in attrs:
        immediate_style = dumb_property_dict(attrs['style'])
        style.update(immediate_style)
    return style


def google_list_style(style: dict) -> str:
    """
    Определяет, является ли список упорядоченным или неупорядоченным.

    :param style: Словарь CSS-стилей элемента.
    :return: 'ul' для неупорядоченного списка, 'ol' для упорядоченного.
    """
    if 'list-style-type' in style:
        list_style = style['list-style-type']
        if list_style in ['disc', 'circle', 'square', 'none']:
            return 'ul'
    return 'ol'


def google_nest_count(style: dict) -> int:
    """
    Вычисляет уровень вложенности списка Google Docs.

    :param style: Словарь CSS-стилей элемента.
    :return: Уровень вложенности списка.
    """
    if 'margin-left' in style:
        try:
            return int(style['margin-left'][:-2]) // GOOGLE_LIST_INDENT
        except ValueError:
            return 0
    return 0


def google_has_height(style: dict) -> bool:
    """
    Проверяет, определен ли атрибут 'height' в стилях элемента.

    :param style: Словарь CSS-стилей элемента.
    :return: True, если атрибут 'height' определен, иначе False.
    """
    return 'height' in style


def google_text_emphasis(style: dict) -> list:
    """
    Извлекает список всех модификаторов выделения текста.

    :param style: Словарь CSS-стилей элемента.
    :return: Список модификаторов выделения текста.
    """
    emphasis = []
    if 'text-decoration' in style:
        emphasis.append(style['text-decoration'])
    if 'font-style' in style:
        emphasis.append(style['font-style'])
    if 'font-weight' in style:
        emphasis.append(style['font-weight'])
    return emphasis


def google_fixed_width_font(style: dict) -> bool:
    """
    Проверяет, определен ли шрифт фиксированной ширины.

    :param style: Словарь CSS-стилей элемента.
    :return: True, если шрифт фиксированной ширины, иначе False.
    """
    font_family = style.get('font-family', '')
    return font_family in ['Courier New', 'Consolas']


def list_numbering_start(attrs: dict) -> int:
    """
    Извлекает начальный номер списка из атрибутов.

    :param attrs: Словарь атрибутов HTML-элемента.
    :return: Начальный номер списка (на 1 меньше фактического).
    """
    return int(attrs.get('start', 1)) - 1


class _html2text(HTMLParser.HTMLParser):
    """
    Класс для преобразования HTML в Markdown.
    
    :param out: Функция для вывода текста. Если None, используется self.outtextf.
    :param baseurl: Базовый URL для ссылок.
    """
    def __init__(self, out=None, baseurl=''):
        HTMLParser.HTMLParser.__init__(self)

        self.out = out if out else self.outtextf
        self.outtextlist = [] # empty list to store output characters before they are  "joined"
        self.outtext = ''
        self.quiet = 0
        self.p_p = 0 # number of newline character to print before next output
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
        self.abbr_title = None  # current abbreviation definition
        self.abbr_data = None # last inner HTML (for abbr being defined)
        self.abbr_list = {}  # stack of abbreviations to write later
        self.baseurl = baseurl

        if options.google_doc:
            del unifiable_n[name2cp('nbsp')]
            unifiable['nbsp'] = '&nbsp_place_holder;'


    def feed(self, data: str):
        """
        Обрабатывает HTML-данные.

        :param data: HTML-данные для обработки.
        """
        data = data.replace("</' + 'script>", "</ignore>")
        HTMLParser.HTMLParser.feed(self, data)

    def outtextf(self, s: str):
        """
        Добавляет текст в список вывода.

        :param s: Строка для добавления.
        """
        self.outtextlist.append(s)
        if s:
            self.lastWasNL = s[-1] == '\n'


    def close(self) -> str:
        """
        Завершает обработку и возвращает результат.

        :return: Markdown-текст.
        """
        HTMLParser.HTMLParser.close(self)

        self.pbr()
        self.o('', 0, 'end')
        self.outtext = ''.join(self.outtextlist)

        if options.google_doc:
            self.outtext = self.outtext.replace('&nbsp_place_holder;', ' ')
        return self.outtext


    def handle_charref(self, c: str):
        """
        Обрабатывает числовые ссылки на символы.

        :param c: Числовая ссылка на символ.
        """
        self.o(charref(c), 1)


    def handle_entityref(self, c: str):
        """
        Обрабатывает именованные ссылки на сущности.

        :param c: Именованная ссылка на сущность.
        """
        self.o(entityref(c), 1)


    def handle_starttag(self, tag: str, attrs: list):
        """
        Обрабатывает открывающие теги.

        :param tag: Имя тега.
        :param attrs: Список атрибутов тега.
        """
        self.handle_tag(tag, attrs, 1)


    def handle_endtag(self, tag: str):
        """
        Обрабатывает закрывающие теги.

        :param tag: Имя тега.
        """
        self.handle_tag(tag, None, 0)


    def previousIndex(self, attrs: dict) -> int | None:
        """
        Возвращает индекс набора атрибутов (ссылки) в списке self.a.

        :param attrs: Словарь атрибутов для поиска.
        :return: Индекс атрибутов в списке self.a или None, если не найдено.
        """
        if 'href' not in attrs:
            return None

        for i, a in enumerate(self.a):
            if a.get('href') == attrs.get('href'):
                if 'title' in a or 'title' in attrs:
                    if a.get('title') == attrs.get('title'):
                        return i
                else:
                    return i
        return None

    def drop_last(self, n_letters: int):
        """
        Удаляет последние символы из вывода.

        :param n_letters: Количество символов для удаления.
        """
        if not self.quiet:
           self.outtext = self.outtext[:-n_letters]

    def handle_emphasis(self, start: int, tag_style: dict, parent_style: dict):
        """
        Обрабатывает выделение текста.

        :param start: 1, если это открывающий тег, 0 - если закрывающий.
        :param tag_style: CSS-стили текущего тега.
        :param parent_style: CSS-стили родительского тега.
        """
        tag_emphasis = google_text_emphasis(tag_style)
        parent_emphasis = google_text_emphasis(parent_style)

        # handle Google's text emphasis
        strikethrough = 'line-through' in tag_emphasis and options.hide_strikethrough
        bold = 'bold' in tag_emphasis and 'bold' not in parent_emphasis
        italic = 'italic' in tag_emphasis and 'italic' not in parent_emphasis
        fixed = google_fixed_width_font(tag_style) and not google_fixed_width_font(parent_style) and not self.pre

        if start:
            # crossed-out text must be handled before other attributes
            # in order not to output qualifiers unnecessarily
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
                # there must not be whitespace before closing emphasis mark
                self.emphasis -= 1
                self.space = 0
                self.outtext = self.outtext.rstrip()
            if fixed:
                if self.drop_white_space:
                    # empty emphasis, drop it
                    self.drop_last(1)
                    self.drop_white_space -= 1
                else:
                    self.o('`')
                self.code = False
            if bold:
                if self.drop_white_space:
                    # empty emphasis, drop it
                    self.drop_last(2)
                    self.drop_white_space -= 1
                else:
                    self.o("**")
            if italic:
                if self.drop_white_space:
                    # empty emphasis, drop it
                    self.drop_last(1)
                    self.drop_white_space -= 1
                else:
                    self.o("_")
            # space is only allowed after *all* emphasis marks
            if (bold or italic) and not self.emphasis:
                self.o(" ")
            if strikethrough:
                self.quiet -= 1

    def handle_tag(self, tag: str, attrs: list | None, start: int):
        """
        Обрабатывает HTML-тег.

        :param tag: Имя тега.
        :param attrs: Словарь атрибутов тега.
        :param start: 1, если это открывающий тег, 0 - если закрывающий.
        """
        if attrs is None:
            attrs = {}
        else:
            attrs = dict(attrs)

        if options.google_doc:
            # the attrs parameter is empty for a closing tag. in addition, we
            # need the attributes of the parent nodes in order to get a
            # complete style description for the current element. we assume
            # that google docs export well formed html.
            parent_style = {}
            if start:
                if self.tag_stack:
                  parent_style = self.tag_stack[-1][2]
                tag_style = element_style(attrs, self.style_def, parent_style)
                self.tag_stack.append((tag, attrs, tag_style))
            else:
                if self.tag_stack:
                    dummy, attrs, tag_style = self.tag_stack.pop()
                    if self.tag_stack:
                        parent_style = self.tag_stack[-1][2]

        if hn(tag):
            self.p()
            if start:
                self.inheader = True
                self.o(hn(tag) * "#" + ' ')
            else:
                self.inheader = False
                return  # prevent redundant emphasis marks on headers

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
            self.quiet = 0  # sites like 9rules.com never close <head>

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
                self.o("<" + tag + ">")
            else:
                self.o("</" + tag + ">")

        if options.google_doc:
            if not self.inheader:
                # handle some font attributes, but leave headers clean
                self.handle_emphasis(start, tag_style, parent_style)

        if tag == "code" and not self.pre:
            self.o('`')  # TODO: `` `this` ``
        if tag == "abbr":
            if start:
                self.abbr_title = None
                self.abbr_data = ''
                if 'title' in attrs:
                    self.abbr_title = attrs['title']
            else:
                if self.abbr_title is not None:
                    self.abbr_list[self.abbr_data] = self.abbr_title
                    self.abbr_title = None
                self.abbr_data = ''

        if tag == "a" and not IGNORE_ANCHORS:
            if start:
                if 'href' in attrs and not (SKIP_INTERNAL_LINKS and attrs['href'].startswith('#')):
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
            if 'src' in attrs:
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
            # Google Docs create sub lists as top level lists
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
                self.o("  " * nest_count)  # TODO: line up <ol><li>s > 9 correctly.
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
        Добавляет один или несколько разрывов строки.
        """
        if self.p_p == 0:
            self.p_p = 1


    def p(self):
        """
        Добавляет два разрыва строки.
        """
        self.p_p = 2


    def soft_br(self):
        """
        Добавляет мягкий разрыв строки.
        """
        self.pbr()
        self.br_toggle = '  '

    def o(self, data: str, puredata: int = 0, force: Any = 0):
        """
         Добавляет текст в вывод, выполняет форматирование.

         :param data: Строка для вывода.
         :param puredata: Флаг, указывающий, нужно ли очищать пробелы.
         :param force: Флаг, указывающий необходимость принудительного вывода.
         """
        if self.abbr_data is not None:
           self.abbr_data += data

        if not self.quiet:
            if options.google_doc:
                # prevent white space immediately after 'begin emphasis' marks ('**' and '_')
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
                # self.out(" :") #TODO: not output when already one there
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
                # It's the end.
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