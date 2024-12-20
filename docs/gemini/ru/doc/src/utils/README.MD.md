# Tiny Utils

## Обзор

**Tiny Utils** — это библиотека утилит, предоставляющая набор легких вспомогательных функций для различных распространенных задач. Эта библиотека включает в себя утилиты для преобразования форматов данных, обработки текста и файлов, строковых операций, форматирования даты и времени, обработки изображений и многое другое. Она организована в несколько модулей для легкого доступа к определенным функциональным возможностям.

## Оглавление

- [Tiny Utils](#tiny-utils)
  - [Обзор](#обзор)
  - [Оглавление](#оглавление)
  - [Установка](#установка)
  - [Обзор модулей](#обзор-модулей)
  - [Описание модулей](#описание-модулей)
    - [Конвертеры](#конвертеры)
      - [Файлы:](#файлы)
    - [Строковые утилиты](#строковые-утилиты)
    - [Файловые операции](#файловые-операции)
    - [Утилиты даты и времени](#утилиты-даты-и-времени)
    - [FTP-утилиты](#ftp-утилиты)
    - [Утилиты для работы с изображениями](#утилиты-для-работы-с-изображениями)
    - [PDF-утилиты](#pdf-утилиты)
    - [Утилиты для принтера](#утилиты-для-принтера)
  - [Примеры использования](#примеры-использования)
    - [Преобразование текста в изображение PNG](#преобразование-текста-в-изображение-png)
    - [Преобразование XML в словарь](#преобразование-xml-в-словарь)
    - [Разбор и обработка JSON](#разбор-и-обработка-json)
  - [Участие в разработке](#участие-в-разработке)
  - [Лицензия](#лицензия)

## Установка

Чтобы использовать **Tiny Utils**, клонируйте репозиторий и установите необходимые зависимости, указанные в файле `requirements.txt`.

```bash
git clone https://github.com/hypo69/tiny-utils.git
cd tiny_utils
pip install -r requirements.txt
```

## Обзор модулей

Эта библиотека содержит несколько подмодулей, каждый из которых обрабатывает определенную задачу:

- **Конвертеры**: Модули для преобразования форматов данных, таких как текст в изображение, webp в png, JSON, XML, кодировка Base64 и многое другое.
- **Строковые утилиты**: Инструменты для расширенной работы со строками.
- **Файловые операции**: Функции для обработки файлов и манипуляций с ними.
- **Утилиты даты и времени**: Инструменты для форматирования даты и времени.
- **FTP-утилиты**: Функции для обработки файлов по FTP.
- **Утилиты для работы с изображениями**: Основные функции обработки изображений.
- **PDF-утилиты**: Манипуляции и преобразования с PDF-файлами.
- **Утилиты для принтера**: Функции для отправки данных на принтер.

## Описание модулей

### Конвертеры

Модуль `convertors` содержит утилиты для преобразования данных между форматами. Эти модули могут обрабатывать различные типы данных, от CSV до JSON и от текста до изображений.

#### Файлы:

- **text2png.py**: Преобразует текстовые данные в файл изображения PNG.
- **tts.py**: Преобразует текст в речь и сохраняет его в виде аудиофайла.
- **webp2png.py**: Преобразует изображения из формата WebP в формат PNG.
- **xls.py**: Обрабатывает преобразования и манипуляции с XLS-файлами.
- **xml2dict.py**: Преобразует данные XML в словарь Python.
- **base64.py**: Кодирует или декодирует данные с использованием кодировки Base64.
- **csv.py**: Предоставляет инструменты для разбора и обработки CSV.
- **dict.py**: Утилиты для обработки словарей Python.
- **html.py**: Преобразует HTML-контент в различные форматы.
- **json.py**: Утилиты для разбора и обработки JSON.
- **md2dict.py**: Преобразует контент Markdown в словарь.
- **ns.py**: Специализированные утилиты для преобразования пространств имен.

### Строковые утилиты

Модуль `string` включает в себя расширенные функции для работы со строками, предоставляя инструменты для улучшения базовых строковых операций Python.

### Файловые операции

Модуль `file.py` включает в себя утилиты для обработки файлов, предоставляя функции для чтения, записи, копирования, удаления и перемещения файлов с дополнительными опциями для обработки ошибок и совместимости форматов файлов.

### Утилиты даты и времени

Модуль `date_time.py` предоставляет различные утилиты для работы с датой и временем, позволяя пользователям анализировать, форматировать и манипулировать значениями даты и времени для согласованного форматирования и преобразований.

### FTP-утилиты

Модуль `ftp.py` включает в себя функции для обработки FTP-операций, таких как подключение к серверам, загрузка, скачивание и управление файлами по FTP.

### Утилиты для работы с изображениями

Модуль `image.py` предоставляет основные инструменты для манипулирования изображениями, такие как изменение размера, обрезка, преобразование форматов и применение фильтров.

### PDF-утилиты

Модуль `pdf.py` предлагает утилиты для работы с PDF, включая преобразование файлов PDF, объединение, разделение и извлечение текста.

### Утилиты для принтера

Модуль `printer.py` включает в себя функции для отправки файлов или форматированных данных на принтер, поддерживая параметры настройки задания печати.

## Примеры использования

Вот несколько примеров использования, демонстрирующих, как работать с библиотекой **Tiny Utils**.

### Преобразование текста в изображение PNG

```python
from tiny_utils.convertors import text2png

text = "Hello, World!"
output_path = "output_image.png"
text2png.convert(text, output_path)
```

### Преобразование XML в словарь

```python
from tiny_utils.convertors import xml2dict

xml_data = "<root><item>Hello</item></root>"
dictionary = xml2dict.convert(xml_data)
print(dictionary)
```

### Разбор и обработка JSON

```python
from tiny_utils.convertors import json

json_data = '{"name": "John", "age": 30}'
parsed_data = json.parse(json_data)
print(parsed_data)
```

## Для получения дополнительных примеров и подробной документации, пожалуйста, посетите
[Tiny Utils Wiki](https://github.com/hypo69/tiny-utils/wiki).

## Участие в разработке

Вклад приветствуется! Пожалуйста, сделайте форк репозитория и отправьте запрос на внесение изменений (pull request) с вашими изменениями. Не забудьте обновить документацию для любых новых функций или изменений.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Смотрите файл [LICENSE](./LICENSE) для получения дополнительной информации.