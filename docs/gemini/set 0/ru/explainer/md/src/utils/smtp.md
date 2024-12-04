# <input code>

```python
## \file hypotez/src/utils/smtp.py
# -*- coding: utf-8 -*-\
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

**Алгоритм работы кода:**

1. **Инициализация:**
    * Загружает необходимые модули (smtplib, imaplib, email, os, MIMEText, typing).
    * Импортирует `logger` из `src.logger`.
    * Загружает настройки из переменной окружения `_connection`.  **Важно**:  Вместо хардкодинга, используется `os.environ`, что делает код безопаснее.
    * **Пример:** `_connection['server']` получает значение из переменной окружения `SMTP_SERVER`, по умолчанию `smtp.example.com`.

2. **Функция `send`:**
    * Создаёт соединение с SMTP сервером (`smtplib.SMTP`).
    * Проверяет соединение (`smtp.ehlo`, `smtp.starttls`).
    * Проводит авторизацию (`smtp.login`).
    * Создаёт объект `MIMEText` для письма.
    * Устанавливает заголовок (`Subject`, `From`, `To`).
    * Отправляет письмо (`smtp.sendmail`).
    * Закрывает соединение (`smtp.quit`).
    * **Пример:** `send(subject='Test', body='Hello', to='recipient@example.com')`. Возвращает `True` при успехе, `False` при ошибке.

3. **Функция `receive`:**
    * Создаёт соединение с IMAP сервером (`imaplib.IMAP4_SSL`).
    * Проводит авторизацию (`mail.login`).
    * Выбирает папку ("inbox") (`mail.select`).
    * Получает список ID писем (`mail.search`).
    * Для каждого письма:
        * Получает сырые данные письма (`mail.fetch`).
        * Парсит данные письма (`email.message_from_bytes`).
        * Извлекает заголовок (`subject`, `from`) и тело письма (`body`).  **Обратите внимание на обработку кодировки (`decode`).**
        * Добавляет данные в список `emails`.
    * Закрывает соединение (`mail.close`, `mail.logout`).
    * **Пример:** `receive(imap_server='imap.example.com', user='user@example.com', password='password', folder='inbox')`. Возвращает список словарей с информацией о письмах или `None` в случае ошибки.

**Передача данных**: Настройки (`_connection`) передаются как константы в функции.  Функция `send` принимает параметры (`subject`, `body`, `to`) и возвращает результат. Функция `receive` принимает параметры (`imap_server`, `user`, `password`, `folder`) и возвращает список словарей.


# <mermaid>

```mermaid
graph TD
    A[utils.smtp] --> B{Import Modules};
    B --> C[send Function];
    B --> D[receive Function];
    C --> E{SMTP Connection};
    E --> F{Authentication};
    F --> G{Email Creation};
    G --> H{Email Sending};
    H --> I[Success/Error];
    D --> J{IMAP Connection};
    J --> K{Authentication};
    K --> L{Select Inbox};
    L --> M{Search Emails};
    M --> N{Fetch Email};
    N --> O{Parse Email};
    O --> P{Extract Data};
    P --> Q{Append to List};
    Q --> R{Close Connection};
    I -- Success --> S[Return True];
    I -- Error --> T[Log Error, Return False];
    R -- Success --> U[Return Emails List];
    R -- Error --> V[Log Error, Return None];
    subgraph src.logger
        T --> W[Logging];
    end
    subgraph Email Modules
        G --> AA[MIMEText];
        O --> BB[email.message_from_bytes]
        O --> CC[decode];

        P -- Extract Subject --> DD[subject];
        P -- Extract From --> EE[from];
        P -- Extract Body --> FF[body];

    end

    style AA fill:#f9f,stroke:#333,stroke-width:2px
```

# <explanation>

**Импорты:**

* `smtplib`, `imaplib`, `email`, `os`: Стандартные библиотеки Python для работы с SMTP и IMAP протоколами.
* `MIMEText`:  Модуль для создания текстовых сообщений email.
* `typing`: Для указания типов данных (List, Dict, Optional).
* `src.logger`: Модуль для ведения логов. Предполагается, что этот модуль находится в директории `hypotez/src/logger.py` и отвечает за запись ошибок и сообщений в лог-файл.

**Классы:**

Нет явных классов. Модуль содержит функции для отправки и получения электронных писем.

**Функции:**

* **`send(subject, body, to)`:**
    * **Аргументы:** `subject`, `body` (строки) - заголовок и текст письма; `to` (строка) - адрес получателя. Имеют значения по умолчанию для удобства.
    * **Возвращаемое значение:** `bool` (True - успех, False - ошибка).
    * **Функциональность:** Отправляет письмо на указанный адрес. Обрабатывает все возможные исключения и пишет их в лог.  Критически важно использование `os.environ` для хранения данных авторизации (e-mail, пароль), вместо хардкодинга.
* **`receive(imap_server, user, password, folder)`:**
    * **Аргументы:** `imap_server`, `user`, `password` (строки) - адрес IMAP сервера, логин и пароль; `folder` (строка) - папка для поиска писем (по умолчанию "inbox").
    * **Возвращаемое значение:** `Optional[List[Dict[str, str]]]` - список словарей с информацией о письмах, либо `None` при ошибке.
    * **Функциональность:** Получает список писем из указанной папки на IMAP сервере. Обрабатывает ошибки и пишет информацию в лог.  Правильно обрабатывает кодировку тела письма (`decode`).

**Переменные:**

* **`_connection`:** Словарь с настройками для SMTP.  Ключевой аспект - использование `os.environ` для безопасного хранения учетных данных.

**Возможные ошибки и улучшения:**

* **Безопасность:**  Прежде чем использовать этот код, необходимо настроить переменные окружения (`SMTP_SERVER`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_RECEIVER`) в соответствии с вашим SMTP сервером.
* **Дополнения:**  Можно добавить обработку различных типов MIME-сообщений (не только текст), обработку вложений и другие возможности.


**Взаимосвязи с другими частями проекта:**

Функции `send` и `receive` зависят от `src.logger` для записи ошибок и сообщений.  Логирование позволяет отследить успешность отправки/получения и выявлять проблемы.