```rst
.. :module: src.ai.gemini
```
[English](https://github.com/hypo69/hypo/tree/master/src/ai/gemini/README.MD)
# Модуль интеграции Google Generative AI

## Обзор

Класс `GoogleGenerativeAI` предназначен для взаимодействия с моделями Google Generative AI. Этот класс предоставляет методы для отправки запросов, обработки ответов, управления диалогами и интеграции с различными функциональностями ИИ. Он включает в себя надежную обработку ошибок, ведение журнала и настройки конфигурации для обеспечения беспрепятственной работы.

## Основные функции

### `__init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs)`

**Назначение**: Инициализирует класс `GoogleGenerativeAI` с необходимыми конфигурациями.

**Детали**:
- Устанавливает ключ API, имя модели, конфигурацию генерации и системную инструкцию.
- Определяет пути для ведения журнала диалогов и хранения истории.
- Инициализирует модель Google Generative AI.

### `config()`

**Назначение**: Получает конфигурацию из файла настроек.

**Детали**:
- Читает и разбирает файл конфигурации, расположенный по пути `gs.path.src / 'ai' / 'gemini' / 'generative_ai.json'`.

### `_start_chat(self)`

**Назначение**: Запускает сессию чата с моделью ИИ.

**Детали**:
- Инициализирует сессию чата с пустой историей.

### `_save_dialogue(self, dialogue: list)`

**Назначение**: Сохраняет диалог в текстовые и JSON файлы.

**Детали**:
- Добавляет каждое сообщение в диалоге в текстовый файл.
- Добавляет каждое сообщение в формате JSON в JSON файл.

### `ask(self, q: str, attempts: int = 15) -> Optional[str]`

**Назначение**: Отправляет текстовый запрос модели ИИ и получает ответ.

**Детали**:
- Обрабатывает несколько попыток в случае ошибок сети или недоступности сервиса.
- Ведет журнал ошибок и повторяет попытки с экспоненциальной задержкой.
- Сохраняет диалог в файлы истории.

### `chat(self, q: str) -> str`

**Назначение**: Отправляет сообщение чата модели ИИ и получает ответ.

**Детали**:
- Использует сессию чата, инициализированную методом `_start_chat`.
- Ведет журнал ошибок и возвращает текст ответа.

### `describe_image(self, image_path: Path) -> Optional[str]`

**Назначение**: Генерирует текстовое описание изображения.

**Детали**:
- Кодирует изображение в base64 и отправляет его модели ИИ.
- Возвращает сгенерированное описание или ведет журнал ошибки, если операция не удалась.

### `upload_file(self, file: str | Path | IOBase, file_name: Optional[str] = None) -> bool`

**Назначение**: Загружает файл в модель ИИ.

**Детали**:
- Обрабатывает загрузку файла и ведет журнал успеха или неудачи.
- Предоставляет логику повторных попыток в случае ошибок.

## Обработка ошибок

Класс включает в себя комплексную обработку ошибок для различных сценариев:
- **Ошибки сети**: Повторяет попытки с экспоненциальной задержкой.
- **Недоступность сервиса**: Ведет журнал ошибок и повторяет попытки.
- **Лимиты квот**: Ведет журнал и ждет перед повторной попыткой.
- **Ошибки аутентификации**: Ведет журнал и прекращает дальнейшие попытки.
- **Неверный ввод**: Ведет журнал и повторяет попытки с таймаутом.
- **Ошибки API**: Ведет журнал и прекращает дальнейшие попытки.

## Ведение журнала и история

Все взаимодействия с моделями ИИ ведутся в журнале, и диалоги сохраняются как в текстовых, так и в JSON форматах для последующего анализа. Это обеспечивает отслеживаемость всех операций и возможность их просмотра для отладки или аудита.

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
ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
response = ai.ask("Как дела?")
print(response)
```

Этот пример инициализирует класс `GoogleGenerativeAI` и отправляет запрос модели ИИ, выводя ответ.

---

Для получения более подробной информации обратитесь к исходному коду и комментариям внутри класса `GoogleGenerativeAI`.