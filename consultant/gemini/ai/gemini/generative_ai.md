```python
## \file hypotez/src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.ai.gemini """
"""Google generative AI integration."""

import time
import json
from pathlib import Path
from datetime import datetime
import base64
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict
import google.generativeai as genai
from src.logger import logger
from __init__ import gs
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI(BaseModel):
    """Class to interact with Google Generative AI models."""
    model_config = {
        "arbitrary_types_allowed": True
    }

    MODELS: List[str] = Field(default_factory=lambda: [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ])

    api_key: str = Field(default='')
    model_name: str = Field(default="gemini-1.5-flash-8b")
    generation_config: Dict = Field(default_factory=lambda: {"response_mime_type": "text/plain"})
    mode: str = Field(default='debug')
    
    dialogue_log_path: Optional[Path] = None
    dialogue_txt_path: Optional[Path] = None
    history_dir: Path = Field(default = gs.path.google_drive / 'AI' / 'history' )
    history_txt_file: Optional[Path] = None
    history_json_file: Optional[Path] = None
    model: Optional[genai.GenerativeModel] = None
    system_instruction: Optional[str] = None 

    def __init__(self, 
                 api_key: str, 
                 model_name: Optional[str] = None, 
                 generation_config: Optional[Dict] = None, 
                 system_instruction: Optional[str] = None, 
                 **kwargs):
        """Initialize the GoogleGenerativeAI model with additional settings."""
        super().__init__(**kwargs)  # Инициализация Pydantic полей

        # Проверка корректности api_key
        if not api_key:
          raise ValueError("API key is required.")

        self.dialogue_log_path = gs.path.google_drive / 'AI' / 'log'
        self.dialogue_txt_path = self.dialogue_log_path / f"gemini_{gs.now}.txt"
        self.history_dir.mkdir(parents=True, exist_ok=True)  # Создать директорию, если не существует
        self.history_txt_file = self.history_dir / f"gemini_{gs.now}.txt"
        self.history_json_file = self.history_dir / f"gemini_{gs.now}.json"

        self.api_key = api_key # Необходимо инициализировать
        self.model_name = model_name or "gemini-1.5-flash-8b"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction

        # Настройка модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name = self.model_name,
            generation_config = self.generation_config,
            system_instruction = self.system_instruction       
        )


    def _save_dialogue(self, dialogue: list):
        """Save dialogue to both txt and json files with size management."""
        save_text_file(json.dumps(dialogue, indent=2), self.history_json_file, mode='a')

    def ask(self, q: str, attempts: int = 3) -> Optional[str]:
        # ... (rest of the ask method is the same)

def chat():
    # ... (rest of the chat function is the same)

if __name__ == "__main__":
    try:
        chat()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

**Изменения и объяснения:**

* **Проверка `api_key`:** Добавлена важная проверка, что `api_key` не пустая строка.  Без неё код рухнет, если `api_key` не будет задана.  Добавлен `ValueError`, который поднимается в этом случае. Это критично для надежности.

* **`history_dir` создание директории:**  Добавлена строка `self.history_dir.mkdir(parents=True, exist_ok=True)`.  Это создает директорию `history` и все родительские каталоги, если они не существуют. Без этого может быть ошибка `FileNotFoundError`.

* **Обработка исключений в `if __name__ == "__main__":`:**
    Добавлен блок `try...except` вокруг вызова `chat()`.  Это предотвращает остановку программы при возникновении любой ошибки (кроме `ValueError`, специально обработанной).


* **Форматирование JSON в `_save_dialogue`:** Используется `json.dumps(dialogue, indent=2)` для сохранения диалога в `history_json_file` в формате JSON с отступами. Это значительно улучшает читаемость файла.



**Почему важно эти изменения?**

* **Надежность:** Проверка `api_key` предотвращает ошибки.
* **Устойчивость:** Обработка исключений в `if __name__ == "__main__":` делает программу более устойчивой к различным ошибкам.
* **Пользовательский опыт:**  Программа не аварийно завершается, а выдаёт понятную информацию, что случилось.

**Как использовать:**

1. Замените `"your_api_key"` в функции `chat` своим API ключом Google Generative AI.
2. Убедитесь, что у вас установлены необходимые библиотеки (`google-generative-ai`, `pydantic`, ...).
3. Запустите скрипт.

Теперь программа будет более надёжной и устойчивой к ошибкам.


```