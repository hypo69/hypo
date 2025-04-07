# Модуль грабера

## Обзор

Модуль `graber.py` предназначен для сбора информации о товарах с веб-страниц поставщиков. Он содержит базовый класс `Graber`, который использует веб-драйвер для извлечения данных, таких как название, описание, характеристики, артикул и цена товара. Локаторы для определения местоположения полей хранятся в JSON-файлах в директории `locators` каждого поставщика.

## Подробней

Этот модуль предоставляет основу для создания специализированных граберов для различных поставщиков. Для нестандартной обработки полей товара рекомендуется переопределять функции в классах-наследниках `Graber`.

## Классы

### `Context`

**Описание**:
Класс `Context` предназначен для хранения глобальных настроек, используемых в процессе сбора данных.

**Атрибуты**:
- `driver` (Optional['Driver']): Объект драйвера, используемый для управления браузером или другим интерфейсом.
- `locator_for_decorator` (Optional[SimpleNamespace]): Локатор для декоратора `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`.
- `supplier_prefix` (Optional[str]): Префикс поставщика.

**Принцип работы**:
Класс `Context` используется для централизованного хранения и доступа к глобальным настройкам, таким как драйвер веб-браузера, локаторы для всплывающих окон и префикс поставщика. Это позволяет избежать передачи этих параметров в каждую функцию и упрощает управление конфигурацией грабера.

### `Graber`

**Описание**:
Базовый класс `Graber` предназначен для сбора данных о товарах с веб-страниц поставщиков.

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика.
- `locator` (SimpleNamespace): Объект, содержащий локаторы элементов страницы, загруженные из JSON.
- `driver` ('Driver'): Экземпляр класса `Driver` для управления браузером.
- `fields` (ProductFields): Объект для хранения собранных данных о товаре.

**Принцип работы**:
Класс `Graber` инициализируется с префиксом поставщика, загружает локаторы элементов страницы из JSON, создает экземпляр драйвера и объект для хранения данных о товаре. Он предоставляет методы для извлечения и нормализации данных с веб-страниц, а также для обработки ошибок.

**Методы**:
- `__init__(supplier_prefix: str, lang_index: int, driver: 'Driver')`: Инициализация класса `Graber`.
- `error(field: str)`: Обработчик ошибок для полей.
- `set_field_value(value: Any, locator_func: Callable[[], Any], field_name: str, default: Any = '')`: Универсальная функция для установки значений полей с обработкой ошибок.
- `grab_page(*args, **kwards)`: Запускает асинхронный сбор полей продукта.
- `grab_page_async(*args, **kwards)`: Асинхронная функция для сбора полей продукта.

## Функции

### `close_pop_up`

```python
def close_pop_up() -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.
    ...
    """
```

**Назначение**:
Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
- `value` ('Driver'): Дополнительное значение для декоратора.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

**Как работает функция**:
1. Определяет декоратор `decorator`, который принимает функцию `func` в качестве аргумента.
2. Внутри `decorator` определяется асинхронная функция `wrapper`, которая будет заменять оригинальную функцию `func`.
3. В `wrapper` проверяется, установлен ли `Context.locator_for_decorator`. Если да, то пытается выполнить локатор для закрытия всплывающего окна с помощью `Context.driver.execute_locator()`.
4. После выполнения локатора (или при возникновении ошибки) `Context.locator_for_decorator` устанавливается в `None`, чтобы декоратор не срабатывал повторно.
5. Вызывает оригинальную функцию `func` с переданными аргументами и возвращает результат её выполнения.
6. Возвращает `wrapper` как результат работы декоратора.

**ASCII flowchart**:

```
A: Проверка Context.locator_for_decorator
|
-- B: Выполнение локатора для закрытия всплывающего окна
|
C: Вызов оригинальной функции func
|
D: Возврат результата выполнения func
```

**Примеры**:

```python
@close_pop_up()
async def my_function():
    # some code here
    pass
```

### `Graber.__init__`

```python
def __init__(self, supplier_prefix: str, lang_index:int, driver: 'Driver'):
    """Инициализация класса Graber.

    Args:
        supplier_prefix (str): Префикс поставщика.
        driver ('Driver'): Экземпляр класса Driver.
    """
    ...
```

