### Анализ кода модуля `html2text`

**Качество кода**:
- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Код выполняет свою основную задачу - преобразование HTML в Markdown.
    - Присутствует поддержка различных HTML-тегов и стилей.
    - Есть возможность настройки параметров преобразования через командную строку.
- **Минусы**:
    -  Используются двойные кавычки для строк, что не соответствует стандартам.
    - Код содержит устаревшие конструкции, несовместимые с Python 3 (например, `has_key`, `unicode`).
    - Отсутствует явная обработка исключений, что может привести к сбоям.
    - Комментарии не соответствуют формату RST.
    -  Импорт `logger` не стандартизирован.
    - Некоторые функции не имеют документации.
    -  Используется `sys.stdout.write`, что может вызвать проблемы с кодировкой.
    -  Не используется `j_loads` или `j_loads_ns`.
    - Присутствуют избыточные конструкции try-except.
    - Есть потенциал для улучшения читаемости кода.

**Рекомендации по улучшению**:

1.  **Форматирование строк**: Замените все двойные кавычки на одинарные (`'`) в коде Python, кроме случаев, когда это вывод данных (например, в `print`, `input`, `logger.error`).
2.  **Импорты**:
    -   Упорядочите импорты по алфавиту, разделив на стандартные и пользовательские.
    -   Используйте `from src.logger.logger import logger` для логирования.
3.  **Устаревшие конструкции**:
    - Замените `has_key` на `in`.
    - Замените `unicode()` на `str()`.
4.  **Обработка ошибок**:
    -   Добавьте обработку исключений с использованием `logger.error` вместо `try-except` для более точной информации об ошибках.
5.  **Документация**:
    -   Добавьте **RST**-комментарии для всех функций, классов и методов.
6.  **Улучшение читаемости**:
    -   Разделите длинные строки кода на более короткие для улучшения читаемости.
    -   Используйте более информативные имена переменных и функций.
7.  **Кодировка**:
     -   Используйте `sys.stdout.buffer.write(text)` вместо `sys.stdout.write(text)` для корректной работы с кодировкой.
8.  **Использовать j_loads**:
    -  Заменить все `json.load` на `j_loads` или `j_loads_ns`
9.  **Убрать try-except**:
     - Убрать лишние `try-except` блоки и использовать `logger.error`.

