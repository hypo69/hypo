## Анализ кода `hypotez/src/suppliers/graber.py`

### 1. **<алгоритм>**

**Блок-схема работы `Graber`:**

1.  **Инициализация (`__init__`)**:
    *   Принимает `supplier_prefix` (префикс поставщика, строка) и `driver` (экземпляр класса `Driver`).
    *   Загружает локаторы из JSON-файла `product.json` в `SimpleNamespace` (атрибут `locator`).
        *   Пример: `j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')`
    *   Инициализирует `ProductFields` (атрибут `fields`) для хранения данных о продукте.
    *   Устанавливает `driver` и `supplier_prefix` в контекст (`Context.driver`, `Context.supplier_prefix`).

2.  **Сбор данных со страницы (`grab_page`)**:
    *   Принимает `args` (кортеж с названиями полей) и `kwargs` (словарь с данными для этих полей).
    *   Вызывает внутреннюю функцию `fetch_all_data`.
        *   `fetch_all_data`  итерируется по `args` (названия полей)
            *   Для каждого имени поля получает метод класса с таким именем (например, `name`, `price` и т.д.).
                *   Пример: `getattr(self, filed_name, None)`
            *   Если метод найден, вызывает его, передавая значение из `kwargs` (если есть) или пустую строку.
                *   Пример: `await function(kwards.get(filed_name, ''))`
                *   Внутри метода извлекаются данные с помощью `driver.execute_locator` и записываются в `self.fields`
    *   Возвращает заполненный объект `ProductFields` (атрибут `fields`).

3.  **Обработка поля (пример: `name`)**:
    *   Декорируется `close_pop_up`, который проверяет наличие `Context.locator_for_decorator`.
        *   Если `Context.locator_for_decorator` установлен, вызывается  `driver.execute_locator` для закрытия всплывающего окна перед выполнением кода
    *   Принимает значение `value` (аргумент, переданный через `kwargs`).
        *   Если `value` передано, оно присваивается в соответствующее поле `self.fields`
        *   Если `value` не передано, вызывается  `driver.execute_locator` с `self.locator.name`
    *   Возвращает `True`, если значение успешно установлено.

4. **Универсальная функция установки значения поля (`set_field_value`)**
     *  Принимает `value`, `locator_func`, `field_name`, `default`.
     *  Выполняет `locator_func` в отдельном потоке с помощью `asyncio.to_thread`.
     *  Если `value` передано, возвращает `value`.
     *  Если результат `locator_func` не пустой, возвращает результат.
     *  Иначе вызывает `self.error(field_name)` и возвращает `default`.

5.  **Декоратор `close_pop_up`**:
    *   Принимает `value` (опционально).
    *   Возвращает функцию-декоратор, которая:
        *   Проверяет, установлен ли `Context.locator_for_decorator`.
        *   Если установлен, пытается выполнить `driver.execute_locator` для закрытия всплывающего окна.
        *   Вызывает декорируемую функцию.

**Поток данных:**

```
[JSON-файл локаторов] --> j_loads_ns --> [SimpleNamespace] (self.locator)
[supplier_prefix, driver] --> __init__ --> [Graber]
[names, {name='value'}] --> grab_page  --> fetch_all_data --> [вызовы методов Graber]
    [driver, locator] --> execute_locator --> [данные с вебстраницы] --> [нормализация данных] --> self.fields
-->  [ProductFields]

```

### 2. **<mermaid>**

```mermaid
graph LR
    A[Graber:__init__] --> B(j_loads_ns:load locators);
    B --> C[Context:set driver, supplier_prefix];
    C --> D(ProductFields:create);
    D --> E[Graber:grab_page];
    E --> F(fetch_all_data);
     F --> G{for filed_name in args};
    G --> H{function = getattr(self, filed_name)};
     H -- function exists --> I[function(value)]
     H -- function not exists --> G
    I --> J{close_pop_up decorator}
    J --> K{execute_locator}
    K --> L[normalize_data];
    L --> M(ProductFields:set field)
    M --> G
    G --> N{Return ProductFields}
    N --> O[Graber:grab_page return ProductFields];
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#ccf,stroke:#333,stroke-width:2px
    style G fill:#ccf,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style J fill:#ccf,stroke:#333,stroke-width:2px
     style K fill:#ccf,stroke:#333,stroke-width:2px
    style L fill:#ccf,stroke:#333,stroke-width:2px
    style M fill:#ccf,stroke:#333,stroke-width:2px
    style N fill:#ccf,stroke:#333,stroke-width:2px
    style O fill:#ccf,stroke:#333,stroke-width:2px


```

