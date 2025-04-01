# Документация модуля LambdaChat

## Обзор

Модуль `LambdaChat` предоставляет класс для взаимодействия с сервисом Lambda Chat, который является одним из провайдеров в g4f (GPT4Free). Он наследуется от класса `HuggingChat` и содержит специфические настройки и параметры, относящиеся к Lambda Chat.

## Подробнее

Этот модуль определяет параметры подключения и работы с сервисом Lambda Chat, включая URL, используемые модели и их алиасы. Он также указывает, что для работы не требуется драйвер или авторизация.

## Классы

### `LambdaChat`

**Описание**: Класс `LambdaChat` предназначен для взаимодействия с сервисом Lambda Chat. Он наследуется от `HuggingChat` и переопределяет некоторые атрибуты для соответствия особенностям этого провайдера.

**Принцип работы**:
1. Класс наследует функциональность от `HuggingChat`, предоставляя базовые методы для взаимодействия с чат-сервисами.
2. Определяются специфичные для `LambdaChat` атрибуты, такие как домен, URL, список моделей и их алиасы.
3. Указывается, что для работы с `LambdaChat` не требуется драйвер (`use_nodriver = False`) и авторизация (`needs_auth = False`).

**Атрибуты**:
- `label` (str): Название провайдера ("Lambda Chat").
- `domain` (str): Доменное имя сервиса ("lambda.chat").
- `origin` (str): Базовый URL сервиса (f"https://{domain}").
- `url` (str): Полный URL сервиса (совпадает с `origin`).
- `working` (bool): Указывает, что провайдер находится в рабочем состоянии (True).
- `use_nodriver` (bool): Указывает, что драйвер не требуется (False).
- `needs_auth` (bool): Указывает, что авторизация не требуется (False).
- `default_model` (str): Модель, используемая по умолчанию ("deepseek-llama3.3-70b").
- `reasoning_model` (str): Модель для логических рассуждений ("deepseek-r1").
- `image_models` (List[str]): Список моделей для обработки изображений (пустой список).
- `fallback_models` (List[str]): Список моделей, используемых в случае сбоя основной модели.
- `models` (List[str]): Копия списка `fallback_models`, используемая для хранения доступных моделей.
- `model_aliases` (Dict[str, str]): Словарь, содержащий алиасы для моделей.

## Функции

В данном классе функции отсутствуют

**Примеры**

```python
from .hf.HuggingChat import HuggingChat

class LambdaChat(HuggingChat):
    label = "Lambda Chat"
    domain = "lambda.chat"
    origin = f"https://{domain}"
    url = origin
    working = True
    use_nodriver = False
    needs_auth = False

    default_model = "deepseek-llama3.3-70b"
    reasoning_model = "deepseek-r1"
    image_models = []
    fallback_models = [
        default_model,
        reasoning_model,
        "hermes-3-llama-3.1-405b-fp8",
        "llama3.1-nemotron-70b-instruct",
        "lfm-40b",
        "llama3.3-70b-instruct-fp8"
    ]
    models = fallback_models.copy()
    
    model_aliases = {
        "deepseek-v3": default_model,
        "hermes-3": "hermes-3-llama-3.1-405b-fp8",
        "nemotron-70b": "llama3.1-nemotron-70b-instruct",
        "llama-3.3-70b": "llama3.3-70b-instruct-fp8"
    }

# Пример использования (не требует создания экземпляра, так как используются атрибуты класса):
print(LambdaChat.label)
print(LambdaChat.default_model)