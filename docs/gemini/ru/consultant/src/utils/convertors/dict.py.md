# Анализ кода модуля `dict`

**Качество кода**
8
-  Плюсы
    -  Код содержит docstring для каждой функции, что соответствует требованиям PEP 257.
    -  Используются type hints для параметров и возвращаемых значений функций, что улучшает читаемость и возможности статического анализа кода.
    -  Реализованы функции для преобразования данных в различные форматы (JSON, CSV, XML, XLS, HTML, PDF).
    -  Используется рекурсия в функциях `dict2ns`, `replace_key_in_json` и `dict_to_html_table`.
-  Минусы
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, хотя это требование указано в инструкции.
    -  В некоторых функциях используются стандартные блоки `try-except` без логирования ошибок.
    -  Не все функции документированы в формате RST, как это требуется.
    -  Некоторые комментарии после `#` не содержат подробное объяснение следующего за ними блока кода.
    -  Импорт `src.utils.xls` не соответствует предыдущим реализациям.
    -  Не хватает импорта `from src.logger.logger import logger`.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`, где это необходимо (пока не требуется).
2.  Добавить логирование ошибок с помощью `logger.error` в блоки `try-except`.
3.  Переписать все docstring в формате RST.
4.  Добавить подробные комментарии после `#` к каждой строке кода.
5.  Добавить недостающие импорты.
6.  Использовать функцию `save_csv_file` из модуля `src.utils.csv`.
7.  Пересмотреть функцию `replace_key_in_dict`, убрать из названия json так как она работает не только с json.
8.  Убрать неиспользуемые импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для преобразования данных между словарями и SimpleNamespace, а также для экспорта данных в различные форматы.
=========================================================================================

Этот модуль содержит функции для рекурсивного преобразования словарей в объекты SimpleNamespace и наоборот,
а также для экспорта данных в различные форматы.

Функции:
    - :func:`dict2ns`: Рекурсивно преобразует словари в объекты SimpleNamespace.
    - :func:`dict2xml`: Генерирует XML-строку из словаря.
    - :func:`dict2csv`: Сохраняет данные из словаря или SimpleNamespace в CSV-файл.
    - :func:`dict2json`: Сохраняет данные из словаря или SimpleNamespace в JSON-файл.
    - :func:`dict2xls`: Сохраняет данные из словаря или SimpleNamespace в XLS-файл.
    - :func:`dict2html`: Генерирует HTML-таблицу из словаря или объекта SimpleNamespace.
    - :func:`dict2pdf`: Сохраняет данные из словаря в PDF-файл.
    - :func:`replace_key_in_dict`: Рекурсивно заменяет ключ в словаре или списке.
