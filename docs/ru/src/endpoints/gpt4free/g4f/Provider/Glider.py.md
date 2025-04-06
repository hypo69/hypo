# Модуль `Glider`

## Обзор

Модуль `Glider` предоставляет класс `Glider`, который является подклассом `OpenaiTemplate` и предназначен для взаимодействия с сервисом Glider. Он определяет параметры подключения и доступные модели для этого сервиса.

## Подробнее

Модуль определяет класс `Glider`, который наследуется от `OpenaiTemplate`. Он задает URL, endpoint API и список поддерживаемых моделей, а также их псевдонимы.

## Классы

### `Glider`

**Описание**: Класс `Glider` предназначен для взаимодействия с сервисом Glider.

**Наследует**:
- `OpenaiTemplate`: Предоставляет базовую структуру для взаимодействия с API, подобными OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера "Glider".
- `url` (str): URL сервиса Glider ("https://glider.so").
- `api_endpoint` (str): Endpoint API для чата ("https://glider.so/api/chat").
- `working` (bool): Индикатор работоспособности провайдера (True).
- `default_model` (str): Модель по умолчанию ('chat-llama-3-1-70b').
- `models` (list[str]): Список поддерживаемых моделей.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- Нет специфических методов, кроме унаследованных от `OpenaiTemplate`.

## Примеры

```python
from g4f.Provider import Glider

# Создание экземпляра класса Glider
glider = Glider()

# Получение информации о провайдере
print(f"Провайдер: {glider.label}")
print(f"URL: {glider.url}")
print(f"API Endpoint: {glider.api_endpoint}")
print(f"Работоспособность: {glider.working}")
print(f"Модель по умолчанию: {glider.default_model}")
print(f"Поддерживаемые модели: {glider.models}")
print(f"Псевдонимы моделей: {glider.model_aliases}")
```