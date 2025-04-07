# Модуль OIVSCode

## Обзор

Модуль `OIVSCode` предоставляет класс `OIVSCode`, который является подклассом `OpenaiTemplate`. Он предназначен для взаимодействия с сервером OI VSCode и предоставляет настройки и параметры для работы с моделями OpenAI, включая поддержку потоковой передачи, системных сообщений и истории сообщений.

## Подробней

Этот модуль определяет настройки для конкретного провайдера OpenAI, а именно OI VSCode Server. Он содержит URL, базовый URL API, список поддерживаемых моделей и их псевдонимы. Класс `OIVSCode` наследуется от `OpenaiTemplate` и переопределяет некоторые его атрибуты для адаптации к особенностям OI VSCode Server.

## Классы

### `OIVSCode`

**Описание**: Класс `OIVSCode` представляет собой конфигурацию для провайдера OI VSCode Server, унаследованную от `OpenaiTemplate`.

**Наследует**:

- `OpenaiTemplate`: Класс, предоставляющий базовую структуру для работы с OpenAI.

**Атрибуты**:

- `label` (str): Название провайдера ("OI VSCode Server").
- `url` (str): URL сервера ("https://oi-vscode-server.onrender.com").
- `api_base` (str): Базовый URL API ("https://oi-vscode-server-2.onrender.com/v1").
- `working` (bool): Указывает, работает ли провайдер (True).
- `needs_auth` (bool): Указывает, требуется ли аутентификация (False).
- `supports_stream` (bool): Указывает, поддерживает ли потоковую передачу (True).
- `supports_system_message` (bool): Указывает, поддерживает ли системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли историю сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию ("gpt-4o-mini-2024-07-18").
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию (совпадает с `default_model`).
- `vision_models` (List[str]): Список моделей для работы с изображениями (включает `default_model` и "gpt-4o-mini").
- `models` (List[str]): Полный список поддерживаемых моделей (включает `vision_models` и "deepseek-ai/DeepSeek-V3").
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей, например, `"gpt-4o-mini": "gpt-4o-mini-2024-07-18"`.

## Функции

В данном модуле нет отдельных функций, но класс `OIVSCode` наследует методы от `OpenaiTemplate`.