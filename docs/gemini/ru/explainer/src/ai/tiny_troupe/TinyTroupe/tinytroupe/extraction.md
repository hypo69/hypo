# <input code>

```python
"""
Simulations produce a lot of data, and it is often useful to extract these data in a structured way. For instance, you might wish to:
  - Extract the main points from an agent's interactions history, so that you can consult them later in a concise form.
  - Generate synthetic data from a simulation, so that you can use it for training machine learning models or testing software.
  - Simply turn some of the data into a more machine-readable format, such as JSON or CSV, so that you can analyze it more easily.

This module provides various utilities to help you extract data from TinyTroupe elements, such as agents and worlds. It also provides a 
mechanism to reduce the extracted data to a more concise form, and to export artifacts from TinyTroupe elements. Incidentaly, it showcases 
one of the many ways in which agent simulations differ from AI assistants, as the latter are not designed to be introspected in this way.
"""

import os
import json
import chevron
import logging
import pandas as pd
import pypandoc
import markdown 
from typing import Union, List
import logging
logger = logging.getLogger("tinytroupe")

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry

from tinytroupe import openai_utils
import tinytroupe.utils as utils
```

```mermaid
graph TD
    subgraph "Data Extraction"
        A[ResultsExtractor] --> B{extract_results_from_agent};
        B --> C[TinyPerson];
        C --> D[pretty_current_interactions];
        D --> E[chevron.render];
        E --> F[openai_utils.client().send_message];
        F --> G[utils.extract_json];
        G --> H[cache result];
        H --> A;
        
        A --> I{extract_results_from_world};
        I --> J[TinyWorld];
        J --> K[pretty_current_interactions];
        K --> E;
        E --> F;
        F --> G;
        G --> H;
        H --> A;
        
    end
    subgraph "Data Reduction"
        L[ResultsReducer] --> M{reduce_agent};
        M --> N[TinyPerson];
        N --> O[episodic_memory.retrieve_all];
        O --> P[if message['role']];
        P -- "system" --> Q[continue];
        P -- "user" --> R[stimulus processing];
        P -- "assistant" --> S[action processing];
        R --> T[self.rules[stimulus_type]];
        R --> U{extracted is not None};
        U -- yes --> V[reduction.append];
        S --> T;
        S --> U;
        T --> V;
        V --> M;
        
    end
    subgraph "Artifact Export"
        W[ArtifactExporter] --> X{export};
        X --> Y[artifact_data];
        Y -- dict --> Z[json.dump];
        Y -- string --> AA[utils.dedent];
        Z --> AB[saving to file];
        AA --> AB;
        
    end
```

# <algorithm>

The code implements a system for extracting and processing data from agent and world simulations using OpenAI API and a set of defined functions and classes.


# <mermaid>

```mermaid
graph TD
    subgraph "Data Extraction"
        A[ResultsExtractor] --> B{extract_results_from_agent};
        B --> C[TinyPerson];
        C --> D[pretty_current_interactions];
        D --> E[chevron.render];
        E --> F[openai_utils.client().send_message];
        F --> G[utils.extract_json];
        G --> H[cache result];
        H --> A;
        
        A --> I{extract_results_from_world};
        I --> J[TinyWorld];
        J --> K[pretty_current_interactions];
        K --> E;
        E --> F;
        F --> G;
        G --> H;
        H --> A;
        
    end
    subgraph "Data Reduction"
        L[ResultsReducer] --> M{reduce_agent};
        M --> N[TinyPerson];
        N --> O[episodic_memory.retrieve_all];
        O --> P[if message['role']];
        P -- "system" --> Q[continue];
        P -- "user" --> R[stimulus processing];
        P -- "assistant" --> S[action processing];
        R --> T[self.rules[stimulus_type]];
        R --> U{extracted is not None};
        U -- yes --> V[reduction.append];
        S --> T;
        S --> U;
        T --> V;
        V --> M;
        
    end
    subgraph "Artifact Export"
        W[ArtifactExporter] --> X{export};
        X --> Y[artifact_data];
        Y -- dict --> Z[json.dump];
        Y -- string --> AA[utils.dedent];
        Z --> AB[saving to file];
        AA --> AB;
        
    end
```

# <explanation>

