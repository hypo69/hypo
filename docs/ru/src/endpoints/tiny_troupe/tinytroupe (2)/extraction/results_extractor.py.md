# Модуль `results_extractor.py`

## Обзор

Модуль предназначен для извлечения результатов из взаимодействий агентов в среде `TinyTroupe`. Он содержит класс `ResultsExtractor`, который использует OpenAI для анализа истории взаимодействий агентов и извлечения ключевой информации на основе заданных целей и подсказок.

## Подробней

Этот модуль позволяет анализировать поведение агентов в смоделированной среде, извлекая полезные данные из их взаимодействий. Он использует шаблоны для формирования запросов к OpenAI, настраивая цели извлечения и предоставляя контекст в виде истории взаимодействий агентов. Результаты извлечения кэшируются для последующего использования и могут быть сохранены в формате JSON.

## Классы

### `ResultsExtractor`

**Описание**: Класс предназначен для извлечения результатов из взаимодействий агентов в среде `TinyTroupe`.

**Принцип работы**: Класс инициализируется с путем к шаблону запроса, целями извлечения, ситуацией, списком полей и подсказками для полей. Он предоставляет методы для извлечения результатов из отдельных агентов или всей среды, используя OpenAI для анализа текста взаимодействий. Результаты кэшируются и могут быть сохранены в формате JSON.

**Атрибуты**:

-   `_extraction_prompt_template_path` (str): Путь к файлу шаблона запроса для извлечения информации.
-   `default_extraction_objective` (str): Цель извлечения по умолчанию (например, "основные моменты в истории взаимодействий агентов").
-   `default_situation` (str): Ситуация по умолчанию, описывающая контекст анализа.
-   `default_fields` (List[str] | None): Список полей для извлечения по умолчанию.
-   `default_fields_hints` (dict | None): Подсказки для полей извлечения по умолчанию.
-   `default_verbose` (bool): Флаг для включения/выключения отладочных сообщений по умолчанию.
-   `agent_extraction` (dict): Кэш последних извлеченных результатов для агентов.
-   `world_extraction` (dict): Кэш последних извлеченных результатов для всей среды.

**Методы**:

-   `__init__`: Инициализирует экземпляр класса `ResultsExtractor` с параметрами по умолчанию.
-   `extract_results_from_agents`: Извлекает результаты из списка агентов.
-   `extract_results_from_agent`: Извлекает результаты из одного агента.
-   `extract_results_from_world`: Извлекает результаты из всей среды.
-   `save_as_json`: Сохраняет последние извлеченные результаты в файл JSON.
-   `_get_default_values_if_necessary`: Возвращает значения по умолчанию для параметров, если они не были переданы.

#### `__init__`

```python
def __init__(self, 
             extraction_prompt_template_path:str = os.path.join(os.path.dirname(__file__), './prompts/interaction_results_extractor.mustache'),
             extraction_objective:str = "The main points present in the agents' interactions history.",
             situation:str = "",
             fields:List[str] = None,
             fields_hints:dict = None,
             verbose:bool = False):
    """
    Initializes the ResultsExtractor with default parameters.

    Args:
        extraction_prompt_template_path (str): The path to the extraction prompt template.
        extraction_objective (str): The default extraction objective.
        situation (str): The default situation to consider.
        fields (List[str], optional): The default fields to extract. Defaults to None.
        fields_hints (dict, optional): The default hints for the fields to extract. Defaults to None.
        verbose (bool, optional): Whether to print debug messages by default. Defaults to False.
    """
```

**Назначение**: Инициализирует экземпляр класса `ResultsExtractor`.

**Параметры**:

