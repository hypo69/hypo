# Модуль установки g4f

## Обзор

Модуль `setup.py` используется для установки библиотеки `g4f`. Он определяет метаданные пакета, зависимости и точки входа.

## Подробнее

Этот файл использует `setuptools` для сборки, распространения и установки пакета `g4f`. Включает чтение файла `README.md` для получения длинного описания, определение зависимостей и дополнительных требований, а также настройку метаданных пакета, таких как имя, версия, автор и URL-адреса проекта.

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

**Назначение**: Настраивает и выполняет установку пакета `g4f`.

**Параметры**:

-   `name` (str): Имя пакета (`g4f`).
-   `version` (str): Версия пакета, извлекаемая из переменной окружения `G4F_VERSION`.
-   `author` (str): Автор пакета (`Tekky`).
-   `author_email` (str): Электронная почта автора (`<support@g4f.ai>`).
-   `description` (str): Краткое описание пакета.
-   `long_description_content_type` (str): Тип контента для длинного описания (`text/markdown`).
-   `long_description` (str): Длинное описание пакета, загруженное из файла `README.md`.
-   `packages` (list): Список пакетов, найденных с помощью `find_packages()`.
-   `package_data` (dict): Дополнительные файлы, включенные в пакет.
-   `include_package_data` (bool): Флаг, указывающий, нужно ли включать данные пакета.
-   `install_requires` (list): Список необходимых зависимостей для установки пакета.
-   `extras_require` (dict): Словарь дополнительных требований для различных функций.
-   `entry_points` (dict): Точки входа для консольных скриптов.
-   `url` (str): URL-адрес репозитория GitHub.
-   `project_urls` (dict): Словарь URL-адресов проекта, таких как репозиторий и трекер ошибок.
-   `keywords` (list): Список ключевых слов, описывающих пакет.
-   `classifiers` (list): Список классификаторов, описывающих пакет.

**Возвращает**:

-   `None`

**Как работает функция**:

1.  Устанавливает имя пакета `g4f`.
2.  Получает версию пакета из переменной окружения `G4F_VERSION`.
3.  Устанавливает автора и его электронную почту.
4.  Определяет краткое описание пакета.
5.  Указывает тип контента для длинного описания как `text/markdown`.
6.  Загружает длинное описание из файла `README.md`.
7.  Находит все пакеты в директории с помощью `find_packages()`.
8.  Включает дополнительные файлы в пакет, такие как файлы в директориях `g4f/interference/`, `g4f/gui/client/`, `g4f/gui/server/`, `g4f/Provider/npm/` и `g4f/local/models/`.
9.  Включает данные пакета.
10. Определяет список необходимых зависимостей для установки пакета.
11. Определяет дополнительные требования для различных функций, такие как `all`, `slim`, `image`, `webview`, `api`, `gui`, `search`, `local` и `files`.
12. Устанавливает точку входа для консольного скрипта `g4f`, который вызывает функцию `main` из модуля `g4f.cli`.
13. Указывает URL-адрес репозитория GitHub.
14. Определяет URL-адреса проекта, такие как репозиторий и трекер ошибок.
15. Указывает список ключевых слов, описывающих пакет.
16. Устанавливает классификаторы, описывающие пакет, такие как статус разработки, целевая аудитория, язык программирования и операционные системы.

```
setup
↓
Получение версии из переменной окружения
↓
Чтение long_description из файла
↓
Определение зависимостей и дополнительных требований
↓
Настройка метаданных пакета
↓
Вызов setuptools.setup()
```

**Примеры**:

```python
# Пример вызова функции setup с минимальным набором параметров
setup(
    name='g4f',
    version='1.0.0',
    packages=find_packages(),
)

# Пример вызова функции setup с полным набором параметров
setup(
    name='g4f',
    version='1.0.0',
    author='Tekky',
    author_email='<support@g4f.ai>',
    description='The official gpt4free repository',
    long_description_content_type='text/markdown',
    long_description='Long description',
    packages=find_packages(),
    package_data={
        'g4f': ['g4f/interference/*', 'g4f/gui/client/*', 'g4f/gui/server/*', 'g4f/Provider/npm/*', 'g4f/local/models/*']
    },
    include_package_data=True,
    install_requires=['requests', 'aiohttp'],
    extras_require={
        'all': ['curl_cffi>=0.6.2', 'certifi']
    },
    entry_points={
        'console_scripts': ['g4f=g4f.cli:main'],
    },
    url='https://github.com/xtekky/gpt4free',
    project_urls={
        'Source Code': 'https://github.com/xtekky/gpt4free',
        'Bug Tracker': 'https://github.com/xtekky/gpt4free/issues',
    },
    keywords=['python', 'chatbot'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
)