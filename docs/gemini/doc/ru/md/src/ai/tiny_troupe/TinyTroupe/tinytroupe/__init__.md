# Модуль tinytroupe.__init__

## Обзор

Этот модуль содержит инициализацию TinyTroupe, включая чтение конфигурации, настройку логгера и корректировку вывода в Jupyter Notebook. Он также содержит предупреждения об использовании AI.

## Импорты

- `os`: Для работы с операционной системой.
- `logging`: Для создания и управления логгером.
- `configparser`: Для чтения конфигурационных файлов.
- `rich`: Для форматированного вывода в консоли.
- `rich.jupyter`: Для интеграции с Jupyter Notebook.
- `sys`: Для добавления текущего каталога в пути поиска модулей.
- `utils`: Для использования утилит из модуля `tinytroupe.utils`.

## Функции

### `read_config_file`

**Описание**: Читает конфигурационный файл и возвращает объект `configparser.ConfigParser`.

**Возвращает**:
- `configparser.ConfigParser`: Объект, содержащий конфигурацию.

**Возможные исключения**:
- `FileNotFoundError`: Если конфигурационный файл не найден.
- `configparser.Error`: Если возникла ошибка при чтении конфигурационного файла.


### `pretty_print_config`

**Описание**: Выводит конфигурацию в красивом формате.

**Параметры**:
- `config` (configparser.ConfigParser): Объект конфигурации.


### `start_logger`

**Описание**: Настраивает и запускает логгер.

**Параметры**:
- `config` (configparser.ConfigParser): Объект конфигурации, содержащий настройки логгера.

### `inject_html_css_style_prefix`

**Описание**: Вставляет префикс CSS-стиля для удаления отступов в Jupyter Notebook.

**Параметры**:
- `html_format (str)`:  Текущий формат HTML.
- `style_prefix (str)`:  Префикс CSS-стиля.

**Возвращает**:
- `str`: Модифицированный HTML-формат.


## AI Предупреждения

Модуль содержит предупреждение об использовании AI моделей, которые могут давать неточные или неподходящие результаты.

## Использование

```python
import tinytroupe

# Запуск инициализации.
tinytroupe.start()
```

```
```
```python
# ... далее код для использования модуля ...
```
```