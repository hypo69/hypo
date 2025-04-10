# Модуль для создания изображений на основе текстовых подсказок
## Обзор

Модуль `create_images.py` предназначен для обработки запросов на создание изображений на основе текстовых подсказок, встроенных в сообщения. Он использует другие провайдеры для обработки задач, не связанных с созданием изображений.

## Подробней

Этот модуль предоставляет класс `CreateImagesProvider`, который расширяет возможности базового провайдера, добавляя функциональность генерации изображений на основе текстовых запросов. Он использует регулярные выражения для поиска специальных тегов `<img data-prompt="текстовый запрос">` в сообщениях и заменяет их сгенерированными изображениями. Это позволяет интегрировать процесс создания изображений непосредственно в процесс обработки текстовых сообщений.

## Классы

### `CreateImagesProvider`

**Описание**: Класс провайдера для создания изображений на основе текстовых подсказок.

**Принцип работы**:
Класс `CreateImagesProvider` принимает базового провайдера, функции для синхронного и асинхронного создания изображений, а также системное сообщение, которое объясняет возможности генерации изображений.
Он перехватывает сообщения, ищет в них теги `<img data-prompt="текстовый запрос">`, извлекает текстовые запросы и использует предоставленные функции для создания изображений. Затем он заменяет теги `<img data-prompt="текстовый запрос">` сгенерированными изображениями.

**Атрибуты**:

- `provider` (ProviderType): Базовый провайдер для обработки задач, не связанных с созданием изображений.
- `create_images` (callable): Функция для синхронного создания изображений.
- `create_images_async` (callable): Функция для асинхронного создания изображений.
- `system_message` (str): Системное сообщение, объясняющее возможности генерации изображений.
- `include_placeholder` (bool): Флаг, определяющий, следует ли включать заполнитель изображения в вывод.
- `__name__` (str): Имя провайдера.
- `url` (str): URL провайдера.
- `working` (bool): Указывает, работает ли провайдер.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу.

### `__init__`

```python
def __init__(
    self,
    provider: ProviderType,
    create_images: callable,
    create_async: callable,
    system_message: str = system_message,
    include_placeholder: bool = True
) -> None:
    """
    Инициализирует `CreateImagesProvider`.

    Args:
        provider (ProviderType): Базовый провайдер.
        create_images (callable): Функция для синхронного создания изображений.
        create_async (callable): Функция для асинхронного создания изображений.
        system_message (str, optional): Системное сообщение, добавляемое к сообщениям. По умолчанию используется предопределенное сообщение.
        include_placeholder (bool, optional): Следует ли включать заполнители изображений в вывод. По умолчанию `True`.
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `CreateImagesProvider`.

**Параметры**:

- `provider` (ProviderType): Базовый провайдер, используемый для выполнения задач, не связанных с генерацией изображений.
- `create_images` (callable): Функция, вызываемая для создания изображений в синхронном режиме.
- `create_async` (callable): Функция, вызываемая для создания изображений в асинхронном режиме.
- `system_message` (str, optional): Системное сообщение, которое будет добавлено к сообщениям для объяснения возможностей генерации изображений. По умолчанию используется значение переменной `system_message`, определенной в модуле.
- `include_placeholder` (bool, optional): Флаг, указывающий, следует ли включать заполнитель изображения в вывод. По умолчанию `True`.

**Как работает функция**:

1.  Присваивает переданные параметры соответствующим атрибутам экземпляра класса.

2.  Устанавливает атрибуты `__name__`, `url`, `working` и `supports_stream` на основе значений, полученных из базового провайдера.

### `create_completion`

```python
def create_completion(
    self,
    model: str,
    messages: Messages,
    stream: bool = False,
    **kwargs
) -> CreateResult:
    """
    Создает результат завершения, обрабатывая все подсказки для создания изображений, найденные в сообщениях.

    Args:
        model (str): Модель, используемая для создания.
        messages (Messages): Сообщения для обработки, которые могут содержать подсказки для изображений.
        stream (bool, optional): Указывает, следует ли передавать результаты потоком. По умолчанию `False`.
        **kwargs: Дополнительные аргументы ключевых слов для провайдера.

    Yields:
        CreateResult: Выдает фрагменты обработанных сообщений, включая данные изображения, если это применимо.

    Note:
        Этот метод обрабатывает сообщения для обнаружения подсказок для создания изображений. Когда такая подсказка найдена,
        он вызывает функцию синхронного создания изображений и включает результирующее изображение в вывод.
    """
    ...
