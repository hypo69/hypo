# Документация для Google Drive Uploader Bot

## Обзор

Этот бот Telegram, написанный на Python, позволяет загружать файлы на Google Drive. Он поддерживает прямые ссылки, ссылки Mega.nz и Dropbox. Также имеется поддержка Teamdrive.
  
## Подробнее

Этот код является частью проекта `hypotez`. Бот использует Google Drive API для загрузки файлов и требует учетные данные API Google Drive и токен бота Telegram. Он также может использовать учетные данные Openload и Mega для поддержки загрузки с этих платформ.

## Содержание

- [Название модуля](#google-drive-uploader-bot)
- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Функции](#функции)
- [Avalible Commands](#avalible-commands)
- [Requirements](#requirements)
- [Setup Your Own Bot](#setup-your-own-bot)
- [TODO](#todo)
- [Лицензия](#лицензия)
## Функции

### Avalible Commands
  - `/start` =  Start Message
  - `/auth` = Authorise You
  - `/revoke` = Delete Your Saved credential
  - `/help` =  help Text

### Requirements
  - [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (Others type)  `Required`
  - Telegram Bot Token (Using BotFather)  `Required`
  - Openload ftp login and Key  `optional`
  - Mega Email and Password  `Optional`

### Setup Your Own Bot
```
1. Create Your  [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (other type) and Download  Its json

2. Paste it In Bot Root Directroy  and Rename it "client_secrets.json"

3. Replace Your Bot Token in  [creds.py file](./creds.py)

4. Your Bot is Ready to Host. 
```

## TODO
  - Rename file while uploading
  - Adding Telegram File Support [ slow Download :( ]
  - Add  Youtube-dl
  - Fix openload support
  - Adding zippyshare , Mediafire , cloud mail  , Yandex disk ,Sourceforge {these are already written In PPE plugin you can use these from there}
  - Google Drive Direct Link Generator

### Лицензия
  - GPLv3