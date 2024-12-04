Как использовать модули src.utils и src.utils.converters
========================================================================================

Описание
-------------------------
Модули `src.utils` и `src.utils.converters` содержат служебные утилиты проекта.  Они предназначены для минимизации использования внутренних утилит, таких как `j_loads`, `j_loads_ns` и `j_dumps`.  Вместо них в этих модулях используется стандартная библиотека `json`.

Шаги выполнения
-------------------------
1. Импортируйте модуль `json`:
   ```python
   import json
   ```
2. Для работы с JSON-данными используйте функции `json.loads()` и `json.dumps()` вместо устаревших методов. Например, для загрузки JSON-строки:
   ```python
   json_string = '{"key": "value"}'
   data = json.loads(json_string)
   ```
3. При работе с модулями `src.utils` и `src.utils.converters` убедитесь, что вы используете `json.loads()` и `json.dumps()` для работы с JSON-данными. Избегайте использования `j_loads`, `j_loads_ns` и `j_dumps`.


Пример использования
-------------------------
.. code-block:: python

    import json
    from src.utils import some_utility_function  # Пример импорта функции из src.utils

    json_string = '{"name": "John Doe", "age": 30}'

    try:
        data = json.loads(json_string)
        result = some_utility_function(data)
        print(json.dumps(result, indent=4))  # Важно: используйте json.dumps для вывода данных
    except json.JSONDecodeError as e:
        print(f"Ошибка при декодировании JSON: {e}")