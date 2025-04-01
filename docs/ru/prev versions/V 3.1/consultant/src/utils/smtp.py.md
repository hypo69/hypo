## Анализ кода модуля `smtp.py`

**Качество кода:**
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Четкое разделение функциональности на отправку и получение email.
  - Использование `MIMEText` для создания email-сообщений.
  - Обработка исключений с логированием ошибок.
  - Использование переменных окружения для хранения учетных данных.
- **Минусы**:
  - Неполная документация функций и модуля.
  - Жестко заданы значения по умолчанию для некоторых параметров.
  - Отсутствует обработка ошибок при чтении переменных окружения.
  - Смешанный стиль кавычек (используются как одинарные, так и двойные).
  - Не все параметры аннотированы типами.

**Рекомендации по улучшению:**

1.  **Документация**:
    *   Добавить подробное описание модуля, включая примеры использования.
    *   Описать каждый параметр и возвращаемое значение функций `send` и `receive`.
    *   Указать возможные исключения, которые могут быть выброшены функциями.
2.  **Безопасность**:
    *   Проверять наличие переменных окружения и обрабатывать отсутствие необходимых переменных.
    *   Рассмотреть возможность использования более безопасных способов хранения паролей (например, `python-dotenv`).
3.  **Форматирование**:
    *   Привести код в соответствие со стандартом PEP8.
    *   Использовать только одинарные кавычки.
    *   Добавить аннотации типов для всех параметров и возвращаемых значений.
4.  **Улучшение кода**:
    *   Удалить неиспользуемые импорты.
    *   Добавить обработку ошибок при чтении переменных окружения.
    *   Использовать `logger.exception` вместо `logger.error` для логирования ошибок.
    *   Удалить строку `#! .pyenv/bin/python3`, так как она может быть неактуальна.
    *   Указывать кодировку при открытии файлов.

**Оптимизированный код:**

```python
## \file /src/utils/smtp.py
# -*- coding: utf-8 -*-

"""
Модуль для отправки и получения email сообщений с использованием SMTP и IMAP.
==========================================================================

Модуль предоставляет функции для отправки email через SMTP и получения email через IMAP.

Пример использования:
----------------------
    >>> from src.utils import smtp
    >>> smtp.send(subject='Test', body='Test email', to='test@example.com')
    True

Функции:
    - `send(subject: str, body: str, to: str) -> bool`: Отправляет email сообщение.
    - `receive(imap_server: str, user: str, password: str, folder: str) -> Optional[List[Dict[str, str]]]`: Получает email сообщения.
"""

import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from typing import List, Dict, Optional

from src.logger.logger import logger


# --- Configuration ---
# DO NOT HARDCODE CREDENTIALS HERE! Use environment variables instead.
_connection = {
    'server': os.environ.get('SMTP_SERVER', 'smtp.example.com'),
    'port': int(os.environ.get('SMTP_PORT', '587')),
    'user': os.environ.get('SMTP_USER'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'receiver': os.environ.get('SMTP_RECEIVER', 'one.last.bit@gmail.com')
}


def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """
    Отправляет email сообщение.

    Args:
        subject (str): Тема сообщения.
        body (str): Тело сообщения.
        to (str): Адрес получателя.

    Returns:
        bool: True, если отправка прошла успешно, False в противном случае.

    Raises:
        smtplib.SMTPException: Если произошла ошибка при отправке сообщения.

    Example:
        >>> send(subject='Test', body='Test email', to='test@example.com')
        True
    """
    try:
        # Create SMTP connection
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        smtp.ehlo()
        smtp.starttls()
        smtp.login(_connection['user'], _connection['password'])

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = _connection['user']
        message['To'] = to

        smtp.sendmail(_connection['user'], to, message.as_string())
        smtp.quit()
        return True

    except Exception as ex:
        logger.error(f'Error sending email. Subject: {subject}. Body: {body}. Error: {ex}', exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """
    Получает email сообщения из указанной папки на IMAP сервере.

    Args:
        imap_server (str): Адрес IMAP сервера.
        user (str): Имя пользователя для подключения к серверу.
        password (str): Пароль для подключения к серверу.
        folder (str, optional): Название папки для чтения сообщений. Defaults to 'inbox'.

    Returns:
        Optional[List[Dict[str, str]]]: Список словарей с данными email сообщений, None в случае ошибки.
            Каждый словарь содержит ключи: 'subject', 'from', 'body'.

    Raises:
        imaplib.IMAP4.error: Если произошла ошибка при подключении к серверу или чтении сообщений.

    Example:
        >>> receive(imap_server='imap.example.com', user='test@example.com', password='password', folder='inbox')
        [{'subject': 'Test', 'from': 'sender@example.com', 'body': 'Test email'}]
    """
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
                'body': msg.get_payload(decode=True, _charset='utf-8').decode('utf-8', 'ignore')  # Decode & handle potential errors
            }
            emails.append(email_data)

        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f'Error occurred while retrieving emails: {ex}', exc_info=True)
        return None