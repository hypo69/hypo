# Модуль setup.py для gpt4free

## Обзор

Этот модуль используется для установки и настройки пакета `g4f` (gpt4free). Он определяет зависимости, дополнительные компоненты, точки входа и метаданные, необходимые для распространения и установки пакета.

## Подробней

Этот файл является скриптом установки, который использует `setuptools` для сборки и установки пакета `g4f`. Он выполняет следующие задачи:

1.  Чтение файла `README.md` для получения длинного описания пакета.
2.  Определение списка необходимых зависимостей (`INSTALL_REQUIRE`).
3.  Определение дополнительных наборов зависимостей (`EXTRA_REQUIRE`) для различных функций, таких как работа с изображениями, веб-интерфейсом, API, графическим интерфейсом, поиском, локальными моделями и файлами.
4.  Настройка метаданных пакета, таких как имя, версия, автор, описание, URL, ключевые слова и классификаторы.
5.  Определение точек входа (entry points) для консольных скриптов.

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

**Назначение**: Настраивает установку пакета `g4f`.

**Параметры**:

*   `name` (str): Имя пакета.
*   `version` (str): Версия пакета, полученная из переменной окружения `G4F_VERSION`.
*   `author` (str): Имя автора пакета.
*   `author_email` (str): Email автора пакета.
*   `description` (str): Краткое описание пакета.
*   `long_description_content_type` (str): Тип контента длинного описания (в данном случае, `text/markdown`).
*   `long_description` (str): Длинное описание пакета, полученное из файла `README.md`.
*   `packages` (list): Список пакетов, которые нужно включить в установку, найденных с помощью `find_packages()`.
*   `package_data` (dict): Дополнительные файлы, которые нужно включить в пакет.
*   `include_package_data` (bool): Если `True`, включает все файлы, соответствующие шаблонам в `package_data`.
*   `install_requires` (list): Список необходимых зависимостей для установки пакета.
*   `extras_require` (dict): Словарь дополнительных зависимостей, разделенных по категориям.
*   `entry_points` (dict): Словарь точек входа, определяющих консольные скрипты.
*   `url` (str): URL репозитория пакета.
*   `project_urls` (dict): Словарь URL, связанных с проектом, таких как URL исходного кода и URL отслеживания ошибок.
*   `keywords` (list): Список ключевых слов, связанных с пакетом.
*   `classifiers` (list): Список классификаторов, описывающих пакет.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:

1.  Функция `setup` вызывается для настройки процесса установки пакета `g4f`.
2.  Она определяет метаданные пакета, такие как имя, версия, автор и описание.
3.  Она находит все пакеты, которые нужно включить в установку, с помощью функции `find_packages()`.
4.  Она определяет список необходимых зависимостей и дополнительных зависимостей для различных функций.
5.  Она определяет точки входа для консольных скриптов, позволяя запускать скрипты из командной строки.
6.  Она определяет URL репозитория пакета и другие URL, связанные с проектом.
7.  Она определяет список ключевых слов и классификаторов, описывающих пакет.

**Примеры**:

```python
# Пример вызова функции setup
setup(
    name='g4f',
    version='1.0.0',
    author='Tekky',
    author_email='<support@g4f.ai>',
    description='The official gpt4free repository',
    long_description='...',
    packages=['g4f'],
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

**Описание**: Абсолютный путь к директории, в которой находится текущий файл (`setup.py`).
Используется для определения местоположения других файлов, таких как `README.md`.

### `long_description`

```python
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

long_description = long_description.replace("[!NOTE]", "")
long_description = long_description.replace("(docs/images/", "(https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/images/")
long_description = long_description.replace("(docs/", "(https://github.com/xtekky/gpt4free/blob/main/docs/")
```

**Описание**:  Содержимое файла `README.md`, которое используется как длинное описание пакета.  
Код открывает файл `README.md`, читает его содержимое и выполняет замену определенных строк в содержимом файла.

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

**Описание**: Список основных зависимостей, необходимых для установки пакета `g4f`.

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

**Описание**: Словарь, определяющий дополнительные зависимости для различных компонентов и функций пакета `g4f`.  
Например, зависимости для работы с изображениями, веб-интерфейсом и т.д.

### `DESCRIPTION`

```python
DESCRIPTION = (
    'The official gpt4free repository | various collection of powerful language models'
)
```

**Описание**: Краткое описание пакета `g4f`.