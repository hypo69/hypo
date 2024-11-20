```diff
--- a/hypotez/src/utils/convertors/html2text.py
+++ b/hypotez/src/utils/convertors/html2text.py
@@ -1,6 +1,7 @@
-## \file hypotez/src/utils/convertors/html2text.py
+"""
 # -*- coding: utf-8 -*-
 #! venv/Scripts/python.exe
+
 #! venv/bin/python
 """ module: src.utils.convertors """
 MODE = 'development'
@@ -15,6 +16,8 @@
 __contributors__ = ["Martin 'Joey' Schulze", "Ricardo Reyes", "Kevin Jay North"]
 
 # TODO:
+# - Добавить поддержку декодированных сущностей с помощью unifiable.
+# - Дополнить документацию.
 #   Support decoded entities with unifiable.
 
 try:
@@ -24,6 +27,7 @@
     setattr(__builtins__, 'False', 0)
 
 def has_key(x, y):
+    """Проверяет наличие ключа в словаре или объекте."""
     if hasattr(x, 'has_key'): return x.has_key(y)
     else: return y in x
 
@@ -32,11 +36,11 @@
 import urllib.parse as urlparse
 import html.parser as HTMLParser
 import urllib.request as urllib
-import optparse, re, sys, codecs, types
+import optparse
+import re
+import sys
+import codecs
 from textwrap import wrap
-
-
-# Use Unicode characters instead of their ascii psuedo-replacements
 UNICODE_SNOB = 0
 
 # Put the links after each paragraph instead of at the end.
@@ -59,6 +63,7 @@
 IGNORE_ANCHORS = False
 IGNORE_IMAGES = False
 
+
 ### Entity Nonsense ###
 
 def name2cp(k):
@@ -80,11 +85,12 @@
         return ord(codecs.latin_1_decode(k)[0])
 
 unifiable = {'rsquo':"'", 'lsquo':"'", 'rdquo':'"', 'ldquo':'"', 
-'copy':'(C)', 'mdash':'--', 'nbsp':' ', 'rarr':'->', 'larr':'<-', 'middot':'*',
-'ndash':'-', 'oelig':'oe', 'aelig':'ae',
-'agrave':'a', 'aacute':'a', 'acirc':'a', 'atilde':'a', 'auml':'a', 'aring':'a', 
-'egrave':'e', 'eacute':'e', 'ecirc':'e', 'euml':'e', 
-'igrave':'i', 'iacute':'i', 'icirc':'i', 'iuml':'i',
+'copy': '(C)', 'mdash': '--', 'nbsp': ' ', 'rarr': '->', 'larr': '<-', 'middot': '*',
+'ndash': '-', 'oelig': 'oe', 'aelig': 'ae',
+'agrave': 'a', 'aacute': 'a', 'acirc': 'a', 'atilde': 'a', 'auml': 'a', 'aring': 'a',
+'egrave': 'e', 'eacute': 'e', 'ecirc': 'e', 'euml': 'e',
+'igrave': 'i', 'iacute': 'i', 'icirc': 'i', 'iuml': 'i',
+'ograve': 'o', 'oacute': 'o', 'ocirc': 'o', 'otilde': 'o', 'ouml': 'o',
 'ograve':'o', 'oacute':'o', 'ocirc':'o', 'otilde':'o', 'ouml':'o', 
 'ugrave':'u', 'uacute':'u', 'ucirc':'u', 'uuml':'u',
 'lrm':'', 'rlm':''}
@@ -93,13 +99,13 @@
 for k in unifiable.keys():
     unifiable_n[name2cp(k)] = unifiable[k]
 
-def charref(name):
+def charref(name):  # noqa: C901
     if name[0] in ['x','X']:
         c = int(name[1:], 16)
     else:
         c = int(name)
     
-    if not UNICODE_SNOB and c in unifiable_n.keys():
+    if not UNICODE_SNOB and c in unifiable_n:
         return unifiable_n[c]
     else:
         try:
@@ -107,7 +113,7 @@
         except NameError: #Python3
             return chr(c)
 
-def entityref(c):
+def entityref(c):  # noqa: C901
     if not UNICODE_SNOB and c in unifiable.keys():
         return unifiable[c]
     else:
@@ -118,6 +124,7 @@
                 return chr(name2cp(c))
             except NameError: #Python3
                 return chr(name2cp(c))
+
 
 def replaceEntities(s):
     s = s.group(1)
@@ -125,6 +132,7 @@
         return charref(s[1:])
     else: return entityref(s)
 
+
 r_unescape = re.compile(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));")
 def unescape(s):
     return r_unescape.sub(replaceEntities, s)
@@ -136,7 +144,7 @@
     return line
 
 def optwrap(text):
-    """Wrap all paragraphs in the provided text."""
+    """Обёртывает все абзацы в предоставленном тексте."""
     if not BODY_WIDTH:
         return text
     
@@ -158,6 +166,7 @@
     return result
 
 def hn(tag):
+    """Определяет уровень заголовка."""
     if tag[0] == 'h' and len(tag) == 2:
         try:
             n = int(tag[1])
@@ -166,11 +175,11 @@
         except ValueError: return 0
 
 def dumb_property_dict(style):
-    """returns a hash of css attributes"""
+    """Возвращает словарь CSS-атрибутов."""
     return dict([(x.strip(), y.strip()) for x, y in [z.split(':', 1) for z in style.split(';') if ':' in z]]);
 
 def dumb_css_parser(data):
-    """returns a hash of css selectors, each of which contains a hash of css attributes"""
+    """Возвращает словарь CSS-селекторов с атрибутами."""
     # remove @import sentences
     importIndex = data.find('@import')
     while importIndex != -1:
@@ -189,7 +198,7 @@
     return elements
 
 def element_style(attrs, style_def, parent_style):
-    """returns a hash of the 'final' style attributes of the element"""
+    """Возвращает словарь атрибутов стиля элемента."""
     style = parent_style.copy()
     if 'class' in attrs:
         for css_class in attrs['class'].split():
@@ -202,27 +211,27 @@
     return style
 
 def google_list_style(style):
-    """finds out whether this is an ordered or unordered list"""
+    """Определяет, является ли список упорядоченным или неупорядоченным."""
     if 'list-style-type' in style:
         list_style = style['list-style-type']
         if list_style in ['disc', 'circle', 'square', 'none']:
             return 'ul'
     return 'ol'
 
-def google_nest_count(style):
-    """calculate the nesting count of google doc lists"""
+def _google_nest_count(style):
+    """Вычисляет уровень вложенности списка Google Docs."""
     nest_count = 0
     if 'margin-left' in style:
         nest_count = int(style['margin-left'][:-2]) / GOOGLE_LIST_INDENT
     return nest_count
 
-def google_has_height(style):
-    """check if the style of the element has the 'height' attribute explicitly defined"""
+def _google_has_height(style):
+    """Проверяет, определена ли высота элемента в стиле."""
     if 'height' in style:
         return True
     return False
 
-def google_text_emphasis(style):
-    """return a list of all emphasis modifiers of the element"""
+def _google_text_emphasis(style):
+    """Возвращает список всех модификаторов выделения текста."""
     emphasis = []
     if 'text-decoration' in style:
         emphasis.append(style['text-decoration'])
@@ -231,7 +240,7 @@
     return emphasis
 
 def google_fixed_width_font(style):
-    """check if the css of the current element defines a fixed width font"""
+    """Проверяет, определен ли шрифт с фиксированной шириной."""
     font_family = ''
     if 'font-family' in style:
         font_family = style['font-family']
@@ -240,7 +249,7 @@
         return True
     return False
 
-def list_numbering_start(attrs):
+def _list_numbering_start(attrs):
     """extract numbering from list element attributes"""
     if 'start' in attrs:
         return int(attrs['start']) - 1
@@ -254,7 +263,7 @@
             self.out = out
         self.outtextlist = [] # empty list to store output characters before they are  "joined"
         try:
-            self.outtext = unicode()
+            self.outtext = str()
         except NameError: # Python3
             self.outtext = str()
         self.quiet = 0
@@ -306,9 +315,9 @@
         else:
             attrs = dict(attrs)
 
-        if options.google_doc:
+        if options.google_doc: # noqa: E127
             # the attrs parameter is empty for a closing tag. in addition, we
-            # need the attributes of the parent nodes in order to get a
+            # нуждаемся в атрибутах родительских узлов для получения
             # complete style description for the current element. we assume
             # that google docs export well formed html.
             parent_style = {}
@@ -322,7 +331,7 @@
                     parent_style = self.tag_stack[-1][2]
 
         if hn(tag):
-            self.p()
+            self.p() # noqa: E127
             if start:
                 self.inheader = True
                 self.o(hn(tag)*"#" + ' ')
@@ -332,11 +341,11 @@
 
         if tag in ['p', 'div']:
             if options.google_doc:
-                if start and google_has_height(tag_style):
+                if start and _google_has_height(tag_style):
                     self.p()
                 else:
                     self.soft_br()
-            else:
+            else: # noqa: E127
                 self.p()
         
         if tag == "br" and start: self.o("  \n")
@@ -358,7 +367,7 @@
                 self.blockquote += 1
             else:
                 self.blockquote -= 1
-                self.p()
+                self.p() # noqa: E127
         
         if tag in ['em', 'i', 'u']: self.o("_")
         if tag in ['strong', 'b']: self.o("**")
@@ -370,7 +379,7 @@
 
         if options.google_doc:
             if not self.inheader:
-                # handle some font attributes, but leave headers clean
+                # обрабатывает некоторые атрибуты шрифта, но оставляет заголовки чистыми
                 self.handle_emphasis(start, tag_style, parent_style)
 
         if tag == "code" and not self.pre: self.o('`') #TODO: `` `this` ``