**Оптимизированный код**:
```python
## \file /src/utils/convertors/html2text.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для преобразования HTML в Markdown
=========================================

Модуль содержит функции и класс для преобразования HTML-контента в Markdown-формат.
Он поддерживает различные HTML-теги и стили, а также имеет настройки для обработки
особенностей Google Docs.

Пример использования
----------------------
.. code-block:: python

    from src.utils.convertors.html2text import html2text

    html_content = "<p>Это <b>пример</b> HTML-кода.</p>"
    markdown_content = html2text(html_content)
    print(markdown_content)
    # Output: "Это **пример** HTML-кода.\n\n"

"""
import codecs
import html.entities as htmlentitydefs
import html.parser as HTMLParser
import optparse
import re
import sys
import types
import urllib.parse as urlparse
import urllib.request as urllib
from textwrap import wrap

from src.logger import logger # Изменен импорт
# from src.utils.jjson import j_loads  # не используется

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
def name2cp(key: str) -> int:
    """
    Преобразует имя HTML-сущности в кодовую точку Unicode.

    :param key: Имя HTML-сущности.
    :type key: str
    :return: Кодовая точка Unicode.
    :rtype: int
    """
    if key == 'apos':
        return ord('\'')
    if hasattr(htmlentitydefs, 'name2codepoint'): # requires Python 2.3
        return htmlentitydefs.name2codepoint[key]
    else:
        key = htmlentitydefs.entitydefs[key]
        if key.startswith('&#') and key.endswith(';'):
            return int(key[2:-1]) # not in latin-1
        return ord(codecs.latin_1_decode(key)[0])

unifiable = {'rsquo':'\'', 'lsquo':'\'', 'rdquo':'"', 'ldquo':'"',
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

def charref(name: str) -> str:
    """
    Преобразует числовую ссылку на символ в символ Unicode.

    :param name: Числовая ссылка на символ.
    :type name: str
    :return: Символ Unicode.
    :rtype: str
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
        except NameError: # Python3
            return chr(c)

def entityref(c: str) -> str:
    """
    Преобразует именованную ссылку на символ в символ Unicode.

    :param c: Именованная ссылка на символ.
    :type c: str
    :return: Символ Unicode.
    :rtype: str
    """
    if not UNICODE_SNOB and c in unifiable.keys():
        return unifiable[c]
    else:
        try:
            name2cp(c)
        except KeyError:
            return '&' + c + ';'
        else:
            try:
                return chr(name2cp(c))
            except NameError: #Python3
                return chr(name2cp(c))

def replaceEntities(s: re.Match) -> str:
    """
    Заменяет HTML-сущности на соответствующие символы.

    :param s: Результат поиска регулярного выражения.
    :type s: re.Match
    :return: Замененная строка.
    :rtype: str
    """
    s = s.group(1)
    if s[0] == '#':
        return charref(s[1:])
    else:
        return entityref(s)

r_unescape = re.compile(r'&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));')
def unescape(s: str) -> str:
    """
    Удаляет HTML-сущности из строки.

    :param s: Строка с HTML-сущностями.
    :type s: str
    :return: Строка без HTML-сущностей.
    :rtype: str
    """
    return r_unescape.sub(replaceEntities, s)

### End Entity Nonsense ###

def onlywhite(line: str) -> bool:
    """
    Проверяет, состоит ли строка только из пробельных символов.

    :param line: Строка для проверки.
    :type line: str
    :return: True, если строка состоит только из пробелов, иначе False.
    :rtype: bool
    """
    for c in line:
        if c != ' ' and c != '  ': # исправлено сравнение
            return c == ' '
    return line

def optwrap(text: str) -> str:
    """
    Оборачивает текст по ширине BODY_WIDTH.

    :param text: Текст для обертывания.
    :type text: str
    :return: Обернутый текст.
    :rtype: str
    """
    if not BODY_WIDTH:
        return text

    assert wrap, 'Requires Python 2.3.' # Изменен текст ошибки
    result = ''
    newlines = 0
    for para in text.split('\n'):
        if len(para) > 0:
            if para[0] != ' ' and para[0] != '-' and para[0] != '*':
                for line in wrap(para, BODY_WIDTH):
                    result += line + '\n'
                result += '\n'
                newlines = 2
            else:
                if not onlywhite(para):
                    result += para + '\n'
                    newlines = 1
        else:
            if newlines < 2:
                result += '\n'
                newlines += 1
    return result

def hn(tag: str) -> int:
    """
    Определяет уровень заголовка на основе HTML-тега.

    :param tag: HTML-тег.
    :type tag: str
    :return: Уровень заголовка или 0, если не заголовок.
    :rtype: int
    """
    if tag[0] == 'h' and len(tag) == 2:
        try:
            n = int(tag[1])
            if 1 <= n <= 9: #  изменено условие
                return n
        except ValueError:
            return 0

def dumb_property_dict(style: str) -> dict:
    """
    Разбирает CSS-свойства в словарь.

    :param style: Строка CSS-свойств.
    :type style: str
    :return: Словарь CSS-свойств.
    :rtype: dict
    """
    return dict(
        (x.strip(), y.strip())
        for x, y in (z.split(':', 1)
                    for z in style.split(';') if ':' in z) # изменено условие
    )

def dumb_css_parser(data: str) -> dict:
    """
    Разбирает CSS в словарь селекторов и их свойств.

    :param data: Строка CSS.
    :type data: str
    :return: Словарь селекторов и их свойств.
    :rtype: dict
    """
    # remove @import sentences
    import_index = data.find('@import')
    while import_index != -1:
        data = data[0:import_index] + data[data.find(';', import_index) + 1:]
        import_index = data.find('@import')

    # parse the css. reverted from dictionary compehension in order to support older pythons
    elements =  [x.split('{') for x in data.split('}') if '{' in x.strip()]
    elements = dict((a.strip(), dumb_property_dict(b)) for a, b in elements)

    return elements

def element_style(attrs: dict, style_def: dict, parent_style: dict) -> dict:
    """
    Определяет финальный стиль элемента, учитывая CSS-классы и inline-стили.

    :param attrs: Атрибуты HTML-элемента.
    :type attrs: dict
    :param style_def: Словарь CSS-определений.
    :type style_def: dict
    :param parent_style: Стиль родительского элемента.
    :type parent_style: dict
    :return: Словарь финального стиля элемента.
    :rtype: dict
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

def google_list_style(style: dict) -> str:
    """
    Определяет тип списка (упорядоченный или неупорядоченный) на основе CSS-стилей Google Docs.

    :param style: Словарь CSS-стилей.
    :type style: dict
    :return: 'ul' для неупорядоченного списка, 'ol' для упорядоченного списка.
    :rtype: str
    """
    if 'list-style-type' in style:
        list_style = style['list-style-type']
        if list_style in ['disc', 'circle', 'square', 'none']:
            return 'ul'
    return 'ol'

def google_nest_count(style: dict) -> int:
    """
    Вычисляет уровень вложенности списка Google Docs на основе CSS-стилей.

    :param style: Словарь CSS-стилей.
    :type style: dict
    :return: Уровень вложенности списка.
    :rtype: int
    """
    nest_count = 0
    if 'margin-left' in style:
        nest_count = int(style['margin-left'][:-2]) / GOOGLE_LIST_INDENT
    return nest_count

def google_has_height(style: dict) -> bool:
    """
    Проверяет, определен ли атрибут 'height' явно в CSS-стилях элемента.

    :param style: Словарь CSS-стилей.
    :type style: dict
    :return: True, если 'height' определен, иначе False.
    :rtype: bool
    """
    return 'height' in style

def google_text_emphasis(style: dict) -> list:
    """
    Определяет модификаторы выделения текста на основе CSS-стилей.

    :param style: Словарь CSS-стилей.
    :type style: dict
    :return: Список модификаторов выделения.
    :rtype: list
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
    Проверяет, используется ли шрифт фиксированной ширины в CSS-стилях.

    :param style: Словарь CSS-стилей.
    :type style: dict
    :return: True, если используется шрифт фиксированной ширины, иначе False.
    :rtype: bool
    """
    font_family = ''
    if 'font-family' in style:
        font_family = style['font-family']
    return font_family in ['Courier New', 'Consolas']

def list_numbering_start(attrs: dict) -> int:
    """
    Извлекает начальное значение нумерации списка из атрибутов HTML-элемента.

    :param attrs: Атрибуты HTML-элемента.
    :type attrs: dict
    :return: Начальное значение нумерации списка.
    :rtype: int
    """
    if 'start' in attrs:
        return int(attrs['start']) - 1
    else:
        return 0

class _html2text(HTMLParser.HTMLParser):
    """
    Класс для преобразования HTML в Markdown.
    
    :param out: Функция для вывода текста.
    :type out: callable, optional
    :param baseurl: Базовый URL для разрешения относительных ссылок.
    :type baseurl: str, optional
    """
    def __init__(self, out=None, baseurl=''):
        HTMLParser.HTMLParser.__init__(self)

        if out is None:
            self.out = self.outtextf
        else:
            self.out = out
        self.outtextlist = [] # empty list to store output characters before they are  "joined"
        try:
            self.outtext = str() # Изменено на str()
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

    def feed(self, data: str):
        """
        Подает HTML-данные для разбора.

        :param data: HTML-данные.
        :type data: str
        """
        data = data.replace("</' + 'script>", "</ignore>")
        HTMLParser.HTMLParser.feed(self, data)

    def outtextf(self, s: str):
        """
        Добавляет текст в список вывода.

        :param s: Строка для добавления.
        :type s: str
        """
        self.outtextlist.append(s)
        if s:
            self.lastWasNL = s[-1] == '\n'

    def close(self) -> str:
        """
        Завершает разбор HTML и возвращает преобразованный текст.

        :return: Преобразованный в Markdown текст.
        :rtype: str
        """
        HTMLParser.HTMLParser.close(self)
        self.pbr()
        self.o('', 0, 'end')

        self.outtext = ''.join(self.outtextlist) # изменено для Python3

        if options.google_doc:
            self.outtext = self.outtext.replace('&nbsp_place_holder;', ' ')

        return self.outtext

    def handle_charref(self, c: str):
        """
        Обрабатывает числовую ссылку на символ.

        :param c: Числовая ссылка.
        :type c: str
        """
        self.o(charref(c), 1)

    def handle_entityref(self, c: str):
        """
        Обрабатывает именованную ссылку на символ.

        :param c: Именованная ссылка.
        :type c: str
        """
        self.o(entityref(c), 1)

    def handle_starttag(self, tag: str, attrs: list):
        """
        Обрабатывает открывающий тег.

        :param tag: Имя тега.
        :type tag: str
        :param attrs: Список атрибутов тега.
        :type attrs: list
        """
        self.handle_tag(tag, attrs, 1)

    def handle_endtag(self, tag: str):
        """
        Обрабатывает закрывающий тег.

        :param tag: Имя тега.
        :type tag: str
        """
        self.handle_tag(tag, None, 0)

    def previousIndex(self, attrs: dict) -> int | None:
        """
        Возвращает индекс ссылки в списке ссылок.

        :param attrs: Атрибуты ссылки.
        :type attrs: dict
        :return: Индекс ссылки или None, если не найдена.
        :rtype: int | None
        """
        if 'href' not in attrs:
            return None

        i = -1
        for a in self.a:
            i += 1
            match = 0

            if 'href' in a and a['href'] == attrs['href']:
                if 'title' in a or 'title' in attrs:
                    if ('title' in a and 'title' in attrs and
                        a['title'] == attrs['title']):
                        match = True
                else:
                    match = True

            if match:
                return i
        return None

    def drop_last(self, nLetters: int):
        """
        Удаляет последние символы из выходного текста.

        :param nLetters: Количество символов для удаления.
        :type nLetters: int
        """
        if not self.quiet:
            self.outtext = self.outtext[:-nLetters]

    def handle_emphasis(self, start: bool, tag_style: dict, parent_style: dict):
        """
        Обрабатывает выделение текста.

        :param start: True, если открывающий тег, False, если закрывающий.
        :type start: bool
        :param tag_style: CSS-стили текущего тега.
        :type tag_style: dict
        :param parent_style: CSS-стили родительского тега.
        :type parent_style: dict
        """
        tag_emphasis = google_text_emphasis(tag_style)
        parent_emphasis = google_text_emphasis(parent_style)

        # handle Google's text emphasis
        strikethrough = 'line-through' in tag_emphasis and options.hide_strikethrough
        bold = 'bold' in tag_emphasis and 'bold' not in parent_emphasis
        italic = 'italic' in tag_emphasis and 'italic' not in parent_emphasis
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
                self.o('_')
                self.drop_white_space += 1
            if bold:
                self.o('**')
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
                    self.o('**')
            if italic:
                if self.drop_white_space:
                    # empty emphasis, drop it
                    self.drop_last(1)
                    self.drop_white_space -= 1
                else:
                    self.o('_')
            # space is only allowed after *all* emphasis marks
            if (bold or italic) and not self.emphasis:
                self.o(' ')
            if strikethrough:
                self.quiet -= 1

    def handle_tag(self, tag: str, attrs: list | None, start: bool):
        """
        Обрабатывает HTML-тег.

        :param tag: Имя тега.
        :type tag: str
        :param attrs: Список атрибутов тега.
        :type attrs: list | None
        :param start: True, если открывающий тег, False, если закрывающий.
        :type start: bool
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
                self.o(hn(tag) * '#' + ' ')
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

        if tag == 'br' and start:
            self.o('  \n')

        if tag == 'hr' and start:
            self.p()
            self.o('* * *')
            self.p()

        if tag in ['head', 'style', 'script']:
            if start:
                self.quiet += 1
            else:
                self.quiet -= 1

        if tag == 'style':
            if start:
                self.style += 1
            else:
                self.style -= 1

        if tag in ['body']:
            self.quiet = 0  # sites like 9rules.com never close <head>

        if tag == 'blockquote':
            if start:
                self.p()
                self.o('> ', 0, 1)
                self.start = 1
                self.blockquote += 1
            else:
                self.blockquote -= 1
                self.p()

        if tag in ['em', 'i', 'u']:
            self.o('_')
        if tag in ['strong', 'b']:
            self.o('**')
        if tag in ['del', 'strike']:
            if start:
                self.o('<' + tag + '>')
            else:
                self.o('</' + tag + '>')

        if options.google_doc:
            if not self.inheader:
                # handle some font attributes, but leave headers clean
                self.handle_emphasis(start, tag_style, parent_style)

        if tag == 'code' and not self.pre:
            self.o('`')  # TODO: `` `this` ``
        if tag == 'abbr':
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

        if tag == 'a' and not IGNORE_ANCHORS:
            if start:
                if 'href' in attrs and not (SKIP_INTERNAL_LINKS and attrs['href'].startswith('#')):
                    self.astack.append(attrs)
                    self.o('[')
                else:
                    self.astack.append(None)
            else:
                if self.astack:
                    a = self.astack.pop()
                    if a:
                        if INLINE_LINKS:
                            self.o('](' + a['href'] + ')')
                        else:
                            i = self.previousIndex(a)
                            if i is not None:
                                a = self.a[i]
                            else:
                                self.acount += 1
                                a['count'] = self.acount
                                a['outcount'] = self.outcount
                                self.a.append(a)
                            self.o('][' + str(a['count']) + ']')

        if tag == 'img' and start and not IGNORE_IMAGES:
            if 'src' in attrs:
                attrs['href'] = attrs['src']
                alt = attrs.get('alt', '')
                if INLINE_LINKS:
                    self.o('![')
                    self.o(alt)
                    self.o('](' + attrs['href'] + ')')
                else:
                    i = self.previousIndex(attrs)
                    if i is not None:
                        attrs = self.a[i]
                    else:
                        self.acount += 1
                        attrs['count'] = self.acount
                        attrs['outcount'] = self.outcount
                        self.a.append(attrs)
                    self.o('![')
                    self.o(alt)
                    self.o('][' + str(attrs['count']) + ']')

        if tag == 'dl' and start:
            self.p()
        if tag == 'dt' and not start:
            self.pbr()
        if tag == 'dd' and start:
            self.o('    ')
        if tag == 'dd' and not start:
            self.pbr()

        if tag in ['ol', 'ul']:
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
                self.o('  ' * nest_count)  # TODO: line up <ol><li>s > 9 correctly.
                if li['name'] == 'ul':
                    self.o(options.ul_item_mark + ' ')
                elif li['name'] == 'ol':
                    li['num'] += 1
                    self.o(str(li['num']) + '. ')
                self.start = 1

        if tag in ['table', 'tr'] and start:
            self.p()
        if tag == 'td':
            self.pbr()

        if tag == 'pre':
            if start:
                self.startpre = 1
                self.pre = 1
            else:
                self.pre = 0
            self.p()

    def pbr(self):
        """
        Управляет добавлением перевода строки для мягкого переноса.
        """
        if self.p_p == 0:
            self.p_p = 1

    def p(self):
        """
        Устанавливает флаг для добавления перевода строки.
        """
        self.p_p = 2

    def soft_br(self):
        """
        Добавляет мягкий перенос строки.
        """
        self.pbr()
        self.br_toggle = '  '

    def o(self, data: str, puredata: int = 0, force: int | str = 0):
        """
        Выводит данные.

        :param data: Данные для вывода.
        :type data: str
        :param puredata: Флаг чистоты данных.
        :type puredata: int