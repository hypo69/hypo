# Анализ кода модуля `dict.py`

**Качество кода**
7
-  Плюсы
    - Код предоставляет функциональность для конвертации между словарями и `SimpleNamespace`, а также для экспорта данных в различные форматы (XML, CSV, JSON, XLS, HTML, PDF).
    - Используются стандартные библиотеки Python для обработки данных.
    - Код хорошо структурирован и разбит на отдельные функции для каждой операции.
    - Присутствуют docstring для большинства функций, что облегчает понимание их назначения и использования.
-  Минусы
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    -  Не везде используется `logger.error` для обработки исключений.
    -  Отсутствуют импорты для `save_csv_file`, хотя она используется в коде.
    -  В некоторых местах код можно упростить (например, обработка словарей в `dict2ns`).
    -  Не все комментарии соответствуют формату reStructuredText (RST).
    -  Иногда вложенность `try-except` является избыточной.
    -  В некоторых функциях не хватает обработки крайних случаев.
    -  Комментарии `#` недостаточно информативны.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить недостающие импорты, такие как `from src.utils.jjson import j_loads, j_loads_ns` и `from src.utils.csv import save_csv_file`, и `from src.logger.logger import logger`.
2.  **Обработка ошибок**: Заменить стандартные блоки `try-except` на использование `logger.error` для логирования ошибок и упрощения кода.
3.  **Форматирование docstring**: Переписать все docstring в формате reStructuredText (RST) для соответствия стандартам оформления документации.
4.  **Улучшения в функциях**: 
    -  В функции `dict2ns` упростить обработку списков и словарей.
    -  Добавить проверку на корректность ввода данных в функциях.
    -  В функции `dict2pdf` добавить возможность настройки шрифтов, размера страниц и прочее.
5. **Комментарии**:
    -  Переписать все комментарии в формате RST и сделать их более информативными.
    -  Добавить описания к переменным и параметрам функций.
    -  Использовать более конкретные формулировки в комментариях, избегая слов типа "получаем", "делаем".

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для преобразования словарей и объектов SimpleNamespace.
=========================================================================================

Этот модуль предоставляет набор функций для рекурсивного преобразования словарей в объекты
:class:`SimpleNamespace` и обратно, а также для экспорта данных в различные форматы, такие
как XML, CSV, JSON, XLS, HTML и PDF.

Модуль включает следующие функции:

- :func:`dict2ns`: Рекурсивно преобразует словари в объекты :class:`SimpleNamespace`.
- :func:`dict2xml`: Генерирует XML строку из словаря.
- :func:`dict2csv`: Сохраняет данные из словаря или :class:`SimpleNamespace` в CSV файл.
- :func:`dict2json`: Сохраняет данные из словаря или :class:`SimpleNamespace` в JSON файл.
- :func:`dict2xls`: Сохраняет данные из словаря или :class:`SimpleNamespace` в XLS файл.
- :func:`dict2html`: Генерирует HTML таблицу из словаря или объекта :class:`SimpleNamespace`.
- :func:`dict2pdf`: Сохраняет данные из словаря в PDF файл.
- :func:`replace_key_in_dict`: Рекурсивно заменяет ключ в словаре или списке.

Примеры использования
--------------------

Пример преобразования словаря в SimpleNamespace:

.. code-block:: python

    data = {'key1': 'value1', 'key2': {'key3': 'value3'}}
    ns_data = dict2ns(data)
    print(ns_data.key1)  # Выведет 'value1'
    print(ns_data.key2.key3)  # Выведет 'value3'
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
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns

MODE = 'dev'


def replace_key_in_dict(data: dict | list, old_key: str, new_key: str) -> dict:
    """
    Рекурсивно заменяет ключ в словаре или списке.

    :param data: Словарь или список, в котором нужно заменить ключ.
    :type data: dict | list
    :param old_key: Ключ, который нужно заменить.
    :type old_key: str
    :param new_key: Новый ключ.
    :type new_key: str
    :return: Обновленный словарь с замененными ключами.
    :rtype: dict

    :Example Usage:

    .. code-block:: python
    
        replace_key_in_json(data, 'name', 'category_name')

        # Пример 1: Простой словарь
        data = {"old_key": "value"}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data становится {"new_key": "value"}

        # Пример 2: Вложенный словарь
        data = {"outer": {"old_key": "value"}}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data становится {"outer": {"new_key": "value"}}

        # Пример 3: Список словарей
        data = [{"old_key": "value1"}, {"old_key": "value2"}]
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data становится [{"new_key": "value1"}, {"new_key": "value2"}]

        # Пример 4: Смешанная вложенная структура со списками и словарями
        data = {"outer": [{"inner": {"old_key": "value"}}]}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data становится {"outer": [{"inner": {"new_key": "value"}}]}
    """
    if isinstance(data, dict):
        # код перебирает ключи словаря
        for key in list(data.keys()):
            # код проверяет, соответствует ли ключ старому ключу
            if key == old_key:
                # код заменяет старый ключ новым
                data[new_key] = data.pop(old_key)
            # код рекурсивно вызывает функцию, если значение - словарь или список
            if isinstance(data[key], (dict, list)):
                replace_key_in_dict(data[key], old_key, new_key)
    elif isinstance(data, list):
        # код проходит по элементам списка
        for item in data:
            # код рекурсивно вызывает функцию для каждого элемента
            replace_key_in_dict(item, old_key, new_key)
    
    return data


