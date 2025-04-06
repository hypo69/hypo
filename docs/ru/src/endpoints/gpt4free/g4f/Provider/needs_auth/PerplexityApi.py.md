# Модуль PerplexityApi

## Обзор

Модуль `PerplexityApi` представляет собой класс `PerplexityApi`, который наследуется от `OpenaiTemplate` и предназначен для взаимодействия с API Perplexity. Он определяет параметры подключения к API, такие как URL, необходимость авторизации, базовый URL API и список поддерживаемых моделей.

## Подробней

Данный модуль является частью проекта `hypotez` и служит для обеспечения взаимодействия с API Perplexity в рамках gpt4free. Он расширяет функциональность `OpenaiTemplate`, добавляя специфические параметры, необходимые для работы с Perplexity, такие как URL для входа в систему и список поддерживаемых моделей. Расположение файла в проекте `hypotez/src/endpoints/gpt4free/g4f/Provider/needs_auth/PerplexityApi.py` указывает на его роль в предоставлении доступа к моделям Perplexity через gpt4free.

## Классы

### `PerplexityApi`

**Описание**: Класс `PerplexityApi` наследуется от `OpenaiTemplate` и предоставляет интерфейс для взаимодействия с API Perplexity.

**Наследует**:
- `OpenaiTemplate`: Предоставляет базовую функциональность для работы с API OpenAI-подобных моделей.

**Атрибуты**:
- `label` (str): Метка провайдера "Perplexity API".
- `url` (str): URL веб-сайта Perplexity.
- `login_url` (str): URL страницы настроек API Perplexity для получения ключа API.
- `working` (bool): Указывает, что API Perplexity работает (True).
- `needs_auth` (bool): Указывает, что для работы с API требуется авторизация (True).
- `api_base` (str): Базовый URL API Perplexity.
- `default_model` (str): Модель, используемая по умолчанию, `"llama-3-sonar-large-32k-online"`.
- `models` (List[str]): Список поддерживаемых моделей Perplexity.

## Функции

В данном модуле функции отсутствуют. Присутствуют только атрибуты класса.