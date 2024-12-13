# `hypotez/src/gui/context_menu/header.py`

## Обзор

Данный модуль `header.py` предназначен для настройки путей и переменных окружения, необходимых для работы приложения `hypotez`. Он загружает настройки из файла `settings.json`, определяет корневую директорию проекта, добавляет пути к исполняемым файлам GTK, FFmpeg и Graphviz в переменную окружения `PATH`, а также устанавливает переменную `WEASYPRINT_DLL_DIRECTORIES` для работы WeasyPrint.

## Содержание

- [Обзор](#обзор)
- [Константы](#константы)
- [Импорт модулей](#импорт-модулей)
- [Загрузка настроек](#загрузка-настроек)
- [Определение корневого пути проекта](#определение-корневого-пути-проекта)
- [Пути к бинарным файлам](#пути-к-бинарным-файлам)
- [Обновление переменной PATH](#обновление-переменной-path)
- [Настройка переменной для WeasyPrint](#настройка-переменной-для-weasyprint)
- [Подавление вывода логов GTK](#подавление-вывода-логов-gtk)

## Константы

### `MODE`

**Описание**: Режим работы приложения. По умолчанию установлен в `dev`.
- Тип: `str`

## Импорт модулей

Модуль импортирует следующие библиотеки:

- `json`: для работы с JSON-файлами.
- `sys`: для доступа к переменным и функциям, связанным с интерпретатором Python.
- `pathlib.Path`: для работы с путями к файлам и директориям.
- `warnings`: для управления выводом предупреждений.

## Загрузка настроек

**Описание**: Загружает настройки проекта из файла `settings.json`, включая имя проекта.

```python
with open('settings.json', 'r') as settings_file:
    settings = json.load(settings_file)
    project_name = settings.get("project_name", "hypotez")
```

## Определение корневого пути проекта

**Описание**: Определяет абсолютный путь к корневой директории проекта на основе имени проекта, полученного из настроек.

```python
__root__: Path = Path.cwd().resolve().parents[Path.cwd().parts.index(project_name)]
sys.path.append(str(__root__))
```

## Пути к бинарным файлам

**Описание**: Определяет пути к бинарным файлам GTK, FFmpeg и Graphviz, находящимся в поддиректориях проекта.

```python
gtk_bin_path = __root__ / "bin" / "gtk" / "gtk-nsis-pack" / "bin"
ffmpeg_bin_path = __root__ / "bin" / "ffmpeg" / "bin"
graphviz_bin_path = __root__ / "bin" / "graphviz" / "bin"
```

## Обновление переменной PATH

**Описание**: Проверяет, добавлены ли пути к исполняемым файлам GTK, FFmpeg и Graphviz в переменную окружения `PATH`, и добавляет их, если они отсутствуют.

```python
paths_to_add = [gtk_bin_path, ffmpeg_bin_path, graphviz_bin_path]
current_paths = set(Path(p) for p in sys.path)

for bin_path in paths_to_add:
    if bin_path not in current_paths:
        sys.path.insert(0, str(bin_path))
```

## Настройка переменной для WeasyPrint

**Описание**: Настраивает переменную окружения `WEASYPRINT_DLL_DIRECTORIES`, добавляя путь к GTK бинарным файлам.

```python
sys_path_env_var = "WEASYPRINT_DLL_DIRECTORIES"
if sys_path_env_var not in sys.path:
    sys.path.insert(0, str(gtk_bin_path))
```

## Подавление вывода логов GTK

**Описание**: Подавляет вывод предупреждений GTK в консоль, чтобы не загромождать вывод приложения.

```python
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
```