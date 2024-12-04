# <input code>

```python
## \file hypotez/src/utils/jjson.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: Module for handling JSON and CSV files, including loading, dumping, and merging data.
 This module provides functions to:
- **Dump JSON data**: Convert JSON or SimpleNamespace objects into JSON format and write to a file, or return the JSON data as a dictionary.
- **Load JSON and CSV data**: Read JSON or CSV data from a file, directory, or string, and convert it into dictionaries or lists of dictionaries.
- **Convert to SimpleNamespace**: Convert loaded JSON data into SimpleNamespace objects for easier manipulation.
- **Merge JSON files**: Combine multiple JSON files from a directory into a single JSON file.
- **Parse Markdown**: Convert Markdown strings to JSON format for structured data representation.

The functions in this module handle various aspects of working with JSON and CSV data, ensuring that data is loaded, saved, and merged efficiently and effectively.
"""
MODE = 'dev'
from datetime import datetime
from math import log
from pathlib import Path
from typing import List, Dict, Optional, Any
from types import SimpleNamespace
import json
import os
import re
import pandas as pd
from json_repair import repair_json
from typing import Any
from pathlib import Path
import json
import pandas as pd
from types import SimpleNamespace
from collections import OrderedDict

from src.logger import logger
from src.utils.printer import pprint
from .convertors.dict import dict2ns
from .convertors.ns import ns2json 

# ... (rest of the code)
```

# <algorithm>

**Алгоритм работы модуля `jjson`:**

1. **`j_dumps` (dump JSON):**
    * Принимает данные (словарь, список словарей, SimpleNamespace или список SimpleNamespace), путь к файлу (опционально), параметры форматирования JSON.
    * Проверяет тип данных. Если это строка, пытается исправить JSON используя `repair_json`
    * Рекурсивно преобразует SimpleNamespace в словари с помощью `convert_to_dict`.
    * Обрабатывает списки и словари.
    * Если путь к файлу указан, определяет режим работы ("w", "a+", "+a").  Если это "a+" или "+a", загружает существующие данные из файла.
    * Объединяет данные в зависимости от режима. ("a+" - добавляет новые данные в начало, "+a" - в конец, "w" - перезаписывает)
    * Записывает данные в файл. Если файла нет, создаются все необходимые родительские директории.
    * Возвращает данные если путь к файлу не указан.


2. **`j_loads` (load JSON):**
    * Принимает данные (путь к файлу, строка JSON, словарь).
    * Обрабатывает разные типы входных данных:
        * Если путь к директории, загружает все *.json файлы, объединяет их.
        * Если путь к файлу CSV, загружает данные и преобразует в список словарей.
        * Если строка, очищает строку от трипл-тильдов и лишних символов.  Попытка декодировать.
        * Если строка JSON некорректна, пытается исправить с помощью `repair_json`.
    * Если данные корректны, загружает их. Если файл не существует, генерируется `FileNotFoundError`.
    * Возвращает загруженные данные (словарь или список словарей).


3. **`j_loads_ns` (load JSON to SimpleNamespace):**
    * Вызывает `j_loads` для загрузки данных.
    * Если данные были загружены, преобразует их в объекты `SimpleNamespace` (или список таких объектов) с помощью `dict2ns`.
    * Возвращает результат.


4. **`replace_key_in_json`:**
    * Рекурсивно заменяет ключ в словаре или списке словарей.
    * Обрабатывает вложенные структуры (списки и словари).


5. **`process_json_file`:**
    * Принимает путь к JSON-файлу.
    * Загружает данные из файла.
    * Заменяет ключ 'name' на 'category_name' с помощью `replace_key_in_json`.
    * Записывает изменённые данные обратно в файл.


6. **`recursive_process_json_files`:**
    * Принимает путь к директории.
    * Рекурсивно обходит все поддиректории и файлы *.json в заданной директории.
    * Обрабатывает каждый найденный JSON-файл с помощью `process_json_file`.


7. **`extract_json_from_string`:**
   * Извлекает JSON из строки Markdown между тегами ```json```.

**Пример данных:**
Вход: `{'old_key': 'value'}` -> Выход: `{'new_key': 'value'}`
Вход: `[{'old_key': 'value1'}, {'old_key': 'value2'}]` -> Выход: `[{'new_key': 'value1'}, {'new_key': 'value2'}]`


# <mermaid>

```mermaid
graph LR
    subgraph "Модуль jjson"
        A[j_dumps] --> B(repair_json);
        B --> C{Преобразование данных};
        C --> D[Запись в файл];
        subgraph "j_loads"
        E[j_loads] --> F{Обработка типа данных};
        F --> G[json.loads];
        G --> H[Обработка ошибок];
        end;
        E --> I[Возврат данных];
        end;
        j_loads_ns --> j_loads;
        replace_key_in_json --> j_dumps;
        process_json_file --> j_dumps;
        j_dumps --> replace_key_in_json;
        recursive_process_json_files --> process_json_file;
        extract_json_from_string --> json.loads;
    end
    A --> j_dumps;
    E --> j_loads_ns;
    I --> j_loads_ns;
    j_loads --> j_loads_ns;
    j_loads --> process_json_file;


    subgraph "Внешние зависимости"
        json_repair[json_repair] --> B;
        pandas[pandas] --> F;
        logger[logger] --> A, E;
        printer[printer] --> A;
        dict2ns[dict2ns] --> C;
        ns2json[ns2json] --> C;
    end
```

