# <input code>

```python
## \file hypotez/src/endpoints/hypo69/psychologist_bot/bot.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.hypo69.psychologist_bot 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.endpoints.hypo69.psychologist_bot """


...
""" t.me/hypo69_psychologist_bot_bot's specific bot with customized behavior."""

import asyncio
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
import random
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext

from src import gs
from src.bots.telegram import TelegramBot
from src.webdriver.driver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import read_text_file, recursively_read_text_files, save_text_file
from src.utils.url import is_url
from src.logger import logger

@dataclass
class PsychologistTelgrambot(TelegramBot):
    """Telegram bot with custom behavior for Kazarinov."""

    token: str = field(init=False)
    d: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: list = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self):
        mode = 'test'
        #self.token = gs.credentials.telegram.hypo69_test_bot if mode == 'test' else gs.credentials.telegram.hypo69_psychologist_bot
        self.token = gs.credentials.telegram.hypo69_psychologist_bot
        super().__init__(self.token)

        self.d = Driver(Chrome)
        
        self.system_instruction = read_text_file(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'chat_system_instruction.txt'
        )
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )

        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.hypo69_psychologist_bot,
            system_instruction=self.system_instruction,
            generation_config={"response_mime_type": "text/plain"}
        )
        
        self.register_handlers()

    # ... (other methods)
```

# <algorithm>

**Шаг 1:** Инициализация `PsychologistTelgrambot`.
   - Получает `token` бота из `gs.credentials`.
   - Инициализирует `Driver` (вероятно, для работы с браузером).
   - Читает `system_instruction` из файла на Google Drive.
   - Читает список вопросов `questions_list` из файлов на Google Drive.
   - Инициализирует `GoogleGenerativeAI` с заданными параметрами.
   - Регистрирует обработчики команд и сообщений (`register_handlers`).

**Шаг 2:** Регистрация обработчиков (`register_handlers`).
   - Добавляет обработчики для команд `/start`, `/help`.
   - Добавляет обработчик для текстовых сообщений (`handle_message`).
   - Добавляет обработчики для голосовых сообщений (`handle_voice`), документов (`handle_document`).

**Шаг 3:** Обработка команды `/start` (`start`).
   - Отправляет приветственное сообщение пользователю.
   - Вызывает `super().start()`.

**Шаг 4:** Обработка текстового сообщения (`handle_message`).
   - Читает текст сообщения.
   - Сохраняет текст в лог-файл на Google Drive.
   - Запрашивает ответ у `GoogleGenerativeAI`, используя текст сообщения и историю (`history_file`).
   - Отправляет ответ пользователю.

**Шаг 5:** Обработка URL-адресов (`get_handler_for_url`).
   - Проверяет, начинается ли полученный текст с URL, определённых в `url_handlers`.
   - Если URL соответствует, вызывает соответствующий обработчик (`handle_suppliers_response`, `handle_onetab_response`).

**Шаг 6:** Обработка URL-адресов поставщиков (`handle_suppliers_response`).
   - Использует `mexiron.run_scenario` для обработки сценария.
   - Отправляет ответ пользователю в зависимости от результата выполнения сценария.

**Шаг 7:** Обработка URL-адресов `OneTab` (`handle_onetab_response`).
   - Использует `mexiron.run_scenario` для обработки сценария.
   - Отправляет ответ пользователю в зависимости от результата выполнения сценария.

**Шаг 8:** Обработка команды `/next` и других похожих (`handle_next_command`).
   - Выбирает случайный вопрос из списка `questions_list`.
   - Запрашивает ответ у `GoogleGenerativeAI`.
   - Отправляет вопрос и ответ пользователю.


**Пример данных:**
- Пользователь вводит сообщение: "Привет"
- Код сохраняет это сообщение в лог-файл.
- `GoogleGenerativeAI` обрабатывает сообщение и генерирует ответ.
- Код отправляет ответ пользователю.

# <mermaid>

