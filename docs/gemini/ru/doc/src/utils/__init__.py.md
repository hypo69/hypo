# Модуль `src.utils`

## Обзор

Модуль `src.utils` предоставляет набор утилит для упрощения повседневных задач программирования. Он включает в себя инструменты для конвертации данных, работы с файлами, форматом вывода и другие полезные функции.

## Содержание

1. [Импорт модулей](#Импорт-модулей)
2. [Модуль convertors](#Модуль-convertors)
3. [Модуль csv](#Модуль-csv)
4. [Модуль date_time](#Модуль-date_time)
5. [Модуль file](#Модуль-file)
6. [Модуль image](#Модуль-image)
7. [Модуль jjson](#Модуль-jjson)
8. [Модуль pdf](#Модуль-pdf)
9. [Модуль printer](#Модуль-printer)
10. [Модуль string](#Модуль-string)
11. [Модуль url](#Модуль-url)
12. [Модуль video](#Модуль-video)
13. [Модуль path](#Модуль-path)

## Импорт модулей

Модуль импортирует различные подмодули и их функции для обеспечения разнообразных утилит.

### Модуль `convertors`

Импортирует функции для конвертации данных между различными форматами, включая:

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

### Модуль `csv`

Импортирует функции для работы с CSV-файлами:

- `read_csv_as_dict`
- `read_csv_as_ns`
- `read_csv_file`
- `save_csv_file`

### Модуль `date_time`

Импортирует класс `TimeoutCheck` для проверки времени выполнения задач.

- `TimeoutCheck`

### Модуль `file`

Импортирует функции для работы с файловой системой:

- `get_directory_names`
- `get_filenames`
- `read_text_file`
- `recursively_get_file_path`
- `recursively_read_text_files`
- `recursively_yield_file_path`
- `remove_bom`
- `save_text_file`

### Модуль `image`

Импортирует функции для работы с изображениями:

- `save_png`
- `save_png_from_url`
- `random_image`

### Модуль `jjson`

Импортирует функции для работы с JSON:

- `j_dumps`
- `j_loads`
- `j_loads_ns`

### Модуль `pdf`

Импортирует класс `PDFUtils` для работы с PDF-файлами.

- `PDFUtils`

### Модуль `printer`

Импортирует функцию `pprint` для удобного вывода данных.

- `pprint`

### Модуль `string`

Импортирует инструменты для работы со строками:

- `ProductFieldsValidator`
- `StringFormatter`
- `normalize_string`
- `normalize_int`
- `normalize_float`
- `normalize_boolean`

### Модуль `url`

Импортирует функции для работы с URL:

- `extract_url_params`
- `is_url`

### Модуль `video`

Импортирует функцию для сохранения видео из URL:

- `save_video_from_url`

### Модуль `path`

Импортирует функцию для работы с путями:

- `get_relative_path`