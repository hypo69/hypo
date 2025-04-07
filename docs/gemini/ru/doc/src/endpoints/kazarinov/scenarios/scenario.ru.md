# Модуль `scenario_pricelist`

## Обзор

Этот скрипт является частью директории `hypotez/src/endpoints/kazarinov/scenarios` и предназначен для автоматизации процесса создания "мехирона" для Сергея Казаринова. Скрипт извлекает, парсит и обрабатывает данные о продуктах от различных поставщиков, подготавливает данные, обрабатывает их через ИИ и интегрирует с Facebook для публикации продуктов.

## Подробней

Более подробное описание. Объясни как и зачем используется данный код в проекте.
Анализируй предоставленный тебе ранее код.

## Классы

### `MexironBuilder`

**Описание**: Класс `MexironBuilder` предназначен для автоматизации процесса создания "мехирона". Он включает в себя функциональность для извлечения, обработки и публикации данных о продуктах.

**Принцип работы**:
Класс инициализируется с драйвером Selenium, загружает конфигурацию, устанавливает пути экспорта, инициализирует модель ИИ и выполняет сценарий парсинга, обработки и публикации данных о продуктах.

**Аттрибуты**:
- `driver`: Экземпляр Selenium WebDriver для управления браузером.
- `export_path`: Путь для экспорта данных.
- `mexiron_name`: Пользовательское имя для процесса мехирона.
- `price`: Цена для обработки.
- `timestamp`: Метка времени для процесса.
- `products_list`: Список обработанных данных о продуктах.
- `model`: Модель Google Generative AI.
- `config`: Конфигурация, загруженная из JSON.

**Методы**:

