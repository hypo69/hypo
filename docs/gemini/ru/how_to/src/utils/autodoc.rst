Как использовать декоратор autodoc для автоматического обновления docstring функции
=================================================================================

Описание
-------------------------
Этот декоратор `autodoc` автоматически обновляет строку документации (docstring) функции, добавляя в неё время последнего вызова.  Декоратор используется для того, чтобы сохранять актуальную информацию о времени выполнения функции в её docstring.  Он оборачивает функцию и перед каждым вызовом обновляет её docstring, добавляя строку с текущим временем.

Шаги выполнения
-------------------------
1. **Импортировать необходимые модули:**  Модули `functools` и `time` необходимы для работы декоратора.
2. **Определить декоратор `autodoc`:**  Декоратор `autodoc` принимает функцию в качестве аргумента.
3. **Обновить docstring внутри декоратора `autodoc`:** Внутри декоратора функция `update_docstring` обновляет docstring функции, добавляя строку с текущим временем.
4. **Проверить наличие docstring:**  Код проверяет, существует ли у функции docstring, прежде чем добавлять к нему информацию о времени.
5. **Добавить информацию о времени последнего вызова:**  Добавляет строку с форматированным временем в docstring.
6. **Возвратить обернутую функцию:** Декоратор возвращает обернутую функцию `wrapper`.

Пример использования
-------------------------
.. code-block:: python

    import time
    import functools
    
    def autodoc(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            update_docstring(func)
            return func(*args, **kwargs)
        return wrapper
    
    def update_docstring(func):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        if func.__doc__:
            func.__doc__ += f"\n\nLast called at: {current_time}"
        else:
            func.__doc__ = f"Last called at: {current_time}"
            
    @autodoc
    def example_function(param1: int, param2: str) -> None:
        """Пример функции.

        Args:
            param1 (int): Первое значение.
            param2 (str): Второе значение.
        """
        print(f"Processing {param1} and {param2}")
        
    example_function(1, "test")
    print(example_function.__doc__)  # Вывод обновленного docstring
    example_function(2, "another test")
    print(example_function.__doc__)  # Вывод обновленного docstring