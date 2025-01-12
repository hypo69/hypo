## АНАЛИЗ КОДА

### <алгоритм>

1.  **Инициализация `PrestaShopAsync`**:
    *   Принимает `api_domain`, `api_key`, `data_format` (по умолчанию 'JSON') и `debug` (по умолчанию True).
    *   Создаёт сессию `aiohttp.ClientSession` с базовой аутентификацией (используя `api_key`) и таймаутом.

2.  **`ping()`**:
    *   Отправляет `HEAD` запрос на `API_DOMAIN`.
    *   Вызывает `_check_response()` для проверки статуса.

3.  **`_check_response()`**:
    *   Проверяет статус код ответа (`200` или `201`).
    *   Если статус код не соответствует `200` или `201`, вызывает `_parse_response_error()`, и возвращает `False`.
    *   Возвращает `True` при успешном запросе.

4.  **`_parse_response_error()`**:
    *   Обрабатывает ошибки API, анализируя JSON или XML ответы.
    *   Если `data_format` равен JSON, извлекает текст ответа, логирует его и статус код в случае ошибки.
    *   Если `data_format` равен XML, парсит XML и извлекает код ошибки и сообщение, которые также логирует.
    *   Возвращает ответ или кортеж (код, сообщение) в случае ошибки.

5.  **`_prepare()`**:
    *   Подготавливает URL для запроса, добавляя параметры.
    *   Использует `PreparedRequest` из `requests` для корректного формирования URL.

6.  **`_exec()`**:
    *   Выполняет HTTP запрос к PrestaShop API.
    *   Принимает параметры `resource`, `resource_id`, `resource_ids`, `method`, `data`, `headers`, `search_filter`, `display`, `schema`, `sort`, `limit`, `language`, `io_format`
    *   Формирует URL используя `_prepare()`, подготавливает `data` (конвертируя `dict` в `xml` при необходимости).
    *   Если включен режим `debug`, перенаправляет вывод `stderr` в файл `stderr.log`.
    *   Отправляет запрос с использованием `aiohttp.ClientSession`.
    *   Проверяет ответ используя `_check_response()`.
    *   Парсит ответ (JSON или XML) и возвращает результат, используя `_parse()`.

7.  **`_parse()`**:
    *   Парсит ответ API из текста в `dict` (если `data_format` = JSON) или `xml.etree.ElementTree.Element` (если `data_format` = XML).
    *   Возвращает `False` если возникает ошибка парсинга.

8.  **`create()`, `read()`, `write()`, `unlink()`, `search()`**:
    *   Методы-обертки для `_exec()`, предоставляющие высокоуровневые операции CRUD (создание, чтение, обновление, удаление) и поиск ресурсов.

9.  **`create_binary()`**:
    *   Загружает бинарный файл (например, изображение) на API PrestaShop.
    *   Отправляет POST запрос с файловыми данными и заголовком `Content-Type: application/octet-stream`.

10. **`_save()`**:
     *   Сохраняет данные в файл в формате JSON.
     *   Использует `src.utils.file.save_text_file`.
     
11. **`get_data()`**:
    *   Извлекает данные из API и сохраняет их в файл, вызывая `_save()`.

12. **`remove_file()`**:
      *  Удаляет файл по указанному пути.
      *  Логирует ошибку в случае неудачи.
    
13. **`get_apis()`**:
      *  Получает список всех доступных API ресурсов.

14. **`get_languages_schema()`**:
      *  Получает схему языка.
    
15. **`upload_image_async()`/ `upload_image()`**:
     *   Загружает изображение по URL в API PrestaShop.
     *   Использует `src.utils.image.save_image_from_url` для загрузки и сохранения изображения.
     *   Вызывает `create_binary()` для загрузки сохраненного файла на сервер.
     *   Удаляет локальный файл после загрузки, используя `remove_file()`.

16. **`get_product_images()`**:
      * Получает список изображений продукта.

### <mermaid>

