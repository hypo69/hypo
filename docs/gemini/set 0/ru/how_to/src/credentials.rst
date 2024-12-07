Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `ProgramSettings`, который загружает настройки программы из файла `config.json` и базы данных KeePass.  Класс является синглтоном, гарантируя, что существует только один экземпляр `ProgramSettings`. Он хранит пути к важным каталогам проекта, а также учетные данные для различных API (AliExpress, OpenAI, Gemini, Discord, Telegram, PrestaShop, SMTP, Facebook, GAPI).  Код также содержит функции для определения корневой директории проекта и работы с базой данных KeePass.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует модули `datetime`, `getpass`, `os`, `sys`, `json`, `warnings`, `dataclasses`, `pathlib`, `types`, `typing`, `pydantic`, `pykeepass`, и другие специфичные для проекта.
2. **Определение функции `set_project_root`:** Эта функция ищет корневую директорию проекта, начиная с директории текущего файла и идя вверх по дереву каталогов. Она останавливается, если находит директории, содержащие маркерные файлы (`pyproject.toml`, `requirements.txt`, `.git`).  Если корневая директория найдена, добавляет её в `sys.path`.
3. **Определение декоратора `singleton`:**  Декоратор `singleton` гарантирует, что класс `ProgramSettings` будет синглтоном.
4. **Определение класса `ProgramSettings`:** Это основной класс настроек программы, использующий `pydantic` для валидации данных.
5. **Инициализация `ProgramSettings`:**  В методе `__init__` класс загружает настройки из `config.json` в `self.config`.
6. **Инициализация путей (`self.path`):** Создаёт `SimpleNamespace` для хранения путей к различным директориям проекта (корень, bin, src, log, tmp, data и т.д.). Пути инициализируются или с конфига, или с корневой директории.
7. **Проверка на наличие новой версии:**  Выполняет проверку на наличие новой версии проекта (`check_latest_release`).
8. **Загрузка учетных данных из KeePass:** В методе `_load_credentials` открывается база данных KeePass, а затем вызываются вспомогательные методы для загрузки данных конкретных API (AliExpress, OpenAI, Gemini, etc.).
9. **Функции `_load_*_credentials`:**  Эти функции извлекают данные API из базы данных KeePass по определённым путям (группам и записям).  Они устанавливают соответствующие поля в `self.credentials` (например, `self.credentials.aliexpress.api_key`). Если загрузка происходит некорректно, происходит вывод сообщения об ошибке.
10. **Метод `_open_kp`:** Метод для открытия базы данных KeePass, включая попытки повторной авторизации.
11. **Глобальная переменная `gs`:**  Создаёт глобальный экземпляр `ProgramSettings`, который используется по всему проекту.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.credentials import gs

    # Получение API ключа для Aliexpress
    aliexpress_api_key = gs.credentials.aliexpress.api_key

    # Получение настроек для PrestaShop
    presta_translations_server = gs.credentials.presta.translations.server

    # Получение пути к корневой директории
    project_root = gs.path.root

    # Получение текущей метки времени
    current_timestamp = gs.now()