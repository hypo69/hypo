# Модуль KazarinovTelegramBot

## Обзор

Этот модуль реализует Telegram бота для взаимодействия с клиентами по запросам цен на товары из различных интернет-магазинов.

## Обработчик (`BotHandler`)

### Описание

Класс `BotHandler` отвечает за обработку сообщений от пользователя, парсинг ссылок на интернет-магазины и передачу данных в сценарий формирования прайслиста.

### Методы

* **`handle_message(message)`**: Обрабатывает полученное сообщение от пользователя.
    * **Описание**:  Метод принимает объект сообщения и выполняет проверку типа сообщения, а затем вызывает соответствующий обработчик сценария.
    * **Параметры**:
        * `message`: Объект сообщения от Telegram.
    * **Возвращает**:
        * `None`: Метод не возвращает значение.
    * **Вызывает исключения**:
        * `TypeError`: При неправильном типе сообщения.
        * `Exception`: При возникновении непредвиденных ошибок.


* **`parse_links(text)`**: Парсит текст сообщения и выделяет ссылки на интернет-магазины.
    * **Описание**: Метод принимает текст сообщения и извлекает из него ссылки.
    * **Параметры**:
        * `text` (str): Текст сообщения.
    * **Возвращает**:
        * `list[str]`: Список ссылок, выделенных из текста.
    * **Вызывает исключения**:
        * `ValueError`: Если текст не содержит корректных ссылок.
        * `Exception`: При возникновении непредвиденных ошибок.


## Сценарий формирования прайслиста (`scenario_pricelist`)

### Описание

Этот сценарий отвечает за извлечение данных о ценах из переданных ссылок и формирование прайслиста.

### Функции


* **`generate_pricelist(links)`**:  Генерирует прайслист по предоставленным ссылкам.
    * **Описание**: Функция принимает список ссылок и генерирует прайслист в формате, определённом для дальнейшего использования.
    * **Параметры**:
        * `links` (list[str]): Список ссылок на интернет-магазины.
    * **Возвращает**:
        * `list[dict]`: Список словарей, содержащих данные о ценах.
    * **Вызывает исключения**:
        * `ValueError`: Если ссылки невалидны или при возникновении ошибок при обращении к сайтам.
        * `Exception`: При возникновении других непредвиденных ошибок.


## Генератор прайслиста (`pricelist_generator`)

### Описание

Этот модуль отвечает за генерацию прайслиста из данных, полученных от сценария `scenario_pricelist`.

### Функции

* **`generate_output(data)`**:  Генерирует результат, передаваемый боту.
    * **Описание**: Функция принимает данные и генерирует строку вывода для Telegram бота.
    * **Параметры**:
        * `data` (list[dict]): Данные, полученные от `scenario_pricelist`.
    * **Возвращает**:
        * `str`: Строка с отформатированными данными для отправки в Telegram.
    * **Вызывает исключения**:
        * `TypeError`: Если входные данные не соответствуют ожидаемому типу.
        * `Exception`: При возникновении непредвиденных ошибок.