def dict2pdf(data: dict | SimpleNamespace, file_path: str | Path) -> None:
    """
    Сохраняет данные из словаря в PDF файл.

    :param data: Словарь, который нужно преобразовать в PDF.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к выходному PDF файлу.
    :type file_path: str | Path
    :raises TypeError: Если входные данные не являются словарем или SimpleNamespace.
    """
    # код преобразует SimpleNamespace в словарь, если это необходимо
    if isinstance(data, SimpleNamespace):
        data = data.__dict__
    if not isinstance(data, dict):
       logger.error(f'неверный тип данных для конвертации в PDF, ожидается dict или SimpleNamespace, получен {type(data)}')
       return
    try:
       # код создает PDF документ
        pdf = canvas.Canvas(str(file_path), pagesize=A4)
        width, height = A4
        x, y = 50, height - 50

        pdf.setFont('Helvetica', 12)
        # код перебирает элементы словаря для записи в PDF
        for key, value in data.items():
            line = f'{key}: {value}'
            pdf.drawString(x, y, line)
            y -= 20
            # код создает новую страницу, если места недостаточно
            if y < 50:
                pdf.showPage()
                pdf.setFont('Helvetica', 12)
                y = height - 50
        # код сохраняет PDF документ
        pdf.save()
    except Exception as e:
        logger.error(f'Ошибка при создании pdf {e}')


def dict2ns(data: Dict[str, Any] | List[Any]) -> Any:
    """
    Рекурсивно преобразует словари в объекты SimpleNamespace.

    :param data: Данные для преобразования.
    :type data: Dict[str, Any] | List[Any]
    :return: Преобразованные данные в виде SimpleNamespace или списка SimpleNamespace.
    :rtype: Any
    """
    if isinstance(data, dict):
        # код рекурсивно преобразует значения словаря
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = dict2ns(value)
            elif isinstance(value, list):
                 data[key] = [dict2ns(item) if isinstance(item, dict) else item for item in value]
        # код возвращает SimpleNamespace
        return SimpleNamespace(**data)
    elif isinstance(data, list):
         # код преобразует каждый элемент списка
        return [dict2ns(item) if isinstance(item, dict) else item for item in data]
    # код возвращает данные без изменений
    return data


def dict2xml(data: Dict[str, Any], encoding: str = 'UTF-8') -> str:
    """
    Генерирует XML строку из словаря.

    :param data: Словарь для преобразования в XML.
    :type data: Dict[str, Any]
    :param encoding: Кодировка данных. По умолчанию 'UTF-8'.
    :type encoding: str
    :raises Exception: Если предоставлено более одного корневого узла.
    :return: XML строка, представляющая входной словарь.
    :rtype: str
    """
    def _process_simple(doc, tag, tag_value):
        """
        Генерирует узел для простых типов (int, str).

        :param doc: XML документ.
        :type doc: xml.dom.minidom.Document
        :param tag: Имя тега для XML элемента.
        :type tag: str
        :param tag_value: Значение тега.
        :type tag_value: Any
        :return: Узел, представляющий тег и значение.
        :rtype: xml.dom.minidom.Element
        """
        node = doc.createElement(tag)
        node.appendChild(doc.createTextNode(str(tag_value)))
        return node

    def _process_attr(doc, attr_value: Dict[str, Any]):
        """
        Генерирует атрибуты для XML элемента.

        :param doc: XML документ.
        :type doc: xml.dom.minidom.Document
        :param attr_value: Словарь атрибутов.
        :type attr_value: Dict[str, Any]
        :return: Список атрибутов для XML элемента.
        :rtype: List[xml.dom.minidom.Attr]
        """
        attrs = []
        # код проходит по всем атрибутам
        for attr_name, value in attr_value.items():
            attr = doc.createAttribute(attr_name)
            # код устанавливает значение атрибута
            attr.nodeValue = value if not isinstance(value, dict) else value.get('value', '')
            attrs.append(attr)
        return attrs

    def _process_complex(doc, children):
        """
        Генерирует узлы для сложных типов, таких как списки или словари.

        :param doc: XML документ.
        :type doc: xml.dom.minidom.Document
        :param children: Список пар тег-значение.
        :type children: List[Tuple[str, Any]]
        :return: Список дочерних узлов и атрибутов.
        :rtype: Tuple[List[xml.dom.minidom.Element], List[xml.dom.minidom.Attr]]
        """
        nodelist = []
        attrs = []
        # код проходит по всем дочерним элементам
        for tag, value in children:
            # код обрабатывает атрибуты
            if tag == 'attrs':
                attrs = _process_attr(doc, value)
            else:
                nodes = _process(doc, tag, value)
                # код добавляет узлы в список
                nodelist.extend(nodes if isinstance(nodes, list) else [nodes])
        return nodelist, attrs

    def _process(doc, tag, tag_value):
        """
        Генерирует XML DOM объект для тега и его значения.

        :param doc: XML документ.
        :type doc: xml.dom.minidom.Document
        :param tag: Имя тега для XML элемента.
        :type tag: str
        :param tag_value: Значение тега.
        :type tag_value: Any
        :return: Узел или список узлов для тега и значения.
        :rtype: xml.dom.minidom.Element | List[xml.dom.minidom.Element]
        """
        # код обрабатывает случай, когда значение это словарь с ключом value
        if isinstance(tag_value, dict) and list(tag_value.keys()) == ['value']:
            tag_value = tag_value['value']
        # код устанавливает значение по умолчанию, если значение None
        if tag_value is None:
            tag_value = ''
        # код обрабатывает простые типы данных
        if isinstance(tag_value, (float, int, str)):
            return _process_simple(doc, tag, tag_value)
        # код обрабатывает списки
        if isinstance(tag_value, list):
            return _process_complex(doc, [(tag, x) for x in tag_value])[0]
        # код обрабатывает словари
        if isinstance(tag_value, dict):
            node = doc.createElement(tag)
            nodelist, attrs = _process_complex(doc, tag_value.items())
            # код добавляет дочерние узлы
            for child in nodelist:
                node.appendChild(child)
            # код добавляет атрибуты
            for attr in attrs:
                node.setAttributeNode(attr)
            return node
    # код создает XML документ
    doc = getDOMImplementation().createDocument(None, None, None)
    # код проверяет, что есть только один корневой узел
    if len(data) > 1:
        logger.error('Only one root node allowed')
        raise Exception('Only one root node allowed')
    # код обрабатывает корневой элемент
    root, _ = _process_complex(doc, data.items())
    doc.appendChild(root[0])
    # код возвращает XML строку
    return doc.toxml(encoding)


