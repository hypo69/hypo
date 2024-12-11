# Тестирование модуля `doc_writer_md_ru.py`

Этот модуль содержит функцию для создания документации в формате Markdown.

## Пример использования

```python
# Пример использования функции для создания документации
from doc_writer_md_ru import generate_docstring

# Входные данные (пример)
class MyClass:
  def my_method(self, arg1, arg2):
    """Описание метода."""
    pass

# Генерация документации
docstring = generate_docstring(MyClass)

# Вывод сгенерированной документации (в консоль, файл, и т.д.)
print(docstring)
```

## Тестирование функции `generate_docstring`

```python
import pytest
from doc_writer_md_ru import generate_docstring

# Тест на корректную генерацию документации для класса
def test_generate_docstring_class():
    class MyClass:
        def my_method(self, arg1, arg2):
            """Описание метода."""
            pass
    expected_docstring = "# Класс: MyClass\n\nКласс MyClass.\n\n## Методы\n### my_method\n\nМетод my_method.\n\n## Параметры\n- `arg1`:\n- `arg2`:\n\n## Возвращаемое значение\n- Возвращает: None\n"
    actual_docstring = generate_docstring(MyClass)
    assert actual_docstring == expected_docstring
```

```python
# Тест на корректную генерацию документации для метода
def test_generate_docstring_method():
    class MyClass:
        def my_method(self, arg1, arg2):
            """Описание метода с параметрами."""
            return arg1 + arg2
    expected_docstring = "# Метод: my_method\n\nМетод my_method с параметрами.\n\n## Параметры\n- `arg1`:\n- `arg2`:\n\n## Возвращаемое значение\n- Возвращает: сумма arg1 и arg2\n"
    actual_docstring = generate_docstring(MyClass.my_method)
    assert actual_docstring == expected_docstring
```


```python
# Тест на генерацию документации для функции без параметров и возвращаемого значения.
def test_generate_docstring_function_no_params_no_return():
    def my_function():
        """Описание функции."""
        pass
    expected_docstring = "# Функция: my_function\n\nФункция my_function.\n\n## Параметры\n\n## Возвращаемое значение\n- Возвращает: None\n"
    actual_docstring = generate_docstring(my_function)
    assert actual_docstring == expected_docstring
```


```python
# Тест на обработку случая, когда у метода нет документации
def test_generate_docstring_method_no_docstring():
    class MyClass:
        def my_method(self, arg1, arg2):
            pass
    expected_docstring = "# Метод: my_method\n\nМетод my_method.\n\n## Параметры\n- `arg1`:\n- `arg2`:\n\n## Возвращаемое значение\n- Возвращает: None\n"
    actual_docstring = generate_docstring(MyClass.my_method)
    assert actual_docstring == expected_docstring
```

```python
# Тест на обработку исключения, если в функцию передается не класс или метод.
def test_generate_docstring_invalid_input():
    with pytest.raises(TypeError):
        generate_docstring(123)  # Неправильный тип данных

```


##  Описание исключений

Этот модуль не содержит специфических исключений.  Тесты проверяют корректную работу с различными входными данными.
```