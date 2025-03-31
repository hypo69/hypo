# Модуль для работы с OpenAI Model

## Обзор

Модуль `training.py` предоставляет класс `OpenAIModel` для взаимодействия с OpenAI API, управления моделями и их обучения. Он включает в себя методы для получения списка доступных моделей и ассистентов, настройки ассистента, отправки сообщений модели, анализа тональности, динамической донастройки и обучения модели на основе предоставленных данных.

## Подробней

Этот модуль используется для упрощения работы с OpenAI API, предоставляя удобный интерфейс для выполнения различных задач, связанных с моделями OpenAI. Он облегчает процесс обучения моделей, управления ассистентами и взаимодействия с ними, а также анализа тональности ответов модели.

## Классы

### `OpenAIModel`

**Описание**: Класс `OpenAIModel` предназначен для взаимодействия с OpenAI API и управления моделями.

**Как работает класс**:
Класс `OpenAIModel` инициализируется с использованием API-ключа, системной инструкции и идентификатора ассистента. Он содержит методы для получения списка доступных моделей и ассистентов, настройки ассистента, отправки сообщений модели, анализа тональности, динамической донастройки и обучения модели на основе предоставленных данных.

**Атрибуты**:
- `model` (str): Имя используемой модели (по умолчанию "gpt-4o-mini").
- `client` (OpenAI): Клиент OpenAI для взаимодействия с API.
- `current_job_id` (str): Идентификатор текущей задачи обучения.
- `assistant_id` (str): Идентификатор ассистента.
- `assistant` (Any): Объект ассистента, полученный из OpenAI API.
- `thread` (Any): Объект треда для взаимодействия с ассистентом.
- `system_instruction` (str): Системная инструкция для модели.
- `dialogue_log_path` (str | Path): Путь к файлу журнала диалогов.
- `dialogue` (List[Dict[str, str]]): Список диалогов.
- `assistants` (List[SimpleNamespace]): Список доступных ассистентов.
- `models_list` (List[str]): Список доступных моделей.

**Методы**:
- `__init__`: Инициализирует объект `OpenAIModel` с API-ключом, системной инструкцией и идентификатором ассистента.
- `list_models`: Возвращает список доступных моделей из OpenAI API.
- `list_assistants`: Возвращает список доступных ассистентов из JSON-файла.
- `set_assistant`: Устанавливает ассистента, используя предоставленный идентификатор.
- `_save_dialogue`: Сохраняет весь диалог в JSON-файл.
- `determine_sentiment`: Определяет тональность сообщения (положительную, отрицательную или нейтральную).
- `ask`: Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.
- `describe_image`: Описывает изображение, используя модель OpenAI.
- `describe_image_by_requests`: Описывает изображение, используя запросы к OpenAI API.
- `dynamic_train`: Динамически дообучает модель на основе предыдущего диалога.
- `train`: Обучает модель на основе предоставленных данных или каталога.
- `save_job_id`: Сохраняет идентификатор задачи обучения с описанием в файл.

### `__init__`
```python
def __init__(self, api_key:str, system_instruction: str = None, model_name:str = 'gpt-4o-mini', assistant_id: str = None):
    """Initialize the Model object with API key, assistant ID, and load available models and assistants.

    Args:
        system_instruction (str, optional): An optional system instruction for the model.
        assistant_id (str, optional): An optional assistant ID. Defaults to 'asst_dr5AgQnhhhnef5OSMzQ9zdk9'.
    """
    ...
```
**Назначение**: Инициализирует объект `OpenAIModel` с API-ключом, системной инструкцией и идентификатором ассистента.

**Как работает функция**:
Функция инициализирует клиент OpenAI с использованием предоставленного API-ключа или ключа по умолчанию из `gs.credentials.openai.api_key`. Она также устанавливает идентификатор ассистента, системную инструкцию и загружает ассистента и тред.

