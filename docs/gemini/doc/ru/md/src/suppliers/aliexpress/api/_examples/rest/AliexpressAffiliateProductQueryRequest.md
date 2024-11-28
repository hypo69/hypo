# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductQueryRequest.py`

## Обзор

Модуль `AliexpressAffiliateProductQueryRequest` предоставляет класс для запроса информации о продуктах на AliExpress с использованием API. Он наследуется от базового класса `RestApi` и предоставляет методы для настройки параметров запроса.

## Классы

### `AliexpressAffiliateProductQueryRequest`

**Описание**: Класс, представляющий запрос к API AliExpress для получения информации о продуктах по партнерским программам.

**Инициализация**:

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    RestApi.__init__(self, domain, port)
```

**Параметры конструктора**:

- `domain` (str, опционально): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, опционально): Порт API. По умолчанию `80`.

**Атрибуты**:

- `app_signature`: Атрибут для хранения подписи приложения.
- `category_ids`: Список идентификаторов категорий.
- `delivery_days`: Максимальное количество дней доставки.
- `fields`: Список полей для возврата.
- `keywords`: Ключевые слова для поиска.
- `max_sale_price`: Максимальная цена.
- `min_sale_price`: Минимальная цена.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `platform_product_type`: Тип продукта платформы.
- `ship_to_country`: Страна доставки.
- `sort`: Сортировка результатов.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.

**Методы**:

- `getapiname()`: Возвращает имя API-метода.

```python
def getapiname(self):
    return 'aliexpress.affiliate.product.query'
```

**Описание**: Возвращает строку 'aliexpress.affiliate.product.query', представляющую имя API-метода.

**Возвращает**:
- str:  Имя API-метода.


## Функции

(В данном модуле нет независимых функций)


## Примеры использования (необходимы дополнительно):

(Здесь можно добавить примеры использования класса, демонстрирующие настройку параметров и выполнение запроса)
```