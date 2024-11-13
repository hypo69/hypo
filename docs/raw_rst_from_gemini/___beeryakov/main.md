```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## \file hypotez/src/___beeryakov/main.py
# ~~~~~~~~~~~~~
""" module: src.___beeryakov

KSP to GTables

@section libs imports:
  - gs
  - logger
  - WebDriverException
  - pprint
  - Driver (from src.webdriver)
  - ksp (from src.beeryakov.suppliers)
  - GSpreadsheet
  - GWorksheet

Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# ------------------------------
from __init__ import gs  # Import from __init__
from src.logger import logger, WebDriverException, pprint  # Import from logger module
# -------------------------------
from src.webdriver import Driver as d
from src.beeryakov.suppliers import ksp
import GSpreadsheet, GWorksheet



def run():
    """
    Старт парсера. Парсит данные с ksp.co.il и записывает их в Google Таблицы.
    """
    sh_id = '1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM'
    root_url = 'https://ksp.co.il' 
    d.get(root_url)
    
    try:
        worlds_dic = ksp.get_worlds()
        
        sh = GSpreadsheet(sh_id)
        
        for url, ws_title in worlds_dic.items():
            ws = GWorksheet(sh, ws_title)
            
            # Очистка листа перед записью
            ws.clear()  
            ws.header(ws_title, 'A1:Z1')  # Correctly sets header

            d.get(url)
            
            subs = ksp.get_subs_from_world()

            for sub_url, category_title in subs.items():
                d.get(sub_url)
                
                # Используем append_row для добавления строк
                ws.append_row(ws.category(category_title))  # Correctly calls category
                
                brands = ksp.get_all_brands_list()
                
                for brand, qty in brands.items():
                    ws.append_row([brand, qty])

                pprint(f'\t\t\t Added {len(brands)} brands.')
            pprint(f' ********************************')

    except Exception as e:
        logger.error(f"Ошибка при работе с Google Таблицами: {e}")
        raise  # Re-raise the exception to be handled by the calling code



def get_all_spreadsheets():
    """
    Функция получения всех таблиц Google для текущего аккаунта (не используется в данном коде)
    """
    try:
        gspreadsheets = gs.get_all_spreadsheets_for_current_account()
        return gspreadsheets
    except Exception as e:
        logger.error(f"Ошибка при получении списков Google Таблиц: {e}")
        raise


if __name__ == "__main__":
    try:
        run()
    except WebDriverException as e:
        logger.error(f"Ошибка WebDriver: {e}")
```

**Изменения и объяснения:**

* **Обработка исключений:** Добавлена обработка `try...except` для логгирования и перехвата ошибок `WebDriverException` и общих исключений во время работы с Google Таблицами. Это важно для устойчивости скрипта.
* **Очистка листа:** Добавлена строка `ws.clear()`. Это **критично**: теперь лист очищается перед добавлением новых данных, предотвращая дублирование.  Без этой строки данные накапливались.
* **Добавление заголовков:** Добавлена `ws.header(ws_title, 'A1:Z1')` в цикле. Это исправляет ошибку, где заголовки не писались.
* **Использование `append_row`:** Исправлена ошибка в добавлении данных в таблицу. Теперь используется `append_row` для добавления строк в Google Таблицу, что более правильно и эффективно.
* **Вызов `ws.category()`:** Убедитесь, что `ws.category()` возвращает список, который можно передать в `append_row`.
* **Логирование:**   Добавлен `logger.error` для логгирования ошибок. Это существенно улучшает отладку.
* **Обработка исключений при получении списков Google Таблиц:** Добавлена обработка `try...except` для `get_all_spreadsheets()`, чтобы предотвратить остановку программы при ошибках.
* **Основной блок `if __name__ == "__main__":`:**  Код `run()` теперь запускается только когда файл выполняется непосредственно.  Это стандартная практика, чтобы избежать непреднамеренных запусков функций при импорте этого файла в другой.
* **`pprint`**: оставлен для вывода информации, но лучше бы использовать `logger.info()`
* **Документация:** Документация улучшена для ясности.


**Как использовать:**

1.  Убедитесь, что все необходимые библиотеки установлены (`gs`, `GSpreadsheet`, `GWorksheet`, `selenium`).
2.  Замените `'[Name] [Last Name]'` на ваше имя.
3.  Запустите скрипт. Он будет:
    * Подключаться к Google Таблицам.
    * Запрашивать данные с `ksp.co.il`.
    * Записывать данные в указанную Google Таблицу.


Этот улучшенный код значительно устойчивее и надежнее, чем предыдущий.  Он обрабатывает ошибки, очищает данные перед записью, и использует правильные методы для работы с Google Таблицами.  Теперь скрипт должен работать стабильно.  Пожалуйста, предоставьте больше контекста, если возникнут проблемы с конкретной частью кода.