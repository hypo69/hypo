# Модуль `executor` для Playwright

## Обзор

Модуль `executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Playwright на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации взаимодействия с веб-страницами через Playwright. Он позволяет выполнять различные действия с веб-элементами, такие как клики, ввод текста, получение атрибутов и создание скриншотов.

## Классы

### `PlaywrightExecutor`

**Описание**:
Класс `PlaywrightExecutor` предназначен для выполнения команд на основе локаторов в стиле executor с использованием Playwright.

**Принцип работы**:
Класс инициализирует драйвер Playwright, запускает браузер и предоставляет методы для выполнения различных действий с веб-элементами на странице.

**Атрибуты**:
- `driver` (Optional[`playwright.async_api`]): Драйвер Playwright.
- `browser_type` (str): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
- `page` (Optional[`playwright.async_api.Page`]): Объект страницы Playwright.
- `config` (SimpleNamespace): Конфигурация Playwright, загруженная из файла `playwrid.json`.

**Методы**:

- `__init__(self, browser_type: str = 'chromium', **kwargs)`
- `start(self) -> None`
- `stop(self) -> None`
- `execute_locator(self, locator: Union[dict, SimpleNamespace], message: Optional[str] = None, typing_speed: float = 0, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = 'presence_of_element_located') -> Union[str, list, dict, Locator, bool, None]`
- `evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`
- `get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]`
- `get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]`
- `get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]`
- `execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]`
- `send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool`
- `goto(self, url: str) -> None`

## Функции

### `__init__(self, browser_type: str = 'chromium', **kwargs)`

**Назначение**:
Инициализирует экземпляр класса `PlaywrightExecutor`.

**Параметры**:
- `browser_type` (str): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
- `**kwargs`: Дополнительные параметры.

**Как работает функция**:
1. Устанавливает значения атрибутов экземпляра класса, такие как `driver`, `browser_type`, `page` и `config`.
2. Загружает конфигурацию Playwright из файла `playwrid.json` с использованием функции `j_loads_ns`.

```
Инициализация экземпляра класса PlaywrightExecutor
│
├─── Установка типа браузера (browser_type)
│
├─── Загрузка конфигурации из playwrid.json (config)
│
└─── Конец
```

### `start(self) -> None`

**Назначение**:
Инициализирует Playwright и запускает экземпляр браузера.

**Как работает функция**:
1. Запускает драйвер Playwright с использованием `async_playwright().start()`.
2. Запускает браузер указанного типа (например, Chromium, Firefox, WebKit) в режиме headless (без графического интерфейса) с использованием параметров из конфигурации.
3. Создает новую страницу в браузере.
4. Обрабатывает исключения, которые могут возникнуть при запуске браузера, и логирует их с использованием `logger.critical`.

```
Запуск Playwright
│
├─── Запуск драйвера Playwright (self.driver)
│
├─── Запуск браузера (browser)
│   ├─── Получение типа браузера из атрибута (self.browser_type)
│   ├─── Запуск браузера в режиме headless с параметрами из конфигурации
│   └─── Создание новой страницы (self.page)
│
└─── Обработка исключений и логирование ошибок
```

### `stop(self) -> None`

**Назначение**:
Закрывает браузер Playwright и останавливает его экземпляр.

**Как работает функция**:
1. Закрывает текущую страницу, если она существует.
2. Останавливает драйвер Playwright, если он существует.
3. Устанавливает значение атрибута `driver` в `None`.
4. Логирует информацию об остановке Playwright с использованием `logger.info`.
5. Обрабатывает исключения, которые могут возникнуть при закрытии браузера, и логирует их с использованием `logger.error`.

```
Остановка Playwright
│
├─── Закрытие текущей страницы (self.page)
│
├─── Остановка драйвера Playwright (self.driver)
│
├─── Установка driver в None
│
├─── Логирование информации об остановке
│
└─── Обработка исключений и логирование ошибок
```

### `execute_locator(self, locator: Union[dict, SimpleNamespace], message: Optional[str] = None, typing_speed: float = 0, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = 'presence_of_element_located') -> Union[str, list, dict, Locator, bool, None]`

**Назначение**:
Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (Union[dict, SimpleNamespace]): Данные локатора (словарь или SimpleNamespace).
- `message` (Optional[str]): Необязательное сообщение для событий.
- `typing_speed` (float): Необязательная скорость ввода текста для событий.
- `timeout` (Optional[float]): Тайм-аут для поиска элемента (в секундах).
- `timeout_for_event` (Optional[str]): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located').

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, локатором, логическим значением или None.

**Как работает функция**:
1. Преобразует локатор в SimpleNamespace, если он представлен в виде словаря.
2. Проверяет, что локатор содержит атрибут и селектор. Если нет, возвращает `None`.
3. Определяет внутреннюю асинхронную функцию `_parse_locator`, которая выполняет разбор и выполнение инструкций локатора.
4. Вызывает функцию `_parse_locator` и возвращает результат ее выполнения.

**Внутренние функции**:

#### `_parse_locator(locator: SimpleNamespace, message: Optional[str]) -> Union[str, list, dict, Locator, bool, None]`

**Назначение**:
Разбирает и выполняет инструкции локатора.

**Параметры**:
- `locator` (SimpleNamespace): Данные локатора.
- `message` (Optional[str]): Необязательное сообщение для событий.

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, локатором, логическим значением или None.

**Как работает функция**:
1. Проверяет наличие атрибута `mandatory` у локатора. Если атрибуты `event` и `attribute` присутствуют, но `mandatory` отсутствует, функция возвращает `None`.
2. Проверяет типы атрибутов `locator.attribute` и `locator.by`. Если они являются строками, выполняет следующие действия:
   - Пытается получить значение атрибута с помощью функции `evaluate_locator`.
   - Если `locator.by` имеет значение "VALUE", возвращает полученное значение атрибута.
   - Если `locator.event` присутствует, выполняет событие с помощью функции `execute_event`.
   - Если `locator.attribute` присутствует, получает атрибут с помощью функции `get_attribute_by_locator`.
   - В противном случае получает веб-элемент с помощью функции `get_webelement_by_locator`.
3. Если `locator.selector` и `locator.by` являются списками, и `locator.sorted` имеет значение "pairs", функция создает пары элементов на основе атрибутов, селекторов и событий из списков.
4. В противном случае логирует предупреждение о неверном значении `sorted` или отсутствии списков `selector` и `by`.

```
Выполнение действий над веб-элементом
│
├─── Преобразование локатора в SimpleNamespace (если это словарь)
│
├─── Проверка наличия атрибута и селектора в локаторе
│   └─── Если атрибут или селектор отсутствуют, возврат None
│
├─── Определение внутренней функции _parse_locator
│   │
│   ├─── Проверка атрибута mandatory
│   │   └─── Если атрибуты event и attribute присутствуют, но mandatory отсутствует, возврат None
│   │
│   ├─── Если атрибуты locator.attribute и locator.by являются строками
│   │   ├─── Получение значения атрибута с помощью evaluate_locator
│   │   │   └─── Если locator.by == "VALUE", возврат полученного значения атрибута
│   │   ├─── Выполнение события с помощью execute_event (если locator.event присутствует)
│   │   ├─── Получение атрибута с помощью get_attribute_by_locator (если locator.attribute присутствует)
│   │   └─── Получение веб-элемента с помощью get_webelement_by_locator (в противном случае)
│   │
│   └─── Если locator.selector и locator.by являются списками и locator.sorted == "pairs"
│       └─── Создание пар элементов на основе атрибутов, селекторов и событий из списков
│
└─── Возврат результата выполнения _parse_locator
```

### `evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`

**Назначение**:
Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для вычисления (строка, список строк или словарь).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

**Как работает функция**:
1. Определяет внутреннюю асинхронную функцию `_evaluate`, которая возвращает переданный ей атрибут.
2. Если атрибут является списком, функция использует `asyncio.gather` для параллельного вычисления каждого элемента списка с помощью функции `_evaluate`.
3. В противном случае функция вычисляет атрибут с помощью функции `_evaluate`.

**Внутренние функции**:

#### `_evaluate(attr: str) -> Optional[str]`

**Назначение**:
Возвращает переданный ей атрибут.

**Параметры**:
- `attr` (str): Атрибут для возврата.

**Возвращает**:
- `Optional[str]`: Переданный атрибут.

```
Вычисление атрибутов локатора
│
├─── Определение внутренней функции _evaluate
│   └─── Возврат переданного атрибута
│
├─── Если атрибут является списком
│   └─── Параллельное вычисление каждого элемента списка с помощью _evaluate
│
└─── Вычисление атрибута с помощью _evaluate (в противном случае)
```

### `get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]`

**Назначение**:
Получает указанный атрибут из веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Атрибут или None.

**Как работает функция**:
1. Преобразует локатор в SimpleNamespace, если он представлен в виде словаря.
2. Получает веб-элемент с помощью функции `get_webelement_by_locator`.
3. Если элемент не найден, функция логирует отладочное сообщение и возвращает `None`.
4. Определяет внутреннюю функцию `_parse_dict_string`, которая преобразует строку в формате '{attr1:attr2}' в словарь.
5. Определяет внутреннюю асинхронную функцию `_get_attribute`, которая извлекает атрибут из Locator.
6. Определяет внутреннюю асинхронную функцию `_get_attributes_from_dict`, которая извлекает несколько атрибутов на основе словаря.
7. Если `locator.attribute` является строкой и начинается с "{", функция преобразует строку в словарь с помощью функции `_parse_dict_string`.
8. Если атрибут является списком, функция использует `asyncio.gather` для параллельного получения атрибутов каждого элемента списка с помощью функции `_get_attribute`.
9. В противном случае функция получает атрибут с помощью функции `_get_attribute`.

**Внутренние функции**:

#### `_parse_dict_string(attr_string: str) -> dict | None`

**Назначение**:
Преобразует строку в формате '{attr1:attr2}' в словарь.

**Параметры**:
- `attr_string` (str): Строка для преобразования.

**Возвращает**:
- `dict | None`: Словарь или None в случае ошибки.

**Как работает функция**:
1. Пытается преобразовать строку в словарь, разделяя ее на пары ключ-значение.
2. В случае ошибки логирует отладочное сообщение и возвращает `None`.

#### `_get_attribute(el: Locator, attr: str) -> Optional[str]`

**Назначение**:
Извлекает один атрибут из Locator.

**Параметры**:
- `el` (Locator): Объект Locator.
- `attr` (str): Имя атрибута для извлечения.

**Возвращает**:
- `Optional[str]`: Значение атрибута или None в случае ошибки.

**Как работает функция**:
1. Пытается извлечь атрибут из Locator с помощью метода `get_attribute`.
2. В случае ошибки логирует отладочное сообщение и возвращает `None`.

#### `_get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict`

**Назначение**:
Извлекает несколько атрибутов на основе словаря.

**Параметры**:
- `element` (Locator): Объект Locator.
- `attr_dict` (dict): Словарь атрибутов для извлечения.

**Возвращает**:
- `dict`: Словарь извлеченных атрибутов.

**Как работает функция**:
1. Создает пустой словарь для хранения результатов.
2. Итерируется по словарю атрибутов и извлекает каждый атрибут с помощью функции `_get_attribute`.
3. Возвращает словарь извлеченных атрибутов.

```
Получение атрибута из веб-элемента
│
├─── Преобразование локатора в SimpleNamespace (если это словарь)
│
├─── Получение веб-элемента с помощью get_webelement_by_locator
│   └─── Если элемент не найден, возврат None
│
├─── Определение внутренней функции _parse_dict_string
│   └─── Преобразование строки в формате '{attr1:attr2}' в словарь
│
├─── Определение внутренней функции _get_attribute
│   └─── Извлечение одного атрибута из Locator
│
├─── Определение внутренней функции _get_attributes_from_dict
│   └─── Извлечение нескольких атрибутов на основе словаря
│
├─── Если locator.attribute является строкой и начинается с "{"
│   └─── Преобразование строки в словарь с помощью _parse_dict_string
│
├─── Если атрибут является списком
│   └─── Параллельное получение атрибутов каждого элемента списка с помощью _get_attribute
│
└─── Получение атрибута с помощью _get_attribute (в противном случае)
```

### `get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]`

**Назначение**:
Получает веб-элемент, используя локатор.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).

**Возвращает**:
- `Optional[Locator | List[Locator]]`: Playwright Locator.

**Как работает функция**:
1. Преобразует локатор в SimpleNamespace, если он представлен в виде словаря.
2. Если локатор недействителен, функция логирует сообщение об ошибке и возвращает `None`.
3. В зависимости от значения `locator.by` (XPATH или другой), функция использует `self.page.locator` для поиска элемента на странице.
4. В зависимости от значения `locator.if_list` (all, first, last, even, odd, list, int), функция возвращает либо все элементы, первый элемент, последний элемент, четные элементы, нечетные элементы, элементы из списка индексов, элемент по индексу, либо все элементы.
5. В случае ошибки при поиске элемента функция логирует сообщение об ошибке и возвращает `None`.

```
Получение веб-элемента по локатору
│
├─── Преобразование локатора в SimpleNamespace (если это словарь)
│
├─── Если локатор недействителен, возврат None
│
├─── Поиск элемента на странице с помощью self.page.locator
│   └─── Если locator.by == "XPATH", используется xpath={locator.selector}
│   └─── Иначе используется locator.selector
│
├─── В зависимости от значения locator.if_list, возврат:
│   ├─── Все элементы (all)
│   ├─── Первый элемент (first)
│   ├─── Последний элемент (last)
│   ├─── Четные элементы (even)
│   ├─── Нечетные элементы (odd)
│   ├─── Элементы из списка индексов (list)
│   ├─── Элемент по индексу (int)
│   └─── Все элементы (в противном случае)
│
└─── В случае ошибки при поиске элемента, возврат None
```

### `get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]`

**Назначение**:
Делает скриншот найденного веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).
- `webelement` (Optional[Locator]): Веб-элемент Locator.

**Возвращает**:
- `Optional[bytes]`: Скриншот в байтах или None.

**Как работает функция**:
1. Преобразует локатор в SimpleNamespace, если он представлен в виде словаря.
2. Если `webelement` не передан, функция получает веб-элемент с помощью функции `get_webelement_by_locator`.
3. Если элемент не найден, функция логирует отладочное сообщение и возвращает `None`.
4. Пытается сделать скриншот элемента с помощью метода `screenshot`.
5. В случае ошибки при создании скриншота функция логирует сообщение об ошибке и возвращает `None`.

```
Создание скриншота веб-элемента
│
├─── Преобразование локатора в SimpleNamespace (если это словарь)
│
├─── Если webelement не передан, получение веб-элемента с помощью get_webelement_by_locator
│   └─── Если элемент не найден, возврат None
│
├─── Создание скриншота элемента с помощью screenshot
│
└─── В случае ошибки при создании скриншота, возврат None
```

### `execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]`

**Назначение**:
Выполняет событие, связанное с локатором.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).
- `message` (Optional[str]): Необязательное сообщение для событий.
- `typing_speed` (float): Необязательная скорость ввода текста для событий.

**Возвращает**:
- `Union[str, List[str], bytes, List[bytes], bool]`: Статус выполнения.

**Как работает функция**:
1. Преобразует локатор в SimpleNamespace, если он представлен в виде словаря.
2. Получает веб-элемент с помощью функции `get_webelement_by_locator`.
3. Если элемент не найден, функция логирует отладочное сообщение и возвращает `False`.
4. Разделяет строку `locator.event` на отдельные события.
5. Итерируется по списку событий и выполняет каждое событие:
   - Если событие "click()", функция пытается выполнить клик по элементу.
   - Если событие начинается с "pause(", функция извлекает длительность паузы из события и приостанавливает выполнение на указанное время.
   - Если событие "upload_media()", функция проверяет наличие сообщения и пытается загрузить файлы, указанные в сообщении.
   - Если событие "screenshot()", функция делает скриншот элемента.
   - Если событие "clear()", функция очищает поле элемента.
   - Если событие начинается с "send_keys(", функция извлекает клавиши для отправки из события и отправляет их элементу.
   - Если событие начинается с "type(", функция извлекает сообщение из события и вводит его в элемент с указанной скоростью ввода.
6. Если все события выполнены успешно, функция возвращает `True`.

```
Выполнение события, связанного с локатором
│
├─── Преобразование локатора в SimpleNamespace (если это словарь)
│
├─── Получение веб-элемента с помощью get_webelement_by_locator
│   └─── Если элемент не найден, возврат False
│
├─── Разделение строки locator.event на отдельные события
│
├─── Итерация по списку событий и выполнение каждого события
│   ├─── Если событие "click()", попытка выполнить клик по элементу
│   ├─── Если событие начинается с "pause(", извлечение длительности паузы и приостановка выполнения
│   ├─── Если событие "upload_media()", проверка наличия сообщения и попытка загрузить файлы
│   ├─── Если событие "screenshot()", создание скриншота элемента
│   ├─── Если событие "clear()", очистка поля элемента
│   ├─── Если событие начинается с "send_keys(", извлечение клавиш и отправка их элементу
│   └─── Если событие начинается с "type(", извлечение сообщения и ввод его в элемент
│
└─── Если все события выполнены успешно, возврат True
```

### `send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool`

**Назначение**:
Отправляет сообщение веб-элементу.

**Параметры**:
- `locator` (dict | SimpleNamespace): Информация о местоположении элемента на странице.
- `message` (str): Сообщение для отправки веб-элементу.
- `typing_speed` (float): Скорость ввода сообщения в секундах.

**Возвращает**:
- `bool`: Возвращает `True`, если сообщение было успешно отправлено, `False` в противном случае.

**Как работает функция**:
1. Преобразует локатор в SimpleNamespace, если он представлен в виде словаря.
2. Получает веб-элемент с помощью функции `get_webelement_by_locator`.
3. Если элемент не найден, функция логирует отладочное сообщение и возвращает `False`.
4. Вводит сообщение в элемент с указанной скоростью ввода.
5. Возвращает `True`, если сообщение было успешно отправлено.

```
Отправка сообщения веб-элементу
│
├─── Преобразование локатора в SimpleNamespace (если это словарь)
│
├─── Получение веб-элемента с помощью get_webelement_by_locator
│   └─── Если элемент не найден, возврат False
│
├─── Ввод сообщения в элемент с указанной скоростью ввода
│
└─── Возврат True, если сообщение было успешно отправлено
```

### `goto(self, url: str) -> None`

**Назначение**:
Переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Как работает функция**:
1. Проверяет, что объект страницы существует.
2. Пытается перейти по указанному URL с помощью метода `goto`.
3. В случае ошибки при переходе функция логирует сообщение об ошибке.

```
Переход по URL
│
├─── Проверка, что объект страницы существует
│
├─── Переход по URL с помощью goto
│
└─── В случае ошибки при переходе, логирование сообщения об ошибке