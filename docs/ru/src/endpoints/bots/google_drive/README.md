# Документация для модуля Google Drive Uploader Bot

## Обзор

Данный модуль представляет собой Telegram-бота, разработанного на Python, который позволяет загружать файлы по прямым и поддерживаемым ссылкам в Google Drive. Бот был вдохновлен проектом [CyberBoySumanjay](https://github.com/cyberboysumanjay) и предоставляет пользователям возможность авторизации, отмены авторизации и получения справки по командам.

## Подробнее

Этот Telegram-бот написан на Python и предназначен для загрузки файлов в Google Drive с использованием прямых ссылок и других поддерживаемых источников. Бот поддерживает авторизацию пользователей через Google Drive API, позволяя им сохранять файлы непосредственно в своем облачном хранилище.

## Функциональность

### Основные возможности:

-   Загрузка файлов в Google Drive по прямым ссылкам.
-   Поддержка ссылок Mega.nz, Dropbox.
-   Авторизация пользователей через Google Drive API.
-   Удаление сохраненных учетных данных.
-   Получение справки по командам бота.

### Команды бота:

-   `/start`: Отображает приветственное сообщение.
-   `/auth`: Запрашивает авторизацию пользователя.
-   `/revoke`: Удаляет сохраненные учетные данные пользователя.
-   `/help`: Отображает справочный текст.

### Поддерживаемые ссылки:

-   Прямые ссылки.
-   Ссылки Mega.nz.
-   Ссылки Dropbox.

## Настройка и установка

### Требования:

-   [Google Drive API Credential](https://console.cloud.google.com/apis/credentials) (Others type)  `Required`
-   Telegram Bot Token (Using BotFather)  `Required`

### Шаги по установке:

1.  Создайте [Google Drive API Credential](https://console.cloud.google.com/apis/credentials) (other type) и скачайте его JSON-файл.
2.  Поместите этот JSON-файл в корневую директорию бота и переименуйте его в "client\_secrets.json".
3.  Замените Bot Token в файле [creds.py](./creds.py) на свой, полученный от BotFather.

```bash
sudo pip3 install -r requirements.txt
python3 bot.py
```

## Использование Teamdrive (Общие диски)

### Настройка Teamdrive:

1.  Замените `TEAMDRIVE_FOLDER_ID` и `TEAMDRIVE_ID` в файле [creds.py](./creds.py) на соответствующие идентификаторы Teamdrive.

**Внимание:** Эта функция предназначена для опытных пользователей и требует хардкодинга параметров.

## Благодарности

-   [CyberBoySumanjay](https://github.com/cyberboysumanjay)
-   [SpEcHiDe](https://github.com/SpEcHiDe)
-   [Atulkadian](https://github.com/atulkadian)

## Планы на будущее (TODO)

-   Переименование файлов при загрузке.
-   Добавление поддержки загрузки файлов из Telegram (медленная загрузка).
-   Добавление поддержки Youtube-dl.
-   Исправление поддержки Openload.
-   Добавление поддержки zippyshare, Mediafire, cloud mail, Yandex disk, Sourceforge.
-   Генератор прямых ссылок Google Drive.

## Лицензия

-   GPLv3