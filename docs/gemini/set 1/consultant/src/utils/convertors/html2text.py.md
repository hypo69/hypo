# Анализ кода модуля html2text

**Качество кода**
8
 -  Плюсы
        - Код выполняет преобразование HTML в Markdown, включая обработку различных тегов, стилей и сущностей.
        - Присутствует поддержка Google Docs HTML.
        - Используются регулярные выражения для обработки текста и сущностей.
        - Есть возможность настройки ширины вывода и символа списка.
 -  Минусы
    -  Много глобальных переменных, что может затруднить понимание и модификацию кода.
    -  Сложная логика обработки стилей и вложенных списков, что усложняет отладку.
    -  Недостаточно документации в формате RST.
    -  Не везде используется логирование ошибок.
    -  Не используется `j_loads` или `j_loads_ns` для загрузки файлов.
    -  Не все комментарии оформлены в стиле RST.

**Рекомендации по улучшению**
1.  Добавить docstring в формате reStructuredText к модулю, классам и функциям.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Улучшить обработку исключений с помощью `logger.error` вместо общих `try-except`.
4.  Избегать избыточных проверок условий.
5.  Рефакторить функции для повышения читаемости и поддерживаемости кода.
6.  Использовать `j_loads` или `j_loads_ns` для чтения файлов, если необходимо.
7.  Сделать код более модульным, выделив отдельные функции или классы.
8.  Переписать все комментарии после `#` с подробным описанием следующего блока кода.

