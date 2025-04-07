# Модуль PerplexityApi

## Обзор

Модуль `PerplexityApi` предоставляет класс `PerplexityApi`, который используется для взаимодействия с API Perplexity.AI. Этот класс наследует от `OpenaiTemplate` и содержит информацию, необходимую для аутентификации и выполнения запросов к API Perplexity.

## Подробней

Этот модуль является частью системы `gpt4free` проекта `hypotez` и предназначен для обеспечения доступа к различным моделям Perplexity.AI. Он определяет URL, базовый API и список поддерживаемых моделей. Для работы с API требуется аутентификация.

## Классы

### `PerplexityApi`

**Описание**: Класс для взаимодействия с API Perplexity.AI.

**Наследует**:
- `OpenaiTemplate`: Предоставляет общую структуру для работы с API, подобными OpenAI.

**Атрибуты**:
- `label` (str): Метка для API ("Perplexity API").
- `url` (str): URL главной страницы Perplexity.AI ("https://www.perplexity.ai").
- `login_url` (str): URL страницы настроек API для получения ключа ("https://www.perplexity.ai/settings/api").
- `working` (bool): Указывает, что API в настоящее время работоспособен (`True`).
- `needs_auth` (bool): Указывает, что для работы с API требуется аутентификация (`True`).
- `api_base` (str): Базовый URL API Perplexity.AI ("https://api.perplexity.ai").
- `default_model` (str): Модель, используемая по умолчанию ("llama-3-sonar-large-32k-online").
- `models` (List[str]): Список поддерживаемых моделей.

```python
class PerplexityApi(OpenaiTemplate):
    """Класс для взаимодействия с API Perplexity.AI.
    Inherits:
        OpenaiTemplate: Предоставляет общую структуру для работы с API, подобными OpenAI.

    Attributes:
        label (str): Метка для API ("Perplexity API").
        url (str): URL главной страницы Perplexity.AI ("https://www.perplexity.ai").
        login_url (str): URL страницы настроек API для получения ключа ("https://www.perplexity.ai/settings/api").
        working (bool): Указывает, что API в настоящее время работоспособен (`True`).
        needs_auth (bool): Указывает, что для работы с API требуется аутентификация (`True`).
        api_base (str): Базовый URL API Perplexity.AI ("https://api.perplexity.ai").
        default_model (str): Модель, используемая по умолчанию ("llama-3-sonar-large-32k-online").
        models (List[str]): Список поддерживаемых моделей.
    """
```
```python
    label = "Perplexity API"
    url = "https://www.perplexity.ai"
    login_url = "https://www.perplexity.ai/settings/api"
    working = True
    needs_auth = True
    api_base = "https://api.perplexity.ai"
    default_model = "llama-3-sonar-large-32k-online"
    models = [
        "llama-3-sonar-small-32k-chat",
        default_model,
        "llama-3-sonar-large-32k-chat",
        "llama-3-sonar-large-32k-online",
        "llama-3-8b-instruct",
        "llama-3-70b-instruct",
    ]
```
**Примеры**:

```python
from ..template import OpenaiTemplate

class PerplexityApi(OpenaiTemplate):
    label = "Perplexity API"
    url = "https://www.perplexity.ai"
    login_url = "https://www.perplexity.ai/settings/api"
    working = True
    needs_auth = True
    api_base = "https://api.perplexity.ai"
    default_model = "llama-3-sonar-large-32k-online"
    models = [
        "llama-3-sonar-small-32k-chat",
        default_model,
        "llama-3-sonar-large-32k-chat",
        "llama-3-sonar-large-32k-online",
        "llama-3-8b-instruct",
        "llama-3-70b-instruct",
    ]