# Модуль `Lockchat`

## Обзор

Модуль `Lockchat` предоставляет класс `Lockchat`, который является провайдером для взаимодействия с API Lockchat. Он поддерживает модели `gpt-3.5-turbo` и `gpt-4`, а также потоковую передачу данных.

## Подробней

Этот модуль используется для отправки запросов к API Lockchat и получения ответов. Lockchat является одним из провайдеров, интегрированных в проект `hypotez`, и позволяет использовать его API для получения ответов от AI-моделей.

## Классы

### `Lockchat(AbstractProvider)`

**Описание**: Класс `Lockchat` предоставляет интерфейс для взаимодействия с API Lockchat.

**Наследует**:

- `AbstractProvider`: Абстрактный класс, определяющий базовый интерфейс для всех провайдеров.

**Атрибуты**:

- `url` (str): URL-адрес API Lockchat (`http://supertest.lockchat.app`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-3.5-turbo` (`True`).
- `supports_gpt_4` (bool): Указывает, поддерживает ли провайдер модель `gpt-4` (`True`).

### `create_completion`

```python
    @staticmethod
    def create_completion(
        model: str,
        messages: list[dict[str, str]],
        stream: bool, **kwargs: Any) -> CreateResult:
        """
        Создает запрос на завершение текста к API Lockchat.

        Args:
            model (str): Идентификатор модели для использования.
            messages (list[dict[str, str]]): Список сообщений для отправки в запросе.
            stream (bool): Указывает, использовать ли потоковую передачу данных.
            **kwargs (Any): Дополнительные параметры запроса.

        Returns:
            CreateResult: Результат создания запроса на завершение текста.

        Raises:
            requests.exceptions.HTTPError: Если HTTP-запрос возвращает код ошибки.

        Example:
            >>> Lockchat.create_completion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello"}], stream=True)
            <generator object Lockchat.create_completion at 0x...>
        """
```

**Назначение**: Функция `create_completion` отправляет запрос к API Lockchat для генерации текста на основе предоставленных сообщений и параметров.

**Параметры**:

- `model` (str): Идентификатор модели для использования. Например, `gpt-3.5-turbo` или `gpt-4`.
- `messages` (list[dict[str, str]]): Список сообщений, представляющих контекст разговора. Каждое сообщение содержит роль (`role`) и содержимое (`content`).
- `stream` (bool): Указывает, использовать ли потоковую передачу данных. Если `True`, ответ будет возвращаться по частям в виде генератора.
- `**kwargs` (Any): Дополнительные параметры запроса, такие как `temperature`.

**Возвращает**:

- `CreateResult`: Генератор токенов, если `stream=True`, или полный текст ответа, если `stream=False`.

**Как работает функция**:

1. **Подготовка полезной нагрузки (payload)**:
   - Извлекает значение температуры из `kwargs` или устанавливает значение по умолчанию 0.7.
   - Формирует словарь `payload`, содержащий `temperature`, `messages`, `model` и `stream`.

2. **Формирование заголовков**:
   - Устанавливает заголовок `user-agent` для имитации запроса от приложения ChatX.

3. **Отправка POST-запроса**:
   - Отправляет POST-запрос к API Lockchat (`http://supertest.lockchat.app/v1/chat/completions`) с использованием `requests.post`.
   - Устанавливает `json=payload`, `headers=headers` и `stream=True` для потоковой передачи.

4. **Обработка ответа**:
   - Вызывает `response.raise_for_status()` для проверки статуса ответа. Если запрос неудачен, будет вызвано исключение.
   - Итерируется по строкам ответа с использованием `response.iter_lines()`.

5. **Обработка ошибок и извлечение токенов**:
   - Проверяет наличие ошибки, связанной с несуществующей моделью `gpt-4`. В случае обнаружения ошибки, функция рекурсивно вызывает себя для повторной попытки.
   - Извлекает содержимое токенов из каждой строки ответа, декодирует JSON и извлекает `content` из `token["choices"][0]["delta"].get("content")`.
   - Возвращает токен с помощью `yield (token)`, если токен не пустой.

```
   Подготовка параметров
   │
   V
   Создание payload (температура, сообщения, модель, стриминг)
   │
   V
   Формирование заголовков (user-agent)
   │
   V
   Отправка POST-запроса к API Lockchat
   │
   V
   Обработка ответа
   │
   V
   Проверка статуса ответа
   │
   V
   Итерация по строкам ответа
   │
   V
   Проверка на наличие ошибки "The model: `gpt-4` does not exist"
   │
   ├───ДА───> Рекурсивный вызов create_completion
   │   
   └───НЕТ───> Извлечение содержимого токенов из JSON
   │
   V
   Выдача токена (yield token)
```

**Примеры**:

```python
# Пример вызова функции create_completion
messages = [{"role": "user", "content": "Напиши короткое стихотворение о весне."}]
for token in Lockchat.create_completion(model="gpt-3.5-turbo", messages=messages, stream=True):
    print(token, end="")