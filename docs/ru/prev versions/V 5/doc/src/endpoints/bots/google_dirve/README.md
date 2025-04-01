# Google Drive Uploader Bot

## Обзор

Этот документ предоставляет информацию о боте для загрузки файлов в Google Drive, написанном на Python. Бот позволяет загружать файлы по прямым ссылкам и ссылкам с поддерживаемых сервисов в Google Drive.

## Подробней

Этот бот был вдохновлен ботом [CyberBoySumanjay](https://github.com/cyberboysumanjay). Бот предоставляет функциональность загрузки файлов в Google Drive через Telegram. Он поддерживает различные типы ссылок, такие как прямые ссылки, Mega.nz и Dropbox.

## Оглавление

- [Обзор](#обзор)
- [Подробней](#подробней)
- [Обновления](#обновления)
- [Как добавить Teamdrive](#как-добавить-teamdrive)
- [Что это такое?](#что-это-такое)
- [Что он может делать?](#что-он-может-делать)
- [Установка модуля](#установка-модуля)
- [Запуск бота](#запуск-бота)
- [Как использовать](#как-использовать)
- [Доступные команды](#доступные-команды)
- [Поддерживаемые ссылки](#поддерживаемые-ссылки)
- [Требования](#требования)
- [Настройка собственного бота](#настройка-собственного-бота)
- [Использование Heroku для хостинга](#использование-heroku-для-хостинга)
- [Благодарности](#благодарности)
- [TODO](#todo)
- [Лицензия](#лицензия)

## Обновления

- (30 мая 2020) Добавлена поддержка Teamdrive.

## Как добавить Teamdrive

- Замените `TEAMDRIVE_FOLDER_ID` и `TEAMDRIVE_ID` в [creds.py](./creds.py).

## Что это такое?

```
A Telegram Bot Written In Python
```

## Что он может делать?

```
It Can Upload Your Direct and Supported links into Google Drive.
```

## Установка модуля

```
sudo pip3 install -r requirements.txt
```

## Запуск бота

```
python3 bot.py
```

## Как использовать

- Сначала авторизуйте бота, используя команду `/auth`. Сгенерируйте ключ и отправьте его боту.
- Теперь вы можете отправлять поддерживаемые ссылки боту.

## Доступные команды

- `/start` = Start Message
- `/auth` = Authorise You
- `/revoke` = Delete Your Saved credential
- `/help` = help Text

## Поддерживаемые ссылки

- Direct Link
- Mega.nz Link
- openload link (not avalibe anymore)
- Dropbox Link

## Требования

- [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (Others type) `Required`
- Telegram Bot Token (Using BotFather) `Required`
- Openload ftp login and Key `optional`
- Mega Email and Password `Optional`

Если вы хотите изменить Openload Api и Mega Email Password, вы можете изменить их по указанному пути:

- Mega => Plugins > TEXT.py
- Openload => Plugins > dlopenload.py

## Настройка собственного бота

```
1. Create Your  [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (other type) and Download  Its json

2. Paste it In Bot Root Directroy  and Rename it "client_secrets.json"

3. Replace Your Bot Token in  [creds.py file](./creds.py)

4. Your Bot is Ready to Host.
```

## Использование Heroku для хостинга

Убедитесь, что вы изменили свой Bot Token и google client api перед размещением.

## Благодарности

:heart:

- [CyberBoySumanjay](https://github.com/cyberboysumanjay)
- [SpEcHiDe](https://github.com/SpEcHiDe)
- [Atulkadian](https://github.com/atulkadian)

## TODO

- Rename file while uploading
- Adding Telegram File Support [ slow Download :( ]
- Add Youtube-dl
- Fix openload support
- Adding zippyshare , Mediafire , cloud mail , Yandex disk ,Sourceforge {these are already written In PPE plugin you can use these from there}
- Google Drive Direct Link Generator

## Лицензия

- GPLv3