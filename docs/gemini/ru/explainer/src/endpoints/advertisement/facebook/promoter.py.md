## <алгоритм>

1.  **Инициализация `FacebookPromoter`**:
    *   Создается экземпляр класса `FacebookPromoter` с передачей `Driver`, имени промоутера (`promoter`), путей к файлам групп (`group_file_paths`) и флага отключения видео (`no_video`).
    *   Если `group_file_paths` не указан, то используется путь по умолчанию из `gs.path.google_drive`.
2.  **`promote`**:
    *   Метод `promote` принимает информацию о группе (`group`), продвигаемый элемент (`item`, может быть событием или категорией) и флаг `is_event`, определяющий тип продвижения.
    *   Проверяется соответствие языка и валюты группы с переданными параметрами (`language`, `currency`).
    *   Если `is_event` равно `True`, то устанавливаются атрибуты события и вызывается функция `post_event` для публикации события.
    *   Если `is_event` равно `False`, то вызывается функция `post_ad` (если промоутер kazarinov или emil) или `post_message` для публикации сообщения (категории).
    *   В конце вызывается функция `update_group_promotion_data` для обновления данных о продвижении группы.

    _Пример:_
    *   `promote(group=group_data, item=event_data, is_event=True)` - опубликует событие
    *   `promote(group=group_data, item=category_data, is_event=False)` - опубликует сообщение (категорию)

3. **`log_promotion_error`**:
    *   Метод `log_promotion_error` записывает в лог ошибку при публикации события или категории.

4.  **`update_group_promotion_data`**:
    *   Обновляет данные о последнем продвижении группы, записывая текущую дату и время, а также добавляя название продвигаемой категории или события в список.

5.  **`process_groups`**:
    *   Перебирает все файлы групп из `group_file_paths`.
    *   Загружает данные из файла JSON в виде пространства имен (`SimpleNamespace`).
    *   Проверяет интервал между публикациями для группы (`check_interval`).
    *   Проверяет, входит ли категория группы в список продвигаемых категорий (`group_categories_to_adv`) и является ли статус группы активным.
    *   Если `is_event` равен `True`, выбирается случайное событие из списка `events`. Если нет - вызывается метод `get_category_item` для получения продвигаемой категории.
    *   Проверяет, не было ли данное событие или категория уже опубликована в данной группе.
    *   Проверяет соответствие языка и валюты группы.
    *   Открывает URL группы в браузере.
    *   Вызывает метод `promote` для публикации.
    *   Обновляет JSON-файл с данными группы.
    *   Делает случайную паузу.

    _Пример:_
    *   `process_groups(campaign_name='summer_sales', group_file_paths=['groups_1.json'], group_categories_to_adv=['sales'])` - обработает файл groups_1.json с продвижением категорий из `summer_sales`, включая только группы с категориями sales
    *   `process_groups(events=[event1, event2], is_event=True, group_file_paths=['groups_1.json'])` - обработает файл groups_1.json и опубликует события event1 и event2

6.  **`get_category_item`**:
    *   В зависимости от промоутера (`self.promoter`), получает данные о категории для продвижения.
    *   Если промоутер `aliexpress`, использует класс `AliCampaignEditor` для получения данных о категории и товарах.
    *   Для других промоутеров загружает данные из JSON-файла кампании и читает описание из текстового файла.
    *   Выбирает первое изображение из папки с изображениями категории.

    _Пример:_
    *   `get_category_item(campaign_name='summer_sales', group=group_data)` - возвращает категорию из кампании `summer_sales`

7.  **`check_interval`**:
    *   Проверяет, прошло ли достаточно времени с момента последней публикации в группе.

8.  **`validate_group`**:
    *   Проверяет, что данные группы корректны и имеют необходимые атрибуты (`group_url`, `group_categories`).

## <mermaid>