Внутри функции происходят следующие действия:
1. Инициализация клиента OpenAI с использованием API-ключа.
2. Установка идентификатора текущей задачи (`current_job_id`) в `None`.
3. Установка идентификатора ассистента, используя предоставленный `assistant_id` или значение по умолчанию из `gs.credentials.openai.assistant_id.code_assistant`.
4. Установка системной инструкции из предоставленного аргумента `system_instruction`.
5. Загрузка ассистента с использованием `client.beta.assistants.retrieve(self.assistant_id)`.
6. Создание треда с использованием `client.beta.threads.create()`.

**Параметры**:
- `api_key` (str): API-ключ для доступа к OpenAI API.
- `system_instruction` (str, optional): Необязательная системная инструкция для модели. По умолчанию `None`.
- `model_name` (str, optional): Имя модели для использования. По умолчанию `'gpt-4o-mini'`.
- `assistant_id` (str, optional): Необязательный идентификатор ассистента. По умолчанию `None`.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Отсутствуют явные исключения, но могут возникнуть исключения при инициализации клиента OpenAI или загрузке ассистента/треда, если API-ключ недействителен или ассистент не существует.

**Примеры**:
```python
model = OpenAIModel(api_key='YOUR_API_KEY', system_instruction='You are a helpful assistant.', assistant_id='asst_123')
```

### `list_models`
```python
@property
def list_models(self) -> List[str]:
    """Dynamically fetch and return available models from the OpenAI API.

    Returns:
        List[str]: A list of model IDs available via the OpenAI API.
    """
    ...
```
**Назначение**: Динамически получает и возвращает список доступных моделей из OpenAI API.

**Как работает функция**:
Функция обращается к OpenAI API для получения списка доступных моделей и возвращает их идентификаторы в виде списка строк.

Внутри функции происходят следующие действия:
1. Попытка получить список моделей с использованием `self.client.models.list()`.
2. Извлечение идентификаторов моделей из полученных данных.
3. Логирование списка загруженных моделей с использованием `logger.info()`.
4. В случае ошибки, логирование ошибки с использованием `logger.error()` и возврат пустого списка.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `List[str]`: Список идентификаторов моделей, доступных через OpenAI API.

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается получить доступ к OpenAI API или если API возвращает ошибку.

**Примеры**:
```python
models = model.list_models
print(models)
```

### `list_assistants`
```python
@property
def list_assistants(self) -> List[str]:
    """Dynamically load available assistants from a JSON file.

    Returns:
        List[str]: A list of assistant names.
    """
    ...
```
**Назначение**: Динамически загружает доступных ассистентов из JSON-файла.

**Как работает функция**:
Функция загружает список ассистентов из JSON-файла, расположенного по пути `gs.path.src / 'ai' / 'openai' / 'model' / 'assistants' / 'assistants.json'`, и возвращает их имена в виде списка строк.

Внутри функции происходят следующие действия:
1. Загрузка списка ассистентов из JSON-файла с использованием `j_loads_ns()`.
2. Извлечение имен ассистентов из загруженных данных.
3. Логирование списка загруженных ассистентов с использованием `logger.info()`.
4. В случае ошибки, логирование ошибки с использованием `logger.error()` и возврат пустого списка.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `List[str]`: Список имен ассистентов.

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается загрузить JSON-файл или если файл имеет неверный формат.

**Примеры**:
```python
assistants = model.list_assistants
print(assistants)
```

### `set_assistant`
```python
def set_assistant(self, assistant_id: str):
    """Set the assistant using the provided assistant ID.

    Args:
        assistant_id (str): The ID of the assistant to set.
    """
    ...
```
**Назначение**: Устанавливает ассистента, используя предоставленный идентификатор.

**Как работает функция**:
Функция устанавливает ассистента, используя предоставленный идентификатор, и загружает информацию об ассистенте из OpenAI API.

Внутри функции происходят следующие действия:
1. Установка идентификатора ассистента `self.assistant_id` в значение `assistant_id`.
2. Получение информации об ассистенте из OpenAI API с использованием `self.client.beta.assistants.retrieve(assistant_id)`.
3. Логирование успешной установки ассистента с использованием `logger.info()`.
4. В случае ошибки, логирование ошибки с использованием `logger.error()`.

