## <алгоритм>

1.  **Инициализация (класс `PrestaShop`):**
    *   При создании экземпляра класса `PrestaShop` происходит инициализация:
        *   Устанавливаются значения по умолчанию для `data_format` (JSON), `language` (1) и `debug` (True).
        *   Извлекаются `API_DOMAIN` и `API_KEY` из конфигурации `gs.credentials.presta.client.api_key`.
        *   Создается объект `Session` для HTTP-запросов и устанавливается базовая аутентификация с использованием `API_KEY`.
        *   Выполняется `HEAD`-запрос к API для получения версии PrestaShop (`ps_version`).
    *   Пример:
        ```python
        api = PrestaShop(
            data_format='JSON',
            default_lang=1,
            debug=True
        )
        ```

2.  **`ping()`:**
    *   Отправляет `HEAD`-запрос к API для проверки доступности сервиса.
    *   Возвращает `True`, если статус ответа 200 или 201, иначе `False`.
    *   Пример:
        ```python
        is_online = api.ping()
        ```

3.  **`_check_response()`:**
    *   Проверяет код статуса ответа. Если он равен 200 или 201, возвращает `True`.
    *   В случае ошибки вызывает `_parse_response_error()` для обработки ошибок и возвращает `False`.

4.  **`_parse_response_error()`:**
    *   Обрабатывает ошибку ответа API.
    *   Если формат данных `JSON`, выводит сообщение об ошибке с кодом статуса, URL, заголовками и текстом ответа.
    *   Если формат данных `XML`, пытается преобразовать XML в словарь и извлекает код и сообщение об ошибке.
    *   Пример:
        ```python
        # response.status_code == 404
        api._parse_response_error(response) # выведет ошибку
        ```

5.  **`_prepare()`:**
    *   Подготавливает URL для запроса, добавляя параметры.
    *   Использует `PreparedRequest` для добавления параметров в URL.
    *   Пример:
        ```python
        url = api._prepare("https://myPrestaShop.com/api/products", {"limit": "10"})
        # url == https://myPrestaShop.com/api/products?limit=10
        ```

6.  **`_exec()`:**
    *   Выполняет HTTP-запрос к API с указанным методом, ресурсом и данными.
    *   Формирует URL с учетом `resource`, `resource_id`, и дополнительных параметров (фильтр, лимит, и т.д.).
    *   Преобразует данные в XML, если `io_format` равен `XML`.
    *   Проверяет ответ с помощью `_check_response()`.
    *   Возвращает данные ответа в формате JSON (если `io_format == 'JSON'`) или XML (после разбора с помощью `_parse()`).
    *   Пример:
        ```python
        response = api._exec(
            resource='products',
            method='GET',
            search_filter='[name]=%[test]%',
            limit='10',
            io_format='JSON'
        )
        ```

7.  **`_parse()`:**
    *   Разбирает текст ответа (XML или JSON) в словарь или дерево XML.
    *   Обрабатывает ошибки при разборе (например, некорректный XML).
    *   Пример:
        ```python
        text = '<PrestaShop><products></products></PrestaShop>'
        data = api._parse(text) # data будет ElementTree.Element
        ```

8.  **CRUD Операции (`create`, `read`, `write`, `unlink`):**
    *   Обертки для `_exec()`, выполняющие операции POST (создание), GET (чтение), PUT (обновление) и DELETE (удаление).
    *   Примеры:
        ```python
        new_tax = api.create('taxes', {'tax': {'rate': 5}})
        tax = api.read('taxes', new_tax['id'])
        updated_tax = api.write('taxes', {'tax': {'id': new_tax['id'], 'rate': 6}})
        is_deleted = api.unlink('taxes', new_tax['id'])
        ```

9.  **`search()`:**
    *   Использует `_exec()` для поиска ресурсов по фильтру.
    *   Пример:
        ```python
        taxes = api.search('taxes', filter='[name]=%[5]%')
        ```

10. **`create_binary()`:**
    *   Отправляет `POST`-запрос с бинарным файлом (например, изображением) в теле запроса.
    *   Устанавливает заголовок `Content-Type` в `application/octet-stream`.
    *   Пример:
        ```python
        image_response = api.create_binary('images/products/22', 'img.jpeg', 'image')
        ```