**Назначение**:
Инициализирует экземпляр класса `Graber`.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика.
- `lang_index` (int): Индекс языка.
- `driver` ('Driver'): Экземпляр класса `Driver` для управления браузером.

**Как работает функция**:
1. Сохраняет префикс поставщика в атрибуте `supplier_prefix`.
2. Загружает локаторы элементов страницы из JSON-файла, расположенного в директории `locators` поставщика, и сохраняет их в атрибуте `locator`.
3. Инициализирует экземпляр `ProductFields` с указанным `lang_index` и сохраняет его в атрибуте `fields`.
4. Устанавливает глобальные настройки `Context.driver`, `Context.supplier_prefix` и `Context.locator_for_decorator`.

**ASCII flowchart**:

```
A: Сохранение supplier_prefix
|
B: Загрузка локаторов из JSON
|
C: Инициализация ProductFields
|
D: Установка глобальных настроек Context
```

### `Graber.error`

```python
async def error(self, field: str):
    """Обработчик ошибок для полей."""
    ...
```

**Назначение**:
Обрабатывает ошибки, возникающие при заполнении полей.

**Параметры**:
- `field` (str): Название поля, для которого произошла ошибка.

**Как работает функция**:
1. Логирует отладочное сообщение с информацией о поле, в котором произошла ошибка.

**ASCII flowchart**:

```
A: Логирование отладочного сообщения
```

### `Graber.set_field_value`

```python
async def set_field_value(
    self,
    value: Any,
    locator_func: Callable[[], Any],
    field_name: str,
    default: Any = ''
) -> Any:
    """Универсальная функция для установки значений полей с обработкой ошибок."""
    ...
```

**Назначение**:
Устанавливает значение поля, используя предоставленную функцию локатора, и обрабатывает возможные ошибки.

**Параметры**:
- `value` (Any): Значение для установки.
- `locator_func` (Callable[[], Any]): Функция для получения значения из локатора.
- `field_name` (str): Название поля.
- `default` (Any): Значение по умолчанию.

**Возвращает**:
- `Any`: Установленное значение.

**Как работает функция**:
1. Асинхронно выполняет функцию локатора `locator_func` для получения значения.
2. Если передано значение `value`, возвращает его.
3. Если функция локатора вернула значение `locator_result`, возвращает его.
4. Если ни `value`, ни `locator_result` не заданы, вызывает метод `error` для логирования ошибки и возвращает значение по умолчанию `default`.

**ASCII flowchart**:

```
A: Выполнение locator_func
|
-- B: Проверка value
|  |
|  C: Возврат value
|
-- D: Проверка locator_result
|  |
|  E: Возврат locator_result
|
-- F: Вызов error(field_name)
|
G: Возврат default
```

### `Graber.grab_page`

```python
def grab_page(self, *args, **kwards) -> ProductFields:
    return asyncio.run(self.grab_page_async(*args, **kwards))
```

**Назначение**:
Запускает асинхронную функцию для сбора полей продукта.

**Параметры**:
- `*args`: Аргументы, передаваемые в `grab_page_async`.
- `**kwards`: Ключевые аргументы, передаваемые в `grab_page_async`.

**Возвращает**:
- `ProductFields`: Объект `ProductFields` с собранными данными.

**Как работает функция**:
1. Запускает асинхронную функцию `grab_page_async` и возвращает результат ее выполнения.

**ASCII flowchart**:

```
A: Запуск grab_page_async
|
B: Возврат результата выполнения grab_page_async
```

### `Graber.grab_page_async`

```python
async def grab_page_async(self, *args, **kwards) -> ProductFields:
    """Асинхронная функция для сбора полей продукта."""
    ...
```

**Назначение**:
Асинхронно собирает поля продукта, вызывая соответствующие методы класса для каждого поля.

**Параметры**:
- `*args`: Список названий полей, которые необходимо собрать.
- `**kwards`: Словарь с дополнительными параметрами для каждого поля.

**Возвращает**:
- `ProductFields`: Объект `ProductFields` с собранными данными.

**Внутренние функции**:
- `fetch_all_data(*args, **kwards)`: Динамически вызывает функции для каждого поля из `args`.

