# Модуль `Glider`

## Обзор

Модуль `Glider` предоставляет класс `Glider`, который является подклассом `OpenaiTemplate` и предназначен для взаимодействия с сервисом Glider. Он определяет специфические параметры, такие как URL, API endpoint и поддерживаемые модели.

## Подробнее

Модуль определяет интеграцию с сервисом Glider, устанавливая конечную точку API и модели, которые могут быть использованы через этот сервис. Класс `Glider` наследует функциональность от `OpenaiTemplate` и переопределяет необходимые атрибуты для работы с Glider.

## Классы

### `Glider`

**Описание**: Класс `Glider` предназначен для взаимодействия с сервисом Glider.

**Наследует**:
- `OpenaiTemplate`: Класс `Glider` наследует атрибуты и методы класса `OpenaiTemplate`.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая провайдера как "Glider".
- `url` (str): URL сервиса Glider ("https://glider.so").
- `api_endpoint` (str): URL API endpoint сервиса Glider ("https://glider.so/api/chat").
- `working` (bool): Указывает, что провайдер в настоящее время работает (значение `True`).
- `default_model` (str): Модель, используемая по умолчанию (`chat-llama-3-1-70b`).
- `models` (list): Список поддерживаемых моделей (`chat-llama-3-1-70b`, `chat-llama-3-1-8b`, `chat-llama-3-2-3b`, `deepseek-ai/DeepSeek-R1`).
- `model_aliases` (dict): Словарь, содержащий псевдонимы моделей для удобства использования.

**Методы**:
- Нет явно определенных методов, но наследует методы от `OpenaiTemplate`.

## Функции

В данном модуле функции отсутствуют.

## Примеры

Пример использования класса `Glider`:

```python
from src.endpoints.gpt4free.g4f.Provider.Glider import Glider

glider = Glider()
print(f"Label: {glider.label}")
print(f"API Endpoint: {glider.api_endpoint}")
print(f"Default Model: {glider.default_model}")
print(f"Supported Models: {glider.models}")