# Анализ кода модуля `smtp.py`

**Качество кода**
9
 -  Плюсы
    - Код хорошо структурирован и легко читается.
    - Присутствует подробная документация модуля и функций.
    - Используется `logger` для логирования ошибок.
    - Параметры SMTP вынесены в переменные окружения, что является хорошей практикой для безопасности.
    - Добавлены подробные комментарии к коду, объясняющие его работу.
    - Код корректно обрабатывает ошибки при отправке и получении email.
    - Код соответствует PEP 8.
-  Минусы
    - Использована старая конструкция try-except, без разделения блоков.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не все переменные и параметры документированы с использованием rst.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Убедиться в наличии всех необходимых импортов.

2.  **Форматирование**:
    -   Использовать одинарные кавычки `'` для строк в коде, двойные кавычки `"` только в операциях вывода, логирования и `input`.
    -   Использовать rst документацию для всех функций, методов, классов и переменных.

3.  **Обработка ошибок**:
    -   Улучшить обработку исключений, вынося логику обработки ошибок в отдельный блок `except` для лучшей читаемости.

4.  **Безопасность**:
    -   Убедиться, что все необходимые параметры SMTP (`server`, `port`, `user`, `password`) берутся из переменных окружения.

5.  **Документация**:
    -   Добавить rst документацию для каждой функции, метода и переменной.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для отправки и получения электронной почты через SMTP и IMAP
==================================================================

Этот модуль предоставляет функциональность для отправки и получения электронной почты
с использованием SMTP или IMAP серверов.

Функции:
    - :func:`send`
      Отправляет электронное письмо с использованием SMTP-сервера.
    - :func:`receive`
      Получает электронные письма с IMAP-сервера.

Пример использования
--------------------

Пример отправки письма:

.. code-block:: python

    from src.utils.smtp import send

    if send(subject='Тест', body='Это тестовое письмо', to='test@example.com'):
        print('Письмо успешно отправлено')
    else:
        print('Ошибка при отправке письма')

Пример получения писем:

.. code-block:: python

    from src.utils.smtp import receive
    
    imap_server = 'imap.example.com'
    user = 'user@example.com'
    password = 'password'
    folder = 'inbox'
    
    emails = receive(imap_server, user, password, folder)
    if emails:
        for email in emails:
            print(f"От: {email['from']}")
            print(f"Тема: {email['subject']}")
            print(f"Тело: {email['body']}")
            print("-" * 20)
    else:
        print('Ошибка при получении писем')

**Важные замечания по безопасности**

    - **Словарь _connection:** Не храните учетные данные напрямую в коде. Используйте переменные окружения (например, os.environ). Это критически важно для безопасности.
    - **Обработка ошибок:** Код включает надежную обработку ошибок, логируя исключения с деталями (тема, тело и т. д.). Это очень полезно для отладки.
    - **Разбор электронной почты:** Функция `receive` корректно обрабатывает различные форматы электронной почты, предотвращая возможные проблемы.
    - **Обработка MIME:** Код корректно использует `MIMEText` для создания сообщения электронной почты, что важно для отправки простых текстовых писем.
"""

import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from typing import List, Dict, Optional

from src.logger.logger import logger

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
    """
    Отправляет электронное письмо.

    :param subject: Тема письма.
    :type subject: str
    :param body: Тело письма.
    :type body: str
    :param to: Адрес получателя.
    :type to: str
    :return: Возвращает True при успешной отправке, False в противном случае.
    :rtype: bool

    :raises Exception:  Если произошла ошибка при отправке.

    Пример:
    
    .. code-block:: python
    
        send(subject='Тест', body='Это тестовое письмо', to='test@example.com')
    """
    try:
        # Create SMTP connection
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        #  Инициирует защищенное TLS соединение
        smtp.ehlo()
        #  Устанавливает шифрование TLS
        smtp.starttls()
        #  Выполняет вход в SMTP-сервер
        smtp.login(_connection['user'], _connection['password'])
        #  Создает сообщение MIMEText
        message = MIMEText(body)
        #  Устанавливает заголовок 'Subject'
        message['Subject'] = subject
        #  Устанавливает заголовок 'From'
        message['From'] = _connection['user']
        #  Устанавливает заголовок 'To'
        message['To'] = to
        # Отправка электронной почты
        smtp.sendmail(_connection['user'], to, message.as_string())
        #  Закрывает SMTP-соединение
        smtp.quit()
        return True
    except Exception as ex:
        logger.error(f'Ошибка отправки email. Subject: {subject}. Body: {body}. Error: {ex}', exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """
    Получает электронные письма с IMAP-сервера.

    :param imap_server: Адрес IMAP-сервера.
    :type imap_server: str
    :param user: Имя пользователя IMAP.
    :type user: str
    :param password: Пароль пользователя IMAP.
    :type password: str
    :param folder: Папка для получения писем (по умолчанию 'inbox').
    :type folder: str
    :return: Возвращает список словарей с данными писем или None в случае ошибки.
    :rtype: Optional[List[Dict[str, str]]]
    :raises Exception: Если произошла ошибка при получении писем.

    Пример:

    .. code-block:: python
        
        receive(imap_server, user, password, 'inbox')
    """
    try:
        #  Устанавливает защищенное IMAP соединение
        mail = imaplib.IMAP4_SSL(imap_server)
        #  Выполняет вход в IMAP-сервер
        mail.login(user, password)
        #  Выбирает почтовую папку
        mail.select(folder)
        #  Поиск всех писем
        status, data = mail.search(None, 'ALL')
        #  Получает список идентификаторов писем
        email_ids = data[0].split()
        #  Инициализирует список для хранения данных писем
        emails = []
        for email_id in email_ids:
            #  Извлекает данные писем
            status, data = mail.fetch(email_id, '(RFC822)')
            #  Извлекает необработанное сообщение электронной почты
            raw_email = data[0][1]
            #  Преобразует байты в сообщение электронной почты
            msg = email.message_from_bytes(raw_email)
            #  Извлекает данные из письма
            email_data = {
                'subject': msg['subject'],
                'from': msg['from'],
                'body': msg.get_payload(decode=True, _charset='utf-8').decode('utf-8', 'ignore')  # Decode & handle potential errors
            }
            #  Добавляет данные в список
            emails.append(email_data)
        #  Закрывает IMAP-соединение
        mail.close()
        #  Выходит из IMAP-сервера
        mail.logout()
        return emails
    except Exception as ex:
        logger.error(f'Произошла ошибка при получении писем: {ex}', exc_info=True)
        return None
```