# <input code>

```python
## \file hypotez/src/utils/smtp.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: SMTP Email Interface

"""
MODE = 'dev'


""" This module provides functionality to send and receive emails using an SMTP or IMAP server.
It includes functions to send emails using SMTP and retrieve emails using IMAP.

Functions:
    - `send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool`
      Sends an email using the SMTP server specified in the `_connection` dictionary.  Returns `True` on success, `False` on failure.  Includes error logging.
    
    - `receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]`
      Retrieves emails from an IMAP server and returns them as a list of dictionaries.  Returns `None` on error. Includes error logging.


** Important Considerations for Security and Robustness **:

    - **_connection Dictionary:** Do *not* hardcode credentials in this file.  Move the `_connection` dictionary to environment variables (e.g., using `os.environ`). This is crucial for security.  Avoid storing passwords directly in source code.

    - **Error Handling:** The code includes robust error handling, logging exceptions with details (subject, body, etc.).  This is very helpful for debugging.

    - **Email Parsing:** The `receive` function handles various email formats gracefully, preventing potential issues.

    - **MIME Handling:**  The code correctly uses `MIMEText` for constructing the email message, crucial for sending basic text emails.


"""

import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from typing import List, Dict, Optional

from src.logger import logger

# --- Configuration ---
# DO NOT HARDCODE CREDENTIALS HERE!  Use environment variables instead.
_connection = {
    'server': os.environ.get('SMTP_SERVER', 'smtp.example.com'),
    'port': int(os.environ.get('SMTP_PORT', 587)),
    'user': os.environ.get('SMTP_USER'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'receiver': os.environ.get('SMTP_RECEIVER', 'one.last.bit@gmail.com')
}


def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """Sends an email.  Returns True if successful, False otherwise. Logs errors."""
    try:
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        smtp.ehlo()
        smtp.starttls()
        smtp.login(_connection['user'], _connection['password'])

        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = _connection['user']
        message["To"] = to

        smtp.sendmail(_connection['user'], to, message.as_string())
        smtp.quit()
        return True

    except Exception as ex:
        logger.error(f"Error sending email. Subject: {subject}. Body: {body}. Error: {ex}", exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """Retrieves emails. Returns a list of email dictionaries if successful, None otherwise. Logs errors."""
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(user, password)
        mail.select(folder)

        status, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        emails = []
        for email_id in email_ids:
            status, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            email_data = {
                'subject': msg['subject'],
                'from': msg['from'],
                'body': msg.get_payload(decode=True, _charset="utf-8").decode("utf-8", "ignore")  # Decode & handle potential errors
            }
            emails.append(email_data)

        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f"Error occurred while retrieving emails: {ex}", exc_info=True)
        return None
```

# <algorithm>

**Функция `send`:**

1. **Попытка подключения:** Пытается установить соединение с SMTP сервером, используя данные из `_connection`.
2. **Авторизация:** Выполняет авторизацию на сервере.
3. **Формирование сообщения:** Создает объект сообщения `MIMEText` с телом, темой и адресами.
4. **Отправка сообщения:** Отправляет сформированное сообщение по указанному адресу.
5. **Закрытие соединения:** Закрывает соединение с сервером.
6. **Обработка ошибок:** Обрабатывает любые ошибки, возникающие на всех этапах, и записывает их в лог.


**Функция `receive`:**

1. **Подключение к IMAP серверу:** Устанавливает соединение с IMAP сервером, используя предоставленные данные.
2. **Выбор папки:** Выбирает папку для получения почты.
3. **Поиск сообщений:** Ищет все сообщения в выбранной папке.
4. **Обработка каждого сообщения:** Для каждого сообщения:
   - Загружает полное сообщение.
   - Извлекает тему и отправителя.
   - Извлекает тело сообщения и декодирует его.
   - Добавляет извлечённые данные в список `emails`.
5. **Закрытие соединения:** Закрывает соединение с сервером.
6. **Обработка ошибок:** Обрабатывает любые ошибки, возникающие на всех этапах, и записывает их в лог.

# <mermaid>

