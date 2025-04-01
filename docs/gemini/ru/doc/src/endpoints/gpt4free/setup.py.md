# Модуль установки g4f

## Обзор

Этот модуль используется для установки библиотеки `g4f` (gpt4free) с помощью `setuptools`. Он определяет зависимости, дополнительные требования и метаданные проекта, такие как имя, версия, автор, описание и URL-адреса репозитория.

## Подробнее

Модуль `setup.py` является стандартным файлом для проектов Python, использующих `setuptools`. Он содержит метаданные о проекте, такие как имя, версия, автор, описание и зависимости. Этот файл позволяет легко устанавливать, распространять и управлять проектом. В данном случае, он используется для установки библиотеки `g4f`, которая предоставляет доступ к различным моделям обработки языка.

## Функции

### `setup`

```python
setup(
    name='g4f',
    version=os.environ.get("G4F_VERSION"),
    author='Tekky',
    author_email='<support@g4f.ai>',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    package_data={
        'g4f': ['g4f/interference/*', 'g4f/gui/client/*', 'g4f/gui/server/*', 'g4f/Provider/npm/*', 'g4f/local/models/*']
    },
    include_package_data=True,
    install_requires=INSTALL_REQUIRE,
    extras_require=EXTRA_REQUIRE,
    entry_points={
        'console_scripts': ['g4f=g4f.cli:main'],
    },
    url='https://github.com/xtekky/gpt4free',  # Link to your GitHub repository
    project_urls={
        'Source Code': 'https://github.com/xtekky/gpt4free',  # GitHub link
        'Bug Tracker': 'https://github.com/xtekky/gpt4free/issues',  # Link to issue tracker
    },
    keywords=[
        'python',
        'chatbot',
        'reverse-engineering',
        'openai',
        'chatbots',
        'gpt',
        'language-model',
        'gpt-3',
        'gpt3',
        'openai-api',
        'gpt-4',
        'gpt4',
        'chatgpt',
        'chatgpt-api',
        'openai-chatgpt',
        'chatgpt-free',
        'chatgpt-4',
        'chatgpt4',
        'chatgpt4-api',
        'free',
        'free-gpt',
        'gpt4free',
        'g4f',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
)
```

**Назначение**: Настройка и выполнение установки пакета `g4f`.

**Параметры**:
- `name` (str): Имя пакета (`g4f`).
- `version` (str): Версия пакета, извлекается из переменной окружения `G4F_VERSION`.
- `author` (str): Имя автора (`Tekky`).
- `author_email` (str): Email автора (`<support@g4f.ai>`).
- `description` (str): Краткое описание пакета (определяется переменной `DESCRIPTION`).
- `long_description_content_type` (str): Тип контента для длинного описания (`text/markdown`).
- `long_description` (str): Длинное описание пакета, считывается из файла `README.md`.
- `packages` (list): Список пакетов, которые будут включены (`find_packages()`).
- `package_data` (dict): Дополнительные файлы, которые будут включены в пакет.
- `include_package_data` (bool): Включать ли данные пакета, указанные в `MANIFEST.in`.
- `install_requires` (list): Список необходимых зависимостей для установки.
- `extras_require` (dict): Словарь дополнительных зависимостей, разделенных по категориям (например, `all`, `slim`, `image`).
- `entry_points` (dict): Определяет точки входа, такие как консольные скрипты.
- `url` (str): URL репозитория проекта.
- `project_urls` (dict): Словарь URL-адресов проекта, таких как репозиторий исходного кода и трекер ошибок.
- `keywords` (list): Список ключевых слов, связанных с пакетом.
- `classifiers` (list): Список классификаторов, описывающих проект (статус разработки, аудитория, язык программирования, операционные системы).

**Возвращает**:
- None

**Вызывает исключения**:
- None

**Как работает функция**:

1.  **Чтение `README.md`**: Читает содержимое файла `README.md`, который содержит подробное описание проекта.
2.  **Настройка длинного описания**: Заменяет определенные строки в длинном описании для корректного отображения ссылок на изображения и документацию в репозитории GitHub.
3.  **Определение зависимостей**: Определяет список необходимых зависимостей (`INSTALL_REQUIRE`) и дополнительных зависимостей (`EXTRA_REQUIRE`). Дополнительные зависимости разделены по категориям, таким как `all`, `slim`, `image`, `webview`, `api`, `gui`, `search`, `local` и `files`.
4.  **Вызов `setup`**: Вызывает функцию `setup` из `setuptools` с указанными параметрами. Эта функция выполняет установку пакета, учитывая все зависимости и метаданные.
5.  **Указание точек входа**: Определяет точку входа для консольного скрипта `g4f`, который будет запускать функцию `main` из модуля `g4f.cli`.

**ASCII flowchart**:

```
A [Чтение README.md]
|
B [Настройка long_description]
|
C [Определение INSTALL_REQUIRE]
|
D [Определение EXTRA_REQUIRE]
|
E [Вызов setup(...)]
```

**Примеры**:

1.  Установка пакета с минимальными зависимостями:

    ```bash
    python setup.py install
    ```

2.  Установка пакета со всеми дополнительными зависимостями:

    ```bash
    python setup.py install --extras-require all
    ```

3.  Установка пакета с зависимостями для работы с изображениями:

    ```bash
    python setup.py install --extras-require image
    ```

## Переменные

- `here`: Абсолютный путь к каталогу, в котором находится файл `setup.py`.
- `long_description`: Длинное описание проекта, прочитанное из файла `README.md`.
- `INSTALL_REQUIRE`: Список основных зависимостей, необходимых для установки пакета.
- `EXTRA_REQUIRE`: Словарь дополнительных зависимостей, которые могут быть установлены в зависимости от потребностей пользователя.
- `DESCRIPTION`: Краткое описание проекта.