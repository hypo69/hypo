# Модуль `src.utils.xml`

## Обзор

Модуль `src.utils.xml` предоставляет функции для очистки и сохранения XML-данных. Он включает в себя инструменты для удаления пустых элементов и CDATA-секций, а также для форматирования XML с отступами перед сохранением в файл.

## Подробней

Этот модуль предназначен для обработки XML-данных, которые могут содержать избыточные пробелы или пустые элементы. Он обеспечивает очистку и форматирование данных для улучшения читаемости и соответствия стандартам. Модуль использует библиотеки `xml.etree.ElementTree` и `xml.dom.minidom` для обработки XML.

## Функции

### `clean_empty_cdata`

```python
def clean_empty_cdata(xml_string: str) -> str:
    """! Cleans empty CDATA sections and unnecessary whitespace in XML string.

    Args:
        xml_string (str): Raw XML content.

    Returns:
        str: Cleaned and formatted XML content.
    """
```

**Назначение**: Очищает XML-строку от пустых CDATA-секций и избыточных пробелов.

**Параметры**:
- `xml_string` (str): XML-контент в виде строки.

**Возвращает**:
- `str`: Очищенный и отформатированный XML-контент.

**Как работает функция**:

1.  **Парсинг XML**: XML-строка преобразуется в дерево элементов с помощью `ET.fromstring`.
2.  **Удаление пустых элементов**: Рекурсивно обходит дерево элементов и удаляет элементы, которые не содержат текста, атрибутов или дочерних элементов.
3.  **Удаление лишних пробелов**: Использует регулярное выражение `re.sub(r">\s+<", "><", cleaned_xml)` для удаления избыточных пробелов между тегами.

```
Парсинг XML --> Удаление пустых элементов --> Удаление лишних пробелов --> Возврат очищенной XML строки
```

**Примеры**:

```python
xml_data = "<root><item>Value</item><empty></empty><item attr='test'>Another</item></root>"
cleaned_xml = clean_empty_cdata(xml_data)
print(cleaned_xml)  # Вывод: <root><item>Value</item><item attr="test">Another</item></root>
```

### `save_xml`

```python
def save_xml(xml_string: str, file_path: str) -> None:
    """! Saves cleaned XML data from a string to a file with indentation.

    Args:
        xml_string (str): XML content as a string.
        file_path (str): Path to the output file.

    Returns:
        None
    """
```

**Назначение**: Сохраняет очищенные XML-данные из строки в файл с отступами.

**Параметры**:
- `xml_string` (str): XML-контент в виде строки.
- `file_path` (str): Путь к выходному файлу.

**Возвращает**:
- `None`

**Как работает функция**:

1.  **Очистка XML**: Вызывает функцию `clean_empty_cdata` для удаления пустых элементов и избыточных пробелов из XML-строки.
2.  **Парсинг XML**: Преобразует очищенную XML-строку в дерево элементов с использованием `ET.fromstring`.
3.  **Форматирование с отступами**: Преобразует дерево элементов в строку с отступами с использованием `minidom.parseString` и `toprettyxml`.
4.  **Запись в файл**: Записывает отформатированную XML-строку в файл, указанный в `file_path`.

```
Очистка XML --> Парсинг XML --> Форматирование с отступами --> Запись в файл
```

**Примеры**:

```python
xml_data = "<root><item>Value</item><empty></empty><item attr='test'>Another</item></root>"
save_xml(xml_data, "output.xml")
```

## Пример использования

Пример использования модуля показан в блоке `if __name__ == '__main__':`. XML данные очищаются и сохраняются в файл `output.xml`.
```python
if __name__ == '__main__':
    ...
    # Пример использования
    # xml_data = """<root><item>Value</item><item attr="test">Another</item></root>"""
    # save_xml(xml_data, "output.xml")