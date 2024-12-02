# <input code>

```python
## \file hypotez/src/endpoints/kazarinov/gemini_chat.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.kazarinov 
	:platform: Windows, Unix
	:synopsis: Module that handles model training using GoogleGenerativeAI for the Kazarinov project

"""
MODE = 'dev'
import header
import time
import json
import random
from typing import Optional
from pathlib import Path
from src import gs
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import get_filenames, read_text_file, recursively_read_text_files, recursively_get_filepath
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger import logger


class KazarinovAI:
    """Handles model training and dialog generation for the Kazarinov project using GoogleGenerativeAI."""

    api_key = gs.credentials.gemini.kazarinov
    # Base paths for system instructions and training files
    base_path = gs.path.google_drive / 'kazarinov'
    system_instruction_list: list = recursively_read_text_files(base_path, ['*.txt', '*.md'])
    #questions_list:list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q', ['*.*'])
    history_file = f'{gs.now}.txt'

    gemini_1: GoogleGenerativeAI
    gemini_2: GoogleGenerativeAI
    timestamp = gs.now

    def __init__(self,
                 system_instruction: str = None,
                 generation_config: dict | list[dict] = {"response_mime_type": "text/plain"}):
        """Initialize the Kazarinov model.

        Args:
            system_instruction (str, optional): Instruction for the model's system role. Defaults to None.
            generation_config (dict | list[dict], optional): Configuration for content generation. 
                Defaults to {"response_mime_type": "text/plain"}.
        """
        self.gemini_1 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={"response_mime_type": "text/plain"},
            history_file=f'{gs.now}.txt'
        )

        self.gemini_2 = GoogleGenerativeAI(
            api_key=self.api_key,
            system_instruction=system_instruction,
            generation_config={"response_mime_type": "text/plain"},
            history_file=f'{gs.now}.txt'
        )


    def train(self):
        """
        Train the model using the provided list of training files, sending data in chunks of specified size.

        Args:
            train_files (list | str): A list or single file name for training.
        """
        chunk_size = 500000
        all_chunks = []
        train_data_list = recursively_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data', ['*.*'], as_list=True)

        current_chunk = ""

        for line in train_data_list:
            while len(current_chunk) + len(line) > chunk_size:
                space_left = chunk_size - len(current_chunk)
                current_chunk += line[:space_left]
                all_chunks.append(current_chunk)
                line = line[space_left:]
                current_chunk = ""

            current_chunk += line

        if current_chunk:
            all_chunks.append(current_chunk)

        for idx, chunk in enumerate(all_chunks):
            pprint(f"{chunk=}\n{len(chunk)}", text_color='light_blue')
            response = self.gemini_1.ask(q=chunk)
            pprint(response, text_color='yellow')
            time.sleep(5)

    def question_answer(self):
        """
        Handles the question-answering process using the provided training files.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', as_list=True)

        for q in questions:
            pprint(self.gemini_1.ask(q))

    def dialog(self):
        """
        Runs a dialog based on pre-defined questions, shuffling questions from different languages.
        """
        questions = recursively_read_text_files(self.base_path / 'prompts' / 'train_data' / 'q', patterns=['*.*'], as_list=True)
        random.shuffle(questions)

        for q in questions:
            pprint(f'Q:> {q}', text_color='yellow')
            pprint(' ', text_color='green')
            a = self.gemini_1.ask(q)
            pprint(f'A:> {a}', text_color='cyan')
            pprint('------------------------------------', text_color='green')
            time.sleep(5)
            ...


    def ask(self, q: str, no_log: bool = False, with_pretrain: bool = True) -> bool:
        """Спрашиваю у машины """
        return self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \n Question: {q}", no_log=no_log, with_pretrain=False)


def chat():
    """Initiates a chat session with the AI assistant, Kazarinov."""
    questions_list = recursively_read_text_files(gs.path.google_drive / 'kazarinov' / 'prompts' / 'q', ['*.*'])

    print(f"""
    Чтобы завершить чат, напишите `--q`
    Чтобы загрузить вопрос из базы вопросов напишите `--next`""")

    logger.info(k.ask("Привет, представься"))
    while True:
        q = input_colored(">>>> ", GREEN)
        if q.lower() == 'exit':
            print("Чат завершен.")
            break

        if q.lower() == '--next' or q.lower() == '--нехт':
            q_list = questions_list[random.randint(0, len(questions_list) - 1)].split('\n')
            q = q_list[random.randint(0, len(q_list) - 1)]
            print(f"{q=}")
            response = k.ask(f"{q}", no_log=True, with_pretrain=False)
            logger.info(response)
            continue

        response = k.ask(q, no_log=False, with_pretrain=False)
        logger.info(response)


if __name__ == "__main__":
    system_instruction = read_text_file(gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt')
    k = KazarinovAI(system_instruction=system_instruction)
    k.train()
    #k.dialog()

```

