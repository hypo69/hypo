# Модуль для проверки валидности ответов от модели

## Обзор

Модуль `ask_model.py` предназначен для взаимодействия с AI-моделью (в частности, Google Gemini) и проверки валидности получаемых от неё ответов. Он выполняет запросы к модели на разных языках (русский и иврит) и сохраняет результаты в формате JSON.

## Подробней

Этот модуль играет важную роль в процессе экспериментов с AI-моделями. Он обеспечивает стандартизированный способ отправки запросов и обработки ответов, что позволяет автоматизировать тестирование и оценку производительности модели. Расположение файла в структуре проекта указывает на его использование в экспериментальных сценариях, связанных с обработкой данных для проекта `kazarinov`.

## Содержание

- [Переменные](#Переменные)
- [Функции](#Функции)
    - [model_ask](#model_ask)

## Переменные

### `test_directory`

```python
test_directory: Path = gs.path.external_storage / 'kazarinov' / 'mexironim' / '24_12_07_19_06_40_508'
```

Путь к директории с тестовыми данными.

### `products_in_test_dir`

```python
products_in_test_dir: Path = test_directory / 'products'
```

Путь к файлу, содержащему список товаров в директории с тестовыми данными.

### `products_list`

```python
products_list: list[dict] = j_loads(products_in_test_dir)
```

Список товаров, загруженных из файла `products_in_test_dir`.

### `system_instruction`

```python
system_instruction = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
```

Содержимое файла с системными инструкциями для модели.

### `command_instruction_ru`

```python
command_instruction_ru = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'command_instruction_mexiron_ru.md').read_text(encoding='UTF-8')
```

Содержимое файла с инструкциями для модели на русском языке.

### `command_instruction_he`

```python
command_instruction_he = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'command_instruction_mexiron_he.md').read_text(encoding='UTF-8')
```

Содержимое файла с инструкциями для модели на иврите.

### `api_key`

```python
api_key = gs.credentials.gemini.kazarinov
```

API-ключ для доступа к Google Gemini.

### `model`

```python
model = GoogleGenerativeAI(
    api_key=api_key,
    system_instruction=system_instruction,
    generation_config={'response_mime_type': 'application/json'}
)
```

Экземпляр класса `GoogleGenerativeAI` для взаимодействия с моделью Google Gemini.

### `q_ru`

```python
q_ru = command_instruction_ru + str(products_list)
```

Запрос к модели на русском языке, включающий инструкции и список товаров.

### `q_he`

```python
q_he = command_instruction_he + str(products_list)
```

Запрос к модели на иврите, включающий инструкции и список товаров.

### `response_ru_dict`

```python
response_ru_dict = model_ask('ru')
```

Словарь с ответом модели на русском языке.

### `response_he_dict`

```python
response_he_dict = model_ask('he')
```

Словарь с ответом модели на иврите.

## Функции

### `model_ask`

```python
def model_ask(lang: str, attempts: int = 3) -> dict:
    """
    Args:
        lang (str): Язык запроса ('ru' или 'he').
        attempts (int): Количество попыток запроса к модели в случае ошибки. По умолчанию 3.

    Returns:
        dict: Словарь с ответом от модели или пустой словарь в случае ошибки.

    Raises:
        Exception: Если возникает ошибка при запросе к модели.
    """
    ...
```

**Как работает функция**:

1. Функция `model_ask` принимает язык (`lang`) и количество попыток (`attempts`) в качестве аргументов.
2. Формирует запрос к модели, используя глобальные переменные `model`, `q_ru` и `q_he`.
3. Отправляет запрос к модели на указанном языке и получает ответ.
4. Если ответ пустой, логирует ошибку и возвращает пустой словарь.
5. Пытается распарсить ответ в формате JSON.
6. Если возникает ошибка парсинга, логирует ошибку и, если количество попыток больше 1, рекурсивно вызывает себя с уменьшенным количеством попыток.
7. Возвращает распарсенный ответ в виде словаря.

**Параметры**:

- `lang` (str): Язык запроса (`'ru'` для русского, `'he'` для иврита).
- `attempts` (int, optional): Количество попыток запроса к модели в случае неудачи. По умолчанию равно 3.

**Возвращает**:

- `dict`: Словарь с ответом от модели в формате JSON или пустой словарь в случае ошибки.

**Примеры**:

```python
response_ru = model_ask('ru')
response_he = model_ask('he', attempts=2)
```