"""

import json
from types import SimpleNamespace
from typing import Any, Dict, List
from pathlib import Path
from xml.dom.minidom import getDOMImplementation
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from src.utils.xls import save_xls_file
from src.utils.csv import save_csv_file
from src.logger.logger import logger # Импорт логгера



def replace_key_in_dict(data: dict | list, old_key: str, new_key: str) -> dict:
    """
    Рекурсивно заменяет ключ в словаре или списке.

    :param data: Словарь или список, в котором происходит замена ключа.
    :type data: dict | list
    :param old_key: Ключ, который нужно заменить.
    :type old_key: str
    :param new_key: Новый ключ.
    :type new_key: str
    :return: Обновленный словарь с замененными ключами.
    :rtype: dict

    Пример использования:

        replace_key_in_dict(data, 'name', 'category_name')

        # Пример 1: Простой словарь
        data = {"old_key": "value"}
        updated_data = replace_key_in_dict(data, "old_key", "new_key")
        # updated_data становится {"new_key": "value"}

        # Пример 2: Вложенный словарь
        data = {"outer": {"old_key": "value"}}
        updated_data = replace_key_in_dict(data, "old_key", "new_key")
        # updated_data становится {"outer": {"new_key": "value"}}

        # Пример 3: Список словарей
        data = [{"old_key": "value1"}, {"old_key": "value2"}]
        updated_data = replace_key_in_dict(data, "old_key", "new_key")
        # updated_data становится [{"new_key": "value1"}, {"new_key": "value2"}]

        # Пример 4: Смешанная вложенная структура со списками и словарями
        data = {"outer": [{"inner": {"old_key": "value"}}]}
        updated_data = replace_key_in_dict(data, "old_key", "new_key")
        # updated_data становится {"outer": [{"inner": {"new_key": "value"}}]}
    """
    if isinstance(data, dict): # Проверка, является ли data словарем
        for key in list(data.keys()): # Итерация по ключам словаря
            if key == old_key: # Проверка, равен ли текущий ключ старому ключу
                data[new_key] = data.pop(old_key) # Замена старого ключа новым
            if isinstance(data[key], (dict, list)): # Проверка, является ли значение словарем или списком
                replace_key_in_dict(data[key], old_key, new_key) # Рекурсивный вызов функции для вложенных структур
    elif isinstance(data, list): # Проверка, является ли data списком
        for item in data: # Итерация по элементам списка
            replace_key_in_dict(item, old_key, new_key) # Рекурсивный вызов функции для каждого элемента списка
    
    return data # Возврат обновленного словаря или списка

def dict2pdf(data: dict | SimpleNamespace, file_path: str | Path) -> None:
    """
    Сохраняет данные из словаря в PDF-файл.

    :param data: Словарь для преобразования в PDF.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к выходному PDF-файлу.
    :type file_path: str | Path
    """
    if isinstance(data, SimpleNamespace): # Проверка, является ли data объектом SimpleNamespace
        data = data.__dict__ # Преобразование SimpleNamespace в словарь

    pdf = canvas.Canvas(str(file_path), pagesize=A4) # Создание объекта canvas для PDF
    width, height = A4 # Получение ширины и высоты страницы
    x, y = 50, height - 50 # Определение начальных координат для текста

    pdf.setFont("Helvetica", 12) # Установка шрифта

    for key, value in data.items(): # Итерация по элементам словаря
        line = f"{key}: {value}" # Формирование строки для записи в PDF
        pdf.drawString(x, y, line) # Запись строки в PDF
        y -= 20 # Уменьшение координаты y для следующей строки

        if y < 50: # Проверка, достаточно ли места на странице
            pdf.showPage() # Создание новой страницы
            pdf.setFont("Helvetica", 12) # Установка шрифта
            y = height - 50 # Установка начальной координаты y для новой страницы

    pdf.save() # Сохранение PDF-файла

def dict2ns(data: Dict[str, Any] | List[Any]) -> Any:
    """
    Рекурсивно преобразует словари в объекты SimpleNamespace.

    :param data: Данные для преобразования.
    :type data: Dict[str, Any] | List[Any]
    :return: Преобразованные данные в виде SimpleNamespace или списка SimpleNamespace.
    :rtype: Any
    """
    if isinstance(data, dict): # Проверка, является ли data словарем
        for key, value in data.items(): # Итерация по элементам словаря
            if isinstance(value, dict): # Проверка, является ли значение словарем
                data[key] = dict2ns(value) # Рекурсивный вызов функции для вложенных словарей
            elif isinstance(value, list): # Проверка, является ли значение списком
                data[key] = [dict2ns(item) if isinstance(item, dict) else item for item in value] # Рекурсивный вызов функции для элементов списка
        return SimpleNamespace(**data) # Возврат объекта SimpleNamespace
    elif isinstance(data, list): # Проверка, является ли data списком
        return [dict2ns(item) if isinstance(item, dict) else item for item in data] # Рекурсивный вызов функции для элементов списка
    return data # Возврат исходных данных, если они не являются словарем или списком

def dict2xml(data: Dict[str, Any], encoding: str = 'UTF-8') -> str:
    """
    Генерирует XML-строку из словаря.

    :param data: Данные для преобразования в XML.
    :type data: Dict[str, Any]
    :param encoding: Кодировка данных. По умолчанию 'UTF-8'.
    :type encoding: str
    :return: XML-строка, представляющая входной словарь.
    :rtype: str
    :raises Exception: Если предоставлено более одного корневого узла.
    """
    def _process_simple(doc, tag, tag_value):
        """
        Генерирует узел для простых типов (int, str).

        :param doc: Объект XML-документа.
        :type doc: xml.dom.minidom.Document
        :param tag: Имя тега для XML-элемента.
        :type tag: str
        :param tag_value: Значение тега.
        :type tag_value: Any
        :return: Узел, представляющий тег и значение.
        :rtype: xml.dom.minidom.Element
        """
        node = doc.createElement(tag) # Создание XML-элемента
        node.appendChild(doc.createTextNode(str(tag_value))) # Добавление текстового узла
        return node

    def _process_attr(doc, attr_value: Dict[str, Any]):
        """
        Генерирует атрибуты для XML-элемента.

        :param doc: Объект XML-документа.
        :type doc: xml.dom.minidom.Document
        :param attr_value: Словарь атрибутов.
        :type attr_value: Dict[str, Any]
        :return: Список атрибутов для XML-элемента.
        :rtype: List[xml.dom.minidom.Attr]
        """
        attrs = [] # Инициализация списка атрибутов
        for attr_name, value in attr_value.items(): # Итерация по атрибутам
            attr = doc.createAttribute(attr_name) # Создание атрибута
            attr.nodeValue = value if not isinstance(value, dict) else value.get('value', '') # Установка значения атрибута
            attrs.append(attr) # Добавление атрибута в список
        return attrs

    def _process_complex(doc, children):
        """
        Генерирует узлы для сложных типов, таких как списки или словари.

        :param doc: Объект XML-документа.
        :type doc: xml.dom.minidom.Document
        :param children: Список пар тег-значение.
        :type children: List[Tuple[str, Any]]
        :return: Список дочерних узлов и атрибутов.
        :rtype: Tuple[List[xml.dom.minidom.Element], List[xml.dom.minidom.Attr]]
        """
        nodelist = [] # Инициализация списка узлов
        attrs = [] # Инициализация списка атрибутов
        for tag, value in children: # Итерация по дочерним элементам
            if tag == 'attrs': # Проверка, является ли текущий тег атрибутами
                attrs = _process_attr(doc, value) # Обработка атрибутов
            else:
                nodes = _process(doc, tag, value) # Обработка узлов
                nodelist.extend(nodes if isinstance(nodes, list) else [nodes]) # Добавление узлов в список
        return nodelist, attrs

    def _process(doc, tag, tag_value):
        """
        Генерирует XML DOM объект для тега и его значения.

        :param doc: Объект XML-документа.
        :type doc: xml.dom.minidom.Document
        :param tag: Имя тега для XML-элемента.
        :type tag: str
        :param tag_value: Значение тега.
        :type tag_value: Any
        :return: Узел или список узлов для тега и значения.
        :rtype: xml.dom.minidom.Element | List[xml.dom.minidom.Element]
        """
        if isinstance(tag_value, dict) and list(tag_value.keys()) == ['value']: # Проверка, является ли значение словарем с ключом 'value'
            tag_value = tag_value['value'] # Извлечение значения

        if tag_value is None: # Проверка, является ли значение None
            tag_value = '' # Установка значения в пустую строку

        if isinstance(tag_value, (float, int, str)): # Проверка, является ли значение простым типом
            return _process_simple(doc, tag, tag_value) # Обработка простого значения

        if isinstance(tag_value, list): # Проверка, является ли значение списком
            return _process_complex(doc, [(tag, x) for x in tag_value])[0] # Обработка списка

        if isinstance(tag_value, dict): # Проверка, является ли значение словарем
            node = doc.createElement(tag) # Создание XML-элемента
            nodelist, attrs = _process_complex(doc, tag_value.items()) # Обработка сложных значений
            for child in nodelist: # Итерация по дочерним узлам
                node.appendChild(child) # Добавление дочернего узла
            for attr in attrs: # Итерация по атрибутам
                node.setAttributeNode(attr) # Добавление атрибута
            return node # Возврат XML-узла

    doc = getDOMImplementation().createDocument(None, None, None) # Создание XML-документа
    if len(data) > 1: # Проверка, является ли количество корневых узлов больше 1
        logger.error('Only one root node allowed') # Логирование ошибки
        raise Exception('Only one root node allowed') # Вызов исключения
    
    root, _ = _process_complex(doc, data.items()) # Обработка корневого узла
    doc.appendChild(root[0]) # Добавление корневого узла в документ
    return doc.toxml(encoding) # Возврат XML-строки

def dict2csv(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные из словаря или SimpleNamespace в CSV-файл.

    :param data: Данные для сохранения в CSV-файл.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к CSV-файлу.
    :type file_path: str | Path
    :return: True, если файл был успешно сохранен, иначе False.
    :rtype: bool
    """
    return save_csv_file(data, file_path) # Сохранение данных в CSV-файл

