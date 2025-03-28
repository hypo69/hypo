# Документация для модуля `instruction_doc_writer_md_en.md`

## Обзор

Данный документ содержит инструкции для создания документации в формате `Markdown` для Python-файлов. Он определяет структуру и требования к оформлению документации для разработчиков.

## Содержание

- [1. Формат документации](#1-формат-документации)
- [2. Содержание (TOC)](#2-содержание-toc)
- [3. Форматирование документации](#3-форматирование-документации)
- [4. Заголовки разделов](#4-заголовки-разделов)
- [5. Пример файла](#5-пример-файла)

## 1. Формат документации

- Используйте стандарт `Markdown (.md)`.
- Каждый файл должен начинаться с заголовка и краткого описания его содержимого.
- Для всех классов и функций используйте следующий формат комментариев:

  ```python
  def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
      """
      Args:
          param (str): Описание параметра `param`.
          param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

      Returns:
          dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

      Raises:
          SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
      """
  ```

- Используйте `ex` вместо `e` в блоках обработки исключений.

## 2. Содержание (TOC)

- В начале каждого файла документации добавьте раздел с оглавлением.
- Структура оглавления должна включать ссылки на все основные разделы документации модуля.

## 3. Форматирование документации

- Используйте правильный синтаксис Markdown для всех заголовков, списков и ссылок.
- Для документирования классов, функций и методов включайте структурированные разделы с описаниями, деталями параметров, возвращаемых значений и вызываемых исключений. Пример:

  ```markdown
  ## Функции

  ### `function_name`

  **Описание**: Краткое описание функции.

  **Параметры**:
  - `param` (str): Описание параметра `param`.
  - `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

  **Возвращает**:
  - `dict | None`: Описание возвращаемого значения.

  **Вызывает исключения**:
  - `SomeError`: Описание ситуации, в которой возникает исключение `SomeError`.
  ```

## 4. Заголовки разделов

- Используйте заголовки первого уровня (`#`), второго уровня (`##`), третьего уровня (`###`) и четвёртого уровня (`####`) последовательно на протяжении всего файла.

## 5. Пример файла

```markdown
# Название модуля

## Обзор

Краткое описание назначения модуля.

## Классы

### `ClassName`

**Описание**: Краткое описание класса.

**Методы**:
- `method_name`: Краткое описание метода.
- `method_name`: Краткое описание метода.
**Параметры**:
- `param` (str): Описание параметра `param`.
- `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.


## Функции

### `function_name`

**Описание**: Краткое описание функции.

**Методы**:
- `method_name`: Краткое описание метода.
- `method_name`: Краткое описание метода.

**Параметры**:
- `param` (str): Описание параметра `param`.
- `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Описание возвращаемого значения.

**Вызывает исключения**:
- `SomeError`: Описание ситуации, в которой возникает исключение `SomeError`.
```