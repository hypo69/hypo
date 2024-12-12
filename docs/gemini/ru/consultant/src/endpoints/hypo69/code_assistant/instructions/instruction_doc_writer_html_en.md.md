## Received Code
```html
<!-- INSTRUCTION -->

<p>For each input Python file, create documentation in <code>HTML</code> format for subsequent use. The documentation must meet the following requirements:</p>

<ol>
  <li>
    <strong>Documentation Format</strong>:
    <ul>
      <li>Use the <code>HTML</code> standard.</li>
      <li>Each file should begin with a header and a brief description of its contents.</li>
      <li>For all classes and functions, use the following comment format:
        <pre><code>python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Description of the `param` parameter.
        param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

    Returns:
        dict | None: Description of the return value. Returns a dictionary or `None`.

    Raises:
        SomeError: Description of the situation in which the `SomeError` exception is raised.
    """
</code></pre>
      </li>
      <li>Use <code>ex</code> instead of <code>e</code> in exception handling blocks.</li>
    </ul>
  </li>

  <li>
    <strong>TOC (Table of Contents)</strong>:
    <ul>
      <li>Include a table of contents section at the beginning of each documentation file.</li>
      <li>The structure should include links to all major sections of the module documentation.</li>
    </ul>
  </li>

  <li>
    <strong>Documentation Formatting</strong>:
    <ul>
      <li>Use proper <code>HTML</code> syntax for all headers, lists, and links.</li>
      <li>For documenting classes, functions, and methods, include structured sections with descriptions, parameter details, return values, and raised exceptions. Example:
        <pre><code>html
<h2>Functions</h2>

<h3><code>function_name</code></h3>

<p><strong>Description</strong>: Brief description of the function.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>param</code> (str): Description of the `param` parameter.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: Description of the return value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>SomeError</code>: Description of the situation in which the `SomeError` exception is raised.</li>
</ul>
</code></pre>
      </li>
    </ul>
  </li>

  <li>
    <strong>Section Headings</strong>:
    <ul>
      <li>Use level 1 headers (<code>&lt;h1&gt;</code>), level 2 headers (<code>&lt;h2&gt;</code>), level 3 headers (<code>&lt;h3&gt;</code>), and level 4 headers (<code>&lt;h4&gt;</code>) consistently throughout the file.</li>
    </ul>
  </li>

  <li>
    <strong>Example File</strong>:
    <pre><code>html
<h1>Module Name</h1>

<h2>Overview</h2>
<p>Brief description of the module's purpose.</p>

<h2>Classes</h2>

<h3><code>ClassName</code></h3>

<p><strong>Description</strong>: Brief description of the class.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>method_name</code>: Brief description of the method.</li>
</ul>

<h2>Functions</h2>

<h3><code>function_name</code></h3>

<p><strong>Description</strong>: Brief description of the function.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>param</code> (str): Description of the `param` parameter.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>dict | None</code>: Description of the return value.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>SomeError</code>: Description of the situation in which the `SomeError` exception is raised.</li>
</ul>
</code></pre>
  </li>
</ol>

<p>Generate the corresponding documentation for each input Python file in <code>HTML</code> format.</p>
<h1>## Response format: `.md` (markdown)</h1>
<!-- END OF INSTRUCTION -->
```
## Improved Code
```html
<!-- INSTRUCTION -->

<p>Для каждого входного файла Python создать документацию в формате <code>HTML</code> для последующего использования. Документация должна соответствовать следующим требованиям:</p>

<ol>
  <li>
    <strong>Формат документации</strong>:
    <ul>
      <li>Используйте стандарт <code>HTML</code>.</li>
      <li>Каждый файл должен начинаться с заголовка и краткого описания его содержимого.</li>
      <li>Для всех классов и функций использовать следующий формат комментариев:
        <pre><code>python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    :param param: Описание параметра `param`.
    :type param: str
    :param param1: Описание параметра `param1`. Значение по умолчанию `None`.
    :type param1: Optional[str | dict | str], optional
    :return: Описание возвращаемого значения. Возвращает словарь или `None`.
    :rtype: dict | None
    :raises SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
</code></pre>
      </li>
      <li>Использовать <code>ex</code> вместо <code>e</code> в блоках обработки исключений.</li>
    </ul>
  </li>

  <li>
    <strong>TOC (Оглавление)</strong>:
    <ul>
      <li>Включить раздел оглавления в начало каждого файла документации.</li>
      <li>Структура должна включать ссылки на все основные разделы документации модуля.</li>
    </ul>
  </li>

  <li>
    <strong>Форматирование документации</strong>:
    <ul>
      <li>Использовать правильный синтаксис <code>HTML</code> для всех заголовков, списков и ссылок.</li>
      <li>Для документирования классов, функций и методов включить структурированные разделы с описаниями, деталями параметров, возвращаемыми значениями и возникающими исключениями. Пример:
        <pre><code>html
<h2>Функции</h2>

<h3><code>function_name</code></h3>

<p><strong>Описание</strong>: Краткое описание функции.</p>

<p><strong>Параметры</strong>:</p>
<ul>
  <li><code>param</code> (str): Описание параметра `param`.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.</li>
</ul>

<p><strong>Возвращает</strong>:</p>
<ul>
  <li><code>dict | None</code>: Описание возвращаемого значения.</li>
</ul>

<p><strong>Вызывает исключения</strong>:</p>
<ul>
  <li><code>SomeError</code>: Описание ситуации, в которой возникает исключение `SomeError`.</li>
</ul>
</code></pre>
      </li>
    </ul>
  </li>

  <li>
    <strong>Заголовки разделов</strong>:
    <ul>
      <li>Использовать заголовки уровня 1 (<code>&lt;h1&gt;</code>), уровня 2 (<code>&lt;h2&gt;</code>), уровня 3 (<code>&lt;h3&gt;</code>) и уровня 4 (<code>&lt;h4&gt;</code>) последовательно по всему файлу.</li>
    </ul>
  </li>

  <li>
    <strong>Пример файла</strong>:
    <pre><code>html
<h1>Название модуля</h1>

<h2>Обзор</h2>
<p>Краткое описание назначения модуля.</p>

<h2>Классы</h2>

<h3><code>ClassName</code></h3>

<p><strong>Описание</strong>: Краткое описание класса.</p>

<p><strong>Методы</strong>:</p>
<ul>
  <li><code>method_name</code>: Краткое описание метода.</li>
</ul>

<h2>Функции</h2>

<h3><code>function_name</code></h3>

<p><strong>Описание</strong>: Краткое описание функции.</p>

<p><strong>Параметры</strong>:</p>
<ul>
  <li><code>param</code> (str): Описание параметра `param`.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.</li>
</ul>

<p><strong>Возвращает</strong>:</p>
<ul>
  <li><code>dict | None</code>: Описание возвращаемого значения.</li>
</ul>

<p><strong>Вызывает исключения</strong>:</p>
<ul>
  <li><code>SomeError</code>: Описание ситуации, в которой возникает исключение `SomeError`.</li>
</ul>
</code></pre>
  </li>
</ol>

<p>Сгенерировать соответствующую документацию для каждого входного файла Python в формате <code>HTML</code>.</p>
<h1>## Формат ответа: `.md` (markdown)</h1>
<!-- END OF INSTRUCTION -->
```
## Changes Made
- Добавлены описания на русском языке к инструкции.
- Заменены английские термины и фразы на русские аналоги.
- Добавлены `type` и `rtype` для более точного описания типов переменных и возвращаемых значений.
- Изменены описания параметров, возвращаемых значений и исключений в соответствии с форматом reStructuredText.
- Добавлены описания в комментариях к примеру файла в формате reStructuredText.