11. **`_save()`:**
    *   Сохраняет данные в файл в формате JSON.
    *   Использует `save_text_file` и `j_dumps` для сохранения.

12. **`get_data()`:**
    *   Получает данные с API и сохраняет их в файл.
    *   Использует `_exec()` для получения и `_save()` для сохранения.

13. **`remove_file()`:**
    *   Удаляет файл с файловой системы.
    *   Обрабатывает возможные исключения.

14. **`get_apis()`:**
    *   Получает список доступных API ресурсов.

15. **`get_languages_schema()`:**
    *   Получает схему для языков.

16. **`upload_image_async()` и `upload_image()`:**
    *   Загружают изображения на сервер PrestaShop.
    *   Используют `save_png_from_url()` для загрузки и конвертации изображения из URL.
    *   Вызывают `create_binary()` для загрузки файла.
    *   Удаляют временный файл с помощью `remove_file()`.

17. **`get_product_images()`:**
    *   Получает изображения для продукта по ID.

## <mermaid>

```mermaid
graph LR
    A[PrestaShop Instance Creation] --> B(init)
    B --> C{Credentials Load};
    C --> D[Session Creation];
    D --> E{Auth};
    E --> F[HEAD Request for version];
    F --> G(set ps_version);
    
    H[ping()] --> I[HEAD Request];
    I --> J{check_response};
    
    K[_check_response()] --> L{status in (200, 201)?};
    L -- Yes --> M[return True];
    L -- No --> N[_parse_response_error()];
    N --> O[return False];
    
    P[_parse_response_error()] --> Q{data_format == 'JSON'?};
    Q -- Yes --> R[Log error];
    Q -- No --> S[_parse()];
    S --> T{is dict?};
    T -- Yes --> U[Extract error content];
    T -- No --> V[Extract error];
    U --> W[log error XML];
    V --> W;

    X[_prepare()] --> Y[PreparedRequest];
    Y --> Z[Prepare URL];
    Z --> AA[return Prepared URL];
    
    BB[_exec()] --> CC[Prepare URL with _prepare()];
    CC --> DD{data and io_format == 'XML'?};
    DD -- Yes --> EE[Convert data to XML with dict2xml];
    DD -- No --> EE[pass];
    EE --> FF[HTTP Request];
    FF --> GG{check_response};
    GG -- Yes --> HH{io_format == 'JSON'?};
    HH -- Yes --> II[response.json()];
    HH -- No --> JJ[_parse()];
    GG -- No --> KK[return False];

    LL[_parse()] --> MM{data_format == 'JSON'?};
    MM -- Yes --> NN[response.json()];
    NN --> OO{if 'PrestaShop' in response?}
    OO -- Yes --> PP[return response.get('PrestaShop')];
    OO -- No --> PP[return response];
    MM -- No --> QQ[ElementTree.fromstring()];
    QQ --> RR[return ElementTree object];

    SS[create()] --> TT[_exec() with POST];
    UU[read()] --> VV[_exec() with GET];
    WW[write()] --> XX[_exec() with PUT];
    YY[unlink()] --> ZZ[_exec() with DELETE];
    AAA[search()] --> BBB[_exec() with GET];
    
    CCC[create_binary()] --> DDD[Open file as binary];
    DDD --> EEE[Set headers];
    EEE --> FFF[POST request with file data];
    FFF --> GGG[return json()];
    
    HHH[_save()] --> III[Save json with save_text_file()];
    
    JJJ[get_data()] --> KKK[_exec() with GET];
    KKK --> LLL{data is true?};
    LLL -- Yes --> MMM[save data with _save()];
    MMM --> NNN[return data];
    LLL -- No --> NNN[return False];
    
    OOO[remove_file()] --> PPP[os.remove()];
    
    QQQ[get_apis()] --> RRR[_exec() with GET 'apis'];
    
    SSS[get_languages_schema()] --> TTT[_exec() with GET 'languages'];

    UUU[upload_image_async()] --> VVV[save_png_from_url()];
    VVV --> WWW[create_binary()];
    WWW --> XXX[remove_file()];

    YYY[upload_image()] --> ZZZ[save_png_from_url()];
    ZZZ --> AAAA[create_binary()];
    AAAA --> BBBB[remove_file()];

    CCCC[get_product_images()] --> DDDD[_exec() with GET images by product id];

    classDef classFill fill:#f9f,stroke:#333,stroke-width:2px
    class A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL,MM,NN,OO,PP,QQ,RR,SS,TT,UU,VV,WW,XX,YY,ZZ,AAA,BBB,CCC,DDD,EEE,FFF,GGG,HHH,III,JJJ,KKK,LLL,MMM,NNN,OOO,PPP,QQQ,RRR,SSS,TTT,UUU,VVV,WWW,XXX,YYY,ZZZ,AAAA,BBBB,CCCC,DDDD classFill
```

