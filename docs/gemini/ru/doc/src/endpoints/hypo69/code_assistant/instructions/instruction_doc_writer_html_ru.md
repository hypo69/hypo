html
<h1>Инструкция по созданию документации в формате HTML</h1>

<p>Данная инструкция описывает процесс создания HTML-документации для Python-файлов.</p>

<h2>Требования</h2>

<ol>
  <li>
    <h3>Формат документации</h3>
    <ul>
      <li>Используйте стандарт HTML.</li>
      <li>Каждый файл должен начинаться с заголовка и краткого описания его содержимого.</li>
      <li>Для функций и методов используйте следующий формат комментариев:</li>
      <pre><code>python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Описание параметра param.
        param1 (Optional[str | dict | str], optional): Описание параметра param1. По умолчанию значение None.

    Returns:
        dict | None: Описание возвращаемого значения. Возвращает словарь или None.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение SomeError.
    """
</code></pre>
      <li>Используйте <code>ex</code> вместо <code>e</code> в блоках обработки исключений.</li>
    </ul>
  </li>

  <li>
    <h3>Оглавление (TOC)</h3>
    <ul>
      <li>Включите раздел оглавления в начале каждого документа.</li>
      <li>Структура должна включать ссылки на все основные разделы документации модуля.</li>
    </ul>
  </li>

  <li>
    <h3>Форматирование документации</h3>
    <ul>
      <li>Используйте правильный синтаксис HTML для всех заголовков, списков и ссылок.</li>
      <li>Для документирования классов, функций и методов включайте структурированные разделы с описаниями, параметрами, возвращаемыми значениями и исключениями. Пример:</li>
    </ul>
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

  <li>
    <h3>Заголовки разделов</h3>
    <ul>
      <li>Используйте заголовки первого уровня (<code><h1></code>), второго уровня (<code><h2></code>), третьего уровня (<code><h3></code>) и четвёртого уровня (<code><h4></code>) последовательно.</li>
    </ul>
  </li>
</ol>

<h2>Пример файла</h2>
<pre><code class="language-html"><h1>Название модуля</h1>

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

<p><strong>Возвращает</strong>:</p>
<ul>
  <li><code>dict | None</code>: Описание возвращаемого значения.</li>
</ul>

<p><strong>Вызывает исключения</strong>:</p>
<ul>
  <li><code>SomeError</code>: Описание ситуации, в которой возникает исключение <code>SomeError</code>.</li>
</ul>
</code></pre>

<p>Следуйте этим инструкциям при создании HTML-документации для ваших Python-файлов.</p>