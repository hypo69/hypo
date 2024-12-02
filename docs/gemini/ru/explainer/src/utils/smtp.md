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
        # Create SMTP connection
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

**Функция send:**

1. **Получение данных:** Получает значения `subject`, `body`, `to`
2. **Обработка исключений:** Блок `try...except` обрабатывает возможные ошибки во время отправки.
3. **Создание соединения:** Создаёт соединение с SMTP сервером, используя данные из словаря `_connection`.
4. **Аутентификация:** Выполняет аутентификацию с использованием логина и пароля.
5. **Формирование письма:** Создаёт объект `MIMEText` для тела письма и устанавливает заголовок, отправителя и получателя.
6. **Отправка письма:** Использует `smtp.sendmail` для отправки письма.
7. **Закрытие соединения:** Закрывает соединение с SMTP сервером.
8. **Возврат результата:** Возвращает `True` если отправка прошла успешно, `False` в противном случае.


**Функция receive:**

1. **Получение данных:** Получает значения `imap_server`, `user`, `password`, `folder`.
2. **Обработка исключений:** Блок `try...except` обрабатывает возможные ошибки во время получения.
3. **Создание соединения:** Создаёт соединение с IMAP сервером.
4. **Аутентификация:** Выполняет аутентификацию с использованием логина и пароля.
5. **Выбор папки:** Выбирает папку для получения писем.
6. **Получение списка писем:** Ищет все письма в указанной папке.
7. **Обработка каждого письма:** Цикл обрабатывает каждое письмо в списке.
   - **Чтение письма:** Читает содержимое письма.
   - **Парсинг данных:** Извлекает `subject`, `from`, `body` из письма.
   - **Добавление в список:** Добавляет полученные данные в список `emails`.
8. **Закрытие соединения:** Закрывает соединение с IMAP сервером.
9. **Возврат результата:** Возвращает список `emails` или `None` при ошибке.

# <mermaid>

```mermaid
graph TD
    A[main] --> B{send(subject, body, to)};
    B -- success --> C[smtp.sendmail];
    B -- error --> D[log error];
    C --> E[return True];
    D --> E;

    A --> F{receive(imap_server, user, password, folder)};
    F -- success --> G[imap.search];
    F -- error --> D;
    G --> H[loop through emails];
    H --> I[imap.fetch];
    I --> J[email.message_from_bytes];
    J --> K[extract subject, from, body];
    K --> L[append to emails];
    L --> H;
    H --> M[imap.close, imap.logout];
    M --> N[return emails];

    subgraph Libraries
        style G fill:#f9f,stroke:#333,stroke-width:2px;
        style I fill:#f9f,stroke:#333,stroke-width:2px;

        smtplib --> B;
        imaplib --> F;
        email --> J;
        logger --> D;
        os --> B,F;

        subgraph src
        logger --> A;
    end
    end
```

# <explanation>

**Импорты:**

- `smtplib`: Модуль для работы с SMTP сервером.
- `imaplib`: Модуль для работы с IMAP сервером.
- `email`: Модуль для работы с электронными письмами.
- `os`: Модуль для взаимодействия с операционной системой, используется для получения переменных окружения.
- `email.mime.text`: Подмодуль для создания текстовых писем в формате MIME.
- `typing`: Модуль для работы с типизированными данными, `List`, `Dict`, `Optional`.
- `src.logger`: Логгер, вероятно, определён в другом модуле проекта (`src.logger`).  Связь с `src` указывает на иерархическую организацию проекта.


**Классы:**

- Нет явных пользовательских классов.

**Функции:**

- `send(subject, body, to)`: Отправляет электронное письмо. Принимает тему, тело и адресата, возвращает `True` при успехе, `False` при ошибке.  Логирует ошибки с помощью `logger`. Важно: использует переменные окружения для хранения данных аутентификации, предотвращая их хранение в коде.
- `receive(imap_server, user, password, folder)`: Получает электронные письма. Принимает данные сервера, пользователя и пароль, а также папку (по умолчанию "inbox"). Возвращает список словарей с данными о письмах или `None` при ошибке.  Аналогично `send`, использует логгирование и обработку ошибок.


**Переменные:**

- `_connection`: Словарь для хранения параметров подключения к SMTP серверу, включает в себя имя сервера, порт, пользователя и пароль (достаются из переменных окружения). Это очень важно для безопасности, предотвращая хранение паролей непосредственно в коде.
- `MODE`: Символьная переменная, вероятно, используемая для обозначения режима работы (например, "dev" или "prod").

**Возможные ошибки и улучшения:**

- **Безопасность:** Обязательно используйте переменные окружения для хранения паролей и других конфиденциальных данных.
- **Обработка ошибок:** Обработка исключений в обеих функциях правильная.
- **Типизация:** Правильное использование `typing` улучшает читаемость и поддерживаемость кода.
- **Детализация логов:**  В логах можно добавить больше контекста о полученной ошибке. Например, при ошибке отправки письма в лог можно добавить информацию об адресате.


**Взаимосвязь с другими частями проекта:**

Функция `send` и `receive` использует `src.logger` для записи сообщений об ошибках. Это указывает на то, что `logger` определён в другом файле, скорее всего, в модуле `logger` в папке `src`.  Функции взаимодействуют с внешними SMTP и IMAP серверами.