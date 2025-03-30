# Модуль `html2text`

## Обзор

Модуль `html2text` предназначен для конвертации HTML-документов в Markdown-текст. Он обеспечивает базовую структуру и форматирование текста, сохраняя при этом удобочитаемость. Модуль поддерживает различные опции, такие как обработка списков, ссылок, изображений и стилей Google Docs.

## Подробней

Этот модуль является частью проекта `hypotez` и используется для преобразования HTML-контента в формат Markdown. Это может быть полезно для извлечения текста из веб-страниц или документов, сохраняя при этом структуру и основные элементы форматирования. Модуль обрабатывает HTML-теги, стили и специальные символы, чтобы создать Markdown-представление исходного контента.

## Функции

### `has_key`

```python
def has_key(x, y):
    """
    Args:
        x: 
        y: 

    Returns:
        bool: Возвращает `True`, если `y` является ключом в `x`, иначе `False`.
    """
```

**Описание**: Проверяет, содержит ли объект `x` ключ `y`.

**Параметры**:
- `x`: Объект, который нужно проверить на наличие ключа.
- `y`: Ключ, наличие которого нужно проверить в объекте `x`.

**Возвращает**:
- `bool`: `True`, если ключ `y` присутствует в объекте `x`, иначе `False`.

### `name2cp`

```python
def name2cp(k):
    """
    Args:
        k: 

    Returns:
        int: 
    """
```

**Описание**: Преобразует имя HTML-сущности в кодовую точку Unicode.

**Параметры**:
- `k` (str): Имя HTML-сущности.

**Возвращает**:
- `int`: Кодовая точка Unicode для данной сущности.

### `charref`

```python
def charref(name):
    """
    Args:
        name: 

    Returns:
        str: 
    """
```

**Описание**: Преобразует числовую ссылку на символ в символ Unicode.

**Параметры**:
- `name` (str): Числовая ссылка на символ.

**Возвращает**:
- `str`: Символ Unicode, соответствующий числовой ссылке.

### `entityref`

```python
def entityref(c):
    """
    Args:
        c: 

    Returns:
        str: 
    """
```

**Описание**: Преобразует ссылку на HTML-сущность в символ Unicode.

**Параметры**:
- `c` (str): Ссылка на HTML-сущность.

**Возвращает**:
- `str`: Символ Unicode, соответствующий HTML-сущности.

### `replaceEntities`

```python
def replaceEntities(s):
    """
    Args:
        s: 

    Returns:
        str: 
    """
```

**Описание**: Заменяет HTML-сущности в строке на соответствующие символы.

**Параметры**:
- `s` (str): Строка, содержащая HTML-сущности.

**Возвращает**:
- `str`: Строка с замененными HTML-сущностями.

### `unescape`

```python
def unescape(s):
    """
    Args:
        s: 

    Returns:
        str: 
    """
```

**Описание**: Удаляет HTML-сущности из строки.

**Параметры**:
- `s` (str): Строка, из которой нужно удалить HTML-сущности.

**Возвращает**:
- `str`: Строка без HTML-сущностей.

### `onlywhite`

```python
def onlywhite(line):
    """Return true if the line does only consist of whitespace characters."""
    for c in line:
        if c is not ' ' and c is not '  ':
            return c is ' '
    return line
```

**Описание**: Проверяет, состоит ли строка только из пробельных символов.

**Параметры**:
- `line` (str): Строка для проверки.

**Возвращает**:
- `bool`: `True`, если строка состоит только из пробельных символов, иначе `False`.

### `optwrap`

```python
def optwrap(text):
    """Wrap all paragraphs in the provided text."""
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
```

**Описание**: Переносит все абзацы в предоставленном тексте.

**Параметры**:
- `text` (str): Текст для переноса.

**Возвращает**:
- `str`: Текст с перенесенными абзацами.

### `hn`

```python
def hn(tag):
    if tag[0] == 'h' and len(tag) == 2:
        try:
            n = int(tag[1])
            if n in range(1, 10): return n
        except ValueError: return 0
```

