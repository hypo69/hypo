## \file hypotez/consultant/gemini/endpoints/advertisement/facebook/scenarios/login.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.endpoints.advertisement.facebook.scenarios """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.advertisement.facebook.scenarios """
""" Facebook login scenario """

from pathlib import Path
from typing import Dict
from __init__ import gs
from src.webdriver import Driver
from src.utils import j_loads, j_loads_ns, j_dumps
from src.logger import logger

# Загрузка локаторов для авторизации Facebook
locators_path = Path(gs.path.src, 'advertisement', 'facebook', 'locators', 'login.json')
locators = j_loads_ns(locators_path)

if locators is None:
    logger.critical(f"Ошибка загрузки локаторов из {locators_path}. Файл пустой или поврежден.")
    raise FileNotFoundError(f"Локаторы не загружены из {locators_path}")  # Поднимаем исключение


def login(d: Driver) -> bool:
    """ Выполняет вход на Facebook.

    Функция использует переданный `Driver` для выполнения авторизации на Facebook, заполняя
    логин и пароль, а затем нажимает кнопку входа.

    Args:
        d (Driver): Экземпляр драйвера для взаимодействия с веб-элементами.

    Returns:
        bool: `True`, если авторизация прошла успешно, иначе `False`.

    Raises:
        Exception: Если возникает ошибка при вводе логина, пароля или нажатии кнопки.
        FileNotFoundError: Если файл локаторов не найден или пуст.
    """
    if not hasattr(gs, 'facebook_credentials') or not gs.facebook_credentials:
      logger.critical("Переменная gs.facebook_credentials не инициализирована или пуста.")
      raise ValueError("Не заданы учетные данные для Facebook.")
    credentials = gs.facebook_credentials[0]

    try:
        # Ввод логина
        d.send_key_to_webelement(locators.get('email'), credentials.get('username'))
    except (AttributeError, KeyError) as ex:
        logger.exception(f"Ошибка ввода логина: {ex}")
        return False
    except Exception as ex:
        logger.exception(f"Непредвиденная ошибка при вводе логина: {ex}")
        return False
    
    d.wait(1.3)  # Ожидание 
    
    try:
        # Ввод пароля
        d.send_key_to_webelement(locators.get('password'), credentials.get('password'))
    except (AttributeError, KeyError) as ex:
        logger.exception(f"Ошибка ввода пароля: {ex}")
        return False
    except Exception as ex:
        logger.exception(f"Непредвиденная ошибка при вводе пароля: {ex}")
        return False

    d.wait(0.5) # Ожидание

    try:
        # Нажатие кнопки входа
        d.execute_locator(locators.get('button'))
    except (AttributeError, KeyError) as ex:
        logger.exception(f"Ошибка нажатия кнопки: {ex}")
        return False
    except Exception as ex:
        logger.exception(f"Непредвиденная ошибка при нажатии кнопки: {ex}")
        return False


    return True
```

**Изменения и пояснения:**

* **Обработка ошибок:**  Добавлены более подробные `try...except` блоки для перехватывания `AttributeError`, `KeyError` и других исключений, которые могут возникнуть при обращении к `locators` и `credentials`.  Важный момент:  использование `.get()` для доступа к элементам словаря с обработкой случаев, когда ключ отсутствует.
* **Проверка `gs.facebook_credentials`:**  Добавлена проверка, что `gs.facebook_credentials` определён и не пуст. Это предотвращает ошибку `IndexError` в случае попытки доступа к несуществующему элементу.  Поднимается `ValueError` с ясным сообщением об ошибке.
* **`logger.critical`:**  Используется `logger.critical` для ошибок, которые могут привести к полному сбою сценария (например, проблема с файлом локаторов или отсутствием необходимых данных).  Это важно для эффективной диагностики.
* **`FileNotFoundError`:** Поднимается `FileNotFoundError` в случае если локаторы не найдены, что значительно улучшает обработку ошибок.
* **`Exception`:** Обработка общего `Exception` блока в `try...except` добавлены для защиты от необработанных исключений, которые могут возникнуть во время выполнения.
* **Конкретизация сообщений об ошибках:** Сообщения об ошибках теперь содержат информацию о том, где именно произошла ошибка (например, "Ошибка ввода логина").


**Важное замечание:**  Код теперь более устойчив к различным ошибкам.  Необходимо убедиться, что `gs.path.src` и `gs.facebook_credentials` инициализированы правильно в вашем коде.  Это ключевой аспект корректной работы.  Без корректной инициализации, даже с обработкой ошибок, сценарий может упасть.  Проверяйте ваши `__init__.py` файлы и другие импортируемые модули.