# ИНСТРУКЦИЯ по использованию бота для обучения модели

## Обзор

Данная документация описывает пошаговую инструкцию по обучению и тестированию модели через бота в Discord.  Она включает в себя шаги по подготовке данных, отправке команд для обучения, мониторингу процесса и тестированию модели.

## Команды

### `!train`

**Описание**: Команда для обучения модели.  Разрешает передавать данные для обучения как текстом, так и файлом.

**Параметры**:

* `"Your training data here"` (str): Текстовые данные для обучения.  Необязательно.
* `positive=True` (bool, optional): Флаг, указывающий, что данные предназначены для положительного класса. По умолчанию `False`.

**Возвращает**:

* `str`: Сообщение об успешном запуске обучения или ошибке. Примеры сообщений: `Model training started. Job ID: <job_id>`, `Error: Invalid training data format`.

**Вызывает исключения**:

* `ValueError`: В случае неверного формата данных для обучения.
* `FileNotFoundError`: Если передан файл, который не найден.
* `IOError`: При проблемах с чтением файла.

### `!test`

**Описание**: Команда для тестирования обученной модели.

**Параметры**:

* `{"test_key": "test_value"}` (dict): Словарь с данными для тестирования.

**Возвращает**:

* `str`: Предсказания модели.

**Вызывает исключения**:

* `ValueError`: В случае неверного формата данных для тестирования.
* `AttributeError`: Если модель не обучена.
* `RuntimeError`: Проблемы при получении ответа от модели.

### `!archive`

**Описание**: Команда для архивирования файлов.

**Параметры**:

* `<directory_path>` (str): Путь к каталогу для архивирования.

**Возвращает**:

* `str`: Сообщение об успешном архивировании или об ошибке.

**Вызывает исключения**:

* `FileNotFoundError`: Если указанный каталог не найден.
* `OSError`: Проблемы с операциями ввода-вывода.

### `!select_dataset`

**Описание**: Команда для выбора набора данных.

**Параметры**:

* `<path_to_dir_positive>` (str): Путь к каталогу с данными для положительного класса.
* `positive=True` (bool, optional): Флаг, указывающий, что данные предназначены для положительного класса.


**Возвращает**:

* `str`: Сообщение об успешном выборе набора данных или об ошибке.


**Вызывает исключения**:

* `FileNotFoundError`: Если указанный каталог не найден.
* `OSError`: Проблемы с операциями ввода-вывода.
* `ValueError`: Неверные параметры.

### `!ask`

**Описание**: Команда для получения ответа от модели.

**Параметры**:

* `<question>` (str): Вопрос, который нужно задать модели.

**Возвращает**:

* `str`: Ответ модели.

**Вызывает исключения**:

* `RuntimeError`: Проблемы при получении ответа от модели.
* `AttributeError`: Если модель не обучена.


## Шаги по обучению

1. **Запуск бота**: Убедитесь, что ваш бот запущен и подключен к Discord.
2. **Приглашение бота**: Пригласите бота на сервер Discord.
3. **Подготовка данных**: Подготовьте данные для обучения в виде текста или файла.
4. **Обучение модели**: Используйте команду `!train` с текстовыми данными или с файлом, прикрепив его к сообщению.
5. **Мониторинг обучения**: Следите за сообщениями бота о статусе обучения.
6. **Тестирование модели**: Используйте команду `!test` с данными для тестирования.
7. **Управление данными**: Используйте команды `!archive` и `!select_dataset` для управления файлами и наборами данных.


## Дополнительная информация

Подробнее о работе с данными и командами см. раздел "Команды".