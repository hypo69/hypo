# Модуль hypotez/src/utils/string/formatter.py

## Обзор

Этот модуль предоставляет функции для форматирования строк, включая удаление переносов строк, HTML-тегов, нелатинских символов и специальных символов. Он также включает функции для преобразования строк в списки, извлечения значений из строк, содержащих скобки, очистки URL-адресов и удаления чисел.

## Оглавление

* [Функции](#функции)
* [Класс StringFormatter](#класс-stringformatter)


## Функции

### `remove_line_breaks`

**Описание**: Удаляет переносы строк из входной строки.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Строка без переносов строк.


### `remove_htmls`

**Описание**: Удаляет HTML-теги из входной строки.

**Параметры**:
- `input_html` (str): Входная строка с HTML-тегами.

**Возвращает**:
- `str`: Строка без HTML-тегов.


### `escape_html_tags`

**Описание**: Заменяет символы `<` и `>` на `&lt;` и `&gt;` в входной строке с HTML-тегами.

**Параметры**:
- `input_html` (str): Входная строка с HTML-тегами.

**Возвращает**:
- `str`: Строка с экранированными HTML-тегами.


### `escape_to_html`

**Описание**: Заменяет символы на их HTML-экранированные последовательности.

**Параметры**:
- `text` (str): Входной текст.

**Возвращает**:
- `str`: Текст с замененными символами на HTML-экранированные последовательности.


### `remove_non_latin_characters`

**Описание**: Удаляет нелатинские символы из входной строки.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Строка без нелатинских символов.


### `remove_special_characters`

**Описание**: Удаляет специальные символы, не разрешенные в определенных контекстах.

**Параметры**:
- `input_str` (str | list): Входная строка или список строк.

**Возвращает**:
- `str | list`: Обработанная строка или список с удаленными специальными символами.


### `clear_numbers`

**Описание**: Очищает входную строку, оставляя только десятичные числа и точки.

**Параметры**:
- `input_str` (str): Входная строка.

**Возвращает**:
- `str`: Очищенная строка, содержащая только десятичные числа и точки.

**Пример**:
```
>>> input_str = 'aaa123.456 cde'
>>> output_str = StringFormatter.clear_numbers(input_str)
>>> print(output_str)
123.456
```


## Класс StringFormatter

### `StringFormatter`

**Описание**: Класс для форматирования строк. Предоставляет вспомогательные функции для форматирования строк, такие как удаление переносов строк, HTML-тегов, нелатинских символов и специальных символов.

**Статические методы**:

- `remove_line_breaks`: см. описание выше.
- `remove_htmls`: см. описание выше.
- `escape_html_tags`: см. описание выше.
- `escape_to_html`: см. описание выше.
- `remove_non_latin_characters`: см. описание выше.
- `remove_special_characters`: см. описание выше.
- `clear_numbers`: см. описание выше.