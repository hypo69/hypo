# `src/gui/openai_trаigner/main.py`

## Обзор

Данный модуль реализует главное окно приложения, которое представляет собой браузер с дополнительными функциями, такими как сворачивание в трей, выбор URL из меню и выбор модели.

## Оглавление

1.  [Классы](#классы)
    *   [`AssistantMainWindow`](#assistantmainwindow)
2.  [Функции](#функции)

## Классы

### `AssistantMainWindow`

**Описание**:
Основное окно приложения, реализующее браузер и дополнительный функционал.

**Методы**:

-   `__init__`: Инициализирует главное окно, устанавливает размеры, создает элементы управления, системный трей, меню и подключает обработчики событий.
-   `ask_for_browser`: Запрашивает у пользователя выбор браузера по умолчанию.
-   `load_url`: Загружает указанный URL в браузере.
-   `hide_to_tray`: Скрывает окно и помещает иконку в системный трей.
-   `quit_app`: Выходит из приложения.
-   `closeEvent`: Переопределенный метод для обработки события закрытия окна.

#### `__init__`

```python
def __init__(self):
```
**Описание**:
Инициализирует главное окно, устанавливает размеры, создает элементы управления, системный трей, меню и подключает обработчики событий.

#### `ask_for_browser`

```python
def ask_for_browser(self) -> str | None:
```
**Описание**:
Запрашивает у пользователя выбор браузера по умолчанию.

**Возвращает**:
- `str | None`: Выбранное имя браузера (Chrome, Firefox, Edge) или `None`, если выбор не сделан или отменен.

#### `load_url`
```python
def load_url(self, url: str = None) -> None:
```
**Описание**:
Загружает указанный URL в браузере.

**Параметры**:
-   `url` (str, optional): URL для загрузки. Если не указан, то URL берется из текстового поля. По умолчанию `None`.

#### `hide_to_tray`
```python
def hide_to_tray(self) -> None:
```
**Описание**:
Скрывает окно и помещает иконку в системный трей.

#### `quit_app`
```python
def quit_app(self) -> None:
```
**Описание**:
Выходит из приложения.

#### `closeEvent`
```python
def closeEvent(self, event) -> None:
```
**Описание**:
Переопределенный метод для обработки события закрытия окна. Скрывает окно и помещает иконку в системный трей вместо закрытия приложения.

**Параметры**:
- `event`: Событие закрытия окна.

## Функции

### `if __name__ == "__main__":`

**Описание**:
Точка входа в приложение. Создает экземпляр `QApplication`, устанавливает флаг для трея, создает и показывает главное окно.

**Параметры**:
- `sys.argv` (list): Список аргументов командной строки.