**Оптимизированный код**
```python
"""
Модуль для конвертации HTML в Markdown.
=========================================================================================

Этот модуль предоставляет функциональность для преобразования HTML-документов
в Markdown-форматированный текст. Он обрабатывает различные HTML-теги, стили
и сущности, обеспечивая корректное отображение структуры и контента в Markdown.

Модуль поддерживает преобразование HTML, сгенерированного Google Docs, и имеет
настройки для ширины вывода и символов списка.

Пример использования
--------------------

.. code-block:: python

    from src.utils.convertors.html2text import html2text
    html_content = "<html><body><h1>Заголовок</h1><p>Текст</p></body></html>"
    markdown_content = html2text(html_content)
    print(markdown_content)

"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import html.entities as htmlentitydefs
import urllib.parse as urlparse
import html.parser as HTMLParser
import urllib.request as urllib
import optparse, re, sys, codecs, types
from textwrap import wrap
from src.logger.logger import logger # импортируем logger




__version__ = "3.1"
__author__ = "Aaron Swartz (me@aaronsw.com)"
__copyright__ = "(C) 2004-2008 Aaron Swartz. GNU GPL 3."
__contributors__ = ["Martin \'Joey\' Schulze", "Ricardo Reyes", "Kevin Jay North"]

# TODO:
#   Support decoded entities with unifiable.


try:
    True
except NameError:
    setattr(__builtins__, 'True', 1)
    setattr(__builtins__, 'False', 0)

def has_key(x, y):
    """
    Проверяет, содержит ли словарь или объект ключ.
    
    :param x: Словарь или объект для проверки.
    :param y: Ключ для поиска.
    :return: True, если ключ присутствует, иначе False.
    """
    if hasattr(x, 'has_key'):
        return x.has_key(y)
    else:
        return y in x


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

### Entity Nonsense ###

def name2cp(k):
    """
    Преобразует имя HTML-сущности в кодовую точку.
    
    :param k: Имя сущности.
    :return: Кодовая точка Unicode.
    """
    if k == 'apos':
        return ord("\'")
    if hasattr(htmlentitydefs, "name2codepoint"): # requires Python 2.3
        return htmlentitydefs.name2codepoint[k]
    else:
        k = htmlentitydefs.entitydefs[k]
        if k.startswith("&#") and k.endswith(";"):
             return int(k[2:-1]) # not in latin-1
        return ord(codecs.latin_1_decode(k)[0])


unifiable = {'rsquo':"'", 'lsquo':"'", 'rdquo':'"', 'ldquo':'"',
'copy':'(C)', 'mdash':'--', 'nbsp':' ', 'rarr':'->', 'larr':'<-', 'middot':'*',
'ndash':'-', 'oelig':'oe', 'aelig':'ae',
'agrave':'a', 'aacute':'a', 'acirc':'a', 'atilde':'a', 'auml':'a', 'aring':'a',
'egrave':'e', 'eacute':'e', 'ecirc':'e', 'euml':'e',
'igrave':'i', 'iacute':'i', 'icirc':'i', 'iuml':'i',
'ograve':'o', 'oacute':'o', 'ocirc':'o', 'otilde':'o', 'ouml':'o',
'ugrave':'u', 'uacute':'u', 'ucirc':'u', 'uuml':'u',
'lrm':'', 'rlm':''}

unifiable_n = {}

for k in unifiable.keys():
    unifiable_n[name2cp(k)] = unifiable[k]

def charref(name):
    """
    Преобразует символьную ссылку в Unicode-символ.
    
    :param name: Символьная ссылка.
    :return: Unicode-символ.
    """
    if name[0] in ['x','X']:
        c = int(name[1:], 16)
    else:
        c = int(name)
    
    if not UNICODE_SNOB and c in unifiable_n.keys():
        return unifiable_n[c]
    else:
        try:
            return chr(c)
        except NameError: #Python3
            return chr(c)

def entityref(c):
    """
    Преобразует ссылку на сущность в Unicode-символ.

    :param c: Ссылка на сущность.
    :return: Unicode-символ или исходная ссылка, если преобразование невозможно.
    """
    if not UNICODE_SNOB and c in unifiable.keys():
        return unifiable[c]
    else:
        try:
            name2cp(c)
        except KeyError:
            return "&" + c + ';'
        else:
            try:
                return chr(name2cp(c))
            except NameError: #Python3
                return chr(name2cp(c))

def replaceEntities(s):
    """
    Заменяет HTML-сущности в строке.
    
    :param s: Объект регулярного выражения.
    :return: Замененная строка.
    """
    s = s.group(1)
    if s[0] == "#":
        return charref(s[1:])
    else:
        return entityref(s)

r_unescape = re.compile(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));")
def unescape(s):
    """
    Удаляет HTML-сущности из строки.
    
    :param s: Строка для обработки.
    :return: Строка без HTML-сущностей.
    """
    return r_unescape.sub(replaceEntities, s)

### End Entity Nonsense ###

def onlywhite(line):
    """
    Проверяет, состоит ли строка только из пробельных символов.
    
    :param line: Строка для проверки.
    :return: True, если строка содержит только пробелы, иначе False.
    """
    for c in line:
        if c is not ' ' and c is not '  ':
            return c is ' '
    return line

def optwrap(text):
    """
    Оборачивает абзацы в предоставленном тексте.
    
    :param text: Текст для оборачивания.
    :return: Обернутый текст.
    """
    if not BODY_WIDTH:
        return text
    
    assert wrap, "Requires Python 2.3."
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
    Определяет уровень заголовка HTML-тега.
    
    :param tag: HTML-тег.
    :return: Уровень заголовка или 0, если тег не является заголовком.
    """
    if tag[0] == 'h' and len(tag) == 2:
        try:
            n = int(tag[1])
            if n in range(1, 10):
                return n
        except ValueError:
            return 0

def dumb_property_dict(style):
    """
    Преобразует строку CSS-стилей в словарь.
    
    :param style: Строка CSS-стилей.
    :return: Словарь атрибутов CSS.
    """
    return dict([(x.strip(), y.strip()) for x, y in [z.split(':', 1) for z in style.split(';') if ':' in z]])

def dumb_css_parser(data):
    """
    Разбирает CSS-данные в словарь селекторов и атрибутов.
    
    :param data: CSS-данные.
    :return: Словарь CSS-селекторов и атрибутов.
    """
    # remove @import sentences
    importIndex = data.find('@import')
    while importIndex != -1:
        data = data[0:importIndex] + data[data.find(';', importIndex) + 1:]
        importIndex = data.find('@import')

    # parse the css. reverted from dictionary compehension in order to support older pythons
    elements =  [x.split('{') for x in data.split('}') if '{' in x.strip()]
    elements = dict([(a.strip(), dumb_property_dict(b)) for a, b in elements])

    return elements

def element_style(attrs, style_def, parent_style):
    """
    Вычисляет окончательные CSS-стили элемента.
    
    :param attrs: Атрибуты элемента.
    :param style_def: Словарь CSS-определений.
    :param parent_style: Стили родительского элемента.
    :return: Словарь стилей элемента.
    """
    style = parent_style.copy()
    if 'class' in attrs:
        for css_class in attrs['class'].split():
            css_style = style_def['.' + css_class]
            style.update(css_style)
    if 'style' in attrs:
        immediate_style = dumb_property_dict(attrs['style'])
        style.update(immediate_style)
    return style

def google_list_style(style):
    """
    Определяет тип списка (упорядоченный или неупорядоченный) из стилей Google Docs.
    
    :param style: Словарь стилей.
    :return: 'ul' для неупорядоченного списка, 'ol' для упорядоченного.
    """
    if 'list-style-type' in style:
        list_style = style['list-style-type']
        if list_style in ['disc', 'circle', 'square', 'none']:
            return 'ul'
    return 'ol'

def google_nest_count(style):
    """
    Вычисляет уровень вложенности списка Google Docs.
    
    :param style: Словарь стилей.
    :return: Уровень вложенности.
    """
    nest_count = 0
    if 'margin-left' in style:
        nest_count = int(style['margin-left'][:-2]) / GOOGLE_LIST_INDENT
    return nest_count

def google_has_height(style):
    """
    Проверяет, задан ли атрибут 'height' в стилях Google Docs.
    
    :param style: Словарь стилей.
    :return: True, если атрибут 'height' задан, иначе False.
    """
    if 'height' in style:
        return True
    return False

def google_text_emphasis(style):
    """
    Извлекает список модификаторов выделения текста из стилей Google Docs.
    
    :param style: Словарь стилей.
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

def google_fixed_width_font(style):
    """
    Проверяет, использует ли элемент шрифт с фиксированной шириной в Google Docs.
    
    :param style: Словарь стилей.
    :return: True, если используется шрифт с фиксированной шириной, иначе False.
    """
    font_family = ''
    if 'font-family' in style:
        font_family = style['font-family']
    if 'Courier New' == font_family or 'Consolas' == font_family:
        return True
    return False

def list_numbering_start(attrs):
    """
    Извлекает начальное значение нумерации из атрибутов списка.
    
    :param attrs: Атрибуты элемента.
    :return: Начальное значение нумерации или 0, если атрибут 'start' не задан.
    """
    if 'start' in attrs:
        return int(attrs['start']) - 1
    else:
        return 0

class _html2text(HTMLParser.HTMLParser):
    """
    Класс для преобразования HTML в Markdown.

    :param out: Функция для вывода текста. Если None, используется self.outtextf.
    :param baseurl: Базовый URL для обработки относительных ссылок.

    :ivar outtextlist: Список для хранения символов вывода.
    :ivar outtext: Выходной текст.
    :ivar quiet: Флаг для игнорирования вывода.
    :ivar p_p: Количество символов новой строки для печати перед следующим выводом.
    :ivar outcount: Счетчик выведенных символов.
    :ivar start: Флаг начала вывода.
    :ivar space: Флаг пробела.
    :ivar a: Список ссылок.
    :ivar astack: Стек атрибутов ссылок.
    :ivar acount: Счетчик ссылок.
    :ivar list: Список вложенных списков.
    :ivar blockquote: Счетчик цитат.
    :ivar pre: Флаг преформатированного текста.
    :ivar startpre: Флаг начала преформатированного текста.
    :ivar code: Флаг кода.
    :ivar br_toggle: Строка для вставки перед переводом строки.
    :ivar lastWasNL: Флаг последнего символа новой строки.
    :ivar lastWasList: Флаг последнего элемента списка.
    :ivar style: Счетчик стилей.
    :ivar style_def: Словарь стилей.
    :ivar tag_stack: Стек тегов.
    :ivar emphasis: Счетчик выделения текста.
    :ivar drop_white_space: Флаг удаления пробелов.
    :ivar inheader: Флаг нахождения внутри заголовка.
    :ivar abbr_title: Определение текущего сокращения.
    :ivar abbr_data: Последний внутренний HTML для сокращения.
    :ivar abbr_list: Список сокращений для записи позже.
    :ivar baseurl: Базовый URL.
    """
    def __init__(self, out=None, baseurl=''):
        HTMLParser.HTMLParser.__init__(self)
        
        if out is None:
            self.out = self.outtextf
        else:
            self.out = out
        self.outtextlist = [] # empty list to store output characters before they are  "joined"
        try:
            self.outtext = str()
        except NameError: # Python3
            self.outtext = str()
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
        self.lastWasNL = 0
        self.lastWasList = False
        self.style = 0
        self.style_def = {}
        self.tag_stack = []
        self.emphasis = 0
        self.drop_white_space = 0
        self.inheader = False
        self.abbr_title = None # current abbreviation definition
        self.abbr_data = None # last inner HTML (for abbr being defined)
        self.abbr_list = {} # stack of abbreviations to write later
        self.baseurl = baseurl

        if options.google_doc:
            del unifiable_n[name2cp('nbsp')]
            unifiable['nbsp'] = '&nbsp_place_holder;'
    
    def feed(self, data):
        """
        Обрабатывает HTML-данные.

        :param data: HTML-данные.
        """
        data = data.replace("</' + 'script>", "</ignore>")
        HTMLParser.HTMLParser.feed(self, data)
    
    def outtextf(self, s):
        """
        Добавляет текст в список вывода.

        :param s: Текст для добавления.
        """
        self.outtextlist.append(s)
        if s:
            self.lastWasNL = s[-1] == '\n'
    
    def close(self):
        """
        Завершает обработку HTML и возвращает полученный текст.

        :return: Преобразованный текст в формате Markdown.
        """
        HTMLParser.HTMLParser.close(self)
        
        self.pbr()
        self.o('', 0, 'end')

        self.outtext = self.outtext.join(self.outtextlist)
        
        if options.google_doc:
            self.outtext = self.outtext.replace('&nbsp_place_holder;', ' ')
        
        return self.outtext
        
    def handle_charref(self, c):
        """
        Обрабатывает символьную ссылку.

        :param c: Символьная ссылка.
        """
        self.o(charref(c), 1)

    def handle_entityref(self, c):
        """
        Обрабатывает ссылку на сущность.

        :param c: Ссылка на сущность.
        """
        self.o(entityref(c), 1)
            
    def handle_starttag(self, tag, attrs):
        """
        Обрабатывает начальный тег.

        :param tag: Имя тега.
        :param attrs: Атрибуты тега.
        """
        self.handle_tag(tag, attrs, 1)
    
    def handle_endtag(self, tag):
        """
        Обрабатывает конечный тег.
        
        :param tag: Имя тега.
        """
        self.handle_tag(tag, None, 0)
        
    def previousIndex(self, attrs):
        """
        Ищет индекс ссылки в списке ссылок.

        :param attrs: Атрибуты ссылки.
        :return: Индекс ссылки или None, если не найдена.
        """
        if not has_key(attrs, 'href'):
            return

        i = -1
        for a in self.a:
            i += 1
            match = 0
            
            if has_key(a, 'href') and a['href'] == attrs['href']:
                if has_key(a, 'title') or has_key(attrs, 'title'):
                    if (has_key(a, 'title') and has_key(attrs, 'title') and
                        a['title'] == attrs['title']):
                        match = True
                else:
                    match = True
            
            if match:
                 return i

    def drop_last(self, nLetters):
        """
        Удаляет последние символы из выходного текста.

        :param nLetters: Количество символов для удаления.
        """
        if not self.quiet:
            self.outtext = self.outtext[:-nLetters]
           
    def handle_emphasis(self, start, tag_style, parent_style):
        """
        Обрабатывает выделение текста.

        :param start: Флаг начала тега.
        :param tag_style: Стили текущего тега.
        :param parent_style: Стили родительского тега.
        """
        tag_emphasis = google_text_emphasis(tag_style)
        parent_emphasis = google_text_emphasis(parent_style)

        # handle Google's text emphasis
        strikethrough =  'line-through' in tag_emphasis and options.hide_strikethrough
        bold = 'bold' in tag_emphasis and not 'bold' in parent_emphasis
        italic = 'italic' in tag_emphasis and not 'italic' in parent_emphasis
        fixed = google_fixed_width_font(tag_style) and not \
                google_fixed_width_font(parent_style) and not self.pre

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

    def handle_tag(self, tag, attrs, start):
        """
        Обрабатывает тег HTML.
        
        :param tag: Имя тега.
        :param attrs: Атрибуты тега.
        :param start: Флаг начала тега.
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
                dummy, attrs, tag_style = self.tag_stack.pop()
                if self.tag_stack:
                    parent_style = self.tag_stack[-1][2]

        if hn(tag):
            self.p()
            if start:
                self.inheader = True
                self.o(hn(tag)*"#" + ' ')
            else:
                self.inheader = False
                return # prevent redundant emphasis marks on headers

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
            self.quiet = 0 # sites like 9rules.com never close <head>
        
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
                # handle some font attributes, but leave headers clean
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
                if self.abbr_title is not None:
                    self.abbr_list[self.abbr_data] = self.abbr_title
                    self.abbr_title = None
                self.abbr_data = ''
        
        if tag == "a" and not IGNORE_ANCHORS:
            if start:
                if has_key(attrs, 'href') and not (SKIP_INTERNAL_LINKS and attrs['href'].startswith('#')):
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
                    self.o("]("+ attrs['href'] +")")
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
                    self.o("]["+ str(attrs['count']) +"]")
        
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
                self.list.append({'name':list_style, 'num':numbering_start})
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
                     li = {'name':'ul', 'num':0}
                if options.google_doc:
                    nest_count = google_nest_count(tag_style)
                else:
                    nest_count = len(self.list)
                self.o("  " * nest_count)
                if li['name'] == "ul":
                    self.o(options.ul_item_mark + " ")
                elif li['name'] == "ol":
                    li['num'] += 1
                    self.o(str(li['num'])+". ")
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
        Добавляет символ новой строки, если необходимо.
        """
        if self.p_p == 0:
            self.p_p = 1

    def p(self):
        """
        Добавляет два символа новой строки.
        """
        self.p_p = 2

    def soft_br(self):
        """
        Добавляет мягкий перенос строки.
        """
        self.pbr()
        self.br_toggle = '  '
    
    def o(self, data, puredata=0, force=0):
        """
        Выводит данные, обрабатывая пробелы и отступы.
        
        :param data: Данные для вывода.
        :param puredata: Флаг обработки пробелов.
        :param force: Флаг принудительного вывода.
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
                data = re.sub('\