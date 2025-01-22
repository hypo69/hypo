# Документация модуля `src.ai.openai`

## Обзор

Модуль представляет собой набор инструментов для взаимодействия с OpenAI API. Он предоставляет функциональность для выполнения запросов к API, управления моделями и обработки ответов.

## Содержание

- [Обзор](#обзор)
- [Классы](#классы)
- [Функции](#функции)
- [Утилиты](#утилиты)

## Классы

### `OpenAIClient`

**Описание**: Этот класс обеспечивает взаимодействие с OpenAI API. Он содержит методы для отправки запросов к API, обработки ответов и управления сессиями.

**Методы**:
  -  `__init__(self, api_key: str, base_url: Optional[str] = "https://api.openai.com/v1/")`: Инициализирует клиента OpenAI с предоставленным API-ключом и базовым URL.
  - `set_base_url(self, base_url: str) -> None`: Устанавливает новый базовый URL для API.
  - `completions(self, model: str, prompt: str, max_tokens: int = 16, temperature: float = 1.0, top_p: float = 1.0, n: int = 1, stream: bool = False, logprobs: Optional[int] = None, stop: Optional[str | List[str]] = None, presence_penalty: float = 0.0, frequency_penalty: float = 0.0, best_of: int = 1, logit_bias: Optional[Dict[str, float]] = None, user: Optional[str] = None) -> Dict[str, Any]`:  Отправляет запрос на завершение текста.
  - `chat(self, model: str, messages: List[Dict[str, str]], temperature: float = 1.0, top_p: float = 1.0, n: int = 1, stream: bool = False, stop: Optional[str | List[str]] = None, max_tokens: Optional[int] = None, presence_penalty: float = 0.0, frequency_penalty: float = 0.0, logit_bias: Optional[Dict[str, float]] = None, user: Optional[str] = None) -> Dict[str, Any]`: Отправляет запрос на завершение чата.
  - `edits(self, model: str, instruction: str, input: Optional[str] = None, n: int = 1, temperature: float = 1.0, top_p: float = 1.0) -> Dict[str, Any]`: Отправляет запрос на редактирование текста.
  - `embeddings(self, model: str, input: str | List[str]) -> Dict[str, Any]`: Отправляет запрос на получение эмбеддингов для текста.
  - `images_generate(self, prompt: str, n: int = 1, size: str = "1024x1024", response_format: str = "url") -> Dict[str, Any]`: Отправляет запрос на генерацию изображений.
  - `images_edit(self, image: str, mask: Optional[str], prompt: str, n: int = 1, size: str = "1024x1024", response_format: str = "url") -> Dict[str, Any]`: Отправляет запрос на редактирование изображений.
  - `images_variations(self, image: str, n: int = 1, size: str = "1024x1024", response_format: str = "url") -> Dict[str, Any]`:  Отправляет запрос на создание вариаций изображений.
  - `audio_transcriptions(self, file: str, model: str = "whisper-1", language: Optional[str] = None, prompt: Optional[str] = None, response_format: str = "json", temperature: float = 0.0) -> Dict[str, Any]`: Отправляет запрос на транскрибирование аудио.
  - `audio_translations(self, file: str, model: str = "whisper-1", prompt: Optional[str] = None, response_format: str = "json", temperature: float = 0.0) -> Dict[str, Any]`: Отправляет запрос на перевод аудио.
  -  `files_list(self) -> Dict[str, Any]`: Получает список файлов, доступных для использования с API.
  - `files_upload(self, file: str, purpose: str) -> Dict[str, Any]`: Загружает файл.
  - `files_delete(self, file_id: str) -> Dict[str, Any]`: Удаляет файл.
  - `files_retrieve(self, file_id: str) -> Dict[str, Any]`: Получает информацию о файле.
  - `fine_tunes_create(self, training_file: str, validation_file: Optional[str] = None, model: str = "curie", n_epochs: int = 4, batch_size: Optional[int] = None, learning_rate_multiplier: Optional[float] = None, prompt_loss_weight: float = 0.01, compute_classification_metrics: bool = False, classification_n_classes: Optional[int] = None, classification_positive_class: Optional[str] = None, classification_betas: Optional[List[float]] = None, suffix: Optional[str] = None) -> Dict[str, Any]`: Запускает процесс тонкой настройки модели.
  - `fine_tunes_list(self) -> Dict[str, Any]`: Получает список настроенных моделей.
  -  `fine_tunes_retrieve(self, fine_tune_id: str) -> Dict[str, Any]`: Получает информацию о процессе тонкой настройки модели.
  - `fine_tunes_cancel(self, fine_tune_id: str) -> Dict[str, Any]`: Отменяет процесс тонкой настройки модели.
  - `fine_tunes_delete(self, fine_tune_id: str) -> Dict[str, Any]`: Удаляет тонко настроенную модель.
  - `fine_tunes_events(self, fine_tune_id: str, stream: bool = False) -> Dict[str, Any]`: Получает события, связанные с процессом тонкой настройки.
  - `models_list(self) -> Dict[str, Any]`: Получает список доступных моделей.
  - `models_retrieve(self, model_id: str) -> Dict[str, Any]`: Получает информацию о модели.
  - `models_delete(self, model_id: str) -> Dict[str, Any]`: Удаляет модель.
  - `moderations(self, input: str | List[str]) -> Dict[str, Any]`: Отправляет запрос на модерацию текста.
  - `get_request(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`: Выполняет GET-запрос к API.
  - `post_request(self, url: str, json_data: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`: Выполняет POST-запрос к API.
  - `delete_request(self, url: str) -> Dict[str, Any]`: Выполняет DELETE-запрос к API.

**Параметры**
- `api_key` (str): API-ключ для OpenAI.
- `base_url` (Optional[str], optional): Базовый URL для OpenAI API. По умолчанию `"https://api.openai.com/v1/"`.

## Функции

### `get_text_from_response`

**Описание**: Извлекает текст из ответа OpenAI API.
   
**Параметры**:
  - `response` (Dict[str, Any]):  Ответ от OpenAI API.

**Возвращает**:
  - `str`: Извлеченный текст из ответа.

### `get_error_from_response`
  
**Описание**: Извлекает сообщение об ошибке из ответа OpenAI API.

**Параметры**:
- `response` (Dict[str, Any]): Ответ от OpenAI API.

**Возвращает**:
  - `str | None`: Сообщение об ошибке или `None`, если ошибки нет.

### `is_response_ok`
  
**Описание**: Проверяет, является ли ответ от OpenAI API успешным.

**Параметры**:
-  `response` (Dict[str, Any]): Ответ от OpenAI API.
  
**Возвращает**:
 - `bool`: `True`, если ответ успешен, в противном случае `False`.

### `create_file_data`
   
**Описание**: Создает словарь с данными файла для передачи в OpenAI API.

**Параметры**:
- `file_path` (str): Путь к файлу.
- `file_purpose` (str): Цель файла.

**Возвращает**:
   - `Tuple[Dict[str, Any], Dict[str, Any]]`: Кортеж, содержащий словарь с файлами и словарь с данными.

**Вызывает исключения**:
   - `FileNotFoundError`: Если файл не найден.

## Утилиты

### `convert_to_dict`
   
**Описание**: Конвертирует объект в словарь.

**Параметры**:
   - `obj` (Any): Объект для конвертации.

**Возвращает**:
   -  `Dict[str, Any]`: Словарь, созданный из объекта.

**Вызывает исключения**:
    - `TypeError`: Если объект не может быть сериализован.

### `check_file_path`
  
**Описание**: Проверяет наличие файла и возвращает его абсолютный путь.

**Параметры**:
-   `file_path` (str): Путь к файлу.

**Возвращает**:
 - `str`: Абсолютный путь к файлу.

**Вызывает исключения**:
    - `FileNotFoundError`: Если файл не найден.

### `read_file`

**Описание**: Читает содержимое файла.

**Параметры**:
- `file_path` (str): Путь к файлу.

**Возвращает**:
  - `str`: Содержимое файла.

**Вызывает исключения**:
 - `FileNotFoundError`: Если файл не найден.
  
### `write_file`
    
**Описание**: Записывает данные в файл.

**Параметры**:
   - `file_path` (str): Путь к файлу.
   - `data` (str): Данные для записи.
  
### `remove_file`

**Описание**: Удаляет файл.
   
**Параметры**:
  -  `file_path` (str): Путь к файлу.
 
**Вызывает исключения**:
    - `FileNotFoundError`: Если файл не найден.