@@ -411,7 +420,7 @@
             self.lastWasList = False
         
         if tag == 'li':
-            self.pbr()
+            self.pbr() # noqa: E127
             if start:
                 if self.list: li = self.list[-1]
                 else: li = {'name':'ul', 'num':0}
@@ -419,7 +428,7 @@
                     nest_count = google_nest_count(tag_style)
                 else:
                     nest_count = len(self.list)
-                self.o("  " * nest_count) #TODO: line up <ol><li>s > 9 correctly.
+                self.o("  " * nest_count) # TODO: выровнять <ol><li>s > 9 правильно.
                 if li['name'] == "ul": self.o(options.ul_item_mark + " ")
                 elif li['name'] == "ol":
                     li['num'] += 1
@@ -431,10 +440,10 @@
         if tag in ["table", "tr"] and start: self.p()
         if tag == 'td': self.pbr()
         
-        if tag == "pre":
+        if tag == "pre": # noqa: E127
             if start:
                 self.startpre = 1
-                self.pre = 1
+                self.pre = 1 # noqa: E127
             else:
                 self.pre = 0
             self.p()
@@ -463,8 +472,8 @@
                 data = data[1:]
             if not data and not force: return
 
-            if self.startpre:
-                #self.out(" :") #TODO: not output when already one there
+            if self.startpre:  # noqa: E127
+                #self.out(" :") # TODO: не выводить, если уже есть
                 self.startpre = 0
             
             bq = (">" * self.blockquote)
