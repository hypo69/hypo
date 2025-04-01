# Модуль setup.py для gpt4free
## Обзор

Модуль `setup.py` используется для сборки, распространения и установки пакета `gpt4free`. Он содержит метаданные о пакете, такие как имя, версия, автор, описание, зависимости и другие. Этот файл позволяет упростить процесс установки и управления зависимостями для проекта `gpt4free`.

## Подробней

Файл `setup.py` выполняет следующие функции:

1.  Определение метаданных пакета: включая имя, версию, автора, адрес электронной почты, описание и URL проекта.
2.  Чтение длинного описания из файла `README.md` и его форматирование.
3.  Определение зависимостей пакета, как обязательных (`INSTALL_REQUIRE`), так и дополнительных (`EXTRA_REQUIRE`).
4.  Указание пакетов, которые необходимо включить в дистрибутив (`find_packages()`).
5.  Определение дополнительных данных пакета, таких как файлы интерфейса и модели.
6.  Создание точки входа для консольной команды `g4f` через `entry_points`.
7.  Определение ключевых слов и классификаторов для PyPI.

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

**Назначение**: Конфигурирует и запускает процесс сборки и установки пакета.

**Параметры**:

*   `name` (str): Имя пакета (`g4f`).
*   `version` (str): Версия пакета, полученная из переменной окружения `G4F_VERSION`.
*   `author` (str): Имя автора пакета (`Tekky`).
*   `author_email` (str): Адрес электронной почты автора (`<support@g4f.ai>`).
*   `description` (str): Краткое описание пакета, хранящееся в переменной `DESCRIPTION`.
*   `long_description_content_type` (str): Тип контента длинного описания (`text/markdown`).
*   `long_description` (str): Длинное описание пакета, считанное из файла `README.md`.
*   `packages` (list): Список пакетов, которые необходимо включить в дистрибутив, полученный с помощью `find_packages()`.
*   `package_data` (dict): Словарь, определяющий дополнительные файлы, которые должны быть включены в пакет.
*   `include_package_data` (bool): Если `True`, включает все файлы, соответствующие шаблонам в `package_data`.
*   `install_requires` (list): Список обязательных зависимостей пакета.
*   `extras_require` (dict): Словарь, определяющий дополнительные группы зависимостей.
*   `entry_points` (dict): Словарь, определяющий точки входа для консольных команд.
*   `url` (str): URL репозитория проекта (`https://github.com/xtekky/gpt4free`).
*   `project_urls` (dict): Словарь, содержащий ссылки на исходный код и систему отслеживания ошибок.
*   `keywords` (list): Список ключевых слов, описывающих пакет.
*   `classifiers` (list): Список классификаторов, описывающих целевую аудиторию и операционные системы.

**Как работает функция**:

1.  **Настройка метаданных**: Определяются основные параметры пакета, такие как имя, версия, автор и описание.
2.  **Чтение описания**: Считывается подробное описание из файла `README.md`, которое будет отображаться на странице пакета в PyPI.
3.  **Определение зависимостей**: Указываются все необходимые зависимости, которые будут установлены вместе с пакетом.
4.  **Определение пакетов**: Находятся все пакеты в проекте, которые необходимо включить в дистрибутив.
5.  **Настройка дополнительных данных**: Указываются дополнительные файлы, такие как модели и ресурсы интерфейса, которые должны быть включены в пакет.
6.  **Создание точек входа**: Определяется консольная команда `g4f`, которая будет доступна после установки пакета.
7.  **Указание URL проекта**: Определяются ссылки на репозиторий проекта и систему отслеживания ошибок.
8.  **Определение ключевых слов и классификаторов**: Указываются ключевые слова и классификаторы, которые помогут пользователям найти пакет в PyPI.

**Примеры**:

```python
setup(
    name='g4f',
    version='0.1.0',
    author='Tekky',
    author_email='<support@g4f.ai>',
    description='The official gpt4free repository',
    long_description_content_type='text/markdown',
    long_description='A collection of powerful language models',
    packages=find_packages(),
    install_requires=['requests', 'aiohttp'],
    entry_points={
        'console_scripts': ['g4f=g4f.cli:main'],
    },
    url='https://github.com/xtekky/gpt4free',
)
```

## Переменные

### `here`

```python
here = os.path.abspath(os.path.dirname(__file__))
```

