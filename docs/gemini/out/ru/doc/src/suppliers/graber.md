# Модуль `hypotez/src/suppliers/graber.py`

## Обзор

Данный модуль предоставляет базовый класс `Graber` для сбора данных о продуктах с веб-страниц поставщиков.  Класс использует веб-драйвер (класс `Driver`) для извлечения данных по заданным локаторам, хранящимся в файлах JSON в подкаталоге `locators`.  Локаторы определяют местоположение полей на странице. Подробная информация о формате локаторов доступна в файле `locators.ru.md`.

## Обработка исключений

В модуле используется декоратор `@close_pop_up` для обработки потенциальных исключений при взаимодействии с веб-драйвером. Этот декоратор выполняет попытку закрыть всплывающие окна до выполнения основной логики функции.

## Декоратор `@close_pop_up`

### `close_pop_up(value: 'Driver' = None) -> Callable`

**Описание**:  Декоратор `@close_pop_up` создает обертку для функций,  позволяющую  выполнить попытку закрытия всплывающих окон с помощью метода `execute_locator` веб-драйвера до выполнения основной логики функции.

**Параметры**:

- `value ('Driver')`:  Дополнитеьное значение. Используется, например, при передаче экземпляра веб-драйвера.
- `func (Callable)`: Функция, которую нужно обернуть декоратором.


**Возвращает**:

- `Callable`: Декоратор для функции.

**Возможные исключения**:

- `ExecuteLocatorException`: Если возникла ошибка при выполнении локатора.


## Классы

### `Graber`

**Описание**: Базовый класс для сбора данных о продуктах с веб-страниц поставщиков.

**Методы**:

- `__init__(self, supplier_prefix: str, driver: 'Driver')`: Инициализирует класс `Graber`. Устанавливает префикс поставщика, экземпляр веб-драйвера (`Driver`), локатор (`locator`), и обьект `ProductFields`. Заполняет атрибут `Context.driver` и `Context.supplier_prefix` глобальными переменными.
- `error(self, field: str)`: Обработчик ошибок для полей. Выводит сообщение об ошибке в лог.
- `set_field_value(self, value: Any, locator_func: Callable[[], Any], field_name: str, default: Any = '')`: Универсальная функция для установки значений полей. Получает значение по локатору, обрабатывает потенциальные ошибки.
- `grab_page(self, *args, **kwards) -> ProductFields`: Асинхронная функция для сбора полей продукта. Принимает имена полей, и аргументы `kwards` для каждого поля. Возвращает объект `ProductFields` со значениями полей.
- `additional_shipping_cost(self, value: Optional[Any] = None)`:  Сбор дополнительных расходов на доставку.
- `delivery_in_stock(self, value: Optional[Any] = None)`: Сбор статуса наличия товара на складе.
- `active(self, value: Optional[Any] = None)`: Сбор статуса активности товара.
- `additional_delivery_times(self, value: Optional[Any] = None)`:  Сбор дополнительных временных параметров доставки.
- ... (много методов, подобных перечисленным выше, для сбора различных полей товара)



## Глобальные настройки

### `Context`

**Описание**: Класс для хранения глобальных настроек.

**Атрибуты**:

- `driver`: Экземпляр веб-драйвера.
- `locator`: Пространство имен для хранения локаторов (SimpleNamespace).
- `supplier_prefix`: Префикс поставщика.


```