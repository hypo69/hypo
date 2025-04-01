# Модуль extraction

## Обзор

Модуль предоставляет утилиты для извлечения данных из элементов TinyTroupe, таких как агенты и миры. Он также предоставляет механизм для сжатия извлеченных данных и экспорта артефактов из элементов TinyTroupe.

## Подробнее

Этот модуль предоставляет инструменты для извлечения данных из элементов TinyTroupe, таких как агенты и миры. Он также предоставляет механизм для сжатия извлеченных данных до более лаконичной формы и экспорта артефактов из элементов TinyTroupe.
Модуль содержит классы:

- `ResultsExtractor`: Извлекает результаты из экземпляров `TinyPerson` и `TinyWorld`.
- `ResultsReducer`: Уменьшает объем данных, извлеченных из агентов.
- `ArtifactExporter`: Экспортирует артефакты из элементов TinyTroupe.
- `Normalizer`: Нормализует текстовые элементы.

## Классы

### `ResultsExtractor`

**Описание**: Класс, предназначенный для извлечения данных из экземпляров `TinyPerson` (агентов) и `TinyWorld` (миров) в TinyTroupe. Он использует шаблоны для формирования запросов к LLM и извлечения структурированных данных.

**Принцип работы**:
Класс инициализируется с путем к шаблону промпта для извлечения (`_extraction_prompt_template_path`) и кэшем для хранения результатов извлечения для агентов и миров (`agent_extraction` и `world_extraction`). Методы `extract_results_from_agent` и `extract_results_from_world` формируют запросы на основе шаблона, отправляют их в LLM (через `openai_utils.client().send_message`) и извлекают JSON-данные из ответа. Результаты кэшируются для последующего использования.

**Аттрибуты**:

- `_extraction_prompt_template_path` (str): Путь к mustache-шаблону, используемому для формирования запроса к LLM.
- `agent_extraction` (dict): Кэш для хранения результатов извлечения для агентов. Ключом является имя агента.
- `world_extraction` (dict): Кэш для хранения результатов извлечения для миров. Ключом является имя мира.

**Методы**:

- `extract_results_from_agent(tinyperson: TinyPerson, extraction_objective: str = "The main points present in the agent's interactions history.", situation: str = "", fields: list = None, fields_hints: dict = None, verbose: bool = False) -> dict | None`: Извлекает результаты из экземпляра `TinyPerson`.
- `extract_results_from_world(tinyworld: TinyWorld, extraction_objective: str = "The main points that can be derived from the agents conversations and actions.", situation: str = "", fields: list = None, fields_hints: dict = None, verbose: bool = False) -> dict | None`: Извлекает результаты из экземпляра `TinyWorld`.
- `save_as_json(filename: str, verbose: bool = False) -> None`: Сохраняет последние результаты извлечения в файл JSON.

### `ResultsReducer`

**Описание**: Класс предназначен для уменьшения объема данных, извлеченных из агентов. Он применяет правила редукции к эпизодической памяти агента и преобразует результаты в DataFrame.

**Принцип работы**:
Класс инициализируется с пустыми словарями для хранения результатов (`results`) и правил редукции (`rules`). Метод `add_reduction_rule` добавляет правила редукции, связывая тип события (триггер) с функцией редукции. Метод `reduce_agent` применяет правила к эпизодической памяти агента, извлекая информацию из сообщений и применяя соответствующие функции редукции. Метод `reduce_agent_to_dataframe` преобразует результаты редукции в DataFrame.

**Аттрибуты**:

- `results` (dict): Словарь для хранения результатов редукции.
- `rules` (dict): Словарь для хранения правил редукции. Ключом является триггер (тип события), значением - функция редукции.

**Методы**:

- `add_reduction_rule(trigger: str, func: callable) -> None`: Добавляет правило редукции.
- `reduce_agent(agent: TinyPerson) -> list`: Уменьшает объем данных, извлеченных из агента, применяя правила редукции к его эпизодической памяти.
- `reduce_agent_to_dataframe(agent: TinyPerson, column_names: list = None) -> pd.DataFrame`: Преобразует результаты редукции в DataFrame.

### `ArtifactExporter`

**Описание**: Класс, отвечающий за экспорт артефактов из элементов TinyTroupe, например, для создания файлов синтетических данных из симуляций.