**Зависимости `mermaid`:**

*   `Graber:__init__`: Инициализирует объект `Graber`, загружает локаторы.
*   `j_loads_ns:load locators`: Загружает локаторы из `JSON` файла.
*  `Context:set driver, supplier_prefix`: Устанавливает контекстные параметры `driver` и `supplier_prefix`.
*   `ProductFields:create`: Инициализирует пустой объект `ProductFields`.
*   `Graber:grab_page`: Запускает процесс сбора данных со страницы.
*   `fetch_all_data`:  Вызывает методы класса для заполнения полей.
*   `for filed_name in args`: Цикл, перебирающий названия полей для извлечения.
*  `function = getattr(self, filed_name)`: Получние метода класса по имени поля.
*  `function(value)`: Вызов метода для сбора данных по конкретному полю.
*   `close_pop_up decorator`: Декоратор для закрытия всплывающих окон (если необходимо).
*   `execute_locator`:  Извлекает данные с вебстраницы используя локатор.
*   `normalize_data`:  Нормализует полученные данные (приводит к нужному типу).
*   `ProductFields:set field`: Устанавливает полученное значение в соответствующее поле объекта `ProductFields`.
*    `Return ProductFields`: Возвращает объект `ProductFields` со всеми собранными данными.
*   `Graber:grab_page return ProductFields`: Возвращает заполненный объект `ProductFields`.

### 3. **<объяснение>**

**Импорты:**

*   `from __future__ import annotations`:  Позволяет использовать аннотации типов, включая ссылки на еще не определенные типы.
*   `datetime`:  Работа с датами и временем.
*   `os`, `sys`:  Взаимодействие с операционной системой и интерпретатором.
*   `asyncio`:  Асинхронное программирование.
*   `pathlib.Path`:  Удобная работа с путями к файлам и директориям.
*   `typing.Optional`, `typing.Any`:  Аннотации типов. `Optional` - может быть `None` или тип, `Any` - любой тип.
*   `types.SimpleNamespace`:  Создание простых объектов для хранения атрибутов.
*    `typing.Callable`:  Тип для вызываемых объектов (функций, методов).
*   `langdetect.detect`:  Определение языка текста.
*   `functools.wraps`:  Декоратор для сохранения метаданных декорируемой функции.
*   `header`:  Импорт модуля `header`, предположительно, содержащего общие заголовки.
*   `src.gs`: Импорт глобальных настроек проекта.
*   `src.product.product_fields.ProductFields`: Класс для хранения полей продукта.
*    `src.category.Category`:  Класс для работы с категориями.
*   `src.utils.jjson`:  Модуль для работы с `JSON` (загрузка, сохранение).
*   `src.utils.image`:  Модуль для работы с изображениями.
*   `src.utils.string.normalizer`:  Модуль для нормализации строк, чисел, логических значений и дат.
*   `src.logger.exceptions.ExecuteLocatorException`: Исключение, возникающее при ошибке выполнения локатора.
*   `src.utils.printer.pprint`: Функция для "красивого" вывода в лог.
*   `src.logger.logger`: Модуль для логирования.

**Классы:**

*   **`Context`**:
    *   Предназначен для хранения глобальных настроек, таких как `driver`, `locator` и `supplier_prefix`.
    *   Используется для доступа к общим ресурсам из разных частей кода.
    *   Имеет статические атрибуты, которые можно изменять.

*   **`Graber`**:
    *   Базовый класс для сбора данных со страниц поставщиков.
    *   **`__init__`**: Инициализирует объект `Graber`, загружает локаторы, создает объект `ProductFields`, устанавливает `driver` и `supplier_prefix` в контекст.
    *   **`error`**: Обработчик ошибок для полей, записывает сообщение в лог.
    *   **`set_field_value`**: Универсальная функция для установки значения поля.
    *   **`grab_page`**: Основная асинхронная функция для сбора данных. Вызывает методы класса для каждого поля, используя `args` и `kwargs`.
    *   Остальные методы (напр. `name`, `price`, `description` и т.д.):  Методы для извлечения конкретных полей со страницы, используя локаторы и `driver`. Все методы декорируются `@close_pop_up`. Принимают `value` как аргумент, переданный через `kwargs`.

