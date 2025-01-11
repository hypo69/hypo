## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
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

**1. Создание рекламной кампании:**

   - **Инициализация кампании**:
     - Ввод имени кампании (`campaign_name`), языка (`language`) и валюты (`currency`).
     - *Пример:* `campaign_name = 'example_campaign'`, `language = 'EN'`, `currency = 'USD'`.

   - **Создание директорий**:
     - Функция `create_directories` создает каталоги для кампании и ее категорий.
     - *Пример:* `categories = ['electronics', 'fashion']`, `create_directories(campaign_name, categories)`.

   - **Сохранение конфигурации**:
     - Формируется словарь `campaign_config` и сохраняется с помощью `save_config`.
     - *Пример:* `campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}`, `save_config(campaign_name, campaign_config)`.

   - **Сбор данных о продуктах**:
     - Функция `collect_product_data` собирает данные о продуктах по их URL.
     - *Пример:* `product_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']`, `product_data = collect_product_data(product_urls)`.

   - **Сохранение данных о продуктах**:
     - Функция `save_product_data` сохраняет собранные данные.
     - *Пример:* `save_product_data(campaign_name, product_data)`.

   - **Создание рекламных материалов**:
     - Функция `create_promotional_materials` создает рекламные материалы на основе данных.
     - *Пример:* `create_promotional_materials(campaign_name, product_data)`.

   - **Просмотр и публикация**:
     - Функции `review_campaign` и `publish_campaign` выполняют просмотр и публикацию кампании.
     - *Пример:* `review_campaign(campaign_name)`, `publish_campaign(campaign_name)`.

**2. Редактирование рекламной кампании:**

   - **Загрузка конфигурации**:
     - Функция `load_config` загружает конфигурацию кампании.
     - *Пример:* `campaign_config = load_config(campaign_name)`.

   - **Обновление конфигурации**:
     - Обновление параметров, например, языка.
     - *Пример:* `campaign_config['language'] = 'RU'`, `save_config(campaign_name, campaign_config)`.

   - **Обновление категорий и директорий**:
     - Функция `update_categories` обновляет список категорий и директории.
     - *Пример:* `new_categories = ['home', 'beauty']`, `update_categories(campaign_name, new_categories)`.

   - **Сбор новых данных**:
     - Сбор данных о новых продуктах.
     - *Пример:* `new_product_urls = ['https://www.aliexpress.com/item/789.html']`, `updated_product_data = collect_product_data(new_product_urls)`.

   - **Сохранение обновленных данных**:
     - Функция `save_product_data` сохраняет обновленные данные.
     - *Пример:* `save_product_data(campaign_name, updated_product_data)`.

   - **Обновление рекламных материалов**:
     - Функция `update_promotional_materials` обновляет рекламные материалы.
     - *Пример:* `update_promotional_materials(campaign_name, updated_product_data)`.

   - **Просмотр и публикация**:
     - Просмотр и публикация обновленной кампании.
     - *Пример:* `review_campaign(campaign_name)`, `publish_campaign(campaign_name)`.

**3. Обработка ошибок и логирование**:

   - **Обработка ошибок**:
     - Использование `try-except` блоков для перехвата исключений.
     - *Пример:*
       ```python
       try:
           # Код, который может вызвать ошибку
       except Exception as ex:
           logger.error("Ошибка", ex)
       ```

   - **Логирование событий**:
     - Логирование важных событий и ошибок.
     - *Пример:*
       ```python
       logger.info("Начало обработки кампании")
       logger.error("Ошибка при обработке кампании", ex)
       ```

**Поток данных:**

1.  **Создание:**
    - Инициализация → `create_directories` → `save_config` → `collect_product_data` → `save_product_data` → `create_promotional_materials` → `review_campaign` → `publish_campaign`.
2.  **Редактирование:**
    - `load_config` → Обновление параметров → `save_config` → `update_categories` → `collect_product_data` → `save_product_data` → `update_promotional_materials` → `review_campaign` → `publish_campaign`.

## <mermaid>

