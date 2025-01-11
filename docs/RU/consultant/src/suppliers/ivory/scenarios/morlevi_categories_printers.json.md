# Анализ кода модуля `morlevi_categories_printers.json`

**Качество кода**
8
-   Плюсы
    -   Код имеет простую структуру и легко читается.
    -   Присутствуют основные поля, необходимые для конфигурации сценария.
-   Минусы
    -   Отсутствует описание назначения полей.
    -   Не используются константы для названий ключей.
    -   Отсутствуют какие-либо проверки корректности данных.

**Рекомендации по улучшению**

1.  **Документирование структуры:**
    -   Добавить описание каждого поля в формате reStructuredText (RST) для лучшего понимания структуры файла.
2.  **Использование констант:**
    -   Ввести константы для строковых ключей (например, `URL_KEY = "url"`, `CHECKBOX_KEY = "checkbox"`), что сделает код более устойчивым к опечаткам и облегчит рефакторинг.
3.  **Проверка данных:**
    -   Добавить валидацию типа данных для каждого поля. Например, проверить, что `checkbox` - это boolean, а `active` тоже boolean и т.д.
4.  **Форматирование JSON:**
    -   Отформатировать JSON для лучшей читаемости.

**Оптимизированный код**

```json
{
  "scenarios": {
    "url": "https://www.morlevi.co.il/Cat/60",
    "checkbox": false,
    "active": true,
    "condition": "new",
    "presta_categories": "151,209"
  }
}
```
```markdown
# Анализ кода модуля `morlevi_categories_printers.json`

**Качество кода**
8
-   Плюсы
    -   Код имеет простую структуру и легко читается.
    -   Присутствуют основные поля, необходимые для конфигурации сценария.
-   Минусы
    -   Отсутствует описание назначения полей.
    -   Не используются константы для названий ключей.
    -   Отсутствуют какие-либо проверки корректности данных.

**Рекомендации по улучшению**

1.  **Документирование структуры:**
    -   Добавить описание каждого поля в формате reStructuredText (RST) для лучшего понимания структуры файла.
2.  **Использование констант:**
    -   Ввести константы для строковых ключей (например, `URL_KEY = "url"`, `CHECKBOX_KEY = "checkbox"`), что сделает код более устойчивым к опечаткам и облегчит рефакторинг.
3.  **Проверка данных:**
    -   Добавить валидацию типа данных для каждого поля. Например, проверить, что `checkbox` - это boolean, а `active` тоже boolean и т.д.
4.  **Форматирование JSON:**
    -   Отформатировать JSON для лучшей читаемости.

**Оптимизированный код**
```json
{
    "scenarios": {
        "url": "https://www.morlevi.co.il/Cat/60",
        "checkbox": false,
        "active": true,
        "condition": "new",
        "presta_categories": "151,209"
    }
}
```
```python
# TODO: Пример реализации проверок и констант (на Python для примера)
"""
Модуль для описания сценариев парсинга категорий Morlevi.
=========================================================================================

Этот модуль содержит определения для сценариев парсинга,
включая URL, настройки чекбоксов, активности, условий и категорий PrestaShop.

Пример использования
--------------------

Пример структуры файла JSON:

.. code-block:: json

    {
        "scenarios": {
            "url": "https://www.morlevi.co.il/Cat/60",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": "151,209"
        }
    }

"""
from typing import Dict, Any
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

URL_KEY = "url"
CHECKBOX_KEY = "checkbox"
ACTIVE_KEY = "active"
CONDITION_KEY = "condition"
PRESTA_CATEGORIES_KEY = "presta_categories"

def validate_scenario(scenario: Dict[str, Any]) -> bool:
    """
    Проверяет валидность данных сценария.
    
    :param scenario: Словарь с данными сценария.
    :return: True, если сценарий валиден, иначе False.
    """
    if not isinstance(scenario.get(URL_KEY), str):
        logger.error(f"Неверный тип для {URL_KEY}")
        return False
    if not isinstance(scenario.get(CHECKBOX_KEY), bool):
        logger.error(f"Неверный тип для {CHECKBOX_KEY}")
        return False
    if not isinstance(scenario.get(ACTIVE_KEY), bool):
        logger.error(f"Неверный тип для {ACTIVE_KEY}")
        return False
    if not isinstance(scenario.get(CONDITION_KEY), str):
        logger.error(f"Неверный тип для {CONDITION_KEY}")
        return False
    if not isinstance(scenario.get(PRESTA_CATEGORIES_KEY), str):
         logger.error(f"Неверный тип для {PRESTA_CATEGORIES_KEY}")
         return False
    return True

def load_and_validate_config(file_path: str) -> Dict[str, Any]:
    """
    Загружает и проверяет конфигурацию из JSON файла.
    
    :param file_path: Путь к файлу JSON.
    :return: Словарь с конфигурацией, если она валидна, иначе пустой словарь.
    """
    try:
        config = j_loads_ns(file_path)
        if not config or not isinstance(config, dict) or "scenarios" not in config:
            logger.error(f"Ошибка: Неверная структура файла {file_path}")
            return {}
        
        scenarios = config["scenarios"]
        if not isinstance(scenarios,dict):
             logger.error(f"Ошибка: Неверная структура в ключе {scenarios}")
             return {}
             
        if validate_scenario(scenarios):
            return config
        else:
            logger.error(f"Ошибка: Неверные данные в файле {file_path}")
            return {}
    except Exception as e:
        logger.error(f"Ошибка загрузки файла {file_path}: {e}")
        return {}

# Пример использования
if __name__ == '__main__':
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_printers.json'
    config = load_and_validate_config(file_path)
    if config:
        print("Конфигурация успешно загружена и проверена:")
        print(config)
    else:
        print("Ошибка загрузки или проверки конфигурации.")
```