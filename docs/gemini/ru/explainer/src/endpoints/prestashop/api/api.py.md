## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
   - **Переменные**: Их типы и использование.
   - Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**Общая схема работы `PrestaShop`:**

1.  **Инициализация `PrestaShop`:**
    *   При создании объекта `PrestaShop` происходит инициализация с API ключом, доменом PrestaShop, форматом данных (JSON или XML) и языком.
    *   Устанавливается `requests.Session` для HTTP-запросов.
    *   Происходит проверка соединения с API PrestaShop (`HEAD`-запрос).
2.  **Выполнение запроса:**
    *   Функция `_exec` отвечает за отправку HTTP запросов.
    *   Она принимает ресурс (например, `products`), ID ресурса, HTTP метод, данные, параметры и другие настройки.
    *   Формирует URL запроса.
    *   Отправляет запрос с помощью `requests.Session`.
    *   Проверяет статус код ответа (через `_check_response`).
    *   Парсит ответ (JSON или XML) через `_parse`.
    *   Возвращает данные.
3.  **Обработка ответа:**
    *   Функция `_check_response` проверяет HTTP статус код (200, 201). Если не успех, вызывает `_parse_response_error` для обработки ошибок.
    *   Функция `_parse_response_error` парсит ошибки, выводя их в лог.
    *   Функция `_parse` парсит XML или JSON.
4.  **CRUD операции:**
    *   `create`: Отправляет `POST` запрос для создания ресурсов.
    *   `read`: Отправляет `GET` запрос для чтения ресурса по ID.
    *   `write`: Отправляет `PUT` запрос для обновления ресурса.
    *   `unlink`: Отправляет `DELETE` запрос для удаления ресурса.
    *   `search`: Отправляет `GET` запрос для поиска ресурсов с фильтром.
5.  **Работа с файлами:**
    *   `create_binary`: Загружает бинарные файлы (изображения).
    *   `_save`: Сохраняет данные в JSON файл.
    *    `remove_file`: Удаляет временные файлы.
6.  **Работа с изображениями:**
    *   `upload_image_async` / `upload_image`: Загружает изображение по URL. Скачивает изображение, сохраняет его локально, затем загружает его через `create_binary`, а после удаляет локальный файл.
    *   `get_product_images`: получает изображения для конкретного продукта.
7.  **Прочие функции:**
    *   `ping`: Проверяет работоспособность API.
    *    `get_apis`: получает список доступных API.
    *   `get_languages_schema`: получает языковую схему.

**Примеры:**

1.  **Создание ресурса (create):**
    *   Входные данные: `resource` = `"taxes"`, `data` = `{'tax': {'rate': 3.0, 'active': '1', 'name': {'language': {'attrs': {'id': '1'}, 'value': '3% tax'}}}}`
    *   `_exec` отправляет `POST` запрос на `API_DOMAIN/taxes`, с `data` в теле.
    *   Возвращает JSON с данными созданного ресурса.

2.  **Чтение ресурса (read):**
    *   Входные данные: `resource` = `"products"`, `resource_id` = `22`
    *   `_exec` отправляет `GET` запрос на `API_DOMAIN/products/22`.
    *   Возвращает JSON с данными продукта 22.

3.  **Обновление ресурса (write):**
    *   Входные данные: `resource` = `"taxes"`, `data` = `{'tax': {'id': '123', 'rate': 5.0, ...}}`
    *   `_exec` отправляет `PUT` запрос на `API_DOMAIN/taxes/123`, с `data` в теле.
    *   Возвращает JSON с обновленными данными.

4.  **Удаление ресурса (unlink):**
    *   Входные данные: `resource` = `"taxes"`, `resource_id` = `123`
    *   `_exec` отправляет `DELETE` запрос на `API_DOMAIN/taxes/123`.
    *   Возвращает `True` при успехе.

5.  **Поиск ресурсов (search):**
    *   Входные данные: `resource` = `"products"`, `filter` = `"[name]=%[тест]%", limit='5'`
    *   `_exec` отправляет `GET` запрос на `API_DOMAIN/products?filter=[name]=%[тест]%&limit=5`.
    *   Возвращает список JSON объектов с результатами поиска.

6.  **Загрузка бинарного файла (create_binary):**
    *   Входные данные: `resource` = `"images/products/22"`, `file_path` = `"image.jpeg"`, `file_name` = `"image"`
    *   Отправляет `POST` запрос с бинарными данными файла на `API_DOMAIN/images/products/22`.
    *   Возвращает JSON с ответом.