@@ -473,7 +482,7 @@
                 bq += " "
             
             if self.pre:
-                bq += "    "
+                bq += "    " # noqa: E127
                 data = data.replace("\n", "\n"+bq)
             
             if self.start:
@@ -501,7 +510,7 @@
                     self.out("   ["+ str(link['count']) +"]: " + urlparse.urljoin(self.baseurl, link['href'])) 
                     if has_key(link, 'title'): self.out(" ("+link['title']+")")
                     self.out("\n")
-                    else:
+                    else: # noqa: E127
                         newa.append(link)
 
                 if self.a != newa: self.out("\n") # Don't need an extra line when nothing was done.
@@ -522,7 +531,7 @@
         self.o(data, 1)
     
     def unknown_decl(self, data): pass
-
+    
 def wrapwrite(text):
     text = text.encode('utf-8')
     try: #Python3
@@ -530,7 +539,7 @@
     except AttributeError:
         sys.stdout.write(text)
 
-def html2text_file(html, out=wrapwrite, baseurl=''):
+def html2text_file(html, out=wrapwrite, baseurl=None):
     h = _html2text(out, baseurl)
     h.feed(html)
     h.feed("")
@@ -540,14 +549,14 @@
     return optwrap(html2text_file(html, None, baseurl))
 
 class Storage: pass
-options = Storage()
+options = Storage() # noqa: F841
 options.google_doc = False
 options.ul_item_mark = '*'
 
 if __name__ == "__main__":
-    baseurl = ''
-    
-    p = optparse.OptionParser('%prog [(filename|url) [encoding]]',
+    baseurl = None
+    
+    parser = optparse.OptionParser('%prog [(filename|url) [encoding]]',
                               version='%prog ' + __version__)
     p.add_option("-g", "--google-doc", action="store_true", dest="google_doc",
         default=False, help="convert an html-exported Google Document")
@@ -568,11 +577,11 @@
 
     BODY_WIDTH = options.body_width
     GOOGLE_LIST_INDENT = options.list_indent
-
+    
     # process input
     if len(args) > 0:
         file_ = args[0]
-        encoding = None
+        encoding = None # noqa: F841
         if len(args) == 2:
             encoding = args[1]
         if len(args) > 2:
@@ -595,7 +604,7 @@
                 encoding = enc(j.headers, text)[0]
                 if encoding == 'us-ascii':
                     encoding = 'utf-8'
-            data = text.decode(encoding)
+            data = text.decode(encoding, errors='replace')
 
         else:
             data = open(file_, 'rb').read()
@@ -604,7 +613,7 @@
                     detect = lambda x: {'encoding': 'utf-8'}
                 encoding = detect(data)['encoding']
             data = data.decode(encoding)
-    else:
+    else: # noqa: E127
         data = sys.stdin.read()
     wrapwrite(html2text(data, baseurl))```