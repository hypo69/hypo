# Модуль `provider.py`

## Обзор

Модуль `provider.py` предназначен для обеспечения локальной поддержки различных языковых моделей, таких как GPT4All, в проекте `hypotez`. Он содержит функции для поиска, загрузки и создания завершений текста с использованием этих моделей.

## Подробнее

Этот модуль позволяет использовать локально установленные языковые модели, что может быть полезно для задач, требующих конфиденциальности или работы в условиях ограниченного доступа к сети. Модуль также предоставляет функциональность для автоматической загрузки недостающих моделей.

## Функции

### `find_model_dir`

```python
def find_model_dir(model_file: str) -> str:
    """
    Определяет директорию, в которой находится файл модели.

    Args:
        model_file (str): Имя файла модели.

    Returns:
        str: Путь к директории, содержащей файл модели.
             Если файл найден в одной из стандартных директорий (внутри проекта или в текущей рабочей директории),
             возвращает путь к этой директории. В противном случае возвращает путь к новой директории `models` в проекте.

    Как работает функция:
    1. Определяет абсолютный путь к текущему файлу.
    2. Определяет путь к корневой директории проекта, поднимаясь на один уровень выше текущей директории.
    3. Формирует путь к новой директории моделей внутри проекта (`<project_dir>/models`).
    4. Формирует полный путь к файлу модели в новой директории.
    5. Проверяет, существует ли файл модели в новой директории. Если да, возвращает путь к новой директории.
    6. Если файл не найден в новой директории, формирует путь к старой директории моделей (внутри текущей директории).
    7. Формирует полный путь к файлу модели в старой директории.
    8. Проверяет, существует ли файл модели в старой директории. Если да, возвращает путь к старой директории.
    9. Если файл не найден в старой директории, устанавливает текущую рабочую директорию (`./`).
    10. Проходит по всем поддиректориям текущей рабочей директории в поисках файла модели.
    11. Если файл найден в какой-либо поддиректории, возвращает путь к этой поддиректории.
    12. Если файл не найден нигде, возвращает путь к новой директории моделей внутри проекта.

    ASCII flowchart:

    Определение путей к директориям и файлам моделей
    │
    ├── Проверка наличия файла модели в новой директории
    │   └── Возврат пути к новой директории (если файл найден)
    │
    ├── Проверка наличия файла модели в старой директории
    │   └── Возврат пути к старой директории (если файл найден)
    │
    ├── Поиск файла модели в текущей рабочей директории и ее поддиректориях
    │   └── Возврат пути к директории, содержащей файл (если файл найден)
    │
    └── Возврат пути к новой директории (если файл не найден нигде)

    """
    local_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(local_dir))

    new_model_dir = os.path.join(project_dir, "models")
    new_model_file = os.path.join(new_model_dir, model_file)
    if os.path.isfile(new_model_file):
        return new_model_dir

    old_model_dir = os.path.join(local_dir, "models")
    old_model_file = os.path.join(old_model_dir, model_file)
    if os.path.isfile(old_model_file):
        return old_model_dir

    working_dir = "./"
    for root, dirs, files in os.walk(working_dir):
        if model_file in files:
            return root

    return new_model_dir
```

### `LocalProvider`

#### `create_completion`

