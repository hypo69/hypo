# Модуль `hypotez/src/endpoints/advertisement/facebook/start_sergey.py`

## Обзор

Этот модуль отвечает за запуск рекламных кампаний в Facebook для разных рекламодателей.  Он использует драйвер веб-драйвера, данные из файлов JSON и библиотеку для работы с датами. Модуль включает цикл для периодического запуска кампаний и логирования.

## Определение переменных

### `MODE`

**Описание**: Переменная, определяющая режим работы (например, 'dev', 'prod').

### `group_file_paths_ru`, `adv_file_paths_ru`, `group_file_paths_he`, `adv_file_paths_he`

**Описание**: Список путей к файлам с данными о группах и рекламных объявлениях для русского и ивритского языков.

### `group_categories_to_adv`

**Описание**: Список категорий групп, в которых будут размещаться рекламные объявления.


## Функции

### `run_campaign`

**Описание**: Запускает рекламную кампанию.

**Параметры**:
- `d` (Driver): Экземпляр драйвера веб-браузера.
- `promoter_name` (str): Имя рекламодателя.
- `campaigns` (list): Список наименований кампаний.
- `group_file_paths` (list): Список путей к файлам с данными о группах.
- `language` (str): Язык рекламной кампании.
- `currency` (str): Валюта рекламной кампании.

**Возвращает**:
- Нет значения возврата.

**Вызывает исключения**:
- Нет.


### `campaign_cycle`

**Описание**: Цикл для управления запуском нескольких рекламных кампаний.

**Параметры**:
- `d` (Driver): Экземпляр драйвера веб-браузера.

**Возвращает**:
- `bool`: Значение `True`, если цикл завершился успешно.

**Вызывает исключения**:
- Нет.

### `main`

**Описание**: Основная функция для запуска всего процесса запуска рекламных кампаний.

**Параметры**:
- Нет

**Возвращает**:
- Нет значения возврата.

**Вызывает исключения**:
- `KeyboardInterrupt`: При прерывании пользователем.


## Использование

Модуль запускается вызовом функции `main()`.  Он инициализирует драйвер, устанавливает URL Facebook и запускает цикл кампаний `campaign_cycle`.  Цикл обрабатывает различные языки и валюты, определяя соответствующие файлы с данными и запуская `run_campaign` для каждой кампании. Процесс будет повторяться периодически, с задержкой, заданной случайным числом от 30 до 360 секунд.


## Замечания

- Модуль использует логирование.
- Логирование может быть настроенно в модуле `logger.py`
- Для работы модуля требуется наличие установленных библиотек (header, random, time, copy, pathlib, gs, Driver, Chrome, FacebookPromoter).
- Используется подход обработки исключений `ex` вместо `e`.
- Модуль предполагает наличие необходимых данных в файлах JSON, указанных в `group_file_paths_*` и `adv_file_paths_*`.
- Должны быть определены `gs.path.google_drive`.