## <mermaid>

```mermaid
flowchart TD
    Start[Начало] --> Initialize[Инициализация PrestaShop]
    Initialize --> PrepareURL[Подготовка URL (_prepare)]
    PrepareURL --> ExecuteRequest[Выполнение запроса (_exec)]
    ExecuteRequest --> CheckResponse[Проверка ответа (_check_response)]
    CheckResponse -- Status 200/201 --> ParseResponse[Парсинг ответа (_parse)]
    CheckResponse -- Error Status --> ParseError[Обработка ошибки (_parse_response_error)]
    ParseError --> LogError[Логирование ошибки]
    ParseResponse --> ReturnData[Возврат данных]
    ReturnData --> End[Конец]
    LogError --> End

    subgraph "Методы PrestaShop"
        Initialize
        PrepareURL
        ExecuteRequest
        CheckResponse
        ParseResponse
        ParseError
        LogError
        ReturnData
    end

    style Initialize fill:#f9f,stroke:#333,stroke-width:2px
    style PrepareURL fill:#ccf,stroke:#333,stroke-width:2px
    style ExecuteRequest fill:#fcc,stroke:#333,stroke-width:2px
    style CheckResponse fill:#cfc,stroke:#333,stroke-width:2px
    style ParseResponse fill:#ccf,stroke:#333,stroke-width:2px
    style ParseError fill:#fcc,stroke:#333,stroke-width:2px
    style LogError fill:#fcf,stroke:#333,stroke-width:2px
    style ReturnData fill:#ccf,stroke:#333,stroke-width:2px

    subgraph "CRUD операции"
        Create[Создание (create)]
        Read[Чтение (read)]
        Update[Обновление (write)]
        Delete[Удаление (unlink)]
        Search[Поиск (search)]
    end
    style Create fill:#fff,stroke:#333,stroke-width:2px
    style Read fill:#fff,stroke:#333,stroke-width:2px
    style Update fill:#fff,stroke:#333,stroke-width:2px
    style Delete fill:#fff,stroke:#333,stroke-width:2px
    style Search fill:#fff,stroke:#333,stroke-width:2px

   Initialize --> Create
   Initialize --> Read
   Initialize --> Update
   Initialize --> Delete
   Initialize --> Search

  Create --> PrepareURL
  Read --> PrepareURL
  Update --> PrepareURL
  Delete --> PrepareURL
  Search --> PrepareURL


    subgraph "Работа с файлами и изображениями"
       CreateBinary[Загрузка бинарного файла (create_binary)]
       SaveData[Сохранение данных (_save)]
       RemoveFile[Удаление файла (remove_file)]
       UploadImageAsync[Загрузка изображения асинхронно (upload_image_async)]
       UploadImage[Загрузка изображения (upload_image)]
       GetProductImages[Получение изображений продукта (get_product_images)]
    end
    style CreateBinary fill:#fff,stroke:#333,stroke-width:2px
    style SaveData fill:#fff,stroke:#333,stroke-width:2px
     style RemoveFile fill:#fff,stroke:#333,stroke-width:2px
    style UploadImageAsync fill:#fff,stroke:#333,stroke-width:2px
    style UploadImage fill:#fff,stroke:#333,stroke-width:2px
    style GetProductImages fill:#fff,stroke:#333,stroke-width:2px

    Initialize --> CreateBinary
    Initialize --> SaveData
    Initialize --> RemoveFile
    Initialize --> UploadImageAsync
    Initialize --> UploadImage
    Initialize --> GetProductImages

    UploadImageAsync --> CreateBinary
    UploadImage --> CreateBinary
    GetProductImages --> PrepareURL



    subgraph "Прочие функции"
        Ping[Проверка связи (ping)]
        GetApis[Получение списка API (get_apis)]
        GetLanguagesSchema[Получение схемы языков (get_languages_schema)]
    end

    style Ping fill:#fff,stroke:#333,stroke-width:2px
    style GetApis fill:#fff,stroke:#333,stroke-width:2px
    style GetLanguagesSchema fill:#fff,stroke:#333,stroke-width:2px
    Initialize --> Ping
    Initialize --> GetApis
    Initialize --> GetLanguagesSchema
    Ping --> PrepareURL
    GetApis --> PrepareURL
    GetLanguagesSchema --> PrepareURL

    Start --> Header[<code>header.py</code><br> Determine Project Root]
    Header --> import[Import Global Settings: <br><code>from src import gs</code>]


```