```python
    @staticmethod
    def create_completion(model: str, messages: Messages, stream: bool = False, **kwargs):
        """
        Создает завершение текста с использованием локальной языковой модели.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для контекста.
            stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу. По умолчанию `False`.
            **kwargs: Дополнительные аргументы.

        Returns:
            Generator[str, None, None] | None: Генератор токенов, если `stream` установлен в `True`, иначе `None`.

        Raises:
            ValueError: Если модель не найдена или не реализована.

        Как работает функция:
        1. Проверяет, инициализирован ли список моделей `MODEL_LIST`. Если нет, инициализирует его с помощью `get_models()`.
        2. Проверяет, есть ли указанная модель в списке `MODEL_LIST`. Если нет, вызывает исключение `ValueError`.
        3. Извлекает информацию о модели из `MODEL_LIST`.
        4. Определяет директорию, в которой находится файл модели, с помощью функции `find_model_dir`.
        5. Проверяет, существует ли файл модели в найденной директории. Если нет, предлагает пользователю загрузить модель.
        6. Если пользователь соглашается, загружает модель с помощью `GPT4All.download_model`.
        7. Инициализирует модель GPT4All с указанными параметрами.
        8. Формирует системное сообщение, объединяя содержимое всех сообщений с ролью "system".
        9. Формирует шаблон запроса и объединяет все сообщения с ролями, отличными от "system", в строку разговора.
        10. Определяет функцию `should_not_stop`, которая определяет, следует ли остановить генерацию токенов на основе содержимого токена.
        11. Открывает сессию чата с моделью, используя системное сообщение и шаблон запроса.
        12. Если `stream` установлен в `True`, генерирует токены в потоковом режиме и возвращает генератор токенов.
        13. Если `stream` установлен в `False`, генерирует все токены сразу и возвращает их.

        ASCII flowchart:

        Инициализация и проверка списка моделей
        │
        ├── Проверка наличия модели в списке
        │   └── Вызов исключения ValueError (если модель не найдена)
        │
        ├── Определение директории файла модели
        │
        ├── Проверка наличия файла модели
        │   └── Предложение пользователю загрузить модель (если файл не найдена)
        │
        ├── Инициализация модели GPT4All
        │
        ├── Формирование системного сообщения и строки разговора
        │
        ├── Генерация токенов в потоковом или не потоковом режиме
        │   └── Возврат генератора токенов (если stream=True)
        │   └── Возврат всех токенов (если stream=False)

        Примеры:
        >>> LocalProvider.create_completion(model="ggml-model-gpt4all-falcon-q4_0.bin", messages=[{"role": "user", "content": "Hello"}])
        <generator object GPT4All.generate at 0x...>
        """
        global MODEL_LIST
        if MODEL_LIST is None:
            MODEL_LIST = get_models()
        if model not in MODEL_LIST:
            raise ValueError(f'Model "{model}" not found / not yet implemented')

        model = MODEL_LIST[model]
        model_file = model["path"]
        model_dir = find_model_dir(model_file)
        if not os.path.isfile(os.path.join(model_dir, model_file)):
            print(f'Model file "models/{model_file}" not found.')
            download = input(f"Do you want to download {model_file}? [y/n]: ")
            if download in ["y", "Y"]:
                GPT4All.download_model(model_file, model_dir)
            else:
                raise ValueError(f'Model "{model_file}" not found.')

        model = GPT4All(model_name=model_file,
                        #n_threads=8,
                        verbose=False,
                        allow_download=False,
                        model_path=model_dir)

        system_message = "\\n".join(message["content"] for message in messages if message["role"] == "system")
        if system_message:
            system_message = "A chat between a curious user and an artificial intelligence assistant."

        prompt_template = "USER: {0}\\nASSISTANT: "
        conversation    = "\\n" . join(
            f"{message['role'].upper()}: {message['content']}"
            for message in messages
            if message["role"] != "system"
        ) + "\\nASSISTANT: "

        def should_not_stop(token_id: int, token: str):
            """
            Определяет, следует ли остановить генерацию токенов на основе содержимого токена.

            Args:
                token_id (int): Идентификатор токена.
                token (str): Содержимое токена.

            Returns:
                bool: `True`, если генерацию следует продолжить, `False`, если следует остановить.

            Как работает внутренняя функция:
            Проверяет, содержит ли токен слово "USER". Если да, возвращает `False`, чтобы остановить генерацию.
            В противном случае возвращает `True`, чтобы продолжить генерацию.

            ASCII flowchart:
            Проверка наличия "USER" в токене
            │
            └── Возврат True или False в зависимости от результата проверки

            Примеры:
            >>> should_not_stop(1, "Hello")
            True
            >>> should_not_stop(2, "USER: How are you?")
            False
            """
            return "USER" not in token

        with model.chat_session(system_message, prompt_template):
            if stream:
                for token in model.generate(conversation, streaming=True, callback=should_not_stop):
                    yield token
            else:
                yield model.generate(conversation, callback=should_not_stop)