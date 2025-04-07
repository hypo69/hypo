# Модуль установки g4f

## Обзор

Этот модуль содержит скрипт установки для библиотеки g4f, предназначенной для работы с различными мощными языковыми моделями. Он определяет параметры установки, зависимости и дополнительные компоненты, необходимые для функционирования библиотеки.

## Подробнее

Этот скрипт установки использует `setuptools` для сборки и установки пакета `g4f`. Он включает в себя чтение файла `README.md` для получения подробного описания проекта, определение зависимостей, дополнительных требований и точек входа для консольных скриптов.

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

**Назначение**: Функция `setup` из `setuptools` используется для настройки процесса установки пакета `g4f`. Она определяет метаданные пакета, такие как имя, версия, автор, описание, зависимости и точки входа.

**Параметры**:
- `name` (str): Имя пакета (`g4f`).
- `version` (str): Версия пакета, полученная из переменной окружения `G4F_VERSION`.
- `author` (str): Автор пакета (`Tekky`).
- `author_email` (str): Email автора (`<support@g4f.ai>`).
- `description` (str): Краткое описание пакета (DESCRIPTION).
- `long_description_content_type` (str): Тип контента для `long_description` (`text/markdown`).
- `long_description` (str): Подробное описание пакета, прочитанное из файла `README.md`.
- `packages` (list): Список пакетов, которые будут включены в установку, найденных с помощью `find_packages()`.
- `package_data` (dict): Дополнительные файлы, которые будут включены в пакет.
- `include_package_data` (bool): Если `True`, включает все файлы, соответствующие шаблонам в `package_data`.
- `install_requires` (list): Список необходимых зависимостей для установки пакета.
- `extras_require` (dict): Словарь дополнительных зависимостей, которые могут быть установлены вместе с пакетом.
- `entry_points` (dict): Определяет точки входа для консольных скриптов.
- `url` (str): URL репозитория проекта на GitHub.
- `project_urls` (dict): Словарь URL для различных ресурсов проекта, таких как исходный код и трекер ошибок.
- `keywords` (list): Список ключевых слов, описывающих пакет.
- `classifiers` (list): Список классификаторов, описывающих целевую аудиторию, язык программирования и операционные системы.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Возможные исключения, связанные с процессом установки `setuptools`, такие как ошибки при чтении файлов или несовместимости зависимостей.

**Как работает функция**:

1. **Определение метаданных пакета**:
   - Функция начинает с определения основных метаданных пакета, таких как имя, версия, автор и описание.
   - Версия пакета извлекается из переменной окружения `G4F_VERSION`.

2. **Чтение подробного описания**:
   - Подробное описание пакета считывается из файла `README.md` и сохраняется в переменной `long_description`.
   - В описании заменяются некоторые строки, чтобы корректно отображать ссылки на изображения и документацию в репозитории GitHub.

3. **Определение зависимостей**:
   - Функция определяет основные зависимости пакета в списке `INSTALL_REQUIRE`.
   - Дополнительные зависимости, которые могут быть установлены вместе с пакетом, определены в словаре `EXTRA_REQUIRE`.

4. **Настройка `setuptools`**:
   - Функция вызывает `setuptools.setup()` с передачей всех определенных метаданных и зависимостей.
   - `setuptools` использует эту информацию для сборки и установки пакета.

5. **Определение точек входа**:
   - Функция определяет точку входа для консольного скрипта `g4f`, которая указывает на функцию `main` в модуле `g4f.cli`.
   - Это позволяет запускать скрипт `g4f` из командной строки после установки пакета.

```mermaid
graph TD
    A[Определение метаданных пакета] --> B{Чтение подробного описания из README.md};
    B --> C{Определение зависимостей};
    C --> D{Вызов setuptools.setup()};
    D --> E[Определение точек входа для консольных скриптов];
    E --> F[Завершение установки];
```

**Примеры**:

```python
# Пример вызова функции setup с минимальными параметрами
setup(
    name='g4f',
    version='1.0.0',
    packages=find_packages(),
)

# Пример вызова функции setup с расширенными параметрами
setup(
    name='g4f',
    version='1.0.0',
    author='Tekky',
    author_email='support@g4f.ai',
    description='Library for language models',
    long_description='Detailed description of the library',
    packages=find_packages(),
    install_requires=['requests', 'aiohttp'],
    entry_points={'console_scripts': ['g4f=g4f.cli:main']},
)