Как использовать класс PrestaLanguage
=========================================================================================

Описание
-------------------------
Этот код определяет класс `PrestaLanguage`, наследующий от класса `PrestaShop`.  Он предназначен для управления языками в магазине PrestaShop. Класс предоставляет методы для добавления, удаления, обновления и получения информации о языковых настройках.  Класс инициализируется с помощью API-ключа и домена API.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:** Код импортирует необходимые модули, включая `PrestaShop`, `gs`, `pprint`, `header`, `logger`, `PrestaShopException`, и `SimpleNamespace`.

2. **Определение класса `PrestaLanguage`:** Определяется класс `PrestaLanguage`, наследующий от `PrestaShop`.  В конструкторе происходит инициализация необходимых параметров.

3. **Инициализация класса:** При создании объекта `PrestaLanguage` необходимо передать данные для подключения к API Престашоп. Это могут быть параметры `api_domain`, `api_key` или объект `credentials`, содержащий эти параметры.

4. **Проверка параметров:**  Код проверяет, что `api_domain` и `api_key` были переданы или получены из `credentials`.  Если они отсутствуют, генерируется исключение `ValueError`.

5. **Использование методов:** После инициализации можно использовать методы класса для работы с языками:
    * `add_language_PrestaShop(name, code)`: Добавляет новый язык.
    * `delete_language_PrestaShop(id)`: Удаляет язык по его идентификатору.
    * `update_language_PrestaShop(id, name)`: Обновляет имя языка по его идентификатору.
    * `get_language_details_PrestaShop(id)`: Возвращает подробную информацию о языке по его идентификатору.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.language import PrestaLanguage
    from types import SimpleNamespace

    # Пример использования с credentials
    credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    prestalanguage = PrestaLanguage(credentials=credentials)

    # Добавление языка
    prestalanguage.add_language_PrestaShop('English', 'en')

    # Удаление языка
    prestalanguage.delete_language_PrestaShop(3)


    # Обновление языка
    prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')

    # Получение данных о языке
    language_details = prestalanguage.get_language_details_PrestaShop(5)
    print(language_details)


    # Пример использования с отдельными параметрами
    prestalanguage2 = PrestaLanguage(api_domain='your_api_domain', api_key='your_api_key')