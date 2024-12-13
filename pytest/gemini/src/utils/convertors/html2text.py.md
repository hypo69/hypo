```python
import pytest
import html2text
from unittest.mock import patch
from io import StringIO
import sys

@pytest.fixture
def h2t():
    """Fixture to create an instance of _html2text class"""
    return html2text._html2text()


def test_unescape_valid_entity():
    """Test unescape with valid HTML entity."""
    assert html2text.unescape("&amp;") == "&"
    assert html2text.unescape("&lt;") == "<"
    assert html2text.unescape("&gt;") == ">"
    assert html2text.unescape("&quot;") == '"'
    assert html2text.unescape("&apos;") == "'"
    assert html2text.unescape("&nbsp;") == " "
    assert html2text.unescape("&#160;") == " " # testing for &#number;


def test_unescape_invalid_entity():
    """Test unescape with an invalid HTML entity."""
    assert html2text.unescape("&invalid;") == "&invalid;"

def test_unescape_hex_entity():
    """Test unescape with hexadecimal entity."""
    assert html2text.unescape("&#x20;") == " "
    assert html2text.unescape("&#x41;") == "A"


def test_unescape_no_entity():
    """Test unescape with no entity."""
    assert html2text.unescape("no entity") == "no entity"

def test_onlywhite_whitespace_only():
    """Test onlywhite with whitespace-only string."""
    assert html2text.onlywhite("   ") is " "
    assert html2text.onlywhite("\t\n ") is False  

def test_onlywhite_non_whitespace():
    """Test onlywhite with string containing non-whitespace."""
    assert html2text.onlywhite(" test ") is False
    assert html2text.onlywhite("test") is False
    assert html2text.onlywhite("   test") is False

def test_optwrap_no_wrap():
    """Test optwrap with BODY_WIDTH=0, should not wrap."""
    html2text.BODY_WIDTH = 0
    text = "This is a long line of text that should not be wrapped."
    assert html2text.optwrap(text) == text

def test_optwrap_wrap():
    """Test optwrap with BODY_WIDTH set to wrap the text."""
    html2text.BODY_WIDTH = 20
    text = "This is a long line of text that should be wrapped."
    expected = "This is a long line\nof text that should\nbe wrapped.\n\n"
    assert html2text.optwrap(text) == expected

def test_optwrap_wrap_with_newlines():
  """Test optwrap with newlines and indentations."""
  html2text.BODY_WIDTH = 20
  text = "  This is an indented line. \n\nThis is another line.\n\n     * This is an item"
  expected = "  This is an\nindented line.\n\nThis is another line.\n\n     * This is an\nitem\n\n"
  assert html2text.optwrap(text) == expected

def test_hn_valid_header():
    """Test hn with valid header tags."""
    assert html2text.hn("h1") == 1
    assert html2text.hn("h2") == 2
    assert html2text.hn("h6") == 6

def test_hn_invalid_header():
    """Test hn with invalid header tags."""
    assert html2text.hn("h0") == 0
    assert html2text.hn("h7") == 0
    assert html2text.hn("h") == 0
    assert html2text.hn("ha") == 0
    assert html2text.hn("h1a") == 0

def test_dumb_property_dict():
    """Test dumb_property_dict with various CSS styles."""
    style1 = "color: red; font-size: 12px;"
    expected1 = {"color": "red", "font-size": "12px"}
    assert html2text.dumb_property_dict(style1) == expected1

    style2 = "  margin-left: 10px;  padding: 5px ; "
    expected2 = {"margin-left": "10px", "padding": "5px"}
    assert html2text.dumb_property_dict(style2) == expected2
  
    style3 = ""
    expected3 = {}
    assert html2text.dumb_property_dict(style3) == expected3

    style4 = "color: red;"
    expected4 = {"color": "red"}
    assert html2text.dumb_property_dict(style4) == expected4

    style5 = "color:red; font-size:12px" #test without spaces
    expected5 = {"color": "red", "font-size":"12px"}
    assert html2text.dumb_property_dict(style5) == expected5

def test_dumb_css_parser():
  """Test dumb_css_parser with valid CSS data."""
  css_data = """
    .class1 { color: red; }
    #id1 { font-size: 14px; }
    .class2 { font-weight: bold; text-decoration: underline; }
    @import url("style.css");
    .class3 { margin: 10px; }
    @import url("other.css");
  """
  expected = {
    ".class1": {"color": "red"},
    "#id1": {"font-size": "14px"},
    ".class2": {"font-weight": "bold", "text-decoration": "underline"},
    ".class3": {"margin": "10px"}
  }
  assert html2text.dumb_css_parser(css_data) == expected

def test_dumb_css_parser_no_styles():
    """Test dumb_css_parser with empty or no styles."""
    assert html2text.dumb_css_parser("") == {}
    assert html2text.dumb_css_parser("  ") == {}
    assert html2text.dumb_css_parser("@import url('test.css');") == {}

def test_element_style():
    """Test element_style with various attributes and styles."""
    style_def = {
      ".class1": {"color": "red", "font-size": "12px"},
      ".class2": {"font-weight": "bold"}
    }
    parent_style = {"font-family": "Arial"}

    # Test case 1: With class and style attributes
    attrs1 = {"class": "class1 class2", "style": "text-align: center;"}
    expected1 = {"font-family": "Arial", "color": "red", "font-size": "12px", "font-weight": "bold", "text-align": "center"}
    assert html2text.element_style(attrs1, style_def, parent_style) == expected1
    
    # Test case 2: With only class attribute
    attrs2 = {"class": "class1"}
    expected2 = {"font-family": "Arial", "color": "red", "font-size": "12px"}
    assert html2text.element_style(attrs2, style_def, parent_style) == expected2

    # Test case 3: With only style attribute
    attrs3 = {"style": "font-style: italic;"}
    expected3 = {"font-family": "Arial", "font-style": "italic"}
    assert html2text.element_style(attrs3, style_def, parent_style) == expected3

    # Test case 4: With no style and class attribute
    attrs4 = {}
    expected4 = {"font-family": "Arial"}
    assert html2text.element_style(attrs4, style_def, parent_style) == expected4

    # Test case 5: With empty parent style
    empty_parent_style = {}
    expected5 = {"color": "red", "font-size": "12px", "font-weight": "bold", "text-align": "center"}
    assert html2text.element_style(attrs1, style_def, empty_parent_style) == expected5

    # Test case 6: With no matching class
    style_def = {}
    attrs6 = {"class": "class3", "style": "color:blue"}
    expected6 = {"color": "blue", "font-family": "Arial"}
    assert html2text.element_style(attrs6, style_def, parent_style) == expected6

def test_google_list_style():
  """Test google_list_style with different list styles."""
  style1 = {"list-style-type": "disc"}
  assert html2text.google_list_style(style1) == "ul"
  
  style2 = {"list-style-type": "circle"}
  assert html2text.google_list_style(style2) == "ul"
  
  style3 = {"list-style-type": "square"}
  assert html2text.google_list_style(style3) == "ul"
  
  style4 = {"list-style-type": "none"}
  assert html2text.google_list_style(style4) == "ul"

  style5 = {"list-style-type": "decimal"}
  assert html2text.google_list_style(style5) == "ol"

  style6 = {}
  assert html2text.google_list_style(style6) == "ol"


def test_google_nest_count():
    """Test google_nest_count with different margin-left values."""
    style1 = {"margin-left": "0px"}
    assert html2text.google_nest_count(style1) == 0

    style2 = {"margin-left": "36px"}
    assert html2text.google_nest_count(style2) == 1

    style3 = {"margin-left": "72px"}
    assert html2text.google_nest_count(style3) == 2

    style4 = {}
    assert html2text.google_nest_count(style4) == 0

def test_google_has_height():
  """Test google_has_height with different styles."""
  style1 = {"height": "20px"}
  assert html2text.google_has_height(style1) is True
  
  style2 = {}
  assert html2text.google_has_height(style2) is False

  style3 = {"margin": "10px"}
  assert html2text.google_has_height(style3) is False


def test_google_text_emphasis():
    """Test google_text_emphasis with different text styles."""
    style1 = {"text-decoration": "underline", "font-style": "italic", "font-weight": "bold"}
    assert html2text.google_text_emphasis(style1) == ["underline", "italic", "bold"]
    
    style2 = {"text-decoration": "line-through"}
    assert html2text.google_text_emphasis(style2) == ["line-through"]
    
    style3 = {"font-style": "italic"}
    assert html2text.google_text_emphasis(style3) == ["italic"]

    style4 = {"font-weight": "bold"}
    assert html2text.google_text_emphasis(style4) == ["bold"]

    style5 = {}
    assert html2text.google_text_emphasis(style5) == []

def test_google_fixed_width_font():
  """Test google_fixed_width_font with different font families."""
  style1 = {"font-family": "Courier New"}
  assert html2text.google_fixed_width_font(style1) is True
  
  style2 = {"font-family": "Consolas"}
  assert html2text.google_fixed_width_font(style2) is True

  style3 = {"font-family": "Arial"}
  assert html2text.google_fixed_width_font(style3) is False

  style4 = {}
  assert html2text.google_fixed_width_font(style4) is False

def test_list_numbering_start():
    """Test list_numbering_start with and without start attribute."""
    attrs1 = {"start": "5"}
    assert html2text.list_numbering_start(attrs1) == 4

    attrs2 = {}
    assert html2text.list_numbering_start(attrs2) == 0
    
    attrs3 = {"start": "1"}
    assert html2text.list_numbering_start(attrs3) == 0


def test_html2text_init(h2t):
    """Test initialization of _html2text class."""
    assert h2t.outtextlist == []
    assert h2t.quiet == 0
    assert h2t.p_p == 0
    assert h2t.outcount == 0
    assert h2t.start == 1
    assert h2t.space == 0
    assert h2t.a == []
    assert h2t.astack == []
    assert h2t.acount == 0
    assert h2t.list == []
    assert h2t.blockquote == 0
    assert h2t.pre == 0
    assert h2t.startpre == 0
    assert h2t.code is False
    assert h2t.br_toggle == ''
    assert h2t.lastWasNL == 0
    assert h2t.lastWasList is False
    assert h2t.style == 0
    assert h2t.style_def == {}
    assert h2t.tag_stack == []
    assert h2t.emphasis == 0
    assert h2t.drop_white_space == 0
    assert h2t.inheader is False
    assert h2t.abbr_title is None
    assert h2t.abbr_data is None
    assert h2t.abbr_list == {}

def test_html2text_feed(h2t):
    """Test the feed method to replace script tag"""
    h2t.feed("<script>alert('hello')</script>")
    assert h2t.outtextlist == []
    h2t.feed("<script>alert('hello')</ignore>")
    assert h2t.outtextlist == []
    h2t.feed("</script>")
    assert h2t.outtextlist == []
    h2t.feed("< /script>")
    assert h2t.outtextlist == []
    h2t.feed("</ ' + script>")
    assert h2t.outtextlist == []
    h2t.feed("</ignore>")

def test_html2text_outtextf(h2t):
  """Test the outtextf method of the _html2text class."""
  h2t.outtextf("test")
  assert h2t.outtextlist == ["test"]
  assert h2t.lastWasNL == False
  
  h2t.outtextf("test\n")
  assert h2t.outtextlist == ["test", "test\n"]
  assert h2t.lastWasNL == True

  h2t.outtextf("")
  assert h2t.outtextlist == ["test", "test\n", ""]
  assert h2t.lastWasNL == False


def test_html2text_close(h2t):
    """Test the close method of the _html2text class."""
    h2t.outtextlist = ["test1", "test2", "test3"]
    h2t.outtext = ""
    result = h2t.close()
    assert result == "test1test2test3\n"
    
def test_html2text_close_google_doc(h2t):
    """Test the close method of the _html2text class with google doc option."""
    h2t.outtextlist = ["test&nbsp_place_holder;test"]
    h2t.outtext = ""
    html2text.options.google_doc = True
    result = h2t.close()
    assert result == "test test\n"
    html2text.options.google_doc = False #reset option to default

def test_html2text_handle_charref(h2t):
    """Test handle_charref method."""
    h2t.handle_charref("34")
    assert h2t.outtextlist == ['"']

def test_html2text_handle_entityref(h2t):
    """Test handle_entityref method."""
    h2t.handle_entityref("amp")
    assert h2t.outtextlist == ['&']

def test_html2text_handle_starttag(h2t):
    """Test handle_starttag method (basic check)."""
    h2t.handle_starttag("p", [])
    assert h2t.outtextlist == ['\n\n']

def test_html2text_handle_endtag(h2t):
    """Test handle_endtag method."""
    h2t.handle_endtag("p")
    assert h2t.outtextlist == []

def test_html2text_previousIndex(h2t):
  """Test the previousIndex method with different scenarios."""
  # Test case 1: No links added yet.
  attrs1 = {"href": "http://example.com"}
  assert h2t.previousIndex(attrs1) is None

  # Test case 2: A link with the same href
  h2t.a = [{"href": "http://example.com"}]
  assert h2t.previousIndex(attrs1) == 0

  # Test case 3: A link with the same href but different title
  attrs2 = {"href": "http://example.com", "title": "link1"}
  h2t.a = [{"href": "http://example.com", "title": "link2"}]
  assert h2t.previousIndex(attrs2) is None
  
  # Test case 4: A link with the same href and same title
  h2t.a = [{"href": "http://example.com", "title": "link1"}]
  assert h2t.previousIndex(attrs2) == 0
  
  # Test case 5: Links with different hrefs
  attrs3 = {"href": "http://example2.com"}
  h2t.a = [{"href": "http://example.com"}, {"href":"http://example2.com"}]
  assert h2t.previousIndex(attrs3) == 1

  # Test case 6: No href in attrs
  attrs4 = {"title": "test"}
  assert h2t.previousIndex(attrs4) is None


def test_html2text_drop_last(h2t):
  """Test drop_last method of the _html2text class."""
  h2t.outtext = "teststring"
  h2t.drop_last(4)
  assert h2t.outtext == "test"

  h2t.outtext = "teststring"
  h2t.quiet = 1
  h2t.drop_last(4)
  assert h2t.outtext == "teststring"


def test_html2text_handle_emphasis(h2t):
    """Test handle_emphasis method."""
    
    #Mock options to be able to call handle_emphasis
    html2text.options.hide_strikethrough = False
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    
    #Test case 1: Bold tag
    tag_style = {"font-weight": "bold"}
    parent_style = {}
    h2t.handle_emphasis(True, tag_style, parent_style)
    assert h2t.outtextlist == ["**"]
    assert h2t.emphasis == 1
    assert h2t.drop_white_space == 1
    h2t.handle_emphasis(False, tag_style, parent_style)
    assert h2t.outtextlist == ["**", "**", " "]
    assert h2t.emphasis == 0
    assert h2t.drop_white_space == 0

    #Test case 2: Italic tag
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    tag_style = {"font-style": "italic"}
    h2t.handle_emphasis(True, tag_style, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_"]
    assert h2t.emphasis == 1
    assert h2t.drop_white_space == 1
    h2t.handle_emphasis(False, tag_style, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " "]
    assert h2t.emphasis == 0
    assert h2t.drop_white_space == 0
    
    #Test case 3: Fixed-width font tag
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    h2t.code = False
    tag_style = {"font-family": "Courier New"}
    h2t.handle_emphasis(True, tag_style, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " ", "`"]
    assert h2t.emphasis == 1
    assert h2t.drop_white_space == 1
    assert h2t.code is True
    h2t.handle_emphasis(False, tag_style, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " ", "`", "`"]
    assert h2t.emphasis == 0
    assert h2t.drop_white_space == 0
    assert h2t.code is False

    #Test case 4: strikethrough tag with hide_strikethrough
    html2text.options.hide_strikethrough = True
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    tag_style = {"text-decoration": "line-through"}
    h2t.handle_emphasis(True, tag_style, parent_style)
    assert h2t.quiet == 1
    h2t.handle_emphasis(False, tag_style, parent_style)
    assert h2t.quiet == 0
    html2text.options.hide_strikethrough = False #reset to default

    #Test case 5: Bold tag, nested
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    tag_style_bold = {"font-weight": "bold"}
    parent_style_bold = {"font-weight": "bold"}
    h2t.handle_emphasis(True, tag_style_bold, {})
    assert h2t.outtextlist == ["**"]
    h2t.handle_emphasis(True, tag_style_bold, parent_style_bold)
    assert h2t.outtextlist == ["**"]
    h2t.handle_emphasis(False, tag_style_bold, parent_style_bold)
    assert h2t.outtextlist == ["**"]
    h2t.handle_emphasis(False, tag_style_bold, {})
    assert h2t.outtextlist == ["**", "**", " "]

    # Test case 6: empty emphasis, should be removed
    h2t.outtext = "test "
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    tag_style_italic = {"font-style": "italic"}
    h2t.handle_emphasis(True, tag_style_italic, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_"]
    h2t.handle_emphasis(False, tag_style_italic, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " "]
    assert h2t.outtext == "test "

    h2t.outtext = "test "
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    tag_style_bold = {"font-weight": "bold"}
    h2t.handle_emphasis(True, tag_style_bold, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " ", "**"]
    h2t.handle_emphasis(False, tag_style_bold, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " ", "**", "**", " "]
    assert h2t.outtext == "test "

    h2t.outtext = "test "
    h2t.emphasis = 0
    h2t.quiet = 0
    h2t.drop_white_space = 0
    h2t.code = False
    tag_style_fixed = {"font-family": "Courier New"}
    h2t.handle_emphasis(True, tag_style_fixed, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " ", "**", "**", " ", "`"]
    h2t.handle_emphasis(False, tag_style_fixed, parent_style)
    assert h2t.outtextlist == ["**", "**", " ", "_", "_", " ", "**", "**", " ", "`", "`"]
    assert h2t.outtext == "test "
    

def test_html2text_handle_tag(h2t):
    """Test handle_tag method with various scenarios."""

    # Mock google_doc to avoid parent style
    html2text.options.google_doc = False
    # Test case 1: Header tag start
    h2t.handle_tag("h1", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# "]
    assert h2t.inheader is True

    # Test case 2: Header tag end
    h2t.handle_tag("h1", {}, 0)
    assert h2t.inheader is False
    
    # Test case 3: Paragraph start
    h2t.handle_tag("p", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n"]

    # Test case 4: Break tag
    h2t.handle_tag("br", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n"]

    # Test case 5: Horizontal Rule tag
    h2t.handle_tag("hr", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n"]

    # Test case 6: head, style, script start tag
    h2t.quiet = 0
    h2t.handle_tag("head", {}, 1)
    assert h2t.quiet == 1
    h2t.handle_tag("style", {}, 1)
    assert h2t.quiet == 2
    h2t.handle_tag("script", {}, 1)
    assert h2t.quiet == 3

    # Test case 7: head, style, script end tag
    h2t.handle_tag("head", {}, 0)
    assert h2t.quiet == 2
    h2t.handle_tag("style", {}, 0)
    assert h2t.quiet == 1
    h2t.handle_tag("script", {}, 0)
    assert h2t.quiet == 0
    
    # Test case 8: body tag
    h2t.quiet = 1
    h2t.handle_tag("body", {}, 1)
    assert h2t.quiet == 0
    
    # Test case 9: blockquote start
    h2t.blockquote = 0
    h2t.handle_tag("blockquote", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> "]
    assert h2t.blockquote == 1

    # Test case 10: blockquote end
    h2t.handle_tag("blockquote", {}, 0)
    assert h2t.blockquote == 0
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n"]

    # Test case 11: em, i, u tag
    h2t.handle_tag("em", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_"]
    h2t.handle_tag("i", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_"]
    h2t.handle_tag("u", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_"]

    # Test case 12: strong, b tag
    h2t.handle_tag("strong", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**"]
    h2t.handle_tag("b", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**", "**"]

    # Test case 13: del, strike tag
    h2t.handle_tag("del", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**", "**", "<del>"]
    h2t.handle_tag("del", {}, 0)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**", "**", "<del>", "</del>"]
    h2t.handle_tag("strike", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**", "**", "<del>", "</del>", "<strike>"]
    h2t.handle_tag("strike", {}, 0)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**", "**", "<del>", "</del>", "<strike>", "</strike>"]

    # Test case 14: code tag
    h2t.pre = 0
    h2t.handle_tag("code", {}, 1)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**", "**", "<del>", "</del>", "<strike>", "</strike>", "`"]
    h2t.handle_tag("code", {}, 0)
    assert h2t.outtextlist == ["\n\n", "# ", "\n\n", "  \n", "\n", "* * *", "\n\n", "\n\n", "> ", "\n\n", "_", "_", "_", "**", "**", "<del>", "</del>", "<strike>", "</strike>", "`"]
    
    # Test case 15: abbr tag
    h2t.abbr_title = None
    h2t.abbr_data = None
    h2t.abbr_list = {}
    h2t.handle_tag("abbr", {"title": "Test Abbr"}, 1)
    assert h2t.abbr_title == "Test Abbr"
    assert h2t.abbr_data == ""
    h2t.handle_tag("abbr", {}, 0)
    assert h2t.abbr_title is None
    assert h2t.abbr_data == ""
    assert h2t.abbr_list == {}
    
    h2t.handle_data("ABBR")
    h2t.handle_tag("abbr", {"title": "Test Abbr"}, 1)
    h2t.handle_data("Inner")
    h2t.handle_tag("abbr", {}, 0)
    assert h2t.abbr_list == {"Inner": "Test Abbr