# <algorithm>

**Алгоритм работы KazarinovAI:**

1. **Инициализация (init):**
   - Создает экземпляры GoogleGenerativeAI (gemini_1, gemini_2) с заданными API-ключом, системными инструкциями и файлом истории.  Эти экземпляры используются для общения с моделью.  
   - Получает системные инструкции из файлов, используя `recursively_read_text_files`.

2. **Обучение (train):**
   - Читает данные для обучения из файлов (`train_data`).
   - Разбивает данные на части (`chunk_size`) для отправки в модель.
   - Отправляет каждую часть (`chunk`) в модель `gemini_1`.
   - Получает ответ от модели.
   - Выводит ответ и ждет 5 секунд, пока не завершится процесс.

3. **Ответ на вопрос (question_answer):**
   - Читает список вопросов из файлов.
   - Отправляет каждый вопрос в модель `gemini_1`.
   - Выводит ответ.

4. **Диалог (dialog):**
   - Читает список вопросов из файлов.
   - Перемешивает вопросы.
   - Выводит вопрос и ждет 5 секунд.
   - Отправляет вопрос в модель `gemini_1`.
   - Выводит ответ.

5. **Запрос (ask):**
   - Формирует запрос для модели, добавляя в него роль и вопрос.
   - Выполняет запрос к модели `gemini_1`.
   - Возвращает ответ.

6. **Чат (chat):**
   - Читает системные инструкции.
   - Создает экземпляр `KazarinovAI`.
   - Выполняет обучение (`k.train()`).
   - Запускает цикл, который:
     - Читает входные данные от пользователя.
     - Если пользователь ввел "--next", выбирает случайный вопрос из базы вопросов и задает его модели.
     - Иначе, отправляет вопрос модели.
     - Выводит ответ модели.
   - Завершается при вводе пользователем "exit".

**Пример:** Пользователь вводит вопрос, чат (chat) отправляет этот вопрос в метод ask класса KazarinovAI, метод ask отправляет его в gemini_1, который возвращает ответ. Чат (chat) выводит ответ пользователю.



# <mermaid>

```mermaid
graph LR
    A[Пользователь] --> B(chat);
    B --> C{Ввод "--next"?};
    C -- Да --> D[Выбрать случайный вопрос];
    D --> E[ask];
    E --> F[gemini_1];
    F --> G[Ответ];
    G --> H[Вывести ответ];
    C -- Нет --> I[Ввод вопроса];
    I --> E;
    subgraph KazarinovAI
        E --> J[ask];
        J --> F;
        F --> G;
        G --> H;
    end
    subgraph GoogleGenerativeAI
      F -- Запрос --> M[Обработка];
      M --> F;  
      M --> G;
    end
    

    
    
```

**Описание диаграммы:**

Диаграмма описывает взаимодействие между пользователем, функцией `chat`, классом `KazarinovAI` и `GoogleGenerativeAI`.
- Пользователь взаимодействует с `chat`, которая вызывает методы класса `KazarinovAI`, в свою очередь взаимодействующие с `GoogleGenerativeAI` для получения ответа.
- Подключаемые зависимости: `gs`, `header`, `time`, `json`, `random`, `typing`, `pathlib`, `src`, `src.ai.openai`, `src.ai.gemini`, `src.utils.file`, `src.utils.jjson`, `src.utils.printer`, `src.logger`.
-  `gs` - предоставляет данные о конфигурации и пути.
-  `header` - вероятно, содержит дополнительные импорты или константы.
- `src` - основной модуль, содержащий утилиты, модели и другие необходимые компоненты.  
- `src.ai` -  содержит классы для работы с моделями OpenAI и Google Generative AI.
- `src.utils` -  содержит утилиты для работы с файлами, JSON, выводом данных.
- `src.logger` - используется для логирования.


