# Анализ кода модуля `smtp.py`

**Качество кода: 7/10**

*   **Плюсы**
    *   Код содержит docstring для модуля, поясняющий его назначение.
    *   Используется логгер для обработки ошибок, что является хорошей практикой.
    *   Есть разделение на функции отправки и получения почты, что делает код более модульным.
    *   Код обрабатывает ошибки и логирует их, что полезно для отладки.
    *   Используются переменные окружения для хранения учетных данных, что является более безопасным, чем жесткое кодирование.
*   **Минусы**
    *   Docstring модуля не соответствует стандарту RST.
    *   Docstring для функций не полные (нет описания параметров и возвращаемого значения).
    *   В комментариях после `#` отсутствует подробное объяснение блока кода.
    *   Используются стандартные `try-except` блоки, хотя можно было бы использовать логгер для обработки исключений более лаконично.
    *   Не используется `j_loads` или `j_loads_ns` для чтения каких-либо файлов.
    *   В коде есть константа `MODE`, но не используется.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Переписать docstring модуля в формате RST.
    *   Добавить docstring к каждой функции, описывая параметры и возвращаемые значения.
    *   Использовать reStructuredText (RST) для всех комментариев.
2.  **Логирование:**
    *   Упростить `try-except` блоки, используя `logger.error` для обработки ошибок.
3.  **Конфигурация:**
    *   Убрать константу `MODE`, так как она не используется.
4.  **Комментарии:**
    *   Добавить комментарии с подробным объяснением для каждого блока кода.
5.  **Импорты:**
    *   Проверить и добавить отсутствующие импорты, если таковые есть.
6.  **Безопасность:**
    *   Убедиться, что все учетные данные и другая важная информация берутся из переменных окружения.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для отправки и получения электронной почты через SMTP и IMAP
=========================================================================================

Этот модуль предоставляет функциональность для отправки и получения электронной почты
с использованием SMTP и IMAP серверов.

.. note::
    Важно! Не храните учетные данные в коде. Используйте переменные окружения.

Пример использования
--------------------

.. code-block:: python

    from src.utils import smtp

    # Отправка письма
    smtp.send(subject='Тема письма', body='Текст письма', to='recipient@example.com')

    # Получение писем
    emails = smtp.receive(imap_server='imap.example.com', user='your_user', password='your_password')
    if emails:
        for email in emails:
            print(f"Subject: {email['subject']}")
            print(f"From: {email['from']}")
            print(f"Body: {email['body']}")
"""

import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from typing import List, Dict, Optional

from src.logger.logger import logger

# --- Конфигурация ---
# Получение настроек подключения из переменных окружения
_connection = {
    'server': os.environ.get('SMTP_SERVER', 'smtp.example.com'),
    'port': int(os.environ.get('SMTP_PORT', 587)),
    'user': os.environ.get('SMTP_USER'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'receiver': os.environ.get('SMTP_RECEIVER', 'one.last.bit@gmail.com')
}

def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """
    Отправляет электронное письмо.

    :param subject: Тема письма.
    :param body: Тело письма.
    :param to: Адрес получателя.
    :return: True, если письмо успешно отправлено, False в противном случае.
    """
    try:
        # Код устанавливает соединение с SMTP сервером
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        smtp.ehlo()
        # Код запускает TLS шифрование
        smtp.starttls()
        # Код выполняет вход в почтовый аккаунт
        smtp.login(_connection['user'], _connection['password'])

        # Код создает сообщение MIME
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = _connection['user']
        message["To"] = to

        # Код отправляет письмо
        smtp.sendmail(_connection['user'], to, message.as_string())
        smtp.quit()
        return True

    except Exception as ex:
        # Код логирует ошибку отправки письма
        logger.error(f"Ошибка отправки email. Тема: {subject}. Тело: {body}. Ошибка: {ex}", exc_info=True)
        return False

def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """
    Получает электронные письма с IMAP сервера.

    :param imap_server: Адрес IMAP сервера.
    :param user: Имя пользователя.
    :param password: Пароль пользователя.
    :param folder: Папка для чтения писем (по умолчанию 'inbox').
    :return: Список словарей с данными писем, или None в случае ошибки.
    """
    try:
         # Код устанавливает соединение с IMAP сервером
        mail = imaplib.IMAP4_SSL(imap_server)
        # Код выполняет вход в почтовый аккаунт
        mail.login(user, password)
        # Код выбирает папку
        mail.select(folder)

        # Код ищет все письма
        status, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        emails = []
        # Код обрабатывает каждое найденное письмо
        for email_id in email_ids:
            # Код извлекает письмо по ID
            status, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            # Код преобразует байты письма в объект Message
            msg = email.message_from_bytes(raw_email)

            # Код извлекает данные письма
            email_data = {
                'subject': msg['subject'],
                'from': msg['from'],
                # Код декодирует тело письма, обрабатывая ошибки
                'body': msg.get_payload(decode=True, _charset="utf-8").decode("utf-8", "ignore")
            }
            emails.append(email_data)

        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        # Код логирует ошибку получения писем
        logger.error(f"Произошла ошибка при получении писем: {ex}", exc_info=True)
        return None
```