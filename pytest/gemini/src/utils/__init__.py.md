```python
import pytest
from hypotez.src.utils import *
import os
import tempfile
import json
import csv
from datetime import datetime, timedelta
from pathlib import Path
from PIL import Image


# Fixture for creating temporary files
@pytest.fixture
def temp_files():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Teardown: remove temporary files and directory
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))
    os.rmdir(temp_dir)
    

# --- Tests for convertors module ---

def test_TextToImageGenerator_valid_text(temp_files):
    """Checks if TextToImageGenerator generates an image for a valid text."""
    generator = TextToImageGenerator()
    img_path = os.path.join(temp_files, "test_image.png")
    generator.generate(text="Test text", output_path=img_path)
    assert os.path.exists(img_path)

def test_base64_to_tmpfile_valid_base64(temp_files):
    """Checks if base64_to_tmpfile correctly saves base64 encoded data to a tmpfile."""
    test_data = b"Test Data"
    base64_data = base64encode(test_data)
    tmp_file = base64_to_tmpfile(base64_data, temp_dir=temp_files)
    assert os.path.exists(tmp_file)
    with open(tmp_file, "rb") as f:
        content = f.read()
    assert content == test_data

def test_base64encode_valid_data():
    """Checks if base64encode correctly encodes data."""
    test_data = b"Test Data"
    encoded_data = base64encode(test_data)
    assert isinstance(encoded_data, str)

def test_csv2dict_valid_csv(temp_files):
    """Checks if csv2dict correctly converts a CSV file to a dictionary."""
    csv_path = os.path.join(temp_files, "test.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["header1", "header2"])
        writer.writerow(["value1", "value2"])
    
    result = csv2dict(csv_path)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == {"header1": "value1", "header2": "value2"}

def test_csv2dict_empty_csv(temp_files):
    """Checks if csv2dict handles an empty CSV file."""
    csv_path = os.path.join(temp_files, "empty.csv")
    open(csv_path, 'a').close()  
    result = csv2dict(csv_path)
    assert result == []

def test_csv2ns_valid_csv(temp_files):
    """Checks if csv2ns correctly converts a CSV file to a namespace."""
    csv_path = os.path.join(temp_files, "test.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["header1", "header2"])
        writer.writerow(["value1", "value2"])

    result = csv2ns(csv_path)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].header1 == "value1"
    assert result[0].header2 == "value2"

def test_decode_unicode_escape_valid_string():
    """Checks if decode_unicode_escape correctly decodes unicode escape sequences."""
    test_string = "\\u041f\\u0440\\u0438\\u0432\\u0435\\u0442" # Привет in unicode escape sequences
    result = decode_unicode_escape(test_string)
    assert result == "Привет"

def test_dict2csv_valid_dict(temp_files):
    """Checks if dict2csv correctly saves a dict to a csv file."""
    test_data = [{"header1": "value1", "header2": "value2"}]
    csv_path = os.path.join(temp_files, "output.csv")
    dict2csv(test_data, csv_path)
    assert os.path.exists(csv_path)
    with open(csv_path, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    assert rows == test_data


def test_dict2html_valid_dict():
    """Checks if dict2html correctly converts a dict to an html table."""
    test_data = [{"header1": "value1", "header2": "value2"}]
    result = dict2html(test_data)
    assert "<table>" in result
    assert "<th>header1</th>" in result
    assert "<td>value1</td>" in result

def test_dict2ns_valid_dict():
    """Checks if dict2ns correctly converts a dictionary to a namespace."""
    test_data = {"header1": "value1", "header2": "value2"}
    result = dict2ns(test_data)
    assert result.header1 == "value1"
    assert result.header2 == "value2"

def test_dict2xls_valid_dict(temp_files):
    """Checks if dict2xls correctly saves a dict to an xlsx file."""
    test_data = [{"header1": "value1", "header2": "value2"}]
    xls_path = os.path.join(temp_files, "output.xlsx")
    dict2xls(test_data, xls_path)
    assert os.path.exists(xls_path)

def test_dict2xml_valid_dict():
    """Checks if dict2xml correctly converts a dict to an xml string."""
    test_data = {"header1": "value1", "header2": "value2"}
    result = dict2xml(test_data)
    assert "<header1>value1</header1>" in result
    assert "<header2>value2</header2>" in result
    
def test_dot2png_valid_dot(temp_files):
    """Checks if dot2png can generate a png file from a valid dot file."""
    dot_data = "digraph G { a -> b; }"
    dot_path = os.path.join(temp_files, "test.dot")
    png_path = os.path.join(temp_files, "test.png")
    with open(dot_path, 'w') as f:
        f.write(dot_data)
    dot2png(dot_path, png_path)
    assert os.path.exists(png_path)

def test_escape2html_valid_string():
    """Checks if escape2html correctly escapes html entities in a string."""
    test_string = "<script>alert('Hello')</script>"
    result = escape2html(test_string)
    assert "&lt;script&gt;alert(&#39;Hello&#39;)&lt;/script&gt;" == result

def test_html2dict_valid_html():
    """Checks if html2dict correctly converts an html table to a dict."""
    test_html = "<table><tr><th>header1</th><th>header2</th></tr><tr><td>value1</td><td>value2</td></tr></table>"
    result = html2dict(test_html)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == {"header1": "value1", "header2": "value2"}

def test_html2escape_valid_html():
    """Checks if html2escape correctly escapes characters in html."""
    test_html = "<p>Test &amp; more</p>"
    result = html2escape(test_html)
    assert result == "&lt;p&gt;Test &amp;amp; more&lt;/p&gt;"

def test_html2ns_valid_html():
    """Checks if html2ns correctly converts an html table to a namespace."""
    test_html = "<table><tr><th>header1</th><th>header2</th></tr><tr><td>value1</td><td>value2</td></tr></table>"
    result = html2ns(test_html)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].header1 == "value1"
    assert result[0].header2 == "value2"

def test_html2text_valid_html():
    """Checks if html2text correctly converts html to text."""
    test_html = "<h1>Header</h1><p>Paragraph <b>bold</b> text.</p>"
    result = html2text(test_html)
    assert result == "Header\nParagraph bold text."

def test_html2text_file_valid_html_file(temp_files):
    """Checks if html2text_file correctly converts an html file to text."""
    html_path = os.path.join(temp_files, "test.html")
    text_path = os.path.join(temp_files, "output.txt")
    with open(html_path, "w") as f:
        f.write("<h1>Header</h1><p>Paragraph</p>")
    html2text_file(html_path, text_path)
    assert os.path.exists(text_path)
    with open(text_path, "r") as f:
        content = f.read()
    assert content == "Header\nParagraph"

def test_json2csv_valid_json(temp_files):
    """Checks if json2csv correctly converts json to a csv file."""
    test_data = [{"header1": "value1", "header2": "value2"}]
    json_path = os.path.join(temp_files, "test.json")
    csv_path = os.path.join(temp_files, "output.csv")
    with open(json_path, "w") as f:
        json.dump(test_data, f)
    json2csv(json_path, csv_path)
    assert os.path.exists(csv_path)
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows == test_data

def test_json2ns_valid_json(temp_files):
    """Checks if json2ns correctly converts json to a namespace."""
    test_data = [{"header1": "value1", "header2": "value2"}]
    json_path = os.path.join(temp_files, "test.json")
    with open(json_path, "w") as f:
        json.dump(test_data, f)
    result = json2ns(json_path)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].header1 == "value1"
    assert result[0].header2 == "value2"
    
def test_json2xls_valid_json(temp_files):
    """Checks if json2xls correctly converts json to an xlsx file."""
    test_data = [{"header1": "value1", "header2": "value2"}]
    json_path = os.path.join(temp_files, "test.json")
    xls_path = os.path.join(temp_files, "output.xlsx")
    with open(json_path, "w") as f:
        json.dump(test_data, f)
    json2xls(json_path, xls_path)
    assert os.path.exists(xls_path)

def test_json2xml_valid_json(temp_files):
    """Checks if json2xml correctly converts json to an xml string."""
    test_data = {"header1": "value1", "header2": "value2"}
    json_path = os.path.join(temp_files, "test.json")
    with open(json_path, "w") as f:
        json.dump(test_data, f)
    result = json2xml(json_path)
    assert "<header1>value1</header1>" in result
    assert "<header2>value2</header2>" in result

def test_md2dict_valid_md():
    """Checks if md2dict correctly converts a markdown file to a dict."""
    test_md = "# Header\n\n* Item 1\n* Item 2"
    result = md2dict(test_md)
    assert isinstance(result, dict)
    assert 'Header' in result
    assert 'Item 1' in result
    assert 'Item 2' in result

def test_ns2csv_valid_ns(temp_files):
    """Checks if ns2csv correctly saves namespace data to a csv file."""
    test_data = [type('TestNS', (object,), {"header1": "value1", "header2": "value2"})()]
    csv_path = os.path.join(temp_files, "output.csv")
    ns2csv(test_data, csv_path)
    assert os.path.exists(csv_path)
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows[0] == {"header1": "value1", "header2": "value2"}
    
def test_ns2dict_valid_ns():
    """Checks if ns2dict correctly converts a namespace to a dict."""
    test_data = type('TestNS', (object,), {"header1": "value1", "header2": "value2"})()
    result = ns2dict(test_data)
    assert isinstance(result, dict)
    assert result == {"header1": "value1", "header2": "value2"}

def test_ns2xls_valid_ns(temp_files):
    """Checks if ns2xls correctly saves namespace data to an xlsx file."""
    test_data = [type('TestNS', (object,), {"header1": "value1", "header2": "value2"})()]
    xls_path = os.path.join(temp_files, "output.xlsx")
    ns2xls(test_data, xls_path)
    assert os.path.exists(xls_path)

def test_ns2xml_valid_ns():
    """Checks if ns2xml correctly converts a namespace to xml."""
    test_data = type('TestNS', (object,), {"header1": "value1", "header2": "value2"})()
    result = ns2xml(test_data)
    assert "<header1>value1</header1>" in result
    assert "<header2>value2</header2>" in result

def test_replace_key_in_dict_valid_dict():
    """Checks if replace_key_in_dict correctly replaces keys in dict."""
    test_dict = {"old_key": "value1", "other_key": "value2"}
    result = replace_key_in_dict(test_dict, "old_key", "new_key")
    assert "old_key" not in result
    assert "new_key" in result
    assert result["new_key"] == "value1"

def test_speech_recognizer_valid_audio(temp_files, mocker):
    """Checks if speech_recognizer can process audio data."""
    mocker.patch("speech_recognition.Recognizer")
    recognizer_mock = mocker.patch("speech_recognition.Recognizer.recognize_google")
    recognizer_mock.return_value = "test audio"

    audio_path = os.path.join(temp_files, "test.wav")
    open(audio_path, 'a').close()  # Create empty file
    result = speech_recognizer(audio_path)

    assert result == "test audio"

def test_text2speech_valid_text(temp_files, mocker):
    """Checks if text2speech can convert text to speech."""
    mocked_tts = mocker.patch('gtts.gTTS')
    mocked_tts.return_value.save = lambda x: open(x, 'a').close()

    text = 'Test text'
    audio_path = os.path.join(temp_files, 'output.mp3')
    text2speech(text, audio_path)
    assert os.path.exists(audio_path)

def test_webp2png_valid_webp(temp_files):
    """Checks if webp2png correctly converts a webp file to a png."""
    try:
        from pillow_heif import register_heif_opener
        register_heif_opener()
    except ImportError:
        pytest.skip("pillow-heif is not installed")
    
    webp_path = os.path.join(temp_files, "test.webp")
    png_path = os.path.join(temp_files, "output.png")

    #Create an dummy webp file
    img = Image.new('RGB', (60, 30), color = 'red')
    img.save(webp_path, format='webp')

    webp2png(webp_path, png_path)
    assert os.path.exists(png_path)

def test_xls2dict_valid_xls(temp_files):
    """Checks if xls2dict correctly converts xlsx to a dict."""
    
    # Create a dummy xlsx file
    xls_path = os.path.join(temp_files, 'test.xlsx')
    test_data = [{"header1": "value1", "header2": "value2"}]
    dict2xls(test_data, xls_path)
    
    result = xls2dict(xls_path)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == test_data[0]


# --- Tests for csv module ---

def test_read_csv_as_dict_valid_csv(temp_files):
    """Checks if read_csv_as_dict correctly reads a CSV file as a dict."""
    csv_path = os.path.join(temp_files, "test.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["header1", "header2"])
        writer.writerow(["value1", "value2"])
    result = read_csv_as_dict(csv_path)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == {"header1": "value1", "header2": "value2"}

def test_read_csv_as_ns_valid_csv(temp_files):
    """Checks if read_csv_as_ns correctly reads a CSV file as a namespace."""
    csv_path = os.path.join(temp_files, "test.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["header1", "header2"])
        writer.writerow(["value1", "value2"])
    result = read_csv_as_ns(csv_path)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].header1 == "value1"
    assert result[0].header2 == "value2"
    
def test_read_csv_file_valid_csv(temp_files):
    """Checks if read_csv_file correctly reads a CSV file."""
    csv_path = os.path.join(temp_files, "test.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["header1", "header2"])
        writer.writerow(["value1", "value2"])
    result = read_csv_file(csv_path)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == ["header1", "header2"]
    assert result[1] == ["value1", "value2"]


def test_save_csv_file_valid_data(temp_files):
    """Checks if save_csv_file correctly saves data to a CSV file."""
    csv_path = os.path.join(temp_files, "output.csv")
    test_data = [["header1", "header2"], ["value1", "value2"]]
    save_csv_file(csv_path, test_data)
    assert os.path.exists(csv_path)
    with open(csv_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert rows == test_data

# --- Tests for date_time module ---

def test_TimeoutCheck_timeout_elapsed():
    """Checks if TimeoutCheck returns True when the timeout has elapsed."""
    timeout_check = TimeoutCheck(timeout=timedelta(seconds=1))
    start_time = datetime.now()
    while (datetime.now() - start_time) < timedelta(seconds=2):
        if timeout_check.check():
            break
    assert timeout_check.check() is True
    
def test_TimeoutCheck_timeout_not_elapsed():
    """Checks if TimeoutCheck returns False when the timeout has not elapsed."""
    timeout_check = TimeoutCheck(timeout=timedelta(seconds=1))
    assert timeout_check.check() is False
    

# --- Tests for file module ---

def test_get_directory_names_valid_path(temp_files):
    """Checks if get_directory_names correctly returns a list of directory names."""
    os.mkdir(os.path.join(temp_files, "dir1"))
    os.mkdir(os.path.join(temp_files, "dir2"))
    result = get_directory_names(temp_files)
    assert isinstance(result, list)
    assert len(result) == 2
    assert "dir1" in result
    assert "dir2" in result

def test_get_filenames_valid_path(temp_files):
    """Checks if get_filenames correctly returns a list of file names."""
    open(os.path.join(temp_files, "file1.txt"), "a").close()
    open(os.path.join(temp_files, "file2.txt"), "a").close()
    result = get_filenames(temp_files)
    assert isinstance(result, list)
    assert len(result) == 2
    assert "file1.txt" in result
    assert "file2.txt" in result

def test_read_text_file_valid_file(temp_files):
    """Checks if read_text_file correctly reads a text file."""
    file_path = os.path.join(temp_files, "test.txt")
    with open(file_path, "w") as f:
        f.write("Test text")
    result = read_text_file(file_path)
    assert result == "Test text"
    
def test_recursively_get_file_path_valid_path(temp_files):
    """Checks if recursively_get_file_path correctly returns a list of file paths."""
    os.makedirs(os.path.join(temp_files, "subdir"))
    open(os.path.join(temp_files, "file1.txt"), "a").close()
    open(os.path.join(temp_files, "subdir", "file2.txt"), "a").close()
    result = recursively_get_file_path(temp_files)
    assert isinstance(result, list)
    assert len(result) == 2
    assert any(os.path.join(temp_files, "file1.txt") in path for path in result)
    assert any(os.path.join(temp_files, "subdir", "file2.txt") in path for path in result)

def test_recursively_read_text_files_valid_path(temp_files):
    """Checks if recursively_read_text_files correctly reads text files recursively."""
    os.makedirs(os.path.join(temp_files, "subdir"))
    with open(os.path.join(temp_files, "file1.txt"), "w") as f:
        f.write("Text 1")
    with open(os.path.join(temp_files, "subdir", "file2.txt"), "w") as f:
        f.write("Text 2")
    result = recursively_read_text_files(temp_files)
    assert isinstance(result, dict)
    assert len(result) == 2
    assert result[os.path.join(temp_files, "file1.txt")] == "Text 1"
    assert result[os.path.join(temp_files, "subdir", "file2.txt")] == "Text 2"
    
def test_recursively_yield_file_path_valid_path(temp_files):
    """Checks if recursively_yield_file_path correctly yields file paths."""
    os.makedirs(os.path.join(temp_files, "subdir"))
    open(os.path.join(temp_files, "file1.txt"), "a").close()
    open(os.path.join(temp_files, "subdir", "file2.txt"), "a").close()
    result = list(recursively_yield_file_path(temp_files))
    assert isinstance(result, list)
    assert len(result) == 2
    assert any(os.path.join(temp_files, "file1.txt") in path for path in result)
    assert any(os.path.join(temp_files, "subdir", "file2.txt") in path for path in result)
    
def test_remove_bom_valid_text_with_bom():
    """Checks if remove_bom correctly removes BOM from text."""
    text_with_bom = "\ufeffTest text"
    result = remove_bom(text_with_bom)
    assert result == "Test text"

def test_remove_bom_valid_text_without_bom():
    """Checks if remove_bom doesn't change a text without BOM."""
    text_without_bom = "Test text"
    result = remove_bom(text_without_bom)
    assert result == "Test text"
    
def test_save_text_file_valid_text(temp_files):
    """Checks if save_text_file correctly saves text to a file."""
    file_path = os.path.join(temp_files, "output.txt")
    save_text_file(file_path, "Test text")
    assert os.path.exists(file_path)
    with open(file_path, "r") as f:
        content = f.read()
    assert content == "Test text"
    

# --- Tests for image module ---

def test_save_png_valid_image(temp_files):
    """Checks if save_png correctly saves an image to a PNG file."""
    img = Image.new('RGB', (60, 30), color = 'red')
    png_path = os.path.join(temp_files, "output.png")
    save_png(img, png_path)
    assert os.path.exists(png_path)
    
def test_save_png_from_url_valid_url(temp_files, mocker):
     """Checks if save_png_from_url correctly downloads and saves a png from a valid url."""
     mocked_response = mocker.patch('requests.get')
     mocked_image = mocker.patch('PIL.Image.open')
     
     png_path = os.path.join(temp_files, "output.png")
     mocked_response.return_value.content = b'image_data'
     mocked_image.return_value.save = lambda x: open(x, 'a').close()
     
     save_png_from_url("http://test.com/test.png", png_path)
     
     assert os.path.exists(png_path)

def test_random_image_valid_size(temp_files):
    """Checks if random_image correctly generates a random image and saves it."""
    img_path = os.path.join(temp_files, "random_img.png")
    random_image(img_path, 50, 50)
    assert os.path.exists(img_path)
    img = Image.open(img_path)
    assert img.size == (50, 50)

# --- Tests for jjson module ---
    
def test_j_dumps_valid_data():
    """Checks if j_dumps correctly dumps data to a JSON string."""
    test_data = {"key1": "value1", "key2": 123}
    result = j_dumps(test_data)
    assert json.loads(result) == test_data

def test_j_loads_valid_json():
    """Checks if j_loads correctly loads JSON from a string."""
    test_json_string = '{"key1": "value1", "key2": 123}'
    result = j_loads(test_json_string)
    assert result == {"key1": "value1", "key2": 123}

def test_j_loads_ns_valid_json():
    """Checks if j_loads_ns correctly loads JSON from a string to a namespace."""
    test_json_string = '[{"key1": "value1", "key2": 123}]'
    result = j_loads_ns(test_json_string)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].key1 == "value1"
    assert result[0].key2 == 123
    

# --- Tests for pdf module ---
def test_PDFUtils_from_text(temp_files):
    """Check if PDFUtils.from_text creates pdf file."""
    pdf_path = os.path.join(temp_files, 'test.pdf')
    pdf_utils = PDFUtils()
    pdf_utils.from_text("Test text", pdf_path)
    assert os.path.exists(pdf_path)
    
def test_PDFUtils_from_html(temp_files):
    """Check if PDFUtils.from_html creates pdf file."""
    pdf_path = os.path.join(temp_files, 'test.pdf')
    pdf_utils = PDFUtils()
    pdf_utils.from_html("<h1>Test</h1>", pdf_path)
    assert os.path.exists(pdf_path)

# --- Tests for printer module ---

def test_pprint_valid_data(mocker):
    """Checks if pprint prints the data as string"""
    mocked_print = mocker.patch('builtins.print')
    test_data = {"key1": "value1", "key2": 123}
    pprint(test_data)
    mocked_print.assert_called_once()

# --- Tests for string module ---

def test_ProductFieldsValidator_valid_data():
    """Checks ProductFieldsValidator with valid data."""
    validator = ProductFieldsValidator()
    data = {"name": "Test Product", "price": "100", "is_active": "true"}
    is_valid, errors = validator.validate(data)
    assert is_valid is True
    assert not errors
    
def test_ProductFieldsValidator_invalid_data():
    """Checks ProductFieldsValidator with invalid data."""
    validator = ProductFieldsValidator()
    data = {"name": 123, "price": "abc", "is_active": "invalid"}
    is_valid, errors = validator.validate(data)
    assert is_valid is False
    assert errors

def test_StringFormatter_valid_string():
    """Checks if StringFormatter can format a string with placeholders."""
    formatter = StringFormatter()
    test_string = "Hello {name}! Your age is {age}."
    result = formatter.format(test_string, name="Test", age=30)
    assert result == "Hello Test! Your age is 30."

def test_normalize_string_valid_string():
    """Checks if normalize_string removes extra spaces and newlines."""
    test_string = "  Test   \n string   \n"
    result = normalize_string(test_string)
    assert result == "Test string"

def test_normalize_int_valid_int():
    """Checks if normalize_int correctly converts a valid string to an int."""
    test_int_string = "123"
    result = normalize_int(test_int_string)
    assert result == 123

def test_normalize_int_invalid_int():
    """Checks if normalize_int returns None for invalid string"""
    test_int_string = "abc"
    result = normalize_int(test_int_string)
    assert result is None

def test_normalize_float_valid_float():
    """Checks if normalize_float correctly converts a valid string to a float."""
    test_float_string = "123.45"
    result = normalize_float(test_float_string)
    assert result == 123.45

def test_normalize_float_invalid_float():
    """Checks if normalize_float returns None for invalid string"""
    test_float_string = "abc"
    result = normalize_float(test_float_string)
    assert result is None
    
def test_normalize_boolean_valid_boolean():
    """Checks if normalize_boolean correctly converts a valid string to a boolean."""
    assert normalize_boolean("true") is True
    assert normalize_boolean("True") is True
    assert normalize_boolean("false") is False
    assert normalize_boolean("False") is False
    
def test_normalize_boolean_invalid_boolean():
    """Checks if normalize_boolean returns None for invalid string"""
    assert normalize_boolean("invalid") is None
    

# --- Tests for url module ---

def test_extract_url_params_valid_url():
    """Checks if extract_url_params correctly extracts parameters from a URL."""
    test_url = "http://test.com/path?param1=value1&param2=value2"
    result = extract_url_params(test