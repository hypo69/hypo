# Модуль example

## Обзор

Этот модуль предоставляет примеры функций и классов для демонстрации.

## Классы

### `ExampleClass`

**Описание**:  Примерный класс для демонстрации.

**Методы**:

- `method_one`:  Метод для демонстрации работы с параметрами и возвращаемыми значениями.
- `method_two`:  Метод для демонстрации обработки исключений.


## Функции

### `example_function`

**Описание**: Функция, которая принимает на вход строку и возвращает словарь.

**Параметры**:

- `input_string` (str): Входная строка.
- `optional_data` (Optional[dict], optional): Дополнительные данные (словарь). По умолчанию `None`.

**Возвращает**:

- `dict | None`: Возвращает словарь, содержащий обработанные данные или `None`, если произошла ошибка.

**Вызывает исключения**:

- `ValueError`: Если входная строка пустая или содержит недопустимые символы.


```python
class ExampleClass:
    """
    Примерный класс для демонстрации.
    """

    def method_one(self, input_param: str, optional_param: Optional[str] = None) -> str:
        """
        Метод для демонстрации работы с параметрами и возвращаемыми значениями.

        Args:
            input_param (str): Входной параметр.
            optional_param (Optional[str], optional): Дополнительный параметр. По умолчанию None.

        Returns:
            str: Обработанный результат.
        """
        return f"Обработанный результат: {input_param}"
    
    def method_two(self, data: str) -> str:
        """
        Метод для демонстрации обработки исключений.

        Args:
            data (str): Входные данные.

        Returns:
            str: Обработанный результат.

        Raises:
            ValueError: Если входные данные не соответствуют ожидаемому формату.
        """
        if not data:
            raise ValueError("Входные данные не должны быть пустыми.")
        return f"Обработанные данные: {data}"

def example_function(input_string: str, optional_data: Optional[dict] = None) -> dict | None:
    """
    Функция, которая принимает на вход строку и возвращает словарь.

    Args:
        input_string (str): Входная строка.
        optional_data (Optional[dict], optional): Дополнительные данные (словарь). По умолчанию None.

    Returns:
        dict | None: Возвращает словарь, содержащий обработанные данные или None, если произошла ошибка.

    Raises:
        ValueError: Если входная строка пустая или содержит недопустимые символы.
    """
    if not input_string:
        raise ValueError("Входная строка не должна быть пустой.")
    
    result = {"input": input_string}
    if optional_data:
        result.update(optional_data)
    return result