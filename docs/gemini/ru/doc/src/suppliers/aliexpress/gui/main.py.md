# src.suppliers.aliexpress.gui.main

## Обзор

Данный модуль определяет основной интерфейс графического приложения для управления рекламными кампаниями AliExpress. Он включает в себя главное окно приложения, вкладки для редактирования JSON, кампаний и продуктов, а также меню с основными операциями, такими как открытие, сохранение и копирование/вставка.

## Подробнее

Модуль `main.py` является отправной точкой для запуска графического интерфейса приложения. Он использует библиотеку `PyQt6` для создания пользовательского интерфейса и `qasync` для интеграции с асинхронным кодом. Приложение состоит из нескольких вкладок, каждая из которых предоставляет инструменты для работы с различными аспектами рекламных кампаний: редактирование JSON-файлов, управление кампаниями и редактирование информации о продуктах. Главное окно приложения содержит меню с командами для работы с файлами (открытие, сохранение, выход) и редактирования (копирование, вставка).

## Классы

### `MainApp`

**Описание**: Главный класс приложения, который создает основное окно с вкладками для редактирования JSON, кампаний и продуктов.

**Методы**:
- `__init__`: Инициализирует главное окно приложения, устанавливает заголовок, размеры и создает вкладки.
- `create_menubar`: Создает меню с опциями для работы с файлами и редактированием.
- `open_file`: Открывает диалоговое окно для выбора и загрузки JSON-файла.
- `save_file`: Сохраняет текущий файл.
- `exit_application`: Закрывает приложение.
- `copy`: Копирует выделенный текст в буфер обмена.
- `paste`: Вставляет текст из буфера обмена.
- `load_file`: Загружает JSON-файл.

**Параметры**:
- Нет параметров.

**Примеры**
```python
import sys
from PyQt6 import QtWidgets
from src.suppliers.aliexpress.gui.main import MainApp

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
```

## Функции

### `main`

```python
def main():
    """ Initialize and run the application """
    app = QtWidgets.QApplication(sys.argv)

    # Create an event loop for asynchronous operations
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    main_app = MainApp()
    main_app.show()

    # Run the event loop
    with loop:
        loop.run_forever()
```

**Описание**: Инициализирует и запускает приложение.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Не вызывает исключений.

**Примеры**:
```python
if __name__ == "__main__":
    main()
```