**Описание**: Определяет уровень заголовка HTML-тега.

**Параметры**:
- `tag` (str): HTML-тег заголовка.

**Возвращает**:
- `int | None`: Уровень заголовка (1-9) или `None`, если тег не является заголовком.

### `dumb_property_dict`

```python
def dumb_property_dict(style):
    """returns a hash of css attributes"""
    return dict([(x.strip(), y.strip()) for x, y in [z.split(':', 1) for z in style.split(';') if ':' in z]]);
```

**Описание**: Возвращает словарь CSS-атрибутов.

**Параметры**:
- `style` (str): Строка CSS-стилей.

**Возвращает**:
- `dict`: Словарь CSS-атрибутов.

### `dumb_css_parser`

```python
def dumb_css_parser(data):
    """returns a hash of css selectors, each of which contains a hash of css attributes"""
    # remove @import sentences
    importIndex = data.find('@import')
    while importIndex != -1:
        data = data[0:importIndex] + data[data.find(';', importIndex) + 1:]
        importIndex = data.find('@import')

    # parse the css. reverted from dictionary compehension in order to support older pythons
    elements =  [x.split('{') for x in data.split('}') if '{' in x.strip()]
    elements = dict([(a.strip(), dumb_property_dict(b)) for a, b in elements])

    return elements
```

**Описание**: Возвращает словарь CSS-селекторов, каждый из которых содержит словарь CSS-атрибутов.

**Параметры**:
- `data` (str): Строка CSS-данных.

**Возвращает**:
- `dict`: Словарь CSS-селекторов и атрибутов.

### `element_style`

```python
def element_style(attrs, style_def, parent_style):
    """returns a hash of the 'final' style attributes of the element"""
    style = parent_style.copy()
    if 'class' in attrs:
        for css_class in attrs['class'].split():
            css_style = style_def['.' + css_class]
            style.update(css_style)
    if 'style' in attrs:
        immediate_style = dumb_property_dict(attrs['style'])
        style.update(immediate_style)
    return style
```

**Описание**: Возвращает словарь "финальных" атрибутов стиля элемента.

**Параметры**:
- `attrs` (dict): Атрибуты элемента.
- `style_def` (dict): Определения стилей.
- `parent_style` (dict): Стили родительского элемента.

**Возвращает**:
- `dict`: Словарь атрибутов стиля элемента.

### `google_list_style`

```python
def google_list_style(style):
    """finds out whether this is an ordered or unordered list"""
    if 'list-style-type' in style:
        list_style = style['list-style-type']
        if list_style in ['disc', 'circle', 'square', 'none']:
            return 'ul'
    return 'ol'
```

**Описание**: Определяет, является ли список упорядоченным или неупорядоченным.

**Параметры**:
- `style` (dict): Стили списка.

**Возвращает**:
- `str`: `'ul'` для неупорядоченного списка, `'ol'` для упорядоченного списка.

### `google_nest_count`

```python
def google_nest_count(style):
    """calculate the nesting count of google doc lists"""
    nest_count = 0
    if 'margin-left' in style:
        nest_count = int(style['margin-left'][:-2]) / GOOGLE_LIST_INDENT
    return nest_count
```

**Описание**: Вычисляет уровень вложенности списков Google Docs.

**Параметры**:
- `style` (dict): Стили списка.

**Возвращает**:
- `int`: Уровень вложенности списка.

### `google_has_height`

```python
def google_has_height(style):
    """check if the style of the element has the 'height' attribute explicitly defined"""
    if 'height' in style:
        return True
    return False
```

**Описание**: Проверяет, определен ли атрибут `height` в стиле элемента.

**Параметры**:
- `style` (dict): Стили элемента.

**Возвращает**:
- `bool`: `True`, если атрибут `height` определен, иначе `False`.

### `google_text_emphasis`