# <explanation>

**Импорты:**

- `header`:  Вероятно, содержит дополнительные импорты, необходимые для работы модуля.
- `time`:  Используется для ввода задержек (например, `time.sleep()`).
- `json`: Для работы с JSON-данными (предполагается, что модель работает с ними).
- `random`: Для генерации случайных чисел (например, для выбора вопросов).
- `typing`:  Для явных типов данных (например, `Optional`, `List`).
- `pathlib`:  Для работы с путями к файлам.
- `gs`:  Этот модуль `gs` является частью проекта и, вероятно, содержит конфигурацию и данные о пути к файлам.  
- `OpenAIModel`, `GoogleGenerativeAI`:  Классы для взаимодействия с моделями OpenAI и Google Generative AI.
- `get_filenames`, `read_text_file`, `recursively_read_text_files`, `recursively_get_filepath`:  Утилиты для работы с файлами.
- `j_dumps`:  Функция для записи данных в формате JSON.
- `pprint`:  Функция для красивого вывода данных (вероятно, из `src.utils.printer`).
- `logger`: Модуль для логирования.

**Классы:**

- `KazarinovAI`:  Класс для управления обучением и диалогом с моделью.
    - `api_key`: Ключ доступа к API.
    - `base_path`:  Базовый путь к данным.
    - `system_instruction_list`: Список системных инструкций для модели.
    - `history_file`:  Файл истории для модели.
    - `gemini_1`, `gemini_2`:  Экземпляры модели `GoogleGenerativeAI` для выполнения задач.
    - `__init__`:  Инициализирует экземпляр `KazarinovAI`, создавая `GoogleGenerativeAI` модели.
    - `train`:  Метод для обучения модели на данных, разбитых на части.
    - `question_answer`:  Метод для ответа на вопросы.
    - `dialog`:  Метод для выполнения диалога с моделями.
    - `ask`: Метод для получения ответа от модели.

**Функции:**

- `chat`:  Функция для запуска чата с `KazarinovAI`.
    - Читает системные инструкции.
    - Инициализирует `KazarinovAI`.
    - Выполняет обучение (`k.train()`).
    - Запускает цикл для обработки запросов пользователя.

**Переменные:**

- `MODE`:  Строковая переменная, вероятно, определяющая режим работы (например, 'dev' или 'prod').
- `chunk_size`: Размер частей данных для обучения.


**Возможные ошибки и улучшения:**

- **Обработка исключений:**  Добавление обработчиков исключений (`try...except`)  для обработки ошибок при чтении файлов, запросах к API и других потенциальных проблем.
- **Логирование:** Более подробное логирование для отладки и анализа ошибок.
- **Параллелизм:**  Использование параллельных вычислений для ускорения обучения (например, при обработке больших данных).
- **Переменные окружения:** Использование переменных окружения для хранения API-ключей и других конфигурционных данных.
- **Объектно-ориентированность:** Добавьте в `KazarinovAI` методы для сохранения данных, чтения данных из истории, или оптимизации взаимодействия с моделями.
- **Управление памятью:** При чтении больших файлов данных необходимо учитывать управление памятью, чтобы избежать проблем с потреблением памяти.

**Взаимосвязи с другими частями проекта:**

- Модуль `gs`  связан с `google_drive` и другими частями проекта, вероятно, для доступа к данным и хранению конфигурации.
- Классы `GoogleGenerativeAI` и `OpenAIModel` зависят от соответствующих API и библиотек.
- `src.utils` -  полезные утилиты для работы с данными.
- `src.logger` - предоставляет функции для логирования.

Код нуждается в дополнительной информации и контексте, чтобы дать более точный анализ.