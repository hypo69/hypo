```markdown
# styles.py

Файл: `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\gui\styles.py`

**Описание:**

Модуль `styles.py` предоставляет общие функции для стилизации элементов пользовательского интерфейса (UI) в приложении. Он находится в пакете `suppliers.aliexpress.gui`.

**Функции:**

* **`set_fixed_size(widget: QtWidgets.QWidget, width: int, height: int)`:** Устанавливает фиксированный размер для переданного виджета `widget`.

**Использование:**

Для использования функции `set_fixed_size`, необходимо импортировать её из модуля `styles.py`.  Затем, передать в функцию виджет `QtWidgets.QWidget` и желаемые ширину и высоту в пикселях.

**Пример:**

```python
import sys
from PyQt6 import QtWidgets
from suppliers.aliexpress.gui.styles import set_fixed_size

# ... (ваш код создания виджетов) ...

button = QtWidgets.QPushButton("Кнопка")
set_fixed_size(button, 100, 50)  # Устанавливает размер кнопки в 100x50 пикселей

# ... (остальной код приложения) ...
```


**Примечание:**

Файл предполагает использование фреймворка PyQt6.  Строка `` указывает на интерпретатор Python, используемый для запуска приложения, и, скорее всего, указывает на виртуальное окружение (`venv`).  Эта строка важна для корректной работы скрипта в Windows.  Если файл используется в другом окружении, возможно, придётся скорректировать эту часть.
```