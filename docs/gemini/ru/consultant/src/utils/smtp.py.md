# Анализ кода модуля `smtp.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на функции `send` и `receive`, что облегчает его понимание и использование.
    - Используется `logger` для логирования ошибок, что помогает в отладке и мониторинге.
    - Присутствует обработка исключений с детальным логированием (сообщение об ошибке и traceback), что позволяет более точно определять проблемы.
    - В `receive` выполняется корректное декодирование тела письма с обработкой возможных ошибок кодирования.
    - Добавлены комментарии в формате `RST`  к модулю и функциям.
-  Минусы
    - В `_connection` используются `os.environ`, но не хватает проверки на наличие переменных окружения, что может привести к ошибкам.
    - Некоторые переменные, такие как `receiver` в `_connection`, могут быть не нужны для работы функции send и использоваться только как значения по умолчанию.

**Рекомендации по улучшению**
1.  Добавить проверку наличия переменных окружения (`SMTP_SERVER`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`) в `_connection`, чтобы избежать ошибок при их отсутствии.
2.  Удалить переменную `receiver` из `_connection`, так как она не используется напрямую.
3.  В функциях `send` и `receive` можно добавить более конкретные сообщения об ошибках, например, указать, что не удалось подключиться к SMTP или IMAP серверу.
4.  Убрать явное использование try-except и перенести логику с обработкой ошибок в декоратор
5.  Вместо использования стандартного блока try-except, перенести логику обработки ошибок в декоратор

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
.. module:: src.utils
    :platform: Windows, Unix
    :synopsis: SMTP Email Interface

Этот модуль предоставляет функциональность для отправки и получения электронных писем
с использованием SMTP или IMAP сервера. Включает функции для отправки писем через SMTP
и получения через IMAP.

Функции:
    - `send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool`
      Отправляет электронное письмо, используя SMTP сервер, указанный в словаре `_connection`.
      Возвращает `True` при успехе, `False` при неудаче. Включает логирование ошибок.

    - `receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]`
      Извлекает электронные письма с IMAP сервера и возвращает их в виде списка словарей.
      Возвращает `None` при ошибке. Включает логирование ошибок.

**Важные соображения для безопасности и надежности**:

    - **Словарь _connection:** Не жестко кодируйте учетные данные в этом файле. Переместите
      словарь `_connection` в переменные окружения (например, с помощью `os.environ`).
      Это крайне важно для безопасности. Избегайте хранения паролей непосредственно в исходном коде.

    - **Обработка ошибок:** Код включает надежную обработку ошибок, логирование исключений
      с подробностями (тема, тело и т. д.). Это очень полезно для отладки.

    - **Разбор электронной почты:** Функция `receive` корректно обрабатывает различные форматы
      электронной почты, предотвращая потенциальные проблемы.

    - **Обработка MIME:** Код правильно использует `MIMEText` для создания сообщения электронной
      почты, что крайне важно для отправки обычных текстовых писем.
"""
import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from typing import List, Dict, Optional
from functools import wraps

from src.logger.logger import logger

# --- Configuration ---
# DO NOT HARDCODE CREDENTIALS HERE!  Use environment variables instead.
_connection = {
    'server': os.environ.get('SMTP_SERVER'),
    'port': os.environ.get('SMTP_PORT'),
    'user': os.environ.get('SMTP_USER'),
    'password': os.environ.get('SMTP_PASSWORD'),
}


def handle_email_errors(func):
    """
    Декоратор для обработки ошибок в функциях отправки и получения email.
    Логирует исключения и возвращает False или None в зависимости от функции.

    :param func: Декорируемая функция.
    :return: Обернутая функция.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            log_message = f"Ошибка при выполнении функции {func.__name__}: {ex}"
            logger.error(log_message, exc_info=True)
            return False if func.__name__ == 'send' else None
    return wrapper


@handle_email_errors
def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """
    Отправляет электронное письмо.

    :param subject: Тема письма.
    :param body: Тело письма.
    :param to: Адрес получателя.
    :return: `True`, если письмо отправлено успешно, `False` в противном случае.
    """
    # Проверка наличия необходимых параметров
    if not all(_connection.get(key) for key in ['server', 'port', 'user', 'password']):
        logger.error('Отсутствуют необходимые параметры для SMTP подключения в переменных окружения')
        return False
    #  Код устанавливает соединение с SMTP сервером
    smtp = smtplib.SMTP(_connection['server'], int(_connection['port']))
    smtp.ehlo()
    smtp.starttls()
    #  Код выполняет вход в SMTP сервер
    smtp.login(_connection['user'], _connection['password'])

    # Код создает MIME сообщение
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = _connection['user']
    message["To"] = to

    # Код отправляет сообщение
    smtp.sendmail(_connection['user'], to, message.as_string())
    smtp.quit()
    return True


@handle_email_errors
def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """
    Извлекает электронные письма с IMAP сервера.

    :param imap_server: Адрес IMAP сервера.
    :param user: Имя пользователя IMAP.
    :param password: Пароль IMAP.
    :param folder: Папка для чтения писем.
    :return: Список словарей с данными писем (тема, отправитель, тело), или `None` в случае ошибки.
    """
    # Код устанавливает соединение с IMAP сервером
    mail = imaplib.IMAP4_SSL(imap_server)
    # Код выполняет вход в IMAP сервер
    mail.login(user, password)
    mail.select(folder)

    # Код выполняет поиск всех писем
    status, data = mail.search(None, 'ALL')
    email_ids = data[0].split()

    emails = []
    for email_id in email_ids:
        # Код извлекает письмо по ID
        status, data = mail.fetch(email_id, '(RFC822)')
        raw_email = data[0][1]
        # Код преобразует полученное письмо в объект
        msg = email.message_from_bytes(raw_email)

        email_data = {
            'subject': msg['subject'],
            'from': msg['from'],
            'body': msg.get_payload(decode=True, _charset="utf-8").decode("utf-8", "ignore")
        }
        emails.append(email_data)

    mail.close()
    mail.logout()
    return emails
```