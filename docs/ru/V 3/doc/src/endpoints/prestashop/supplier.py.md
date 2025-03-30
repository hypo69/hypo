# Модуль `supplier.py`

## Обзор

Модуль `supplier.py` предоставляет класс `PrestaSupplier`, предназначенный для взаимодействия с API PrestaShop для управления поставщиками. Он наследуется от класса `PrestaShop` и предоставляет функциональность для инициализации и настройки подключения к API PrestaShop с использованием предоставленных учетных данных.

## Подорбней

Этот модуль является частью подсистемы `endpoints.prestashop` проекта `hypotez` и обеспечивает абстракцию для работы с сущностями поставщиков в PrestaShop. Он использует классы `SimpleNamespace` и `PrestaShop` для организации и выполнения API-запросов. Для чтения конфигурационных файлов используется `j_loads_ns` из `src.utils.jjson`. Модуль включает в себя обработку ошибок и логирование для обеспечения стабильности и информативности работы.

## Классы

### `PrestaSupplier`

**Описание**: Класс `PrestaSupplier` предназначен для работы с поставщиками PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для взаимодействия с API PrestaShop, специфичные для поставщиков.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaSupplier`, устанавливая параметры подключения к API PrestaShop.

- `__init__(self, credentials: Optional[dict | SimpleNamespace] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None, *args, **kwards)`

    ```python
    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """Инициализация поставщика PrestaShop.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
            api_domain (Optional[str], optional): Домен API. Defaults to None.
            api_key (Optional[str], optional): Ключ API. Defaults to None.
        """
        ...
    ```
    **Описание**: Инициализирует экземпляр класса `PrestaSupplier`.

    **Параметры**:
    - `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. По умолчанию `None`.
    - `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
    - `api_key` (Optional[str], optional): Ключ API PrestaShop. По умолчанию `None`.
    - `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.
    - `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.

    **Вызывает исключения**:
    - `ValueError`: Если не указаны `api_domain` и `api_key`.

**Примеры**
```python
from types import SimpleNamespace
from src.endpoints.prestashop.supplier import PrestaSupplier

# Пример 1: Инициализация с использованием параметров
supplier = PrestaSupplier(api_domain='your_api_domain', api_key='your_api_key')

# Пример 2: Инициализация с использованием объекта SimpleNamespace
credentials = SimpleNamespace(api_domain='your_api_domain', api_key='your_api_key')
supplier = PrestaSupplier(credentials=credentials)

# Пример 3: Обработка исключения при отсутствии необходимых параметров
try:
    supplier = PrestaSupplier()
except ValueError as ex:
    print(f"Ошибка: {ex}")