# <input code>

```python
## \file hypotez/src/endpoints/kazarinov/gemini_chat.py
# -*- coding: utf-8 -*-
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

    gemini_1:GoogleGenerativeAI
    gemini_2:GoogleGenerativeAI
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
        train_data_list = recursively_read_text_files(gs.path.data / 'kazarinov' / 'prompts' / 'train_data', ['*.*'], as_list = True)

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
            response = self.gemini_1.ask(q = chunk)
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
            pprint(f'Q:> {q}', text_color = 'yellow')
            pprint(' ', text_color = 'green')
            a = self.gemini_1.ask(q)
            pprint(f'A:> {a}', text_color = 'cyan')
            pprint('------------------------------------', text_color = 'green')
            time.sleep(5)
            ...


    def ask(self, q:str, no_log:bool=False, with_pretrain:bool = True) -> bool:
        return self.gemini_1.ask(f"role: ** assistant asst_w5cM3yqOX1pDJARO2hzNMVZrq ** \n Question: {q}", no_log = no_log, with_pretrain = False )


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
            response = k.ask(f"{q}", no_log = True, with_pretrain = False)
            logger.info(response)
            continue

        response = k.ask(q, no_log = False, with_pretrain = False)
        logger.info(response)


if __name__ == "__main__":
    system_instruction = read_text_file( gs.path.google_drive / 'kazarinov' / 'prompts' / 'system_instruction.txt' )
    k = KazarinovAI(system_instruction = system_instruction)
    k.train()
    #k.dialog()
```

# <algorithm>

(Блок-схема слишком обширна для вставки в markdown.  Предлагаю алгоритм в виде текстового описания с примерами.  Конкретная блок-схема для каждого метода будет слишком громоздкой)

**Описание алгоритма:**

Код реализует взаимодействие с моделью Google Gemini для обучения и диалога.

1. **Инициализация `KazarinovAI`:**  Создает экземпляры `GoogleGenerativeAI` (gemini_1 и gemini_2) с заданными параметрами (API ключ, системные инструкции, файл истории).
   * **Пример:** `self.gemini_1 = GoogleGenerativeAI(api_key='...', system_instruction='...', generation_config={'...'}, history_file='...')`

2. **Метод `train`:** Читает данные для обучения из файлов (разбивая на куски заданного размера), отправляет куски модели `gemini_1`, получает ответ и логгирует его.
   * **Пример:** Если кусок данных `chunk` превышает `chunk_size`, то он разбивается на более мелкие куски. Каждый кусок отправляется в `gemini_1.ask`

3. **Метод `question_answer`:** Задает вопросы из файла вопросов (`train_data/q`), получает ответы от `gemini_1`.

4. **Метод `dialog`:** Случайным образом выбирает вопросы из файлов вопросов, получает ответы от `gemini_1`.
   * **Пример**: Если есть вопросы на разных языках, они перемешиваются перед использованием.

5. **Метод `ask`:** Отправляет вопрос `gemini_1` с дополнительными параметрами (no_log, with_pretrain). Возвращает ответ.
   * **Пример:** `k.ask("Привет, как дела?", no_log=False, with_pretrain=False)`

6. **Функция `chat`:** Запрашивает у пользователя ввод, если пользователь вводит `--next`, то случайным образом выбирает вопрос из базы вопросов. Иначе передает вопрос модели `gemini_1` и логгирует ответ.  
   * **Пример**: если пользователь ввел вопрос, то функция отправляет его в метод ask, а затем обрабатывает полученный ответ.

Взаимодействие между функциями, классами и методами осуществляется через вызовы методов и передачу данных в качестве аргументов.


# <mermaid>

```mermaid
graph LR
    subgraph KazarinovAI
        KazarinovAI --> init; __init__
        init --> train; train()
        init --> question_answer; question_answer()
        init --> dialog; dialog()
        init --> ask; ask()
        train --> gemini_1.ask; ask()  
        question_answer --> gemini_1.ask; ask()
        dialog --> gemini_1.ask; ask()
        ask --> gemini_1.ask; ask()
    end
    subgraph GoogleGenerativeAI
        gemini_1.ask --> response; response()
    end
    subgraph utils
        read_text_files --> data; data()
    end
    subgraph gs
        gs --> credentials; credentials()
        gs --> path; path()
        gs --> now; timestamp()
    end
    
    init -- api_key --> gs.credentials.gemini.kazarinov
    init -- system_instruction_list --> recursively_read_text_files
    train -- train_data --> recursively_read_text_files
    question_answer -- train_data/q --> recursively_read_text_files
    dialog -- train_data/q --> recursively_read_text_files
    
    chat --> KazarinovAI.ask; ask()
    chat -- user input --> KazarinovAI.ask; ask()
    KazarinovAI.ask --> logger; log()
    KazarinovAI.ask --> pprint; display()

```

# <explanation>

**Импорты:**

Код импортирует необходимые модули для работы.  `src` - это корневая директория проекта, где находятся все модули, включая `gs`, `ai.openai`, `ai.gemini`, `utils.file`, `utils.jjson`, `utils.printer`, и `logger`.  Эти импорты позволяют использовать функции и классы из других модулей проекта.

**Классы:**

* **`KazarinovAI`:**  Этот класс является центральным для управления взаимодействием с моделью Gemini. Он имеет атрибуты `gemini_1`, `gemini_2` для хранения экземпляров модели, `api_key`, `base_path`, `system_instruction_list`, для хранения информации о модели и путях к файлам.  Методы `train`, `question_answer`, `dialog`, и `ask` обеспечивают функциональность обучения модели и диалога с ней.

**Функции:**

* **`chat()`:**  Функция инициализирует сеанс диалога с пользователем и получает пользовательские вопросы и отправляет их модели `KazarinovAI`.
* **`train()`:** Функция обучения модели.  Данные разделены на куски (`chunk_size`) для отправки модели, что важно для обработки больших наборов данных.
* **`question_answer()`:**  Задает вопросы из заранее подготовленного набора данных и получает ответы от модели.
* **`dialog()`:** Создает диалоговый процесс.
* **`ask()`:** Отправляет вопрос модели `GoogleGenerativeAI`.

**Переменные:**

Переменные типа `list`, `str`, `dict` используются для хранения данных, например, `system_instruction_list`, `train_data_list`, `all_chunks`, `response`, `q`.

**Возможные ошибки и улучшения:**

* **Обработка исключений:** Код не содержит обработки исключений, связанных с чтением файлов, запросами к модели, или другими потенциальными ошибками. Добавление обработки исключений (try-except блоки) значительно повысит надежность.
* **Конфигурация:** Параметры, такие как `chunk_size`, `api_key`, и другие константы, должны быть определены в отдельном файле конфигурации, что сделает код более гибким и поддерживаемым.
* **Логирование:** Присутствуют логирования с помощью `logger`, но не все действия имеют подробное логгирование.  Это можно улучшить, добавив больше информации о вызовах методов и состояниях модели.
* **Повторное использование кода:** Логика обработки запросов к модели (`gemini_1.ask(chunk)`) повторяется. Возможно, можно вынести ее в отдельную функцию.

**Взаимосвязи с другими частями проекта:**

Код использует модули из других частей проекта (пакет `src`):  `gs` для доступа к конфигурации, `utils.file` для работы с файлами, `ai.gemini` для работы с моделью Gemini и так далее.  Это указывает на модульную архитектуру проекта, где различные модули взаимодействуют для достижения конечной цели.  Проект использует систему конфигурации (gs.path.google_drive), что позволяет легко изменять пути к файлам и другие параметры.