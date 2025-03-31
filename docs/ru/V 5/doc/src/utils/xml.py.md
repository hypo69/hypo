# Модуль `src.utils.xml`

## Обзор

Модуль `src.utils.xml` предоставляет инструменты для работы с XML-данными, включая очистку, форматирование и сохранение XML в файл. Он включает функции для удаления пустых элементов и CDATA-секций, а также для форматирования XML с отступами.

## Подробней

Этот модуль предоставляет функции для очистки и форматирования XML-данных. Он используется для подготовки XML к сохранению в файл, удаляя ненужные пробелы и пустые элементы, что позволяет получить более чистый и читаемый XML-файл. Модуль использует библиотеки `xml.etree.ElementTree` и `xml.dom.minidom` для обработки XML.

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

**Описание**: Очищает XML-строку от пустых CDATA-секций и лишних пробелов.

**Как работает функция**:
1. Преобразует XML-строку в объект `ElementTree`.
2. Определяет рекурсивную функцию `remove_empty_elements` для удаления пустых элементов из дерева XML.
3. Рекурсивно проходит по всем элементам, удаляя пустые элементы.
4. Преобразует очищенное дерево обратно в XML-строку.
5. Удаляет лишние пробелы между тегами.

**Параметры**:
- `xml_string` (str): XML-контент в виде строки.

**Возвращает**:
- `str`: Очищенный и отформатированный XML-контент.

**Примеры**:

```python
xml_data = '<root><item>Value</item><empty></empty></root>'
cleaned_xml = clean_empty_cdata(xml_data)
print(cleaned_xml)
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

**Описание**: Сохраняет очищенные XML-данные из строки в файл с отступами.

**Как работает функция**:
1. Очищает XML-строку с помощью функции `clean_empty_cdata`.
2. Преобразует очищенную XML-строку в объект `ElementTree`.
3. Преобразует дерево XML в строку с отступами с использованием `minidom`.
4. Записывает отформатированную XML-строку в файл, указанный в `file_path`.

**Параметры**:
- `xml_string` (str): XML-контент в виде строки.
- `file_path` (str): Путь к выходному файлу.

**Возвращает**:
- `None`

**Примеры**:

```python
xml_data = '<root><item>Value</item><item attr="test">Another</item></root>'
save_xml(xml_data, "output.xml")