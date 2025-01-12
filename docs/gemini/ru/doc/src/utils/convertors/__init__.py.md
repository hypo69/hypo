# Модуль `src.utils.convertors`

## Обзор

Модуль `src.utils.convertors` предназначен для конвертации данных между различными форматами, такими как CSV, JSON, XML, HTML, Markdown, Base64, а также для работы с изображениями и текстом. Он предоставляет инструменты для преобразования данных в словари, списки, форматы для работы с таблицами и т.д.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
    - [base64_to_tmpfile](#base64_to_tmpfile)
    - [base64encode](#base64encode)
    - [csv2dict](#csv2dict)
    - [csv2ns](#csv2ns)
    - [dict2ns](#dict2ns)
    - [dict2csv](#dict2csv)
    - [dict2html](#dict2html)
    - [dict2xls](#dict2xls)
    - [dict2xml](#dict2xml)
    - [replace_key_in_dict](#replace_key_in_dict)
    - [dot2png](#dot2png)
    - [html2escape](#html2escape)
    - [html2ns](#html2ns)
    - [html2dict](#html2dict)
    - [escape2html](#escape2html)
    - [html2text](#html2text)
    - [html2text_file](#html2text_file)
    - [google_fixed_width_font](#google_fixed_width_font)
    - [google_has_height](#google_has_height)
    - [google_list_style](#google_list_style)
    - [google_nest_count](#google_nest_count)
    - [google_text_emphasis](#google_text_emphasis)
    - [dumb_css_parser](#dumb_css_parser)
    - [dumb_property_dict](#dumb_property_dict)
    - [json2csv](#json2csv)
    - [json2ns](#json2ns)
    - [json2xls](#json2xls)
    - [json2xml](#json2xml)
    - [md2dict](#md2dict)
    - [ns2csv](#ns2csv)
    - [ns2dict](#ns2dict)
    - [ns2xls](#ns2xls)
    - [ns2xml](#ns2xml)
    - [TextToImageGenerator](#TextToImageGenerator)
    - [webp2png](#webp2png)
    - [speech_recognizer](#speech_recognizer)
    - [text2speech](#text2speech)
    - [decode_unicode_escape](#decode_unicode_escape)
    - [xml2dict](#xml2dict)
    - [xls2dict](#xls2dict)

## Функции

### `base64_to_tmpfile`

**Описание**: Функция для декодирования base64 и сохранения в временный файл.

### `base64encode`

**Описание**: Функция для кодирования данных в base64.

### `csv2dict`

**Описание**: Функция для преобразования CSV в словарь.

### `csv2ns`

**Описание**: Функция для преобразования CSV в пространство имен.

### `dict2ns`

**Описание**: Функция для преобразования словаря в пространство имен.

### `dict2csv`

**Описание**: Функция для преобразования словаря в CSV.

### `dict2html`

**Описание**: Функция для преобразования словаря в HTML.

### `dict2xls`

**Описание**: Функция для преобразования словаря в XLSX.

### `dict2xml`

**Описание**: Функция для преобразования словаря в XML.

### `replace_key_in_dict`

**Описание**: Функция для замены ключа в словаре.

### `dot2png`

**Описание**: Функция для преобразования DOT в PNG.

### `html2escape`

**Описание**: Функция для экранирования HTML.

### `html2ns`

**Описание**: Функция для преобразования HTML в пространство имен.

### `html2dict`

**Описание**: Функция для преобразования HTML в словарь.

### `escape2html`

**Описание**: Функция для обратного экранирования HTML.

### `html2text`

**Описание**: Функция для преобразования HTML в текст.

### `html2text_file`

**Описание**: Функция для преобразования HTML файла в текст.

### `google_fixed_width_font`

**Описание**: Функция для определения, является ли шрифт фиксированной ширины.

### `google_has_height`

**Описание**: Функция для определения, есть ли высота у элемента.

### `google_list_style`

**Описание**: Функция для извлечения стиля списка.

### `google_nest_count`

**Описание**: Функция для подсчета вложенности элемента.

### `google_text_emphasis`

**Описание**: Функция для извлечения стилей выделения текста.

### `dumb_css_parser`

**Описание**: Простой парсер CSS.

### `dumb_property_dict`

**Описание**: Функция для преобразования CSS свойств в словарь.

### `json2csv`

**Описание**: Функция для преобразования JSON в CSV.

### `json2ns`

**Описание**: Функция для преобразования JSON в пространство имен.

### `json2xls`

**Описание**: Функция для преобразования JSON в XLSX.

### `json2xml`

**Описание**: Функция для преобразования JSON в XML.

### `md2dict`

**Описание**: Функция для преобразования Markdown в словарь.

### `ns2csv`

**Описание**: Функция для преобразования пространства имен в CSV.

### `ns2dict`

**Описание**: Функция для преобразования пространства имен в словарь.

### `ns2xls`

**Описание**: Функция для преобразования пространства имен в XLSX.

### `ns2xml`

**Описание**: Функция для преобразования пространства имен в XML.

### `TextToImageGenerator`

**Описание**: Класс для генерации изображений из текста.

### `webp2png`

**Описание**: Функция для преобразования WebP в PNG.

### `speech_recognizer`

**Описание**: Функция для распознавания речи.

### `text2speech`

**Описание**: Функция для преобразования текста в речь.

### `decode_unicode_escape`

**Описание**: Функция для декодирования escape-последовательностей Unicode.

### `xml2dict`

**Описание**: Функция для преобразования XML в словарь.

### `xls2dict`

**Описание**: Функция для преобразования XLSX в словарь.