**Как работает функция**:
1. Определяет асинхронную внутреннюю функцию `fetch_all_data`, которая выполняет динамический вызов методов для каждого поля, указанного в `args`.
2. Для каждого имени поля в `args` функция пытается получить соответствующий метод из класса `self`.
3. Если метод существует, он вызывается с использованием `await` и передачей дополнительных параметров из `kwards`.
4. После вызова всех методов возвращает объект `self.fields`, содержащий собранные данные.

**ASCII flowchart**:

```
A: Определение fetch_all_data
|
-- B: Для каждого filed_name в args
|  |
|  C: Получение функции из self
|  |
|  D: Если функция существует
|  |  |
|  |  E: Вызов функции с await
|
F: Возврат self.fields
```

### `Graber.additional_shipping_cost`

```python
@close_pop_up()
async def additional_shipping_cost(self, value:Optional[Any] = None):
    """Fetch and set additional shipping cost."""
    ...
```

**Назначение**:
Извлекает и устанавливает стоимость дополнительной доставки.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `additional_shipping_cost`. Если `value` передано, оно будет установлено в поле `ProductFields.additional_shipping_cost`.

**Как работает функция**:
1. Пытается получить значение стоимости дополнительной доставки из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.additional_shipping_cost)`.
2. Нормализует полученное значение с помощью `normalize_string`.
3. Если значение не получено, логирует ошибку и возвращает `None`.
4. В случае возникновения исключения логирует ошибку и возвращает `None`.
5. Записывает полученное значение в поле `self.fields.additional_shipping_cost`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Нормализация значения
|  |
|  C: Если значение не получено -> Логирование ошибки
|
D: Запись значения в self.fields.additional_shipping_cost
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.additional_shipping_cost()

# Вызов функции с передачей значения
await grabber.additional_shipping_cost(value='10.00')
```

### `Graber.delivery_in_stock`

```python
@close_pop_up()
async def delivery_in_stock(self, value:Optional[Any] = None):
    """Fetch and set delivery in stock status."""
    ...
```

**Назначение**:
Извлекает и устанавливает статус доставки в наличии.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `delivery_in_stock`. Если `value` передано, оно будет установлено в поле `ProductFields.delivery_in_stock`.

**Как работает функция**:
1. Пытается получить значение статуса доставки из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.delivery_in_stock)`.
2. Нормализует полученное значение с помощью `normalize_string`.
3. Если значение не получено, логирует ошибку и возвращает `None`.
4. В случае возникновения исключения логирует ошибку и возвращает `None`.
5. Записывает полученное значение в поле `self.fields.delivery_in_stock`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Нормализация значения
|  |
|  C: Если значение не получено -> Логирование ошибки
|
D: Запись значения в self.fields.delivery_in_stock
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.delivery_in_stock()

# Вызов функции с передачей значения
await grabber.delivery_in_stock(value='В наличии')
```

### `Graber.active`

```python
@close_pop_up()
async def active(self, value:Optional[Any] = None):
    """Fetch and set active status."""
    ...
```

**Назначение**:
Извлекает и устанавливает статус активности товара.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `active`. Если `value` передано, оно будет установлено в поле `ProductFields.active`. Принимает значения 1/0.

**Как работает функция**:
1. Пытается получить значение статуса активности из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.active)`.
2. Нормализует полученное значение с помощью `normalize_int`.
3. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
4. В случае возникновения исключения логирует ошибку и возвращает `None`.
5. Если значение `value` невалидно, логирует отладочное сообщение и возвращает `None`.
6. Записывает полученное значение в поле `self.fields.active`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Нормализация значения
|  |
|  C: Если значение не получено -> Логирование отладочного сообщения
|
D: Проверка валидности value
|
-- E: Запись значения в self.fields.active
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.active()

# Вызов функции с передачей значения
await grabber.active(value=1)
```

### `Graber.additional_delivery_times`

```python
@close_pop_up()
async def additional_delivery_times(self, value:Optional[Any] = None):
    """Fetch and set additional delivery times."""
    ...
```

**Назначение**:
Извлекает и устанавливает дополнительное время доставки.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `additional_delivery_times`. Если `value` передано, оно будет установлено в поле `ProductFields.additional_delivery_times`.

