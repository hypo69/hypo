# Модуль HuggingFaceInference

## Обзор

Модуль `HuggingFaceInference` предоставляет асинхронный генератор для взаимодействия с моделями Hugging Face Inference API. Он поддерживает как текстовые, так и графические модели и предоставляет методы для получения списка доступных моделей, а также для создания асинхронных запросов к API.

## Подробней

Этот модуль позволяет использовать различные модели машинного обучения, размещенные на платформе Hugging Face, для генерации текста и изображений. Он включает в себя поддержку стриминга ответов, обработки ошибок и форматирования запросов для разных типов моделей. Модуль предназначен для интеграции с другими компонентами системы, требующими доступа к моделям Hugging Face.

## Классы

### `HuggingFaceInference`

**Описание**: Класс `HuggingFaceInference` предоставляет методы для асинхронного взаимодействия с API Hugging Face Inference, наследуя функциональность от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями провайдера.

**Атрибуты**:
- `url` (str): URL главной страницы Hugging Face.
- `parent` (str): Название родительского провайдера ("HuggingFace").
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `default_model` (str): Модель, используемая по умолчанию.
- `default_image_model` (str): Графическая модель, используемая по умолчанию.
- `model_aliases` (dict): Псевдонимы моделей.
- `image_models` (list[str]): Список поддерживаемых графических моделей.
- `model_data` (dict[str, dict]): Кэш данных моделей.

**Методы**:
- `get_models()`: Возвращает список доступных моделей.
- `get_model_data(session: StreamSession, model: str) -> str`: Возвращает данные о модели из API Hugging Face.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для взаимодействия с API Hugging Face.

## Функции

### `get_models`

```python
@classmethod
def get_models(cls) -> list[str]:
    """
    Возвращает список доступных моделей.

    Returns:
        list[str]: Список доступных моделей.
    """
```

**Назначение**:
Функция `get_models` извлекает и возвращает список доступных моделей из API Hugging Face. Она делает HTTP-запросы к API Hugging Face для получения списка моделей, подходящих для генерации текста и изображений.

**Как работает функция**:

1. **Проверка кэша моделей**: Сначала проверяется, был ли уже получен список моделей и сохранен в `cls.models`. Если список уже есть, он возвращается.
2. **Получение списка текстовых моделей**:
   - Исходный список текстовых моделей копируется в переменную `models`.
   - Делается HTTP-запрос к API Hugging Face для получения списка моделей с тегом `text-generation`.
   - Если запрос успешен, извлекаются идентификаторы моделей с `trendingScore` >= 10 и добавляются в начало списка `models`.
   - Из исходного списка `models` удаляются все модели, которые уже добавлены из API.
3. **Получение списка графических моделей**:
   - Исходный список графических моделей копируется в `cls.image_models`.
   - Делается HTTP-запрос к API Hugging Face для получения списка моделей с тегом `text-to-image`.
   - Если запрос успешен, извлекаются идентификаторы моделей с `trendingScore` >= 20 и добавляются в `cls.image_models`.
   - В список `cls.image_models` добавляются модели, которых еще нет в основном списке.
4. **Объединение списков**:
   - Графические модели добавляются в общий список `models`, если их там еще нет.
5. **Кэширование и возврат**:
   - Полученный список моделей сохраняется в `cls.models` для последующего использования.
   - Функция возвращает список доступных моделей.

**Примеры**:

```python
models = HuggingFaceInference.get_models()
print(models)
```

### `get_model_data`

```python
@classmethod
async def get_model_data(cls, session: StreamSession, model: str) -> str:
    """
    Возвращает данные о модели из API Hugging Face.

    Args:
        session (StreamSession): Асинхронная сессия для выполнения HTTP-запросов.
        model (str): Имя модели.

    Returns:
        str: Данные о модели в формате JSON.

    Raises:
        ModelNotSupportedError: Если модель не поддерживается.
    """
```

**Назначение**:
Функция `get_model_data` асинхронно извлекает данные о конкретной модели из API Hugging Face. Она использует асинхронную сессию для выполнения HTTP-запроса к API и возвращает данные о модели в формате JSON.

**Как работает функция**:

1. **Проверка кэша**: Сначала проверяется, есть ли данные о модели в кэше `cls.model_data`. Если есть, они возвращаются.
2. **Выполнение HTTP-запроса**:
   - Создается асинхронный HTTP-запрос к API Hugging Face для получения данных о модели.
   - Если статус ответа 404, выбрасывается исключение `ModelNotSupportedError`.
   - В противном случае проверяется статус ответа и выбрасывается исключение, если возникла ошибка.
3. **Сохранение в кэш**:
   - Полученные данные о модели сохраняются в кэше `cls.model_data` для последующего использования.
4. **Возврат данных**:
   - Функция возвращает данные о модели.

**Примеры**:

```python
import asyncio
from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
        model_data = await HuggingFaceInference.get_model_data(session, "gpt2")
        print(model_data)

if __name__ == "__main__":
    asyncio.run(main())
```

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = True,
    proxy: str = None,
    timeout: int = 600,
    api_base: str = "https://api-inference.huggingface.co",
    api_key: str = None,
    max_tokens: int = 1024,
    temperature: float = None,
    prompt: str = None,
    action: str = None,
    extra_data: dict = {},
    seed: int = None,
    aspect_ratio: str = None,
    width: int = None,
    height: int = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API Hugging Face.

    Args:
        model (str): Имя модели.
        messages (Messages): Список сообщений для отправки в API.
        stream (bool, optional): Флаг, указывающий на использование стриминга. По умолчанию True.
        proxy (str, optional): URL прокси-сервера. По умолчанию None.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию 600.
        api_base (str, optional): Базовый URL API Hugging Face. По умолчанию "https://api-inference.huggingface.co".
        api_key (str, optional): API ключ. По умолчанию None.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 1024.
        temperature (float, optional): Температура для генерации текста. По умолчанию None.
        prompt (str, optional): Промпт для генерации изображения. По умолчанию None.
        action (str, optional): Действие (например, "continue"). По умолчанию None.
        extra_data (dict, optional): Дополнительные данные для отправки в API. По умолчанию {}.
        seed (int, optional): Зерно для случайной генерации. По умолчанию None.
        aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию None.
        width (int, optional): Ширина изображения. По умолчанию None.
        height (int, optional): Высота изображения. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Yields:
        AsyncResult: Асинхронный генератор, выдающий результаты из API.

    Raises:
        ModelNotSupportedError: Если модель не поддерживается.
        ResponseError: Если произошла ошибка в ответе от API.
    """
```

**Назначение**:
Функция `create_async_generator` создает и возвращает асинхронный генератор для взаимодействия с API Hugging Face. Этот генератор используется для отправки запросов к API и получения результатов, будь то текст или изображения.

**Как работает функция**:

1. **Подготовка заголовков**:
   - Создаются заголовки HTTP-запроса, включающие `Accept-Encoding` и `Content-Type`.
   - Если предоставлен `api_key`, он добавляется в заголовок `Authorization`.
2. **Обработка параметров изображения**:
   - Параметры `width`, `height` и `aspect_ratio` обрабатываются с помощью функции `use_aspect_ratio` для формирования `image_extra_data`.
3. **Создание асинхронной сессии**:
   - Создается асинхронная сессия с заданными заголовками, прокси и таймаутом.
4. **Обработка запросов к `provider_together_urls`**:
   - Если модель есть в списке `provider_together_urls`, формируется запрос к соответствующему URL для генерации изображения.
   - Результат возвращается как объект `ImageResponse`.
5. **Формирование полезной нагрузки (payload) и параметров**:
   - Определяются параметры запроса, такие как `return_full_text`, `max_new_tokens` и `temperature`.
   - В зависимости от типа модели и `pipeline_tag` формируется полезная нагрузка `payload`.
   - Для моделей `text-to-image` формируется запрос на генерацию изображения.
   - Для моделей `text-generation` и `image-text-to-text` формируется запрос на генерацию текста.
   - Используются функции `get_inputs` для форматирования входных данных.
6. **Отправка запроса и обработка ответа**:
   - Отправляется POST-запрос к API Hugging Face с сформированной полезной нагрузкой.
   - Если `stream` установлен в `True`, ответ обрабатывается как поток данных.
   - Если `stream` установлен в `False`, ответ обрабатывается как JSON и возвращается результат.
7. **Обработка потока данных (stream=True)**:
   - Ответ разбивается на строки.
   - Каждая строка, начинающаяся с `data:`, парсится как JSON.
   - Извлекается текст из токенов и возвращается как часть генератора.
   - В конце потока возвращается `FinishReason`.
8. **Обработка не потокового ответа (stream=False)**:
   - Сохраняются медиафайлы из ответа.
   - Извлекается сгенерированный текст из JSON и возвращается.

**Внутренние функции**: Отсутствуют. Однако внутри используются другие функции форматирования промптов. Они описаны ниже

**Примеры**:

```python
import asyncio
from aiohttp import ClientSession

async def main():
    messages = [{"role": "user", "content": "Напиши короткий рассказ."}]
    async with ClientSession() as session:
        generator = HuggingFaceInference.create_async_generator(
            model="gpt2", messages=messages, stream=True
        )
        async for chunk in generator:
            print(chunk, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

### `format_prompt_mistral`

```python
def format_prompt_mistral(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Mistral.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг, указывающий на продолжение диалога. По умолчанию False.

    Returns:
        str: Отформатированный промпт.
    """