-   `extraction_prompt_template_path` (str): Путь к шаблону запроса для извлечения информации. По умолчанию указывает на файл `interaction_results_extractor.mustache` в поддиректории `prompts`.
-   `extraction_objective` (str): Цель извлечения по умолчанию. По умолчанию: "The main points present in the agents' interactions history.".
-   `situation` (str): Описание ситуации по умолчанию. По умолчанию пустая строка.
-   `fields` (List[str] | None): Список полей для извлечения по умолчанию. По умолчанию `None`.
-   `fields_hints` (dict | None): Подсказки для полей извлечения по умолчанию. По умолчанию `None`.
-   `verbose` (bool): Флаг для включения/выключения отладочных сообщений по умолчанию. По умолчанию `False`.

**Как работает функция**:

1.  Сохраняет путь к шаблону запроса `extraction_prompt_template_path` в атрибуте `self._extraction_prompt_template_path`.
2.  Устанавливает значения по умолчанию для цели извлечения, ситуации, полей, подсказок для полей и флага `verbose`.
3.  Инициализирует кэш для хранения извлеченных данных агентов (`self.agent_extraction`) и среды (`self.world_extraction`).

**Примеры**:

```python
extractor = ResultsExtractor()  # Инициализация с параметрами по умолчанию
extractor = ResultsExtractor(verbose=True)  # Инициализация с включенным режимом отладки
```

#### `extract_results_from_agents`

```python
def extract_results_from_agents(self,
                                    agents:List[TinyPerson],
                                    extraction_objective:str=None,
                                    situation:str =None,
                                    fields:list=None,
                                    fields_hints:dict=None,
                                    verbose:bool=None):
    """
    Extracts results from a list of TinyPerson instances.

    Args:
        agents (List[TinyPerson]): The list of TinyPerson instances to extract results from.
        extraction_objective (str): The extraction objective.
        situation (str): The situation to consider.
        fields (list, optional): The fields to extract. If None, the extractor will decide what names to use. 
            Defaults to None.
        fields_hints (dict, optional): Hints for the fields to extract. Maps field names to strings with the hints. Defaults to None.
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """
```

**Назначение**: Извлекает результаты из списка агентов (`TinyPerson`).

**Параметры**:

-   `agents` (List[TinyPerson]): Список экземпляров `TinyPerson`, из которых нужно извлечь результаты.
-   `extraction_objective` (str | None): Цель извлечения. Если `None`, используется значение по умолчанию.
-   `situation` (str | None): Описание ситуации. Если `None`, используется значение по умолчанию.
-   `fields` (list | None): Список полей для извлечения. Если `None`, экстрактор сам определяет, какие имена использовать.
-   `fields_hints` (dict | None): Подсказки для полей извлечения. Соответствует именам полей строкам с подсказками.
-   `verbose` (bool | None): Флаг для включения/выключения отладочных сообщений. Если `None`, используется значение по умолчанию.

**Возвращает**:

-   `results` (list): Список результатов, извлеченных из каждого агента.

**Как работает функция**:

1.  Инициализирует пустой список `results`.
2.  Перебирает каждого агента в списке `agents`.
3.  Для каждого агента вызывает метод `extract_results_from_agent` для извлечения результатов.
4.  Добавляет результат в список `results`.
5.  Возвращает список `results`.

```
     Начало
     │
     │ agents: List[TinyPerson], extraction_objective: str, situation: str, fields: list, fields_hints: dict, verbose: bool
     │
     │ results = []
     │
     loop по agent in agents
     │
     │ result = self.extract_results_from_agent(agent, extraction_objective, situation, fields, fields_hints, verbose)
     │
     │ results.append(result)
     │
     Конец цикла
     │
     │ return results
     │
     Конец
```

**Примеры**:

```python
# Предположим, что у нас есть список агентов и экземпляр ResultsExtractor
agents = [TinyPerson(), TinyPerson()]
extractor = ResultsExtractor()
results = extractor.extract_results_from_agents(agents, extraction_objective="Find the main goal")
print(results)
```

#### `extract_results_from_agent`

