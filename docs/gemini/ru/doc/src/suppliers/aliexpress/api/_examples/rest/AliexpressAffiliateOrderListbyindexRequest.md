# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListbyindexRequest.py`

## Обзор

Модуль `AliexpressAffiliateOrderListbyindexRequest` предоставляет класс для взаимодействия с API AliExpress для получения списка заказов аффилированного партнера.  Класс наследуется от базового класса `RestApi`.  Он предоставляет методы для инициализации запроса и получения имени API.

## Классы

### `AliexpressAffiliateOrderListbyindexRequest`

**Описание**: Класс для построения и отправки запроса на получение списка заказов аффилированного партнера на AliExpress.

**Методы**:

- `__init__`

**Описание**: Инициализирует объект запроса.

**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API AliExpress.
- `port` (int, опционально, по умолчанию 80): Порт API AliExpress.

**Атрибуты**:
- `app_signature`:  Строка, представляющая подпись приложения.
- `end_time`: Конечная дата для фильтрации заказов.
- `fields`: Список полей для возвращения в ответе.
- `page_size`: Размер страницы для возвращения заказов.
- `start_query_index_id`: Начальный индекс для постраничного запроса.
- `start_time`: Начальная дата для фильтрации заказов.
- `status`: Статус заказа для фильтрации.


- `getapiname`

**Описание**: Возвращает имя API метода.

**Возвращает**:

- str: Имя API метода (`aliexpress.affiliate.order.listbyindex`).


## Функции

В данном модуле нет функций, кроме методов класса.


## Примеры использования (если есть)

```python
# Пример использования
# (Необходимо импортировать соответствующие классы и библиотеки)
request = AliexpressAffiliateOrderListbyindexRequest(
    domain="api-cn.aliexpress.com", 
    port=8080
)
request.app_signature = "your_app_signature"
request.end_time = "2024-10-27"
request.start_time = "2024-10-20"
request.page_size = 10
request.status = "success"

try:
    response = request.execute()
    # Обработка ответа
    print(response)
excep
t Exception as ex:
    print(f"Ошибка: {ex}")

```
**Примечание**:  Для использования этого класса потребуется реализовать метод `execute()` в базовом классе `RestApi`, который отвечает за отправку запроса и обработку ответа.  Также, необходимо установить необходимые библиотеки для работы с API AliExpress.  Замените `your_app_signature` на действительную подпись приложения.