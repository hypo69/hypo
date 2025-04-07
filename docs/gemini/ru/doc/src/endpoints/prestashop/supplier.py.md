# Модуль для работы с поставщиками PrestaShop

## Обзор

Модуль `src.endpoints.prestashop.supplier` предназначен для взаимодействия с API PrestaShop для управления информацией о поставщиках. Он содержит класс `PrestaSupplier`, который расширяет базовый класс `PrestaShop` и предоставляет функциональность для работы с поставщиками.

## Подробней

Этот модуль предоставляет класс `PrestaSupplier`, который упрощает взаимодействие с API PrestaShop для управления поставщиками. Он позволяет инициализировать подключение к PrestaShop с использованием домена API и ключа API, а также предоставляет методы для выполнения запросов к API, специфичных для поставщиков. Модуль использует библиотеки `requests` для выполнения HTTP-запросов и `xml.etree.ElementTree` для обработки XML-ответов от API PrestaShop.
Расположение файла в проекте указывает на то, что он является частью подсистемы, отвечающей за интеграцию с PrestaShop, и, вероятно, используется для автоматизации задач, связанных с управлением поставщиками, таких как получение информации о поставщиках, создание, обновление или удаление записей о поставщиках.

## Классы

### `PrestaSupplier`

**Описание**: Класс для работы с поставщиками PrestaShop.

**Наследует**:
- `PrestaShop`:  Этот класс наследует функциональность для взаимодействия с API PrestaShop.

**Аттрибуты**:
- Нет специфичных атрибутов, все атрибуты наследуются от `PrestaShop`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaSupplier`.

### `PrestaSupplier.__init__`

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
```

**Назначение**: Инициализация класса `PrestaSupplier`, устанавливает соединение с API PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace`, содержащий параметры `api_domain` и `api_key`. Используется для аутентификации в API. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API PrestaShop. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API для доступа к PrestaShop. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.

**Возвращает**:
- None

**Вызывает исключения**:
- `ValueError`: Если `api_domain` или `api_key` не предоставлены и отсутствуют в `credentials`.

**Как работает функция**:

1.  **Инициализация параметров API**: Функция проверяет, переданы ли `api_domain` и `api_key` напрямую или через аргумент `credentials`. Если передан `credentials`, функция пытается извлечь `api_domain` и `api_key` из него.
2.  **Проверка наличия необходимых параметров**: Функция проверяет, что `api_domain` и `api_key` установлены. Если один из них отсутствует, выбрасывается исключение `ValueError`.
3.  **Инициализация родительского класса**: Функция вызывает конструктор родительского класса `PrestaShop` с переданными `api_domain`, `api_key`, `*args` и `**kwards`.

**Примеры**:

```python
from types import SimpleNamespace

# Инициализация с передачей параметров напрямую
supplier = PrestaSupplier(api_domain='example.com', api_key='test_key')

# Инициализация с использованием объекта SimpleNamespace
credentials = SimpleNamespace(api_domain='example.com', api_key='test_key')
supplier = PrestaSupplier(credentials=credentials)

# Инициализация с использованием словаря
credentials = {'api_domain': 'example.com', 'api_key': 'test_key'}
supplier = PrestaSupplier(credentials=credentials)
```
```
Инициализация класса PrestaSupplier
│
├───> Проверка параметров: credentials, api_domain, api_key
│   │   Если credentials присутствует:
│   │   ├───> Извлечение api_domain и api_key из credentials
│   │   │
│   ├───> Проверка наличия api_domain и api_key
│   │   │   Если api_domain или api_key отсутствуют:
│   │   │   └───> Выброс ValueError
│   │   │
│   └───> Инициализация родительского класса PrestaShop
│
└───> Конец