```

**Назначение**: Создает результат завершения, обрабатывая запросы на создание изображений, найденные в сообщениях.

**Параметры**:

- `model` (str): Модель, используемая для генерации.
- `messages` (Messages): Список сообщений, которые могут содержать запросы на создание изображений.
- `stream` (bool, optional): Флаг, указывающий, следует ли возвращать результаты в виде потока. По умолчанию `False`.
- `**kwargs`: Дополнительные именованные аргументы, передаваемые базовому провайдеру.

**Возвращает**:

- `CreateResult`: Итератор, возвращающий фрагменты обработанных сообщений, включая данные изображений, если они были сгенерированы.

**Как работает функция**:

1.  Добавляет системное сообщение в начало списка сообщений, чтобы объяснить возможности генерации изображений.

2.  Итерируется по фрагментам, возвращаемым базовым провайдером.

3.  Если фрагмент является экземпляром `ImageResponse`, он возвращается напрямую.

4.  Если фрагмент содержит тег `<img data-prompt="текстовый запрос">`, извлекается текстовый запрос, вызывается функция `create_images` для создания изображения, и изображение вставляется в результат.

5.  Если `include_placeholder` имеет значение `True`, заполнитель изображения также включается в результат.

     ```
     A (Добавление системного сообщения)
     ↓
     B (Итерация по фрагментам)
     ↓
     C (Проверка типа фрагмента)
     ↓
     D (Обработка тега <img data-prompt>)
     ↓
     E (Создание изображения)
     ↓
     F (Включение заполнителя)
     ```

**Примеры**:

```python
# Пример использования create_completion с потоковой передачей
provider = CreateImagesProvider(
    provider=SomeBaseProvider(),
    create_images=some_create_images_function,
    create_async=some_create_async_function
)
for chunk in provider.create_completion(model="dalle3", messages=[{"role": "user", "content": "Создай изображение: <img data-prompt='кошка'>"}], stream=True):
    print(chunk)

# Пример использования create_completion без потоковой передачи
provider = CreateImagesProvider(
    provider=SomeBaseProvider(),
    create_images=some_create_images_function,
    create_async=some_create_async_function
)
result = "".join(provider.create_completion(model="dalle3", messages=[{"role": "user", "content": "Создай изображение: <img data-prompt='кошка'>"}]))
print(result)
```

### `create_async`

```python
async def create_async(
    self,
    model: str,
    messages: Messages,
    **kwargs
) -> str:
    """
    Асинхронно создает ответ, обрабатывая все подсказки для создания изображений, найденные в сообщениях.

    Args:
        model (str): Модель, используемая для создания.
        messages (Messages): Сообщения для обработки, которые могут содержать подсказки для изображений.
        **kwargs: Дополнительные аргументы ключевых слов для провайдера.

    Returns:
        str: Обработанная строка ответа, включая асинхронно сгенерированные данные изображения, если это применимо.

    Note:
        Этот метод обрабатывает сообщения для обнаружения подсказок для создания изображений. Когда такая подсказка найдена,
        он вызывает функцию асинхронного создания изображений и включает результирующее изображение в вывод.
    """
    ...
```

**Назначение**: Асинхронно создает ответ, обрабатывая запросы на создание изображений, найденные в сообщениях.

**Параметры**:

- `model` (str): Модель, используемая для генерации.
- `messages` (Messages): Список сообщений, которые могут содержать запросы на создание изображений.
- `**kwargs`: Дополнительные именованные аргументы, передаваемые базовому провайдеру.

**Возвращает**:

- `str`: Строка, содержащая обработанный ответ, включая сгенерированные изображения.

**Как работает функция**:

1.  Добавляет системное сообщение в начало списка сообщений, чтобы объяснить возможности генерации изображений.

2.  Вызывает асинхронную функцию `create_async` базового провайдера для получения ответа.

3.  Ищет в ответе теги `<img data-prompt="текстовый запрос">`.

4.  Извлекает текстовые запросы из тегов `<img data-prompt="текстовый запрос">`.

5.  Вызывает асинхронную функцию `create_images_async` для создания изображений.

6.  Заменяет теги `<img data-prompt="текстовый запрос">` сгенерированными изображениями.

7.  Если `include_placeholder` имеет значение `True`, заполнитель изображения также включается в результат.

     ```
     A (Добавление системного сообщения)
     ↓
     B (Получение ответа от базового провайдера)
     ↓
     C (Поиск тегов <img data-prompt>)
     ↓
     D (Извлечение текстовых запросов)
     ↓
     E (Создание изображений)
     ↓
     F (Замена тегов изображениями)
     ↓
     G (Включение заполнителя)
     ```

**Примеры**:

```python
# Пример использования create_async
async def main():
    provider = CreateImagesProvider(
        provider=SomeBaseProvider(),
        create_images=some_create_images_function,
        create_async=some_create_async_function
    )
    result = await provider.create_async(model="dalle3", messages=[{"role": "user", "content": "Создай изображение: <img data-prompt='кошка'>"}])
    print(result)

asyncio.run(main())
```