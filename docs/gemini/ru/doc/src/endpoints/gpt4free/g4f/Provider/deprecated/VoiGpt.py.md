# Документация для модуля `VoiGpt.py`

## Обзор

Модуль `VoiGpt.py` предоставляет класс `VoiGpt`, который является провайдером для взаимодействия с сайтом VoiGpt.com. Он позволяет отправлять запросы к моделям GPT через этот сайт.

## Подробней

Этот модуль предназначен для интеграции с VoiGpt.com и предоставляет способ использования моделей GPT, таких как "gpt-3.5-turbo", через API этого сайта. Для работы с провайдером требуется получить CSRF токен/cookie с сайта voigpt.com.

## Классы

### `VoiGpt`

**Описание**: Класс `VoiGpt` является провайдером для VoiGpt.com. Он наследуется от `AbstractProvider` и реализует метод `create_completion` для отправки запросов к моделям GPT.

**Наследует**:
- `AbstractProvider`: Абстрактный класс, определяющий интерфейс для провайдеров.

**Атрибуты**:
- `url` (str): URL сайта VoiGpt.com.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий, поддерживает ли провайдер модель "gpt-3.5-turbo".
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.
- `_access_token` (str): Приватный атрибут для хранения access token.

**Методы**:
- `create_completion`: Отправляет запрос к VoiGpt.com и возвращает ответ.

## Функции

### `create_completion`

```python
def create_completion(
    cls,
    model: str,
    messages: Messages,
    stream: bool,
    proxy: str = None,
    access_token: str = None,
    **kwargs
) -> CreateResult:
    """
    Создает запрос к VoiGpt.com и возвращает ответ.

    Args:
        cls: Ссылка на класс.
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
        proxy (str, optional): Прокси для использования. По умолчанию `None`.
        access_token (str, optional): Access token для использования. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        CreateResult: Объект, содержащий результат запроса.

    Raises:
        RuntimeError: Если возникает ошибка при получении ответа от сервера.

    Как работает функция:
    1. Проверяет, передана ли модель. Если нет, устанавливает значение по умолчанию "gpt-3.5-turbo".
    2. Проверяет, передан ли access_token. Если нет, использует значение из атрибута класса `_access_token`.
    3. Если access_token отсутствует, выполняет GET-запрос к сайту VoiGpt.com для получения CSRF токена из cookies.
    4. Формирует заголовки запроса, включая CSRF токен.
    5. Формирует payload с сообщениями для отправки.
    6. Выполняет POST-запрос к API VoiGpt.com.
    7. Пытается извлечь текст ответа из JSON ответа.
    8. Если происходит ошибка при обработке ответа, вызывает исключение RuntimeError с текстом ответа.

    ASCII flowchart:

    Проверка модели и access_token -> Получение CSRF токена (если необходимо) -> Формирование заголовков и payload -> POST запрос к API -> Извлечение текста ответа -> Возврат результата
    """
    ...
```

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `stream` (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
- `proxy` (str, optional): Прокси для использования. По умолчанию `None`.
- `access_token` (str, optional): Access token для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `CreateResult`: Объект, содержащий результат запроса.

**Вызывает исключения**:
- `RuntimeError`: Если возникает ошибка при получении ответа от сервера.

**Примеры**:

```python
# Пример вызова функции create_completion
# messages = [{"role": "user", "content": "Hello, how are you?"}]
# result = VoiGpt.create_completion(model="gpt-3.5-turbo", messages=messages, stream=False)
# for chunk in result:
#     print(chunk)