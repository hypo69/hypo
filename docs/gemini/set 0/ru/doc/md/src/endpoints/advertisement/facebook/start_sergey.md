# Модуль `hypotez/src/endpoints/advertisement/facebook/start_sergey.py`

## Обзор

Модуль `start_sergey.py` отвечает за запуск рекламных кампаний на Facebook для аккаунтов рекламодателей.  Он определяет параметры кампаний, включая язык, валюту и целевые группы, загружает данные из файлов JSON и использует `FacebookPromoter` для отправки объявлений. Модуль предусматривает циклический запуск кампаний с периодическими задержками и обработкой исключений.

## Определения

### Переменные

```python
MODE = 'dev'
```

**Описание**:  Переменная, хранящая режим работы (например, 'dev' или 'prod').


### Список путей к файлам

```python
group_file_paths_ru: list[str] = ["sergey_pages.json"]
adv_file_paths_ru: list[str] = ["ru_ils.json"]
group_file_paths_he: list[str] = ["sergey_pages.json"]
adv_file_paths_he: list[str] = ["he_ils.json"]
group_categories_to_adv = ['sales', 'biz']
```

**Описание**:  Список путей к файлам с данными о группах и рекламными объявлениями для разных языков (русский и иврит). `group_categories_to_adv` - список категорий для рекламных объявлений.


## Функции

### `run_campaign`

**Описание**: Запускает рекламную кампанию для заданных параметров.

**Параметры**:

- `d` (Driver): Экземпляр драйвера веб-драйвера.
- `promoter_name` (str): Имя рекламодателя.
- `campaigns` (list): Список названий кампаний.
- `group_file_paths` (list): Пути к файлам с данными о группах.
- `language` (str): Язык рекламной кампании.
- `currency` (str): Валюта рекламной кампании.

**Возвращает**:
  - Не определено.

**Вызывает исключения**:
  Возможны исключения, генерируемые классом `FacebookPromoter`.


### `campaign_cycle`

**Описание**: Цикл для управления запуском кампаний с разными языками и валютами.

**Параметры**:

- `d` (Driver): Экземпляр драйвера веб-драйвера.

**Возвращает**:
  - `True`: Указывает на успешное завершение цикла.

**Вызывает исключения**:
  Возможны исключения, генерируемые при работе с файлами и `run_campaign`.


### `main`

**Описание**: Основная функция для запуска рекламных кампаний.

**Параметры**:
  Нет.

**Возвращает**:
  - Не определено.

**Вызывает исключения**:

- `KeyboardInterrupt`:  Исключение, генерируемое при прерывании пользователем процесса. В этом случае происходит логирование.


## Примечания

- Модуль использует несколько внешних библиотек (`header`, `random`, `time`, `copy`, `Path`, `gs`, `get_directory_names`, `get_filenames`, `Driver`, `Chrome`, `FacebookPromoter`, `logger`, `interval`).
-  Предполагается, что `FacebookPromoter` и `Driver` реализованы в других модулях и обладают соответствующими методами и свойствами.
- Логирование осуществляется с использованием `logger.debug` и `logger.info`.
-  В `campaign_cycle` реализован цикл обработки разных языков и валют с использованием `language_currency_pairs`.
- В коде присутствуют `...` для обозначения неполных или предполагаемых участков кода.


```