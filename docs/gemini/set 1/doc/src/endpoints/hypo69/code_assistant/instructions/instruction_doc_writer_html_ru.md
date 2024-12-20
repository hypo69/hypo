html
<h1>Инструкция по созданию документации для Python-файлов</h1>

<h2>Описание</h2>
<p>Данная инструкция описывает формат и структуру документации для Python-файлов в формате HTML.</p>

<h2>Требования</h2>

<ol>
  <li>
    <strong>Формат документации</strong>:
    <ul>
      <li>Используется стандарт HTML.</li>
      <li>Каждый файл начинается с заголовка и краткого описания.</li>
      <li>Для функций и классов используется специальный формат комментариев, описывающий параметры, возвращаемые значения и возможные исключения:</li>
      <li>Используйте <code>ex</code> вместо <code>e</code> в блоках обработки исключений.</li>
    </ul>
  </li>

  <li>
    <strong>Оглавление (TOC)</strong>:
    <ul>
      <li>В начале каждого файла документации размещается оглавление с ссылками на все разделы.</li>
    </ul>
  </li>

  <li>
    <strong>Форматирование документации</strong>:
    <ul>
      <li>Используйте правильный синтаксис HTML для заголовков, списков и ссылок.</li>
      <li>Описание функций/классов включает разделы: "Описание", "Параметры", "Возвращаемое значение", "Исключения" (примеры приведены ниже).</li>
    </ul>
  </li>

  <li>
    <strong>Заголовки разделов</strong>:
    <ul>
      <li>Используйте заголовки первого уровня (<code><h1></code>), второго уровня (<code><h2></code>), третьего уровня (<code><h3></code>) и четвертого уровня (<code><h4></code>).</li>
    </ul>
  </li>
</ol>

<h2>Пример формата документации</h2>

<pre><code>html
<h1>Модуль my_module</h1>

<h2>Обзор</h2>
<p>Краткое описание модуля.</p>

<h2>Классы</h2>

<h3>Класс MyClass</h3>

<h4>Описание</h4>
<p>Описание класса.</p>

<h4>Методы</h4>
<ul>
  <li><code>my_method</code>: Описание метода.</li>
</ul>

<h4>Параметры</h4>
<ul>
  <li><code>param1</code> (str): Описание параметра <code>param1</code>.</li>
</ul>

<h4>Возвращаемое значение</h4>
<ul>
  <li><code>str</code>: Описание возвращаемого значения.</li>
</ul>

<h4>Исключения</h4>
<ul>
  <li><code>ValueError</code>: Описание ситуации, при которой возникает <code>ValueError</code>.</li>
</ul>

<h2>Функции</h2>

<h3>Функция my_function</h3>

<h4>Описание</h4>
<p>Описание функции.</p>

<h4>Параметры</h4>
<ul>
  <li><code>param1</code> (int): Описание параметра.</li>
</ul>

<h4>Возвращаемое значение</h4>
<ul>
  <li><code>int</code>: Описание возвращаемого значения.</li>
</ul>

<h4>Исключения</h4>
<ul>
  <li><code>TypeError</code>: Описание ситуации, при которой возникает <code>TypeError</code>.</li>
</ul>
</code></pre>

<h2>Важно!</h2>
<p>Для корректной работы, пожалуйста, предоставьте Python-файлы, для которых требуется создать HTML-документацию.</p>