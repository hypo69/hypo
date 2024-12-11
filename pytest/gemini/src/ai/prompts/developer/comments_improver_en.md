```python
import pytest

def add_numbers(a, b):
    """Adds two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
        Raises TypeError if inputs are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers.")
    return a + b


def test_add_numbers_valid_input():
    """Tests add_numbers with valid integer input."""
    assert add_numbers(5, 3) == 8
    assert add_numbers(-2, 7) == 5
    assert add_numbers(0, 0) == 0


def test_add_numbers_valid_float_input():
    """Tests add_numbers with valid float input."""
    assert add_numbers(2.5, 3.5) == 6.0
    assert add_numbers(-1.2, 4.8) == 3.6


def test_add_numbers_invalid_input_type():
    """Tests add_numbers with invalid input type (not a number)."""
    with pytest.raises(TypeError):
        add_numbers("hello", 5)
    with pytest.raises(TypeError):
        add_numbers(5, "world")
    with pytest.raises(TypeError):
        add_numbers([1, 2], 3)
    with pytest.raises(TypeError):
        add_numbers(5, {1:2})


# This test case is for string input, which raises TypeError
def test_add_numbers_invalid_string_input():
    with pytest.raises(TypeError) as excinfo:
        add_numbers("abc", 123)
    assert "Inputs must be numbers." in str(excinfo.value)



```

### Изменения:

- **Добавлены тесты:**
    - `test_add_numbers_valid_input`: Проверка корректной работы с целыми числами.
    - `test_add_numbers_valid_float_input`: Проверка корректной работы с числами с плавающей точкой.
    - `test_add_numbers_invalid_input_type`: Проверка обработки исключений `TypeError` при передаче не числовых значений.
    - `test_add_numbers_invalid_string_input`:  Добавлен тест, чтобы проверить ошибку `TypeError` для строк, который проверяет, что сообщение об ошибке точно такое, как ожидалось.
- **Улучшены имена тестов:** Имена тестов теперь более информативные и описывают цель теста.
- **Использование `pytest.raises`:** Используется `pytest.raises` для проверки исключений.
- **Ясность и читаемость:** Добавлены комментарии, поясняющие логику тестов.
- **Покрытие edge case:**  Добавлен тест на нечисловые входные данные (строки, списки, словари).
- **Дополнения:** Добавлена обработка ошибки для нечисловых типов данных в самой функции `add_numbers` для более надежной работы.
- **Уточнения:** Документация функции `add_numbers` обновлена для ясности и полноты.


**Примечание:**  Тесты проверяют корректную обработку различных типов входных данных, включая целые и вещественные числа, а также нечисловые значения, вызывая исключения `TypeError`. Это обеспечивает более полное тестирование функции.  Все тесты написаны с учетом принципов `pytest` и покрывают различные сценарии использования.  Важно использовать `pytest.raises` для проверки исключений.