```mermaid
graph LR
    subgraph SMTP Сервис
        A[send(subject, body, to)] --> B{Подключение к SMTP};
        B --> C{Авторизация};
        C --> D{Создание сообщения};
        D --> E{Отправка сообщения};
        E --> F{Закрытие соединения};
        F --> G[Возврат True/False];
    end
    subgraph IMAP Сервис
        H[receive(imap_server, user, password, folder)] --> I{Подключение к IMAP};
        I --> J{Выбор папки};
        J --> K{Поиск сообщений};
        K --> L{Обработка каждого сообщения};
        L --> M{Извлечение данных};
        M --> N{Добавление в список};
        N --> O{Закрытие соединения};
        O --> P[Возврат списка сообщений/None];
    end
    A --> B
    H --> I
    G -->|Error| logger
    P -->|Error| logger
```

# <explanation>

**Импорты:**

- `smtplib`:  Библиотека для работы с SMTP-серверами.
- `imaplib`: Библиотека для работы с IMAP-серверами.
- `email`: Библиотека для работы с объектами электронной почты.
- `os`: Библиотека для взаимодействия с операционной системой, в частности, для получения переменных окружения.
- `MIMEText`: Класс из библиотеки `email` для создания текстовых сообщений электронной почты.
- `typing`:  Для типизации данных (List, Dict, Optional).
- `src.logger`:  Логгер, вероятно, созданный в другом модуле проекта (`src`).  Связь: этот модуль используется для логирования ошибок и информации.


**Классы:**

- Нет значимых классов, только встроенные типы данных используются в функциях.

**Функции:**

- `send(subject, body, to)`: Отправляет электронное письмо.
    - `subject`, `body`, `to`: Строки, представляющие тему, тело и получателя сообщения.
    - Возвращает `True` при успешной отправке, `False` — в случае ошибки.
    - Использует данные из `_connection` для подключения к SMTP-серверу и отправки.  Важная особенность: использует `os.environ` для доступа к переменным окружения, что критически важно для безопасности.
- `receive(imap_server, user, password, folder)`: Получает электронные письма из почтового ящика.
    - `imap_server`, `user`, `password`: Необходимые данные для подключения к IMAP-серверу.
    - `folder`:  Имя папки для получения сообщений. По умолчанию 'inbox'.
    - Возвращает список словарей, каждый из которых представляет собой электронное письмо с темой, отправителем и телом; возвращает `None` при ошибке.
    - Обрабатывает полученные сообщения, декодирует тела и добавляет в список.


**Переменные:**

- `_connection`: Словарь, содержащий настройки подключения к SMTP-серверу (сервер, порт, пользователь, пароль, получатель).  **Критически важно**: эти данные извлекаются из переменных окружения (`os.environ`), что повышает безопасность.


**Возможные ошибки и улучшения:**

- **Безопасность:** Хотя переменные окружения используются,  рекомендуется использовать более надёжные методы хранения паролей, например, секретные хранилища.
- **Обработка кодировки:**  В функции `receive` используется `decode("utf-8", "ignore")`,  что помогает обрабатывать различные кодировки сообщений. Однако, если проблемы с кодировкой остаются, стоит использовать более специализированные методы обработки.
- **Обработка больших вложений:**  Функция `receive` не обрабатывает сообщения с большими вложениями. При их обработке лучше использовать специализированные методы, например, получать и обрабатывать вложения отдельно.
- **Улучшенный логгер:**  Можно добавить более подробную информацию в сообщения логгера, например, ID сообщения, время отправки/получения.
- **Проверка валидности входящих данных:** Функция `send` и `receive` принимают параметры без проверки на корректность, например, проверка типов данных, пустых строк.


**Цепочка взаимосвязей:**

Этот модуль (`hypotez/src/utils/smtp.py`) зависит от модуля `logger`, находящегося в `src.logger`.  В свою очередь,  код в этом файле `smtp.py` зависит от настроек, хранящихся в переменных окружения.  Функции `send` и `receive` взаимодействуют с SMTP- и IMAP-серверами.  Они могут быть использованы другими частями приложения для отправки и получения электронной почты.