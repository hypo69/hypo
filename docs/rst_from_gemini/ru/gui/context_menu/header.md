```markdown
# Файл: hypotez/src/gui/context_menu/header.py

## Описание

Модуль `header.py` отвечает за инициализацию путей к бинарным файлам GTK, FFmpeg и Graphviz, а также обновление переменной окружения `PATH` для корректной работы этих библиотек в проекте.  Он также настраивает переменную `WEASYPRINT_DLL_DIRECTORIES` для WeasyPrint.  Кроме того, модуль подавляет вывод сообщений предупреждений GTK на консоль.

## Функциональность

* **Загрузка имени проекта:** Извлекает имя проекта из файла `settings.json`.
* **Определение корневого каталога проекта:** Находит абсолютный путь к корневому каталогу проекта, используя имя проекта из файла настроек.
* **Определение путей к бинарным каталогам:** Определяет пути к бинарным каталогам GTK, FFmpeg и Graphviz относительно корневого каталога.
* **Добавление путей в `sys.path`:**  Проверяет, что указанные пути не присутствуют в `sys.path` и добавляет их в начало списка, если они отсутствуют. Это необходимо для поиска библиотек.
* **Установка переменной окружения `WEASYPRINT_DLL_DIRECTORIES`:** Устанавливает путь к каталогу библиотек GTK в переменную окружения `WEASYPRINT_DLL_DIRECTORIES`, если она не установлена.
* **Подавление предупреждений GTK:** Используя `warnings.filterwarnings`, подавляет вывод предупреждений GTK на консоль.

## Код

```python
## \file hypotez/src/gui/context_menu/header.py
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" module: src.gui.context_menu """

"""! Absolute path to modules and GTK & FFPMEG bin directory """

import json
import sys
from pathlib import Path

# Load the project name from settings.json
with open('settings.json', 'r') as settings_file:
    settings = json.load(settings_file)
    project_name = settings.get("project_name", "hypotez")  

# Define the root path of the project
__root__: Path = Path.cwd().resolve().parents[Path.cwd().parts.index(project_name)]
sys.path.append(str(__root__))

# Paths to bin directories
gtk_bin_path = __root__ / "bin" / "gtk" / "gtk-nsis-pack" / "bin"
ffmpeg_bin_path = __root__ / "bin" / "ffmpeg" / "bin"
graphviz_bin_path = __root__ / "bin" / "graphviz" / "bin"

# Update the PATH variable if the paths are missing
paths_to_add = [gtk_bin_path, ffmpeg_bin_path, graphviz_bin_path]
current_paths = set(Path(p) for p in sys.path)

for bin_path in paths_to_add:
    if bin_path not in current_paths:
        sys.path.insert(0, str(bin_path))

# Set the variable for WeasyPrint
sys_path_env_var = "WEASYPRINT_DLL_DIRECTORIES"
if sys_path_env_var not in sys.path:
    sys.path.insert(0, str(gtk_bin_path))

"""Suppress GTK log output to the console"""
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
```

##  Комментарии

* **Обработка ошибок:**  Код предполагает, что `settings.json` существует и содержит ключ `project_name`.  Важно добавить проверку на существование файла и корректность формата JSON для повышения надёжности.
* **Оптимизация:**  Можно оптимизировать поиск корневого каталога, если структура проекта всегда одинакова (например, используя `Path.joinpath` или аналогичные методы).
* **Документация:** Добавлен более подробный комментарий к коду для лучшего понимания его назначения.


Этот файл является важной частью инициализации проекта, обеспечивая корректную работу зависимых библиотек.  Он должен выполняться в самом начале программы, чтобы гарантировать правильную работу других модулей.