**Параметры**:
- `assistant_id` (str): Идентификатор ассистента для установки.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается получить доступ к OpenAI API или если ассистент с указанным идентификатором не существует.

**Примеры**:
```python
model.set_assistant(assistant_id='asst_123')
```

### `_save_dialogue`
```python
def _save_dialogue(self):
    """Save the entire dialogue to the JSON file."""
    ...
```
**Назначение**: Сохраняет весь диалог в JSON-файл.

**Как работает функция**:
Функция сохраняет весь накопленный диалог (список сообщений) в JSON-файл, путь к которому указан в `self.dialogue_log_path`.

Внутри функции происходят следующие действия:
1. Сохранение диалога в JSON-файл с использованием `j_dumps(self.dialogue, self.dialogue_log_path)`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается записать в файл или если файл не существует.

**Примеры**:
```python
model._save_dialogue()
```

### `determine_sentiment`
```python
def determine_sentiment(self, message: str) -> str:
    """Determine the sentiment of a message (positive, negative, or neutral).

    Args:
        message (str): The message to analyze.

    Returns:
        str: The sentiment ('positive', 'negative', or 'neutral').
    """
    ...
```
**Назначение**: Определяет тональность сообщения (положительную, отрицательную или нейтральную).

**Как работает функция**:
Функция анализирует сообщение и определяет его тональность на основе наличия ключевых слов, связанных с положительными, отрицательными или нейтральными эмоциями.

Внутри функции происходят следующие действия:
1. Преобразование сообщения в нижний регистр.
2. Проверка наличия положительных слов в сообщении. Если есть, возвращается "positive".
3. Проверка наличия отрицательных слов в сообщении. Если есть, возвращается "negative".
4. Проверка наличия нейтральных слов в сообщении. Если есть, возвращается "neutral".
5. Если ни одно из вышеперечисленных условий не выполнено, возвращается "neutral".

**Параметры**:
- `message` (str): Сообщение для анализа.

**Возвращает**:
- `str`: Тональность сообщения ('positive', 'negative' или 'neutral').

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
```python
sentiment = model.determine_sentiment("This is a great day!")
print(sentiment)  # Вывод: positive
```

### `ask`
```python
def ask(self, message: str, system_instruction: str = None, attempts: int = 3) -> str:
    """Send a message to the model and return the response, along with sentiment analysis.

    Args:
        message (str): The message to send to the model.
        system_instruction (str, optional): Optional system instruction.
        attempts (int, optional): Number of retry attempts. Defaults to 3.

    Returns:
        str: The response from the model.
    """
    ...
```
**Назначение**: Отправляет сообщение модели и возвращает ответ вместе с анализом тональности.

**Как работает функция**:
Функция отправляет сообщение модели OpenAI и возвращает ответ. Она также выполняет анализ тональности ответа и сохраняет диалог.

Внутри функции происходят следующие действия:
1. Формирование списка сообщений для отправки в модель.
2. Добавление системной инструкции (если указана) в список сообщений.
3. Добавление сообщения пользователя в список сообщений.
4. Отправка запроса к модели с использованием `self.client.chat.completions.create()`.
5. Извлечение ответа из полученного результата.
6. Анализ тональности ответа с использованием `self.determine_sentiment()`.
7. Добавление сообщений и тональности в диалог.
8. Сохранение диалога с использованием `self._save_dialogue()`.
9. В случае ошибки, логирование ошибки и повторная попытка отправки сообщения (если количество попыток не исчерпано).

**Параметры**:
- `message` (str): Сообщение для отправки модели.
- `system_instruction` (str, optional): Необязательная системная инструкция. По умолчанию `None`.
- `attempts` (int, optional): Количество попыток повторной отправки сообщения в случае ошибки. По умолчанию `3`.

**Возвращает**:
- `str`: Ответ от модели.

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается получить доступ к OpenAI API или если модель возвращает ошибку.

