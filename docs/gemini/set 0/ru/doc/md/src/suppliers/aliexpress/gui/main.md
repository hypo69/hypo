# Модуль `hypotez/src/suppliers/aliexpress/gui/main.py`

## Обзор

Данный модуль предоставляет главный интерфейс приложения для управления рекламными кампаниями на AliExpress. Модуль построен на основе PyQt6 и использует асинхронные операции.  Он содержит класс `MainApp`, реализующий главное окно приложения с вкладками для редактирования JSON-файлов, управления кампаниями и продуктами.

## Оглавление

* [Классы](#классы)
    * [`MainApp`](#class-mainapp)
* [Функции](#функции)
    * [`main`](#function-main)

## Классы

### `MainApp`

**Описание**: Главный класс приложения, представляющий собой главное окно с вкладками.

**Методы**:

#### `__init__`

**Описание**: Инициализирует приложение с созданием главного окна и вкладок для различных операций.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.


#### `create_menubar`

**Описание**: Создает главное меню приложения с опциями для работы с файлами (открытие, сохранение, выход) и редактированием.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.


#### `open_file`

**Описание**: Открывает диалоговое окно для выбора и загрузки JSON-файла. Загружает файл в соответствующую вкладку в зависимости от текущей выбранной вкладки.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.


#### `save_file`

**Описание**: Сохраняет текущий файл в зависимости от выбранной вкладки.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.


#### `exit_application`

**Описание**: Закрывает приложение.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.


#### `copy`

**Описание**: Копирует выделенный текст в буфер обмена.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.

**Возможные исключения**:
  - `Exception`: Возникает, если нет выделенного текста в виджете.


#### `paste`

**Описание**: Вставляет текст из буфера обмена.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.


**Возможные исключения**:
  - `Exception`: Возникает, если нет активного виджета для вставки текста.


#### `load_file`

**Описание**: Загружает JSON-файл в приложение.

**Параметры**:
  - `campaign_file` (str): Путь к загружаемому JSON-файлу.

**Возвращает**:
  - Не возвращает значения.

**Возможные исключения**:
  - `Exception`: Возникает при ошибке загрузки файла.


## Функции

### `main`

**Описание**: Инициализирует и запускает приложение.

**Параметры**:
  - Не принимает параметры.

**Возвращает**:
  - Не возвращает значения.


**Замечания**:  Функция использует `QEventLoop` для обработки асинхронных операций внутри GUI.