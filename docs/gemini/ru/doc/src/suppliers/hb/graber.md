# Модуль hypotez/src/suppliers/hb/graber.py

## Обзор

Модуль `graber.py` содержит класс `Graber`, предназначенный для сбора данных с сайта `hb.co.il`. Класс наследуется от родительского класса `Graber` и предоставляет методы для обработки полей страницы товара.  Для нестандартных операций обработки полей, можно переопределить методы в этом классе.  Возможно использование декоратора `close_pop_up` для выполнения предварительных действий перед запросом к веб-драйверу.  Для работы декоратора, необходимо установить значение в `Context.locator`.

## Классы

### `Graber`

**Описание**: Класс `Graber` расширяет функционал родительского класса для сбора данных с сайта `hb.co.il`.

**Атрибуты**:

- `supplier_prefix: str`: Префикс поставщика данных.

**Методы**:

- `__init__(self, driver: Driver)`: Инициализирует экземпляр класса.
    - **Параметры**:
        - `driver (Driver)`: Экземпляр класса `Driver` для управления веб-драйвером.
    - **Описание**: Устанавливает `supplier_prefix` и вызывает конструктор родительского класса. Также устанавливает значение `Context.locator_for_decorator`.


## Функции

### `close_pop_up` (комментирована)

**Описание**: Декоратор для закрытия всплывающих окон перед выполнением функции. (Не используется в текущем коде)

**Параметры**:
- `value (Any, optional)`: Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

**Вызывает исключения**:
- `ExecuteLocatorException`: Ошибка выполнения локатора.


## Глобальные переменные

### `MODE`

**Описание**: Глобальная переменная, хранящая режим работы.

**Значение**: `'dev'`