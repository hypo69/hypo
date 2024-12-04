# Модуль `hypotez/src/suppliers/aliexpress/gui/styles.py`

## Обзор

Модуль `styles.py` содержит функции для настройки размеров элементов пользовательского интерфейса (UI) в приложении `hypotez`.  Он предоставляет общие функции для установки фиксированных размеров виджетов.

## Функции

### `set_fixed_size`

**Описание**: Устанавливает фиксированный размер для заданного виджета.

**Параметры**:
- `widget` (QtWidgets.QWidget): Виджет, для которого необходимо установить размер.
- `width` (int): Ширина виджета.
- `height` (int): Высота виджета.

**Возвращает**:
-  Не возвращает значение.

**Вызывает исключения**:
-  Не вызывает исключений.


```python
def set_fixed_size(widget: QtWidgets.QWidget, width: int, height: int):
    """ Set a fixed size for a given widget """
    widget.setFixedSize(width, height)
```