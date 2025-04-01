# Модуль `MiniMax`

## Обзор

Модуль `MiniMax` предоставляет класс `MiniMax`, который является наследником класса `OpenaiTemplate` и предназначен для взаимодействия с API MiniMax. Он определяет параметры подключения и модели, используемые для обмена сообщениями с сервисом MiniMax.

## Подробнее

Модуль устанавливает основные атрибуты, необходимые для работы с API MiniMax, такие как URL, базовый URL API, флаги для аутентификации и доступности, а также список поддерживаемых моделей.

## Классы

### `MiniMax`

**Описание**: Класс `MiniMax` предназначен для взаимодействия с API MiniMax.

**Наследует**:
- `OpenaiTemplate`: Класс `MiniMax` наследует функциональность от `OpenaiTemplate`, что позволяет использовать общие методы и структуру для взаимодействия с API.

**Атрибуты**:
- `label` (str): Название провайдера API ("MiniMax API").
- `url` (str): URL для доступа к веб-интерфейсу MiniMax ("https://www.hailuo.ai/chat").
- `login_url` (str): URL для входа в личный кабинет и получения ключа API ("https://intl.minimaxi.com/user-center/basic-information/interface-key").
- `api_base` (str): Базовый URL для API MiniMax ("https://api.minimaxi.chat/v1").
- `working` (bool): Флаг, указывающий, что провайдер работает (True).
- `needs_auth` (bool): Флаг, указывающий необходимость аутентификации (True).
- `default_model` (str): Модель, используемая по умолчанию ("MiniMax-Text-01").
- `default_vision_model` (str): Модель для обработки изображений по умолчанию (`default_model`).
- `models` (list[str]): Список поддерживаемых моделей ([default_model, "abab6.5s-chat"]).
- `model_aliases` (dict[str, str]): Псевдонимы моделей ({"MiniMax": default_model}).

## Функции
В классе `MiniMax` функции отсутствуют.