# Модуль DeepSeek.py

## Обзор

Модуль `DeepSeek.py` предоставляет класс `DeepSeek`, который является наследником класса `OpenaiAPI`.
Этот класс предназначен для взаимодействия с API DeepSeek, предоставляя функциональность для работы с моделью deepseek-chat.
Модуль определяет базовые параметры подключения к сервису DeepSeek, такие как URL, необходимость аутентификации, поддержку потоковой передачи и истории сообщений.

## Подробней

Модуль `DeepSeek` используется для упрощения взаимодействия с API DeepSeek. Он наследует основные функции от `OpenaiAPI` и переопределяет некоторые атрибуты для соответствия спецификациям DeepSeek. Это позволяет единообразно использовать различные модели, предоставляемые через API, такие как `deepseek-chat`.

## Классы

### `DeepSeek`

**Описание**: Класс `DeepSeek` предназначен для взаимодействия с API DeepSeek.

**Наследует**:
- `OpenaiAPI`: Класс наследует функциональность для работы с API OpenAI и адаптирует её для DeepSeek.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая провайдера как "DeepSeek".
- `url` (str): URL платформы DeepSeek: "https://platform.deepseek.com".
- `login_url` (str): URL для получения API ключей DeepSeek: "https://platform.deepseek.com/api_keys".
- `working` (bool): Указывает, что провайдер находится в рабочем состоянии: `True`.
- `api_base` (str): Базовый URL API DeepSeek: "https://api.deepseek.com".
- `needs_auth` (bool): Указывает на необходимость аутентификации для работы с API: `True`.
- `supports_stream` (bool): Указывает на поддержку потоковой передачи данных: `True`.
- `supports_message_history` (bool): Указывает на поддержку истории сообщений: `True`.
- `default_model` (str): Модель, используемая по умолчанию: "deepseek-chat".
- `fallback_models` (list[str]): Список моделей для переключения в случае проблем с основной моделью.

```python
from __future__ import annotations

from .OpenaiAPI import OpenaiAPI

class DeepSeek(OpenaiAPI):
    """
    Класс для взаимодействия с API DeepSeek.

    Inherits:
        OpenaiAPI: Наследует функциональность для работы с API OpenAI и адаптирует её для DeepSeek.

    Attributes:
        label (str): Метка, идентифицирующая провайдера как "DeepSeek".
        url (str): URL платформы DeepSeek.
        login_url (str): URL для получения API ключей DeepSeek.
        working (bool): Указывает, что провайдер находится в рабочем состоянии.
        api_base (str): Базовый URL API DeepSeek.
        needs_auth (bool): Указывает на необходимость аутентификации для работы с API.
        supports_stream (bool): Указывает на поддержку потоковой передачи данных.
        supports_message_history (bool): Указывает на поддержку истории сообщений.
        default_model (str): Модель, используемая по умолчанию.
        fallback_models (list[str]): Список моделей для переключения в случае проблем с основной моделью.
    """
    label = "DeepSeek"
    url = "https://platform.deepseek.com"
    login_url = "https://platform.deepseek.com/api_keys"
    working = True
    api_base = "https://api.deepseek.com"
    needs_auth = True
    supports_stream = True
    supports_message_history = True
    default_model = "deepseek-chat"
    fallback_models = [default_model]