```python
def extract_results_from_agent(self, 
                    tinyperson:TinyPerson, 
                    extraction_objective:str="The main points present in the agent's interactions history.", 
                    situation:str = "", 
                    fields:list=None,
                    fields_hints:dict=None,
                    verbose:bool=None):
    """
    Extracts results from a TinyPerson instance.

    Args:
        tinyperson (TinyPerson): The TinyPerson instance to extract results from.
        extraction_objective (str): The extraction objective.
        situation (str): The situation to consider.
        fields (list, optional): The fields to extract. If None, the extractor will decide what names to use. 
            Defaults to None.
        fields_hints (dict, optional): Hints for the fields to extract. Maps field names to strings with the hints. Defaults to None.
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """
```

**Назначение**: Извлекает результаты из экземпляра `TinyPerson`.

**Параметры**:

-   `tinyperson` (TinyPerson): Экземпляр `TinyPerson`, из которого нужно извлечь результаты.
-   `extraction_objective` (str): Цель извлечения. По умолчанию: "The main points present in the agent's interactions history.".
-   `situation` (str): Описание ситуации. По умолчанию пустая строка.
-   `fields` (list | None): Список полей для извлечения. Если `None`, экстрактор сам определяет, какие имена использовать. По умолчанию `None`.
-   `fields_hints` (dict | None): Подсказки для полей извлечения. Соответствует именам полей строкам с подсказками. По умолчанию `None`.
-   `verbose` (bool | None): Флаг для включения/выключения отладочных сообщений. Если `None`, используется значение по умолчанию. По умолчанию `False`.

**Возвращает**:

-   `result` (dict | None): Извлеченные результаты в виде словаря или `None`, если извлечение не удалось.

**Как работает функция**:

1.  Получает значения по умолчанию для параметров, если они не были переданы. Использует `_get_default_values_if_necessary` для этого.
2.  Инициализирует пустой список `messages`.
3.  Создает словарь `rendering_configs` для хранения конфигураций рендеринга. Если `fields` не `None`, добавляет их в `rendering_configs`. Если `fields_hints` не `None`, добавляет их в `rendering_configs`.
4.  Добавляет системное сообщение в список `messages` с использованием шаблона из файла, указанного в `self._extraction_prompt_template_path`.
5.  Получает историю взаимодействий агента с помощью `tinyperson.pretty_current_interactions`.
6.  Формирует запрос к OpenAI, включая цель извлечения, ситуацию и историю взаимодействий агента.
7.  Отправляет запрос в OpenAI с помощью `openai_utils.client().send_message`.
8.  Извлекает JSON из ответа OpenAI с помощью `utils.extract_json`.
9.  Кэширует результат в `self.agent_extraction`.
10. Возвращает результат.

```
     Начало
     │
     │ tinyperson: TinyPerson, extraction_objective: str, situation: str, fields: list, fields_hints: dict, verbose: bool
     │
     │ extraction_objective, situation, fields, fields_hints, verbose = self._get_default_values_if_necessary(...)
     │
     │ messages = []
     │
     │ rendering_configs = {}
     │
     │ if fields is not None: rendering_configs["fields"] = ", ".join(fields)
     │
     │ if fields_hints is not None: rendering_configs["fields_hints"] = list(fields_hints.items())
     │
     │ messages.append({"role": "system", "content": chevron.render(...)})
     │
     │ interaction_history = tinyperson.pretty_current_interactions(...)
     │
     │ extraction_request_prompt = f"""..."""
     │
     │ messages.append({"role": "user", "content": extraction_request_prompt})
     │
     │ next_message = openai_utils.client().send_message(messages, ...)
     │
     │ result = utils.extract_json(next_message["content"])
     │
     │ self.agent_extraction[tinyperson.name] = result
     │
     │ return result
     │
     Конец
```

**Примеры**:

```python
# Предположим, что у нас есть экземпляр TinyPerson и ResultsExtractor
agent = TinyPerson()
extractor = ResultsExtractor()
result = extractor.extract_results_from_agent(agent, extraction_objective="Find the main goal")
print(result)
```

