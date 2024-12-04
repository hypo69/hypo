Как использовать модуль `hypotez/src/scenario/__init__.py`
==========================================================================================

Описание
-------------------------
Этот модуль предоставляет функции для выполнения сценариев. Он предназначен для управления выполнением сценариев поставщиками, такими как AliExpress, и их интеграцией с системой PrestaShop. Модуль предоставляет функции для работы с файлами сценариев и с отдельными сценариями, предоставляя гибкость в управлении.

Шаги выполнения
-------------------------
1. **Инициализация поставщика**:  Создайте экземпляр класса `Supplier`, передав в конструктор имя поставщика (например, 'aliexpress').  Это необходимо для указания, с каким поставщиком будут работать сценарии.
    ```python
    s = Supplier('aliexpress')
    ```
2. **Выполнение сценариев из файлов**:  Для выполнения сценариев, определённых в файлах, используйте функцию `run_scenario_files`.  Передайте экземпляр поставщика `s` и список путей к файлам сценариев.
    ```python
    scenario_files = ['file1', 'file2']
    run_scenario_files(s, scenario_files)
    ```
3. **Выполнение отдельных сценариев**:  Функция `run_scenarios` позволяет выполнять сценарии, представленные в виде словарей.  Передайте экземпляр поставщика `s` и список или словарь сценариев.
    ```python
    scenario1 = {'key': 'value'}
    run_scenarios(s, scenario1)
    
    list_of_scenarios = [scenario1, scenario2]
    run_scenarios(s, list_of_scenarios)
    ```
4. **Обработка сценариев в файлах**: Кажды файл сценария должен содержать структурированные данные, обычно в формате JSON, описывающие сценарий.  Пример структуры файла сценария:
    ```json
    {
      "scenarios": {
        "feet-hand-treatment": {
          "url": "https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/",
          "name": "Foot and Hand Care",
          "condition": "new",
          "presta_categories": {
            "default_category": 11259,
            "additional_categories": []
          }
        },
        // другие сценарии
      }
    }
    ```


Пример использования
-------------------------
```python
from hypotez.src.scenario import run_scenario_files, run_scenarios
from hypotez.src.scenario.supplier import Supplier

# Инициализация поставщика
s = Supplier('aliexpress')

# Список файлов сценариев
scenario_files = ['path/to/file1.json', 'path/to/file2.json']

# Выполнение сценариев из файлов
run_scenario_files(s, scenario_files)

# Список отдельных сценариев
scenario1 = {'key': 'value', 'param2': 123}
run_scenarios(s, scenario1)

list_of_scenarios = [
    {'key': 'value1', 'param2': 456},
    {'key': 'value2', 'param3': True}
]

run_scenarios(s, list_of_scenarios)
```

**Примечание:**  В примере пути к файлам сценариев нужно заменить на фактические пути.
```
```
```
```
```
```