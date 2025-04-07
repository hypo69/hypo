# Модуль `gpt_traigner`

## Обзор

Модуль предназначен для обучения моделей GPT (Generative Pre-trained Transformer) на основе данных, собранных из чатов с использованием веб-драйвера. Он включает в себя сбор и обработку данных разговоров, определение тональности и сохранение обработанных данных в форматах JSONL и CSV.

## Подробнее

Данный модуль является частью системы, в которой происходит сбор данных из чатов, их анализ и подготовка для обучения моделей машинного обучения. Он автоматизирует процесс сбора данных, их очистку и преобразование в форматы, пригодные для дальнейшего использования в задачах машинного обучения. Модуль использует веб-драйвер для доступа к веб-страницам с чатами, извлекает текстовые данные, определяет тональность и сохраняет результаты в файлы.

## Классы

### `GPT_Traigner`

**Описание**: Класс предназначен для сбора и обработки данных разговоров с целью обучения моделей GPT.

**Принцип работы**:
1.  Инициализация драйвера веб-браузера (Chrome) для взаимодействия с веб-страницами.
2.  Определение местоположения элементов на странице чата с использованием локаторов.
3.  Сбор данных из HTML-файлов, содержащих историю разговоров.
4.  Преобразование данных в структурированный формат (DataFrame).
5.  Сохранение данных в файлы форматов CSV, JSONL и TXT.

**Атрибуты**:
-   `driver` (Driver): Экземпляр класса `Driver` для управления веб-браузером.
-   `gs` (GptGs): Экземпляр класса `GptGs`, используемый для доступа к различным путям и настройкам.

**Методы**:
-   `__init__`: Инициализирует экземпляр класса `GPT_Traigner`.
-   `determine_sentiment`: Определяет тональность для пары сообщений в разговоре.
-   `save_conversations_to_jsonl`: Сохраняет пары сообщений разговоров в файл JSONL.
-   `dump_downloaded_conversations`: Собирает разговоры со страницы чата и сохраняет их в файлы CSV, JSONL и TXT.

## Функции

### `__init__`

```python
def __init__(self):
    """"""
    ...
    self.gs = GptGs()
```

**Назначение**: Инициализирует экземпляр класса `GPT_Traigner`.

**Параметры**:
-   Отсутствуют.

**Возвращает**:
-   Отсутствует.

**Как работает функция**:
1.  Инициализирует объект `GptGs`, который используется для доступа к различным путям и настройкам, связанным с Google Drive.

### `determine_sentiment`

```python
def determine_sentiment(self, conversation_pair: dict[str, str], sentiment: str = 'positive') -> str:
    """ Determine sentiment label for a conversation pair """
    ...
    if sentiment:
        return "positive"
    else:
        return "negative"
```

**Назначение**: Определяет тональность для пары сообщений в разговоре.

**Параметры**:
-   `conversation_pair` (dict[str, str]): Пара сообщений в разговоре (вопрос и ответ).
-   `sentiment` (str, optional): Тональность, которую нужно определить. По умолчанию `'positive'`.

**Возвращает**:
-   `str`: Строка `'positive'`, если тональность определена, иначе `'negative'`.

**Как работает функция**:
1.  Проверяет, передана ли тональность (`sentiment`).
2.  Если тональность передана, возвращает строку `'positive'`.
3.  Если тональность не передана, возвращает строку `'negative'`.

ASCII flowchart:

```
Проверка наличия sentiment
│
└───> Да: Возврат "positive"
│
└───> Нет: Возврат "negative"
```

**Примеры**:

```python
traigner = GPT_Traigner()
conversation_pair = {'user': 'Привет', 'assistant': 'Здравствуйте'}
sentiment = 'positive'
result = traigner.determine_sentiment(conversation_pair, sentiment)
print(result)  # Вывод: positive

sentiment = ''
result = traigner.determine_sentiment(conversation_pair, sentiment)
print(result)  # Вывод: negative
```

### `save_conversations_to_jsonl`

```python
def save_conversations_to_jsonl(self, data: list[dict], output_file: str):
    """ Save conversation pairs to a JSONL file """
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(j_dumps(clean_string(item)) + "\n")
```

**Назначение**: Сохраняет пары сообщений разговоров в файл JSONL.

