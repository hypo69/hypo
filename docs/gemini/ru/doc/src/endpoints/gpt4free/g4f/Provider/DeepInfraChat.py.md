# Модуль DeepInfraChat

## Обзор

Модуль `DeepInfraChat.py` предназначен для взаимодействия с платформой DeepInfra Chat через API OpenAI. Он определяет класс `DeepInfraChat`, который является подклассом `OpenaiTemplate` и предоставляет конфигурацию для работы с различными моделями, размещенными на DeepInfra.

## Подробней

Этот модуль предоставляет удобный способ использования различных AI-моделей, доступных через DeepInfra Chat. Он определяет URL, базовый URL API, список поддерживаемых моделей и их псевдонимы. Это позволяет легко переключаться между разными моделями и использовать их в проекте `hypotez`.

## Классы

### `DeepInfraChat`

**Описание**: Класс `DeepInfraChat` предоставляет конфигурацию для взаимодействия с платформой DeepInfra Chat.

**Наследует**:
- `OpenaiTemplate`: Этот класс наследует функциональность из `OpenaiTemplate`, который, вероятно, предоставляет базовую реализацию для взаимодействия с API OpenAI.

**Аттрибуты**:
- `url` (str): URL для доступа к DeepInfra Chat. Значение: `"https://deepinfra.com/chat"`.
- `api_base` (str): Базовый URL для API OpenAI на DeepInfra. Значение: `"https://api.deepinfra.com/v1/openai"`.
- `working` (bool): Указывает, что провайдер работает. Значение: `True`.
- `default_model` (str): Модель, используемая по умолчанию. Значение: `'deepseek-ai/DeepSeek-V3'`.
- `default_vision_model` (str): Модель для обработки изображений по умолчанию. Значение: `'openbmb/MiniCPM-Llama3-V-2_5'`.
- `vision_models` (list[str]): Список моделей, поддерживающих обработку изображений.
- `models` (list[str]): Список поддерживаемых моделей.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей для удобства использования.

**Принцип работы**:
Класс `DeepInfraChat` определяет атрибуты, необходимые для подключения и работы с DeepInfra Chat. Он наследует базовую функциональность от `OpenaiTemplate` и переопределяет необходимые параметры, такие как URL, API base и список поддерживаемых моделей.

## Функции

В данном модуле функции отсутствуют.

## Примеры

Примеры использования данного класса могут включать создание экземпляра класса `DeepInfraChat` и использование его для отправки запросов к API DeepInfra Chat. Например:

```python
from src.endpoints.gpt4free.g4f.Provider.DeepInfraChat import DeepInfraChat

deep_infra_chat = DeepInfraChat()
print(deep_infra_chat.url)
print(deep_infra_chat.default_model)