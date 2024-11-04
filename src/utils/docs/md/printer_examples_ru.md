Вот обновленный файл `pprint_examples.md` с использованием "Output" вместо "Вывод":

```markdown
# Примеры использования pprint

## Пример 1: Красивый вывод словаря
```python
example_dict = {
    'name': 'Алиса',
    'age': 30,
    'hobbies': ['чтение', 'походы', 'программирование'],
    'address': {'city': 'Нью-Йорк', 'country': 'США'}
}
pprint(example_dict)
```
**Output:**
```json
{
    "name": "Алиса",
    "age": 30,
    "hobbies": [
        "чтение",
        "походы",
        "программирование"
    ],
    "address": {
        "city": "Нью-Йорк",
        "country": "США"
    }
}
```

## Пример 2: Красивый вывод списка
```python
example_list = [
    "Привет, мир!",
    Path("/example/path"),
    42,
    {"key": "value"}
]
pprint(example_list)
```
**Output:**
```
[
    Привет, мир! - <class 'str'>,
    /example/path - <class 'pathlib.PosixPath'>,
    42 - <class 'int'>,
    {'key': 'value'} - <class 'dict'>
]
```

## Пример 3: Вывод первых 5 строк из CSV файла
```python
import csv
from pathlib import Path

# Содержимое example.csv:
csv_data = """name,age,city
Алиса,30,Нью-Йорк
Боб,25,Лос-Анджелес
Чарли,35,Чикаго
Дэвид,28,Хьюстон
Ева,22,Финикс
"""
with open(Path('example.csv'), 'w', encoding='utf-8') as f:
    f.write(csv_data)

pprint('example.csv', max_lines=5)
```
**Output:**
```
CSV Header: ['name', 'age', 'city']
Row 1: ['Алиса', '30', 'Нью-Йорк']
Row 2: ['Боб', '25', 'Лос-Анджелес']
Row 3: ['Чарли', '35', 'Чикаго']
Row 4: ['Дэвид', '28', 'Хьюстон']
Row 5: ['Ева', '22', 'Финикс']
```

## Пример 4: Вывод первых 3 строк из XLS файла
```python
import pandas as pd
from pathlib import Path

# Создание DataFrame и сохранение его в Excel файл
data = {
    'name': ['Алиса', 'Боб', 'Чарли'],
    'age': [30, 25, 35],
    'city': ['Нью-Йорк', 'Лос-Анджелес', 'Чикаго']
}
df = pd.DataFrame(data)
df.to_excel('example.xls', index=False)

pprint('example.xls', max_lines=3)
```
**Output:**
```
    name  age          city
0  Алиса   30      Нью-Йорк
1    Боб   25  Лос-Анджелес
2  Чарли   35       Чикаго
```

## Пример 5: Чтение из JSON файла
```python
import json
from pathlib import Path

# Содержимое example_json.json:
dct = {
    "name": "Боб",
    "age": 25,
    "city": "Нью-Йорк",
    "skills": ["Python", "Data Science"]
}

# Сохранение словаря в JSON файл
with open(Path('example_json.json'), 'w', encoding='utf-8') as f:
    json.dump(dct, f, ensure_ascii=False, indent=4)

pprint('example_json.json')
```
**Output:**
```json
{
    "name": "Боб",
    "age": 25,
    "city": "Нью-Йорк",
    "skills": [
        "Python",
        "Data Science"
    ]
}
```

## Пример 6: Вывод 10 строк из TXT файла
```python
from pathlib import Path

s = """Строка 1: Это строка из файла.
Строка 2: Вот еще одна строка.
Строка 3: И еще одна для верности.
Строка 4: Это четвертая строка.
Строка 5: Вот пятая строка.
Строка 6: Теперь мы на шестой строке.
Строка 7: Седьмая строка здесь.
Строка 8: Это восьмая строка.
Строка 9: Девятая строка на подходе.
Строка 10: Мы достигли десятой строки.
Строка 11: Это одиннадцатая строка.
Строка 12: Теперь на двенадцатой строке.
Строка 13: Тринадцать строк прошло.
Строка 14: Почти на месте, это четырнадцатая строка.
Строка 15: Наконец, это пятнадцатая строка."""

# Сохранение текстового файла
with open(Path('example_txt.txt'), 'w', encoding='utf-8') as f:
    f.write(s)

# Вызов pprint с правильным именем файла
pprint('example_txt.txt')
```
**Output:**
```
Строка 1: Это строка из файла.
Строка 2: Вот еще одна строка.
Строка 3: И еще одна для верности.
Строка 4: Это четвертая строка.
Строка 5: Вот пятая строка.
```

## Пример 7: Красивый вывод экземпляра пользовательского класса
```python
class MyClass:
    def __init__(self, var1: str, var2: bool = False):
        self.var1 = var1
        self.var2 = var2

    def method1(self):
        return "метод1 вызван"

obj = MyClass("значение1", True)
pprint(obj)
```
**Output:**
```
Class: MyClass
['object']
Methods:
method1()
Properties:
var1 = значение1
var2 = True
```

## Пример 8: Красивый вывод вложенного списка
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pprint(nested_list)
```
**Output:**
```
[
    [
        1,
        2,
        3
    ],
    [
        4,
        5,
        6
    ],
    [
        7,
        8,
        9
    ]
]
```

## Пример 9: Красивый вывод данных, похожих на JSON
```python
example_json = {
    "name": "Боб",
    "age": 25,
    "languages": ["Python", "JavaScript"],
    "details": {"employed": True, "skills": ["Django", "Flask"]}
}
pprint(example_json)
```
**Output:**
```json
{
    "name": "Боб",
    "age": 25,
    "languages": [
        "Python",
        "JavaScript"
    ],
    "details": {
        "employed": true,
        "skills": [
            "Django",
            "Flask"
        ]
    }
}
```

## Пример 10: Вывод объекта Path
```python
pprint(Path("/example/path"))
```
**Output:**
```
/example/path
```

## Пример 11: Вывод различных примитивных типов
```python
pprint("Это простая строка.")
pprint(123)
pprint(3.14159)
pprint(True)
```
**Output:**
```
Это простая строка.
123
3.14159
True
```
```

Если нужно внести дополнительные изменения или добавления, дай знать!