```python
def google_text_emphasis(style):
    """return a list of all emphasis modifiers of the element"""
    emphasis = []
    if 'text-decoration' in style:
        emphasis.append(style['text-decoration'])
    if 'font-style' in style:
        emphasis.append(style['font-style'])
    if 'font-weight' in style:
        emphasis.append(style['font-weight'])
    return emphasis
```

**Описание**: Возвращает список всех модификаторов выделения элемента.

**Параметры**:
- `style` (dict): Стили элемента.

**Возвращает**:
- `list`: Список модификаторов выделения.

### `google_fixed_width_font`

```python
def google_fixed_width_font(style):
    """check if the css of the current element defines a fixed width font"""
    font_family = ''
    if 'font-family' in style:
        font_family = style['font-family']
    if 'Courier New' == font_family or 'Consolas' == font_family:
        return True
    return False
```

**Описание**: Проверяет, использует ли элемент шрифт фиксированной ширины.

**Параметры**:
- `style` (dict): Стили элемента.

**Возвращает**:
- `bool`: `True`, если используется шрифт фиксированной ширины, иначе `False`.

### `list_numbering_start`

```python
def list_numbering_start(attrs):
    """extract numbering from list element attributes"""
    if 'start' in attrs:
        return int(attrs['start']) - 1
    else:
        return 0
```

**Описание**: Извлекает начальный номер из атрибутов элемента списка.

**Параметры**:
- `attrs` (dict): Атрибуты элемента списка.

**Возвращает**:
- `int`: Начальный номер списка.

### `_html2text`

