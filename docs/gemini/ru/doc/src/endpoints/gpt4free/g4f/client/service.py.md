# Модуль service.py

## Обзор

Модуль `service.py` содержит функции для получения моделей и провайдеров, а также для управления провайдерами в контексте библиотеки g4f. Он предоставляет функциональность для конвертации строк в объекты провайдеров, выбора оптимальных моделей и провайдеров на основе заданных критериев, а также для получения информации о последнем использованном провайдере.

## Подробней

Этот модуль играет важную роль в динамическом выборе и управлении провайдерами, используемыми для работы с различными моделями. Он обеспечивает абстракцию над конкретными реализациями провайдеров и моделей, что позволяет легко переключаться между ними и конфигурировать их поведение.

## Функции

### `convert_to_provider`

```python
def convert_to_provider(provider: str) -> ProviderType:
    """
    Преобразует строку с именем провайдера в объект ProviderType.

    Args:
        provider (str): Строка с именем провайдера или списком провайдеров, разделенных пробелами.

    Returns:
        ProviderType: Объект провайдера.

    Raises:
        ProviderNotFoundError: Если провайдер не найден.
    """
```

**Как работает функция**:

1. **Проверка наличия пробелов**: Функция проверяет, содержит ли строка `provider` пробелы. Если да, то она разделяет строку на список имен провайдеров.
2. **Конвертация провайдеров**: Если провайдеров несколько, то функция преобразует каждое имя провайдера в соответствующий объект `ProviderType`, используя `ProviderUtils.convert`.
3. **Создание IterListProvider**: Если список провайдеров не пуст, создается объект `IterListProvider` из списка найденных провайдеров.
4. **Конвертация одиночного провайдера**: Если в строке `provider` нет пробелов, функция пытается преобразовать её в объект `ProviderType` напрямую, используя `ProviderUtils.convert`.
5. **Обработка ошибок**: Если провайдер не найден в `ProviderUtils.convert`, выбрасывается исключение `ProviderNotFoundError`.

**Примеры**:

```python
# Пример вызова функции convert_to_provider
provider = convert_to_provider('Gpt4free')
# => <g4f.providers.gpt4free.Gpt4free object at 0x...>

provider = convert_to_provider('Gpt4free You')
# => <g4f.providers.retry_provider.IterListProvider object at 0x...>
```

### `get_model_and_provider`

```python
def get_model_and_provider(model: Union[Model, str],
                           provider: Union[ProviderType, str, None],
                           stream: bool,
                           ignore_working: bool = False,
                           ignore_stream: bool = False,
                           logging: bool = True,
                           has_images: bool = False) -> tuple[str, ProviderType]:
    """
    Получает модель и провайдера на основе входных параметров.

    Args:
        model (Union[Model, str]): Модель для использования (объект или строковый идентификатор).
        provider (Union[ProviderType, str, None]): Провайдер для использования (объект, строковый идентификатор или None).
        stream (bool): Указывает, должна ли операция выполняться в режиме потока.
        ignore_working (bool, optional): Если True, игнорирует статус работы провайдера. По умолчанию False.
        ignore_stream (bool, optional): Если True, игнорирует возможность потоковой передачи провайдера. По умолчанию False.
        logging (bool, optional):  Определяет, следует ли вести лог использования провайдера и модели. По умолчанию True.
        has_images (bool, optional): Указывает, есть ли изображения во входных данных. По умолчанию False.

    Returns:
        tuple[str, ProviderType]: Кортеж, содержащий имя модели и тип провайдера.

    Raises:
        ProviderNotFoundError: Если провайдер не найден.
        ModelNotFoundError: Если модель не найдена.
        ProviderNotWorkingError: Если провайдер не работает.
        StreamNotSupportedError: Если потоковая передача не поддерживается провайдером.
    """
```

**Как работает функция**:

1. **Проверка версии**: Если включена проверка версии, она выполняется.
2. **Преобразование провайдера**: Если `provider` является строкой, она преобразуется в объект `ProviderType` с использованием `convert_to_provider`.
3. **Преобразование модели**: Если `model` является строкой, она преобразуется в объект `Model` с использованием `ModelUtils.convert`.
4. **Выбор провайдера и модели по умолчанию**: Если `provider` не указан, выбирается провайдер и модель по умолчанию. Если `has_images` имеет значение `True`, то выбираются значения по умолчанию для обработки изображений, в противном случае выбираются общие значения по умолчанию.
5. **Обработка ошибок**: Функция проверяет, найден ли провайдер, работает ли он, и поддерживает ли он потоковую передачу, если это необходимо.
6. **Логирование**: Если `logging` имеет значение `True`, функция записывает в лог информацию об используемом провайдере и модели.

**Примеры**:

```python
# Пример вызова функции get_model_and_provider
model, provider = get_model_and_provider(model='gpt-3.5-turbo', provider='Gpt4free', stream=False)
# => ('gpt-3.5-turbo', <g4f.providers.gpt4free.Gpt4free object at 0x...>)

model, provider = get_model_and_provider(model=None, provider=None, stream=False, has_images=True)
# => ('vision', <g4f.providers.dalle.Dalle object at 0x...>)
```

### `get_last_provider`

```python
def get_last_provider(as_dict: bool = False) -> Union[ProviderType, dict[str, str], None]:
    """
    Получает последнего использованного провайдера.

    Args:
        as_dict (bool, optional): Если True, возвращает информацию о провайдере в виде словаря. По умолчанию False.

    Returns:
        Union[ProviderType, dict[str, str], None]: Последний использованный провайдер (объект или словарь).
    """
```

**Как работает функция**:

1. **Получение последнего провайдера**: Функция получает последнего использованного провайдера из `debug.last_provider`.
2. **Обработка RetryProvider**: Если последний провайдер является экземпляром `BaseRetryProvider`, функция получает последнего провайдера из него.
3. **Форматирование результата**: Если `as_dict` имеет значение `True`, функция возвращает информацию о провайдере в виде словаря, содержащего имя, URL, модель и метку провайдера.

**Примеры**:

```python
# Пример вызова функции get_last_provider
last_provider = get_last_provider()
# => <g4f.providers.gpt4free.Gpt4free object at 0x...>

last_provider_dict = get_last_provider(as_dict=True)
# => {'name': 'Gpt4free', 'url': 'https://gpt4free.com', 'model': 'gpt-3.5-turbo', 'label': None}