```mermaid
flowchart TD
    subgraph PrestaShopAsync
        A[__init__] --> B(ClientSession);
        B --> C[ping()]
        C --> D[_check_response()];
        D --> E{status_code == 200 or 201?}
        E -- Yes --> F(return True)
        E -- No --> G[_parse_response_error()]
        G --> H(return False)
        F --> C
        H --> C

        G --> I{data_format == 'JSON'}
        I -- Yes --> J[log error details]
        J --> K(return response)

        I -- No --> L[_parse(text)]
        L --> M{isinstance(error_answer, dict)}
        M -- Yes --> N[extract code and message]
        M -- No --> O[extract code and message from Element]
        N --> P[log XML error]
        O --> P
        P --> K
        
        A --> Q[_prepare()]
        Q --> R[_exec()]
        R --> S{debug == True}
        S -- Yes --> T[create stderr log, open file]
        T --> U[prepare url, request data]
        S -- No --> U
        
        U --> V(ClientSession.request)
        V --> D
        V --> W{io_format == 'JSON'}
        W -- Yes --> X(response.json())
        W -- No --> Y[_parse(text)]
        X --> R
        Y --> R

        R --> Z[create()]
        Z --> R
        R --> AA[read()]
        AA --> R
        R --> AB[write()]
        AB --> R
        R --> AC[unlink()]
        AC --> R
        R --> AD[search()]
        AD --> R
        
        R --> AE[create_binary()]
        AE --> AF[open file in rb]
        AF --> AG(ClientSession.post)
        AG --> AH(return response.json())
        
        A --> AI[_save()]
        AI --> AJ(save_text_file)

        A --> AK[get_data()]
        AK --> AL[_exec()]
        AL --> AM{data}
        AM -- Yes --> AN[_save()]
        AN --> AO(return data)
        AM -- No --> AP(return False)
        AO --> AK
        AP --> AK

        A --> AQ[remove_file()]
        AQ --> AR(os.remove)
        
        A --> AS[get_apis()]
        AS --> R
        
        A --> AT[get_languages_schema()]
        AT --> AU[_exec()]

        A --> AV[upload_image_async()]
        AV --> AW[save_image_from_url]
        AW --> AX(create_binary)
        AX --> AY[remove_file]

        A --> AZ[get_product_images]
        AZ --> R
    end

    subgraph header.py
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    end
```

**Зависимости `mermaid`:**

*   `PrestaShopAsync`: Основной класс, инкапсулирующий логику взаимодействия с PrestaShop API.
*   `__init__`: Метод инициализации класса.
*   `ClientSession`:  Создание сессии aiohttp для асинхронных запросов.
*   `ping()`:  Метод для проверки доступности API.
*   `_check_response()`: Метод для проверки статуса ответа.
*   `_parse_response_error()`: Метод для обработки ошибок от API.
*   `_prepare()`: Метод для подготовки URL.
*   `_exec()`: Метод для выполнения HTTP запросов.
*   `_parse()`: Метод для разбора ответов API.
*   `create()`: Метод для создания ресурса в API.
*   `read()`: Метод для чтения ресурса из API.
*   `write()`: Метод для обновления ресурса в API.
*   `unlink()`: Метод для удаления ресурса из API.
*   `search()`: Метод для поиска ресурса в API.
*  `create_binary()`: Метод для отправки бинарных данных в API.
*  `_save()`: Метод для сохранения данных в файл.
*  `get_data()`: Метод для загрузки и сохранения данных из API.
*  `remove_file()`: Метод для удаления файла.
*  `get_apis()`: Метод для получения списка доступных API.
*  `get_languages_schema()`: Метод для получения схемы языка.
*  `upload_image_async()`: Метод для асинхронной загрузки изображения.
*  `upload_image()`: Метод для загрузки изображения.
* `get_product_images()`: Метод для получения изображений продукта.

### <объяснение>

**Импорты:**

*   `os`, `sys`:  Стандартные модули Python для работы с операционной системой и системными переменными.
*   `enum.Enum`: Для создания перечислений, в данном случае для форматов данных (JSON, XML).
*   `http.client.HTTPConnection`: Для создания HTTP соединений (используется внутри `requests`).
*   `pathlib.Path`: Для работы с путями файлов.
*   `typing`:  Для статической типизации.
*   `xml.etree.ElementTree`: Для работы с XML.
*   `xml.parsers.expat.ExpatError`: Исключение, которое может возникнуть при парсинге XML.
*   `requests.Session`, `requests.models.PreparedRequest`: Для создания и подготовки HTTP запросов.
*   `header`: Самописный модуль, вероятно, для определения корневой директории проекта и установки глобальных параметров.
*   `src.gs`: Глобальные настройки проекта.
*   `src.logger.exceptions`: Пользовательские исключения для ошибок PrestaShop API.
*   `src.logger.logger`: Модуль логирования.
*   `src.utils.convertors`:  Модули для конвертации данных (base64, dict to xml, xml to dict).
*   `src.utils.file`:  Модуль для работы с файловой системой.
*   `src.utils.image`: Модуль для работы с изображениями.
*   `src.utils.jjson`: Модуль для работы с JSON (возможно, с какими-то кастомными настройками).
*   `src.utils.printer`: Модуль для форматированного вывода.
*  `asyncio`: Модуль для асинхронного программирования.
*   `aiohttp`: Библиотека для асинхронных HTTP запросов.

