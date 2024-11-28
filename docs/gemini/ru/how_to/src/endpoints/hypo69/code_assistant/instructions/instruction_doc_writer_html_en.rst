Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода содержит инструкции по генерации HTML-документации для Python-файлов. Он описывает, как структурировать документацию, используя заголовки разных уровней, списки, описания функций и классов, а также таблицы содержания. Документация должна соответствовать стандартам HTML и включать в себя подробные пояснения для каждой функции, класса и их методов, параметры, возвращаемые значения и возможные исключения.

Шаги выполнения
-------------------------
1. **Анализ Python-файла**: Проанализировать входной Python-файл, выделить классы, функции и методы.
2. **Создание HTML-структуры**: Создать структуру HTML-документа с использованием тегов заголовков (`<h1>`, `<h2>`, `<h3>`, `<h4>`), списков (`<ul>`, `<ol>`) и параграфов (`<p>`).
3. **Документирование классов и функций**: Для каждого класса, функции и метода создать описание с использованием тегов HTML и следующего формата комментариев в Python-коде:
   ```python
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
   ```
   Используйте `ex` вместо `e` в блоках обработки исключений.
4. **Добавление таблицы содержания (TOC)**:  В начало документации добавить таблицу содержания (TOC), которая должна содержать ссылки на все основные разделы.
5. **Форматирование документации**:  Использовать правильную HTML-синтаксис для заголовков, списков и ссылок.
6. **Пример**: Привести пример HTML-документации (в формате .md или аналогичном, для упрощения перевода в HTML).

Пример использования
-------------------------
```html
<h1>Module Name</h1>

<h2>Overview</h2>
<p>Brief description of the module's purpose.</p>

<h2>Classes</h2>

<h3>ClassName</h3>

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
```
```