## FULL Code
```html
<!-- INSTRUCTION -->

<p>Для каждого входного файла Python создать документацию в формате <code>HTML</code> для последующего использования. Документация должна соответствовать следующим требованиям:</p>

<ol>
  <li>
    <strong>Формат документации</strong>:
    <ul>
      <li>Используйте стандарт <code>HTML</code>.</li>
      <li>Каждый файл должен начинаться с заголовка и краткого описания его содержимого.</li>
      <li>Для всех классов и функций использовать следующий формат комментариев:
        <pre><code>python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    :param param: Описание параметра `param`.
    :type param: str
    :param param1: Описание параметра `param1`. Значение по умолчанию `None`.
    :type param1: Optional[str | dict | str], optional
    :return: Описание возвращаемого значения. Возвращает словарь или `None`.
    :rtype: dict | None
    :raises SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
</code></pre>
      </li>
      <li>Использовать <code>ex</code> вместо <code>e</code> в блоках обработки исключений.</li>
    </ul>
  </li>

  <li>
    <strong>TOC (Оглавление)</strong>:
    <ul>
      <li>Включить раздел оглавления в начало каждого файла документации.</li>
      <li>Структура должна включать ссылки на все основные разделы документации модуля.</li>
    </ul>
  </li>

  <li>
    <strong>Форматирование документации</strong>:
    <ul>
      <li>Использовать правильный синтаксис <code>HTML</code> для всех заголовков, списков и ссылок.</li>
      <li>Для документирования классов, функций и методов включить структурированные разделы с описаниями, деталями параметров, возвращаемыми значениями и возникающими исключениями. Пример:
        <pre><code>html
<h2>Функции</h2>

<h3><code>function_name</code></h3>

<p><strong>Описание</strong>: Краткое описание функции.</p>

<p><strong>Параметры</strong>:</p>
<ul>
  <li><code>param</code> (str): Описание параметра `param`.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.</li>
</ul>

<p><strong>Возвращает</strong>:</p>
<ul>
  <li><code>dict | None</code>: Описание возвращаемого значения.</li>
</ul>

<p><strong>Вызывает исключения</strong>:</p>
<ul>
  <li><code>SomeError</code>: Описание ситуации, в которой возникает исключение `SomeError`.</li>
</ul>
</code></pre>
      </li>
    </ul>
  </li>

  <li>
    <strong>Заголовки разделов</strong>:
    <ul>
      <li>Использовать заголовки уровня 1 (<code>&lt;h1&gt;</code>), уровня 2 (<code>&lt;h2&gt;</code>), уровня 3 (<code>&lt;h3&gt;</code>) и уровня 4 (<code>&lt;h4&gt;</code>) последовательно по всему файлу.</li>
    </ul>
  </li>

  <li>
    <strong>Пример файла</strong>:
    <pre><code>html
<h1>Название модуля</h1>

<h2>Обзор</h2>
<p>Краткое описание назначения модуля.</p>

<h2>Классы</h2>

<h3><code>ClassName</code></h3>

<p><strong>Описание</strong>: Краткое описание класса.</p>

<p><strong>Методы</strong>:</p>
<ul>
  <li><code>method_name</code>: Краткое описание метода.</li>
</ul>

<h2>Функции</h2>

<h3><code>function_name</code></h3>

<p><strong>Описание</strong>: Краткое описание функции.</p>

<p><strong>Параметры</strong>:</p>
<ul>
  <li><code>param</code> (str): Описание параметра `param`.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.</li>
</ul>

<p><strong>Возвращает</strong>:</p>
<ul>
  <li><code>dict | None</code>: Описание возвращаемого значения.</li>
</ul>

<p><strong>Вызывает исключения</strong>:</p>
<ul>
  <li><code>SomeError</code>: Описание ситуации, в которой возникает исключение `SomeError`.</li>
</ul>
</code></pre>
  </li>
</ol>

<p>Сгенерировать соответствующую документацию для каждого входного файла Python в формате <code>HTML</code>.</p>
<h1>## Формат ответа: `.md` (markdown)</h1>
<!-- END OF INSTRUCTION -->