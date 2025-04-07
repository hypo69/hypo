# Модуль GlhfChat
## Обзор

Модуль `GlhfChat` представляет собой класс `GlhfChat`, который наследуется от `OpenaiTemplate` и предназначен для взаимодействия с сервисом Glhf.chat. Он определяет URL-адреса, необходимые для подключения к сервису, а также список поддерживаемых моделей. Модуль требует авторизации.

## Подробней

Этот модуль является частью проекта `hypotez` и предоставляет интерфейс для работы с Glhf.chat, используя API OpenAI. Класс `GlhfChat` содержит информацию о конечных точках (URL), необходимых для аутентификации и взаимодействия с сервисом. Он также определяет список моделей, которые поддерживаются сервисом Glhf.chat.

## Классы

### `GlhfChat`

**Описание**: Класс `GlhfChat` предоставляет интерфейс для взаимодействия с сервисом Glhf.chat, который использует API OpenAI.

**Наследует**:
- `OpenaiTemplate`: Этот класс наследуется от `OpenaiTemplate`, который, вероятно, содержит общую логику для взаимодействия с API OpenAI.

**Атрибуты**:
- `url` (str): URL-адрес сервиса Glhf.chat (`https://glhf.chat`).
- `login_url` (str): URL-адрес для авторизации (`https://glhf.chat/user-settings/api`).
- `api_base` (str): Базовый URL-адрес API OpenAI (`https://glhf.chat/api/openai/v1`).
- `working` (bool): Флаг, указывающий, что сервис работает (True).
- `needs_auth` (bool): Флаг, указывающий, что для работы требуется авторизация (True).
- `default_model` (str): Модель, используемая по умолчанию (`hf:meta-llama/Llama-3.3-70B-Instruct`).
- `models` (List[str]): Список поддерживаемых моделей.

**Методы**:
- Нет явных методов, кроме атрибутов класса.

```python
from __future__ import annotations

from ..template import OpenaiTemplate

class GlhfChat(OpenaiTemplate):
    """
    Класс для взаимодействия с сервисом Glhf.chat, использующим API OpenAI.
    
    Inherits:
        OpenaiTemplate: Наследует общую логику для взаимодействия с API OpenAI.

    Attributes:
        url (str): URL-адрес сервиса Glhf.chat.
        login_url (str): URL-адрес для авторизации.
        api_base (str): Базовый URL-адрес API OpenAI.
        working (bool): Флаг, указывающий, что сервис работает.
        needs_auth (bool): Флаг, указывающий, что для работы требуется авторизация.
        default_model (str): Модель, используемая по умолчанию.
        models (List[str]): Список поддерживаемых моделей.
    """
    url = "https://glhf.chat"
    login_url = "https://glhf.chat/user-settings/api"
    api_base = "https://glhf.chat/api/openai/v1"

    working = True
    needs_auth = True

    default_model = "hf:meta-llama/Llama-3.3-70B-Instruct"
    models = ["hf:meta-llama/Llama-3.1-405B-Instruct", default_model, "hf:deepseek-ai/DeepSeek-V3", "hf:Qwen/QwQ-32B-Preview", "hf:huihui-ai/Llama-3.3-70B-Instruct-abliterated", "hf:anthracite-org/magnum-v4-12b", "hf:meta-llama/Llama-3.1-70B-Instruct", "hf:meta-llama/Llama-3.1-8B-Instruct", "hf:meta-llama/Llama-3.2-3B-Instruct", "hf:meta-llama/Llama-3.2-11B-Vision-Instruct", "hf:meta-llama/Llama-3.2-90B-Vision-Instruct", "hf:Qwen/Qwen2.5-72B-Instruct", "hf:Qwen/Qwen2.5-Coder-32B-Instruct", "hf:google/gemma-2-9b-it", "hf:google/gemma-2-27b-it", "hf:mistralai/Mistral-7B-Instruct-v0.3", "hf:mistralai/Mixtral-8x7B-Instruct-v0.1", "hf:mistralai/Mixtral-8x22B-Instruct-v0.1", "hf:NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO", "hf:Qwen/Qwen2.5-7B-Instruct", "hf:upstage/SOLAR-10.7B-Instruct-v1.0", "hf:nvidia/Llama-3.1-Nemotron-70B-Instruct-HF"]
```
**Принцип работы**:

Класс `GlhfChat` предоставляет конфигурацию для подключения и использования сервиса Glhf.chat. Он задает основные параметры, такие как URL-адреса, флаги состояния и список поддерживаемых моделей. Этот класс, вероятно, используется для создания экземпляров, которые затем применяются для взаимодействия с Glhf.chat через API OpenAI.