**Импорты**:
- `os`, `json`, `chevron`, `logging`, `pandas`, `pypandoc`, `markdown`, `typing`: Стандартные библиотеки Python для работы с файлами, JSON, логированием, обработкой данных и т.д.
- `pypandoc`: Библиотека для конвертации между форматами документов (например, Markdown в DOCX).
- `pandas`: Библиотека для работы с DataFrame.
- `markdown`: Библиотека для обработки Markdown.
- `tinytroupe.agent`, `tinytroupe.environment`, `tinytroupe.factory`, `tinytroupe.utils`: Импортируются классы и функции из собственного пакета TinyTroupe, обеспечивая взаимодействие с компонентами моделирования агентов.
- `openai_utils`: Скорее всего, это импорт из пакета `tinytroupe`, предназначенный для взаимодействия с OpenAI API.
- `tinytroupe.utils`: Импортируется модуль `utils` из пакета `tinytroupe` для предоставления различных вспомогательных функций.

**Классы**:
- `ResultsExtractor`:  Класс для извлечения результатов из объектов `TinyPerson` и `TinyWorld` с помощью запросов к OpenAI. Содержит методы `extract_results_from_agent`, `extract_results_from_world`, и `save_as_json`.  Хранит кэшированные результаты.
- `ResultsReducer`: Класс для сокращения извлеченных результатов. Содержит метод `reduce_agent` для обработки истории взаимодействия агента, применяя правила (`self.rules`).
- `ArtifactExporter`:  Класс для экспорта данных в различные форматы (JSON, TXT, DOCX). Реализует методы для экспорта артефактов в файлы. Использует `JsonSerializableRegistry` для сериализации данных.
- `Normalizer`: Класс для нормализации текстовых данных. Использует OpenAI для нормализации списка строк.


**Функции**:
- `extract_results_from_agent`, `extract_results_from_world`:  Получают данные от OpenAI API на основе истории взаимодействия агентов или мира, используя шаблон `interaction_results_extractor.mustache`, для получения структурированных результатов.
- `save_as_json`: Сохраняет кэшированные результаты извлечения в файл JSON.
- `reduce_agent`:  Обрабатывает историю взаимодействия агента, применяя правила для сокращения данных.
- `export`: Экспортирует данные в указанный формат файла.
- `_export_as_txt`, `_export_as_json`, `_export_as_docx`:  Вспомогательные функции для экспорта данных в различные форматы.
- `normalize`: Нормализует входные данные с помощью запроса к OpenAI API.

**Переменные**:
- `_extraction_prompt_template_path`: Путь к шаблону запроса к OpenAI.
- `agent_extraction`, `world_extraction`: Словари для хранения кэшированных результатов извлечения.
- `rules`: Словарь для хранения правил сокращения результатов.

**Возможные ошибки и улучшения**:
- Обработка исключений при работе с файлами и OpenAI API могла бы быть улучшена.
- Добавление проверки валидности входных данных (типы, форматы) сделало бы код более robust.
- Улучшение методов для работы с различными форматами данных (например, DOCX) может повысить гибкость.
- Использование логирования с разными уровнями важности (DEBUG, INFO, WARNING) улучшило бы отладку и сопровождение кода.
- Явное указание типов для переменных улучшило бы понятность кода и уменьшило бы количество ошибок.


**Цепочка взаимосвязей**:
Код реализует обработку данных от взаимодействия агентов и мира. `ResultsExtractor` извлекает данные с помощью OpenAI, `ResultsReducer` обрабатывает эти данные, а `ArtifactExporter` экспортирует результаты в файлы.  Функции `extract_results_from_agent` и `extract_results_from_world` напрямую зависят от `openai_utils` для работы с API OpenAI.

**Замечания**:

- Шаблон `interaction_results_extractor.mustache` (не представлен в коде) определяет структуру запросов к OpenAI.
- Приведенный код предоставляет общую структуру; для полной работы необходимо наличие соответствующих данных и других файлов проекта (например, определения классов `TinyPerson` и `TinyWorld`).
- Вероятно, код предназначен для обработки больших данных из симуляций, что может потребовать оптимизаций в зависимости от масштаба проекта.
- Логирование используется, но его конфигурация и использование могли бы быть более полными.