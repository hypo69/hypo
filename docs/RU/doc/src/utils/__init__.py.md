# Модуль `src.utils`

## Обзор

Модуль `src.utils` представляет собой коллекцию утилит, предназначенных для упрощения часто выполняемых задач программирования. Он включает в себя инструменты для конвертации данных, работы с файлами, форматированного вывода, обработки изображений, видео и других задач.

## Содержание

- [Обзор](#обзор)
- [Модули](#модули)
    - [convertors](#convertors)
    - [csv](#csv)
    - [date_time](#date_time)
    - [file](#file)
    - [image](#image)
    - [jjson](#jjson)
    - [pdf](#pdf)
    - [printer](#printer)
    - [string](#string)
    - [url](#url)
    - [video](#video)
    - [path](#path)
## Модули

### `convertors`

Модуль содержит функции для конвертации различных форматов данных.

- `TextToImageGenerator`
- `base64_to_tmpfile`
- `base64encode`
- `csv2dict`
- `csv2ns`
- `decode_unicode_escape`
- `dict2csv`
- `dict2html`
- `dict2ns`
- `dict2xls`
- `dict2xml`
- `dot2png`
- `escape2html`
- `html2dict`
- `html2escape`
- `html2ns`
- `html2text`
- `html2text_file`
- `json2csv`
- `json2ns`
- `json2xls`
- `json2xml`
- `md2dict`
- `ns2csv`
- `ns2dict`
- `ns2xls`
- `ns2xml`
- `replace_key_in_dict`
- `speech_recognizer`
- `text2speech`
- `webp2png`
- `xls2dict`

### `csv`

Модуль содержит функции для работы с CSV файлами.

- `read_csv_as_dict`
- `read_csv_as_ns`
- `read_csv_file`
- `save_csv_file`

### `date_time`

Модуль содержит функции для работы с датой и временем.

- `TimeoutCheck`

### `file`

Модуль содержит функции для работы с файлами и директориями.

- `get_directory_names`
- `get_filenames`
- `read_text_file`
- `recursively_get_file_path`
- `recursively_read_text_files`
- `recursively_yield_file_path`
- `remove_bom`
- `save_text_file`

### `image`

Модуль содержит функции для работы с изображениями.

- `save_png`
- `save_png_from_url`
- `random_image`

### `jjson`

Модуль содержит функции для работы с JSON.

- `j_dumps`
- `j_loads`
- `j_loads_ns`

### `pdf`

Модуль содержит функции для работы с PDF.

- `PDFUtils`

### `printer`

Модуль содержит функции для форматированного вывода.

- `pprint`

### `string`

Модуль содержит функции для работы со строками.

- `ProductFieldsValidator`
- `StringFormatter`
- `normalize_string`
- `normalize_int`
- `normalize_float`
- `normalize_boolean`

### `url`

Модуль содержит функции для работы с URL.

- `extract_url_params`
- `is_url`

### `video`

Модуль содержит функции для работы с видео.

- `save_video_from_url`

### `path`

Модуль содержит функции для работы с путями.

- `get_relative_path`