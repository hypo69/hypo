html
<h1>Инструкция по генерации документации</h1>

<h2>Описание</h2>
<p>Данная инструкция описывает процесс создания документации для Python-файлов в формате Markdown.</p>

<h2>Требования к документации</h2>

<ol>
  <li>
    <h3>Формат документации</h3>
    <ul>
      <li>Используйте стандарт Markdown (.md).</li>
      <li>Каждый файл должен начинаться с заголовка и краткого описания его содержимого.</li>
      <li>Для всех классов и функций используйте следующий формат комментариев:</li>
      <pre><code>python
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
</code></pre>
      <li>Используйте `ex` вместо `e` в блоках обработки исключений.</li>
    </ul>
  </li>

  <li>
    <h3>Содержание (TOC)</h3>
    <ul>
      <li>В начале каждого файла документации добавьте раздел с оглавлением.</li>
      <li>Структура оглавления должна включать ссылки на все основные разделы документации модуля.</li>
    </ul>
  </li>

  <li>
    <h3>Форматирование документации</h3>
    <ul>
      <li>Используйте правильный синтаксис Markdown для всех заголовков, списков и ссылок.</li>
      <li>Для документирования классов, функций и методов используйте структурированные разделы с описаниями, параметрами, возвращаемыми значениями и исключениями. Пример:</li>
      <pre><code>markdown
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
</code></pre>
    </ul>
  </li>

  <li>
    <h3>Заголовки разделов</h3>
    <ul>
      <li>Используйте заголовки первого уровня (#), второго уровня (##), третьего уровня (###) и четвёртого уровня (####) последовательно на протяжении всего файла.</li>
    </ul>
  </li>

  <li>
    <h3>Пример файла</h3>
    <pre><code>markdown
# Название модуля

## Обзор

Краткое описание назначения модуля.

## Классы

### `ClassName`

**Описание**: Краткое описание класса.

**Методы**:
- `method_name`: Краткое описание метода.

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
</code></pre>
  </li>
</ol>

<h2>Заключение</h2>
<p>Следуя данным требованиям, вы сможете генерировать хорошо структурированную и понятную документацию для ваших Python-файлов.</p>