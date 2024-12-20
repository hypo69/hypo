# Модуль интеграции с Google Generative AI

## Обзор

Класс `GoogleGenerativeAI` предназначен для взаимодействия с моделями генеративного ИИ Google. Он предоставляет методы для отправки запросов, обработки ответов, управления диалогами и интеграции с различными функциями ИИ. Включает надежную обработку ошибок, ведение журнала и параметры конфигурации для обеспечения бесперебойной работы.

## Оглавление

- [Модуль интеграции с Google Generative AI](#модуль-интеграции-с-google-generative-ai)
- [Обзор](#обзор)
- [Основные функции](#основные-функции)
- [Обработка ошибок](#обработка-ошибок)
- [Ведение журнала и история](#ведение-журнала-и-история)
- [Зависимости](#зависимости)
- [Пример использования](#пример-использования)


## Основные функции

### `__init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs)`

**Описание**: Инициализирует класс `GoogleGenerativeAI` необходимыми конфигурациями.

**Детали**:
- Устанавливает API ключ, имя модели, конфигурацию генерации и инструкцию системы.
- Определяет пути для ведения журнала диалогов и хранения истории.
- Инициализирует модель Google Generative AI.

### `config()`

**Описание**: Получает конфигурацию из файла настроек.

**Детали**:
- Читает и парсит файл конфигурации, расположенный по пути `gs.path.src / 'ai' / 'gemini' / 'generative_ai.json'`.

### `_start_chat(self)`

**Описание**: Запускает сеанс чата с моделью ИИ.

**Детали**:
- Инициализирует сеанс чата с пустой историей.


### `_save_dialogue(self, dialogue: list)`

**Описание**: Сохраняет диалог в текстовый и JSON файлы.

**Детали**:
- Добавляет каждый сообщение в диалоге в текстовый файл.
- Добавляет каждое сообщение в JSON формате в JSON файл.


### `ask(self, q: str, attempts: int = 15) -> Optional[str]`

**Описание**: Отправляет текстовый запрос модели ИИ и получает ответ.

**Детали**:
- Обрабатывает несколько попыток в случае сетевых ошибок или недоступности сервиса.
- Ведёт журнал ошибок и повторяет попытки с экспоненциальным увеличением задержки.
- Сохраняет диалог в файлы истории.


### `chat(self, q: str) -> str`

**Описание**: Отправляет сообщение в чат модели ИИ и получает ответ.

**Детали**:
- Использует сеанс чата, инициализированный `_start_chat`.
- Ведёт журнал ошибок и возвращает текст ответа.


### `describe_image(self, image_path: Path) -> Optional[str]`

**Описание**: Генерирует текстовое описание изображения.

**Детали**:
- Кодирует изображение в base64 и отправляет его модели ИИ.
- Возвращает сгенерированное описание или записывает ошибку, если операция не удалась.


### `upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool`

**Описание**: Загружает файл в модель ИИ.

**Детали**:
- Обрабатывает загрузку файла и записывает успех или неудачу.
- Обеспечивает повторную логику в случае ошибок.


## Обработка ошибок

Класс включает всестороннюю обработку ошибок для различных сценариев:
- **Сетевые ошибки**: Повторяет попытки с экспоненциальным увеличением задержки.
- **Недоступность сервиса**: Записывает ошибки и повторяет попытки.
- **Превышение лимитов квоты**: Записывает и ожидает перед повтором попытки.
- **Ошибки аутентификации**: Записывает и останавливает дальнейшие попытки.
- **Неверный ввод**: Записывает и повторяет попытки с таймаутом.
- **Ошибки API**: Записывает и останавливает дальнейшие попытки.


## Ведение журнала и история

Все взаимодействия с моделями ИИ регистрируются, а диалоги сохраняются в текстовом и JSON форматах для последующего анализа. Это гарантирует, что все операции могут быть отслежены и просмотрены для отладки или аудита.


## Зависимости

- `google.generativeai`
- `requests`
- `grpc`
- `google.api_core.exceptions`
- `google.auth.exceptions`
- `src.logger`
- `src.utils.printer`
- `src.utils.file`
- `src.utils.date_time`
- `src.utils.convertors.unicode`
- `src.utils.jjson`


## Пример использования

```python
ai = GoogleGenerativeAI(api_key="ваш_ключ_api", system_instruction="Инструкция")
response = ai.ask("Как дела?")
print(response)
```

Этот пример инициализирует класс `GoogleGenerativeAI` и отправляет запрос модели ИИ, выводит ответ.