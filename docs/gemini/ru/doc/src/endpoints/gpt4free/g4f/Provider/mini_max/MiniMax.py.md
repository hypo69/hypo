# Модуль для работы с MiniMax API

## Обзор

Модуль определяет класс `MiniMax`, который является подклассом `OpenaiTemplate` и предназначен для взаимодействия с MiniMax API. MiniMax API - это платформа для создания чат-ботов и других приложений на основе искусственного интеллекта. Модуль предоставляет базовые настройки и параметры для подключения к MiniMax API, такие как URL, URL для входа, базовый URL API, а также список поддерживаемых моделей.

## Подробней

Этот модуль является частью проекта `hypotez` и используется для обеспечения взаимодействия с MiniMax API в рамках этого проекта. Он определяет основные параметры, необходимые для аутентификации и работы с MiniMax API, такие как URL, URL для входа в систему и базовый URL API. Кроме того, он предоставляет список поддерживаемых моделей, которые могут быть использованы для генерации текста.

## Классы

### `MiniMax`

**Описание**: Класс `MiniMax` наследуется от `OpenaiTemplate` и предоставляет интерфейс для работы с MiniMax API.

**Наследует**:

-   `OpenaiTemplate`: класс-шаблон для работы с API OpenAI.

**Аттрибуты**:

-   `label` (str): Название API ("MiniMax API").
-   `url` (str): URL для доступа к MiniMax API ("https://www.hailuo.ai/chat").
-   `login_url` (str): URL для входа в MiniMax API ("https://intl.minimaxi.com/user-center/basic-information/interface-key").
-   `api_base` (str): Базовый URL API ("https://api.minimaxi.chat/v1").
-   `working` (bool): Указывает, работает ли API (True).
-   `needs_auth` (bool): Указывает, требуется ли аутентификация для доступа к API (True).
-   `default_model` (str): Модель, используемая по умолчанию ("MiniMax-Text-01").
-   `default_vision_model` (str): Модель для работы с изображениями, используемая по умолчанию (`default_model`).
-   `models` (list): Список поддерживаемых моделей (`[default_model, "abab6.5s-chat"]`).
-   `model_aliases` (dict): Псевдонимы моделей (`{"MiniMax": default_model}`).

## Функции

В данном коде функции отсутствуют.