# Документация для Google Drive Uploader Bot

## Обзор

Этот документ содержит информацию о Telegram-боте, написанном на Python, который позволяет загружать файлы по прямым и поддерживаемым ссылкам в Google Drive. Бот был вдохновлен проектом [CyberBoySumanjay](https://github.com/cyberboysumanjay) [Google Drive Uploader](https://telegram.dog/driveuploadbot).

## Подробней

Этот бот может быть использован для загрузки файлов в Google Drive через Telegram. Он поддерживает прямые ссылки, ссылки Mega.nz, ссылки openload (больше не доступны) и ссылки Dropbox.

## Функциональность

- Загрузка файлов в Google Drive по прямым и поддерживаемым ссылкам.
- Поддержка TeamDrive (требуется хардкодинг).
- Авторизация пользователя через команду `/auth`.
- Удаление учетных данных пользователя через команду `/revoke`.

## Установка

### Необходимые модули

```
sudo pip3 install -r requirements.txt
```

### Запуск бота

```
python3 bot.py
```

## Использование

1.  Авторизуйте бота с помощью команды `/auth`, сгенерируйте ключ и отправьте его боту.
2.  Отправьте боту поддерживаемую ссылку.

## Доступные команды

-   `/start` - Начальное сообщение.
-   `/auth` - Авторизация пользователя.
-   `/revoke` - Удаление сохраненных учетных данных.
-   `/help` - Текст справки.

## Поддерживаемые ссылки

-   Прямые ссылки
-   Mega.nz ссылки
-   openload ссылки (больше не доступны)
-   Dropbox ссылки

## Требования

-   [Google Drive API Credential](https://console.cloud.google.com/apis/credentials) (другие типы) - `Обязательно`
-   Telegram Bot Token (с использованием BotFather) - `Обязательно`
-   Openload ftp логин и ключ - `опционально`
-   Mega Email и Password - `Опционально`

Изменить API Openload и пароль Mega можно по следующим путям:

-   Mega => Plugins > TEXT.py
-   Openload => Plugins > dlopenload.py

## Настройка собственного бота

```
1. Создайте [Google Drive API Credential](https://console.cloud.google.com/apis/credentials) (другой тип) и скачайте его JSON.

2. Поместите его в корневую директорию бота и переименуйте в "client_secrets.json".

3. Замените Bot Token в [creds.py file](./creds.py).

4. Ваш бот готов к размещению.
```

### Размещение на Heroku

Убедитесь, что вы изменили свой Bot Token и Google Client API перед размещением.

## TODO

-   Переименование файла при загрузке.
-   Добавление поддержки файлов Telegram [медленная загрузка :( ].
-   Добавление youtube-dl.
-   Исправление поддержки openload.
-   Добавление zippyshare, Mediafire, cloud mail, Яндекс диск, Sourceforge {они уже написаны в PPE плагине, вы можете использовать их оттуда}.
-   Google Drive Direct Link Generator.

## Лицензия

-   GPLv3