- `__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`

    **Назначение**: Инициализирует класс `MexironBuilder` с необходимыми компонентами.
    Args:
        driver (Driver): Экземпляр Selenium WebDriver.
        mexiron_name (Optional[str], optional): Пользовательское имя для процесса мехирона. По умолчанию `None`.

    **Параметры**:
    - `driver` (Driver): Экземпляр Selenium WebDriver.
    - `mexiron_name` (Optional[str], optional): Пользовательское имя для процесса мехирона. По умолчанию `None`.

    **Как работает функция**:
    1. Инициализирует экземпляр класса `MexironBuilder`, принимая драйвер WebDriver и пользовательское имя для мехирона.
    2. Загружает конфигурацию из JSON-файла с помощью `j_loads_ns`.
    3. Устанавливает путь для экспорта данных, используя текущую директорию и поддиректорию `mexiron_name`.
    4. Загружает системные инструкции для модели ИИ из файла `system_instruction.txt`.
    5. Инициализирует модель Google Generative AI.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver, mexiron_name="test_mexiron")
    ```
    
- `run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool`

    **Назначение**: Выполняет сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.
    
    Args:
        system_instruction (Optional[str], optional): Системные инструкции для модели ИИ. По умолчанию `None`.
        price (Optional[str], optional): Цена для обработки. По умолчанию `None`.
        mexiron_name (Optional[str], optional): Пользовательское имя мехирона. По умолчанию `None`.
        urls (Optional[str  |  List[str]], optional): URLs страниц продуктов. По умолчанию `None`.

    **Параметры**:
    - `system_instruction` (Optional[str], optional): Системные инструкции для модели ИИ. По умолчанию `None`.
    - `price` (Optional[str], optional): Цена для обработки. По умолчанию `None`.
    - `mexiron_name` (Optional[str], optional): Пользовательское имя мехирона. По умолчанию `None`.
    - `urls` (Optional[str | List[str]], optional): URLs страниц продуктов. По умолчанию `None`.

    **Возвращает**:
    - `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

    **Блок-схема**:
    ```mermaid
    flowchart TD
    Start[Start] --> IsOneTab{URL is from OneTab?}
    IsOneTab -->|Yes| GetDataFromOneTab[Get data from OneTab]
    IsOneTab -->|No| ReplyTryAgain[Reply - Try again]
    GetDataFromOneTab --> IsDataValid{Data valid?}
    IsDataValid -->|No| ReplyIncorrectData[Reply Incorrect data]
    IsDataValid -->|Yes| RunMexironScenario[Run Mexiron scenario]
    RunMexironScenario --> IsGraberFound{Graber found?}
    IsGraberFound -->|Yes| StartParsing[Start parsing: `url`]
    IsGraberFound -->|No| LogNoGraber[Log: No graber for `url`]
    StartParsing --> IsParsingSuccessful{Parsing successful?}
    IsParsingSuccessful -->|Yes| ConvertProductFields[Convert product fields]
    IsParsingSuccessful -->|No| LogParsingFailed[Log: Failed to parse product fields]
    ConvertProductFields --> IsConversionSuccessful{Conversion successful?}
    IsConversionSuccessful -->|Yes| SaveProductData[Save product data]
    IsConversionSuccessful -->|No| LogConversionFailed[Log: Failed to convert product fields]
    SaveProductData --> IsDataSaved{Data saved?}
    IsDataSaved -->|Yes| AppendToProductsList[Append to products_list]
    IsDataSaved -->|No| LogDataNotSaved[Log: Data not saved]
    AppendToProductsList --> ProcessAIHe[AI processing lang = he]
    ProcessAIHe --> ProcessAIRu[AI processing lang = ru]
    ProcessAIRu --> SaveHeJSON{Save JSON for he?}
    SaveHeJSON -->|Yes| SaveRuJSON[Save JSON for ru]
    SaveHeJSON -->|No| LogHeJSONError[Log: Error saving he JSON]
    SaveRuJSON --> IsRuJSONSaved{Save JSON for ru?}
    IsRuJSONSaved -->|Yes| GenerateReports[Generate reports]
    IsRuJSONSaved -->|No| LogRuJSONError[Log: Error saving ru JSON]
    GenerateReports --> IsReportGenerationSuccessful{Report generation successful?}
    IsReportGenerationSuccessful -->|Yes| SendPDF[Send PDF via Telegram]
    IsReportGenerationSuccessful -->|No| LogPDFError[Log: Error creating PDF]
    SendPDF --> ReturnTrue[Return True]
    LogPDFError --> ReturnTrue[Return True]
    ReplyIncorrectData --> ReturnTrue[Return True]
    ReplyTryAgain --> ReturnTrue[Return True]
    LogNoGraber --> ReturnTrue[Return True]
    LogParsingFailed --> ReturnTrue[Return True]
    LogConversionFailed --> ReturnTrue[Return True]
    LogDataNotSaved --> ReturnTrue[Return True]
    LogHeJSONError --> ReturnTrue[Return True]
    LogRuJSONError --> ReturnTrue[Return True]
    ```

    **Легенда**:

    1. **Начало (Start)**: Сценарий начинает выполнение.

    2. **Проверка источника URL (IsOneTab)**:
        - Если URL из OneTab, данные извлекаются из OneTab.
        - Если URL не из OneTab, пользователю отправляется сообщение "Try again".

    3. **Проверка валидности данных (IsDataValid)**:
        - Если данные не валидны, пользователю отправляется сообщение "Incorrect data".
        - Если данные валидны, запускается сценарий Mexiron.

    4. **Поиск грабера (IsGraberFound)**:
        - Если грабер найден, начинается парсинг страницы.
        - Если грабер не найден, логируется сообщение о том, что грабер отсутствует для данного URL.

    5. **Парсинг страницы (StartParsing)**:
        - Если парсинг успешен, данные преобразуются в нужный формат.
        - Если парсинг не удался, логируется ошибка.

    6. **Преобразование данных (ConvertProductFields)**:
        - Если преобразование успешно, данные сохраняются.
        - Если преобразование не удалось, логируется ошибка.

    7. **Сохранение данных (SaveProductData)**:
        - Если данные сохранены, они добавляются в список продуктов.
        - Если данные не сохранены, логируется ошибка.

    8. **Обработка через AI (ProcessAIHe, ProcessAIRu)**:
        - Данные обрабатываются AI для языков `he` (иврит) и `ru` (русский).

    9. **Сохранение JSON (SaveHeJSON, SaveRuJSON)**:
        - Результаты обработки сохраняются в формате JSON для каждого языка.
        - Если сохранение не удалось, логируется ошибка.

    10. **Генерация отчетов (GenerateReports)**:
        - Создаются HTML и PDF отчеты для каждого языка.
        - Если создание отчета не удалось, логируется ошибка.

    11. **Отправка PDF через Telegram (SendPDF)**:
        - PDF-файлы отправляются через Telegram.
        - Если отправка не удалась, логируется ошибка.

    12. **Завершение (ReturnTrue)**:
        - Сценарий завершается, возвращая `True`.
    
    **Как работает функция**:

        1. **Проверка источника URL**:
        Функция начинает с проверки, предоставлен ли URL из OneTab. Если это так, данные извлекаются из OneTab. Если URL не из OneTab, пользователю отправляется сообщение с просьбой повторить попытку.

        2. **Проверка валидности данных**:
        После извлечения данных функция проверяет, являются ли данные валидными. Если данные не валидны, пользователю отправляется сообщение об ошибке. Если данные валидны, выполняется сценарий Mexiron.

        3. **Поиск грабера**:
        Функция пытается найти соответствующий грабер для предоставленного URL. Если грабер найден, начинается парсинг страницы. Если грабер не найден, в журнал записывается сообщение об отсутствии грабера для данного URL.

        4. **Парсинг страницы**:
        С использованием найденного грабера функция выполняет парсинг страницы. Если парсинг успешен, данные преобразуются в нужный формат. Если парсинг не удался, в журнал записывается сообщение об ошибке парсинга.

        5. **Преобразование данных**:
        После успешного парсинга данные преобразуются в нужный формат. Если преобразование успешно, данные сохраняются. Если преобразование не удалось, в журнал записывается сообщение об ошибке преобразования.

        6. **Сохранение данных**:
        Сохраненные данные добавляются в список продуктов. Если данные не сохранены, в журнал записывается сообщение об ошибке сохранения.

        7. **Обработка через AI**:
        Данные обрабатываются с использованием AI для языков he (иврит) и ru (русский).

        8. **Сохранение JSON**:
        Результаты обработки сохраняются в формате JSON для каждого языка. Если сохранение не удалось, в журнал записывается сообщение об ошибке.

        9. **Генерация отчетов**:
        Создаются HTML и PDF отчеты для каждого языка. Если создание отчета не удалось, в журнал записывается сообщение об ошибке.

        10. **Отправка PDF через Telegram**:
        PDF-файлы отправляются через Telegram. Если отправка не удалась, в журнал записывается сообщение об ошибке.

        11. **Завершение**:
        Сценарий завершается, возвращая True.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Запуск сценария
    urls = ['https://example.com/product1', 'https://example.com/product2']
    mexiron_builder.run_scenario(urls=urls)
    ```

- `get_graber_by_supplier_url(self, url: str)`

    **Назначение**: Возвращает соответствующий грабер для данного URL поставщика.

    Args:
        url (str): URL страницы поставщика.

    **Параметры**:
    - `url` (str): URL страницы поставщика.

    **Возвращает**:
    - Экземпляр грабера, если найден, иначе `None`.

    **Как работает функция**:
    1. Принимает URL страницы поставщика в качестве аргумента.
    2. Проверяет, соответствует ли URL одному из известных поставщиков (например, OneTab, Go-up).
    3. Если URL соответствует известному поставщику, функция возвращает соответствующий грабер.
    4. Если URL не соответствует ни одному из известных поставщиков, функция возвращает `None`.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Получение грабера для URL
    url = "https://example.com/product"
    graber = mexiron_builder.get_graber_by_supplier_url(url)
    if graber:
        print("Graber найден")
    else:
        print("Graber не найден")
    ```