**Как работает функция**:
1. Пытается получить значение времени доставки из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.additional_delivery_times)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.additional_delivery_times`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.additional_delivery_times
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.additional_delivery_times()

# Вызов функции с передачей значения
await grabber.additional_delivery_times(value='3-5 дней')
```

### `Graber.advanced_stock_management`

```python
@close_pop_up()
async def advanced_stock_management(self, value:Optional[Any] = None):
    """Fetch and set advanced stock management status."""
    ...
```

**Назначение**:
Извлекает и устанавливает статус расширенного управления запасами.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `advanced_stock_management`. Если `value` передано, оно будет установлено в поле `ProductFields.advanced_stock_management`.

**Как работает функция**:
1. Пытается получить значение статуса управления запасами из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.advanced_stock_management)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.advanced_stock_management`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.advanced_stock_management
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.advanced_stock_management()

# Вызов функции с передачей значения
await grabber.advanced_stock_management(value='1')
```

### `Graber.affiliate_short_link`

```python
@close_pop_up()
async def affiliate_short_link(self, value:Optional[Any] = None):
    """Fetch and set affiliate short link."""
    ...
```

**Назначение**:
Извлекает и устанавливает короткую партнерскую ссылку.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `affiliate_short_link`. Если `value` передано, оно будет установлено в поле `ProductFields.affiliate_short_link`.

**Как работает функция**:
1. Пытается получить значение короткой партнерской ссылки из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.affiliate_short_link)`.
2. В случае возникновения исключения логирует ошибку и возвращает `None`.
3. Записывает полученное значение в поле `self.fields.affiliate_short_link`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
B: Запись значения в self.fields.affiliate_short_link
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.affiliate_short_link()

# Вызов функции с передачей значения
await grabber.affiliate_short_link(value='https://short.link')
```

### `Graber.affiliate_summary`

```python
@close_pop_up()
async def affiliate_summary(self, value:Optional[Any] = None):
    """Fetch and set affiliate summary."""
    ...
```

**Назначение**:
Извлекает и устанавливает партнерское описание.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `affiliate_summary`. Если `value` передано, оно будет установлено в поле `ProductFields.affiliate_summary`.

**Как работает функция**:
1. Пытается получить значение партнерского описания из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.affiliate_summary)`.
2. Нормализует полученное значение с помощью `normalize_string`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.affiliate_summary`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Нормализация значения
|
C: Запись значения в self.fields.affiliate_summary
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.affiliate_summary()

# Вызов функции с передачей значения
await grabber.affiliate_summary(value='Краткое описание партнерской программы')
```

### `Graber.affiliate_summary_2`

```python
@close_pop_up()
async def affiliate_summary_2(self, value:Optional[Any] = None):
    """Fetch and set affiliate summary 2."""
    ...
```

**Назначение**:
Извлекает и устанавливает второе партнерское описание.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `affiliate_summary_2`. Если `value` передано, оно будет установлено в поле `ProductFields.affiliate_summary_2`.

**Как работает функция**:
1. Пытается получить значение второго партнерского описания из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.affiliate_summary_2)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.affiliate_summary_2`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.affiliate_summary_2
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.affiliate_summary_2()

# Вызов функции с передачей значения
await grabber.affiliate_summary_2(value='Более подробное описание партнерской программы')
```

### `Graber.affiliate_text`

```python
@close_pop_up()
async def affiliate_text(self, value:Optional[Any] = None):
    """Fetch and set affiliate text."""
    ...
```

**Назначение**:
Извлекает и устанавливает партнерский текст.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `affiliate_text`. Если `value` передано, оно будет установлено в поле `ProductFields.affiliate_text`.

**Как работает функция**:
1. Пытается получить значение партнерского текста из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.affiliate_text)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.affiliate_text`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.affiliate_text
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.affiliate_text()

# Вызов функции с передачей значения
await grabber.affiliate_text(value='Текст партнерской программы')
```

### `Graber.affiliate_image_large`

```python
@close_pop_up()
async def affiliate_image_large(self, value:Optional[Any] = None):
    """Fetch and set affiliate large image."""
    ...