**Объяснение зависимостей `mermaid`:**

*   **flowchart TD**: Определяет тип диаграммы как блок-схему.
*   **Start, Initialize, PrepareURL, ExecuteRequest, CheckResponse, ParseResponse, ParseError, LogError, ReturnData, End:** Узлы, представляющие шаги процесса.
*   **Методы PrestaShop, CRUD операции, Работа с файлами и изображениями, Прочие функции:** Подграфы, группирующие связанные узлы.
*   **Стрелки `-->`**: Показывают поток выполнения операций.
*   **`subgraph`**: Группирует узлы.
*   **`style`**: Определяет стили для узлов.

## <объяснение>

**Импорты:**

*   `os`: Модуль для взаимодействия с операционной системой (например, для удаления файлов).
*   `sys`: Модуль для работы с параметрами и функциями времени выполнения.
*   `enum.Enum`: Класс для создания перечислений (используется для `Format`).
*   `http.client.HTTPConnection`: Класс для установления HTTP-соединений (не используется напрямую, но может использоваться `requests` под капотом).
*   `pathlib.Path`: Класс для работы с путями файловой системы.
*   `typing`: Модуль для статической типизации.
*   `xml.etree.ElementTree`: Модуль для работы с XML.
*   `xml.parsers.expat.ExpatError`: Исключение, которое может возникнуть при парсинге XML.
*   `requests.Session`: Класс для управления HTTP-сессиями.
*   `requests.models.PreparedRequest`: Класс для подготовки HTTP-запросов.
*   `header`: Модуль, определяющий корень проекта (в связке с `src`).
*   `src.gs`: Модуль глобальных настроек приложения.
*   `src.logger.exceptions`: Модуль с кастомными исключениями для ошибок PrestaShop.
*   `src.logger.logger`: Модуль для логирования.
*   `src.utils.convertors`: Модули для конвертации данных.
*    `src.utils.file`: Модуль для работы с файловой системой.
*   `src.utils.image`: Модуль для работы с изображениями.
*   `src.utils.jjson`: Модуль для работы с JSON (кастомные функции).
*   `src.utils.printer`: Модуль для форматированного вывода.

**Класс `PrestaShop`:**

*   **Назначение:** Обеспечивает взаимодействие с PrestaShop API.
*   **Атрибуты:**
    *   `client`: `requests.Session` для HTTP запросов.
    *   `debug`: Флаг для включения/выключения режима отладки.
    *   `language`: ID языка по умолчанию.
    *   `data_format`: Формат данных по умолчанию (`JSON` или `XML`).
    *    `ps_version`: Версия PrestaShop.
    *    `API_DOMAIN`: Доменное имя API.
    *    `API_KEY`: API ключ.
*   **Методы:**
    *   `__init__`: Инициализирует объект `PrestaShop` с настройками API. Проверяет соединение с PrestaShop API.
    *   `ping`: Проверяет доступность API.
    *   `_check_response`: Проверяет статус ответа и возвращает результат.
    *   `_parse_response_error`: Парсит ответ API в случае ошибки и логирует ее.
    *   `_prepare`: Формирует URL запроса с параметрами.
    *   `_exec`: Выполняет HTTP-запрос к API.
    *    `_parse`: Парсит XML или JSON ответ.
    *   `create`, `read`, `write`, `unlink`, `search`: Методы для выполнения CRUD операций.
    *   `create_binary`: Загружает бинарные данные через API.
    *   `_save`: Сохраняет данные в файл.
    *   `remove_file`: Удаляет файл с диска.
    *    `get_data`: Получает и сохраняет данные ресурса.
    *   `get_apis`: Возвращает список доступных API.
    *   `get_languages_schema`: Возвращает схему для языков.
    *   `upload_image_async`, `upload_image`: Загружают изображения в API.
    *   `get_product_images`: Получает изображения продукта.

**Класс `Format`:**

*   **Назначение:** Представляет формат данных (`JSON`, `XML`).
*   **Атрибуты:** `JSON`, `XML`.

**Функции:**

*   `ping()`:
    *   **Аргументы:** Нет
    *   **Возвращаемое значение:** `bool` (`True` если ping успешен, иначе `False`).
    *   **Назначение:** Проверяет работоспособность API.
