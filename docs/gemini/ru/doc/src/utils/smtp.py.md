# Модуль для работы с SMTP

## Обзор

Модуль `smtp.py` предоставляет интерфейс для отправки и получения электронных писем с использованием протоколов SMTP и IMAP. Он содержит функции для отправки электронных писем через SMTP-сервер и получения электронных писем через IMAP-сервер.

## Подробней

Этот модуль предоставляет функциональность для отправки и получения электронных писем. Он включает функции для отправки электронных писем с использованием SMTP и получения электронных писем с использованием IMAP.
Модуль содержит функции `send` и `receive`, которые обеспечивают отправку и получение электронных писем соответственно. Функция `send` использует SMTP для отправки писем, а функция `receive` использует IMAP для получения писем с сервера.

**Важные аспекты безопасности и надежности**:

- **Словарь `_connection`**: Не рекомендуется жестко кодировать учетные данные в этом файле. Переместите словарь `_connection` в переменные среды (например, с помощью `os.environ`). Это крайне важно для безопасности. Избегайте хранения паролей непосредственно в исходном коде.

- **Обработка ошибок**: Код включает надежную обработку ошибок, регистрируя исключения с подробностями (тема, тело и т. д.). Это очень полезно для отладки.

- **Разбор электронной почты**: Функция `receive` корректно обрабатывает различные форматы электронной почты, предотвращая потенциальные проблемы.

- **Обработка MIME**: Код правильно использует `MIMEText` для создания сообщения электронной почты, что крайне важно для отправки простых текстовых писем.

## Функции

### `send`

```python
def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """Отправляет электронное письмо. Возвращает True в случае успеха, False в противном случае. Логирует ошибки."""
    try:
        # Создание SMTP-соединения
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
```

**Как работает функция**:

1.  Функция пытается установить соединение с SMTP-сервером, используя данные из словаря `_connection`.
2.  После успешного подключения функция создает объект `MIMEText` с телом письма.
3.  Затем устанавливаются заголовки письма, такие как тема, отправитель и получатель.
4.  Функция отправляет письмо и закрывает соединение.
5.  Если в процессе отправки возникает ошибка, она логируется с использованием `logger.error`, и функция возвращает `False`.

**Параметры**:

*   `subject` (str, optional): Тема письма. По умолчанию ''.
*   `body` (str, optional): Тело письма. По умолчанию ''.
*   `to` (str, optional): Адрес получателя. По умолчанию 'one.last.bit@gmail.com'.

**Возвращает**:

*   `bool`: `True`, если письмо успешно отправлено, `False` в противном случае.

**Вызывает исключения**:

*   `Exception`: В случае ошибки при отправке письма.

**Примеры**:

```python
# Отправка простого письма
send(subject='Тест', body='Это тестовое письмо', to='test@example.com')

# Отправка письма без указания получателя (будет использован адрес по умолчанию)
send(subject='Тест', body='Это тестовое письмо')
```

### `receive`

```python
def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """Получает электронные письма. Возвращает список словарей с данными писем в случае успеха, None в противном случае. Логирует ошибки."""
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

**Как работает функция**:

1.  Функция устанавливает соединение с IMAP-сервером, используя предоставленные учетные данные.
2.  Выполняется вход в почтовый ящик и выбор указанной папки (по умолчанию 'inbox').
3.  Функция выполняет поиск всех писем в выбранной папке.
4.  Для каждого найденного письма извлекается его содержимое и формируется словарь с данными письма (тема, отправитель, тело).
5.  Все полученные словари добавляются в список `emails`.
6.  После обработки всех писем соединение с сервером закрывается, и функция возвращает список словарей с данными писем.
7.  В случае возникновения ошибки в процессе получения писем, она логируется с использованием `logger.error`, и функция возвращает `None`.

**Параметры**:

*   `imap_server` (str): Адрес IMAP-сервера.
*   `user` (str): Имя пользователя для входа в почтовый ящик.
*   `password` (str): Пароль для входа в почтовый ящик.
*   `folder` (str, optional): Папка для поиска писем. По умолчанию 'inbox'.

**Возвращает**:

*   `Optional[List[Dict[str, str]]]`: Список словарей с данными писем в случае успеха, `None` в противном случае.

**Вызывает исключения**:

*   `Exception`: В случае ошибки при получении писем.

**Примеры**:

```python
# Получение писем из почтового ящика
emails = receive(imap_server='imap.example.com', user='test@example.com', password='password')
if emails:
    for email in emails:
        print(f"Тема: {email['subject']}")
        print(f"Отправитель: {email['from']}")
        print(f"Тело: {email['body']}")
```