# Модуль для работы с провайдером Theb.ai

## Обзор

Модуль предоставляет интерфейс для взаимодействия с сервисом Theb.ai, использующим модель `gpt-3.5-turbo`. Он позволяет отправлять запросы к модели и получать ответы в потоковом режиме.

## Подробней

Модуль содержит функции и настройки, необходимые для аутентификации и взаимодействия с API Theb.ai. Он использует subprocess для запуска скрипта `theb.py`, который выполняет фактические запросы к API.

## Переменные

- `url (str)`: URL сервиса Theb.ai.
- `model (list)`: Список поддерживаемых моделей (в данном случае `gpt-3.5-turbo`).
- `supports_stream (bool)`: Указывает, поддерживает ли провайдер потоковый режим (в данном случае `True`).
- `needs_auth (bool)`: Указывает, требуется ли аутентификация для доступа к провайдеру (в данном случае `False`).
- `params (str)`: Строка, содержащая информацию о поддерживаемых типах данных для параметров функции `_create_completion`.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к API Theb.ai и возвращает ответ в потоковом режиме.

    Args:
        model (str): Идентификатор модели для использования.
        messages (list): Список сообщений для отправки в запросе.
        stream (bool): Указывает, следует ли возвращать ответ в потоковом режиме.
        **kwargs: Дополнительные аргументы для передачи в запрос.

    Returns:
        Generator[str, None, None]: Генератор строк, содержащий ответ от API Theb.ai.

    Как работает функция:
    1. Функция определяет путь к директории, где расположен текущий скрипт.
    2. Формирует JSON-конфигурацию с сообщениями и моделью.
    3. Запускает subprocess с Python-скриптом `theb.py`, передавая JSON-конфигурацию в качестве аргумента.
    4. Итерируется по строкам, возвращаемым из стандартного вывода subprocess, и возвращает их в виде генератора.

    Flowchart:

    Определение пути к скрипту
    |
    Создание JSON конфигурации
    |
    Запуск subprocess с theb.py
    |
    Чтение и передача строк из stdout
    
    """
    path = os.path.dirname(os.path.realpath(__file__))
    config = json.dumps({
        'messages': messages,
        'model': model}, separators=(',', ':'))
    
    cmd = ['python3', f'{path}/helpers/theb.py', config]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def read_output():
        """
        Внутренняя функция для чтения и декодирования вывода из subprocess.
        Args:
            None
        Returns:
            yield line.decode('utf-8')
        """
        for line in iter(p.stdout.readline, b''):
            yield line.decode('utf-8')

    return read_output()
```

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Данная переменная формирует строку, содержащую информацию о поддерживаемых типах данных для параметров функции `_create_completion`.

**Пример:**

```python
print(params)
```

Вывод:

```
g4f.Providers.Theb supports: (model: str, messages: list, stream: bool)