*   `_check_response(status_code: int, response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None) -> bool`:
    *   **Аргументы:**
        *   `status_code`: HTTP статус код.
        *   `response`: объект ответа `requests`.
         *   `method`: HTTP метод.
         *   `url`: URL запроса.
         *    `headers`: заголовки запроса.
         *    `data`: данные запроса.
    *   **Возвращаемое значение:** `bool` (`True` если код 200/201, иначе `False`).
    *   **Назначение:** Проверяет успешность HTTP-ответа.
*   `_parse_response_error(response, method: Optional[str] = None, url: Optional[str] = None,headers: Optional[dict] = None, data: Optional[dict] = None)`
    *   **Аргументы:**
        *    `response`: объект ответа `requests`.
        *   `method`: HTTP метод.
         *   `url`: URL запроса.
         *    `headers`: заголовки запроса.
         *    `data`: данные запроса.
    *   **Возвращаемое значение:** `requests.Response` или кортеж `code, message`
    *   **Назначение:** Парсит и обрабатывает ошибки ответа.
*   `_prepare(url: str, params: dict) -> str`:
    *   **Аргументы:**
        *   `url`: базовый URL.
        *   `params`: параметры запроса.
    *   **Возвращаемое значение:** `str` (полный URL с параметрами).
    *   **Назначение:** Готовит URL для запроса.
*   `_exec(resource: str, resource_id: Optional[Union[int, str]] = None, resource_ids: Optional[Union[int, Tuple[int]]] = None, method: str = 'GET', data: Optional[dict] = None, headers: Optional[dict] = None, search_filter: Optional[Union[str, dict]] = None, display: Optional[Union[str, list]] = 'full', schema: Optional[str] = None, sort: Optional[str] = None, limit: Optional[str] = None, language: Optional[int] = None, io_format: str = 'JSON') -> Optional[dict]`:
    *   **Аргументы:** Различные параметры для запроса (ресурс, ID, метод, данные, фильтры, формат и т.д.).
    *   **Возвращаемое значение:** `Optional[dict]` (данные от API или `False`).
    *   **Назначение:** Основная функция для выполнения запросов к API.
*   `_parse(text: str) -> Union[dict, ElementTree.Element, bool]`:
    *   **Аргументы:** `text`: текст ответа.
    *   **Возвращаемое значение:** `Union[dict, ElementTree.Element, bool]` (словарь, элемент XML или `False`).
    *   **Назначение:** Парсит ответ сервера (JSON/XML).
*   `create(resource: str, data: dict) -> Optional[dict]`:
    *   **Аргументы:**
        *   `resource`: ресурс API.
        *   `data`: данные для создания.
    *   **Возвращаемое значение:** `Optional[dict]` (данные от API).
    *   **Назначение:** Создает новый ресурс.
*   `read(resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]`:
    *   **Аргументы:**
        *   `resource`: ресурс API.
        *   `resource_id`: ID ресурса.
         *   `**kwargs`: дополнительные параметры.
    *   **Возвращаемое значение:** `Optional[dict]` (данные от API).
    *   **Назначение:** Получает данные ресурса.
*   `write(resource: str, data: dict) -> Optional[dict]`:
    *   **Аргументы:**
        *   `resource`: ресурс API.
        *   `data`: данные для обновления.
    *   **Возвращаемое значение:** `Optional[dict]` (данные от API).
    *   **Назначение:** Обновляет ресурс.
*   `unlink(resource: str, resource_id: Union[int, str]) -> bool`:
    *   **Аргументы:**
        *   `resource`: ресурс API.
        *   `resource_id`: ID ресурса.
    *   **Возвращаемое значение:** `bool` (`True` если удаление успешно, иначе `False`).
    *   **Назначение:** Удаляет ресурс.
*   `search(resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]`:
    *   **Аргументы:**
        *   `resource`: ресурс API.
        *   `filter`: фильтр поиска.
        *    `**kwargs`: дополнительные параметры.
    *   **Возвращаемое значение:** `List[dict]` (список найденных ресурсов).
    *   **Назначение:** Выполняет поиск ресурсов.
*   `create_binary(resource: str, file_path: str, file_name: str) -> dict`:
    *   **Аргументы:**
        *   `resource`: ресурс API.
        *   `file_path`: путь к бинарному файлу.
        *   `file_name`: имя файла.
    *   **Возвращаемое значение:** `dict` (ответ от API).
    *   **Назначение:** Загружает бинарный файл через API.