```

**Назначение**:
Извлекает и устанавливает большую партнерскую картинку.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `affiliate_image_large`. Если `value` передано, оно будет установлено в поле `ProductFields.affiliate_image_large`.

**Как работает функция**:
1. Пытается получить значение большой партнерской картинки из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.affiliate_image_large)`.
2. В случае возникновения исключения логирует ошибку и возвращает `None`.
3. Записывает полученное значение в поле `self.fields.affiliate_image_large`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
B: Запись значения в self.fields.affiliate_image_large
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.affiliate_image_large()

# Вызов функции с передачей значения
await grabber.affiliate_image_large(value='https://example.com/large.jpg')
```

### `Graber.affiliate_image_medium`

```python
@close_pop_up()
async def affiliate_image_medium(self, value:Optional[Any] = None):
    """Fetch and set affiliate medium image."""
    ...
```

**Назначение**:
Извлекает и устанавливает среднюю партнерскую картинку.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `affiliate_image_medium`. Если `value` передано, оно будет установлено в поле `ProductFields.affiliate_image_medium`.

**Как работает функция**:
1. Пытается получить значение средней партнерской картинки из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.affiliate_image_medium)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.affiliate_image_medium`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.affiliate_image_medium
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.affiliate_image_medium()

# Вызов функции с передачей значения
await grabber.affiliate_image_medium(value='https://example.com/medium.jpg')
```

### `Graber.affiliate_image_small`

```python
@close_pop_up()
async def affiliate_image_small(self, value:Optional[Any] = None):
    """Fetch and set affiliate small image."""
    ...
```

**Назначение**:
Извлекает и устанавливает маленькую партнерскую картинку.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `affiliate_image_small`. Если `value` передано, оно будет установлено в поле `ProductFields.affiliate_image_small`.

**Как работает функция**:
1. Пытается получить значение маленькой партнерской картинки из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.affiliate_image_small)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.affiliate_image_small`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.affiliate_image_small
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.affiliate_image_small()

# Вызов функции с передачей значения
await grabber.affiliate_image_small(value='https://example.com/small.jpg')
```

### `Graber.available_date`

```python
@close_pop_up()
async def available_date(self, value:Optional[Any] = None):
    """Fetch and set available date."""
    ...
```

**Назначение**:
Извлекает и устанавливает дату доступности товара.

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `available_date`. Если `value` передано, оно будет установлено в поле `ProductFields.available_date`.

**Как работает функция**:
1. Пытается получить значение даты доступности товара из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.available_date)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.available_date`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.available_date
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.available_date()

# Вызов функции с передачей значения
await grabber.available_date(value='2024-12-31')
```

### `Graber.available_for_order`

```python
@close_pop_up()
async def available_for_order(self, value:Optional[Any] = None):
    """Fetch and set available for order status."""
    ...
```

**Назначение**:
Извлекает и устанавливает статус "доступно для заказа".

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `available_for_order`. Если `value` передано, оно будет установлено в поле `ProductFields.available_for_order`.

**Как работает функция**:
1. Пытается получить значение статуса "доступно для заказа" из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_locator(self.locator.available_for_order)`.
2. Если значение не получено, логирует отладочное сообщение и возвращает `None`.
3. В случае возникновения исключения логирует ошибку и возвращает `None`.
4. Записывает полученное значение в поле `self.fields.available_for_order`.

**ASCII flowchart**:

```
A: Получение значения из value или локатора
|
-- B: Если значение не получено -> Логирование отладочного сообщения
|
D: Запись значения в self.fields.available_for_order
```

**Примеры**:

```python
# Вызов функции без передачи значения
await grabber.available_for_order()

# Вызов функции с передачей значения
await grabber.available_for_order(value='1')
```

### `Graber.available_later`

```python
@close_pop_up()
async def available_later(self, value:Optional[Any] = None):
    """Fetch and set available later status."""
    ...
```

**Назначение**:
Извлекает и устанавливает статус "доступно позже".

**Параметры**:
- `value` (Optional[Any]): Значение, которое можно передать в словаре `kwargs` через ключ `available_later`. Если `value` передано, оно будет установлено в поле `ProductFields.available_later`.

**Как работает функция**:
1. Пытается получить значение статуса "доступно позже" из следующих источников:
   - Если передано значение `value`, использует его.
   - Если `value` не передано, пытается получить значение с помощью `self.driver.execute_