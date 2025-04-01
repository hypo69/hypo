# Модуль установки g4f

## Обзор

Этот модуль используется для настройки и установки пакета `g4f`, который представляет собой коллекцию различных мощных языковых моделей. Он автоматизирует процесс установки, определения зависимостей и создания исполняемых скриптов.

## Подробнее

Модуль `setup.py` является стандартным файлом для сборки, упаковки и установки пакетов Python. В данном случае, он используется для пакета `g4f`, который, судя по описанию, предоставляет интерфейс к различным языковым моделям.
Этот скрипт выполняет следующие задачи:

- Чтение и обработка файла `README.md` для получения длинного описания пакета.
- Определение зависимостей пакета, как обязательных (`INSTALL_REQUIRE`), так и дополнительных (`EXTRA_REQUIRE`).
- Настройка пакета с использованием `setuptools.setup`, включая имя, версию, автора, описание, зависимости и другие метаданные.
- Создание точки входа для консольной команды `g4f`.

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

**Назначение**: Функция `setup` из `setuptools` используется для настройки процесса установки пакета. Она принимает различные аргументы, определяющие метаданные пакета, зависимости, точки входа и другие параметры.

**Параметры**:

-   `name` (str): Имя пакета (`g4f`).
-   `version` (str): Версия пакета, извлекается из переменной окружения `G4F_VERSION`.
-   `author` (str): Автор пакета (`Tekky`).
-   `author_email` (str): Email автора пакета (`<support@g4f.ai>`).
-   `description` (str): Краткое описание пакета (`DESCRIPTION`).
-   `long_description_content_type` (str): Тип контента для длинного описания (`text/markdown`).
-   `long_description` (str): Длинное описание пакета, прочитанное из файла `README.md`.
-   `packages` (list): Список пакетов, которые нужно включить, найденных с помощью `find_packages()`.
-   `package_data` (dict): Дополнительные файлы, которые нужно включить в пакет.
-   `include_package_data` (bool): Если `True`, включает все файлы, указанные в `package_data`.
-   `install_requires` (list): Список обязательных зависимостей пакета.
-   `extras_require` (dict): Словарь дополнительных зависимостей пакета, разделенных по категориям.
-   `entry_points` (dict): Словарь точек входа, определяющих консольные скрипты и другие расширения.
-   `url` (str): URL репозитория пакета на GitHub.
-   `project_urls` (dict): Словарь URL, содержащий ссылки на исходный код и систему отслеживания ошибок.
-   `keywords` (list): Список ключевых слов, описывающих пакет.
-   `classifiers` (list): Список классификаторов, описывающих целевую аудиторию, операционные системы и языки программирования.

**Возвращает**:

-   `None`

**Вызывает исключения**:

-   `OSError`: Если не удается прочитать файл `README.md`.

**Как работает функция**:

1.  Определяются основные параметры пакета, такие как имя, версия, автор и описание.
2.  Извлекается длинное описание пакета из файла `README.md` и выполняется замена некоторых строк в этом описании.
3.  Определяются зависимости пакета, как обязательные, так и дополнительные.
4.  Настраивается пакет с использованием функции `setup` из `setuptools`, передавая ей все необходимые параметры.
5.  Определяется точка входа для консольной команды `g4f`, которая указывает на функцию `main` в модуле `g4f.cli`.
6.  Указываются URL для репозитория пакета и системы отслеживания ошибок.
7.  Определяются ключевые слова и классификаторы, описывающие пакет.

**Примеры**:

Пример вызова функции `setup`:

```python
setup(
    name='g4f',
    version='1.0.0',
    author='Tekky',
    author_email='support@g4f.ai',
    description='The official gpt4free repository',
    long_description='...',
    packages=find_packages(),
    install_requires=['requests', 'aiohttp'],
    entry_points={'console_scripts': ['g4f=g4f.cli:main']},
    url='https://github.com/xtekky/gpt4free',
)
```
```python
def find_packages(where: str = ".") -> list[str]:
    """
    Find all packages in a directory.
    """
```

**Назначение**: Находит все пакеты в указанной директории.

**Параметры**:

-   `where` (str, optional): Директория, в которой нужно искать пакеты. По умолчанию "." (текущая директория).

**Возвращает**:

-   `list[str]`: Список имен найденных пакетов.

**Как работает функция**:

1.  Использует `setuptools.find_packages` для поиска всех пакетов в указанной директории.
2.  Возвращает список имен найденных пакетов.

**Примеры**:

Пример использования функции `find_packages`:

```python
packages = find_packages()
print(packages)
# ['g4f', 'g4f.cli', 'g4f.Provider']
```

## Переменные

-   `here` (str): Абсолютный путь к директории, в которой находится файл `setup.py`.
-   `long_description` (str): Длинное описание пакета, прочитанное из файла `README.md`.
-   `INSTALL_REQUIRE` (list): Список обязательных зависимостей пакета.
-   `EXTRA_REQUIRE` (dict): Словарь дополнительных зависимостей пакета, разделенных по категориям.
-   `DESCRIPTION` (str): Краткое описание пакета.