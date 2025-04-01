# Модуль для сбора данных о товарах с AliExpress

## Обзор

Модуль `src.suppliers.aliexpress.graber` предназначен для сбора данных о товарах с веб-сайта AliExpress. Он содержит класс `Graber`, который наследуется от базового класса `src.suppliers.graber.Graber` и предоставляет методы для обработки различных полей товара на странице.

## Подробнее

Модуль предоставляет функциональность для сбора информации о товарах с AliExpress, позволяя переопределять методы обработки полей товара для нестандартных случаев. Также поддерживается выполнение предварительных действий перед запросом к веб-драйверу с использованием декораторов.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с AliExpress.

**Наследует**:
- `src.suppliers.graber.Graber`: Базовый класс для сбора данных о товарах с различных платформ.

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, в данном случае всегда `'aliexpress'`.

**Методы**:
- `__init__(driver: Driver, lang_index: int)`: Инициализирует экземпляр класса `Graber`.

### `__init__`

```python
 def __init__(self, driver: Driver, lang_index:int):
        """
        Инициализация класса сбора полей товара.

        :param driver: Экземпляр веб-драйвера для взаимодействия с браузером.
        :type driver: Driver
        """
        self.supplier_prefix = 'aliexpress'
        # вызов конструктора родительского класса
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

        # устанавливает значение локатора для декоратора в `None`
        # если будет установленно значение - то оно выполнится в декораторе `@close_pop_up`
        Context.locator_for_decorator = None
```

**Назначение**: Инициализация экземпляра класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с браузером.
- `lang_index` (int): Индекс языка.

**Как работает функция**:
1. Устанавливает атрибут `supplier_prefix` равным `'aliexpress'`.
2. Вызывает конструктор родительского класса `Graber` из модуля `src.suppliers.graber`, передавая `supplier_prefix`, `driver` и `lang_index`.
3. Устанавливает атрибут `Context.locator_for_decorator` в `None`. Это необходимо для того, чтобы декоратор `@close_pop_up` не выполнялся по умолчанию, если не установлено иное значение локатора.

```
Инициализация Graber
│
├── Установка supplier_prefix = 'aliexpress'
│
├── Вызов конструктора родительского класса (Graber из src.suppliers.graber)
│   │
│   └── Передача supplier_prefix, driver и lang_index
│
└── Установка Context.locator_for_decorator = None
```

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
from src.suppliers.aliexpress.graber import Graber

# Создание инстанса драйвера (пример с Chrome)
driver = Driver(Chrome)

# Создание инстанса класса Graber
graber = Graber(driver=driver, lang_index=0)