*   `_save(file_name: str, data: dict)`:
    *   **Аргументы:**
        *   `file_name`: имя файла.
        *   `data`: данные для сохранения.
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Сохраняет данные в файл.
*    `get_data(resource: str, **kwargs) -> Optional[dict]`:
    *    **Аргументы:**
        *    `resource`: ресурс API.
        *   `**kwargs`: дополнительные параметры.
    *    **Возвращаемое значение:** `Optional[dict]` (данные или `False` при ошибке).
    *    **Назначение:** Получает данные и сохраняет их в файл.
*   `remove_file(file_path: str)`:
    *   **Аргументы:** `file_path`: путь к файлу.
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Удаляет файл.
*   `get_apis() -> Optional[dict]`:
    *   **Аргументы:** Нет.
    *   **Возвращаемое значение:** `Optional[dict]` (список API или `None`).
    *   **Назначение:** Возвращает список доступных API.
*    `get_languages_schema() -> Optional[dict]`:
    *   **Аргументы:** Нет.
    *   **Возвращаемое значение:** `Optional[dict]` (языковая схема или `None`).
    *   **Назначение:** Возвращает схему языков.
*   `upload_image_async(resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]`:
     *   **Аргументы:**
        *    `resource`: ресурс API.
        *    `resource_id`: ID ресурса.
        *   `img_url`: URL изображения.
        *    `img_name`: имя файла изображения.
    *    **Возвращаемое значение:** `Optional[dict]` (ответ API или `None`).
    *    **Назначение:** Загружает изображение (асинхронно).
*   `upload_image(resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]`:
    *   **Аргументы:**
        *    `resource`: ресурс API.
        *    `resource_id`: ID ресурса.
        *   `img_url`: URL изображения.
        *    `img_name`: имя файла изображения.
    *    **Возвращаемое значение:** `Optional[dict]` (ответ API или `None`).
    *    **Назначение:** Загружает изображение.
*   `get_product_images(product_id: int) -> Optional[dict]`:
    *   **Аргументы:** `product_id`: ID продукта.
    *   **Возвращаемое значение:** `Optional[dict]` (список изображений или `None`).
    *   **Назначение:** Возвращает список изображений продукта.

**Переменные:**

*   `API_DOMAIN`, `API_KEY`: Строки, содержащие домен и ключ API.
*   `client`: Экземпляр `requests.Session`, используемый для HTTP-запросов.
*   `debug`: Логическая переменная, контролирующая режим отладки.
*   `language`: Целое число, ID языка по умолчанию.
*   `data_format`: Строка, определяющая формат данных (`JSON` или `XML`).
*    `ps_version`: Версия PrestaShop.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок**: Ошибки в `_parse` обрабатываются, но могут быть более информативными, например, добавляя конкретное описание ошибки.
*   **Валидация данных:** Нет валидации входящих данных, что может привести к ошибкам.
*   **Асинхронная загрузка:** Метод `upload_image_async` объявлен, но не используется асинхронно, по факту это таже функция `upload_image`, но с теми же входными данными.  Реализовать действительно асинхронную загрузку.
*   **Дублирование кода:** Методы `upload_image_async` и `upload_image` делают практически одно и тоже. Стоит объединить в одну функцию.
*   **Логирование:**  Временный файл `stderr.log` в режиме отладки является неудобным способом логирования. Следует заменить его на стандартную систему логирования.
*   **Управление сессиями:** Сессия `requests.Session` создается в начале. Возможно, стоит сделать её более управляемой.
*   **Параметры запроса:** Параметры запроса передаются как `dict`, но стоит продумать более удобный способ формирования.
*   **Типизация:** Местами можно добавить более строгую типизацию.
*   **Удаление файлов:** Использование `try-except` для удаления файлов — хороший тон.

**Взаимосвязи с другими частями проекта:**

*   **`src.gs`**: Получение учетных данных (API_KEY) и других глобальных настроек.
*   **`src.logger`**: Логирование ошибок.
*   **`src.utils`**: Конвертация данных, работа с файлами, изображениями и JSON.
*   `header`: определение корня проекта для импорта `src`.

Этот класс является ключевым компонентом для взаимодействия с PrestaShop API и используется в других частях проекта, где требуются операции с PrestaShop.