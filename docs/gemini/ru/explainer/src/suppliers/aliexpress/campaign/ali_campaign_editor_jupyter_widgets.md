# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor_jupyter_widgets.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.aliexpress.campaign 
	:platform: Windows, Unix
	:synopsis: Jupyter widgets for the AliExpress campaign editor.

This module contains widgets for managing AliExpress campaigns in Jupyter notebooks.

Testfile:
    file test_ali_campaign_editor_jupyter_widgets.py

"""
MODE = 'dev'


from types import SimpleNamespace
import header
from pathlib import Path
from ipywidgets import widgets
from IPython.display import display
import webbrowser

from src import gs
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.utils import locales
from src.utils import pprint, get_directory_names
from src.logger import logger

class JupyterCampaignEditorWidgets:
    """Widgets for the AliExpress campaign editor.

    This class provides widgets for interacting with and managing AliExpress campaigns,
    including selecting campaigns, categories, and languages, and performing actions such as
    initializing editors, saving campaigns, and showing products.

    Example:
        >>> editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
        >>> editor_widgets.display_widgets()
    """

    # Class attributes declaration
    language: str = None
    currency: str = None
    campaign_name: str = None
    category_name: str = None
    category:SimpleNamespace = None
    campaign_editor: AliCampaignEditor = None
    products:list[SimpleNamespace] = None
    def __init__(self):
        """Initialize the widgets and set up the campaign editor.

        Sets up the widgets for selecting campaigns, categories, and languages. Also sets up
        default values and callbacks for the widgets.
        """
        self.campaigns_directory:str = Path(
            gs.path.google_drive, "aliexpress", "campaigns"
        )
        
        if not self.campaigns_directory.exists():
            raise FileNotFoundError(
                f"Directory does not exist: {self.campaigns_directory}"
            )

        #self.languages = {"EN": "USD", "HE": "ILS", "RU": "ILS"}
        self.campaign_name_dropdown = widgets.Dropdown(
            options = get_directory_names(self.campaigns_directory),
            description = "Campaign Name:",
        )
        self.category_name_dropdown = widgets.Dropdown(
            options=[], description="Category:"
        )
        self.language_dropdown = widgets.Dropdown(
            options=[f"{key} {value}" for locale in locales for key, value in locale.items()],
            description="Language/Currency:",
        )
        # ... (rest of the class)
```

# <algorithm>

**Пошаговый алгоритм работы класса `JupyterCampaignEditorWidgets`:**

1. **Инициализация (`__init__`):**
    * Определяет директорию кампаний.
    * Проверяет существование директории. Если нет, выбрасывает ошибку.
    * Создает `widgets.Dropdown` для выбора кампании, категории и языка/валюты.
    * Создает `widgets.Button` для инициализации редактора, сохранения кампании, отображения продуктов и открытия таблицы Google.
    * Устанавливает обратные вызовы (`callbacks`) для `Dropdown` и `Button`.
    * Инициализирует `campaign_editor` с первой кампанией.

2. **Инициализация редактора кампании (`initialize_campaign_editor`):**
    * Получает выбранное значение из `campaign_name_dropdown`.
    * Получает выбранные значения из `category_name_dropdown` и `language_dropdown`.
    * Если имя кампании выбрано:
        * Обновляет `category_name_dropdown` в зависимости от выбранной кампании.
        * Создает экземпляр `AliCampaignEditor` с выбранными параметрами.
        * Если выбрана категория:
            * Получает категорию из `AliCampaignEditor`.
            * Получает продукты из категории из `AliCampaignEditor`.
    * Если имя кампании не выбрано, выводит предупреждение в лог.

3. **Обновление выпадающего списка категорий (`update_category_dropdown`):**
    * Строит путь к категории по имени кампании.
    * Получает список категорий из указанного пути.
    * Обновляет опции `category_name_dropdown` с полученным списком категорий.

4. **Обработка событий (`on_campaign_name_change`, `on_category_change`, `on_language_change`):**
    * Обновляет соответствующие атрибуты класса.
    * Вызывает `initialize_campaign_editor`, чтобы обновить состояние редактора.

5. **Сохранение кампании (`save_campaign`):**
    * Получает данные из `Dropdown`-ов.
    * Если имя кампании и язык выбраны:
        * Создает экземпляр `AliCampaignEditor` с выбранными данными.
        * Пытается сохранить категории из Google таблицы.
        * Обрабатывает потенциальные ошибки при сохранении.
    * Иначе выводит предупреждение в лог.

6. **Отображение продуктов (`show_products`):**
    * Получает данные из `Dropdown`-ов.
    * Создает экземпляр `AliCampaignEditor` с выбранными данными.
    * Задает Google таблицу по категории, что-то там делает с ней.
    * Обрабатывает потенциальные ошибки при отображении продуктов.


7. **Открытие таблицы Google (`open_spreadsheet`):**
    * Проверяет, что редактор кампании инициализирован.
    * Если инициализирован, формирует URL и открывает его в браузере.
    * Иначе выводит сообщение об отсутствии редактора.

8. **Установка обратных вызовов (`setup_callbacks`):**
   * Подписывает обратные вызовы на изменения в `Dropdown` и `Button` для реагирования на изменения введенных данных.

9. **Отображение виджетов (`display_widgets`):**
   * Отображает все созданные виджеты в Jupyter Notebook.
   * Автоматически вызывает `initialize_campaign_editor` для обработки данных первой выбранной кампании.


# <mermaid>

```mermaid
graph LR
    A[JupyterCampaignEditorWidgets] --> B{__init__};
    B --> C[get_campaigns_directory];
    C --> D{Check directory existence};
    D -- Exist --> E[Create Dropdown widgets];
    D -- Not exist --> F[Raise FileNotFoundError];
    E --> G[Create Button widgets];
    G --> H[setup_callbacks];
    H --> I[initialize_campaign_editor];
    I --> J[Get campaign name];
    J --> K[Get category name];
    K --> L[Get language/currency];
    L --> M[Create AliCampaignEditor];
    M --> N[update_category_dropdown];
    N --> O[Get category];
    O --> P[Get products];
    P --> Q[display_widgets];
    Q --> R[Display widgets];
    H --> S[on_campaign_name_change];
    S --> I;
    H --> T[on_category_change];
    T --> I;
    H --> U[on_language_change];
    U --> I;
    H --> V[save_campaign];
    V --> W[Create AliCampaignEditor];
    W --> X[Save categories];
    H --> Y[show_products];
    Y --> Z[Set products worksheet];
    H --> AA[open_spreadsheet];
    AA --> AB[Get Spreadsheet URL];
    AA --> AC[Open URL in Browser];

    subgraph Dependencies
        C --> |gs.path.google_drive|
        E --> |ipywidgets|
        E --> |IPython.display|
        E --> |webbrowser|
        E --> |src.suppliers.aliexpress.campaign.AliCampaignEditor|
        E --> |src.suppliers.aliexpress.utils.locales|
        E --> |src.utils.pprint|
        E --> |src.utils.get_directory_names|
        E --> |src.logger|
    end
```

**Объяснение зависимостей (из диаграммы):**

* `gs.path.google_drive`: Получение пути к директории Google Drive из пакета `src`.
* `ipywidgets`: Библиотека для создания интерактивных виджетов в Jupyter Notebook.
* `IPython.display`: Библиотека для отображения результатов в Jupyter Notebook.
* `webbrowser`: Библиотека для открытия URL в браузере.
* `src.suppliers.aliexpress.campaign.AliCampaignEditor`:  Класс для работы с редактором кампаний AliExpress.
* `src.suppliers.aliexpress.utils.locales`: Список языков/валют.
* `src.utils.pprint`: Функция для красивой печати.
* `src.utils.get_directory_names`: Функция для получения списка директорий.
* `src.logger`: Модуль для логирования.

# <explanation>

**Импорты:**

* `from types import SimpleNamespace`:  Используется для создания объектов, содержащих атрибуты.
* `import header`:  Скорее всего, для импорта вспомогательных функций или настроек.  Необходим анализ файла `header.py`.
* `from pathlib import Path`:  Обеспечивает работу с путями к файлам и директориям в системе.
* `from ipywidgets import widgets`:  Библиотека для создания интерактивных виджетов.
* `from IPython.display import display`: Для отображения виджетов в Jupyter.
* `import webbrowser`:  Для открытия веб-страниц.
* `from src import gs`:  Пакет `gs` скорее всего содержит конфигурацию или данные для доступа к Google Drive.
* `from src.suppliers.aliexpress.campaign import AliCampaignEditor`:  Класс для работы с редактором кампаний AliExpress.
* `from src.suppliers.aliexpress.utils import locales`:  Словарь локализованных языков и валют (возможно, для международной поддержки).
* `from src.utils import pprint, get_directory_names`:  Дополнительные утилиты для работы с данными (например, для форматирования вывода или получения списка файлов).
* `from src.logger import logger`:  Логирование для отслеживания событий и ошибок.

**Классы:**

* `JupyterCampaignEditorWidgets`: Класс предоставляет виджеты для управления кампаниями AliExpress в Jupyter Notebook.
    * Атрибуты: `language`, `currency`, `campaign_name`, `category_name`, `category`, `campaign_editor`, `products`,  хранят данные о текущей кампании, языке, валюте, категории и связанных с ней объектах.
    * Методы: `__init__`, `initialize_campaign_editor`, `update_category_dropdown`, `on_campaign_name_change`, `on_category_change`, `on_language_change`, `save_campaign`, `show_products`, `open_spreadsheet`, `setup_callbacks`, `display_widgets`.

**Функции:**

* `get_directory_names(path: Path) -> list[str]`:  (В коде находится как comment) - Получает список имен директорий в указанной директории.  Функция  `get_directory_names` из пакета `src.utils` предназначена для получения имен каталогов в заданном пути.

**Переменные:**

* `MODE`: Строковая переменная, хранящая режим работы (например, 'dev' или 'prod').
* `self.campaigns_directory`: Путь к директории с кампаниями на Google Диске.

**Возможные ошибки и улучшения:**

* **Обработка исключений:** Обработка исключений (например, `FileNotFoundError`) в `__init__` и других методах является хорошим практикой.
* **Улучшение `get_directory_names`:**  Функция (закомментирована) могла бы быть переписана как статический метод класса.

**Взаимосвязи с другими частями проекта:**

* Класс `AliCampaignEditor` напрямую связан с обработкой данных кампании, вероятно, в других модулях.
* Модули `src.utils` и `src.logger` обеспечивают общие функции для всей системы.
* Пакет `gs` обеспечивает взаимодействие с Google Drive.


**Общий вывод:**

Код организован достаточно хорошо для управления данными кампаний.  Разделение на классы и функции улучшает читаемость и поддерживаемость.  Однако необходимо более глубокое понимание пакета `gs` и класса `AliCampaignEditor` для полноценного анализа.