**Параметры**:
-   `data` (list[dict]): Список словарей, содержащих данные разговоров.
-   `output_file` (str): Путь к файлу, в который нужно сохранить данные.

**Возвращает**:
-   Отсутствует.

**Как работает функция**:
1.  Открывает файл для записи с указанной кодировкой (`utf-8`).
2.  Проходит по каждому элементу в списке `data`.
3.  Очищает строку `item` с помощью `clean_string(item)`.
4.  Преобразует очищенный элемент в JSON-формат с помощью `j_dumps`.
5.  Записывает JSON-представление элемента в файл, добавляя символ новой строки (`\n`).

ASCII flowchart:

```
A: Открытие файла для записи
│
└───> B: Перебор элементов в data
│    │
│    └───> C: Очистка элемента с помощью clean_string
│    │
│    └───> D: Преобразование элемента в JSON с помощью j_dumps
│    │
│    └───> E: Запись JSON в файл с добавлением новой строки
│
└───> Закрытие файла
```

**Примеры**:

```python
from pathlib import Path
from src.utils.jjson import j_dumps

traigner = GPT_Traigner()
data = [{'user': 'Привет', 'assistant': 'Здравствуйте'}, {'user': 'Как дела?', 'assistant': 'Всё хорошо!'}]
output_file = 'conversations.jsonl'
traigner.save_conversations_to_jsonl(data, output_file)
# Результат: Файл conversations.jsonl содержит JSON-представления данных разговоров.
```

### `dump_downloaded_conversations`

```python
def dump_downloaded_conversations(self):
    """ Collect conversations from the chatgpt page """
    ...
    conversation_directory = Path(gs.path.google_drive / 'chat_gpt' / 'conversation')
    html_files = conversation_directory.glob("*.html")

    all_data = []
    counter: int = 0  # <- counter

    for local_file_path in html_files:
        # Get the HTML content
        file_uri = local_file_path.resolve().as_uri()
        self.driver.get_url(file_uri)
        
        user_elements = self.driver.execute_locator(locator.user)
        assistant_elements = self.driver.execute_locator(locator.assistant)
        
        user_content = [element.text for element in user_elements] if isinstance(user_elements, list) else [user_elements.text] if user_elements  else None
        assistant_content = [element.text for element in assistant_elements] if isinstance(assistant_elements, list) else [assistant_elements.text] if assistant_elements  else None

        if not user_content and not assistant_content:
            logger.error(f"Где данные?")
            continue

        for user_text, assistant_text in zip_longest(user_content, assistant_content):
            if user_text and assistant_text:
                data = {
                    'role': ['user', 'assistant'],
                    'content': [clean_string(user_text), clean_string(assistant_text)],
                    'sentiment': ['neutral', 'neutral']
                }
                all_data.append(pd.DataFrame(data))
                print(f'{counter} - {local_file_path}')
                counter += 1

    if all_data:
        all_data_df = pd.concat(all_data, ignore_index=True)

        # Save all accumulated results to a single CSV file
        csv_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.csv'
        all_data_df.to_csv(csv_file_path, index=False, encoding='utf-8')

        # Save all accumulated results to a single JSONL file
        jsonl_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'all_conversations.jsonl'
        all_data_df.to_json(jsonl_file_path, orient='records', lines=True, force_ascii=False)
        
        # Save raw conversations to a single line without formatting
        raw_conversations = ' '.join(all_data_df['content'].dropna().tolist())
        raw_file_path = gs.path.google_drive / 'chat_gpt' / 'conversation' / 'raw_conversations.txt'
        with open(raw_file_path, 'w', encoding='utf-8') as raw_file:
            raw_file.write(raw_conversations)
```

**Назначение**: Собирает разговоры со страницы чата и сохраняет их в файлы CSV, JSONL и TXT.

**Параметры**:
-   Отсутствуют.

**Возвращает**:
-   Отсутствует.

**Как работает функция**:

1.  **Определение директории с HTML файлами**:
    -   Определяется путь к директории, где хранятся HTML-файлы с разговорами, используя `gs.path.google_drive / 'chat_gpt' / 'conversation'`.
    -   Используется `Path` для представления пути к директории.

2.  **Поиск HTML файлов**:
    -   В директории ищутся все HTML-файлы, соответствующие маске `"*.html"`.

3.  **Инициализация переменных**:
    -   `all_data`: Список для хранения данных из всех файлов.
    -   `counter`: Счетчик обработанных файлов, инициализированный нулем.

