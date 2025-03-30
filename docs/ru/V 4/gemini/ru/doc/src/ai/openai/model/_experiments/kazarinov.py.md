# Модуль _experiments.kazarinov

## Обзор

Модуль `_experiments.kazarinov` предназначен для экспериментов с OpenAI API. Он содержит класс `OpenAIChat` для взаимодействия с моделью GPT-3.5-turbo и функцию `chat` для организации диалога с пользователем через консоль.

## Подробней

Этот модуль предоставляет базовый интерфейс для отправки запросов в OpenAI и получения ответов. Он загружает системную инструкцию из файла `system_instruction.txt` и использует её для инициализации модели. Класс `OpenAIChat` инкапсулирует логику взаимодействия с OpenAI API, а функция `chat` обеспечивает простой способ ведения диалога с пользователем через консоль.

## Классы

### `OpenAIChat`

**Описание**: Класс для взаимодействия с OpenAI API.

**Методы**:
- `__init__`: Инициализирует объект `OpenAIChat`.
- `ask`: Отправляет вопрос в модель OpenAI и возвращает ответ.

**Параметры**:
- `api_key` (str): Ключ API для доступа к OpenAI.
- `system_instruction` (str, optional): Системная инструкция для модели. По умолчанию `None`.

**Примеры**

```python
from pathlib import Path
from src.utils.file import read_text_file
from src.ai.openai.model._experiments.kazarinov import OpenAIChat

system_instruction_path = Path('../src/ai/openai/model/_experiments/system_instruction.txt')
system_instruction = read_text_file(system_instruction_path)

api_key = "YOUR_API_KEY"  # Замените на ваш реальный API-ключ
ai = OpenAIChat(api_key=api_key, system_instruction=system_instruction)
response = ai.ask(prompt="Привет, как дела?")
print(response)
```

## Функции

### `chat`

```python
def chat():
    """
    """
```

**Описание**: Функция для организации диалога с пользователем через консоль.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- `Exception`: В случае ошибки при обработке запроса к OpenAI.

**Примеры**:

```python
from src.ai.openai.model._experiments.kazarinov import chat

chat() # запускает сессию чата