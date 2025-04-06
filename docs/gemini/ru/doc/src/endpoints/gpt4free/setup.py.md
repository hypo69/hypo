# Модуль установки g4f

## Обзор

Этот модуль используется для установки библиотеки `g4f` (gpt4free) с использованием `setuptools`. Он определяет зависимости, дополнительные требования и точки входа для консольных скриптов.

## Подробней

Этот файл содержит конфигурацию для установки пакета `g4f`. Он использует `setuptools` для определения зависимостей, дополнительных требований и точек входа для консольных скриптов. Также он читает `README.md` для использования в качестве подробного описания пакета. Расположение этого файла указывает на то, что он является частью процесса сборки и публикации пакета `g4f`.

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

**Назначение**: Конфигурирует и выполняет установку пакета `g4f`.

**Параметры**:

- `name` (str): Имя пакета (`g4f`).
- `version` (str): Версия пакета, извлекается из переменной окружения `G4F_VERSION`.
- `author` (str): Автор пакета (`Tekky`).
- `author_email` (str): Email автора (`<support@g4f.ai>`).
- `description` (str): Краткое описание пакета (DESCRIPTION).
- `long_description_content_type` (str): Тип контента для подробного описания (`text/markdown`).
- `long_description` (str): Подробное описание пакета, загруженное из файла `README.md`.
- `packages` (list): Список пакетов, которые нужно включить, найденные с помощью `find_packages()`.
- `package_data` (dict): Дополнительные файлы, которые нужно включить в пакет.
- `include_package_data` (bool): Если `True`, включает все файлы, указанные в `package_data`.
- `install_requires` (list): Список основных зависимостей, необходимых для установки пакета.
- `extras_require` (dict): Словарь дополнительных зависимостей, разделенных по категориям (`all`, `slim`, `image`, `webview`, `api`, `gui`, `search`, `local`, `files`).
- `entry_points` (dict): Определяет точки входа для консольных скриптов (`g4f=g4f.cli:main`).
- `url` (str): URL репозитория GitHub.
- `project_urls` (dict): Словарь URL для различных ресурсов проекта (исходный код, трекер ошибок).
- `keywords` (list): Список ключевых слов, связанных с пакетом.
- `classifiers` (list): Список классификаторов, описывающих пакет.

**Возвращает**:

- Ничего явно не возвращает, но функция выполняет установку пакета.

**Вызывает исключения**:

- Возможные исключения, возникающие при ошибках во время установки пакета.

**Как работает функция**:

1.  Чтение файла `README.md` для получения подробного описания пакета.
2.  Определение основных зависимостей (`INSTALL_REQUIRE`) и дополнительных зависимостей (`EXTRA_REQUIRE`).
3.  Настройка установки пакета с использованием `setuptools.setup()`, включая имя, версию, автора, описание, зависимости и другие метаданные.
4.  Определение точки входа для консольного скрипта `g4f`.

```
A: Чтение README.md
|
B: Определение зависимостей
|
C: Настройка установки пакета
|
D: Выполнение установки пакета
```

**Примеры**:

```python
# Пример вызова setup() с минимальными параметрами
setup(
    name='g4f',
    version='1.0.0',
    packages=find_packages(),
)

# Пример вызова setup() с дополнительными зависимостями
setup(
    name='g4f',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['requests', 'aiohttp'],
)

# Пример вызова setup() с определением консольного скрипта
setup(
    name='g4f',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['g4f=g4f.cli:main'],
    },
)