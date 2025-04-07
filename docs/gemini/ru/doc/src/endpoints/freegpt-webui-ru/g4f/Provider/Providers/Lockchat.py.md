# Модуль Lockchat

## Обзор

Модуль `Lockchat.py` предназначен для взаимодействия с API Lockchat для генерации ответов моделей GPT-4 и GPT-3.5-turbo. Он отправляет запросы к API и возвращает ответы в потоковом режиме.

## Подробней

Этот модуль предоставляет функцию `_create_completion`, которая принимает параметры модели, сообщения и другие настройки для создания запроса к API Lockchat. Модуль использует библиотеку `requests` для отправки POST-запросов и обработки потоковых ответов. В случае ошибки, связанной с недоступностью модели, функция выполняет повторный запрос.
В модуле также определена переменная `params`, которая содержит информацию о поддержке типов данных для функции `_create_completion`.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, temperature: float = 0.7, **kwargs):
    """
    Создает запрос к API Lockchat и возвращает ответ в потоковом режиме.

    Args:
        model (str): Имя модели для использования (например, 'gpt-4', 'gpt-3.5-turbo').
        messages (list): Список сообщений для отправки в запросе.
        stream (bool): Флаг, указывающий, следует ли возвращать ответ в потоковом режиме.
        temperature (float, optional): Температура для генерации текста. По умолчанию 0.7.
        **kwargs: Дополнительные аргументы.

    Returns:
        Generator[str, None, None]: Генератор токенов ответа от API.

    Raises:
        Exception: Если происходит ошибка при отправке запроса или обработке ответа.
    """
```

**Как работает функция**:

1. **Подготовка полезной нагрузки (payload)**:
   - Создает словарь `payload`, содержащий параметры запроса, такие как `temperature`, `messages`, `model` и `stream`.
2. **Подготовка заголовков (headers)**:
   - Создаёт словарь `headers`, содержащий информацию о `user-agent`.
3. **Отправка POST-запроса**:
   - Отправляет POST-запрос к API Lockchat (`http://super.lockchat.app/v1/chat/completions?auth=FnMNPlwZEnGFqvEc9470Vw==`) с использованием библиотеки `requests`. Указываются параметры `json` (полезная нагрузка), `headers` и `stream=True` для потоковой передачи.
4. **Обработка потоковых ответов**:
   - Итерируется по строкам ответа, полученным с помощью `response.iter_lines()`.
   - Проверяет наличие ошибки, связанной с недоступностью модели (`The model: gpt-4 does not exist`). Если ошибка обнаружена, выводит сообщение в консоль и рекурсивно вызывает `_create_completion` с теми же параметрами для повторной попытки.
   - Извлекает содержимое токена из каждой строки ответа, декодирует его из UTF-8, разделяет строку по `data: `, загружает JSON и извлекает `content` из структуры `['choices'][0]['delta']`.
   - Если `token` существует, возвращает его с помощью `yield (token)`.

```
Подготовка -> Формирование Payload и Headers
      |
      V
Отправка  -> POST-запрос к API Lockchat
      |
      V
Обработка -> Потоковый ответ от API
      |
      V
Извлечение -> Извлечение контента из JSON ответа
      |
      V
Вывод -> Вывод токенов
```

**Примеры**:

```python
# Пример вызова функции _create_completion
messages = [{"role": "user", "content": "Привет, как дела?"}]
for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
    print(token, end='')
```

## Переменные

### `url`
```python
url = 'http://super.lockchat.app'
```
- **Описание**: URL-адрес API Lockchat.

### `model`
```python
model = ['gpt-4', 'gpt-3.5-turbo']
```
- **Описание**: Список поддерживаемых моделей.

### `supports_stream`
```python
supports_stream = True
```
- **Описание**: Флаг, указывающий, поддерживает ли провайдер потоковый режим.

### `needs_auth`
```python
needs_auth = False
```
- **Описание**: Флаг, указывающий, требуется ли аутентификация для доступа к API.

### `params`
```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' +     '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```
- **Описание**: Строка, содержащая информацию о поддерживаемых типах данных для функции `_create_completion`.