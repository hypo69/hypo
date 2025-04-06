# Модуль для работы с MiniMax API

## Обзор

Модуль `MiniMax` предназначен для взаимодействия с MiniMax API. Он наследует класс `OpenaiTemplate` и предоставляет функциональность для обмена сообщениями с моделью MiniMax.

## Подробнее

Модуль предоставляет удобный интерфейс для работы с MiniMax API, включая установку URL, базового URL API, а также списка поддерживаемых моделей. Он определяет, что для работы требуется аутентификация.

## Классы

### `MiniMax`

**Описание**: Класс для взаимодействия с MiniMax API.

**Наследует**:
- `OpenaiTemplate`: Предоставляет базовую функциональность для работы с API, совместимыми с OpenAI.

**Атрибуты**:
- `label` (str): Название провайдера API ("MiniMax API").
- `url` (str): URL для доступа к веб-интерфейсу MiniMax ("https://www.hailuo.ai/chat").
- `login_url` (str): URL для страницы получения ключа API ("https://intl.minimaxi.com/user-center/basic-information/interface-key").
- `api_base` (str): Базовый URL для API запросов ("https://api.minimaxi.chat/v1").
- `working` (bool): Флаг, указывающий, что провайдер работает (True).
- `needs_auth` (bool): Флаг, указывающий необходимость аутентификации (True).
- `default_model` (str): Модель, используемая по умолчанию ("MiniMax-Text-01").
- `default_vision_model` (str): Модель для работы с изображениями, по умолчанию совпадает с `default_model`.
- `models` (list): Список поддерживаемых моделей ([default_model, "abab6.5s-chat"]).
- `model_aliases` (dict): Псевдонимы моделей ({"MiniMax": default_model}).

```python
class MiniMax(OpenaiTemplate):
    """Класс для взаимодействия с MiniMax API.

    Inherits:
        OpenaiTemplate: Предоставляет базовую функциональность для работы с API, совместимыми с OpenAI.

    Attributes:
        label (str): Название провайдера API ("MiniMax API").
        url (str): URL для доступа к веб-интерфейсу MiniMax ("https://www.hailuo.ai/chat").
        login_url (str): URL для страницы получения ключа API ("https://intl.minimaxi.com/user-center/basic-information/interface-key").
        api_base (str): Базовый URL для API запросов ("https://api.minimaxi.chat/v1").
        working (bool): Флаг, указывающий, что провайдер работает (True).
        needs_auth (bool): Флаг, указывающий необходимость аутентификации (True).
        default_model (str): Модель, используемая по умолчанию ("MiniMax-Text-01").
        default_vision_model (str): Модель для работы с изображениями, по умолчанию совпадает с `default_model`.
        models (list): Список поддерживаемых моделей ([default_model, "abab6.5s-chat"]).
        model_aliases (dict): Псевдонимы моделей ({"MiniMax": default_model}).
    """
    label = "MiniMax API"
    url = "https://www.hailuo.ai/chat"
    login_url = "https://intl.minimaxi.com/user-center/basic-information/interface-key"
    api_base = "https://api.minimaxi.chat/v1"
    working = True
    needs_auth = True

    default_model = "MiniMax-Text-01"
    default_vision_model = default_model
    models = [default_model, "abab6.5s-chat"]
    model_aliases = {"MiniMax": default_model}