#### `extract_results_from_world`

```python
def extract_results_from_world(self, 
                                   tinyworld:TinyWorld, 
                                   extraction_objective:str="The main points that can be derived from the agents conversations and actions.", 
                                   situation:str="", 
                                   fields:list=None,
                                   fields_hints:dict=None,
                                   verbose:bool=None):
    """
    Extracts results from a TinyWorld instance.

    Args:
        tinyworld (TinyWorld): The TinyWorld instance to extract results from.
        extraction_objective (str): The extraction objective.
        situation (str): The situation to consider.
        fields (list, optional): The fields to extract. If None, the extractor will decide what names to use. 
            Defaults to None.
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """
```

**Назначение**: Извлекает результаты из экземпляра `TinyWorld`.

**Параметры**:

-   `tinyworld` (TinyWorld): Экземпляр `TinyWorld`, из которого нужно извлечь результаты.
-   `extraction_objective` (str): Цель извлечения. По умолчанию: "The main points that can be derived from the agents conversations and actions.".
-   `situation` (str): Описание ситуации. По умолчанию пустая строка.
-   `fields` (list | None): Список полей для извлечения. Если `None`, экстрактор сам определяет, какие имена использовать. По умолчанию `None`.
-   `fields_hints` (dict | None): Подсказки для полей извлечения. Соответствует именам полей строкам с подсказками.
-   `verbose` (bool | None): Флаг для включения/выключения отладочных сообщений. Если `None`, используется значение по умолчанию. По умолчанию `False`.

**Возвращает**:

-   `result` (dict | None): Извлеченные результаты в виде словаря или `None`, если извлечение не удалось.

**Как работает функция**:

1.  Получает значения по умолчанию для параметров, если они не были переданы. Использует `_get_default_values_if_necessary` для этого.
2.  Инициализирует пустой список `messages`.
3.  Создает словарь `rendering_configs` для хранения конфигураций рендеринга. Если `fields` не `None`, добавляет их в `rendering_configs`. Если `fields_hints` не `None`, добавляет их в `rendering_configs`.
4.  Добавляет системное сообщение в список `messages` с использованием шаблона из файла, указанного в `self._extraction_prompt_template_path`.
5.  Получает историю взаимодействий в мире с помощью `tinyworld.pretty_current_interactions`.
6.  Формирует запрос к OpenAI, включая цель извлечения, ситуацию и историю взаимодействий.
7.  Отправляет запрос в OpenAI с помощью `openai_utils.client().send_message`.
8.  Извлекает JSON из ответа OpenAI с помощью `utils.extract_json`.
9.  Кэширует результат в `self.world_extraction`.
10. Возвращает результат.

```
     Начало
     │
     │ tinyworld: TinyWorld, extraction_objective: str, situation: str, fields: list, fields_hints: dict, verbose: bool
     │
     │ extraction_objective, situation, fields, fields_hints, verbose = self._get_default_values_if_necessary(...)
     │
     │ messages = []
     │
     │ rendering_configs = {}
     │
     │ if fields is not None: rendering_configs["fields"] = ", ".join(fields)
     │
     │ if fields_hints is not None: rendering_configs["fields_hints"] = list(fields_hints.items())
     │
     │ messages.append({"role": "system", "content": chevron.render(...)})
     │
     │ interaction_history = tinyworld.pretty_current_interactions(...)
     │
     │ extraction_request_prompt = f"""..."""
     │
     │ messages.append({"role": "user", "content": extraction_request_prompt})
     │
     │ next_message = openai_utils.client().send_message(messages, temperature=0.0)
     │
     │ result = utils.extract_json(next_message["content"])
     │
     │ self.world_extraction[tinyworld.name] = result
     │
     │ return result
     │
     Конец
```

**Примеры**:

```python
# Предположим, что у нас есть экземпляр TinyWorld и ResultsExtractor
world = TinyWorld()
extractor = ResultsExtractor()
result = extractor.extract_results_from_world(world, extraction_objective="Find the main trends")
print(result)
```

