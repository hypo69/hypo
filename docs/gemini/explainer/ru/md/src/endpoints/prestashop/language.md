# Предоставление кода из файла `hypotez/src/endpoints/prestashop/language.py`

```markdown
## Файл `hypotez/src/endpoints/prestashop/language.py`

Этот файл определяет класс `PrestaLanguage`, который взаимодействует с API магазина PrestaShop для управления языками.

### Описание класса `PrestaLanguage`

Класс `PrestaLanguage` наследуется от класса `PrestaShop`. Он предоставляет методы для добавления, удаления, обновления и получения информации о языках магазина PrestaShop.

#### Конструктор `__init__`

Метод `__init__` инициализирует экземпляр класса `PrestaLanguage`. Он принимает следующие аргументы:

*   `credentials`: Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`.
*   `api_domain`: Домен API.
*   `api_key`: Ключ API.

Если `credentials` указан, значения `api_domain` и `api_key` из него будут использоваться.  Если ни `credentials`, ни `api_domain`, ни `api_key` не заданы, то будет выброшено исключение `ValueError`.

После инициализации, класс вызывает конструктор родительского класса `PrestaShop`, передавая ему полученные параметры `api_domain` и `api_key`.

#### Доступные методы

Класс `PrestaLanguage` предоставляет следующие методы:

*   `add_language_PrestaShop`: Добавляет новый язык в магазин PrestaShop.
*   `delete_language_PrestaShop`: Удаляет язык из магазина PrestaShop по его ID.
*   `update_language_PrestaShop`: Обновляет имя языка в магазине PrestaShop по его ID.
*   `get_language_details_PrestaShop`: Получает подробную информацию о языке по его ID.


#### Пример использования

```python
prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestalanguage.add_language_PrestaShop('English', 'en')
prestalanguage.delete_language_PrestaShop(3)
prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
print(prestalanguage.get_language_details_PrestaShop(5))
```

**Важно:**  Для корректной работы необходимо определить переменные `API_DOMAIN` и `API_KEY` в области видимости, где используется этот код.  Также предполагается, что классы `PrestaShop`, `gs`, `pprint`, `header`, `logger` и `PrestaShopException` уже определены в других файлах проекта.


### Ошибки

Класс использует исключение `ValueError`, если не указаны необходимые параметры `api_domain` и `api_key`.

### Зависимости

Код зависит от модулей:

*   `types` (для `SimpleNamespace`)
*   `.api` (для класса `PrestaShop`)
*   `src` (для `gs`)
*   `src.utils` (для `pprint`)
*   `header`
*   `src.logger`
*   `src.logger.exceptions` (для `PrestaShopException`)
*   `typing` (для `Optional`)


```