Как использовать модуль нормализации строк (hypotez/src/utils/string/normalizer.py)
=====================================================================================

Описание
-------------------------
Модуль `normalizer.py` предоставляет функции для нормализации различных типов данных, связанных со строками, в том числе boolean, строки и числа. Функции выполняют очистку, преобразование и валидацию входных данных, возвращая результат в указанном формате.  Если нормализация не удается, функция возвращает исходное значение.  Модуль использует модули `formatter` и `logger` для обработки строк и логирования ошибок соответственно.

Шаги выполнения
-------------------------
1. **Импортирование функций:**  Импортируйте необходимые функции из модуля `normalizer.py`:

   .. code-block:: python

       from hypotez.src.utils.string.normalizer import normalize_boolean, normalize_string, normalize_int, normalize_float

2. **Нормализация boolean значения:** Вызовите функцию `normalize_boolean`, передав в нее значение, которое требуется привести к типу boolean:

   .. code-block:: python

       boolean_value = normalize_boolean('yes')  # Пример
       print(boolean_value) # Выведет True

3. **Нормализация строки:** Вызовите функцию `normalize_string`, передав ей строку или список строк:

   .. code-block:: python

       string_value = normalize_string("  <p>Hello</p> World!  ")  # Пример
       print(string_value) # Выведет "Hello World!"
       list_of_strings = normalize_string(['Hello', '  World!  '])  # Пример со списком
       print(list_of_strings)  # Выведет "Hello World!"


4. **Нормализация целого числа:** Вызовите функцию `normalize_int`, передав ей строковое или числовое значение, которое необходимо привести к типу int:

   .. code-block:: python

       int_value = normalize_int('42') # Пример
       print(int_value) # Выведет 42

5. **Нормализация вещественного числа:** Вызовите функцию `normalize_float`, передав ей числовое значение или список чисел, которое требуется привести к типу float:

   .. code-block:: python

       float_value = normalize_float('3.14')  # Пример
       print(float_value) # Выведет 3.14
       list_of_floats = normalize_float([1, '2.5', 3])  # Пример со списком
       print(list_of_floats) # Выведет [1.0, 2.5, 3.0]

6. **Обработка ошибок:** Модуль обрабатывает ошибки при преобразованиях. Если преобразование невозможно, исходное значение возвращается, и выводится сообщение об ошибке в лог.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.string.normalizer import normalize_boolean, normalize_string, normalize_int, normalize_float

    boolean_result = normalize_boolean('on')  # Приведение к boolean
    string_result = normalize_string(['  Hello  ', 'World!']) # Нормализация списка строк
    int_result = normalize_int('123')  # Приведение к int
    float_result = normalize_float("3.14159") # Приведение к float
    invalid_result = normalize_float("abc") # Обработка ошибки

    print(boolean_result) # Выведет True
    print(string_result) # Выведет "Hello World!"
    print(int_result) # Выведет 123
    print(float_result) # Выведет 3.14159
    print(invalid_result) # Выведет "abc" (в лог будет запись об ошибке)