**Примеры**:
```python
response = model.ask("What is the capital of France?")
print(response)
```

### `describe_image`
```python
def describe_image(self, image_path: str | Path, prompt:Optional[str] = None, system_instruction:Optional[str] = None ) -> str:
    """"""
    ...
```
**Назначение**: Описывает изображение, используя модель OpenAI.

**Как работает функция**:
Функция отправляет изображение в OpenAI API и получает описание изображения.

Внутри функции происходят следующие действия:
1. Кодирование изображения в base64.
2. Формирование списка сообщений, включающего системную инструкцию (если есть) и запрос с изображением.
3. Отправка запроса к OpenAI API с использованием `self.client.chat.completions.create()`.
4. Извлечение ответа из полученного результата.
5. В случае ошибки, логирование ошибки.

**Параметры**:
- `image_path` (str | Path): Путь к изображению.
- `prompt` (Optional[str], optional): Необязательный запрос для описания изображения. По умолчанию `None`.
- `system_instruction` (Optional[str], optional): Необязательная системная инструкция. По умолчанию `None`.

**Возвращает**:
- `str`: Описание изображения.

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается получить доступ к OpenAI API или если модель возвращает ошибку.

**Примеры**:
```python
description = model.describe_image("path/to/image.jpg", prompt="Describe this image in detail.")
print(description)
```

### `describe_image_by_requests`
```python
def describe_image_by_requests(self, image_path: str | Path, prompt:str = None) -> str:
    """Send an image to the OpenAI API and receive a description."""
    ...
```
**Назначение**: Отправляет изображение в OpenAI API и получает описание.

**Как работает функция**:
Функция отправляет изображение в OpenAI API с использованием библиотеки `requests` и получает описание изображения в ответ.

Внутри функции происходят следующие действия:
1. Кодирование изображения в base64.
2. Формирование заголовков запроса, включающих API-ключ.
3. Формирование полезной нагрузки (payload) запроса, включающей модель, сообщение с изображением и максимальное количество токенов.
4. Отправка POST-запроса к OpenAI API с использованием `requests.post()`.
5. Обработка ответа от API.
6. В случае ошибки, логирование ошибки.

**Параметры**:
- `image_path` (str | Path): Путь к изображению.
- `prompt` (str, optional): Необязательный запрос для описания изображения. По умолчанию `None`.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается отправить запрос к OpenAI API или если API возвращает ошибку.

**Примеры**:
```python
model.describe_image_by_requests("path/to/image.jpg", prompt="Describe this image.")
```

### `dynamic_train`
```python
def dynamic_train(self):
    """Dynamically load previous dialogue and fine-tune the model based on it."""
    ...
```
**Назначение**: Динамически загружает предыдущий диалог и дообучает модель на его основе.

**Как работает функция**:
Функция загружает предыдущий диалог из JSON-файла и использует его для дообучения модели.

Внутри функции происходят следующие действия:
1. Загрузка диалога из JSON-файла с использованием `j_loads()`.
2. Если диалог существует, отправка запроса к OpenAI API для дообучения модели с использованием загруженного диалога.
3. Логирование успешного дообучения или отсутствия предыдущего диалога.
4. В случае ошибки, логирование ошибки.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается загрузить JSON-файл или если API возвращает ошибку.

**Примеры**:
```python
model.dynamic_train()
```

### `train`
```python
def train(self, data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> str | None:
    """Train the model on the specified data or directory.

    Args:
        data (str, optional): Path to a CSV file or CSV-formatted string with data.
        data_dir (Path | str, optional): Directory containing CSV files for training.
        data_file (Path | str, optional): Path to a single CSV file with training data.
        positive (bool, optional): Whether the data is positive or negative. Defaults to True.

    Returns:
        str | None: The job ID of the training job or None if an error occurred.
    """
    ...
```
**Назначение**: Обучает модель на основе предоставленных данных или каталога.

**Как работает функция**:
Функция обучает модель OpenAI на основе предоставленных данных, которые могут быть в виде строки, файла или каталога с файлами.

