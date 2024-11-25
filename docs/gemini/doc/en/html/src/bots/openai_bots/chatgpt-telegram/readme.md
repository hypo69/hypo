html
<h1>Голосовой помощник chatgpt - telegram</h1>

<h2>Обзор</h2>
<p>Этот модуль предоставляет интеграцию между чат-ботом ChatGPT и Telegram-ботом. Он позволяет использовать ChatGPT для обработки сообщений в Telegram.</p>

<h2>Классы</h2>

<h3><code>ChatGPTBot</code></h3>

<p><strong>Описание</strong>: Класс, представляющий бота ChatGPT, интегрированного с Telegram.</p>

<p><strong>Методы</strong>:</p>
<ul>
  <li><code>__init__(token: str, api_key: str)</code>:
    <p><strong>Описание</strong>: Инициализирует объект бота.
    <p><strong>Параметры</strong>:</p>
    <ul>
      <li><code>token</code> (str): Токен доступа к Telegram-боту.</li>
      <li><code>api_key</code> (str): API-ключ для доступа к ChatGPT.</li>
    </ul>
    </p>
    <p><strong>Возвращает</strong>:</p>
    <ul>
      <li><code>None</code>: Возвращает ничего.</li>
    </ul>
  </li>
  <li><code>process_message(update: Update)</code>:
    <p><strong>Описание</strong>: Обрабатывает поступающее сообщение из Telegram.
    <p><strong>Параметры</strong>:</p>
    <ul>
      <li><code>update</code> (Update): Объект, содержащий данные о сообщении.</li>
    </ul>
    </p>
    <p><strong>Возвращает</strong>:</p>
    <ul>
      <li><code>str | None</code>: Ответ бота или <code>None</code>, если ответ не получен.</li>
    </ul>
    <p><strong>Возможные исключения</strong>:</p>
    <ul>
      <li><code>Exception</code>:  Возможные ошибки при работе с ChatGPT или Telegram API.</li>
    </ul>
  </li>
  <li><code>send_message(chat_id: int, text: str)</code>:
    <p><strong>Описание</strong>: Отправляет сообщение в Telegram.
    <p><strong>Параметры</strong>:</p>
    <ul>
      <li><code>chat_id</code> (int): ID чата, куда нужно отправить сообщение.</li>
      <li><code>text</code> (str): Текст сообщения.</li>
    </ul>
    </p>
    <p><strong>Возвращает</strong>:</p>
    <ul>
      <li><code>bool</code>: <code>True</code>, если сообщение отправлено успешно, иначе <code>False</code>.</li>
    </ul>
    <p><strong>Возможные исключения</strong>:</p>
    <ul>
      <li><code>Exception</code>: Возможные ошибки при работе с Telegram API.</li>
    </ul>
  </li>
</ul>
</ul>


<h2>Функции</h2>

<!-- В этом разделе необходимо добавить документацию для функций, если они есть. -->


</html>