```mermaid
flowchart TD
    Start(Начало) --> InitializeCampaign[Инициализация кампании: <br>Имя, язык, валюта]
    InitializeCampaign --> CreateDirectories[Создание директорий: <br><code>create_directories(campaign_name, categories)</code>]
    CreateDirectories --> SaveConfig[Сохранение конфигурации: <br><code>save_config(campaign_name, campaign_config)</code>]
    SaveConfig --> CollectProductData[Сбор данных о продуктах: <br><code>collect_product_data(product_urls)</code>]
    CollectProductData --> SaveProductData[Сохранение данных о продуктах: <br><code>save_product_data(campaign_name, product_data)</code>]
    SaveProductData --> CreatePromotionalMaterials[Создание рекламных материалов: <br><code>create_promotional_materials(campaign_name, product_data)</code>]
    CreatePromotionalMaterials --> ReviewCampaign[Просмотр кампании: <br><code>review_campaign(campaign_name)</code>]
    ReviewCampaign --> PublishCampaign[Публикация кампании: <br><code>publish_campaign(campaign_name)</code>]
    PublishCampaign --> EndCreate(Конец создания)

    StartEdit(Начало редактирования) --> LoadConfig[Загрузка конфигурации: <br><code>load_config(campaign_name)</code>]
    LoadConfig --> UpdateConfig[Обновление конфигурации: <br>Обновление параметров]
    UpdateConfig --> SaveConfigEdit[Сохранение конфигурации: <br><code>save_config(campaign_name, campaign_config)</code>]
    SaveConfigEdit --> UpdateCategories[Обновление категорий: <br><code>update_categories(campaign_name, new_categories)</code>]
    UpdateCategories --> CollectNewProductData[Сбор новых данных о продуктах: <br><code>collect_product_data(new_product_urls)</code>]
    CollectNewProductData --> SaveNewProductData[Сохранение новых данных о продуктах: <br><code>save_product_data(campaign_name, updated_product_data)</code>]
    SaveNewProductData --> UpdatePromotionalMaterials[Обновление рекламных материалов: <br><code>update_promotional_materials(campaign_name, updated_product_data)</code>]
    UpdatePromotionalMaterials --> ReviewCampaignEdit[Просмотр кампании: <br><code>review_campaign(campaign_name)</code>]
    ReviewCampaignEdit --> PublishCampaignEdit[Публикация кампании: <br><code>publish_campaign(campaign_name)</code>]
    PublishCampaignEdit --> EndEdit(Конец редактирования)

    EndCreate -->|Создание| Finish(Конец)
    EndEdit --> |Редактирование| Finish
```

**Объяснение зависимостей:**

- `InitializeCampaign`: Входная точка для создания новой рекламной кампании. Принимает начальные данные, такие как имя, язык и валюту.
- `CreateDirectories`: Функция создает необходимые директории на основе имени кампании и списка категорий.
- `SaveConfig`: Сохраняет конфигурацию кампании, включая имя, язык и валюту в файл.
- `CollectProductData`: Собирает информацию о продуктах на основе URL-адресов.
- `SaveProductData`: Сохраняет собранные данные о продуктах в файл.
- `CreatePromotionalMaterials`: Создает рекламные материалы, используя данные о продуктах.
- `ReviewCampaign`: Позволяет просмотреть кампанию перед публикацией.
- `PublishCampaign`: Публикует кампанию.
- `StartEdit`: Входная точка для редактирования существующей кампании.
- `LoadConfig`: Загружает ранее сохраненную конфигурацию кампании.
- `UpdateConfig`: Обновляет параметры конфигурации кампании, такие как язык.
- `SaveConfigEdit`: Сохраняет обновленную конфигурацию кампании.
- `UpdateCategories`: Обновляет список категорий и соответствующие директории.
- `CollectNewProductData`: Собирает данные о новых продуктах на основе URL-адресов.
- `SaveNewProductData`: Сохраняет новые данные о продуктах.
- `UpdatePromotionalMaterials`: Обновляет рекламные материалы, используя новые данные.
- `ReviewCampaignEdit`: Просмотр обновленной кампании.
- `PublishCampaignEdit`: Публикует обновленную кампанию.
- `EndCreate`:  Конечная точка процесса создания
- `EndEdit`: Конечная точка процесса редактирования
- `Finish`: Конечная точка выполнения

## <объяснение>

**Импорты:**

- В предоставленном коде нет явных импортов, что подразумевает использование функций, определенных в том же модуле, или в глобальном контексте.
- Для обработки ошибок используется `logger`, который, предположительно, импортируется из модуля логирования.
- Отсутствие явных импортов делает код более абстрактным и требует дополнительной информации о реализации функций.

**Классы:**

- В коде нет классов. Вся логика реализована через функции.

**Функции:**

- `create_campaign(campaign_name, language, currency, categories, product_urls)`:
  - **Аргументы**:
    - `campaign_name` (строка): Имя кампании.
    - `language` (строка): Язык кампании.
    - `currency` (строка): Валюта кампании.
    - `categories` (список строк): Список категорий для кампании.
    - `product_urls` (список строк): Список URL-адресов продуктов.
  - **Возвращаемое значение**: Нет явного возвращаемого значения.
  - **Назначение**: Создает новую рекламную кампанию, выполняя шаги инициализации, создания директорий, сохранения конфигурации, сбора и сохранения данных о продуктах, создания рекламных материалов, просмотра и публикации.
  - **Пример**:
    ```python
    create_campaign(
      'summer_sale',
      'EN',
      'USD',
      ['electronics', 'clothing'],
      ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
    )
    ```

