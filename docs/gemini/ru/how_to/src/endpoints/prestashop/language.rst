Как использовать класс PrestaLanguage
========================================================================================

Описание
-------------------------
Этот код определяет класс `PrestaLanguage`, который наследуется от класса `PrestaShop`.  Он предназначен для работы с настройками языков в магазине PrestaShop.  Класс предоставляет методы для добавления, удаления, обновления и получения подробностей о языках. Он также включает валидацию входных параметров для предотвращения ошибок.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**:  Код импортирует необходимые библиотеки, включая `PrestaShop`, `gs`, `pprint`, `header`, `logger`, `PrestaShopException` и `SimpleNamespace` для работы с API PrestaShop и другими вспомогательными функциями.

2. **Определение класса `PrestaLanguage`**: Определяется класс `PrestaLanguage`, который наследуется от `PrestaShop`,  позволяя использовать методы родительского класса.

3. **Документирование класса и методов**: Класс и его методы содержат строковые комментарии (docstrings), которые подробно описывают назначение класса и каждого метода, включая примеры использования. Это важный шаг для удобочитаемости и поддержки кода.

4. **Конструктор `__init__`**: Конструктор `__init__` принимает параметры `credentials`, `api_domain` и `api_key`. Он позволяет инициализировать класс с данными, полученными из словаря или объекта `SimpleNamespace`.

5. **Валидация входных данных**:  Код проверяет, что значения `api_domain` и `api_key`  установлены. Если нет, генерирует исключение `ValueError`.

6. **Наследование и инициализация родительского класса**:  Вызов `super().__init__(api_domain, api_key, *args, **kwards)` инициализирует родительский класс `PrestaShop` с полученными данными.

7. **Методы для работы с языками**: Класс предоставляет методы `add_language_PrestaShop`, `delete_language_PrestaShop`, `update_language_PrestaShop` и `get_language_details_PrestaShop` для управления языками в PrestaShop.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.language import PrestaLanguage
    import os

    # Замените на ваши данные
    API_DOMAIN = os.environ.get('API_DOMAIN')
    API_KEY = os.environ.get('API_KEY')

    prestalanguage = PrestaLanguage(api_domain=API_DOMAIN, api_key=API_KEY)
    try:
        prestalanguage.add_language_PrestaShop('English', 'en')
        print("Язык добавлен успешно.")
    except Exception as e:
        print(f"Ошибка при добавлении языка: {e}")
    
    try:
        language_details = prestalanguage.get_language_details_PrestaShop(1)
        print(language_details)
    except Exception as e:
        print(f"Ошибка при получении данных о языке: {e}")