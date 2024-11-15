## \file hypotez/consultant/gemini/endpoints/prestashop/api/_experiments/header.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.endpoints.prestashop.api._experiments """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop.api._experiments """
""" Тестовые настройки для проверки PrestaAPIV.
создает словари подключеня к API Prestashop из списка `gs.presta_credentials`

"""

import os, sys
from pathlib import Path

# ----------------
dir_root = Path(os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append(str(dir_root))  # Добавляю корневую папку в sys.path
dir_src = Path(dir_root, 'src')
sys.path.append(str(dir_src))  # Добавляю src в sys.path, это важно!
# ----------------

from __init__ import gs
from src.utils import pprint, jprint
#from src.suppliers import Supplier
#from src.product import Product, ProductFields
from src.logger import logger


def get_api_credentials(api_url: str) -> dict:
    """ Функция вытаскивает из объекта глобальных настроек `gs` список словарей подключений
    к клиентским сайтам (f.e. https://e-cat.co.il/api, https://sergey.mymaster/api)
    @param api_url `str` - URI API клиента. (https://emil-design.com/api)
    @returns словарь API параметров подключения или None, если нет совпадения.
    """
    try:
        return next((item for item in gs.presta_credentials if api_url == item['api_domain']), None)
    except AttributeError as e:
        logger.error(f"Ошибка: {e}. Проверьте, что gs.presta_credentials существует и содержит корректные данные.")
        return None


emil_api_credentials = get_api_credentials('https://emil-design.com/api')
ecat_api_credentials = get_api_credentials('https://e-cat.co.il/api')

# Добавлена проверка на корректность полученных данных
if emil_api_credentials:
    print("emil_api_credentials:")
    jprint(emil_api_credentials)
else:
    print("emil_api_credentials не найдены.")

if ecat_api_credentials:
    print("\necatt_api_credentials:")
    jprint(ecat_api_credentials)
else:
    print("ecatt_api_credentials не найдены.")


```

**Изменения и объяснения:**

* **`sys.path.append(str(dir_src))`:**  Это *очень* важно!  Предыдущий код добавлял корневую папку дважды, а `src` папка не была в пути.  Теперь `src` добавляется правильно.  Это исправляет ошибку импорта.

* **Обработка исключения `AttributeError`:** Добавлено обработка исключения `AttributeError`.  Если `gs.presta_credentials` не существует или не имеет нужного формата, функция теперь возвращает `None` и выводит сообщение об ошибке в лог.  Это предотвращает сбой программы из-за неверных данных. Важно, чтобы логгер был правильно настроен и работал.

* **Проверка на `None`:**  Код теперь проверяет, возвращает ли `get_api_credentials` `None`.  Если так, выводится сообщение, что данные не найдены.  Это улучшает чтение и отладку.

* **`jprint`:**  Используйте `jprint` для красивой печати словарей.


**Как использовать:**

1.  **Убедитесь, что `gs` и `src/utils` и `src/logger` корректно импортированы.**
2.  **`gs.presta_credentials` должен содержать список словарей,** где каждый словарь описывает credentials для одного API.  Пример:

```python
gs = {
    "presta_credentials": [
        {"api_domain": "https://emil-design.com/api", "api_key": "your_api_key", ...},
        {"api_domain": "https://e-cat.co.il/api", "api_key": "another_api_key", ...},
    ]
}
```

3.  **Запустите скрипт.**  Теперь он будет выводить найденные credentials (или сообщения об ошибках), если они есть.


Этот улучшенный код более надежен, удобен в отладке и показывает, как правильно обрабатывать потенциальные ошибки.  Важное замечание:  Вы должны убедиться, что ваша структура папок соответствует этим изменениям.  Если вы используете `gs` из `__init__.py`  в другом модуле, убедитесь, что эти файлы доступны.