```python
class _html2text(HTMLParser.HTMLParser):
    def __init__(self, out=None, baseurl=''):
        HTMLParser.HTMLParser.__init__(self)
        
        if out is None: self.out = self.outtextf
        else: self.out = out
        self.outtextlist = [] # empty list to store output characters before they are  "joined"
        try:
            self.outtext = unicode()
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
        data = data.replace("</\' + \'script>", "</ignore>")
        HTMLParser.HTMLParser.feed(self, data)
    
    def outtextf(self, s): 
        self.outtextlist.append(s)
        if s: self.lastWasNL = s[-1] == '\n'
    
    def close(self):
        HTMLParser.HTMLParser.close(self)
        
        self.pbr()
        self.o('', 0, 'end')

        self.outtext = self.outtext.join(self.outtextlist)
        
        if options.google_doc:
            self.outtext = self.outtext.replace('&nbsp_place_holder;', ' ');
        
        return self.outtext
        
    def handle_charref(self, c):
        self.o(charref(c), 1)

    def handle_entityref(self, c):
        self.o(entityref(c), 1)
            
    def handle_starttag(self, tag, attrs):
        self.handle_tag(tag, attrs, 1)
    
    def handle_endtag(self, tag):
        self.handle_tag(tag, None, 0)
        
    def previousIndex(self, attrs):
        """ returns the index of certain set of attributes (of a link) in the
            self.a list
 
            If the set of attributes is not found, returns None
        """
        if not has_key(attrs, 'href'): return
        
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

            if match: return i

    def drop_last(self, nLetters):
        if not self.quiet:
            self.outtext = self.outtext[:-nLetters]
           
    def handle_emphasis(self, start, tag_style, parent_style):
        """handles various text emphases"""
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
        #attrs = fixattrs(attrs)
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
        
        if tag == "br" and start: self.o("  \n")

        if tag == "hr" and start:
            self.p()
            self.o("* * *")
            self.p()

        if tag in ["head", "style", 'script']: 
            if start: self.quiet += 1
            else: self.quiet -= 1

        if tag == "style":
            if start: self.style += 1
            else: self.style -= 1

        if tag in ["body"]:
            self.quiet = 0 # sites like 9rules.com never close <head>
        
        if tag == "blockquote":
            if start: 
                self.p(); self.o('> ', 0, 1); self.start = 1
                self.blockquote += 1
            else:
                self.blockquote -= 1
                self.p()
        
        if tag in ['em', 'i', 'u']: self.o("_")
        if tag in ['strong', 'b']: self.o("**")
        if tag in ['del', 'strike']:
            if start:                                                           
                self.o("<"+tag+">")
            else:
                self.o("</"+tag+">")

        if options.google_doc:
            if not self.inheader:
                # handle some font attributes, but leave headers clean
                self.handle_emphasis(start, tag_style, parent_style)

        if tag == "code" and not self.pre: self.o('`') #TODO: `` `this` ``
        if tag == "abbr":
            if start:
                self.abbr_title = None
                self.abbr_data = ''
                if has_key(attrs, 'title'):
                    self.abbr_title = attrs['title']
            else:
                if self.abbr_title != None:
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
        
        if tag == 'dl' and start: self.p()
        if tag == 'dt' and not start: self.pbr()
        if tag == 'dd' and start: self.o('    ')
        if tag == 'dd' and not start: self.pbr()
        
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
                if self.list: self.list.pop()
            self.lastWasList = True
        else:
            self.lastWasList = False
        
        if tag == 'li':
            self.pbr()
            if start:
                if self.list: li = self.list[-1]
                else: li = {'name':'ul', 'num':0}
                if options.google_doc:
                    nest_count = google_nest_count(tag_style)
                else:
                    nest_count = len(self.list)
                self.o("  " * nest_count) #TODO: line up <ol><li>s > 9 correctly.
                if li['name'] == "ul": self.o(options.ul_item_mark + " ")
                elif li['name'] == "ol":
                    li['num'] += 1
                    self.o(str(li['num'])+". ")
                self.start = 1
        
        if tag in ["table", "tr"] and start: self.p()
        if tag == 'td': self.pbr()
        
        if tag == "pre":
            if start:
                self.startpre = 1
                self.pre = 1
            else:
                self.pre = 0
            self.p()
            
    def pbr(self):
        if self.p_p == 0: self.p_p = 1

    def p(self): self.p_p = 2

    def soft_br(self):
        self.pbr()
        self.br_toggle = '  '
    
    def o(self, data, puredata=0, force=0):
        if self.abbr_data is not None: self.abbr_data += data
        
        if not self.quiet: 
            if options.google_doc:
                # prevent white space immediately after 'begin emphasis' marks ('**' and '_')
                lstripped_data = data.lstrip()
                if self.drop_white_space and not (self.pre or self.code):
                    data = lstripped_data
                if lstripped_data != '':
                    self.drop_white_space = 0
            
            if puredata and not self.pre:
                data = re.sub('\s+', ' ', data)
                if data and data[0] == ' ':
                    self.space = 1
                    data = data[1:]
            if not data and not force: return

            if self.startpre:
                #self.out(" :") #TODO: not output when already one there
                self.startpre = 0
            
            bq = (">" * self.blockquote)
            if not (force and data and data[0] == ">") and self.blockquote: bq += " "
            
            if self.pre:
                bq += "    "
                data = data.replace("\n", "\n"+bq)
            
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
                self.out((self.br_toggle+'\n'+bq)*self.p_p)
                self.space = 0
                self.br_toggle = ''
                
            if self.space:
                if not self.lastWasNL: self.out(' ')
                self.space = 0

            if self.a and ((self.p_p == 2 and LINKS_EACH_PARAGRAPH) or force == "end"):
                if force == "end": self.out("\n")

                newa = []
                for link in self.a:
                    if self.outcount > link['outcount']:
                        self.out("   ["+ str(link['count']) +"]: " + urlparse.urljoin(self.baseurl, link['href'])) 
                        if has_key(link, 'title'): self.out(" ("+link['title']+")")
                        self.out("\n")
                    else:
                        newa.append(link)

                if self.a != newa: self.out("\n") # Don't need an extra line when nothing was done.

                self.a = newa
            
            if self.abbr_list and force == "end":
                for abbr, definition in self.abbr_list.items():
                    self.out("  *[" + abbr + "]: " + definition + "\n")

            self.p_p = 0
            self.out(data)
            self.outcount += 1

    def handle_data(self, data):
        if r'\/script>' in data: self.quiet -= 1

        if self.style:
            self.style_def.update(dumb_css_parser(data))

        self.o(data, 1)
    
    def unknown_decl(self, data): pass
