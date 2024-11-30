Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `PrestaSupplier`, наследующийся от класса `PrestaShop`.  Этот класс предназначен для работы с поставщиками в системе PrestaShop.  Он инициализируется данными для доступа к API, а также содержит методы для взаимодействия с поставщиками.  Важная часть кода - проверка обязательности параметров `api_domain` и `api_key`. Если они не предоставлены, то генерируется исключение `ValueError`.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:** Код импортирует необходимые модули, такие как `SimpleNamespace`, `Optional`, `header`, `gs`, `logger`, `j_loads`, `PrestaShop`. Это необходимо для использования функций и классов из других частей проекта.

2. **Определение класса `PrestaSupplier`:** Определяется класс `PrestaSupplier`, наследующийся от класса `PrestaShop`. Это означает, что `PrestaSupplier` получает все возможности и атрибуты класса `PrestaShop`.

3. **Инициализация класса:** Метод `__init__` инициализирует экземпляр класса. Он принимает необязательные аргументы `credentials`, `api_domain`, `api_key` и `*args, **kwards`.  Если `credentials` предоставлен, то значения `api_domain` и `api_key` берутся из него, в противном случае используются переданные аргументы.

4. **Проверка параметров:** Код проверяет, что `api_domain` и `api_key` установлены. Если один из них отсутствует, то генерируется исключение `ValueError`, уведомляющее о необходимости предоставления обоих параметров.

5. **Вызов конструктора родительского класса:**  В случае успешной проверки, `super().__init__(api_domain, api_key, *args, **kwards)` вызывает конструктор родительского класса `PrestaShop`, передавая ему полученные данные для авторизации в системе.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier
    import os

    # Пример использования с creds как dict:
    credentials = {
        'api_domain': 'your_api_domain',
        'api_key': 'your_api_key'
    }

    try:
        supplier = PrestaSupplier(credentials=credentials)
        # Теперь можно использовать методы класса PrestaSupplier,
        # например, методы, унаследованные от PrestaShop.
        # ...
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Пример использования с creds как SimpleNamespace (менее распространён):
    credentials_ns = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    try:
        supplier_ns = PrestaSupplier(credentials=credentials_ns)
        # ...
    except ValueError as e:
        print(f"Ошибка: {e}")