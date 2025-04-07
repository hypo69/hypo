# Модуль `emil_design`

## Обзор

Модуль `emil_design.py` предназначен для управления и обработки изображений, а также для автоматизации процессов продвижения продуктов в Facebook и PrestaShop. Он ориентирован на использование в контексте магазина `emil-design.com`.

## Подробнее

Этот модуль предоставляет функциональность для:

- Описания изображений с использованием Gemini AI.
- Загрузки описаний продуктов в PrestaShop.

Расположение файла в проекте: `hypotez/src/endpoints/emil/emil_design.py`.

## Классы

### `Config`

**Описание**: Класс `Config` предназначен для хранения конфигурационных параметров, необходимых для работы с API PrestaShop и другими сервисами. Он определяет режимы работы (dev, dev8, prod) и соответствующие API ключи и домены.

**Принцип работы**:
Класс определяет статические атрибуты, такие как `ENDPOINT`, `MODE`, `POST_FORMAT`, `API_DOMAIN` и `API_KEY`. В зависимости от значения переменной окружения `USE_ENV` или значения атрибута `MODE`, класс определяет значения `API_DOMAIN` и `API_KEY` либо из переменных окружения, либо из учетных данных, хранящихся в `gs.credentials`.

### `EmilDesign`

**Описание**: Класс `EmilDesign` предназначен для автоматизации процессов проектирования и продвижения изображений на различных платформах, включая PrestaShop и Facebook. Он включает в себя функциональность для описания изображений с использованием AI, загрузки этих описаний в PrestaShop и публикации изображений с описаниями в Facebook.

**Принцип работы**:
Класс инициализируется с настройками путей, конфигураций и API ключей для Gemini и PrestaShop. Он использует методы для описания изображений на основе инструкций и примеров, сохранения описаний и загрузки продуктов в PrestaShop.

**Методы**:

- `describe_images`: Описывает изображения, используя Gemini AI, на основе предоставленных инструкций и примеров.
- `promote_to_facebook`: Продвигает изображения и их описания в Facebook.
- `upload_described_products_to_prestashop`: Загружает информацию о продуктах в PrestaShop.

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
```

**Назначение**: Описывает изображения на основе предоставленных инструкций и примеров с использованием моделей AI (Gemini или OpenAI).

**Параметры**:
- `lang` (str): Язык, на котором должно быть сгенерировано описание изображения.
- `models` (dict, optional): Конфигурация моделей AI для использования. По умолчанию использует Gemini и OpenAI.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `FileNotFoundError`: Если не найдены файлы инструкций.
- `Exception`: Если произошла ошибка во время обработки изображения.

**Как работает функция**:
1. **Чтение инструкций и конфигураций**: Сначала функция пытается прочитать инструкции и категории мебели из файлов, расположенных в каталогах `instructions` и `categories` базового пути. Эти инструкции и категории используются для формирования запроса к модели AI.
2. **Подготовка списка изображений для обработки**: Функция получает список всех файлов изображений из каталога `images/furniture_images` и фильтрует их, чтобы исключить изображения, которые уже были описаны (согласно списку в файле `described_images.txt`).
3. **Использование моделей AI для описания изображений**: В зависимости от конфигурации, функция использует либо Gemini, либо OpenAI для генерации описаний изображений. Изображения передаются в модель AI, которая генерирует JSON-описание.
4. **Сохранение результатов**: Сгенерированные описания сохраняются в JSON-файлы, а путь к обработанному изображению добавляется в файл `described_images.txt`, чтобы избежать повторной обработки.
5. **Обработка ошибок**: Если во время процесса возникают ошибки (например, не найдены файлы инструкций или произошла ошибка при обработке изображения), они логируются с использованием `logger.error`.

```
Начало
│
├── Чтение инструкций и конфигураций
│   │
│   └── Получение путей к файлам инструкций и категорий
│
├── Подготовка списка изображений для обработки
│   │
│   └── Фильтрация изображений (исключение уже описанных)
│
├── Описание изображений с использованием моделей AI
│   │
│   └── Генерация JSON-описания с использованием Gemini или OpenAI
│
├── Сохранение результатов
│   │
│   └── Сохранение JSON-описания и обновление списка описанных изображений
│
└── Конец
```

**Внутренние функции**: Нет.

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
```

**Назначение**: Продвигает изображения и их описания в Facebook.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если произошла ошибка во время продвижения в Facebook.

**Как работает функция**:
1. **Инициализация драйвера веб-браузера**: Функция создает экземпляр драйвера Chrome, используя класс `Driver` из модуля `src.webdriver.driver`.
2. **Загрузка данных для публикации**: Функция загружает JSON-файл, содержащий описания изображений, используя `j_loads_ns`.
3. **Публикация сообщений в Facebook**: Функция перебирает сообщения и публикует каждое сообщение в Facebook, используя функцию `post_message`.

```
Начало
│
├── Инициализация драйвера веб-браузера
│   │
│   └── Создание экземпляра драйвера Chrome
│
├── Загрузка данных для публикации
│   │
│   └── Загрузка JSON-файла с описаниями изображений
│
├── Публикация сообщений в Facebook
│   │
│   └── Перебор сообщений и публикация каждого сообщения
│
└── Конец
```

**Внутренние функции**: Нет.

**Примеры**:

```python
emil = EmilDesign()
asyncio.run(emil.promote_to_facebook())
```

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
        Вот образец кода для получения слопваря языков из конкретной базы данных
        >>import language
        >>lang_class = PrestaLanguage()
        >>print(lang_class.get_languages_schema())


    Returns:
        bool: True if upload succeeds, False otherwise.

    Raises:
        FileNotFoundError: If locales file is not found.
        Exception: If any error occurs during PrestaShop upload.
    """
```

**Назначение**: Загружает информацию о продуктах в PrestaShop.

**Параметры**:
- `products_list` (Optional[List[SimpleNamespace]], optional): Список информации о продуктах. По умолчанию `None`.
- `id_lang` (Optional[int | str], optional): ID языка для базы данных PrestaShop. По умолчанию 2 (иврит).

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если не найден файл `locales.json`.
- `Exception`: Если произошла ошибка во время загрузки в PrestaShop.

**Как работает функция**:

1. **Получение списка файлов продуктов**: Функция получает список JSON файлов, содержащих информацию о продуктах, из указанной директории.
2. **Загрузка информации о продуктах**: Для каждого файла продукта функция загружает информацию и создает экземпляр класса `ProductFields`, заполняя его данными из JSON.
3. **Загрузка продукта в PrestaShop**: Используя экземпляр класса `PrestaProduct`, функция добавляет новый продукт в PrestaShop с использованием информации, содержащейся в экземпляре `ProductFields`.
4. **Обработка ошибок**: Если во время процесса возникают ошибки (например, не найден файл `locales.json` или произошла ошибка при загрузке в PrestaShop), они логируются с использованием `logger.error`.

```
Начало
│
├── Получение списка файлов продуктов
│   │
│   └── Получение списка JSON файлов из директории
│
├── Загрузка информации о продуктах
│   │
│   └── Загрузка данных из JSON и создание экземпляра ProductFields
│
├── Загрузка продукта в PrestaShop
│   │
│   └── Добавление нового продукта в PrestaShop с использованием API
│
└── Конец
```

**Внутренние функции**: Нет.

**Примеры**:

```python
emil = EmilDesign()
emil.upload_described_products_to_prestashop(id_lang=2)