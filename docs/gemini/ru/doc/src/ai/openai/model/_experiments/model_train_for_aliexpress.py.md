# Модуль `model_train_for_aliexpress.py`

## Обзор

Модуль `model_train_for_aliexpress.py` предназначен для обучения и экспериментов с моделями искусственного интеллекта (OpenAI и Google Gemini) для задач, связанных с AliExpress. В частности, модуль использует заголовки товаров AliExpress для генерации контента или анализа данных.

## Подробней

Этот модуль является частью проекта `hypotez` и служит для экспериментов с AI-моделями, такими как OpenAI и Google Gemini, в контексте данных AliExpress. Он использует заголовки товаров для обучения моделей или генерации контента.

## Функции

### `recursively_get_filenames`

```python
from src.utils.file import recursively_get_filenames
recursively_get_filenames(gs.path.google_drive / 'aliexpress' / 'campaigns', 'product_titles.txt')
```

**Назначение**: Получение списка файлов с заголовками товаров рекурсивно из указанной директории.

**Как работает функция**:
Функция `recursively_get_filenames` рекурсивно просматривает указанную директорию (`gs.path.google_drive / 'aliexpress' / 'campaigns'`) и возвращает список полных путей ко всем файлам, имеющим расширение `product_titles.txt`.

**Параметры**:
- `gs.path.google_drive / 'aliexpress' / 'campaigns'` (Path): Путь к директории, в которой нужно искать файлы.
- `'product_titles.txt'` (str): Расширение файлов, которые нужно найти.

**Возвращает**:
- `list`: Список полных путей к файлам, найденных в директории.

**Вызывает исключения**:
- `FileNotFoundError`: Если директория не существует.
- `OSError`: В случае проблем с доступом к директории.

### `read_text_file`

```python
from src.utils.file import read_text_file
read_text_file(system_instruction_path)
```

**Назначение**: Чтение содержимого текстового файла.

**Как работает функция**:
Функция `read_text_file` считывает содержимое текстового файла, расположенного по указанному пути (`system_instruction_path`), и возвращает его в виде строки.

**Параметры**:
- `system_instruction_path` (str): Путь к текстовому файлу.

**Возвращает**:
- `str`: Содержимое текстового файла.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `OSError`: В случае проблем с чтением файла.

### `OpenAIModel`

```python
from src.ai import OpenAIModel
openai = OpenAIModel(system_instruction=system_instruction)
```

**Назначение**: Инициализация модели OpenAI для генерации ответов на основе предоставленных заголовков товаров.

**Как работает функция**:
Функция `OpenAIModel` инициализирует модель OpenAI с использованием предоставленной системной инструкции (`system_instruction`). Затем модель OpenAI используется для генерации ответов на основе предоставленных заголовков продуктов.

**Параметры**:
- `system_instruction` (str): Системная инструкция для модели OpenAI.

**Возвращает**:
- `OpenAIModel`: Объект модели OpenAI, сконфигурированный с системной инструкцией.

### `GoogleGenerativeAI`

```python
from src.ai import GoogleGenerativeAI
gemini = GoogleGenerativeAI(system_instruction=system_instruction)
```

**Назначение**: Инициализация модели Google Gemini для генерации ответов на основе предоставленных заголовков продуктов.

**Как работает функция**:
Функция `GoogleGenerativeAI` инициализирует модель Google Gemini с использованием предоставленной системной инструкции (`system_instruction`). Затем модель Gemini используется для генерации ответов на основе предоставленных заголовков продуктов.

**Параметры**:
- `system_instruction` (str): Системная инструкция для модели Google Gemini.

**Возвращает**:
- `GoogleGenerativeAI`: Объект модели Google Gemini, сконфигурированный с системной инструкцией.

### Основной цикл обработки файлов

```python
for file in product_titles_files:
    ...
    product_titles = read_text_file(file)
    response_openai = openai.ask(product_titles)
    response_gemini = gemini.ask(product_titles)
    ...
```

**Назначение**: Обработка каждого файла с заголовками товаров.

**Как работает цикл**:
Цикл `for file in product_titles_files:` перебирает каждый файл с заголовками товаров. Внутри цикла происходят следующие действия:

1.  **Чтение заголовков**: Читает заголовки товаров из текущего файла с использованием функции `read_text_file`.

2.  **Получение ответа от OpenAI**: Отправляет заголовки товаров в модель OpenAI и получает ответ.

3.  **Получение ответа от Gemini**: Отправляет заголовки товаров в модель Gemini и получает ответ.

4.  **Обработка ответов**: <далее, если есть>

## Переменные

-   `product_titles_files` (list): Список файлов, содержащих заголовки продуктов AliExpress.
-   `system_instruction_path` (Path): Путь к файлу с системными инструкциями для моделей AI.
-   `system_instruction` (str): Содержимое файла с системными инструкциями.
-   `openai` (OpenAIModel): Экземпляр модели OpenAI.
-   `gemini` (GoogleGenerativeAI): Экземпляр модели Google Gemini.
-   `file` (Path): Текущий файл в цикле обработки.
-   `product_titles` (str): Заголовки продуктов, прочитанные из текущего файла.
-   `response_openai` (str): Ответ, полученный от модели OpenAI.
-   `response_gemini` (str): Ответ, полученный от модели Gemini.