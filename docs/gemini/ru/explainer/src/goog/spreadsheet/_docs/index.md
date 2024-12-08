# Код для работы с Google Sheets API v4

```markdown
## <input code>

```python
## \file hypotez/src/goog/spreadsheet/_docs/index.html
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.goog.spreadsheet._docs """
MODE = 'debug'
<div class="article-formatted-body article-formatted-body article-formatted-body_version-1"><div xmlns="http://www.w3.org/1999/xhtml"><h2>Постановка задачи</h2><br>
    Пусть нам нужно создать программой на языке Python <a href="https://docs.google.com/spreadsheets/d/1kygOW5wSSVqwf26M-OCT72i0FX0olZAz4duT2i6psp4/edit?usp=sharing">вот такую таблицу</a>:<br>
    <br>
    <a href="https://habrahabr.ru/post/305378/"><img src="https://habrastorage.org/r/w1560/files/5c8/3b1/1f8/5c83b11f836a4dac84a584158a40a6c1.png" alt="image" data-src="https://habrastorage.org/files/5c8/3b1/1f8/5c83b11f836a4dac84a584158a40a6c1.png"></a><br>
    ... (много текста о создании сервисного аккаунта, установки библиотек и т.д.)
</div></div>
```
```markdown
## <algorithm>

Этот код описывает алгоритм создания и настройки Google Spreadsheets через API.  Пошаговая блок-схема:

1. **Инициализация:**
    * Импортируются необходимые библиотеки (`httplib2`, `apiclient`, `oauth2client`).
    * Задается путь к файлу с закрытым ключом сервисного аккаунта (`CREDENTIALS_FILE`).
    * Создается объект `credentials` с помощью `ServiceAccountCredentials`. Он отвечает за аутентификацию.
    * Создается объект `httpAuth` для авторизации запросов.
    * Создается объект `service` для взаимодействия с Google Sheets API.

2. **Создание документа:**
    * Вызывается метод `spreadsheets.create` для создания нового документа.
    * `body` содержит параметры нового документа, такие как `title`, `locale` и `sheets`.
    * Полученный ответ содержит `spreadsheetId`.

3. **Назначение доступа:**
    * Создается объект `driveService` для работы с Google Drive API.
    * Вызывается метод `permissions.create` для назначения доступа к документу.
    * `fileId` — ID созданного документа, `body` содержит типы и роли доступа (`type`, `role`).

4. **Установка ширины столбцов:**
    * Используется метод `spreadsheets.batchUpdate` для одновременного изменения свойств документа.
    * В запросе содержатся `UpdateDimensionPropertiesRequest` для изменения ширины каждого столбца.

5. **Заполнение данных:**
    * Используется метод `spreadsheets.values.batchUpdate` для добавления данных в ячейки.
    * `valueInputOption` определяет способ интерпретации данных (в данном случае `USER_ENTERED` для работы с формулами).
    * В `data` передаются объекты `GridRange` с диапазонами ячеек и массивами значений.


6. **Настройка форматирования:**
    * Используются запросы `MergeCellsRequest`, `RepeatCellRequest`, `UpdateCellsRequest`, `UpdateBordersRequest` для настройки форматирования ячеек (выравнивание, жирность, цвет, границы).


**Примеры данных:**
* `spreadsheetId`: `1Sfl7EQ0Yuyo65INidt4LCrHMzFI9wrmc96qHq6EEqHM`
* `body` (создание документа): `{ "properties": {"title": "Название документа", "locale": "ru_RU"}, "sheets": [...] }`
* `body` (разрешение доступа): `{ "type": "anyone", "role": "reader" }`
* `requests` (batchUpdate): список запросов на изменение ширины столбцов или форматирования.


```markdown
## <mermaid>

```mermaid
graph TD
    A[Пользовательский код] --> B{Создать сервис аккаунт};
    B --> C[Получить credentials];
    C --> D[Создать service объект];
    D --> E[Создать Spreadsheet];
    E --> F[Получить spreadsheetId];
    F --> G[Создать driveService объект];
    G --> H[Назначить доступ];
    H --> I[Получить доступные права];
    I --> J[Формирование запросов batchUpdate];
    J --> K[Выполнение batchUpdate];
    K --> L[Заполнение данных (values.batchUpdate)];
    L --> M[Дополнительная настройка форматирования (Merge, Repeat, Update)];
    M --> N[Выполнение batchUpdate];
    N --> O[Получение результатов];
    O --> P[Обработка результатов];
    P --> Q[Завершение];

    subgraph "Библиотеки"
        C --> |httplib2| httplib2;
        C --> |apiclient| apiclient;
        C --> |oauth2client| oauth2client;
        C --> |google-api-python-client| google-api-python-client;
    end
```

**Зависимости:**
* `httplib2`: Библиотека для работы с HTTP-запросами. Используется для взаимодействия с Google API.
* `apiclient`: Библиотека для работы с Google API. Позволяет строить запросы и получать ответы.
* `oauth2client`: Библиотека для работы с OAuth 2.0. Используется для аутентификации сервисного аккаунта.
* `google-api-python-client`: Клиентская библиотека для доступа к разным Google API.  Обеспечивает структурированный способ взаимодействия.

```markdown
## <explanation>

**Импорты:**
* `httplib2`: Библиотека для работы с HTTP-запросами. Необходима для отправки запросов к API.
* `apiclient`: Библиотека для работы с Google API. В данном случае используется для доступа к Google Sheets API.
* `oauth2client`: Библиотека для работы с OAuth 2.0. Используется для аутентификации сервисного аккаунта.

**Классы:**
* `Spreadsheet`:  Обёртка над Google Sheets API v4.  Предоставляет удобные методы для подготовки и выполнения запросов (например, `prepare_setColumnWidth`, `prepare_setValues`, `runPrepared`).  Этот класс организует и объединяет запросы для улучшения кода.

**Функции:**
* `spreadsheets.create`: Создает новый Google Spreadsheet документ.
* `permissions.create`: Назначает разрешения сервисному аккаунту на доступ к документу.
* `spreadsheets.batchUpdate`: Применяет пакет изменений к Google Spreadsheet (ширина столбцов, форматирование).
* `spreadsheets.values.batchUpdate`: Заполняет ячейки Google Spreadsheet данными.
* `prepare_setColumnWidth`, `prepare_setColumnsWidth`, `prepare_setValues`: вспомогательные функции класса `Spreadsheet` для подготовки отдельных запросов.

**Переменные:**
* `CREDENTIALS_FILE`: Путь к файлу с закрытым ключом сервисного аккаунта.
* `spreadsheet`: Объект, содержащий данные о созданном документе.
* `service`, `driveService`: Объекты для работы с Google Sheets и Google Drive API соответственно.

**Возможные ошибки/улучшения:**
* **Ошибка доступа:**  Код не обрабатывает случаи, когда у сервисного аккаунта нет доступа. Важно проверять ответы на запросы и обрабатывать возможные ошибки.
* **Масштабируемость:** Класс `Spreadsheet` хорошо организует запросы, но для очень сложных операций с большим количеством данных потребуется более продуманная архитектура.
* **Обработка ошибок:**  Не хватает обработки исключений, которые могут возникнуть при выполнении запросов к API.
* **Документация:** Код содержит много ссылок на документацию, но для лучшего понимания его работы было бы полезно добавить комментарии к отдельным частям кода.
* **Пикачу:**  Пока не понятно, как программа должна интегрировать картинку Пикачу в таблицу.

**Взаимосвязи с другими частями проекта:**
Код предполагает существование сервисного аккаунта и файла ключей (`test-proj-for-habr-article-1ab131d98a6b.json`) для аутентификации с Google API.  Это предполагает предварительную настройку и конфигурацию в рамках проекта.
```