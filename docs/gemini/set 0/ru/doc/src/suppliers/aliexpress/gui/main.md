# Модуль `hypotez/src/suppliers/aliexpress/gui/main.py`

## Обзор

Данный модуль предоставляет основной интерфейс приложения для управления рекламными кампаниями на AliExpress. Он использует PyQt6 для создания графического интерфейса и предоставляет инструменты для редактирования и управления JSON-файлами, а также данными кампаний и продуктами. Модуль также содержит функции для загрузки, сохранения и обработки файлов.

## Оглавление

- [Модуль `hypotez/src/suppliers/aliexpress/gui/main.py`](#модуль-hypotezsrcsuppliersaliexpressguimainpy)
- [Класс `MainApp`](#класс-mainapp)
- [Функция `main`](#функция-main)


## Класс `MainApp`

**Описание**: Класс `MainApp` представляет собой главное окно приложения. Он содержит вкладки для редактирования JSON-файлов, управления кампаниями и продуктами.

**Методы**:

### `__init__`

**Описание**: Инициализирует главное окно приложения с вкладками.

**Параметры**:
- Нет

**Возвращает**:
- Нет

### `create_menubar`

**Описание**: Создаёт строку меню с опциями для работы с файлами (открытие, сохранение, выход) и редактирования (копирование, вставка).

**Параметры**:
- Нет

**Возвращает**:
- Нет


### `open_file`

**Описание**: Открывает диалоговое окно для выбора и загрузки JSON-файла.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет


### `save_file`

**Описание**: Сохраняет текущий файл, в зависимости от выбранной вкладки.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет


### `exit_application`

**Описание**: Закрывает приложение.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет


### `copy`

**Описание**: Копирует выделенный текст в буфер обмена.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет


### `paste`

**Описание**: Вставляет текст из буфера обмена.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет


### `load_file`

**Описание**: Загружает JSON-файл.

**Параметры**:
- `campaign_file` (str): Путь к файлу.

**Возвращает**:
- Нет

**Вызывает исключения**:
- `Exception`: Возникает при ошибке загрузки файла.


## Функция `main`

**Описание**: Инициализирует и запускает приложение.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет