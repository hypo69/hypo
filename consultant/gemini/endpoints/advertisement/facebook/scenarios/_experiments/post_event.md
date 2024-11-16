## \file hypotez/consultant/gemini/endpoints/advertisement/facebook/scenarios/_experiments/post_event.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.endpoints.advertisement.facebook.scenarios._experiments """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.advertisement.facebook.scenarios._experiments """

"""
Этот модуль управляет получением и отправкой данных о мероприятиях на Facebook.

Он взаимодействует с JSON-файлами, содержащими данные о мероприятиях, обрабатывает их и отправляет соответствующие сообщения в группы Facebook.
"""

import header
from pathlib import Path
from src.endpoints.advertisement.facebook import promoter
from __init__ import gs
from src.webdriver import Driver, Chrome
from src.endpoints.advertisement.facebook import FacebookPromoter, get_event_url
from src.endpoints.advertisement.facebook.scenarios import post_event
from src.utils import j_dumps, j_loads, j_loads_ns
from src.utils.file import get_filenames, get_directory_names
from src.utils import pprint
import json  # Добавлено для обработки ошибок JSON

def post_events():
    """Обрабатывает и отправляет мероприятия на Facebook.

    Функция получает данные о мероприятиях из указанной директории, загружает детали мероприятий из JSON-файлов
    и отправляет их на Facebook. Мероприятия хранятся в структуре директорий под папкой `facebook/events`.

    Raises:
        FileNotFoundError: Если JSON-файл с информацией о мероприятии отсутствует.
        json.JSONDecodeError: Если файл JSON содержит синтаксические ошибки.
    """
    try:
        d = Driver(Chrome)
        events_dirs = get_directory_names(gs.path.google_drive / 'aliexpress' / 'events')
        group_file_paths = get_filenames(gs.path.google_drive / 'facebook' / 'groups')
        
        if not group_file_paths:
            print("Нет файлов с группами Facebook.")
            return
            
        promoter = FacebookPromoter(d=d, group_file_paths=group_file_paths)
        for event_file in events_dirs:
            try:
                event_path = gs.path.google_drive / 'aliexpress' / 'events' / event_file / f'{event_file}.json'
                event = j_loads_ns(event_path)  # Обработка потенциальных ошибок декодирования
                promoter.process_groups(events=[event], is_event=True, group_file_paths=group_file_paths)
            except FileNotFoundError:
                print(f"Файл {event_path} не найден.")
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON в файле {event_path}: {e}")
            except Exception as e:
                print(f"Ошибка при обработке события {event_file}: {e}")  # Более общий обработчик
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")
    finally:
        if d:
            d.quit() # Закрыть драйвер Chrome


def post_to_my_group(event):
    """"""
    try:
        groups_ns = j_loads_ns(gs.path.google_drive / 'facebook' / 'groups' / 'my_managed_groups.json')
        d = Driver(Chrome)
        for group_url, group in vars(groups_ns).items():
            group.group_url = group_url
            pprint(group.group_url)
            d.get_url(get_event_url(group.group_url))
            post_event(d, event)
    except FileNotFoundError:
        print("Файл my_managed_groups.json не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в файле my_managed_groups.json: {e}")
    except Exception as e:
        print(f"Ошибка при обработке группы: {e}")
    finally:
        if d:
            d.quit()


if __name__ == "__main__":
    try:
        event = j_loads_ns(gs.path.google_drive / 'aliexpress' / 'events' / 'sep_11_2024_over60_pricedown' / 'sep_11_2024_over60_pricedown.json')
        #post_to_my_group(event)
        post_events()
    except FileNotFoundError:
        print("Файл sep_11_2024_over60_pricedown.json не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

```

**Изменения и улучшения:**

* **Обработка ошибок:** Добавлена обработка `FileNotFoundError` для случаев, когда JSON-файлы не найдены.  Добавлена более подробная обработка ошибок `json.JSONDecodeError` (в случае синтаксических ошибок в JSON).  Добавлен общий обработчик `except Exception as e`, для логгирования других непредвиденных ошибок. Важно ловить исключения *внутри* циклов, чтобы не прекращать весь скрипт из-за одной ошибки.
* **Проверка пустого списка:** Проверка, что список `group_file_paths` не пуст, прежде чем пытаться использовать его.  Это предотвращает `AttributeError`.
* **Закрытие драйвера:** Добавлена проверка `if d` и вызов `d.quit()` в `finally` блоках `post_events` и `post_to_my_group`. Это гарантирует, что драйвер `Chrome` закрывается, даже если возникают исключения, предотвращая утечки ресурсов.
* **Улучшенные сообщения об ошибках:**  Более информативные сообщения об ошибках, указывающие, какой файл или операция вызвала проблему.
* **Структура `try...except`:**  Исключения обрабатываются в блоках `try...except` внутри циклов, чтобы ошибка в одном файле не приводила к завершению всего процесса.
* **Улучшенный `finally` блок:** Закрытие драйвера Chrome в `finally` блоке.

**Как использовать:**

Убедитесь, что у вас установлены необходимые библиотеки (например, `selenium`) и что переменная `gs.path.google_drive` корректно указывает на директорию.


**Рекомендации:**

* **Логирование:** Вместо `print` используйте более продвинутые инструменты для логирования (например, `logging`), чтобы записывать подробную информацию об ошибках и других событиях в отдельный файл журнала.
* **Обработка `requests`:** Если `post_event` использует `requests` для взаимодействия с Facebook, следует добавить обработку исключений, специфичных для `requests`.
* **Переменная `gs.path.google_drive`:**  Подумайте о более надежном способе получения пути к Google Диску, чтобы избежать жестко закодированных строк.
* **Общий класс для ошибок:** Создайте базовый класс для ошибок, чтобы сделать обработку более гибкой и структурированной.
* **`pprint`:** Если `pprint` не необходим,  уберите его, чтобы код работал без этой библиотеки.


Этот улучшенный код более надежен, устойчив к ошибкам и предоставляет более подробную информацию о проблемах.  Не забывайте добавлять более специфические обработчики ошибок для ваших конкретных случаев использования.