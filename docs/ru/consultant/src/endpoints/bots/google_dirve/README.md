# Анализ кода модуля `README.md`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Документ содержит инструкции по использованию бота, установке и настройке.
    - Присутствуют описания команд и поддерживаемых ссылок.
    - Предоставлены ссылки на необходимые ресурсы и репозитории.
- **Минусы**:
    - Документ не следует единому стилю оформления, много лишних пробелов.
    - Используются обратные кавычки (`) вместо тройных (```) для блоков кода, что не совсем корректно.
    - Некоторые комментарии и фразы не соответствуют стандартам оформления Markdown.
    - Нет четкой структуры в описании, некоторые части могут быть объединены или перефразированы.
    -  Присутствуют опечатки и орфографические ошибки.

## Рекомендации по улучшению:

- Улучшить форматирование документа, привести к общему стилю, удалить лишние пробелы.
- Исправить форматирование блоков кода, используя тройные обратные кавычки (```) для корректного отображения кода.
- Проверить текст на наличие опечаток и орфографических ошибок.
- Сгруппировать информацию по разделам для удобства чтения.
-  Использовать более точные формулировки в описаниях.
-  Убрать лишние фразы и повторы.
-  Переформулировать разделы "TODO" в более понятные и развернутые.
-  Добавить информацию о возможных проблемах и способах их решения.
-  Разделить установку и настройку на отдельные подразделы.

## Оптимизированный код:
```markdown
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Google Drive Uploader Bot

`It Was my first Python Project And behind this Whole credit goes To ` [CyberBoySumanjay](https://github.com/cyberboysumanjay)

### Inspired By Sumanjay Bot :D [Google Drive Uploader](https://telegram.dog/driveuploadbot)

Here Is Live Version Of Bot [Gdriveupme_bot](http://telegram.dog/gdriveupme_bot)

# Update (30 May 2020)

- Teamdrive Support added

`Teamdrive is not for users You have to hardcode it ,`
`Wait for V2 bot This Bot don't have active development I will add User Specfic Teamdrive option`

# How to Add Teamdrive
- Replace `TEAMDRIVE_FOLDER_ID` and `TEAMDRIVE_ID` in [creds.py](./creds.py)

### What Is this?
```
 A Telegram Bot Written In Python
```
### What can it do?
```
 It Can Upload Your Direct and Supported links into Google Drive.
```
### Install Module
```
sudo pip3 install -r requirements.txt
```
### Run This bot
```
python3 bot.py
```
### How Can We use It
- First authorise Bot Using `/auth` command Generate a Key and send it To bot.
- Now You can Send Supported Link To Bot.

### Available Commands
- `/start` - Start Message
- `/auth` - Authorise You
- `/revoke` - Delete Your Saved credential
- `/help` - help Text

## Supported Links:
- Direct Link
- Mega.nz Link
- Dropbox Link

## Requirements
- [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (Others type)  `Required`
- Telegram Bot Token (Using BotFather)  `Required`
- Mega Email and Password  `Optional`

`If You wanna Change Mega Email Password You Can Change it From Given Path`
- Mega => Plugins > TEXT.py

## Setup Your Own Bot
```
1. Create Your  [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (other type) and Download  Its json.

2. Paste it In Bot Root Directroy  and Rename it "client_secrets.json".

3. Replace Your Bot Token in  [creds.py file](./creds.py).

4. Your Bot is Ready to Host.
```
### You Can Use Heroku To host It.

`Make sure You have Changed Your Bot Token and google client api Before Hosting It`

### My Hidden Thanks To :heart:
- [CyberBoySumanjay](https://github.com/cyberboysumanjay)
- [SpEcHiDe](https://github.com/SpEcHiDe)
- [Atulkadian](https://github.com/atulkadian)

# TODO
- Rename file while uploading
- Add Telegram File Support [ slow Download :( ]
- Add Youtube-dl
- Add support for zippyshare, Mediafire, cloud mail, Yandex disk, Sourceforge {these are already written In PPE plugin you can use these from there}
- Add Google Drive Direct Link Generator

### Licence
- GPLv3