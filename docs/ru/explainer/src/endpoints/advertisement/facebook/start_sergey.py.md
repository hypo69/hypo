## <алгоритм>

1.  **Начало:** Запускается функция `main()`.
2.  **Инициализация драйвера:**
    *   Создается экземпляр драйвера `Driver` с типом `Chrome`.
    *   Драйвер открывает страницу Facebook (`https://facebook.com`).
    *   Устанавливается флаг `aliexpress_adv = True` (используется в более старой версии кода, но в данной не используется).
3.  **Бесконечный цикл:**
    *   Проверяется, если наступило время ночного сна (`interval()`).
        *   Если время сна, выводится сообщение "Good night!", и поток засыпает на 1000 секунд.
    *   Запускается функция `campaign_cycle(d)`, передавая ей экземпляр драйвера.
4.  **Функция `campaign_cycle(d)`:**
    *   Создаются копии путей к файлам групп (`group_file_paths_ru` и `group_file_paths_he`) и добавляются к ним пути к файлам объявлений (`adv_file_paths_ru` и `adv_file_paths_he`).
        *   Пример: `file_paths_ru` = `['sergey_pages.json', 'ru_ils.json']`
    *   Создается список словарей `language_currency_pairs`, содержащий пары "язык-валюта".
        *   Пример: `language_currency_pairs = [{"HE": "ILS"}, {"RU": "ILS"}]`
    *   Цикл по `language_currency_pairs`:
        *   Извлекается пара `language` и `currency` из словаря.
            *   Пример: `language = "HE", currency = "ILS"`
        *   Определяется `group_file_paths` на основе значения `language`:
            *   Если `language` == "RU", то `group_file_paths` = `file_paths_ru`, иначе `file_paths_he`.
        *   Определяется список кампаний `campaigns` на основе `language`.
             *   Пример: `campaigns = ["kazarinov_ru"]` если `language = "RU"`
        *   Цикл по `campaigns`:
            *   Запускается функция `run_campaign()`.
                *   Пример: `run_campaign(d, 'kazarinov', 'kazarinov_ru', group_file_paths, 'RU', 'ILS')`
        *    Список кампаний  `campaigns` обновляется.
             *  `campaigns` = `get_directory_names(gs.path.google_drive / 'aliexpress' / 'campaigns')`
        *   Запускается функция `run_campaign()`.
             *    Пример: `run_campaign(d, 'aliexpress', campaigns, group_file_paths, 'HE', 'ILS')`
5.  **Функция `run_campaign()`:**
    *   Создается экземпляр `FacebookPromoter`.
        *   Пример: `promoter = FacebookPromoter(d, promoter='kazarinov')`
    *   Вызывается метод `promoter.run_campaigns()`.
        *   Метод получает данные о кампаниях, путях к файлам групп, категориях групп, языке и валюте, и запускает рекламные кампании.
6.  **Завершение цикла `campaign_cycle()`:** Функция возвращает `True`.
7.  **Логирование и задержка:**
    *   Выводится отладочное сообщение в лог.
    *   Генерируется случайное число от 30 до 360 секунд.
    *   Поток засыпает на это количество секунд.
8.  **Обработка прерывания:** Если возникает прерывание с клавиатуры, выводится сообщение об этом в лог.
9.  **Конец:** Если не возникает прерывание, процесс продолжается бесконечно, повторяя шаги 3-8.

## <mermaid>