Внутри функции происходят следующие действия:
1. Определение источника данных (строка, файл или каталог).
2. Загрузка данных из определенного источника.
3. Отправка запроса к OpenAI API для обучения модели с использованием загруженных данных.
4. Получение идентификатора задачи обучения.
5. В случае ошибки, логирование ошибки.

**Параметры**:
- `data` (str, optional): Путь к CSV-файлу или строка в формате CSV с данными.
- `data_dir` (Path | str, optional): Каталог, содержащий CSV-файлы для обучения.
- `data_file` (Path | str, optional): Путь к отдельному CSV-файлу с данными для обучения.
- `positive` (bool, optional): Указывает, являются ли данные положительными или отрицательными. По умолчанию `True`.

**Возвращает**:
- `str | None`: Идентификатор задачи обучения или `None` в случае ошибки.

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается загрузить данные или если API возвращает ошибку.

**Примеры**:
```python
job_id = model.train(data_file="path/to/training_data.csv")
print(job_id)
```

### `save_job_id`
```python
def save_job_id(self, job_id: str, description: str, filename: str = "job_ids.json"):
    """Save the job ID with description to a file.

    Args:
        job_id (str): The job ID to save.
        description (str): Description of the job.
        filename (str, optional): The file to save job IDs. Defaults to "job_ids.json".
    """
    ...
```
**Назначение**: Сохраняет идентификатор задачи обучения с описанием в файл.

**Как работает функция**:
Функция сохраняет идентификатор задачи обучения и его описание в JSON-файл.

Внутри функции происходят следующие действия:
1. Формирование словаря с данными о задаче обучения (идентификатор, описание, время создания).
2. Определение пути к файлу для сохранения данных.
3. Если файл не существует, создание файла и сохранение данных в виде списка.
4. Если файл существует, загрузка существующих данных, добавление новых данных в список и сохранение обновленного списка в файл.

**Параметры**:
- `job_id` (str): Идентификатор задачи обучения.
- `description` (str): Описание задачи обучения.
- `filename` (str, optional): Имя файла для сохранения данных. По умолчанию `"job_ids.json"`.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Исключение может быть вызвано, если не удается записать в файл или если файл не существует.

**Примеры**:
```python
model.save_job_id("job_123", "Training model with new data")
```

## Функции

### `main`
```python
def main():
    """Main function to initialize the OpenAIModel and demonstrate usage.
    Explanation:
        Initialization of the Model:

        The OpenAIModel is initialized with a system instruction and an assistant ID. You can modify the parameters if necessary.
        Listing Models and Assistants:

        The list_models and list_assistants methods are called to print the available models and assistants.
        Asking the Model a Question:

        The ask() method is used to send a message to the model and retrieve its response.
        Dynamic Training:

        The dynamic_train() method performs dynamic fine-tuning based on past dialogue.
        Training the Model:

        The train() method trains the model using data from a specified file (in this case, 'training_data.csv').
        Saving the Training Job ID:

        After training, the job ID is saved with a description to a JSON file."""
    ...
```

**Назначение**: Главная функция для инициализации `OpenAIModel` и демонстрации использования.

**Как работает функция**:
Функция `main` инициализирует класс `OpenAIModel`, демонстрирует методы для получения списка доступных моделей и ассистентов, отправки сообщений модели, динамической донастройки и обучения модели.

Внутри функции происходят следующие действия:
1. Инициализация модели с системной инструкцией и идентификатором ассистента.
2. Вывод списка доступных моделей.
3. Вывод списка доступных ассистентов.
4. Отправка вопроса модели и вывод ответа.
5. Выполнение динамической донастройки модели.
6. Обучение модели с использованием данных из файла.
7. Сохранение идентификатора задачи обучения.
8. Описание изображения.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего (None).

**Вызывает исключения**:
- Отсутствуют явные исключения, но могут возникнуть исключения при взаимодействии с OpenAI API.

**Примеры**:
```python
if __name__ == "__main__":
    main()