4.  **Цикл по HTML файлам**:
    -   Для каждого найденного HTML-файла выполняется следующий набор действий:
        -   **Получение URI файла**:
            -   Определяется URI файла с использованием `local_file_path.resolve().as_uri()`.
        -   **Загрузка содержимого HTML в драйвер**:
            -   Используется `self.driver.get_url(file_uri)` для открытия HTML-страницы в браузере, управляемом `webdriver`.
        -   **Извлечение элементов пользователя и ассистента**:
            -   Используется `self.driver.execute_locator` с локаторами `locator.user` и `locator.assistant` для получения элементов, содержащих сообщения пользователя и ассистента.
            -   Локаторы определяют, как искать элементы на странице (например, по CSS-селектору или XPath).
        -   **Извлечение текста из элементов**:
            -   Извлекается текст из найденных элементов пользователя и ассистента.
            -   Проверяется, является ли результат списком элементов или одним элементом, и извлекается текст соответствующим образом.
        -   **Проверка наличия данных**:
            -   Если ни пользователь, ни ассистент не имеют содержимого, в лог записывается сообщение об ошибке (`logger.error(f"Где данные?")`) и происходит переход к следующему файлу.
        -   **Обработка пар сообщений**:
            -   Используется `zip_longest` для итерации по сообщениям пользователя и ассистента.
            -   Для каждой пары сообщений создается словарь `data`, содержащий роли (`user`, `assistant`), содержимое сообщений и тональность (`neutral`).
            -   Созданный словарь преобразуется в `pd.DataFrame` и добавляется в список `all_data`.
            -   Выводится сообщение с номером обработанного файла и его путем.
            -   Увеличивается счетчик обработанных файлов.

5.  **Сохранение обработанных данных**:
    -   После обработки всех файлов проверяется, есть ли данные для сохранения (`if all_data:`).
    -   **Конкатенация данных**:
        -   Все собранные `pd.DataFrame` объединяются в один `all_data_df` с помощью `pd.concat`.
    -   **Сохранение в CSV файл**:
        -   Данные сохраняются в CSV файл с именем `all_conversations.csv` по указанному пути.
        -   Используется `all_data_df.to_csv` с параметрами `index=False` (не сохранять индекс) и `encoding='utf-8'`.
    -   **Сохранение в JSONL файл**:
        -   Данные сохраняются в JSONL файл с именем `all_conversations.jsonl` по указанному пути.
        -   Используется `all_data_df.to_json` с параметрами `orient='records'` (каждая строка - запись), `lines=True` (каждая запись на новой строке), `force_ascii=False` (не экранировать Unicode символы).
    -   **Сохранение "сырых" разговоров в TXT файл**:
        -   Извлекается содержимое всех сообщений из столбца `'content'` DataFrame, удаляются пропущенные значения (`dropna()`), и все сообщения объединяются в одну строку с пробелами.
        -   Строка сохраняется в TXT файл с именем `raw_conversations.txt` по указанному пути.

ASCII flowchart:

```
A: Определение директории с HTML файлами
│
└───> B: Поиск HTML файлов
│
└───> C: Цикл по HTML файлам
│    │
│    └───> D: Получение URI файла
│    │
│    └───> E: Загрузка содержимого HTML в драйвер
│    │
│    └───> F: Извлечение элементов пользователя и ассистента
│    │
│    └───> G: Извлечение текста из элементов
│    │
│    └───> H: Проверка наличия данных
│    │    │
│    │    └───> Нет данных: Запись в лог и переход к следующему файлу
│    │
│    └───> I: Обработка пар сообщений
│    │    │
│    │    └───> J: Создание словаря с данными
│    │    │
│    │    └───> K: Добавление данных в список
│
└───> L: Проверка наличия данных для сохранения
│    │
│    └───> Нет данных: Завершение
│    │
│    └───> M: Конкатенация данных в DataFrame
│    │
│    └───> N: Сохранение в CSV файл
│    │
│    └───> O: Сохранение в JSONL файл
│    │
│    └───> P: Сохранение "сырых" разговоров в TXT файл
│
└───> Завершение
```

**Примеры**:

Примеры не требуются, так как функция выполняет автоматизированный процесс с использованием данных из Google Drive и веб-драйвера.