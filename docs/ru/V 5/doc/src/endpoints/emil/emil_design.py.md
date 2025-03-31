# Модуль `emil_design`

## Обзор

Модуль `emil_design` предназначен для управления и обработки изображений, а также для их продвижения на платформах Facebook и PrestaShop. Он включает в себя функции для описания изображений с использованием AI, загрузки описаний продуктов в PrestaShop и публикации рекламных сообщений в Facebook.

## Подробней

Этот модуль играет важную роль в автоматизации процессов, связанных с созданием контента для e-commerce платформ и социальных сетей. Он использует AI для генерации описаний изображений, что позволяет сократить время на подготовку материалов для продуктов. Модуль также автоматизирует загрузку информации о продуктах в PrestaShop, что уменьшает вероятность ошибок и экономит ресурсы.

## Классы

### `Config`

**Описание**: Класс `Config` предназначен для хранения конфигурационных параметров, необходимых для работы модуля `EmilDesign`. Он содержит информацию о конечной точке API, режиме работы (dev, dev8 или production), формате POST-запросов, а также ключи API и домены для PrestaShop.

**Как работает класс**:
Класс `Config` определяет статические атрибуты, которые используются для настройки соединения с API PrestaShop. В зависимости от значения переменной `USE_ENV`, он либо загружает значения из переменных окружения, либо использует значения, сохраненные в файле конфигурации `gs.credentials`. Это позволяет легко переключаться между разными окружениями (разработка, тестирование, production) без изменения кода.

- `ENDPOINT` (str): Конечная точка API (значение: 'emil').
- `MODE` (str): Режим работы ('dev').
- `POST_FORMAT` (str): Формат POST-запросов ('JSON').
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

### `EmilDesign`

**Описание**: Класс `EmilDesign` является основным классом модуля, который предоставляет функциональность для описания и продвижения изображений на различных платформах, таких как PrestaShop и Facebook. Он использует модели AI (Gemini и OpenAI) для генерации описаний изображений и автоматизирует процесс загрузки этих описаний в PrestaShop.

**Как работает класс**:
Класс `EmilDesign` инициализирует необходимые параметры и объекты для работы с AI-моделями, API PrestaShop и Facebook. Он содержит методы для описания изображений с использованием Gemini и OpenAI, загрузки информации о продуктах в PrestaShop и продвижения изображений на Facebook. Класс также управляет путями к файлам конфигурации, инструкциям и изображениям.

**Методы**:
- `describe_images`: Описывает изображения на основе предоставленных инструкций и примеров.
- `promote_to_facebook`: Продвигает изображения и их описания на Facebook.
- `upload_described_products_to_prestashop`: Загружает информацию о продуктах в PrestaShop.

**Параметры**:
- `gemini` (Optional[GoogleGenerativeAI]): Экземпляр класса `GoogleGenerativeAI` для работы с моделью Gemini.
- `openai` (Optional[OpenAIModel]): Экземпляр класса `OpenAIModel` для работы с моделью OpenAI.
- `base_path` (Path): Базовый путь к файлам конфигурации и инструкциям.
- `config` (SimpleNamespace): Объект, содержащий параметры конфигурации из файла `emil.json`.
- `data_path` (Path): Путь к каталогу с данными (изображения, описания).
- `gemini_api` (str): Ключ API для доступа к Gemini.
- `presta_api` (str): Ключ API для доступа к PrestaShop.
- `presta_domain` (str): Домен API PrestaShop.

**Примеры**
```python
emil = EmilDesign()
emil.describe_images('he')
```

## Функции

### `describe_images`

```python
def describe_images(
    self,
    lang: str,
    models: dict = {
        'gemini': {'model_name': 'gemini-1.5-flash'},
        'openai': {'model_name': 'gpt-4o-mini', 'assistant_id': 'asst_uDr5aVY3qRByRwt5qFiMDk43'},
    },
) -> None:
    """Describe images based on the provided instruction and examples.

    Args:
        lang (str): Language for the description.
        models (dict, optional): Models configuration. Defaults to Gemini and OpenAI models.

    Returns:
        None

    Raises:
        FileNotFoundError: If instruction files are not found.
        Exception: If any error occurs during image processing.

    Example:
        >>> emil = EmilDesign()
        >>> emil.describe_images('he')
    """
    ...
```

**Описание**: Описывает изображения на основе предоставленных инструкций и примеров, используя модели Gemini и OpenAI.

**Как работает функция**:
Функция `describe_images` считывает системные инструкции и примеры описаний из файлов, расположенных в каталоге `instructions`. Она использует эти инструкции для генерации описаний изображений с помощью моделей Gemini и OpenAI. Сначала она загружает изображения из указанной директории, затем для каждого изображения генерирует описание, сохраняет описание в JSON-файл и добавляет путь к изображению в список обработанных изображений.

**Параметры**:
- `lang` (str): Язык, на котором нужно сгенерировать описание.
- `models` (dict, optional): Конфигурация моделей Gemini и OpenAI. По умолчанию используются модели `gemini-1.5-flash` и `gpt-4o-mini`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `FileNotFoundError`: Если не найдены файлы с инструкциями.
- `Exception`: Если произошла ошибка во время обработки изображения.

**Примеры**:
```python
emil = EmilDesign()
emil.describe_images('he')
```

### `promote_to_facebook`

```python
async def promote_to_facebook(self) -> None:
    """Promote images and their descriptions to Facebook.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If any error occurs during Facebook promotion.
    """
    ...
```

**Описание**: Продвигает изображения и их описания на Facebook.

**Как работает функция**:
Функция `promote_to_facebook` использует веб-драйвер для автоматизации процесса публикации сообщений в Facebook. Она открывает указанную группу Facebook, загружает описания изображений из JSON-файла и публикует каждое изображение с соответствующим описанием.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если произошла ошибка во время продвижения на Facebook.

### `upload_described_products_to_prestashop`

```python
def upload_described_products_to_prestashop(
    self, products_list: Optional[List[SimpleNamespace]] = None, id_lang: Optional[int | str] = 2, *args, **kwards
) -> bool:
    """Upload product information to PrestaShop.

    Args:
        products_list (Optional[List[SimpleNamespace]], optional): List of product info. Defaults to None.
        id_lang (Optional[str], optional): Language id for prestasop databases.
        Обычно я назначаю языки в таком порядке 1 - en;2 - he; 3 - ru. 
        Важно проверить порядок якыков целевой базе данных.
        >>import language
        >>lang_class = PrestaLanguage()
        >>print(lang_class.get_languages_schema())


    Returns:
        bool: True if upload succeeds, False otherwise.

    Raises:
        FileNotFoundError: If locales file is not found.
        Exception: If any error occurs during PrestaShop upload.
    """
    ...
```

**Описание**: Загружает информацию о продуктах в PrestaShop.

**Как работает функция**:
Функция `upload_described_products_to_prestashop` загружает информацию о продуктах в PrestaShop, используя API PrestaShop. Она считывает JSON-файлы, содержащие информацию о продуктах, и создает новые продукты в PrestaShop с использованием предоставленных данных. Функция также обрабатывает указание языка для загружаемых данных.

**Параметры**:
- `products_list` (Optional[List[SimpleNamespace]], optional): Список объектов `SimpleNamespace`, содержащих информацию о продуктах. По умолчанию `None`.
- `id_lang` (Optional[int  |  str], optional): Идентификатор языка для PrestaShop. По умолчанию `2` (иврит).

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если не найден файл `locales.json`.
- `Exception`: Если произошла ошибка во время загрузки в PrestaShop.