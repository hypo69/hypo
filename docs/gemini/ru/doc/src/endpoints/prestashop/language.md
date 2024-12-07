# Модуль hypotez/src/endpoints/prestashop/language.py

## Обзор

Модуль `language.py` предоставляет класс `PrestaLanguage` для управления языками в магазине PrestaShop.  Он наследуется от класса `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о языках.  Включает в себя инициализацию с использованием параметров API и обработку ошибок.


## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` предназначен для управления языками в магазине PrestaShop через API.  Он расширяет функционал базового класса `PrestaShop`, добавляя специфические методы для работы с языками.

**Методы**:

- `__init__`: Инициализирует объект `PrestaLanguage`.

#### `__init__`

**Описание**: Конструктор класса.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  None.

**Вызывает исключения**:
- `ValueError`: Если не указаны `api_domain` и `api_key`.


## Функции


(В данном файле нет независимых функций)


## Примеры использования

```python
# Пример инициализации с использованием словаря
credentials = {'api_domain': 'ваш_домен', 'api_key': 'ваш_ключ'}
prestalanguage = PrestaLanguage(credentials=credentials)

# Пример инициализации с отдельными параметрами
prestalanguage = PrestaLanguage(api_domain='ваш_домен', api_key='ваш_ключ')

# Пример использования методов
prestalanguage.add_language_PrestaShop('English', 'en')
prestalanguage.delete_language_PrestaShop(3)
prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
print(prestalanguage.get_language_details_PrestaShop(5))
```

**Примечание:**  В примере `add_language_PrestaShop`, `delete_language_PrestaShop`, `update_language_PrestaShop` и `get_language_details_PrestaShop` — это методы, которые должны быть определены в классе, но не определены в предоставленном коде.  Необходимо добавить их определения, чтобы получить полную функциональность.