```mermaid
graph TD
    A[FacebookPromoter Initialization] --> B{group_file_paths?};
    B -- Yes --> C[Use Provided group_file_paths];
    B -- No --> D[Get default group_file_paths];
    C --> E[Set Attributes];
    D --> E;
    E --> F{promote()};
    F --> G{is_event?};
    G -- Yes --> H[Set event attributes];
    H --> I[post_event()];
    G -- No --> J{promoter in ['kazarinov', 'emil']?};
    J -- Yes --> K[post_ad()];
    J -- No --> L[post_message()];
    I --> M{update_group_promotion_data()};
    K --> M;
    L --> M;
    M --> N[Return True];
    
    O[process_groups()] --> P{campaign_name or events?};
    P -- Yes --> Q[Iterate through group_file_paths];
    P -- No --> R[Log 'Nothing to promote'];
    Q --> S[Load group data from JSON];
    S --> T[Iterate through groups];
    T --> U{check_interval()?};
    U -- No --> T;
    U -- Yes --> V{group_categories_to_adv intersection?};
    V -- No --> T;
    V -- Yes --> W{is_event?};
    W -- Yes --> X[Randomly select event];
    W -- No --> Y[get_category_item()];
    X --> Z{item already promoted?};
    Y --> Z
    Z -- Yes --> T;
    Z -- No --> AA{group.language == language? and group.currency == currency?};
     AA -- No --> T;
    AA -- Yes --> AB[Open group URL];
    AB --> AC[promote()];
    AC --> AD[Update group data];
    AD --> AE[Sleep];
     AE --> T;

    
    AF[get_category_item()] --> AG{promoter == 'aliexpress'?};
    AG -- Yes --> AH[AliCampaignEditor()] ;
    AH --> AI[Get category data and products];
    AI --> AJ[Return item];
    AG -- No --> AK[Load campaign data];
    AK --> AL[Read category description];
    AL --> AM[Get first image];
    AM --> AJ;

    
    
   
    
    

    
    
    

    
    
    
    
    
    

```

## <объяснение>

### Импорты:

*   `random`: Используется для генерации случайных значений, например, для перемешивания списка событий и для выбора случайной паузы после публикации.
*   `datetime`, `timedelta`: Используется для работы с датой и временем, в частности для записи времени последней публикации.
*   `pathlib.Path`: Используется для представления путей к файлам и директориям в файловой системе.
*   `urllib.parse.urlencode`: Используется для кодирования параметров URL.
*   `types.SimpleNamespace`: Используется для создания объектов с атрибутами, которые могут быть добавлены динамически (удобно для хранения данных из JSON).
*   `typing.Optional`: Используется для обозначения необязательных параметров в функциях.

Из `src`:

*   `gs`: Модуль с глобальными настройками и путями проекта.
*   `src.endpoints.advertisement.facebook`:  Пакет, содержащий специфичные для Facebook функции.
*   `src.webdriver.driver.Driver`: Класс для управления веб-драйвером браузера.
*   `src.suppliers.aliexpress.campaign.AliCampaignEditor`: Класс для работы с кампаниями AliExpress.
*   `src.endpoints.advertisement.facebook.scenarios`: Модуль со сценариями постинга в Facebook.
*   `src.utils.file`: Модуль с функциями для работы с файлами.
*   `src.utils.jjson`: Модуль для работы с JSON файлами.
*   `src.utils.cursor_spinner`: Модуль для отображения спиннера в консоли.
*   `src.logger.logger`: Модуль для логирования событий.

**Взаимосвязь с другими пакетами `src`**:
    *   Используются модули для работы с веб-драйвером (`src.webdriver`), файловой системой (`src.utils.file`, `src.utils.jjson`), поставщиками (`src.suppliers`), логированием (`src.logger`) и глобальными настройками (`src.gs`). Это демонстрирует модульную структуру проекта.

### Классы:

*   **`FacebookPromoter`**:
    *   **Роль**: Класс, отвечающий за автоматизацию продвижения товаров и событий в группах Facebook. Он использует `Driver` для управления браузером.
    *   **Атрибуты**:
        *   `d`: Экземпляр класса `Driver` для управления браузером.
        *   `group_file_paths`: Путь к файлу или списку файлов с информацией о группах.
        *   `no_video`: Флаг, отключающий использование видео в публикациях.
        *   `promoter`: Имя промоутера (например, 'aliexpress', 'kazarinov').
        *   `spinner`: Объект для отображения спиннера загрузки.
    *   **Методы**:
        *   `__init__`: Инициализация объекта `FacebookPromoter`.
        *   `promote`: Публикует категорию или событие в группе.
        *  `log_promotion_error`: Записывает ошибку при публикации в лог.
        *   `update_group_promotion_data`: Обновляет информацию о последней публикации группы.
        *   `process_groups`: Основной метод, который перебирает группы и запускает процесс публикации.
        *   `get_category_item`: Получает данные о категории для публикации.
        *  `check_interval`: Проверяет интервал между публикациями для группы.
        *   `validate_group`: Проверяет корректность данных группы.