**Принцип работы**:
Класс инициализируется с базовой папкой вывода (`base_output_folder`). Метод `export` принимает имя артефакта, данные, тип контента и формат, и сохраняет данные в файл в указанном формате. Поддерживаются форматы JSON, TXT и DOCX. Класс также обрабатывает недопустимые символы в именах артефактов и создает промежуточные каталоги, если это необходимо.

**Аттрибуты**:

- `base_output_folder` (str): Базовая папка, в которой будут сохранены экспортированные артефакты.

**Методы**:

- `export(artifact_name: str, artifact_data: Union[dict, str], content_type: str, content_format: str = None, target_format: str = "txt", verbose: bool = False) -> None`: Экспортирует данные артефакта в файл.
- `_export_as_txt(artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False) -> None`: Экспортирует данные артефакта в текстовый файл.
- `_export_as_json(artifact_file_path: str, artifact_data: Union[dict, str], content_type: str, verbose: bool = False) -> None`: Экспортирует данные артефакта в файл JSON.
- `_export_as_docx(artifact_file_path: str, artifact_data: Union[dict, str], content_original_format: str, verbose: bool = False) -> None`: Экспортирует данные артефакта в файл DOCX.
- `_compose_filepath(artifact_data: Union[dict, str], artifact_name: str, content_type: str, target_format: str = None, verbose: bool = False) -> str`: Формирует путь к файлу для экспортируемого артефакта.

### `Normalizer`

**Описание**: Класс, предназначенный для нормализации текстовых элементов, таких как пассажи, концепции и другие текстовые элементы. Он использует LLM для объединения нескольких элементов в один нормализованный элемент.

**Принцип работы**:

Класс инициализируется списком элементов для нормализации (`elements`), количеством нормализованных элементов для вывода (`n`) и флагом verbose (`verbose`). В конструкторе происходит отправка запроса в LLM с использованием шаблонов `normalizer.system.mustache` и `normalizer.user.mustache`. Ответ LLM, содержащий нормализованные элементы, извлекается и сохраняется в `self.normalized_elements`. Метод `normalize` принимает элемент или список элементов для нормализации и возвращает соответствующий нормализованный элемент или список. Для повышения производительности используется кэширование результатов нормализации в `self.normalizing_map`.

**Атрибуты**:

- `elements` (List[str]): Список элементов для нормализации.
- `n` (int): Количество нормализованных элементов для вывода.
- `verbose` (bool): Флаг, определяющий, выводить ли отладочные сообщения.
- `normalized_elements` (dict): JSON-структура, где каждый выходной элемент является ключом к списку входных элементов, которые были объединены в него.
- `normalizing_map` (dict): Словарь, который сопоставляет каждый входной элемент с его нормализованным выводом.

**Методы**:

- `__init__(self, elements: List[str], n: int, verbose: bool = False) -> None`: Инициализирует экземпляр класса `Normalizer`.
- `normalize(self, element_or_elements: Union[str, List[str]]) -> Union[str, List[str]]`: Нормализует указанный элемент или элементы.

## Функции

### `ResultsExtractor.extract_results_from_agent`

```python
def extract_results_from_agent(self, 
                        tinyperson:TinyPerson, 
                        extraction_objective:str="The main points present in the agent's interactions history.", 
                        situation:str = "", 
                        fields:list=None,
                        fields_hints:dict=None,
                        verbose:bool=False) -> dict | None:
    """
    Извлекает результаты из экземпляра TinyPerson.

    Args:
        tinyperson (TinyPerson): Экземпляр TinyPerson, из которого нужно извлечь результаты.
        extraction_objective (str): Цель извлечения.
        situation (str): Ситуация, которую следует учитывать.
        fields (list, optional): Поля для извлечения. Если None, экстрактор сам решает, какие имена использовать.
            Defaults to None.
        verbose (bool, optional): Выводить ли отладочные сообщения. Defaults to False.
    
    Returns:
        dict | None: Извлеченные результаты в формате словаря или None в случае ошибки.
    """
```

**Назначение**: Извлечение результатов из истории взаимодействий агента `TinyPerson` с использованием языковой модели.

**Параметры**:

- `tinyperson` (TinyPerson): Объект агента, из которого извлекаются данные.
- `extraction_objective` (str): Цель извлечения, например, "Основные моменты в истории взаимодействий агента". По умолчанию - "The main points present in the agent's interactions history.".
- `situation` (str): Контекст или ситуация, которую следует учитывать при извлечении данных. По умолчанию "".
- `fields` (list, optional): Список полей, которые нужно извлечь. Если не указан, модель сама определяет, какие поля извлекать. По умолчанию `None`.
- `fields_hints` (dict, optional): Словарь с подсказками для модели о том, как интерпретировать поля. По умолчанию `None`.
- `verbose` (bool, optional): Флаг, указывающий, нужно ли выводить отладочные сообщения. По умолчанию `False`.

**Возвращает**:

- `dict | None`: Извлеченные результаты в виде словаря, если успешно, или `None`, если не удалось извлечь результаты.

**Как работает функция**:

1.  **Инициализация**:
    - Создается пустой список `messages` для хранения сообщений, отправляемых в языковую модель.
    - Создается словарь `rendering_configs` для хранения конфигураций рендеринга шаблона.
2.  **Подготовка конфигураций рендеринга**:
    - Если указан список полей `fields`, они объединяются в строку через запятую и добавляются в `rendering_configs` под ключом `"fields"`.
    - Если указан словарь подсказок для полей `fields_hints`, он преобразуется в список пар ключ-значение и добавляется в `rendering_configs` под ключом `"fields_hints"`.
3.  **Формирование системного сообщения**:
    - Читается содержимое файла шаблона промпта `self._extraction_prompt_template_path` (предположительно, mustache-шаблон).
    - Шаблон рендерится с использованием `rendering_configs` и добавляется в список `messages` как системное сообщение.
4.  **Получение истории взаимодействий агента**:
    - Вызывается метод `tinyperson.pretty_current_interactions()` для получения истории взаимодействий агента в удобочитаемом формате.
5.  **Формирование запроса на извлечение**:
    - Формируется строка запроса `extraction_request_prompt`, включающая цель извлечения, ситуацию и историю взаимодействий агента.
6.  **Отправка запроса в языковую модель**:
    - Запрос добавляется в список `messages` как сообщение пользователя.
    - Метод `openai_utils.client().send_message()` отправляет сообщения в языковую модель с температурой 0.0.
7.  **Обработка ответа языковой модели**:
    - Полученный ответ сохраняется в переменной `next_message`.
    - Извлекается JSON из содержимого ответа с помощью `utils.extract_json()`.
8.  **Кэширование результата**:
    - Результат извлечения кэшируется в словаре `self.agent_extraction` под ключом, соответствующим имени агента.
9.  **Возврат результата**:
    - Функция возвращает извлеченный результат.

**ASCII схема работы функции**:

```
    Начало
    │
    ├──► Подготовка конфигураций рендеринга (rendering_configs)
    │    │
    │    └──► Формирование системного сообщения (messages)
    │
    ├──► Получение истории взаимодействий агента (interaction_history)
    │    │
    │    └──► Формирование запроса на извлечение (extraction_request_prompt)
    │
    ├──► Отправка запроса в LLM (openai_utils.client().send_message)
    │    │
    │    └──► Обработка ответа LLM (next_message)
    │
    ├──► Извлечение JSON из ответа (utils.extract_json)
    │    │
    │    └──► Кэширование результата (self.agent_extraction)
    │
    └──► Возврат результата
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from extraction import ResultsExtractor

# Создание экземпляра агента (предполагается, что TinyPerson инициализирован)
agent = TinyPerson(name='Alice')
agent.pretty_current_interactions = lambda max_content_length=None: "Взаимодействие 1: ...\nВзаимодействие 2: ..."

# Создание экземпляра ResultsExtractor
extractor = ResultsExtractor()

# Пример 1: Извлечение основных моментов из истории взаимодействий агента
results = extractor.extract_results_from_agent(agent)
if results:
    print(f"Извлеченные результаты: {results}")
else:
    print("Не удалось извлечь результаты.")

# Пример 2: Извлечение с указанием цели и ситуации
results = extractor.extract_results_from_agent(agent, 
                                            extraction_objective="Определить эмоциональное состояние агента",
                                            situation="Агент находится в стрессовой ситуации")
if results:
    print(f"Извлеченные результаты: {results}")
else:
    print("Не удалось извлечь результаты.")

# Пример 3: Извлечение с указанием полей
results = extractor.extract_results_from_agent(agent, 
                                            fields=["эмоция", "причина"])
if results:
    print(f"Извлеченные результаты: {results}")
else:
    print("Не удалось извлечь результаты.")
```

