# Модуль MiniMax

## Обзор

Модуль `MiniMax` предоставляет класс `MiniMax`, который используется для взаимодействия с API MiniMax. Этот класс является подклассом `OpenaiTemplate` и содержит информацию о URL, требованиях к аутентификации, поддерживаемых моделях и другие параметры, необходимые для работы с MiniMax API.

## Подробнее

Этот модуль предназначен для интеграции с MiniMax API в проекте `hypotez`. Он определяет параметры подключения и список поддерживаемых моделей, что упрощает использование MiniMax API для задач обработки текста и изображений. Расположение файла в проекте (`hypotez/src/endpoints/gpt4free/g4f/Provider/mini_max/MiniMax.py`) указывает на то, что он является частью функциональности для работы с различными провайдерами API, используемыми в проекте.

## Классы

### `MiniMax`

**Описание**: Класс `MiniMax` предназначен для взаимодействия с MiniMax API.

**Наследует**:
- `OpenaiTemplate`: Класс наследует `OpenaiTemplate`, который, вероятно, предоставляет общую структуру и функциональность для взаимодействия с API, подобными OpenAI.

**Атрибуты**:
- `label` (str): Метка для MiniMax API ("MiniMax API").
- `url` (str): URL для MiniMax API ("https://www.hailuo.ai/chat").
- `login_url` (str): URL для страницы входа в MiniMax ("https://intl.minimaxi.com/user-center/basic-information/interface-key").
- `api_base` (str): Базовый URL для API запросов MiniMax ("https://api.minimaxi.chat/v1").
- `working` (bool): Указывает, что API работает (True).
- `needs_auth` (bool): Указывает, требуется ли аутентификация для доступа к API (True).
- `default_model` (str): Модель, используемая по умолчанию ("MiniMax-Text-01").
- `default_vision_model` (str): Модель для обработки изображений по умолчанию (совпадает с `default_model`).
- `models` (list): Список поддерживаемых моделей ([default_model, "abab6.5s-chat"]).
- `model_aliases` (dict): Псевдонимы моделей ({"MiniMax": default_model}).

## Примеры

Примеры использования класса `MiniMax`:

```python
from src.endpoints.gpt4free.g4f.Provider.mini_max.MiniMax import MiniMax

# Создание экземпляра класса MiniMax
minimax = MiniMax()

# Вывод информации о классе
print(f"Label: {minimax.label}")
print(f"API Base: {minimax.api_base}")
print(f"Default Model: {minimax.default_model}")