# Модуль aliexpress.affiliate.category.get

## Обзор

Этот модуль содержит класс `AliexpressAffiliateCategoryGetRequest`, который представляет собой API-запрос для получения информации о категориях товаров на AliExpress.  Класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateCategoryGetRequest`

**Описание**:  Класс `AliexpressAffiliateCategoryGetRequest` предоставляет методы для взаимодействия с API AliExpress для получения данных о категориях товаров.

**Конструктор**:

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
	RestApi.__init__(self,domain, port)
	self.app_signature = None
```

**Описание**: Инициализирует экземпляр класса. Принимает `domain` и `port` для API-запроса. По умолчанию используется `api-sg.aliexpress.com` и порт 80.  Инициализирует `app_signature` со значением `None`.

**Методы**:

### `getapiname`

```python
def getapiname(self):
	return 'aliexpress.affiliate.category.get'
```

**Описание**: Возвращает имя API-метода. В данном случае, это 'aliexpress.affiliate.category.get'.

**Возвращает**:

- `str`: Строковое представление имени API-метода.