**Назначение**: Абсолютный путь к директории, в которой находится файл `setup.py`.

**Как работает**:
Функция `os.path.dirname(__file__)` возвращает путь к директории, содержащей текущий файл (`setup.py`). Затем `os.path.abspath()` преобразует этот путь в абсолютный.

### `long_description`

```python
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

long_description = long_description.replace("[!NOTE]", "")
long_description = long_description.replace("(docs/images/", "(https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/images/")
long_description = long_description.replace("(docs/", "(https://github.com/xtekky/gpt4free/blob/main/docs/")
```

**Назначение**: Длинное описание пакета, считанное из файла `README.md` и отформатированное для отображения на странице пакета в PyPI.

**Как работает**:

1.  **Чтение файла**: Файл `README.md` открывается с использованием кодировки UTF-8, и его содержимое считывается в переменную `long_description`.
2.  **Удаление заметок**: Заменяет строку "[!NOTE]" на пустую строку.
3.  **Замена путей к изображениям и документам**: Заменяются относительные пути к изображениям и документам на абсолютные URL-адреса, чтобы они корректно отображались на странице пакета в PyPI.

### `INSTALL_REQUIRE`

```python
INSTALL_REQUIRE = [
    "requests",
    "aiohttp",
    "brotli",
    "pycryptodome",
    "nest_asyncio",
]
```

**Назначение**: Список обязательных зависимостей пакета.

**Описание**:
Содержит перечень пакетов Python, которые необходимо установить вместе с `gpt4free`.

### `EXTRA_REQUIRE`

```python
EXTRA_REQUIRE = {
    'all': [
        "curl_cffi>=0.6.2",
        "certifi",
        "browser_cookie3",         # get_cookies
        "duckduckgo-search>=5.0",  # internet.search
        "beautifulsoup4",          # internet.search and bing.create_images
        "platformdirs",
        "aiohttp_socks",           # proxy
        "pillow",                  # image
        "cairosvg",                # svg image
        "werkzeug", "flask",       # gui
        "fastapi",                 # api
        "uvicorn",                 # api
        "nodriver",
        "python-multipart",
        "pywebview",
        "plyer",
        "setuptools",
        "pypdf2", # files
        "python-docx",
        "odfpy",
        "ebooklib",
        "openpyxl",
    ],
    'slim': [
        "curl_cffi>=0.6.2",
        "certifi",
        "browser_cookie3",
        "duckduckgo-search>=5.0"  ,# internet.search
        "beautifulsoup4",          # internet.search and bing.create_images
        "aiohttp_socks",           # proxy
        "pillow",                  # image
        "werkzeug", "flask",       # gui
        "fastapi",                 # api
        "uvicorn",                 # api
        "python-multipart",
        "pypdf2", # files
        "python-docx",
    ],
    "image": [
        "pillow",
        "cairosvg",
        "beautifulsoup4"
    ],
    "webview": [
        "pywebview",
        "platformdirs",
        "plyer",
        "cryptography",
    ],
    "api": [
        "loguru", "fastapi",
        "uvicorn",
        "python-multipart",
    ],
    "gui": [
        "werkzeug", "flask",
        "beautifulsoup4", "pillow",
        "duckduckgo-search>=5.0",
    ],
    "search": [
        "beautifulsoup4",
        "pillow",
        "duckduckgo-search>=5.0",
    ],
    "local": [
        "gpt4all"
    ],
    "files": [
        "spacy",
        "beautifulsoup4",
        "pypdf2",
        "python-docx",
        "odfpy",
        "ebooklib",
        "openpyxl",
    ]
}
```

**Назначение**: Словарь, определяющий дополнительные группы зависимостей.

**Описание**:
Позволяет устанавливать дополнительные зависимости в зависимости от конкретных потребностей пользователя.

### `DESCRIPTION`

```python
DESCRIPTION = (
    'The official gpt4free repository | various collection of powerful language models'
)
```

**Назначение**: Краткое описание пакета.

**Описание**:
Используется для предоставления краткой информации о пакете.

## Дополнительная информация

Данный файл `setup.py` играет важную роль в экосистеме Python, так как он позволяет стандартизировать процесс установки и распространения пакетов. Подробное описание зависимостей и метаданных облегчает использование пакета `gpt4free` другими разработчиками.