**Функции:**

*   **`close_pop_up`**:
    *   Декоратор для закрытия всплывающих окон перед выполнением основной функции.
    *   Применяется ко всем методам класса `Graber`.
    *   Использует `Context.locator_for_decorator` для определения локатора закрытия всплывающего окна.

**Переменные:**

*   `MODE`: Глобальная переменная режима работы (`dev`).
*   `Context.driver`: Экземпляр класса `Driver`.
*   `Context.locator_for_decorator`:  Локатор для закрытия всплывающих окон.
*    `Context.supplier_prefix`: Префикс поставщика.
*   `self.supplier_prefix`: Префикс поставщика для конкретного экземпляра `Graber`.
*   `self.locator`: `SimpleNamespace` с локаторами для текущего поставщика.
*   `self.driver`:  Экземпляр класса `Driver` для текущего поставщика.
*   `self.fields`:  Объект `ProductFields` для хранения собранных данных о продукте.

**Потенциальные ошибки и области для улучшения:**

*   **Жесткая привязка путей**:  Пути к файлам локаторов и временным изображениям (`gs.path.tmp`) жестко заданы. Следует рассмотреть возможность использовать относительные пути или конфигурационные файлы.
*   **Обработка исключений**:  В методах сбора данных (например, `name`, `price`) используются общие блоки `except Exception as ex`, но не все исключения обрабатываются корректно. Стоит сделать более детальную обработку исключений и предусмотреть разные типы ошибок.
*   **Динамическое получение методов:** `grab_page`  получает методы по имени из args, что делает код гибким, но может усложнить отладку.
*   **`local_saved_image`**: Имеет недоработанную логику передачи параметров.
*   **Множество однотипных методов**: Методы для каждого поля (например, `name`, `price`, `description` и т.д.) имеют много повторяющегося кода. Стоит рассмотреть возможность рефакторинга для сокращения дублирования кода.
*   **`Context.locator_for_decorator`**: Использование статического атрибута для хранения локатора для декоратора может привести к проблемам при конкурентном использовании класса `Graber` в многопоточной среде.
*   **Непоследовательная логика обработки `value`**:  Иногда `value` проверяется в начале функции, иногда в конце.
*   **Не всегда явное логирование**: Некоторые методы не имеют подробного логирования ошибок, что затрудняет отладку.
* **`await self.id_product()`**: Не очевидно как этот метод будет выполнен, если он вызывается в `self.local_saved_image`.

**Взаимосвязи с другими частями проекта:**

*   **`src.webdriver.driver.Driver`**:  Используется для управления браузером и выполнения локаторов.  Класс `Graber` сильно зависит от `Driver`.
*   **`src.product.product_fields.ProductFields`**:  Используется для хранения данных о продукте.
*   **`src.utils.jjson`**:  Используется для загрузки локаторов из `JSON` файлов.
*   **`src.utils.image`**:  Используется для сохранения изображений.
*   **`src.utils.string.normalizer`**:  Используется для нормализации данных, полученных со страницы.
*   **`src.logger.logger`**:  Используется для логирования ошибок и отладочной информации.
*   **`src.gs`**:  Используется для доступа к глобальным настройкам проекта.
*   **`src.suppliers`**:  Класс `Graber` является частью пакета поставщиков, для каждого поставщика создаётся свой класс на основе Graber.

**Дополнительные комментарии:**

*   Код представляет собой базовый класс для сбора данных с веб-страниц поставщиков.
*   Используется асинхронное программирование для параллельного сбора данных.
*   Локаторы хранятся в отдельных файлах `JSON`, что обеспечивает гибкость и возможность настройки для разных поставщиков.
*   Для расширения функциональности конкретного поставщика нужно создать класс-наследник от `Graber` и переопределить в нем необходимые методы.
*   Код требует рефакторинга для уменьшения дублирования кода и улучшения обработки ошибок.