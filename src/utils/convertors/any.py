def any2dict(any_data):
    """
    Рекурсивно преобразует любой тип данных в словарь.

    Args:
      any_data: Любой тип данных.

    Returns:
      Словарь, представляющий входные данные, или False, если преобразование невозможно.
    """
    if isinstance(any_data, dict):
        result_dict = {}
        for key, value in any_data.items():
            converted_key = any2dict(key)
            converted_value = any2dict(value)
            if converted_key is False or converted_value is False:
              return False
            result_dict[converted_key] = converted_value
        return result_dict
    elif isinstance(any_data, list) or isinstance(any_data, tuple):
        result_list = []
        for item in any_data:
            converted_item = any2dict(item)
            if converted_item is False:
                return False
            result_list.append(converted_item)
        return result_list
    elif isinstance(any_data, set):
        result_set = []
        for item in any_data:
            converted_item = any2dict(item)
            if converted_item is False:
                return False
            result_set.append(converted_item)
        return result_set
    elif isinstance(any_data, (int, float, str, bool, type(None))):
        return any_data  # Базовые типы данных возвращаем как есть
    else:
      return False  # Неподдерживаемый тип данных.

if __name__ == '__main__':
    # Примеры использования
    data1 = {
        "name": "John",
        "age": 30,
        "address": {
            "city": "New York",
            "street": "Main St",
            "numbers":[1,2,3]
        },
       "phones": ["123-456-7890", "987-654-3210"],
       "skills": {"python", "java", "c++"}
    }

    print(any2dict(data1))
    # Вывод: {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'street': 'Main St', 'numbers': [1, 2, 3]}, 'phones': ['123-456-7890', '987-654-3210'], 'skills': ['python', 'java', 'c++']}

    data2 = [1, 2, "three", {"key": "value"}]
    print(any2dict(data2))
    # Вывод: [1, 2, 'three', {'key': 'value'}]

    data3 = 123
    print(any2dict(data3))
    # Вывод: 123

    data4 = "string"
    print(any2dict(data4))
    # Вывод: string

    data5 = None
    print(any2dict(data5))
    # Вывод: None

    class MyClass:
        def __init__(self, x):
            self.x = x

    data6 = MyClass(10)
    print(any2dict(data6))
    # Вывод: False