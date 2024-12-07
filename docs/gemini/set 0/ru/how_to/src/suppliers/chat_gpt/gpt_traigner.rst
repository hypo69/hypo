Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предназначен для сбора данных диалогов из файлов HTML, хранящихся в папке "conversation" на Google Диске.  Он парсит файлы, извлекает текст сообщений пользователя и чат-бота, очищает его, и сохраняет результаты в нескольких форматах: CSV, JSONL и текстовый файл с необработанными данными.  Также определяет и записывает в данные "sentiment" (положительный, отрицательный или нейтральный), но в данном примере используется значение "neutral".


Шаги выполнения
-------------------------
1. **Инициализация:** Создается экземпляр класса `GPT_Traigner`.  Этот класс, по-видимому, взаимодействует с веб-драйвером (Chrome, Firefox или Edge) и  инструментарием для работы с Google Диском.
2. **Получение списка файлов HTML:**  Функция `dump_downloaded_conversations` определяет все файлы с расширением `.html` в указанной папке на Google Диске.
3. **Обработка каждого файла:** Для каждого файла выполняется:
    * **Загрузка страницы:**  Веб-драйвер загружает страницу с содержимым файла HTML.
    * **Поиск элементов:** Используя `locator`, который содержит информацию о расположении элементов на странице (сообщения пользователя и чат-бота),  получаются элементы с текстом сообщений.
    * **Извлечение текста:**  Извлекается текст из найденных элементов. Обрабатываются случаи, когда элементы не найдены или возвращают пустые значения.
    * **Обработка пар "пользователь-чат-бот":** Для каждой пары сообщений (пользователь и чат-бот) создаётся словарь с данными, где `role` определяет, чье это сообщение, `content` - содержимое сообщения, а `sentiment` - определённый (в данном случае, нейтральный)
    * **Добавление к списку:** Результат добавляется в список `all_data`.
    * **Проверка и обработка ошибок:** Проверяется, получен ли текст от обоих источников, и, если нет, выводится сообщение об ошибке в лог.
4. **Объединение данных:** После обработки всех файлов данные собираются в единую таблицу Pandas (`all_data_df`).
5. **Сохранение данных:** Результаты сохраняются в следующие файлы:
    * CSV файл (`all_conversations.csv`): Содержит данные в формате CSV.
    * JSONL файл (`all_conversations.jsonl`): Содержит данные в формате JSON Lines.
    * Текстовый файл (`raw_conversations.txt`): Содержит необработанные данные в строковом формате.  Это, вероятно, используется для использования с другими инструментами, не требующими формата CSV или JSONL.
6. **Дополнительные действия:**
    * Запуск модели для обработки данных (используется класс `Model`).  Этот шаг происходит после сохранения данных.  Для работы с `model` необходимы данные в формате CSV.
7. **Выполнение:**  Код запускается путем вызова метода `dump_downloaded_conversations`.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.chat_gpt import GPT_Traigner
    from hypotez.src import gs

    # Инициализация
    traigner = GPT_Traigner()

    # Выполнение
    traigner.dump_downloaded_conversations()