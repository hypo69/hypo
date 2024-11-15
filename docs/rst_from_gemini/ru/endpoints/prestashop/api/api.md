```markdown
# api.py - Престашоп API Коннектор

Расположение: `C:\Users\user\Documents\repos\hypotez\src\endpoints\prestashop\api\api.py`

Этот модуль предоставляет класс `Prestashop` для взаимодействия с API веб-сервиса PrestaShop. Он поддерживает обмен данными в формате JSON и XML.


## Модуль: `src.endpoints.prestashop.api`

Этот модуль отвечает за взаимодействие с API Prestashop.


## Класс `Prestashop`

Класс `Prestashop` реализует методы для работы с API PrestaShop:

* **CRUD операции:** `create()`, `read()`, `write()`, `unlink()`.
* **Поиск:** `search()`.
* **Загрузка изображений:** `upload_image()`, `upload_image_async()`, `get_product_images()`.
* **Обработка ошибок:** Методы обработки ошибок ответов от сервера, включая `PrestaShopAuthenticationError` и `PrestaShopException`.
* **Работа с разными форматами:**  Поддержка JSON и XML.  Несмотря на аннотацию, рекомендуется использовать `JSON`.
* **Диспетчеризация HTTP запросов:**  Выполняет HTTP запросы через `requests` библиотеку.


### Использование

Пример использования:

```python
from prestashop import Prestashop, Format

api = Prestashop(
    API_DOMAIN="https://ваш-домен-prestashop.com",
    API_KEY="ваш_ключ_API",
    default_lang=1,
    debug=True,
    data_format='JSON',
)

# Проверка работы API
if api.ping():
    print("API доступен.")
else:
    print("Ошибка доступа к API.")

# Пример создания записи (замените на свои данные)
data = {
    'tax': {
        'rate': 3.00,
        'active': '1',
        'name': {
            'language': {
                'attrs': {'id': '1'},
                'value': '3% НДС'
            }
        }
    }
}
rec = api.create('taxes', data)
print(f"Создана запись с ID: {rec['id']}")

# ... (другие примеры использования методов) ...

```

### Параметры конструктора `Prestashop`:

* `data_format`:  Формат данных (JSON или XML). По умолчанию JSON.
* `default_lang`:  ID языка по умолчанию.
* `debug`:  Включить режим отладки.


### Методы класса `Prestashop`:

Подробное описание каждого метода (включая параметры, возвращаемые значения, обработку ошибок) должно быть дополнено.  Это особенно важно для методов `_check_response`, `_parse_response_error`, `_exec`, `_parse`.

**Важно**:

* Замените `https://ваш-домен-prestashop.com` и `ваш_ключ_API` на ваши реальные данные.
* Добавьте подробные комментарии к каждому методу, описывая его функциональность, параметры, возвращаемое значение, возможные исключения и примеры использования.
* Добавьте описания атрибутов класса `Prestashop`
* Укажите, как использовать параметры `kwargs` в методах, если они применяются.


##  Файл `__init__.py`

Файл `__init__.py` используется для импорта переменных `gs` из других модулей. Важно описать, что представляет собой переменная `gs`.


## Другие модули

Документируйте также модули `src.utils.file`, `src.utils.convertors`, `src.utils.image`, `src.utils.printer`, `src.utils.jjson`, `src.logger`, `src.logger.exceptions`.


##  Документация к  `gs`

Укажите, что содержит переменная `gs`, для чего она нужна. Опишите, как она используется в модуле.
