```markdown
# Файл: `hypotez/src/suppliers/aliexpress/api/skd/api/rest/AliexpressAffiliateOrderListbyindexRequest.py`

**Расположение:** `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\skd\api\rest\AliexpressAffiliateOrderListbyindexRequest.py`

**Роль:** `doc_creator` (генератор документации)

**Описание:**

Этот Python-файл определяет класс `AliexpressAffiliateOrderListbyindexRequest`, представляющий собой запрос к API AliExpress для получения списка заказов по партнёрской программе. Класс наследуется от `RestApi`, являющегося базовым классом для работы с REST API.

**Класс `AliexpressAffiliateOrderListbyindexRequest`:**

Этот класс предназначен для формирования запроса к API AliExpress, который возвращает список заказов по партнёрской программе.  Он позволяет задать параметры запроса, такие как:

* **`app_signature`**:  (Не описано) -  Вероятно, подпись приложения.
* **`end_time`**:  (Не описано) - Конечная дата для фильтрации заказов.
* **`fields`**:  (Не описано) - Список полей для возвращаемых данных.
* **`page_size`**:  (Не описано) - Размер страницы результатов.
* **`start_query_index_id`**:  (Не описано) - Индекс начала запроса для пагинации.
* **`start_time`**: (Не описано) - Начальная дата для фильтрации заказов.
* **`status`**: (Не описано) - Статус заказа.

**Методы:**

* **`getapiname(self)`**: Возвращает имя API-метода `aliexpress.affiliate.order.listbyindex`.

**Конструктор (`__init__`)**:

Инициализирует объект запроса:

* `domain` и `port`: Параметры подключения к API (по умолчанию `api-sg.aliexpress.com` и `80`).
* Инициализирует все перечисленные выше атрибуты (параметры запроса) со значениями по умолчанию (`None`).


**Примечание:**

Файл содержит неполные или отсутствующие комментарии к параметрам запроса.  Для создания полной документации необходимо добавить подробное описание каждой переменной и её роли в запросе к API.  Также, следует указать возможные типы данных для каждой переменной.
```