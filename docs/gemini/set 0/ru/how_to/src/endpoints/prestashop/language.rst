Как использовать класс PrestaLanguage
========================================================================================

Описание
-------------------------
Этот код определяет класс `PrestaLanguage`, который расширяет класс `PrestaShop`.  Этот класс предоставляет методы для работы с языками в магазине PrestaShop, такие как добавление, удаление и обновление языков, а также получение их деталей.  Он использует API PrestaShop для взаимодействия с сервером.  Класс требует валидные `api_domain` и `api_key` для авторизации.

Шаги выполнения
-------------------------
1. **Импорт необходимых библиотек**:  Код импортирует нужные модули: `SimpleNamespace`, `PrestaShop`, `gs`, `pprint`, `header`, `logger`, `PrestaShopException`, и `typing`.  Это необходимо для работы класса и взаимодействия с другими частями проекта.

2. **Определение класса `PrestaLanguage`**:  Создается класс `PrestaLanguage`, наследующий от `PrestaShop`.  В нем определены атрибуты `api_domain` и `api_key`, которые необходимы для доступа к API PrestaShop.

3. **Инициализация класса `PrestaLanguage`**: Метод `__init__` инициализирует класс. Он принимает необязательные аргументы `credentials`, `api_domain` и `api_key`. Если передан `credentials`, то значения `api_domain` и `api_key` из него будут использоваться.  Если ни `api_domain`, ни `api_key` не предоставлены, генерируется исключение `ValueError`.  Также происходит вызов конструктора родительского класса `PrestaShop`.

4. **Методы для работы с языками**: Класс предоставляет методы `add_language_PrestaShop`, `delete_language_PrestaShop`, `update_language_PrestaShop`, и `get_language_details_PrestaShop`. Они позволяют соответственно добавлять, удалять, обновлять и получать информацию о языковых настройках в магазине.

5. **Документация**: Класс и его методы снабжены подробными документами, включая описание, примеры использования и типы аргументов. Это помогает разработчикам понимать и использовать класс правильно.

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
        print("Язык успешно добавлен")
    except Exception as e:
        print(f"Ошибка добавления языка: {e}")