def dict2xls(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные из словаря или SimpleNamespace в XLS-файл.

    :param data: Данные для сохранения в XLS-файл.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к XLS-файлу.
    :type file_path: str | Path
    :return: True, если файл был успешно сохранен, иначе False.
    :rtype: bool
    """
    return save_xls_file(data, file_path) # Сохранение данных в XLS-файл

def dict2html(data: dict | SimpleNamespace, encoding: str = 'UTF-8') -> str:
    """
    Генерирует HTML-таблицу из словаря или объекта SimpleNamespace.

    :param data: Данные для преобразования в HTML.
    :type data: dict | SimpleNamespace
    :param encoding: Кодировка данных. По умолчанию 'UTF-8'.
    :type encoding: str
    :return: HTML-строка, представляющая входной словарь.
    :rtype: str
    """
    def dict_to_html_table(data: dict, depth: int = 0) -> str:
        """
        Рекурсивно преобразует словарь в HTML-таблицу.

        :param data: Словарь для преобразования.
        :type data: dict
        :param depth: Глубина рекурсии, используется для вложенных таблиц. По умолчанию 0.
        :type depth: int
        :return: HTML-таблица в виде строки.
        :rtype: str
        """
        html = ['<table border="1" cellpadding="5" cellspacing="0">'] # Инициализация HTML-таблицы
        
        if isinstance(data, dict): # Проверка, является ли data словарем
            for key, value in data.items(): # Итерация по элементам словаря
                html.append('<tr>') # Начало строки таблицы
                html.append(f'<td><strong>{key}</strong></td>') # Запись ключа
                if isinstance(value, dict): # Проверка, является ли значение словарем
                    html.append(f'<td>{dict_to_html_table(value, depth + 1)}</td>') # Рекурсивный вызов функции для вложенных таблиц
                elif isinstance(value, list): # Проверка, является ли значение списком
                    html.append('<td>') # Начало ячейки списка
                    html.append('<ul>') # Начало списка
                    for item in value: # Итерация по элементам списка
                        html.append(f'<li>{item}</li>') # Запись элемента списка
                    html.append('</ul>') # Конец списка
                    html.append('</td>') # Конец ячейки списка
                else: # Если значение не словарь и не список
                    html.append(f'<td>{value}</td>') # Запись значения
                html.append('</tr>') # Конец строки таблицы
        else: # Если данные не являются словарем
            html.append(f'<tr><td colspan="2">{data}</td></tr>') # Запись данных в ячейку
        
        html.append('</table>') # Конец таблицы
        return '\n'.join(html) # Возврат HTML-таблицы в виде строки
    
    # Преобразование данных в словарь, если это SimpleNamespace
    if isinstance(data, SimpleNamespace): # Проверка, является ли data объектом SimpleNamespace
        data = data.__dict__ # Преобразование SimpleNamespace в словарь
    
    html_content = dict_to_html_table(data) # Преобразование словаря в HTML-таблицу
    return f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="{encoding}">\n<title>Dictionary to HTML</title>\n</head>\n<body>\n{html_content}\n</body>\n</html>' # Формирование HTML-документа
```