```

**Описание**: Класс `_html2text` является подклассом `HTMLParser.HTMLParser` и используется для преобразования HTML в Markdown.

**Методы**:
- `__init__`: Инициализирует объект класса `_html2text`.
- `feed`: Обрабатывает HTML-данные.
- `outtextf`: Добавляет текст в список вывода.
- `close`: Завершает обработку HTML и возвращает Markdown-текст.
- `handle_charref`: Обрабатывает числовые ссылки на символы.
- `handle_entityref`: Обрабатывает ссылки на HTML-сущности.
- `handle_starttag`: Обрабатывает начальные теги HTML.
- `handle_endtag`: Обрабатывает конечные теги HTML.
- `previousIndex`: Возвращает индекс атрибутов ссылки в списке ссылок.
- `drop_last`: Удаляет последние символы из текста вывода.
- `handle_emphasis`: Обрабатывает выделение текста.
- `handle_tag`: Обрабатывает HTML-теги.
- `pbr`: Устанавливает перенос строки.
- `p`: Устанавливает двойной перенос строки.
- `soft_br`: Устанавливает мягкий перенос строки.
- `o`: Выводит данные.
- `handle_data`: Обрабатывает данные HTML.
- `unknown_decl`: Обрабатывает неизвестные объявления.

### `wrapwrite`

```python
def wrapwrite(text):
    text = text.encode('utf-8')
    try: #Python3
        sys.stdout.buffer.write(text)
    except AttributeError:
        sys.stdout.write(text)
```

**Описание**: Записывает текст в стандартный вывод, кодируя его в UTF-8.

**Параметры**:
- `text` (str): Текст для записи.

### `html2text_file`

```python
def html2text_file(html, out=wrapwrite, baseurl=''):
    h = _html2text(out, baseurl)
    h.feed(html)
    h.feed("")
    return h.close()
```

**Описание**: Преобразует HTML-текст из файла в Markdown.

**Параметры**:
- `html` (str): HTML-текст.
- `out` (Callable[[str], None], optional): Функция для вывода. По умолчанию `wrapwrite`.
- `baseurl` (str, optional): Базовый URL. По умолчанию пустая строка.

**Возвращает**:
- `str`: Markdown-текст.

### `html2text`

```python
def html2text(html, baseurl=''):
    return optwrap(html2text_file(html, None, baseurl))
```

**Описание**: Преобразует HTML-текст в Markdown, оборачивая текст.

**Параметры**:
- `html` (str): HTML-текст.
- `baseurl` (str, optional): Базовый URL. По умолчанию пустая строка.

**Возвращает**:
- `str`: Markdown-текст с обернутым текстом.

### `Storage`

```python
class Storage: pass
```

**Описание**: Пустой класс для хранения опций.

## Переменные

### `options`

```python
options = Storage()
options.google_doc = False
options.ul_item_mark = '*'
```

**Описание**: Объект для хранения опций.

### `__version__`

```python
__version__ = "3.1"
```

**Описание**: Версия модуля.

### `__author__`

```python
__author__ = "Aaron Swartz (me@aaronsw.com)"
```

**Описание**: Автор модуля.

### `__copyright__`

```python
__copyright__ = "(C) 2004-2008 Aaron Swartz. GNU GPL 3."
```

**Описание**: Информация об авторских правах.

### `__contributors__`

```python
__contributors__ = ["Martin 'Joey' Schulze", "Ricardo Reyes", "Kevin Jay North"]
```

**Описание**: Список контрибьюторов.

### `UNICODE_SNOB`

```python
UNICODE_SNOB = 0
```

**Описание**: Флаг для использования символов Unicode вместо ASCII.

### `LINKS_EACH_PARAGRAPH`

```python
LINKS