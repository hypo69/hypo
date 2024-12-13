```python
import pytest
import os
from pathlib import Path
from unittest.mock import mock_open, patch

# Assuming the code is in a file named 'convertors.py' in the same directory as the tests
# and that all modules are accessible through the __init__.py file
from hypotez.src.utils.convertors import (
    base64_to_tmpfile,
    base64encode,
    csv2dict,
    csv2ns,
    dict2ns,
    dict2csv,
    dict2html,
    dict2xls,
    dict2xml,
    replace_key_in_dict,
    dot2png,
    html2escape,
    html2ns,
    html2dict,
    escape2html,
    html2text,
    html2text_file,
    google_fixed_width_font,
    google_has_height,
    google_list_style,
    google_nest_count,
    google_text_emphasis,
    dumb_css_parser,
    dumb_property_dict,
    json2csv,
    json2ns,
    json2xls,
    json2xml,
    md2dict,
    ns2csv,
    ns2dict,
    ns2xls,
    ns2xml,
    TextToImageGenerator,
    webp2png,
    speech_recognizer,
    text2speech,
    decode_unicode_escape,
    xml2dict,
    xls2dict,
)


# --- Fixtures ---
@pytest.fixture
def sample_csv_file(tmp_path):
    """Provides a sample CSV file for testing."""
    csv_content = "name,age\nJohn,30\nJane,25"
    csv_file = tmp_path / "sample.csv"
    with open(csv_file, "w") as f:
        f.write(csv_content)
    return csv_file


@pytest.fixture
def sample_json_file(tmp_path):
    """Provides a sample JSON file for testing."""
    json_content = '{"name": "John", "age": 30}'
    json_file = tmp_path / "sample.json"
    with open(json_file, "w") as f:
        f.write(json_content)
    return json_file


@pytest.fixture
def sample_html_file(tmp_path):
    """Provides a sample HTML file for testing."""
    html_content = "<html><body><h1>Hello</h1><p>World</p></body></html>"
    html_file = tmp_path / "sample.html"
    with open(html_file, "w") as f:
        f.write(html_content)
    return html_file

@pytest.fixture
def sample_xls_file(tmp_path):
    """Provides a sample xls file for testing."""
    xls_file = tmp_path / "sample.xls"
    # Since creating a valid .xls file within a test is complex, we will mock its reading
    # For actual testing of xls file interaction, we will mock the xls2dict function.
    return xls_file


@pytest.fixture
def sample_xml_file(tmp_path):
    """Provides a sample XML file for testing."""
    xml_content = "<root><name>John</name><age>30</age></root>"
    xml_file = tmp_path / "sample.xml"
    with open(xml_file, "w") as f:
        f.write(xml_content)
    return xml_file


@pytest.fixture
def sample_base64_string():
    """Provides a sample base64 string for testing."""
    return "SGVsbG8gV29ybGQh"


@pytest.fixture
def sample_dict():
    """Provides a sample dict for testing."""
    return {"name": "John", "age": 30}


@pytest.fixture
def sample_ns():
    """Provides a sample Namespace for testing."""
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    return Namespace(name="John", age=30)

@pytest.fixture
def sample_md_file(tmp_path):
    """Provides a sample markdown file for testing."""
    md_content = "# Hello World\nThis is a test."
    md_file = tmp_path / "sample.md"
    with open(md_file, "w") as f:
        f.write(md_content)
    return md_file

@pytest.fixture
def sample_unicode_string():
    """Provides a sample unicode string for testing."""
    return r"Hello\u0020World\u0021"


# --- Tests for base64 ---
def test_base64_to_tmpfile(sample_base64_string, tmp_path):
    """Test base64_to_tmpfile function."""
    tmp_file = base64_to_tmpfile(sample_base64_string, tmp_path)
    assert isinstance(tmp_file, Path)
    assert tmp_file.exists()
    with open(tmp_file, "r") as f:
        assert f.read() == "Hello World!"


def test_base64encode():
    """Test base64encode function."""
    assert base64encode("Hello World!") == "SGVsbG8gV29ybGQh"
    assert base64encode(b"Hello World!") == "SGVsbG8gV29ybGQh"


# --- Tests for csv ---
def test_csv2dict_valid(sample_csv_file):
    """Test csv2dict with valid input."""
    result = csv2dict(sample_csv_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"name": "John", "age": "30"}
    assert result[1] == {"name": "Jane", "age": "25"}


def test_csv2dict_invalid_file():
    """Test csv2dict with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        csv2dict("invalid.csv")


def test_csv2ns_valid(sample_csv_file):
    """Test csv2ns with valid input."""
    result = csv2ns(sample_csv_file)
    assert hasattr(result, 'name')
    assert hasattr(result, 'age')
    assert result.name == ['John','Jane']
    assert result.age == ['30','25']

def test_csv2ns_invalid_file():
    """Test csv2ns with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        csv2ns("invalid.csv")

# --- Tests for dict ---
def test_dict2ns_valid(sample_dict):
    """Test dict2ns with valid input."""
    result = dict2ns(sample_dict)
    assert hasattr(result, 'name')
    assert hasattr(result, 'age')
    assert result.name == "John"
    assert result.age == 30


def test_dict2csv_valid(sample_dict, tmp_path):
    """Test dict2csv with valid input."""
    csv_file = tmp_path / "output.csv"
    dict2csv(sample_dict, csv_file)
    assert csv_file.exists()
    with open(csv_file, "r") as f:
        content = f.read()
        assert "name,age\nJohn,30\n" == content


def test_dict2html_valid(sample_dict):
    """Test dict2html with valid input."""
    result = dict2html(sample_dict)
    assert "<table" in result
    assert "John" in result
    assert "30" in result


def test_dict2xls_valid(sample_dict, tmp_path):
    """Test dict2xls with valid input."""
    xls_file = tmp_path / "output.xls"

    # Mock the function logic since it's complex.
    with patch("hypotez.src.utils.convertors.dict.dict2xls") as mock_dict2xls:
       dict2xls(sample_dict, xls_file)
       mock_dict2xls.assert_called_once_with(sample_dict, xls_file)

def test_dict2xml_valid(sample_dict):
    """Test dict2xml with valid input."""
    result = dict2xml(sample_dict)
    assert "<name>John</name>" in result
    assert "<age>30</age>" in result


def test_replace_key_in_dict(sample_dict):
    """Test replace_key_in_dict function."""
    result = replace_key_in_dict(sample_dict, "name", "fullname")
    assert "fullname" in result
    assert "name" not in result
    assert result["fullname"] == "John"


# --- Tests for dot ---
def test_dot2png(tmp_path):
    """Test dot2png function."""
    dot_content = 'digraph G { rankdir=LR; a [label="first"]; b [label="second"]; a -> b; }'
    png_file = tmp_path / "output.png"

    # Mocking the subprocess.run since it is not the point of test
    with patch("hypotez.src.utils.convertors.dot.subprocess.run") as mock_run:
        dot2png(dot_content, png_file)
        mock_run.assert_called_once()


# --- Tests for html ---
def test_html2escape(sample_html_file):
    """Test html2escape function."""
    with open(sample_html_file, "r") as f:
        html_content = f.read()

    escaped = html2escape(html_content)
    assert "&lt;html&gt;" in escaped
    assert "&lt;body&gt;" in escaped
    assert "&lt;h1&gt;" in escaped
    assert "&lt;p&gt;" in escaped


def test_html2ns_valid(sample_html_file):
    """Test html2ns with valid input."""
    result = html2ns(sample_html_file)
    assert hasattr(result, 'h1')
    assert hasattr(result, 'p')
    assert result.h1 == "Hello"
    assert result.p == "World"

def test_html2ns_invalid_file():
    """Test html2ns with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        html2ns("invalid.html")


def test_html2dict_valid(sample_html_file):
    """Test html2dict with valid input."""
    result = html2dict(sample_html_file)
    assert isinstance(result, dict)
    assert "h1" in result
    assert "p" in result
    assert result["h1"] == "Hello"
    assert result["p"] == "World"


def test_escape2html():
    """Test escape2html function."""
    escaped = "&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello&lt;/h1&gt;&lt;p&gt;World&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;"
    unescaped = escape2html(escaped)
    assert "<html>" in unescaped
    assert "<body>" in unescaped
    assert "<h1>" in unescaped
    assert "<p>" in unescaped

# --- Tests for html2text ---
def test_html2text_valid(sample_html_file):
    """Test html2text function."""
    with open(sample_html_file, "r") as f:
        html_content = f.read()
    result = html2text(html_content)
    assert "Hello" in result
    assert "World" in result
    assert isinstance(result, str)

def test_html2text_file_valid(sample_html_file):
    """Test html2text_file function."""
    result = html2text_file(sample_html_file)
    assert "Hello" in result
    assert "World" in result
    assert isinstance(result, str)

def test_html2text_file_invalid_file():
    """Test html2text_file with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        html2text_file("invalid.html")


def test_google_fixed_width_font():
    """Test google_fixed_width_font function."""
    assert google_fixed_width_font("pre") == True
    assert google_fixed_width_font("code") == True
    assert google_fixed_width_font("other") == False


def test_google_has_height():
    """Test google_has_height function."""
    assert google_has_height({"style": "height: 20px;"})
    assert not google_has_height({"style": "width: 20px;"})


def test_google_list_style():
    """Test google_list_style function."""
    assert google_list_style("ul")
    assert google_list_style("ol")
    assert not google_list_style("p")


def test_google_nest_count():
    """Test google_nest_count function."""
    node = {"parent": {"parent": {}}}
    assert google_nest_count(node) == 2
    assert google_nest_count({}) == 0


def test_google_text_emphasis():
    """Test google_text_emphasis function."""
    assert google_text_emphasis("b") == True
    assert google_text_emphasis("strong") == True
    assert google_text_emphasis("i") == True
    assert google_text_emphasis("em") == True
    assert google_text_emphasis("other") == False


def test_dumb_css_parser():
    """Test dumb_css_parser function."""
    style = "color: red; font-size: 12px;"
    parsed = dumb_css_parser(style)
    assert "color" in parsed
    assert "font-size" in parsed
    assert parsed["color"] == "red"
    assert parsed["font-size"] == "12px"


def test_dumb_property_dict():
    """Test dumb_property_dict function."""
    attrs = {'class': 'test-class', 'style': 'color: red;'}
    parsed = dumb_property_dict(attrs)
    assert "class" in parsed
    assert "style" in parsed
    assert parsed["class"] == "test-class"
    assert parsed["style"] == 'color: red;'



# --- Tests for json ---
def test_json2csv_valid(sample_json_file, tmp_path):
    """Test json2csv with valid input."""
    csv_file = tmp_path / "output.csv"
    json2csv(sample_json_file, csv_file)
    assert csv_file.exists()
    with open(csv_file, "r") as f:
       content = f.read()
       assert "name,age\nJohn,30\n" == content

def test_json2csv_invalid_file():
    """Test json2csv with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        json2csv("invalid.json", "output.csv")


def test_json2ns_valid(sample_json_file):
    """Test json2ns with valid input."""
    result = json2ns(sample_json_file)
    assert hasattr(result, 'name')
    assert hasattr(result, 'age')
    assert result.name == "John"
    assert result.age == 30

def test_json2ns_invalid_file():
    """Test json2ns with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        json2ns("invalid.json")


def test_json2xls_valid(sample_json_file, tmp_path):
    """Test json2xls with valid input."""
    xls_file = tmp_path / "output.xls"
    
    # Mock the function logic since it's complex.
    with patch("hypotez.src.utils.convertors.json.json2xls") as mock_json2xls:
       json2xls(sample_json_file, xls_file)
       mock_json2xls.assert_called_once_with(sample_json_file, xls_file)


def test_json2xml_valid(sample_json_file):
    """Test json2xml with valid input."""
    result = json2xml(sample_json_file)
    assert "<name>John</name>" in result
    assert "<age>30</age>" in result

# --- Tests for md2dict ---
def test_md2dict_valid(sample_md_file):
    """Test md2dict with valid input."""
    result = md2dict(sample_md_file)
    assert isinstance(result, dict)
    assert "h1" in result
    assert "p" in result
    assert result["h1"] == "Hello World"
    assert result["p"] == "This is a test."

def test_md2dict_invalid_file():
    """Test md2dict with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        md2dict("invalid.md")

# --- Tests for ns ---
def test_ns2csv_valid(sample_ns, tmp_path):
    """Test ns2csv with valid input."""
    csv_file = tmp_path / "output.csv"
    ns2csv(sample_ns, csv_file)
    assert csv_file.exists()
    with open(csv_file, "r") as f:
        content = f.read()
        assert "name,age\nJohn,30\n" == content


def test_ns2dict_valid(sample_ns):
    """Test ns2dict with valid input."""
    result = ns2dict(sample_ns)
    assert isinstance(result, dict)
    assert result["name"] == "John"
    assert result["age"] == 30


def test_ns2xls_valid(sample_ns, tmp_path):
    """Test ns2xls with valid input."""
    xls_file = tmp_path / "output.xls"

    # Mock the function logic since it's complex.
    with patch("hypotez.src.utils.convertors.ns.ns2xls") as mock_ns2xls:
       ns2xls(sample_ns, xls_file)
       mock_ns2xls.assert_called_once_with(sample_ns, xls_file)


def test_ns2xml_valid(sample_ns):
    """Test ns2xml with valid input."""
    result = ns2xml(sample_ns)
    assert "<name>John</name>" in result
    assert "<age>30</age>" in result

# --- Tests for png ---
def test_text_to_image_generator(tmp_path):
    """Test TextToImageGenerator class."""
    generator = TextToImageGenerator(font_path="arial.ttf") # Use arial if available on test environment. Mock otherwise
    image_file = tmp_path / "output.png"
    with patch("hypotez.src.utils.convertors.png.ImageFont.truetype") as mock_truetype, \
            patch("hypotez.src.utils.convertors.png.Image.new") as mock_new_image, \
            patch("hypotez.src.utils.convertors.png.ImageDraw.Draw") as mock_draw, \
            patch("hypotez.src.utils.convertors.png.Image.save") as mock_save:
      generator.generate("Hello World", image_file)
      mock_truetype.assert_called_once()
      mock_new_image.assert_called_once()
      mock_draw.assert_called_once()
      mock_save.assert_called_once()

def test_webp2png(tmp_path):
    """Test webp2png function."""
    webp_file = tmp_path / "sample.webp" # create dummy file
    png_file = tmp_path / "output.png"
    with open(webp_file, "w") as f:
       f.write("webp file")

    with patch("hypotez.src.utils.convertors.png.subprocess.run") as mock_run:
        webp2png(webp_file, png_file)
        mock_run.assert_called_once()


# --- Tests for tts ---
def test_speech_recognizer():
    """Test speech_recognizer function."""
    # Mock the speech_recognizer function to avoid external calls.
    with patch("hypotez.src.utils.convertors.tts.speech_recognizer") as mock_recognizer:
        mock_recognizer.return_value = "Hello World"
        result = speech_recognizer("test.wav")
        assert result == "Hello World"

def test_text2speech():
    """Test text2speech function."""
     # Mock the text2speech function to avoid external calls.
    with patch("hypotez.src.utils.convertors.tts.text2speech") as mock_text2speech:
        mock_text2speech.return_value = b"audio_data" # Mock the return value of the actual text2speech function
        result = text2speech("Hello World", "output.mp3")
        assert result == b"audio_data"

# --- Tests for unicode ---
def test_decode_unicode_escape(sample_unicode_string):
    """Test decode_unicode_escape function."""
    result = decode_unicode_escape(sample_unicode_string)
    assert result == "Hello World!"

# --- Tests for xml2dict ---
def test_xml2dict_valid(sample_xml_file):
    """Test xml2dict with valid input."""
    result = xml2dict(sample_xml_file)
    assert isinstance(result, dict)
    assert result["name"] == "John"
    assert result["age"] == "30"


def test_xml2dict_invalid_file():
    """Test xml2dict with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        xml2dict("invalid.xml")

# --- Tests for xls ---
def test_xls2dict_valid(sample_xls_file):
    """Test xls2dict with valid input."""
    # Mock the function to return a known result
    with patch("hypotez.src.utils.convertors.xls.xls2dict") as mock_xls2dict:
      mock_xls2dict.return_value = [{"name": "John", "age": "30"}]
      result = xls2dict(sample_xls_file)
      assert isinstance(result, list)
      assert result == [{"name": "John", "age": "30"}]

def test_xls2dict_invalid_file():
    """Test xls2dict with an invalid file path."""
    with pytest.raises(FileNotFoundError):
        xls2dict("invalid.xls")
```