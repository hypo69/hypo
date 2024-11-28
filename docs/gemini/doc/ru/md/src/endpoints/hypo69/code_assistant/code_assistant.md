# Модуль code_assistant

## Обзор

Модуль `code_assistant` предназначен для обработки файлов кода с использованием моделей ИИ (в частности, Gemini). Он читает файлы, создает запросы для модели, получает ответы и сохраняет результаты в указанной директории.  Модуль обеспечивает гибкую настройку через аргументы командной строки и конфигурационный файл.

## Оглавление

* [Модуль code_assistant](#модуль-code-assistant)
* [Обзор](#обзор)
* [Классы](#классы)
    * [Класс `CodeAssistant`](#класс-codeassistant)
        * [Метод `__init__`](#метод-init)
        * [Метод `_initialize_models`](#метод-initialize_models)
        * [Метод `parse_args`](#метод-parse_args)
        * [Свойство `system_instruction`](#свойство-system_instruction)
        * [Свойство `code_instruction`](#свойство-code_instruction)
        * [Свойство `translations`](#свойство-translations)
        * [Метод `process_files`](#метод-process_files)
        * [Метод `_create_request`](#метод-create_request)
        * [Метод `_yield_files_content`](#метод-yield_files_content)
        * [Метод `_save_response`](#метод-save_response)
        * [Метод `_remove_outer_quotes`](#метод-remove_outer_quotes)
        * [Метод `run`](#метод-run)
* [Функции](#функции)
    * [Функция `main`](#функция-main)

## Классы

### Класс `CodeAssistant`

**Описание**: Класс для работы ассистента программиста с моделями ИИ.  Предназначен для чтения файлов, формирования запросов к моделям, получения ответов и сохранения результатов.

**Атрибуты**:

* `role`: (str) Роль ассистента (например, `code_checker`).
* `lang`: (str) Язык обработки (например, `ru`).
* `start_dirs`: (Path | str | list[Path] | list[str]) Директории для обработки файлов.
* `base_path`: (Path) Базовая директория для работы.
* `config`: (SimpleNamespace) Конфигурация из файла `code_assistant.json`.
* `gemini_model`: (GoogleGenerativeAI) Объект модели Gemini.
* `openai_model`: (OpenAIModel) Объект модели OpenAI.
* `start_file_number`: (int) Номер файла для начала обработки (для продолжения после ошибок).

**Методы**:

#### Метод `__init__`

```python
def __init__(self, **kwargs):
    """Инициализация ассистента с заданными параметрами."""
    # ... (Код инициализации)
```

#### Метод `_initialize_models`

```python
def _initialize_models(self, **kwargs):
    """Инициализация моделей на основе заданных параметров."""
    # ... (Код инициализации моделей)
```

#### Метод `parse_args`

```python
@staticmethod
def parse_args():
    """Разбор аргументов командной строки."""
    # ... (Код разбора аргументов)
```

#### Свойство `system_instruction`

```python
@property
def system_instruction(self) -> str | bool:
    """Чтение инструкции из файла."""
    # ... (Код чтения инструкции)
```

#### Свойство `code_instruction`

```python
@property
def code_instruction(self) -> str | bool:
    """Чтение инструкции для кода."""
    # ... (Код чтения инструкции)
```

#### Свойство `translations`

```python
@property
def translations(self) -> SimpleNamespace:
    """Загрузка переводов для ролей и языков."""
    # ... (Код загрузки переводов)
```


#### Метод `process_files`

```python
def process_files(self, start_file_number: Optional[int] = 1):
    """компиляция, отправка запроса и сохранение результата."""
    # ... (Подробное описание метода, включая блок обработки исключений)
```

#### Метод `_create_request`

```python
def _create_request(self, file_path: str, content: str) -> str:
    """Создание запроса с учетом роли и языка."""
    # ... (Описание метода)
```

#### Метод `_yield_files_content`

```python
def _yield_files_content(
    self,
    start_dirs: List[Path] = [gs.path.src],
) -> Iterator[tuple[Path, str]]:
    """Генерирует пути файлов и их содержимое по указанным шаблонам."""
    # ... (Описание метода, включая обработку исключений)
```

#### Метод `_save_response`

```python
def _save_response(self, file_path: Path, response: str, model_name: str) -> None:
    """Сохранение ответа модели в файл."""
    # ... (Подробное описание метода, включая блок обработки исключений)
```

#### Метод `_remove_outer_quotes`

```python
def _remove_outer_quotes(self, response: str) -> str:
    """Удаляет внешние кавычки в начале и в конце строки."""
    # ... (Описание метода)
```

#### Метод `run`

```python
def run(self, start_file_number: int = 1):
    """Запуск процесса обработки файлов."""
    # ... (Описание метода)
```

## Функции

### Функция `main`

```python
def main():
    """Основная функция для запуска."""
    # ... (Код запуска ассистента)
```

**Примечания**:  В коде присутствуют комментарии, описывающие функциональность отдельных частей, но для лучшего понимания потребуется детальный разбор каждого метода и атрибута.  Для полного понимания документации, необходимо также ознакомиться с зависимостями (импортами) и конфигурационными файлами, используемыми модулем.