**Объяснение зависимостей:**

* `json`: Стандартный модуль Python для работы с JSON.
* `pandas`: Библиотека для обработки данных, используется для работы с CSV-файлами.
* `json_repair`: Библиотека для исправления невалидных JSON-строк.
* `logger` и `printer`: Модули для логирования и вывода информации.  Находятся в `src`
* `dict2ns`, `ns2json`: Модули для преобразования словарей в SimpleNamespace и обратно. Расположены в подпапке `convertors`.

# <explanation>

**Импорты:**

* `from datetime import datetime`, `from math import log`:  Импортируются стандартные библиотечные классы для работы со временем и математическими операциями.  Непосредственно к функциональности модуля не относятся, скорее всего нужны для других модулей или для будущей работы с временем/логированием.
* `from pathlib import Path`: Обеспечивает работу с путями к файлам, независимо от операционной системы.  Очень важный импорт для файлового взаимодействия.
* `from typing import List, Dict, Optional, Any`:  Типы данных из `typing` для ясности кода.
* `from types import SimpleNamespace`: Поддержка работы с объектами `SimpleNamespace` для более удобной обработки данных.
* `import json`: Стандартный модуль Python для работы с JSON.
* `import os`: Модуль для взаимодействия с операционной системой (например, создание директорий).
* `import re`: Регулярные выражения для работы со строками.
* `import pandas as pd`: Импорт `pandas` для обработки CSV-файлов.
* `from json_repair import repair_json`: Модуль для исправления невалидных JSON-строк.
* `from src.logger import logger`: Подключение модуля для логирования.
* `from src.utils.printer import pprint`:  Для отображения данных в понятном формате при ошибках.
* `from .convertors.dict import dict2ns`: Импорт функции для преобразования словаря в `SimpleNamespace`.
* `from .convertors.ns import ns2json`: Импорт функции для преобразования `SimpleNamespace` в словарь.


**Классы:**

Модуль содержит функции, а не классы.

**Функции:**

* **`j_dumps`:**  Запись данных в JSON-файл или возврат данных в формате JSON.  
    * `data`: данные для записи (словарь, список, SimpleNamespace или список SimpleNamespace).
    * `file_path`: путь к выводу.
    * `ensure_ascii`: флаг для экранирования не-ASCII символов.
    * `mode`: режим открытия файла.
    * `exc_info`: включение отладки ошибок.
* **`j_loads`:** Загрузка данных из JSON-файла, директории, или строки.
    * `jjson`: путь к файлу, директории, строка или словарь.
    * `ordered`: флаг для использования `OrderedDict` (чтобы сохранять порядок элементов в словаре).
    * `exc_info`: логирование информации об ошибке.
* **`j_loads_ns`:** Загрузка данных из JSON или CSV, и преобразование в `SimpleNamespace`.
* **`replace_key_in_json`:** Замена ключа во вложенных структурах (словарях и списках).  Полезная функция.
* **`process_json_file`:** Обработка JSON-файла (замена ключа `name` на `category_name`).
* **`recursive_process_json_files`:** Рекурсивный обход и обработка JSON-файлов в директории.
* **`extract_json_from_string`:** Извлечение JSON из строки Markdown.


**Переменные:**

* `MODE`: Строковая переменная, вероятно, для определения режима работы (например, `dev` или `prod`).
* `logger`: Переменная для доступа к объекту `logger` из модуля логирования.
* `pprint`: Вероятно, функция для красивой печати данных.


**Возможные ошибки и улучшения:**

* Недостаточно проверок типов. Например, `j_loads` мог бы лучше проверять типы входных данных.
* Необходимо добавить обработку различных ситуаций, включая отсутствие файлов, невалидные JSON-строки, различные типы данных.
* Документация в отдельных случаях могла быть более подробной.
* Не ясен смысл использования `repair_json` - нужно убедиться в наличии и правильности работы этой функции.
* Уточнить использование `mode` (режимы открытия файла, особенно, поведение для разных).
* Лучше было бы использовать try-except внутри функций для обработки ошибок.
* Код можно сделать более читабельным, сократив количество вложенных блоков и функций.
* Использовать `json.JSONDecodeError` вместо общего `Exception`.

**Взаимосвязи с другими частями проекта:**

Функции из этого модуля (`j_dumps`, `j_loads`, `j_loads_ns`) тесно связаны с модулем `logger` и `printer` из пакета `src`, так как использует их для вывода сообщений об ошибках и информационных сообщений.  Также зависимость от `dict2ns` и `ns2json` (обработка SimpleNamespace) отражает интеграцию с компонентами преобразования данных.