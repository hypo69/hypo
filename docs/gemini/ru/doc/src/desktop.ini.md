# Документация к файлу `desktop.ini`

## Обзор

Файл `desktop.ini` является конфигурационным файлом Windows, который используется для настройки внешнего вида и поведения папок. 
Этот файл содержит информацию, определяющую, как папка должна отображаться в проводнике Windows, включая пользовательские значки и настройки отображения.

## Содержание

- [Обзор](#обзор)
- [Секция `.ShellClassInfo`](#секция-shellclassinfo)
- [Секция `ViewState`](#секция-viewstate)

## Секция `.ShellClassInfo`

### Описание

Секция `[.ShellClassInfo]` содержит информацию о классе оболочки папки.

### Параметры

- `IconResource`: Указывает путь к значку, который будет использоваться для этой папки. В данном случае, `C:\\WINDOWS\\System32\\SHELL32.dll,300` означает использование значка из системной библиотеки `SHELL32.dll` под индексом 300.

## Секция `ViewState`

### Описание

Секция `[ViewState]` содержит настройки вида папки.

### Параметры

- `Mode`: Не указано значение, что может указывать на использование режима по умолчанию или отсутствие пользовательских настроек режима отображения.
- `Vid`: Не указано значение, что может указывать на отсутствие пользовательских настроек для идентификатора вида.
- `FolderType`: Указывает на то, что тип папки является `Generic`, что означает обычный тип папки без специальных настроек.