- `convert_product_fields(self, f: ProductFields) -> dict`

    **Назначение**: Конвертирует поля продукта в словарь.

    Args:
        f (ProductFields): Объект, содержащий парсированные данные о продукте.

    **Параметры**:
    - `f` (ProductFields): Объект, содержащий парсированные данные о продукте.

    **Возвращает**:
    - `dict`: Форматированный словарь данных о продукте.

    **Как работает функция**:
    1. Принимает объект `ProductFields`, содержащий парсированные данные о продукте.
    2. Извлекает значения из полей объекта `ProductFields` и формирует словарь, где ключами являются названия полей, а значениями - соответствующие данные о продукте.
    3. Возвращает полученный словарь.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
    from types import SimpleNamespace

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Пример объекта ProductFields
    product_fields = SimpleNamespace(name="Product Name", price="100", description="Product Description")

    # Конвертация полей продукта
    product_data = mexiron_builder.convert_product_fields(product_fields)
    print(product_data)
    ```

- `save_product_data(self, product_data: dict)`

    **Назначение**: Сохраняет данные о продукте в файл.

    Args:
        product_data (dict): Форматированные данные о продукте.

    **Параметры**:
    - `product_data` (dict): Форматированные данные о продукте.

    **Как работает функция**:
    1. Принимает словарь `product_data`, содержащий форматированные данные о продукте.
    2. Формирует имя файла для сохранения данных, используя `timestamp` и название продукта.
    3. Сохраняет данные в файл в формате JSON.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Пример данных о продукте
    product_data = {"name": "Product Name", "price": "100", "description": "Product Description"}

    # Сохранение данных о продукте
    mexiron_builder.save_product_data(product_data)
    ```

