```markdown
# Модуль `AliexpressAffiliateFeaturedpromoProductsGetRequest`

Файл: `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\_examples\rest\AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

**Описание:**

Данный модуль предоставляет класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, который реализует REST API запрос для получения информации о промо-товарах на AliExpress.  Этот класс наследуется от базового класса `RestApi`.

**Класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`:**

Класс `AliexpressAffiliateFeaturedpromoProductsGetRequest` используется для формирования и выполнения запроса к API AliExpress для получения списка товаров, участвующих в специальных акциях.

**Параметры:**

Класс принимает следующие параметры при инициализации:

* `domain`: Домен API (по умолчанию `api-sg.aliexpress.com`).
* `port`: Порт API (по умолчанию `80`).

Имеет следующие атрибуты, которые позволяют настраивать запрос:

* `app_signature`: Подпись приложения.
* `category_id`: ID категории товаров.
* `country`: Страна.
* `fields`: Поля, которые нужно получить (строка с разделителями).
* `page_no`: Номер страницы (для постраничного вывода).
* `page_size`: Размер страницы (для постраничного вывода).
* `promotion_end_time`: Дата окончания акции.
* `promotion_name`: Название акции.
* `promotion_start_time`: Дата начала акции.
* `sort`: Сортировка результатов.
* `target_currency`: Целевая валюта.
* `target_language`: Целевой язык.
* `tracking_id`: ID отслеживания.

**Метод `getapiname()`:**

Возвращает имя API-метода: `aliexpress.affiliate.featuredpromo.products.get`.

**Пример использования (неполный):**

```python
from ...suppliers.aliexpress.api._examples.rest import AliexpressAffiliateFeaturedpromoProductsGetRequest

# Создание экземпляра класса
request = AliexpressAffiliateFeaturedpromoProductsGetRequest()

# Установка параметров запроса
request.category_id = 123
request.page_no = 1
request.page_size = 10

# Выполнение запроса и обработка результата (оставлены для полноты)
try:
    response = request.getResponse()
    # Обработка ответа
    print(response.body)
except Exception as e:
    print(f"Ошибка: {e}")
```

**Примечания:**

* Код содержит константу `MODE = 'debug'`.  Предполагается, что она используется для настройки режима работы (отладка, производство).  Важно понимать, для чего используется эта константа в конкретной системе.
* Для полного примера использования необходимо добавить код для обработки ответа от API.
* Документация должна содержать информацию о форматах ответа от API.
* Документация должна содержать информацию об ожидаемых ошибках и их обработке.


```