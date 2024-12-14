# Анализ кода модуля smtp.py

**Качество кода**
7
-  Плюсы
    - Код предоставляет функциональность для отправки и получения электронной почты с использованием SMTP и IMAP.
    - Используется `MIMEText` для создания email-сообщений.
    - Присутствует логирование ошибок с помощью `logger.error`, что помогает в отладке.
    - Параметры подключения к SMTP-серверу берутся из переменных окружения, что способствует безопасности.
    - Код обрабатывает исключения и корректно завершает соединения.
    - Имеется docstring для модуля и функций.
-  Минусы
    - В начале файла присутствуют shebang, которые обычно не нужны для модулей.
    - Не все комментарии соответствуют reStructuredText.
    -  Не все переменные и функции имеют docstring в формате RST.
    - Желательно добавить docstring для переменных модуля.
    -  В функции receive, не обрабатывается ситуация, когда email может быть multipart.

**Рекомендации по улучшению**

1. **Удалить shebang:** Удалить строки `#! venv/Scripts/python.exe` и `#! venv/bin/python/python3.12` так как они избыточны для модуля.
2. **Документация в reStructuredText:** Все комментарии и docstring должны быть в формате reStructuredText (RST).
3. **Обработка multipart email:** В функции `receive` необходимо добавить обработку multipart email.
4.  **Улучшить docstring переменных модуля**: Добавить документацию в формате RST для переменных модуля.
5. **Улучшить обработку ошибок**: В функции `receive` добавить более детальное логирование, например, id письма в случае ошибки.
6. **Улучшить форматирование**: Использовать f-строки для форматирования строк с логами.

**Оптимизированный код**

```python
"""
Модуль для работы с SMTP и IMAP
=========================================================================================

Этот модуль предоставляет функциональность для отправки и получения электронной почты с использованием
SMTP и IMAP серверов.

:platform: Windows, Unix
:synopsis: SMTP Email Interface

Пример использования
--------------------

.. code-block:: python

    from src.utils.smtp import send, receive

    # Отправка письма
    if send(subject='Тестовое письмо', body='Это тело тестового письма.', to='recipient@example.com'):
        print('Письмо успешно отправлено')
    else:
        print('Ошибка отправки письма')

    # Получение писем
    emails = receive(imap_server='imap.example.com', user='user', password='password', folder='inbox')
    if emails:
       for email in emails:
           print(f'От: {email["from"]}, Тема: {email["subject"]}')
           print(f'Содержание: {email["body"]}')
    else:
        print('Не удалось получить письма')
"""
import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #  Импорт для работы с multipart
from typing import List, Dict, Optional

from src.logger.logger import logger

#: Режим работы модуля
MODE = 'dev'

#: Словарь для хранения параметров подключения
#:
#: .. note::
#:
#:     Не храните учетные данные напрямую в коде. Используйте переменные окружения.
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
    :type subject: str
    :param body: Текст письма.
    :type body: str
    :param to: Адрес получателя.
    :type to: str
    :return: Возвращает True, если письмо отправлено успешно, иначе False.
    :rtype: bool
    """
    try:
        # Создание SMTP подключения
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
        logger.error(f"Ошибка отправки письма. Тема: {subject}. Текст: {body}. Ошибка: {ex}", exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """
    Получает электронные письма с IMAP сервера.

    :param imap_server: Адрес IMAP сервера.
    :type imap_server: str
    :param user: Имя пользователя для IMAP сервера.
    :type user: str
    :param password: Пароль для IMAP сервера.
    :type password: str
    :param folder: Папка для поиска писем.
    :type folder: str
    :return: Возвращает список словарей с данными писем, или None в случае ошибки.
    :rtype: Optional[List[Dict[str, str]]]
    """
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(user, password)
        mail.select(folder)

        status, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        emails = []
        for email_id in email_ids:
            try: #  Добавлена обработка ошибок для каждого письма
                status, data = mail.fetch(email_id, '(RFC822)')
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                body = ''
                if msg.is_multipart():
                  for part in msg.walk():
                      content_type = part.get_content_type()
                      content_disposition = str(part.get("Content-Disposition"))

                      if content_type == "text/plain" and "attachment" not in content_disposition:
                        try:
                             body = part.get_payload(decode=True).decode("utf-8", "ignore")
                        except Exception as ex:
                           logger.error(f"Ошибка декодирования тела письма {email_id}: {ex}", exc_info=True)
                           continue

                elif msg.get_content_type() == "text/plain":
                  try:
                    body = msg.get_payload(decode=True).decode("utf-8", "ignore")
                  except Exception as ex:
                    logger.error(f"Ошибка декодирования тела письма {email_id}: {ex}", exc_info=True)

                email_data = {
                    'subject': msg['subject'],
                    'from': msg['from'],
                    'body': body
                }
                emails.append(email_data)
            except Exception as ex:
                logger.error(f"Ошибка при обработке письма {email_id}: {ex}", exc_info=True)
                continue

        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f"Ошибка при получении писем: {ex}", exc_info=True)
        return None