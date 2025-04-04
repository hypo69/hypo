# Модуль TypeGPT для g4f

## Обзор

Модуль `TypeGPT` предоставляет класс `TypeGPT`, который является частью проекта `hypotez` и предназначен для взаимодействия с сервисом TypeGPT (chat.typegpt.net) через его API. Класс наследует от `OpenaiTemplate` и предоставляет методы для получения моделей, используемых сервисом.

## Подробнее

Этот модуль обеспечивает интеграцию с сервисом TypeGPT, позволяя использовать его возможности для обработки и генерации текста. Он содержит настройки для API, такие как URL, заголовки запросов и список моделей. `TypeGPT` используется для настройки запросов к API TypeGPT и обработки ответов.

## Классы

### `TypeGPT`

**Описание**: Класс `TypeGPT` предназначен для взаимодействия с API сервиса TypeGPT. Он наследует от класса `OpenaiTemplate` и содержит настройки, специфичные для TypeGPT.

**Наследует**:
- `OpenaiTemplate`: Этот класс, вероятно, предоставляет общую структуру и функциональность для взаимодействия с API, подобными OpenAI.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая провайдера как "TypeGpt".
- `url` (str): URL сервиса TypeGPT ("https://chat.typegpt.net").
- `api_base` (str): Базовый URL API сервиса TypeGPT ("https://chat.typegpt.net/api/openai/v1").
- `working` (bool): Указывает, что провайдер в данный момент работает (True).
- `headers` (dict): Заголовки HTTP-запроса, необходимые для взаимодействия с API.
- `default_model` (str): Модель, используемая по умолчанию ('gpt-4o-mini-2024-07-18').
- `default_vision_model` (str): Модель для работы с изображениями по умолчанию, совпадающая с `default_model`.
- `vision_models` (List[str]): Список моделей, поддерживающих работу с изображениями.
- `fallback_models` (List[str]): Список моделей, используемых в качестве запасных.
- `image_models` (List[str]): Список моделей для генерации изображений.
- `model_aliases` (dict): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `get_models(**kwargs)`: Получает список доступных моделей от API TypeGPT.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls, **kwargs):
    """
    Получает список доступных моделей от API TypeGPT.

    Args:
        **kwargs: Дополнительные аргументы (не используются).

    Returns:
        List[str]: Список доступных моделей.
    """
```

**Назначение**: Метод `get_models` класса `TypeGPT` предназначен для получения списка доступных моделей от API сервиса TypeGPT.

**Параметры**:
- `cls`: Ссылка на класс `TypeGPT`.
- `**kwargs`: Дополнительные аргументы (не используются).

**Возвращает**:
- `List[str]`: Список доступных моделей, полученных от API.

**Как работает функция**:

1. **Проверка наличия моделей в кэше**:
   - Функция проверяет, были ли модели уже получены и сохранены в атрибуте `cls.models`.

2. **Получение моделей из API (если необходимо)**:
   - Если `cls.models` пуст (то есть модели еще не были получены), функция выполняет HTTP GET-запрос к эндпоинту `/api/config` на сервере TypeGPT.
   - Полученный JSON-ответ содержит строку `customModels`, которая разделяется на список моделей.
   -  A
     ↓
     B → C
     ↓
     D
   -  A: Проверка `cls.models`
   -  B: Если `cls.models` пуст, выполнить GET запрос `/api/config`
   -  C: Получение значения `customModels` из ответа и преобразование в список
   -  D: Возврат списка моделей

3. **Обработка полученных моделей**:
   - Из списка исключаются модели, начинающиеся с `+` и содержащиеся в `cls.image_models`.

4. **Возврат списка моделей**:
   - Функция возвращает список доступных моделей.

**Примеры**:

```python
models = TypeGPT.get_models()
print(models)
# ['gpt-4o-mini-2024-07-18', 'gpt-3.5-turbo', ...]
```
```python
models = TypeGPT.get_models() # последующий вызов не делает запрос к api, а возвращает сохраненный список моделей
print(models)
# ['gpt-4o-mini-2024-07-18', 'gpt-3.5-turbo', ...]