- `edit_campaign(campaign_name, language, categories, product_urls)`:
  - **Аргументы**:
    - `campaign_name` (строка): Имя кампании для редактирования.
    - `language` (строка): Новый язык кампании.
    - `categories` (список строк): Новый список категорий.
    - `product_urls` (список строк): Новый список URL-адресов продуктов.
  - **Возвращаемое значение**: Нет явного возвращаемого значения.
  - **Назначение**: Редактирует существующую рекламную кампанию, загружая конфигурацию, обновляя язык, категории, данные о продуктах и рекламные материалы, а также выполняет просмотр и публикацию.
  - **Пример**:
    ```python
    edit_campaign(
      'summer_sale',
      'RU',
      ['home', 'garden'],
      ['https://www.aliexpress.com/item/789.html']
    )
    ```

- Вспомогательные функции (упоминаются в инструкциях, но не определены явно в коде):
  - `create_directories(campaign_name, categories)`: Создает директории для кампании и категорий.
  - `save_config(campaign_name, campaign_config)`: Сохраняет конфигурацию кампании в файл.
  - `collect_product_data(product_urls)`: Собирает данные о продуктах по URL.
  - `save_product_data(campaign_name, product_data)`: Сохраняет данные о продуктах в файл.
  - `create_promotional_materials(campaign_name, product_data)`: Создает рекламные материалы на основе данных о продуктах.
  - `review_campaign(campaign_name)`: Позволяет просмотреть кампанию.
  - `publish_campaign(campaign_name)`: Публикует кампанию.
  - `load_config(campaign_name)`: Загружает конфигурацию кампании из файла.
  - `update_categories(campaign_name, new_categories)`: Обновляет список категорий и директории.
  - `update_promotional_materials(campaign_name, updated_product_data)`: Обновляет рекламные материалы.
  - `logger.info(message)`: Записывает информационное сообщение в лог.
  - `logger.error(message, exception)`: Записывает сообщение об ошибке в лог.

**Переменные:**

- `campaign_name` (строка): Имя кампании.
- `language` (строка): Язык кампании.
- `currency` (строка): Валюта кампании.
- `categories` (список строк): Список категорий для кампании.
- `product_urls` (список строк): Список URL-адресов продуктов.
- `campaign_config` (словарь): Словарь с конфигурацией кампании.
- `product_data` (данные): Данные о продуктах, полученные из URL.
- `updated_product_data` (данные): Обновленные данные о продуктах.
- `new_categories`(список строк): Новый список категорий.
- `new_product_urls` (список строк): Новый список URL-адресов продуктов.

**Потенциальные ошибки и области для улучшения:**

- **Отсутствие явных импортов**: Необходимо явно импортировать модули, такие как `logger` и другие необходимые для работы с файлами или API.
- **Обработка ошибок**: Хотя `try-except` блоки используются, необходимо более подробное логирование ошибок, включая стектрейс, и возможно, более специфичные исключения.
- **Обработка данных**: Код подразумевает, что функции, такие как `collect_product_data` и `save_product_data` корректно работают с данными, но детали реализации отсутствуют.
- **Общая абстракция**: Отсутствие конкретики в реализации вспомогательных функций делает код сложным для понимания.
- **Дублирование кода**: Код создания и редактирования имеет много дублирующихся шагов (сбор данных, сохранение, публикация). Можно выделить общую функцию или использовать паттерн "шаблонный метод".
- **Нет проверки на корректность данных**: Входные данные, такие как URL, имена кампаний, язык и валюта, должны проверяться на корректность.

**Взаимосвязи с другими частями проекта:**

- В контексте проекта, эти инструкции и код будут частью более крупной системы, вероятно, включающей:
    - Модули для работы с API Aliexpress (для сбора данных).
    - Модули для работы с файловой системой (для сохранения конфигурации и данных).
    - Модули для логирования.
    - Модули для генерации и управления рекламными материалами.
    - Пользовательский интерфейс или CLI для запуска процессов.

**Общее заключение:**

Предоставленный код представляет собой набор инструкций и примерный код для создания и редактирования рекламных кампаний. Он описывает последовательность действий, но не предоставляет конкретной реализации. Для более эффективного использования и сопровождения кода требуется явное определение и реализация всех вспомогательных функций, а также подробная обработка ошибок и логирование событий.