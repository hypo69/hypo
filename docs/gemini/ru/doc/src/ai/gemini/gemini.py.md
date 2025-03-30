# Модуль gemini

## Обзор

Модуль `gemini` предоставляет интеграцию с Google Generative AI для выполнения различных задач, таких как генерация текста, описание изображений и ведение диалогов. Он включает в себя класс `GoogleGenerativeAI`, который упрощает взаимодействие с API Google Gemini.

## Подробнее

Этот модуль позволяет использовать модели Google Gemini для обработки текстовых запросов, анализа изображений и поддержания истории диалогов. Он включает в себя функции для очистки ответов, сохранения и загрузки истории чата, а также обработки ошибок и повторных попыток при взаимодействии с API. Модуль предназначен для использования в асинхронном режиме, что позволяет эффективно обрабатывать запросы и избегать блокировки основного потока выполнения.

## Классы

### `Config`

**Описание**:
Описание класса отсутствует в предоставленном коде.

### `GoogleGenerativeAI`

**Описание**:
Класс для взаимодействия с моделями Google Generative AI.

**Методы**:
- `__post_init__`: Инициализация модели GoogleGenerativeAI с дополнительными настройками.
- `normalize_answer`: Очистка вывода от ` ```md, ```python, ```json, ```html,` ит.п.
- `_start_chat`: Запуск чата с начальной настройкой.
- `clear_history`: Очищает историю чата в памяти и удаляет файл истории, если он существует.
- `_save_chat_history`: Сохраняет всю историю чата в JSON файл.
- `_load_chat_history`: Загружает историю чата из JSON файла.
- `chat`: Обрабатывает чат-запрос с различными режимами управления историей чата.
- `ask`: Метод отправляет текстовый запрос модели и возвращает ответ.
- `ask_async`: Метод асинхронно отправляет текстовый запрос модели и возвращает ответ.
- `describe_image`: Отправляет изображение в Gemini Pro Vision и возвращает его текстовое описание.
- `upload_file`: Загружает файл в Google Generative AI.

**Параметры**:
- `api_key` (str): Ключ API для доступа к Google Generative AI.
- `model_name` (str): Имя используемой модели. По умолчанию "gemini-2.0-flash-exp".
- `dialogue_txt_path` (Path): Путь к файлу для записи диалогов.
- `generation_config` (Dict): Конфигурация генерации. По умолчанию `{"response_mime_type": "text/plain"}`.
- `system_instruction` (Optional[str]): Системные инструкции для модели.
- `history_dir` (Path): Путь к директории для хранения истории.
- `history_txt_file` (Path): Путь к файлу для сохранения истории в текстовом формате.
- `history_json_file` (Path): Путь к файлу для сохранения истории в формате JSON.
- `config` (SimpleNamespace): Конфигурация, загруженная из `gemini.json`.
- `chat_history` (List[Dict]): История чата.
- `model` (Any): Объект модели.
- `_chat` (Any): Объект чата.
- `MODELS` (List[str]): Список доступных моделей.

**Примеры**

```python
from pathlib import Path
from src.ai.gemini.gemini import GoogleGenerativeAI

# Замените 'YOUR_API_KEY' на ваш фактический ключ API
api_key = 'YOUR_API_KEY'
image_path = Path(r"test.jpg")
# Создание экземпляра класса GoogleGenerativeAI
ai = GoogleGenerativeAI(api_key=api_key, system_instruction="Ты - полезный ассистент. Отвечай на все вопросы кратко")

prompt = """Проанализируй это изображение. Выдай ответ в формате JSON,
where the key will be the name of the object, and the value its description.
If there are people, describe their actions."""

async def main():
    if not image_path.is_file():
        print(
            f"Файл {image_path} не существует. Поместите в корневую папку с программой файл с названием test.jpg"
        )
    else:
        description = await ai.describe_image(image_path, prompt=prompt)
        if description:
            print("Описание изображения (с JSON форматом):")
            print(description)
        else:
            print("Не удалось получить описание изображения.")
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Функции

### `main`

```python
async def main():
    ...
```

**Описание**:
Основная функция для демонстрации работы с классом `GoogleGenerativeAI`.

**Примеры**:

```python
# Пример асинхронного запуска функции main
import asyncio
asyncio.run(main())
```