```mermaid
flowchart TD
    Start(Начало) --> InitializeDriver[Инициализация драйвера: <br><code>Driver(Chrome)</code>]
    InitializeDriver --> OpenFacebook[Открыть страницу Facebook <br><code>d.get_url("https://facebook.com")</code>]
    OpenFacebook --> StartMainLoop[Начало бесконечного цикла]
    StartMainLoop --> CheckInterval{Проверка времени сна <br><code>interval()</code>}
    CheckInterval -- Да --> SleepForNight[Сон: <br><code>time.sleep(1000)</code>]
    SleepForNight --> StartMainLoop
    CheckInterval -- Нет --> CallCampaignCycle[Вызов <code>campaign_cycle(d)</code>]
    CallCampaignCycle --> CycleStart[Начало цикла <code>campaign_cycle(d)</code>]

    CycleStart --> CreateFilePaths[Создание путей к файлам:<br><code>file_paths_ru = ...</code><br><code>file_paths_he = ...</code>]
    CreateFilePaths --> LanguageCurrencyLoop[Цикл по парам язык-валюта:<br><code>language_currency_pairs</code>]

    LanguageCurrencyLoop --> GetLanguageCurrency{Получение языка и валюты}
    GetLanguageCurrency --> DetermineGroupPaths{Определение путей к файлам групп <br><code>group_file_paths</code>}
    DetermineGroupPaths --> DetermineCampaigns{Определение списка кампаний:<br><code>campaigns</code>}

    DetermineCampaigns --> CampaignLoopStart[Начало цикла по кампаниям]
    CampaignLoopStart --> CallRunCampaign[Вызов <code>run_campaign(d, 'kazarinov', c, ...)</code>]
    CallRunCampaign --> CampaignLoopEnd{Конец цикла по кампаниям?}
    CampaignLoopEnd -- Нет --> CampaignLoopStart
    CampaignLoopEnd -- Да --> GetAliexpressCampaigns[Получение кампаний из AliExpress <br><code>get_directory_names(...)</code>]

    GetAliexpressCampaigns --> CallRunCampaignAli[Вызов <code>run_campaign(d, 'aliexpress', campaigns, ...)</code>]
    CallRunCampaignAli --> LanguageCurrencyLoopEnd{Конец цикла по <br>язык-валютным парам?}
    LanguageCurrencyLoopEnd -- Нет --> LanguageCurrencyLoop
    LanguageCurrencyLoopEnd -- Да --> CycleEnd[Конец цикла <code>campaign_cycle(d)</code>]
    CycleEnd --> MainLoopLog[Логирование и задержка <br><code>logger.debug(...)</code><br><code>time.sleep(t)</code>]
    MainLoopLog --> StartMainLoop
    StartMainLoop --> KeyboardInterrupt{Прерывание с клавиатуры?}
    KeyboardInterrupt -- Да --> LogInterrupt[Логирование прерывания]
    LogInterrupt --> End(Конец)
    KeyboardInterrupt -- Нет --> StartMainLoop

    subgraph "run_campaign(d, promoter_name, campaigns, group_file_paths, language, currency)"
        run_campaign_start[Начало] --> create_promoter[Создание экземпляра <br><code>FacebookPromoter</code>]
        create_promoter --> run_campaigns_method[Вызов метода <code>run_campaigns()</code>]
        run_campaigns_method --> run_campaign_end[Конец]
        
    end
     CallRunCampaign --> run_campaign_start
     CallRunCampaignAli --> run_campaign_start

     subgraph "header.py"
        flowchart TD
            Start_header[Начало] --> Header[<code>header.py</code><br> Determine Project Root]

            Header --> import_gs[Import Global Settings: <br><code>from src import gs</code>]
            import_gs --> End_header[Конец]
        end
```

## <объяснение>

### Импорты:
*   `import header`: Импортирует модуль `header.py`, предположительно, для определения корня проекта и настройки глобальных переменных, таких как пути к файлам.  `header.py` обычно отвечает за настройку путей проекта и глобальных переменных. Этот импорт позволяет всему проекту знать, где находится корень и как получить доступ к другим частям проекта.
*   `import random`:  Используется для генерации случайных чисел, например, для задержки между циклами рекламных кампаний.
*   `import time`: Используется для работы со временем, например, для задержки выполнения программы и для получения текущего времени.
*   `import copy`: Используется для создания копий списков и других объектов, чтобы избежать изменения исходных данных.
*   `from pathlib import Path`:  Используется для работы с путями к файлам и директориям.
*   `from src import gs`: Импортирует глобальные настройки проекта, такие как пути к директориям, настройки API и т. д. Переменная `gs` скорее всего хранит глобальные настройки, определенные в `header.py`.
*   `from src.utils.file import get_directory_names, get_filenames`: Импортирует функции для работы с файловой системой, включая получение списка имен директорий и файлов.
*   `from src.webdriver.driver import Driver, Chrome`: Импортирует классы для управления браузером через WebDriver.  `Driver` является базовым классом, а `Chrome` — его конкретной реализацией для браузера Chrome.
*   `from src.endpoints.advertisement.facebook import FacebookPromoter`: Импортирует класс, отвечающий за запуск рекламных кампаний в Facebook.
*   `from src.logger.logger import logger`: Импортирует объект для логирования событий и ошибок.
*   `from src.utils.date_time import interval`: Импортирует функцию для определения интервала времени, например, для ночного отдыха.

### Переменные:

