# Модуль Glider

## Обзор

Модуль `Glider` предоставляет класс `Glider`, который является наследником класса `OpenaiTemplate` и предназначен для взаимодействия с сервисом `Glider`. Он определяет endpoint, поддерживает список моделей, предоставляет алиасы для моделей и указывает на работоспособность сервиса.

## Подробнее

Модуль содержит определение класса `Glider`, который специализируется на работе с API сервиса `Glider`. Он устанавливает конкретные параметры, такие как URL, endpoint API и список поддерживаемых моделей, а также их альтернативные названия. Класс используется для унификации доступа к различным моделям через интерфейс, предоставляемый `OpenaiTemplate`.

## Классы

### `Glider(OpenaiTemplate)`

**Описание**: Класс `Glider` наследуется от `OpenaiTemplate` и представляет собой адаптер для работы с сервисом Glider.

**Наследует**:
- `OpenaiTemplate`: Предоставляет базовый интерфейс для взаимодействия с OpenAI-подобными API.

**Атрибуты**:
- `label` (str): Название провайдера - `"Glider"`.
- `url` (str): URL сервиса - `"https://glider.so"`.
- `api_endpoint` (str): Endpoint API для чата - `"https://glider.so/api/chat"`.
- `working` (bool): Указывает на работоспособность сервиса - `True`.
- `default_model` (str): Модель, используемая по умолчанию - `'chat-llama-3-1-70b'`.
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь, содержащий алиасы для моделей.

**Методы**:
- Нет собственных методов, использует методы родительского класса `OpenaiTemplate`.

## Функции

В данном модуле нет отдельных функций, только класс `Glider` с атрибутами, определяющими конфигурацию для работы с API Glider.

**Как работает класс**:

1. **Инициализация**: Класс `Glider` инициализируется как подкласс `OpenaiTemplate`.
2. **Конфигурация**: При инициализации устанавливаются значения атрибутов, такие как `label`, `url`, `api_endpoint`, `working`, `default_model`, `models` и `model_aliases`, которые определяют параметры для взаимодействия с API Glider.
3. **Использование**: Класс используется для создания экземпляра, который затем может быть использован для отправки запросов к API Glider с использованием методов, унаследованных от `OpenaiTemplate`.

```ascii
    Glider(OpenaiTemplate)
    │
    ├───label, url, api_endpoint, working, default_model, models, model_aliases (Установка атрибутов)
    │
    └───Использование методов OpenaiTemplate для взаимодействия с API Glider
```

**Примеры**:

```python
from src.endpoints.gpt4free.g4f.Provider.Glider import Glider

# Создание экземпляра класса Glider
glider_provider = Glider()

# Получение информации о провайдере
print(f"Label: {glider_provider.label}")
print(f"URL: {glider_provider.url}")
print(f"API Endpoint: {glider_provider.api_endpoint}")
print(f"Working: {glider_provider.working}")
print(f"Default Model: {glider_provider.default_model}")
print(f"Models: {glider_provider.models}")
print(f"Model Aliases: {glider_provider.model_aliases}")