**Классы:**

*   **`Format(Enum)`**: Перечисление для определения форматов данных (JSON, XML).

*   **`PrestaShopAsync`**:
    *   `client`: Атрибут `aiohttp.ClientSession` для асинхронных запросов.
    *   `debug`: Флаг для отладочного режима.
    *   `lang_index`: Индекс языка по умолчанию.
    *   `data_format`: Формат данных (JSON или XML) по умолчанию.
    *   `ps_version`: Версия PrestaShop.
    *  `API_DOMAIN`: Домен PrestaShop API.
    *  `API_KEY`: Ключ PrestaShop API.
    *   Методы:
        *   `__init__`: Инициализирует класс, устанавливает настройки и создает сессию `aiohttp`.
        *   `ping()`: Проверка доступности API.
        *   `_check_response()`: Проверяет статус ответа и обрабатывает ошибки.
        *   `_parse_response_error()`: Разбирает ошибки API.
        *   `_prepare()`: Подготовка URL.
        *  `_exec()`: Выполнение HTTP запроса.
        *   `_parse()`: Парсинг ответа (JSON или XML).
        *   `create()`: Создание ресурса.
        *   `read()`: Чтение ресурса.
        *   `write()`: Обновление ресурса.
        *   `unlink()`: Удаление ресурса.
        *   `search()`: Поиск ресурсов.
        *   `create_binary()`: Загрузка бинарных данных.
        *   `_save()`: Сохранение данных в файл.
        *   `get_data()`: Получение и сохранение данных.
        *  `remove_file()`: Удаление файла.
        *  `get_apis()`: Получение списка доступных API.
        *  `get_languages_schema()`: Получение схемы языка.
        *  `upload_image_async()`: Загрузка изображения асинхронно.
        *   `upload_image()`: Загрузка изображения.
        *   `get_product_images()`: Получение списка изображений продукта.

**Функции:**

*   Все методы класса `PrestaShopAsync` описаны выше.

**Переменные:**

*   `API_DOMAIN`, `API_KEY`: Строки для хранения URL API и ключа API.
*   `client`: Экземпляр `aiohttp.ClientSession`.
*   `debug`: Булево значение для отладочного режима.
*   `lang_index`: Целое число, индекс языка по умолчанию.
*   `data_format`: Строка, формат данных (JSON или XML).
*   `ps_version`: Строка, версия PrestaShop.

**Потенциальные ошибки и области для улучшения:**

*   Обработка ошибок в `_parse_response_error()` для XML ответов может быть улучшена. Сейчас код предполагает наличие элементов `code` и `message`, но XML может варьироваться.
*   В методе `_exec()` можно добавить retry logic для временных ошибок сети.
*   В методах `upload_image_async` и `upload_image` не используется `url_without_extension`.
*   В методе `_prepare` не обрабатывается случай с отсутствующими `params`.
*   Метод `_parse` возвращает `False` при ошибке парсинга, что может привести к последующим ошибкам. Желательно было бы возвращать более конкретные исключения.
*  Метод `_save` использует `j_dumps` с `ensure_ascii=False`, что может вызвать проблемы с unicode при работе с разными системами.
*  Метод `upload_image` дублирует логику метода `upload_image_async`.
*  В методе `_exec` открывается файл для записи `stderr` при каждом запросе, это не эффективно, логику лучше перенести в `__init__` и закрывать по завершению работы класса.

**Взаимосвязи с другими частями проекта:**

*   Использует `header` для определения корня проекта.
*   Использует `src.gs` для глобальных настроек.
*   Использует `src.logger` для логирования.
*   Использует утилиты из `src.utils` для конвертации, работы с файлами, изображениями и JSON.

Этот анализ обеспечивает полное представление о функциональности кода, его архитектуре и взаимодействиях с другими частями проекта.