*   `group_file_paths_ru`: Список путей к файлам, содержащим информацию о группах для русскоязычных кампаний.
*   `adv_file_paths_ru`: Список путей к файлам с объявлениями для русскоязычных кампаний.
*   `group_file_paths_he`: Список путей к файлам, содержащим информацию о группах для ивритоязычных кампаний.
*    `adv_file_paths_he`: Список путей к файлам с объявлениями для ивритоязычных кампаний.
*   `group_categories_to_adv`: Список категорий групп, в которых размещаются объявления (`'sales'`, `'biz'`).
*   `language_currency_pairs`: Список словарей, где ключи - это язык, а значение - валюта.
*   `d`: Экземпляр класса `Driver`, используемый для управления браузером.
*  `aliexpress_adv`: Флаг для определения рекламодателя (устаревшее).

### Функции:

*   `run_campaign(d, promoter_name, campaigns, group_file_paths, language, currency)`:
    *   **Аргументы**:
        *   `d`: Экземпляр драйвера браузера.
        *   `promoter_name`: Имя рекламодателя (например, "kazarinov" или "aliexpress").
        *   `campaigns`: Список или строка с названием кампании(й).
        *   `group_file_paths`: Список путей к файлам с группами для продвижения.
        *   `language`: Язык рекламной кампании.
        *   `currency`: Валюта рекламной кампании.
    *   **Назначение**: Запускает рекламные кампании через объект `FacebookPromoter`. Создает экземпляр `FacebookPromoter` и вызывает его метод `run_campaigns`.
    *  **Пример**: `run_campaign(d, 'kazarinov', 'kazarinov_ru', ['sergey_pages.json'], 'RU', 'ILS')`
*   `campaign_cycle(d)`:
    *   **Аргументы**:
        *   `d`: Экземпляр драйвера браузера.
    *   **Назначение**: Управляет циклом запуска кампаний. Проходит по парам язык-валюта, определяет пути к файлам групп и запускает `run_campaign` для каждой кампании.
    * **Пример**: `campaign_cycle(d)`
*   `main()`:
    *   **Аргументы**: Нет.
    *   **Назначение**: Основная функция для запуска рекламных кампаний. Создает драйвер, запускает бесконечный цикл, вызывает `campaign_cycle`, делает паузы и логгирует события.
    *  **Пример**: `main()`

### Классы:

*   `Driver`:
    *   **Роль**: Абстрактный класс для управления браузером.
    *   **Методы**: `get_url()` для открытия страницы.
*   `Chrome`:
    *   **Роль**: Конкретная реализация класса `Driver` для браузера Chrome.
*  `FacebookPromoter`:
    *   **Роль**: Класс, отвечающий за запуск рекламных кампаний на Facebook.
    *   **Методы**: `run_campaigns()` для запуска рекламных кампаний.
*  **logger**:
    *  **Роль**: Класс для логгирования событий и ошибок.
    *   **Методы**: `debug()`, `info()`.

### Цепочка взаимосвязей:

1.  `main()` инициализирует `Driver` и вызывает `campaign_cycle()`.
2.  `campaign_cycle()`  обрабатывает кампании и вызывает `run_campaign()` для каждой из них.
3.  `run_campaign()` создает экземпляр `FacebookPromoter`, который запускает рекламные кампании, используя информацию о группах и объявлениях.
4.  `logger` используется для логгирования событий во всех частях программы.
5.  Функция `interval()` из `src.utils.date_time` используется для контроля ночного сна.
6.  `get_directory_names()` используется для получения списка директорий из Google Drive.

### Потенциальные ошибки и области для улучшения:

1.  **Обработка ошибок:** Код не имеет явной обработки ошибок внутри `campaign_cycle` и `run_campaign`. Необходимо добавить блоки `try-except` для обработки исключений, таких как ошибки при загрузке файлов или при взаимодействии с веб-страницей.
2.  **Управление драйвером:** Код не закрывает драйвер в случае завершения программы (кроме `KeyboardInterrupt`), что может привести к утечкам ресурсов. Нужно добавить `d.quit()` в блок `finally`, чтобы гарантировать закрытие драйвера.
3.  **Настройка:** Пути к файлам, рекламным кампаниям и другие параметры должны быть вынесены в конфигурационный файл.
4.  **Гибкость**: Код жестко привязан к двум языкам ("RU", "HE") и двум рекламодателям ("kazarinov" и "aliexpress"). Нужно сделать код более гибким, чтобы легко было добавить другие языки и кампании.
5. **Устаревший флаг**: Переменная `aliexpress_adv` устанавливается в значение `True`, но нигде не используется. Она должна быть удалена из кода.

Этот анализ предоставляет подробное понимание функциональности и взаимосвязей в предоставленном коде.