```

**Назначение**:
Функция `format_prompt_mistral` форматирует список сообщений в строку, пригодную для использования с моделью Mistral. Она создает промпт, который включает в себя системные сообщения, историю диалога и последний вопрос пользователя.

**Как работает функция**:

1. **Извлечение системных сообщений**:
   - Извлекаются все сообщения с ролью "system" и объединяются в список `system_messages`.
2. **Формирование вопроса**:
   - Последнее сообщение пользователя объединяется с системными сообщениями в переменную `question`.
3. **Формирование истории**:
   - История диалога формируется путем итерации по сообщениям с ролью "assistant" и создания строк вида `<s>[INST]...[/INST]...</s>`.
4. **Обработка флага `do_continue`**:
   - Если `do_continue` установлен в `True`, из истории удаляется последний тег `</s>`.
5. **Формирование итогового промпта**:
   - Итоговый промпт формируется путем объединения истории и вопроса.

**Примеры**:

```python
messages = [
    {"role": "system", "content": "Ты — полезный ассистент."},
    {"role": "user", "content": "Что такое Python?"},
    {"role": "assistant", "content": "Python — это язык программирования."},
    {"role": "user", "content": "Приведи пример кода на Python."}
]
prompt = format_prompt_mistral(messages)
print(prompt)
```

### `format_prompt_qwen`

```python
def format_prompt_qwen(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Qwen.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг, указывающий на продолжение диалога. По умолчанию False.

    Returns:
        str: Отформатированный промпт.
    """
```

**Назначение**:
Функция `format_prompt_qwen` форматирует список сообщений в строку, пригодную для использования с моделью Qwen. Она создает промпт, в котором каждое сообщение обрамляется тегами `<|im_start|>` и `<|im_end|>`.

**Как работает функция**:

1. **Формирование промпта**:
   - Итерируется по списку сообщений и для каждого сообщения создается строка вида `<|im_start|>role\ncontent\n<|im_end|>\n`.
   - Все строки объединяются в одну.
2. **Обработка флага `do_continue`**:
   - Если `do_continue` установлен в `True`, из промпта удаляется последний тег `\n<|im_end|>\n`.
3. **Формирование итогового промпта**:
   - К промпту добавляется тег `<|im_start|>assistant\n`, если `do_continue` равен `False`.

**Примеры**:

```python
messages = [
    {"role": "system", "content": "Ты — полезный ассистент."},
    {"role": "user", "content": "Что такое Python?"},
    {"role": "assistant", "content": "Python — это язык программирования."},
    {"role": "user", "content": "Приведи пример кода на Python."}
]
prompt = format_prompt_qwen(messages)
print(prompt)
```

### `format_prompt_qwen2`

```python
def format_prompt_qwen2(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Qwen2.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг, указывающий на продолжение диалога. По умолчанию False.

    Returns:
        str: Отформатированный промпт.
    """
```

**Назначение**:
Функция `format_prompt_qwen2` форматирует список сообщений в строку, пригодную для использования с моделью Qwen2. Она создает промпт, в котором каждое сообщение обрамляется тегами `\u003C｜...｜\u003E`.

**Как работает функция**:

1. **Формирование промпта**:
   - Итерируется по списку сообщений и для каждого сообщения создается строка вида `\u003C｜role｜\u003Econtent\u003C｜end of sentence｜\u003E`.
   - Все строки объединяются в одну.
2. **Обработка флага `do_continue`**:
   - Если `do_continue` установлен в `True`, из промпта удаляется последний тег `\u003C｜Assistant｜\u003E`.
3. **Формирование итогового промпта**:
   - К промпту добавляется тег `\u003C｜Assistant｜\u003E`, если `do_continue` равен `False`.

**Примеры**:

```python
messages = [
    {"role": "system", "content": "Ты — полезный ассистент."},
    {"role": "user", "content": "Что такое Python?"},
    {"role": "assistant", "content": "Python — это язык программирования."},
    {"role": "user", "content": "Приведи пример кода на Python."}
]
prompt = format_prompt_qwen2(messages)
print(prompt)
```

### `format_prompt_llama`

```python
def format_prompt_llama(messages: Messages, do_continue: bool = False) -> str:
    """
    Форматирует сообщения для модели Llama.

    Args:
        messages (Messages): Список сообщений.
        do_continue (bool, optional): Флаг, указывающий на продолжение диалога. По умолчанию False.

    Returns:
        str: Отформатированный промпт.
    """
```

**Назначение**:
Функция `format_prompt_llama` форматирует список сообщений в строку, пригодную для использования с моделью Llama. Она создает промпт, в котором каждое сообщение обрамляется тегами `<|start_header_id|>`, `<|end_header_id|>` и `<|eot_id|>`.

**Как работает функция**:

1. **Формирование промпта**:
   - Итерируется по списку сообщений и для каждого сообщения создается строка вида `<|start_header_id|>role<|end_header_id|>\n\ncontent\n<|eot_id|>\n`.
   - Все строки объединяются в одну.
2. **Обработка флага `do_continue`**:
   - Если `do_continue` установлен в `True`, из промпта удаляется последний тег `\n<|eot_id|>\n`.
3. **Формирование итогового промпта**:
   - К промпту добавляется тег `<|start_header_id|>assistant<|end_header_id|>\n\n`, если `do_continue` равен `False`.
   - В начало промпта добавляется тег `<|begin_of_text|>`.

**Примеры**:

```python
messages = [
    {"role": "system", "content": "Ты — полезный ассистент."},
    {"role": "user", "content": "Что такое Python?"},
    {"role": "assistant", "content": "Python — это язык программирования."},
    {"role": "user", "content": "Приведи пример кода на Python."}
]
prompt = format_prompt_llama(messages)
print(prompt)
```

### `format_prompt_custom`

```python
def format_prompt_custom(messages: Messages, end_token: str = "</s>", do_continue: bool = False) -> str:
    """
    Форматирует сообщения с использованием пользовательского токена конца сообщения.

    Args:
        messages (Messages): Список сообщений.
        end_token (str, optional): Токен конца сообщения. По умолчанию "</s>".
        do_continue (bool, optional): Флаг, указывающий на продолжение диалога. По умолчанию False.

    Returns:
        str: Отформатированный промпт.
    """
```

**Назначение**:
Функция `format_prompt_custom` форматирует список сообщений в строку, используя пользовательский токен конца сообщения (`end_token`). Она создает промпт, в котором каждое сообщение обрамляется тегами `<|role|>`, и завершается указанным токеном.

**Как работает функция**:

1. **Формирование промпта**:
   - Итерируется по списку сообщений и для каждого сообщения создается строка вида `<|role|>\ncontent{end_token}\n`.
   - Все строки объединяются в одну.
2. **Обработка флага `do_continue`**:
   - Если `do_continue` установлен в `True`, из промпта удаляется последний тег `{end_token}\n`.
3. **Формирование итогового промпта**:
   - К промпту добавляется тег `<|assistant|>\n`, если `do_continue` равен `False`.

**Примеры**:

```python
messages = [
    {"role": "system", "content": "Ты — полезный ассистент."},
    {"role": "user", "content": "Что такое Python?"},
    {"role": "assistant", "content": "Python — это язык программирования."},
    {"role": "user", "content": "Приведи пример кода на Python."}
]
prompt = format_prompt_custom(messages, end_token="<|file_separator|>")
print(prompt)
```

### `get_inputs`

```python
def get_inputs(messages: Messages, model_data: dict, model_type: str, do_continue: bool = False) -> str:
    """
    Определяет и форматирует входные данные для разных типов моделей.

    Args:
        messages (Messages): Список сообщений.
        model_data (dict): Данные о модели.
        model_type (str): Тип модели.
        do_continue (bool, optional): Флаг, указывающий на продолжение диалога. По умолчанию False.

    Returns:
        str: Отформатированные входные данные.
    """
```

**Назначение**:
Функция `get_inputs` определяет и форматирует входные данные для различных типов моделей на основе предоставленных данных о модели и типе модели. Она выбирает подходящую функцию форматирования промпта и возвращает отформатированные входные данные.

**Как работает функция**:

1. **Обработка различных типов моделей**:
   - Если `model_type` входит в список `("gpt2", "gpt_neo", "gemma", "gemma2")`, используются общие функции форматирования.
   - Если `model_type` равен "mistral" и `author` модели равен "mistralai", используется функция `format_prompt_mistral`.
   - Если в данных модели есть информация о `eos_token`, выбирается соответствующая функция форматирования:
     - Если `eos_token` равен "<|endoftext|>", "<eos>" или "</s>", используется `format_prompt_custom`.
     - Если `eos_token` равен "<|im_end|>", используется `format_prompt_qwen`.
     - Если `eos_token` содержит `content` равный "\\u003C｜end of sentence｜\\u003E", используется `format_prompt_qwen2`.
     - Если `eos_token` равен "<|eot_id|>", используется `format_prompt_llama`.
   - В противном случае используются общие функции форматирования.
2. **Возврат отформатированных входных данных**:
   - Возвращаются отформатированные входные данные, готовые для отправки в модель.

**Примеры**:

```python
messages = [
    {"role": "system", "content": "Ты — полезный ассистент."},
    {"role": "user", "content": "Что такое Python?"},
    {"role": "assistant", "content": "Python — это язык программирования."},
    {"role": "user", "content": "Приведи пример кода на Python."}
]
model_data = {"config": {"tokenizer_config": {"eos_token": "</s>"}}}
model_type = "gpt2"
inputs = get_inputs(messages, model_data, model_type)
print(inputs)