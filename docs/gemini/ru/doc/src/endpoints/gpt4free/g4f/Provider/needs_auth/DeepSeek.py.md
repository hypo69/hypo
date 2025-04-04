# Документация модуля DeepSeek

## Обзор

Модуль `DeepSeek` предназначен для взаимодействия с API DeepSeek, предоставляя функциональность для работы с языковой моделью `deepseek-chat`. Он наследуется от класса `OpenaiAPI` и реализует специфические настройки для аутентификации и подключения к сервисам DeepSeek.

## Подробнее

Модуль предоставляет удобный интерфейс для использования модели `deepseek-chat`, включая поддержку потоковой передачи данных и истории сообщений. Он требует аутентификации через API-ключ, который можно получить на платформе DeepSeek. Расположение файла в проекте указывает на его роль как одного из провайдеров для g4f, что позволяет использовать различные API, включая DeepSeek, для генерации текста.

## Классы

### `DeepSeek`

**Описание**: Класс `DeepSeek` предназначен для взаимодействия с API DeepSeek. Он наследует функциональность от `OpenaiAPI` и добавляет специфические параметры, необходимые для работы с сервисами DeepSeek.

**Наследует**:
- `OpenaiAPI`: Предоставляет базовую функциональность для взаимодействия с API OpenAI-подобных моделей.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая провайдера как "DeepSeek".
- `url` (str): URL платформы DeepSeek.
- `login_url` (str): URL страницы для получения API-ключей DeepSeek.
- `working` (bool): Указывает, что провайдер находится в рабочем состоянии (`True`).
- `api_base` (str): Базовый URL для API DeepSeek.
- `needs_auth` (bool): Указывает, что для работы с API требуется аутентификация (`True`).
- `supports_stream` (bool): Указывает, поддерживает ли API потоковую передачу данных (`True`).
- `supports_message_history` (bool): Указывает, поддерживает ли API историю сообщений (`True`).
- `default_model` (str): Модель, используемая по умолчанию, `"deepseek-chat"`.
- `fallback_models` (List[str]): Список моделей, используемых в случае недоступности основной модели.

## Функции

В данном классе функции отсутствуют, так как он наследует и переопределяет атрибуты из класса `OpenaiAPI`.

## Пример использования

```python
from src.endpoints.gpt4free.g4f.Provider.needs_auth.DeepSeek import DeepSeek

# Создание экземпляра класса DeepSeek
deepseek = DeepSeek()

# Вывод информации о провайдере
print(f"Провайдер: {deepseek.label}")
print(f"Требуется аутентификация: {deepseek.needs_auth}")
print(f"Модель по умолчанию: {deepseek.default_model}")