### `ResultsExtractor.extract_results_from_world`

```python
def extract_results_from_world(self, 
                                   tinyworld:TinyWorld, 
                                   extraction_objective:str="The main points that can be derived from the agents conversations and actions.", 
                                   situation:str="", 
                                   fields:list=None,\
                                   fields_hints:dict=None,\
                                   verbose:bool=False) -> dict | None:
    """
    Извлекает результаты из экземпляра TinyWorld.

    Args:
        tinyworld (TinyWorld): Экземпляр TinyWorld, из которого нужно извлечь результаты.
        extraction_objective (str): Цель извлечения.
        situation (str): Ситуация, которую следует учитывать.
        fields (list, optional): Поля для извлечения. Если None, экстрактор сам решает, какие имена использовать.
            Defaults to None.
        verbose (bool, optional): Выводить ли отладочные сообщения. Defaults to False.
    """
```

**Назначение**: Извлечение результатов из взаимодействий агентов в виртуальном мире `TinyWorld` с использованием языковой модели.

**Параметры**:

- `tinyworld` (TinyWorld): Объект виртуального мира, из которого извлекаются данные.
- `extraction_objective` (str): Цель извлечения, например, "Основные выводы из разговоров и действий агентов". По умолчанию - "The main points that can be derived from the agents conversations and actions.".
- `situation` (str): Контекст или ситуация, которую следует учитывать при извлечении данных. По умолчанию "".
- `fields` (list, optional): Список полей, которые нужно извлечь. Если не указан, модель сама определяет, какие поля извлекать. По умолчанию `None`.
- `fields_hints` (dict, optional): Словарь с подсказками для модели о том, как интерпретировать поля. По умолчанию `None`.
- `verbose` (bool, optional): Флаг, указывающий, нужно ли выводить отладочные сообщения. По умолчанию `False`.

**Возвращает**:

- `dict | None`: Извлеченные результаты в виде словаря, если успешно, или `None`, если не удалось извлечь результаты.

**Как работает функция**:

Функция `extract_results_from_world` аналогична функции `extract_results_from_agent`, но применяется к экземпляру `TinyWorld`. Она формирует запрос к языковой модели на основе цели извлечения, ситуации и истории взаимодействий агентов в мире. Затем она извлекает JSON из ответа модели и кэширует результат.

1.  **Инициализация**:
    - Создается пустой список `messages` для хранения сообщений, отправляемых в языковую модель.
    - Создается словарь `rendering_configs` для хранения конфигураций рендеринга шаблона.
2.  **Подготовка конфигураций рендеринга**:
    - Если указан список полей `fields`, они объединяются в строку через запятую и добавляются в `rendering_configs` под ключом `"fields"`.
    - Если указан словарь подсказок для полей `fields_hints`, он преобразуется в список пар ключ-значение и добавляется в `rendering_configs` под ключом `"fields_hints"`.
3.  **Формирование системного сообщения**:
    - Читается содержимое файла шаблона промпта `self._extraction_prompt_template_path` (предположительно, mustache-шаблон).
    - Шаблон рендерится с использованием `rendering_configs` и добавляется в список `messages` как системное сообщение.
4.  **Получение истории взаимодействий агентов в мире**:
    - Вызывается метод `tinyworld.pretty_current_interactions()` для получения истории взаимодействий агентов в удобочитаемом формате.
5.  **Формирование запроса на извлечение**:
    - Формируется строка запроса `extraction_request_prompt`, включающая цель извлечения, ситуацию и историю взаимодействий агентов в мире.
6.  **Отправка запроса в языковую модель**:
    - Запрос добавляется в список `messages` как сообщение пользователя.
    - Метод `openai_utils.client().send_message()` отправляет сообщения в языковую модель с температурой 0.0.
7.  **Обработка ответа языковой модели**:
    - Полученный ответ сохраняется в переменной `next_message`.
    - Извлекается JSON из содержимого ответа с помощью `utils.extract_json()`.
8.  **Кэширование результата**:
    - Результат извлечения кэшируется в словаре `self.world_extraction` под ключом, соответствующим имени мира.
