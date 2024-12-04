# Модуль `hypotez/src/suppliers/supplier.py`

## Обзор

Модуль `supplier.py` содержит базовый класс `Supplier` для работы с поставщиками данных. Класс отвечает за загрузку настроек, выполнение входной авторизации и запуск сценариев.

## Классы

### `Supplier`

**Описание**: Базовый класс для работы с поставщиками данных. Он загружает конфигурацию поставщика, выполняет вход и запускает сценарии.

**Атрибуты**:

- `supplier_id` (Optional[int]): Идентификатор поставщика. По умолчанию `None`.
- `supplier_prefix` (str): Префикс поставщика. Обязательный параметр.
- `locale` (str): Код локали в формате ISO 639-1. По умолчанию 'en'.
- `price_rule` (Optional[str]): Правило расчета цен. По умолчанию `None`.
- `related_modules` (Optional[ModuleType]): Функции, относящиеся к каждому поставщику.
- `scenario_files` (List[str]): Список файлов сценариев для выполнения. По умолчанию пустой список.
- `current_scenario` (Dict[str, Any]): Текущий исполняемый сценарий. По умолчанию пустой словарь.
- `locators` (Dict[str, Any]): Локаторы для элементов страницы. По умолчанию пустой словарь.
- `driver` (Optional[Driver]): Веб-драйвер. По умолчанию `None`.


**Методы**:

- `check_supplier_prefix`: Проверяет, что `supplier_prefix` не пустое значение. Возвращает значение `supplier_prefix`. Бросает исключение `ValueError`, если `supplier_prefix` пустое.
- `__init__(self, **data)`: Инициализация поставщика, загрузка конфигурации. Вызывает `super().__init__(**data)` и проверяет загрузку настроек, если загрузка не прошла - бросает `DefaultSettingsException`.
- `_payload(self)`: Загрузка параметров поставщика с использованием `j_loads_ns`. Возвращает `True`, если загрузка успешна, `False` - иначе.
  - Обрабатывает `ModuleNotFoundError`, логируя ошибку и возвращая `False`.
  - Обрабатывает `Exception`, логируя ошибку и возвращая `False`.
- `login(self)`: Выполняет вход на сайт поставщика. Возвращает `True`, если вход выполнен успешно, иначе `False`. Вызывает метод `login` из модуля `related_modules`.
- `run_scenario_files(self, scenario_files=None)`: Выполнение одного или нескольких файлов сценариев. Возвращает `True`, если все сценарии успешно выполнены, иначе `False`.  Если `scenario_files` не указан, берет список из `self.scenario_files`. Вызывает функцию `run_scenario_files` из `src.scenario`.
- `run_scenarios(self, scenarios)`: Выполнение списка или одного сценария. Возвращает `True`, если сценарий успешно выполнен, иначе `False`. Вызывает функцию `run_scenarios` из `src.scenario`.


## Модули

- `header`
- `gs`
- `src.utils.jjson`
- `src.webdriver.driver`
- `src.scenario`
- `src.logger`
- `src.logger.exceptions`


## Функции

Не содержит функций.

## Исключения

- `DefaultSettingsException`: Бросается, если произошла ошибка при загрузке настроек.
- `ValueError`: Бросается, если `supplier_prefix` пустое.
- `ModuleNotFoundError`: Бросается, если модуль, связанный с поставщиком, не найден.


## Примечания

- Класс `Supplier` использует `pydantic` для валидации данных.
- Класс `Supplier` использует `importlib` для импорта модулей, связанных с поставщиками.
- Класс `Supplier` использует `j_loads_ns` для загрузки настроек поставщика из JSON-файла.
- Методы `run_scenario_files` и `run_scenarios` вызывают функции из модуля `src.scenario`.