## <объяснение>

### Импорты

*   `os`: Для работы с файловой системой (удаление файлов).
*   `sys`: Для управления потоками ввода-вывода (перенаправление stderr).
*   `enum.Enum`: Для создания перечисления `Format` (JSON, XML).
*   `http.client.HTTPConnection`: Не используется в коде, возможно, это устаревший импорт.
*   `requests.Session`: Для создания и управления HTTP-сессиями.
*   `requests.models.PreparedRequest`: Для подготовки URL-адреса с параметрами.
*   `typing.Dict, List`: Для аннотации типов данных.
*   `pathlib.Path`: Для работы с путями файлов (не используется напрямую в коде, но импортирован).
*   `xml.etree.ElementTree`: Для работы с XML.
*   `xml.parsers.expat.ExpatError`: Для обработки ошибок XML-парсинга.
*   `header`: Возможно, собственный модуль, но не используется в предоставленном коде, вероятно, это артефакт другого файла, так как в коде импортировано `from src import gs`
*   `src.gs`: (название изменено на `gs`) Вероятно, это модуль конфигурации или настроек проекта. Используется для получения ключа API.
*   `src.utils.file.save_text_file`: Функция для сохранения текста в файл.
*   `src.utils.convertors.base64.base64_to_tmpfile`: Функция для конвертации Base64 в временный файл (не используется).
*    `src.utils.convertors.dict.dict2xml`: Функция для конвертации словаря в XML.
*   `src.utils.convertors.xml2dict.xml2dict`: Функция для конвертации XML в словарь (не используется).
*   `src.utils.image.save_png_from_url`: Функция для загрузки и сохранения изображений из URL.
*   `src.utils.printer.pprint`: Функция для форматированного вывода данных.
*   `src.utils.jjson.j_loads, j_loads_ns, j_dumps`: Функции для работы с JSON, возможно с дополнительными опциями.
*   `src.logger.logger`: Модуль для логирования.
*   `src.logger.exceptions.PrestaShopException, PrestaShopAuthenticationError`: Кастомные исключения для ошибок PrestaShop.

### Классы

1.  **`Format(Enum)`:**
    *   Перечисление для представления формата данных (`JSON` или `XML`).
    *   Используется как тип для `data_format`, но в коде используется только `JSON`.

2.  **`PrestaShop`:**
    *   **Назначение:** Класс для взаимодействия с API PrestaShop.
    *   **Атрибуты:**
        *   `client`: HTTP-сессия (`requests.Session`).
        *   `debug`: Флаг для отладки (по умолчанию `True`).
        *   `language`: ID языка по умолчанию.
        *   `data_format`: Формат данных по умолчанию (`JSON`).
        *   `ps_version`: Версия PrestaShop, полученная из заголовков.
        *   `API_DOMAIN`: Домен API PrestaShop.
        *   `API_KEY`: Ключ API PrestaShop.
    *   **Методы:**
        *   `__init__`: Инициализация объекта, установка API-ключа, домена и параметров.
        *   `ping`: Проверка доступности сервиса.
        *   `_check_response`: Проверка статуса ответа HTTP.
        *   `_parse_response_error`: Обработка ошибок от API.
        *   `_prepare`: Подготовка URL-адреса для запроса.
        *   `_exec`: Выполнение HTTP-запроса.
        *   `_parse`: Разбор ответа API.
        *   `create`, `read`, `write`, `unlink`, `search`: CRUD-операции для ресурсов PrestaShop.
        *   `create_binary`: Отправка бинарного файла.
        *   `_save`: Сохранение данных в файл.
        *   `get_data`: Получение данных и сохранение в файл.
        *   `remove_file`: Удаление файла.
        *   `get_apis`: Получение списка доступных API.
        *  `get_languages_schema`: Получение схемы языков.
        *   `upload_image_async`, `upload_image`: Загрузка изображений.
        *   `get_product_images`: Получение изображений продукта.
    *   **Взаимодействие:**
        *   Использует `requests.Session` для выполнения HTTP-запросов.
        *   Использует `src.gs` для получения учетных данных.
        *   Использует другие утилиты `src.utils` для конвертации, сохранения, загрузки и т.д.
        *   Вызывает методы логирования `src.logger` для ошибок.