def dict2csv(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные из словаря или SimpleNamespace в CSV файл.

    :param data: Данные для сохранения в CSV файл.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к CSV файлу.
    :type file_path: str | Path
    :return: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool
    """
    # код вызывает функцию для сохранения CSV
    return save_csv_file(data, file_path)


def dict2xls(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные из словаря или SimpleNamespace в XLS файл.

    :param data: Данные для сохранения в XLS файл.
    :type data: dict | SimpleNamespace
    :param file_path: Путь к XLS файлу.
    :type file_path: str | Path
    :return: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool
    """
    # код вызывает функцию для сохранения XLS
    return save_xls_file(data, file_path)


def dict2html(data: dict | SimpleNamespace, encoding: str = 'UTF-8') -> str:
    """
    Генерирует HTML таблицу из словаря или объекта SimpleNamespace.

    :param data: Данные для преобразования в HTML.
    :type data: dict | SimpleNamespace
    :param encoding: Кодировка данных. По умолчанию 'UTF-8'.
    :type encoding: str
    :return: HTML строка, представляющая входной словарь.
    :rtype: str
    """
    def dict_to_html_table(data: dict, depth: int = 0) -> str:
        """
        Рекурсивно преобразует словарь в HTML таблицу.

        :param data: Словарь для преобразования.
        :type data: dict
        :param depth: Глубина рекурсии, используется для вложенных таблиц. По умолчанию 0.
        :type depth: int
        :return: HTML таблица в виде строки.
        :rtype: str
        """
        html = ['<table border="1" cellpadding="5" cellspacing="0">']
        # код обрабатывает словарь
        if isinstance(data, dict):
            # код проходит по элементам словаря
            for key, value in data.items():
                html.append('<tr>')
                html.append(f'<td><strong>{key}</strong></td>')
                # код обрабатывает вложенные словари
                if isinstance(value, dict):
                    html.append(f'<td>{dict_to_html_table(value, depth + 1)}</td>')
                 # код обрабатывает списки
                elif isinstance(value, list):
                    html.append('<td>')
                    html.append('<ul>')
                    for item in value:
                        html.append(f'<li>{item}</li>')
                    html.append('</ul>')
                    html.append('</td>')
                else:
                    html.append(f'<td>{value}</td>')
                html.append('</tr>')
        else:
             # код обрабатывает другие типы данных
            html.append(f'<tr><td colspan="2">{data}</td></tr>')
        
        html.append('</table>')
        return '\n'.join(html)
    
    # код преобразует SimpleNamespace в словарь
    if isinstance(data, SimpleNamespace):
        data = data.__dict__
    
    html_content = dict_to_html_table(data)
    # код возвращает HTML страницу
    return f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="{encoding}">\n<title>Dictionary to HTML</title>\n</head>\n<body>\n{html_content}\n</body>\n</html>'
```