# <input code>

```rst
.. module: src.ai.gemini
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


```markdown
# <algorithm>

В целом, алгоритм работы `GoogleGenerativeAI` заключается в инициализации, получении конфигурации, запуске сессии чата, обработке запросов, описании изображений и загрузке файлов, с учетом обработки ошибок и ведения журналов.

**1. Инициализация (`__init__`)**:
   - Принимает API-ключ, имя модели, конфигурацию, системную инструкцию и другие параметры.
   - Устанавливает пути для сохранения истории диалогов.
   - Инициализирует модель Google Generative AI (подробности скрыты).

**Пример**:  `ai = GoogleGenerativeAI(api_key="YOUR_API_KEY")`

**2. Получение конфигурации (`config`)**:
   - Читает и парсит JSON файл `generative_ai.json`.

**Пример**:  Извлекает значения `api_key` и `model_name` из файла.

**3. Запуск чата (`_start_chat`)**:
   - Инициализирует пустую историю диалога.


**4. Запрос (`ask`)**:
   - Повторяет попытку отправки запроса `q` до `attempts` раз с экспоненциальной задержкой при ошибках.
   - Сохраняет диалог в файлы.


**Пример**:  `ai.ask("Расскажите что-нибудь интересное")`

**5. Диалог (`chat`)**:
   - Использует инициализированную сессию чата для отправки запроса `q`.


**Пример**: `ai.chat("Какой сейчас день недели?")`

**6. Описание изображения (`describe_image`)**:
    - Кодирует изображение `image_path` в base64.
    - Отправляет закодированное изображение модели.


**7. Загрузка файла (`upload_file`)**:
   - Загружает файл `file` в модель.
   - Обрабатывает возможные ошибки и повторяет попытки.


# <mermaid>

```mermaid
graph LR
    A[GoogleGenerativeAI] --> B{__init__(api_key, ...)};
    B --> C[config()];
    B --> D[_start_chat()];
    C --> E[generative_ai.json];
    D --> F[_save_dialogue()];
    A --> G[ask(q)];
    G --> H[Обработка ошибок и повторы];
    H --> I[Модель ИИ];
    I --> J[Ответ];
    J --> K[Сохранение истории];
    A --> L[chat(q)];
    L --> I;
    A --> M[describe_image(image_path)];
    M --> I;
    A --> N[upload_file(file)];
    N --> I;

    subgraph "Взаимодействие с библиотеками"
        I --> O[google.generativeai];
        I --> P[requests];
        I --> Q[grpc];
        I --> R[google.api_core.exceptions];
        I --> S[google.auth.exceptions];
        I --> T[src.logger];
        I --> U[src.utils];
    end
```

**Объяснение диаграммы:**

Диаграмма показывает взаимодействие компонентов `GoogleGenerativeAI` с другими модулями, в частности, с внешними библиотеками (`google.generativeai`, `requests`, `grpc`).  Обработка запроса `ask`, `chat`, `describe_image` и `upload_file` происходит через общую точку - взаимодействие с моделью ИИ (`google.generativeai` и др.). Взаимодействие со `src.utils` указывает на использование вспомогательных функций для работы с файлами, временем и т.д.


# <explanation>

**Импорты**: Импортируются необходимые библиотеки для взаимодействия с Google Generative AI (`google.generativeai`, `requests`, `grpc`), обработки исключений (`google.api_core.exceptions`, `google.auth.exceptions`),  а также вспомогательные модули из `src.utils` (для работы с файлами, временем, кодировками).

**Классы**: Класс `GoogleGenerativeAI` представляет собой интерфейс для взаимодействия с Google Generative AI моделями. Он содержит методы для работы с запросами, диалогами, изображениями и файлами.

**Функции**:
- `__init__`: Инициализирует объект с ключом API, настройками и файлами.
- `config`: Читает конфигурацию из файла.
- `_start_chat`: Начинает сессию чата.
- `_save_dialogue`: Сохраняет диалоги в файлы.
- `ask`: Отправляет запрос и обрабатывает возможные ошибки.
- `chat`: Отправляет сообщение в сессию чата.
- `describe_image`: Генерирует описание изображения.
- `upload_file`: Загружает файл.


**Переменные**: Переменные хранят ключи API, пути к файлам, конфигурацию, запросы и ответы.

**Возможные ошибки и улучшения**:
- Отсутствие явного указания обработанных исключений. Для повышения надежности необходимо добавить `try...except` блоки для конкретных видов исключений (например, `requests.exceptions.RequestException` для сетевых ошибок).
- Нехватка документации о используемых методах Google Generative AI.


**Связь с другими частями проекта**: `GoogleGenerativeAI` использует компоненты `src.logger` (для ведения журналов),  `src.utils` (для работы с файлами и другими вспомогательными функциями) и, очевидно,  зависит от остальных частей приложения `hypo` для работы с конфигурацией.