9.  **Возврат результата**:
    - Функция возвращает извлеченный результат.

**ASCII схема работы функции**:

```
    Начало
    │
    ├──► Подготовка конфигураций рендеринга (rendering_configs)
    │    │
    │    └──► Формирование системного сообщения (messages)
    │
    ├──► Получение истории взаимодействий агентов в мире (interaction_history)
    │    │
    │    └──► Формирование запроса на извлечение (extraction_request_prompt)
    │
    ├──► Отправка запроса в LLM (openai_utils.client().send_message)
    │    │
    │    └──► Обработка ответа LLM (next_message)
    │
    ├──► Извлечение JSON из ответа (utils.extract_json)
    │    │
    │    └──► Кэширование результата (self.world_extraction)
    │
    └──► Возврат результата
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from extraction import ResultsExtractor

# Создание экземпляра мира (предполагается, что TinyWorld инициализирован)
world = TinyWorld(name='Wonderland')
world.pretty_current_interactions = lambda max_content_length=None: "Агент Alice: ...\nАгент Bob: ..."

# Создание экземпляра ResultsExtractor
extractor = ResultsExtractor()

# Пример 1: Извлечение основных моментов из взаимодействий агентов в мире
results = extractor.extract_results_from_world(world)
if results:
    print(f"Извлеченные результаты: {results}")
else:
    print("Не удалось извлечь результаты.")

# Пример 2: Извлечение с указанием цели и ситуации
results = extractor.extract_results_from_world(world, 
                                            extraction_objective="Определить общее настроение в мире",
                                            situation="В мире произошли важные события")
if results:
    print(f"Извлеченные результаты: {results}")
else:
    print("Не удалось извлечь результаты.")

# Пример 3: Извлечение с указанием полей
results = extractor.extract_results_from_world(world, 
                                            fields=["общее настроение", "ключевые события"])
if results:
    print(f"Извлеченные результаты: {results}")
else:
    print("Не удалось извлечь результаты.")
```

### `ResultsExtractor.save_as_json`

```python
def save_as_json(self, filename: str, verbose: bool = False) -> None:
    """
    Сохраняет последние результаты извлечения в JSON.

    Args:
        filename (str): Имя файла для сохранения JSON.
        verbose (bool, optional): Выводить ли отладочные сообщения. Defaults to False.
    """
```

**Назначение**: Сохранение последних извлеченных данных агента и мира в файл в формате JSON.

**Параметры**:

- `filename` (str): Имя файла, в который будут сохранены данные JSON.
- `verbose` (bool, optional): Если установлено значение `True`, в консоль будет выведено сообщение о том, что данные были сохранены в указанный файл. По умолчанию `False`.

**Как работает функция**:

1.  **Открытие файла**: Открывает файл с указанным именем в режиме записи (`'w'`).
2.  **Запись JSON**: Записывает словарь, содержащий извлечения агента и мира (`self.agent_extraction` и `self.world_extraction`), в файл в формате JSON с отступом 4 для удобочитаемости.
3.  **Вывод сообщения (если verbose)**: Если параметр `verbose` установлен в `True`, выводит сообщение в консоль, подтверждающее, что данные были сохранены в указанный файл.

**ASCII схема работы функции**:

```
    Начало
    │
    ├──► Открытие файла (open(filename, 'w'))
    │
    ├──► Запись JSON (json.dump)
    │
    └──► Вывод сообщения (print) - условно
    │
    Конец
```

**Примеры**:

```python
from extraction import ResultsExtractor

# Создание экземпляра ResultsExtractor
extractor = ResultsExtractor()

# (Предположим, что extractor.agent_extraction и extractor.world_extraction уже содержат какие-то данные)

# Пример 1: Сохранение результатов в файл
extractor.save_as_json("extraction_results.json")

# Пример 2: Сохранение результатов с выводом отладочного сообщения
extractor.save_as_json("extraction_results_verbose.json", verbose=True)
```

### `ResultsReducer.add_reduction_rule`

```python
def add_reduction_rule(self, trigger: str, func: callable) -> None:
    """ Undocumented """
```

**Назначение**: Добавление правила редукции в класс `ResultsReducer`.

**Параметры**:

- `trigger` (str): Триггер, определяющий, когда применяется правило редукции.
- `func` (callable): Функция, выполняющая редукцию.

**Как работает функция**:

1.  **Проверка существования правила**: Проверяет, существует ли уже правило для данного триггера.
2.  **Выброс исключения**: Если правило для данного триггера уже существует, выбрасывается исключение.
3.  **Добавление правила**: Добавляет правило в словарь `self.rules`, связывая триггер с функцией редукции.

**ASCII схема работы функции**:

```
    Начало
    │
    ├──► Проверка существования правила (trigger in self.rules)
    │    │
    │    └──► Выброс исключения (raise Exception) - условно
    │
    └──► Добавление правила (self.rules[trigger] = func)
    │
    Конец
```

**Примеры**:

```python
from extraction import ResultsReducer

# Создание экземпляра ResultsReducer
reducer = ResultsReducer()

# Пример: Добавление правила редукции
def my_reduction_function(focus_agent, source_agent, target_agent, kind, event, content, timestamp):
    return {"event": event, "content": content}

reducer.add_reduction_rule("стимул", my_reduction_function)
```

### `ResultsReducer.reduce_agent`

```python
def reduce_agent(self, agent: TinyPerson) -> list:
    """ Undocumented """
```

**Назначение**: Уменьшение объема данных агента `TinyPerson` на основе заданных правил редукции.

**Параметры**:

- `agent` (TinyPerson): Агент, данные которого необходимо уменьшить.

**Возвращает**:

- `list`: Список уменьшенных данных.

**Как работает функция**:

1.  **Инициализация**: Создается пустой список `reduction` для хранения уменьшенных данных.
2.  **Итерация по сообщениям**: Перебирает все сообщения из эпизодической памяти агента.
3.  **Обработка сообщений**: В зависимости от роли сообщения (system, user, assistant) выполняются различные действия:
    - **system**: Пропускается.
    - **user**: Извлекается информация о стимуле (тип, содержимое, источник, время) и применяется правило редукции, если оно существует для данного типа стимула.
    - **assistant**: Извлекается информация о действии (тип, содержимое, цель, время) и применяется правило редукции, если оно существует для данного типа действия.
4.  **Добавление уменьшенных данных**: Если правило редукции вернуло не `None`, уменьшенные данные добавляются в список `reduction`.
5.  **Возврат уменьшенных данных**: Функция возвращает список `reduction`.

**ASCII схема работы функции**:

```
    Начало
    │
    ├──► Инициализация (reduction = [])
    │
    ├──► Итерация по сообщениям (for message in agent.episodic_memory.retrieve_all())
    │    │
    │    ├──► Обработка сообщений (switch message['role'])
    │    │    │
    │    │    ├──► system: continue
    │    │    │
    │    │    ├──► user: Извлечение информации о стимуле и применение правила редукции
    │    │    │
    │    │    └──► assistant: Извлечение информации о действии и применение правила редукции
    │    │
    │    └──► Добавление уменьшенных данных (reduction.append) - условно
    │
    └──► Возврат уменьшенных данных (return reduction)
    │
    Конец
```

**Примеры**:

```python
from extraction import ResultsReducer
from tinytroupe.agent import TinyPerson

# Создание экземпляра ResultsReducer
reducer = ResultsReducer()

# Создание экземпляра агента (предполагается, что TinyPerson инициализирован)
agent = TinyPerson(name='Alice')
agent.episodic_memory.store({"role": "user", "content": {"stimuli": [{"type": "стимул", "content": "содержимое", "source": "источник"}]}, "simulation_timestamp": 1})
agent.episodic_memory.store({"role": "assistant", "content": {"action": {"type": "действие", "content": "содержимое", "target": "цель"}}, "simulation_timestamp": 2})

# Пример: Уменьшение данных агента
def my_reduction_function(focus_agent, source_agent, target_agent, kind, event, content, timestamp):
    return {"event": event, "content": content}

reducer.add_reduction_rule("стимул", my_reduction_function)
reducer.add_reduction_rule("действие", my_reduction_function)

reduction = reducer.reduce_agent(agent)
print(reduction)
```

### `ResultsReducer.reduce_agent_to_dataframe`

```python
def reduce_agent_to_dataframe(self, agent: TinyPerson, column_names: list = None) -> pd.DataFrame:
    """ Undocumented """
```

**Назначение**: Преобразование уменьшенных данных агента в DataFrame.

**Параметры**:

- `agent` (TinyPerson): Агент, данные которого необходимо уменьшить и преобразовать в DataFrame.
- `column_names` (list, optional): Список имен столбцов для DataFrame. По умолчанию `None`.

**Возвращает**:

- `pd.DataFrame`: DataFrame, содержащий уменьшенные данные агента.

**Как работает функция**:

1.  **Уменьшение данных агента**: Вызывает метод `self.reduce_agent(agent)` для получения уменьшенных данных агента.
2.  **Создание DataFrame**: Создает DataFrame из уменьшенных данных с использованием `pd.DataFrame()`. Если указаны имена столбцов, они используются для DataFrame.
3.  **Возврат DataFrame**: Функция возвращает созданный DataFrame.

**ASCII схема работы функции**:

```
    Начало
    │
    ├──► Уменьшение данных агента (self.reduce_agent(agent))
    │
    └──► Создание DataFrame (pd.DataFrame)
    │
    Конец
```

**Примеры**:

```python
from extraction import ResultsReducer
from tinytroupe.agent import TinyPerson
import pandas as pd

# Создание экземпляра ResultsReducer
reducer = ResultsReducer()

# Создание экземпляра агента (предполагается, что TinyPerson инициализирован)
agent = TinyPerson(name='Alice')
agent.episodic_memory.store({"role": "user", "content": {"stimuli": [{"type": "стимул", "content": "содержимое", "source": "источник"}]}, "simulation_timestamp": 1})
agent.episodic_memory.store({"role": "assistant", "content": {"action": {"type": "действие", "content": "содержимое", "target": "цель"}}, "simulation_timestamp": 2})

# Пример: Преобразование уменьшенных данных в DataFrame
def my_reduction_function(focus_agent, source_agent, target_agent, kind, event, content, timestamp):
    return {"event": event, "content": content}

reducer.add_reduction_rule("стимул", my_reduction_function)
reducer.add_reduction_rule("действие", my_reduction_function)

df = reducer.reduce_agent_to_dataframe(agent, column_names=["event", "content"])
print(df)
```

### `ArtifactExporter.export`

```python
def export(self, artifact_name:str, artifact_data:Union[dict, str], content_type:str, content_format:str=None, target_format:str="txt", verbose:bool=False) -> None:
    """
    Exports the specified artifact data to a file.

    Args:
        artifact_name (str): The name of the artifact.
        artifact_data (Union[dict, str]): The data to export. If a dict is given, it will be saved as JSON. 
            If a string is given, it will be saved as is.
        content_type (str): The type of the content within the artifact.
        content_format (str, optional): The format of the content within the artifact (e.g., md, csv, etc). Defaults to None.
        target_format (str): The format to export the artifact to (e.g., json, txt, docx, etc).
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """
```

**Назначение**: Экспорт данных артефакта в файл в указанном формате.

**Параметры**:

- `artifact_name` (str): Имя артефакта.
- `artifact_data` (Union[dict, str]): Данные для экспорта. Если это словарь, он будет сохранен в формате JSON. Если это строка, она будет сохранена как есть.
- `content_type` (str): Тип контента в артефакте.
- `content_format` (str, optional): Формат контента в артефакте (например, md, csv и т.д.). По умолчанию `None`.
- `target_format` (str): Формат, в который нужно экспортировать артефакт (например, json, txt, docx и т.д.).
- `verbose` (bool, optional): Выводить ли отладочные сообщения. По умолчанию `False`.

**Как работает функция**:

1.  **Дедупликация отступов**: Удаляет лишние отступы из данных артефакта, чтобы обеспечить правильное форматирование.
2.  **Очистка имени артефакта**: Заменяет недопустимые символы в имени артефакта на дефисы.
3.  **Формирование пути к файлу**: Формирует полный путь к файлу, в который будет сохранен артефакт.
4.  **Экспорт в указанном формате**: В зависимости от `target_format` вызывается соответствующий метод для экспорта данных:
    - `"json"`: `self._export_as_json()`
    - `"txt"`, `"text"`, `"md"`, `"markdown"`: `self._export_as_txt()`
    - `"docx"`: `self._export_as_docx()`
5.  **Обработка ошибок**: Если `target_format` не поддерживается, выбрасывается исключение `ValueError`.

**ASCII схема работы функции**:

```
    Начало
    │
    ├──