```mermaid
graph LR
    A[User] --> B(PsychologistTelgrambot);
    B --> C{Command / Message};
    C -- /start --> D[start];
    C -- /help --> E[help_command];
    C -- Text --> F[handle_message];
    C -- URL --> G[get_handler_for_url];
    G --> H[handle_suppliers_response];
    G --> I[handle_onetab_response];
    F --> J[save_text_file];
    J --> K[GoogleGenerativeAI];
    K --> L[Generate Answer];
    L --> M[Send Answer];
    M --> A;
    D --> N[Reply "Hi!"];
    N --> A;
    H --> O[mexiron.run_scenario];
    O -- Success --> P[Reply "Готово!"];
    O -- Failure --> Q[Reply "Хуёвенько"];
    P --> A;
    Q --> A;
    I --> O;

    subgraph Dependencies
        gs --> B;
        TelegramBot --> B;
        Driver --> B;
        Chrome --> Driver;
        GoogleGenerativeAI --> B;
        read_text_file --> B;
        recursively_read_text_files --> B;
        save_text_file --> B;
        is_url --> G;
        logger --> B;
    end
```

# <explanation>

**Импорты:**
- `asyncio`: Для асинхронного программирования.
- `pathlib`: Для работы с путями к файлам.
- `typing`: Для типизации.
- `dataclasses`: Для создания данных классов.
- `random`: Для генерации случайных чисел.
- `telegram`: Библиотека для работы с Telegram API.
- `telegram.ext`: Модуль для создания Telegram ботов.
- `src`: Корневой пакет проекта.
    - `gs`: Вероятно, содержит глобальные настройки и данные.
    - `bots.telegram`: Классы для работы с Telegram ботами.
    - `webdriver.driver`: Классы для работы с веб-драйверами.
    - `ai.gemini`: Класс для работы с Gemini API.
    - `utils.file`: Функции для работы с файлами.
    - `utils.url`: Функция для проверки URL.
    - `logger`: Логгер ошибок и информации.

**Классы:**
- `PsychologistTelgrambot(TelegramBot)`: Наследует от `TelegramBot`, добавляя специализированные методы для психологического бота.
    - `token`, `d`, `model`, `system_instruction`, `questions_list`, `timestamp`: Атрибуты для хранения данных.
    - `__post_init__`: Инициализация атрибутов, выполняется после инициализации объекта.
    - `register_handlers`: Регистрирует обработчики команд и сообщений.
    - `start`, `handle_message`, `handle_voice`, `handle_document`, `get_handler_for_url`, `handle_suppliers_response`, `handle_onetab_response`, `handle_next_command`: Методы для обработки различных типов сообщений.
    - Взаимодействие: Использует `TelegramBot`, `GoogleGenerativeAI`, `Driver` и другие компоненты из `src` для выполнения задач.

**Функции:**
- `read_text_file`, `recursively_read_text_files`, `save_text_file`: Работа с файлами.
- `get_handler_for_url`: Выбирает обработчик для определенного URL-адреса.
- `handle_suppliers_response`, `handle_onetab_response`: Обработка сообщений, связанных с URL-адресами.
- `handle_next_command`: Обработка команд, связанных с получением случайного вопроса.


**Переменные:**
- `MODE`: Значение для выбора режима работы бота ('dev' или 'test').

**Возможные ошибки и улучшения:**
- Отсутствует проверка на существование файлов на Google Drive, что может привести к ошибкам.
- Словарь `url_handlers` содержит жестко закодированные URL-адреса.
- `mexiron` не определен, что указывает на зависимость от внешнего компонента, нуждающегося в описании.
- Отсутствие обработки ошибок в функциях (например, `handle_suppliers_response`) может привести к сбою.
- `random.choice` может вызвать исключение, если `questions_list` пустое.
- Необходимо добавить обработку различных типов ошибок в коде, что позволит повысить устойчивость бота.
- Можно использовать `try...except` блоки для обработки исключений.


**Взаимосвязи с другими частями проекта:**
- `PsychologistTelgrambot` использует компоненты из `src` (например, `gs`, `TelegramBot`, `GoogleGenerativeAI`), демонстрируя зависимость от других частей проекта.
- `mexiron` - предполагается, что это часть проекта или внешний сервис.  Требуется дополнительная информация о его функциональности.