**Взаимодействие с другими компонентами проекта**:
*   Использует `Driver` из `src.webdriver` для управления браузером.
*   Использует `AliCampaignEditor` из `src.suppliers.aliexpress` для получения данных для Aliexpress.
*   Использует функции из `src.utils` для работы с файлами и JSON.
*   Использует `post_message`, `post_event`  `post_message_title` `upload_post_media` и `message_publish` из `src.endpoints.advertisement.facebook.scenarios` для публикации сообщений и событий.

### Функции:

*   **`get_event_url(group_url: str) -> str`**:
    *   **Аргументы**:
        *   `group_url`: URL группы Facebook.
    *   **Возвращаемое значение**: URL для создания события в указанной группе.
    *   **Назначение**: Формирует URL для создания события в Facebook, заменяя `group_id` в базовом URL.
        
    *   **Пример**:
        *   `get_event_url("https://www.facebook.com/groups/123456789/")` вернёт `"https://www.facebook.com/events/create/?acontext=...&dialog_entry_point=group_events_tab&group_id=123456789"`

### Переменные:

*   `MODE`: Строка, устанавливающая режим работы (например, 'dev').
*   `d`: экземпляр класса `Driver` (используется как атрибут класса).
*   `group_file_paths`: Путь к файлу или списку файлов, содержащих данные о группах.
*   `no_video`: Флаг, указывающий, следует ли публиковать сообщения с видео или нет.
*   `promoter`: Имя промоутера.

**Типы и использование**:
*   Большинство переменных являются строками (`str`) или `Path`, либо экземплярами `SimpleNamespace`, что позволяет гибко хранить данные.
*   `no_video` — логическая переменная (`bool`).
*   Используются для хранения конфигураций, путей к файлам и состояний промоутера.

### Потенциальные ошибки и области для улучшения:

*   **Обработка ошибок**: В коде есть `try...except` блоки, но они не всегда обрабатывают исключения конкретно (например, просто `except:` без указания типа исключения).
*   **Логирование**: Логирование ошибок могло бы быть более детализированным, включая больше информации о контексте ошибки.
*   **Модульность**:  Можно выделить больше логики в отдельные методы или классы для повышения читаемости и переиспользования кода.
*   **Использование констант**: Магические строки (например, `'sales'`, `'active'`) можно было бы вынести в константы для лучшей читаемости и простоты обслуживания.
*   **Проверка типов**: В некоторых местах кода явно проверяется тип переменной `isinstance(group.promoted_events, list)`, что указывает на возможные проблемы в структуре данных.

### Цепочка взаимосвязей с другими частями проекта:

1.  **`src.endpoints.advertisement.facebook.promoter.FacebookPromoter`** зависит от:
    *   **`src.webdriver.driver.Driver`**: Для управления браузером.
    *   **`src.suppliers.aliexpress.campaign.AliCampaignEditor`**: Для работы с кампаниями AliExpress.
    *   **`src.endpoints.advertisement.facebook.scenarios`**: Для выполнения сценариев постинга (например, `post_message`, `post_event`).
    *   **`src.utils.file`, `src.utils.jjson`**: Для работы с файлами и JSON.
    *   **`src.logger.logger`**: Для логирования событий.
    *   **`src.gs`**: Для доступа к глобальным настройкам и путям.

2.  `FacebookPromoter` использует эти компоненты для выполнения своей основной функции - автоматизированного продвижения в группах Facebook.
3.  Данные о группах, категориях и событиях хранятся в файлах (JSON, TXT), к которым обращается `FacebookPromoter` через модули `src.utils.file` и `src.utils.jjson`.
4.  Логирование событий происходит с помощью `src.logger.logger`, что позволяет отслеживать работу системы.

Таким образом, `FacebookPromoter` является центральным компонентом в подсистеме продвижения в Facebook, который координирует работу множества других модулей и классов.