#### `save_as_json`

```python
def save_as_json(self, filename:str, verbose:bool=False):
    """
    Saves the last extraction results as JSON.

    Args:
        filename (str): The filename to save the JSON to.
        verbose (bool, optional): Whether to print debug messages. Defaults to False.
    """
```

**Назначение**: Сохраняет последние извлеченные результаты в формате JSON в файл.

**Параметры**:

-   `filename` (str): Имя файла для сохранения JSON.
-   `verbose` (bool): Флаг для включения/выключения отладочных сообщений. По умолчанию `False`.

**Как работает функция**:

1.  Открывает файл с указанным именем в режиме записи (`'w'`).
2.  Сохраняет словарь, содержащий извлечения агентов (`self.agent_extraction`) и извлечения среды (`self.world_extraction`), в формате JSON с отступом 4.
3.  Если `verbose` установлен в `True`, выводит сообщение о сохранении файла.

```
     Начало
     │
     │ filename: str, verbose: bool
     │
     │ open(filename, 'w') as f
     │
     │ json.dump({"agent_extractions": self.agent_extraction, "world_extraction": self.world_extraction}, f, indent=4)
     │
     │ if verbose: print(f"Saved extraction results to {filename}")
     │
     Конец
```

**Примеры**:

```python
# Предположим, что у нас есть экземпляр ResultsExtractor
extractor = ResultsExtractor()
extractor.save_as_json("results.json", verbose=True)
```

#### `_get_default_values_if_necessary`

```python
def _get_default_values_if_necessary(self,
                            extraction_objective:str,
                            situation:str,
                            fields:List[str],
                            fields_hints:dict,
                            verbose:bool):
    """

    """
```

**Назначение**: Возвращает значения по умолчанию для параметров, если они не были переданы.

**Параметры**:

-   `extraction_objective` (str): Цель извлечения.
-   `situation` (str): Описание ситуации.
-   `fields` (List[str]): Список полей для извлечения.
-   `fields_hints` (dict): Подсказки для полей извлечения.
-   `verbose` (bool): Флаг для включения/выключения отладочных сообщений.

**Возвращает**:

-   Кортеж значений: `(extraction_objective, situation, fields, fields_hints, verbose)`.

**Как работает функция**:

1.  Проверяет, является ли `extraction_objective` равным `None`. Если да, устанавливает значение по умолчанию из `self.default_extraction_objective`.
2.  Проверяет, является ли `situation` равным `None`. Если да, устанавливает значение по умолчанию из `self.default_situation`.
3.  Проверяет, является ли `fields` равным `None`. Если да, устанавливает значение по умолчанию из `self.default_fields`.
4.  Проверяет, является ли `fields_hints` равным `None`. Если да, устанавливает значение по умолчанию из `self.default_fields_hints`.
5.  Проверяет, является ли `verbose` равным `None`. Если да, устанавливает значение по умолчанию из `self.default_verbose`.
6.  Возвращает кортеж с обновленными значениями параметров.

```
     Начало
     │
     │ extraction_objective: str, situation: str, fields: List[str], fields_hints: dict, verbose: bool
     │
     │ if extraction_objective is None: extraction_objective = self.default_extraction_objective
     │
     │ if situation is None: situation = self.default_situation
     │
     │ if fields is None: fields = self.default_fields
     │
     │ if fields_hints is None: fields_hints = self.default_fields_hints
     │
     │ if verbose is None: verbose = self.default_verbose
     │
     │ return extraction_objective, situation, fields, fields_hints, verbose
     │
     Конец
```

**Примеры**:

```python
# Предположим, что у нас есть экземпляр ResultsExtractor
extractor = ResultsExtractor()
objective, situation, fields, hints, verbose = extractor._get_default_values_if_necessary(None, None, None, None, None)
print(objective, situation, fields, hints, verbose)