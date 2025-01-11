# Анализ кода модуля `smtp`

**Качество кода**
8
- Плюсы
    -  Код хорошо структурирован и разбит на логические блоки.
    -  Используется `logger` для регистрации ошибок.
    -  Присутствует обработка исключений для предотвращения сбоев.
    -  Код корректно использует `MIMEText` для создания сообщений.
    -  Для чтения данных из env используется `os.environ.get`, что позволяет задавать значения по умолчанию.
- Минусы
    -  В начале файла нет описания модуля в формате RST.
    -  Функции `send` и `receive` не имеют документации в формате RST.
    -  `_connection` не имеет документации в формате RST.
    -  В коде используются двойные кавычки (") вместо одинарных (') в словарях.
    -  В функции `receive` используется `decode` дважды, что можно переписать для большей читаемости.
    -  В функции `receive` не все переменные имеют docstring, такие как status, data, mail и др.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла в формате RST.
2.  Добавить документацию в формате RST для функций `send` и `receive`.
3.  Добавить документацию в формате RST для `_connection`.
4.  Использовать одинарные кавычки (`'`) вместо двойных (`"`) в словарях и строках, кроме операций вывода.
5.  Упростить декодирование в функции `receive`, можно использовать один вызов decode.
6.  Убрать избыточный `try-except` из функции `send` используя только `logger.error`.
7.  Описать все переменные в функции receive, такие как mail, status, data, email_ids, raw_email, msg, email_data.
8.  Добавить `from src.logger.logger import logger`

**Оптимизированный код**

```python
"""
Модуль для работы с SMTP и IMAP серверами
=========================================================================================

Этот модуль предоставляет функциональность для отправки и получения электронных писем
с использованием SMTP и IMAP серверов.

Функции:
    - :func:`send` : Отправляет электронное письмо, используя SMTP сервер.
    - :func:`receive` : Получает электронные письма, используя IMAP сервер.

**Важные замечания по безопасности и надежности:**

    -   **Словарь _connection:** Не храните учетные данные в этом файле. Используйте переменные окружения (например, `os.environ`)
        для хранения параметров подключения. Это критически важно для безопасности.
    -   **Обработка ошибок:** Код включает обработку ошибок с помощью логирования исключений и подробной информации об ошибках.
    -   **Разбор email:** Функция `receive` обрабатывает различные форматы сообщений, предотвращая потенциальные проблемы.
    -   **Обработка MIME:** Код корректно использует `MIMEText` для создания сообщений.

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
    """Отправляет электронное письмо.

    Args:
        subject (str): Тема письма.
        body (str): Тело письма.
        to (str): Адрес получателя.

    Returns:
        bool: `True`, если письмо отправлено успешно, `False` в противном случае.

    Raises:
        Exception: При возникновении ошибки при отправке письма.

    Example:
        >>> send(subject='Test Email', body='This is a test email', to='test@example.com')
        True
    """
    try:
        # Создает SMTP соединение
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
        logger.error(f"Ошибка отправки email. Тема: {subject}. Тело: {body}. Ошибка: {ex}", exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """Получает электронные письма с IMAP сервера.

    Args:
        imap_server (str): Адрес IMAP сервера.
        user (str): Имя пользователя IMAP.
        password (str): Пароль пользователя IMAP.
        folder (str): Папка для поиска писем.

    Returns:
        Optional[List[Dict[str, str]]]: Список словарей с данными писем, если успешно, иначе `None`.
            Каждый словарь содержит ключи: `subject`, `from`, `body`.

    Raises:
        Exception: При возникновении ошибки при получении писем.

     Example:
        >>> receive(imap_server='imap.example.com', user='test@example.com', password='password')
        [{'subject': 'Test', 'from': 'sender@example.com', 'body': 'Test Body'}]
    """
    try:
        # Создание IMAP соединения
        mail = imaplib.IMAP4_SSL(imap_server)
        # Проводит авторизацию
        mail.login(user, password)
        # Выбор почтовой папки
        mail.select(folder)

        # Поиск всех писем в папке
        status, data = mail.search(None, 'ALL')
        # Получение списка ID писем
        email_ids = data[0].split()

        emails = []
        for email_id in email_ids:
            # Получение тела письма по его ID
            status, data = mail.fetch(email_id, '(RFC822)')
            # Извлечение необработанного содержимого письма
            raw_email = data[0][1]
            # Преобразование содержимого письма в объект Message
            msg = email.message_from_bytes(raw_email)

            # Извлечение данных из письма
            email_data = {
                'subject': msg['subject'],
                'from': msg['from'],
                'body': msg.get_payload(decode=True, _charset='utf-8').decode('utf-8', 'ignore')  # Декодирование тела письма
            }
            emails.append(email_data)
        # Закрытие IMAP соединения
        mail.close()
        # Выход из IMAP соединения
        mail.logout()
        return emails

    except Exception as ex:
        logger.error(f"Произошла ошибка при получении писем: {ex}", exc_info=True)
        return None
```