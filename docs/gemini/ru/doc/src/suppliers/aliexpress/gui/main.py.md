# src.suppliers.aliexpress.gui.main.py

## Обзор

Данный модуль реализует главное окно приложения для управления рекламными кампаниями. Он включает в себя несколько вкладок для редактирования JSON, управления кампаниями и продуктами. Модуль использует PyQt6 для создания графического интерфейса и qasync для асинхронных операций.

## Оглавление

- [Классы](#Классы)
  - [`MainApp`](#MainApp)
- [Функции](#Функции)
  - [`main`](#main)

## Классы

### `MainApp`

**Описание**: Главное окно приложения, которое содержит в себе вкладки для различных редакторов и обеспечивает базовые операции с файлами и текстом.

**Методы**:

- `__init__(self)`:
    ```python
    def __init__(self):
        """ Initialize the main application with tabs """
    ```
    Инициализирует главное окно приложения, добавляя вкладки для редактора JSON, редактора кампаний и редактора продуктов.
- `create_menubar(self)`:
    ```python
    def create_menubar(self):
        """ Create a menu bar with options for file operations and edit commands """
    ```
    Создает строку меню с опциями для работы с файлами (открытие, сохранение, выход) и редактирования (копирование, вставка).
- `open_file(self)`:
    ```python
    def open_file(self):
        """ Open a file dialog to select and load a JSON file """
    ```
    Открывает диалоговое окно выбора файла для загрузки JSON-файла. Загружает файл в активную вкладку (редактор JSON).
- `save_file(self)`:
    ```python
    def save_file(self):
        """ Save the current file """
    ```
    Сохраняет изменения в текущем активном редакторе. Сохраняет JSON в редакторе JSON и продукт в редакторе продуктов.
- `exit_application(self)`:
    ```python
    def exit_application(self):
        """ Exit the application """
    ```
    Закрывает приложение.
- `copy(self)`:
    ```python
    def copy(self):
        """ Copy selected text to the clipboard """
    ```
    Копирует выделенный текст в буфер обмена из виджетов `QLineEdit`, `QTextEdit` или `QPlainTextEdit`.
- `paste(self)`:
    ```python
    def paste(self):
        """ Paste text from the clipboard """
    ```
    Вставляет текст из буфера обмена в виджеты `QLineEdit`, `QTextEdit` или `QPlainTextEdit`.
- `load_file(self, campaign_file)`:
    ```python
    def load_file(self, campaign_file):
         """ Load the JSON file """
    ```
    Загружает JSON-файл в редактор JSON.

    **Параметры**:
    - `campaign_file` (str): Путь к JSON-файлу.
    
    **Вызывает исключения**:
      - `Exception`: Возникает при ошибке загрузки JSON-файла.

## Функции

### `main`

**Описание**: Инициализирует и запускает приложение. Создаёт цикл событий для асинхронных операций.

```python
def main():
    """ Initialize and run the application """
```