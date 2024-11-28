Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `PrestaSupplier`, который наследуется от класса `PrestaShop`.  Класс предназначен для работы с поставщиками в системе PrestaShop.  Он инициализируется параметрами, необходимыми для доступа к API PrestaShop, такими как `api_domain` и `api_key`.  Если эти параметры переданы в виде словаря или объекта `SimpleNamespace`, они извлекаются из него.  Если параметры не указаны явно, то генерируется исключение `ValueError`.  После успешной инициализации, происходит вызов конструктора родительского класса `PrestaShop`.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек**: Код импортирует нужные модули, такие как `SimpleNamespace`, `Optional`, `header`, `gs`, `logger`, `j_loads`, и `PrestaShop` из соответствующих файлов.
2. **Определение класса `PrestaSupplier`**: Создается класс `PrestaSupplier`, который наследуется от `PrestaShop`.
3. **Инициализация класса `PrestaSupplier`**:  Метод `__init__` принимает необязательные аргументы `credentials`, `api_domain`, и `api_key`.
4. **Обработка параметров `credentials`**: Если аргумент `credentials` передан, он используется для извлечения значений `api_domain` и `api_key` из него.
5. **Проверка наличия необходимых параметров**: Код проверяет, что `api_domain` и `api_key` определены. Если нет, то генерируется исключение `ValueError`.
6. **Вызов конструктора родительского класса**:  Код вызывает метод `__init__` родительского класса `PrestaShop`, передавая ему полученные значения `api_domain`, `api_key`, и другие аргументы.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier
    import SimpleNamespace

    # Пример использования с credentials в виде словаря
    credentials = {'api_domain': 'your_api_domain', 'api_key': 'your_api_key'}
    supplier = PrestaSupplier(credentials=credentials)

    # Пример использования с credentials в виде SimpleNamespace
    credentials_ns = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
    supplier = PrestaSupplier(credentials=credentials_ns)

    # Пример использования с explicit передачей api_domain и api_key
    supplier = PrestaSupplier(api_domain='your_api_domain', api_key='your_api_key')

    # Обратите внимание, что дальше следует код для использования созданного объекта supplier
    # (например, для выполнения запросов к API PrestaShop)