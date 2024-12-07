html
<h1>Инструкция по созданию документации в формате HTML</h1>

<p>Данная инструкция описывает процесс создания документации для Python-файлов в формате HTML. Документация должна соответствовать указанным требованиям.</p>

<h2>Требования к формату документации</h2>

<ol>
  <li>
    <strong>Формат документации</strong>:
    <ul>
      <li>Используйте стандарт HTML.</li>
      <li>Каждый файл должен начинаться с заголовка и краткого описания его содержимого.</li>
      <li>Для всех классов и функций используйте следующий формат комментариев:</li>
      <pre><code>python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Описание параметра <code>param</code>.
        param1 (Optional[str | dict | str], optional): Описание параметра <code>param1</code>. По умолчанию значение равно <code>None</code>.

    Returns:
        dict | None: Описание возвращаемого значения. Возвращает словарь или <code>None</code>.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение <code>SomeError</code>.
    """
</code></pre>
      <li>Используйте <code>ex</code> вместо <code>e</code> в блоках обработки исключений.</li>
    </ul>
  </li>
  <li>
    <strong>Оглавление (TOC)</strong>:
    <ul>
      <li>Включите раздел оглавления в начале каждого документа.</li>
      <li>Структура должна включать ссылки на все основные разделы документации модуля.</li>
    </ul>
  </li>
  <li>
    <strong>Форматирование документации</strong>:
    <ul>
      <li>Используйте правильный синтаксис HTML для всех заголовков, списков и ссылок.</li>
      <li>Для документирования классов, функций и методов включайте структурированные разделы с описаниями, деталями параметров, значениями возвращаемых данных и поднятыми исключениями.  Пример:</li>
      <pre><code>html
<h2>Функции</h2>

<h3><code>function_name</code></h3>

<p><strong>Описание</strong>: Краткое описание функции.</p>

<p><strong>Параметры</strong>:</p>
<ul>
  <li><code>param</code> (str): Описание параметра <code>param</code>.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Описание параметра <code>param1</code>. По умолчанию значение равно <code>None</code>.</li>
</ul>

<p><strong>Возвращаемое значение</strong>:</p>
<ul>
  <li><code>dict | None</code>: Описание возвращаемого значения.</li>
</ul>

<p><strong>Исключения</strong>:</p>
<ul>
  <li><code>SomeError</code>: Описание ситуации, в которой возникает исключение <code>SomeError</code>.</li>
</ul>
</code></pre>
      </li>
    </ul>
  </li>
  <li>
    <strong>Заголовки разделов</strong>:
    <ul>
      <li>Используйте заголовки первого уровня (<code><h1></code>), второго уровня (<code><h2></code>), третьего уровня (<code><h3></code>) и четвертого уровня (<code><h4></code>) последовательно по всему файлу.</li>
    </ul>
  </li>
</ol>

<h2>Пример файла (HTML)</h2>

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
  <li><code>param</code> (str): Описание параметра <code>param</code>.</li>
  <li><code>param1</code> (Optional[str | dict | str], optional): Описание параметра <code>param1</code>. По умолчанию значение равно <code>None</code>.</li>
</ul>

<p><strong>Возвращаемое значение</strong>:</p>
<ul>
  <li><code>dict | None</code>: Описание возвращаемого значения.</li>
</ul>

<p><strong>Исключения</strong>:</p>
<ul>
  <li><code>SomeError</code>: Описание ситуации, в которой возникает исключение <code>SomeError</code>.</li>
</ul>
</code></pre>

<p>Создайте соответствующую документацию для каждого входного Python-файла в формате HTML.</p>

```