### Функции

*   Все функции, кроме методов класса `PrestaShop`, описаны в разделе "Импорты".

### Переменные

*   `MODE`:  Глобальная переменная, установленная в `dev`.
*   `client`:  Экземпляр `requests.Session` для выполнения HTTP-запросов.
*   `debug`: Флаг отладки (логирование в stderr и файл).
*   `language`:  ID языка PrestaShop.
*   `data_format`: Формат данных (JSON или XML).
*   `ps_version`:  Версия PrestaShop.
*   `API_DOMAIN`: URL API PrestaShop.
*   `API_KEY`: Ключ API PrestaShop.
*   `resource`, `resource_id`, `resource_ids`: Параметры для работы с API PrestaShop.
*   `method`: HTTP-метод (GET, POST, PUT, DELETE).
*   `data`, `headers`: Данные и заголовки для HTTP-запроса.
*    `search_filter`: Фильтр для запроса.
*   `display`, `schema`, `sort`, `limit`, `language`, `io_format`: Параметры запроса к API.
*   `file_path`, `file_name`: Путь к файлу и имя файла.
*    `img_url`: URL изображения.
*   `filename`: имя файла для сохранения
*   `png_file_path`: путь к сохраненному файлу изображения

### Потенциальные ошибки и области для улучшения

1.  **Зависимость от `gs.credentials`:** Жесткая зависимость от `gs.credentials`, делает класс менее переносимым. Следует использовать передачу через параметры или переменные окружения.
2.  **Жесткая привязка к JSON:** Хотя присутствует поддержка XML, код явно ориентирован на JSON.
3.  **Обработка ошибок:** Не всегда используются кастомные исключения.
4.  **Логирование:** Логирование не всегда достаточно информативное.
5.  **Дублирование кода:**  `upload_image_async` и `upload_image` выполняют один и тот же код (загрузка и удаление), следует выделить это в отдельный метод.
6.  **Отсутствие асинхронности:**  Хотя есть функция `upload_image_async`, все запросы выполняются синхронно.
7.  **Управление ресурсами**: Отсутствует обработка ошибок при работе с файлами (например, если файл не удалось удалить)
8.  **Устаревший импорт:** `http.client.HTTPConnection` импортирован, но не используется.
9.  **Возможный `None` return:** некоторые методы, например `get_languages_schema` могут вернуть `None`, это нужно учитывать при их вызове.

### Взаимосвязь с другими частями проекта

*   **`src.gs`:** Получение учетных данных API (зависимость).
*   **`src.utils.file`:** Сохранение данных в файлы.
*   **`src.utils.convertors`:** Конвертация данных в различные форматы.
*   **`src.utils.image`:** Загрузка и обработка изображений.
*   **`src.utils.printer`:** Форматированный вывод.
*   **`src.utils.jjson`:** Работа с JSON.
*   **`src.logger`:** Логирование.
*   **`src.logger.exceptions`:** Обработка специфичных ошибок PrestaShop.

Этот класс `PrestaShop` является основным интерфейсом для работы с API PrestaShop в рамках проекта, обеспечивая CRUD-операции, поиск, загрузку файлов и другие необходимые функции.