- `process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool`

    **Назначение**: Обрабатывает список продуктов через модель ИИ.

    Args:
        products_list (List[str]): Список словарей данных о продуктах в виде строки.
        lang (str): Язык обработки (`ru` или `he`).
        attempts (int, optional): Количество попыток повторного запроса в случае неудачи. По умолчанию 3.

    **Параметры**:
    - `products_list` (List[str]): Список словарей данных о продуктах в виде строки.
    - `lang` (str): Язык обработки (`ru` или `he`).
    - `attempts` (int, optional): Количество попыток повторного запроса в случае неудачи. По умолчанию 3.

    **Возвращает**:
    - `tuple | bool`: Обработанный ответ в форматах `ru` и `he`.

    **Как работает функция**:
    1. Принимает список продуктов (`products_list`) в виде строки, язык обработки (`lang`) и количество попыток повторного запроса (`attempts`).
    2. Формирует запрос для модели ИИ, включающий список продуктов и системные инструкции.
    3. Отправляет запрос в модель ИИ и получает ответ.
    4. В случае неудачи повторяет запрос указанное количество раз.
    5. Возвращает обработанный ответ.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Пример списка продуктов
    products_list = '[{"name": "Product Name", "price": "100", "description": "Product Description"}]'

    # Обработка данных через AI на русском языке
    result = mexiron_builder.process_ai(products_list, "ru")
    print(result)
    ```

- `post_facebook(self, mexiron: SimpleNamespace) -> bool`

    **Назначение**: Выполняет сценарий публикации в Facebook.

    Args:
        mexiron (SimpleNamespace): Обработанные данные для публикации.

    **Параметры**:
    - `mexiron` (SimpleNamespace): Обработанные данные для публикации.

    **Возвращает**:
    - `bool`: `True`, если публикация успешна, иначе `False`.

    **Как работает функция**:
    1. Принимает объект `mexiron`, содержащий обработанные данные для публикации.
    2. Выполняет сценарий публикации в Facebook, используя данные из объекта `mexiron`.
    3. Возвращает `True`, если публикация успешна, и `False` в противном случае.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
    from types import SimpleNamespace

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Пример данных для публикации
    mexiron_data = SimpleNamespace(name="Product Name", price="100", description="Product Description")

    # Публикация в Facebook
    result = mexiron_builder.post_facebook(mexiron_data)
    print(result)
    ```

- `create_report(self, data: dict, html_file: Path, pdf_file: Path)`

    **Назначение**: Генерирует HTML и PDF отчеты из обработанных данных.

    Args:
        data (dict): Обработанные данные.
        html_file (Path): Путь для сохранения HTML отчета.
        pdf_file (Path): Путь для сохранения PDF отчета.

    **Параметры**:
    - `data` (dict): Обработанные данные.
    - `html_file` (Path): Путь для сохранения HTML отчета.
    - `pdf_file` (Path): Путь для сохранения PDF отчета.

    **Как работает функция**:
    1. Принимает обработанные данные (`data`), путь для сохранения HTML отчета (`html_file`) и путь для сохранения PDF отчета (`pdf_file`).
    2. Генерирует HTML отчет из данных.
    3. Конвертирует HTML отчет в PDF формат.
    4. Сохраняет HTML и PDF отчеты в указанные файлы.

    **Примеры**:

    ```python
    from src.webdriver.driver import Driver
    from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
    from pathlib import Path

    # Инициализация Driver
    driver = Driver(...)

    # Инициализация MexironBuilder
    mexiron_builder = MexironBuilder(driver)

    # Пример данных для отчета
    report_data = {"name": "Product Name", "price": "100", "description": "Product Description"}

    # Пути для сохранения отчетов
    html_file = Path("report.html")
    pdf_file = Path("report.pdf")

    # Создание отчета
    mexiron_builder.create_report(report_data, html_file, pdf_file)
    ```

## Функции

### `Нет отдельных функций, только методы в классе MexironBuilder`

## Использование

Для использования этого скрипта выполните следующие шаги:

1. **Инициализация Driver**: Создайте экземпляр класса `Driver`.
2. **Инициализация MexironBuilder**: Создайте экземпляр класса `MexironBuilder` с драйвером.
3. **Запуск сценария**: Вызовите метод `run_scenario` с необходимыми параметрами.

#### Пример

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Запуск сценария
urls = ['https://example.com/product1', 'https://example.com/product2']
mexiron_builder.run_scenario(urls=urls)
```

## Зависимости

- `selenium`: Для веб-автоматизации.
- `asyncio`: Для асинхронных операций.
- `pathlib`: Для обработки путей к файлам.
- `types`: Для создания простых пространств имен.
- `typing`: Для аннотаций типов.
- `src.ai.gemini`: Для обработки данных через ИИ.
- `src.suppliers.*.graber`: Для извлечения данных от различных поставщиков.
- `src.endpoints.advertisement.facebook.scenarios`: Для публикации в Facebook.

## Обработка ошибок

Скрипт включает надежную обработку ошибок, чтобы обеспечить продолжение выполнения даже в случае, если некоторые элементы не найдены или если возникли проблемы с веб-страницей. Это особенно полезно для обработки динамических или нестабильных веб-страниц.

## Вклад

Вклад в этот скрипт приветствуется. Пожалуйста, убедитесь, что любые изменения хорошо документированы и включают соответствующие тесты.

## Лицензия

Этот скрипт лицензирован под MIT License. Подробности смотрите в файле `LICENSE`.