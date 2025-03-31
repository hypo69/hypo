# Модуль `emil_design`

## Обзор

Модуль предназначен для управления и обработки изображений, а также продвижения товаров магазина `emil-design.com` на платформах Facebook и PrestaShop. Он включает в себя функции для описания изображений с использованием AI, загрузки описаний продуктов в PrestaShop и продвижения контента в Facebook.

## Подробней

Модуль автоматизирует процессы, связанные с созданием контента для онлайн-магазина, используя возможности AI для генерации описаний товаров и автоматизации публикации в социальных сетях и на платформе электронной коммерции PrestaShop. Это позволяет сократить время и ресурсы, затрачиваемые на ручное создание контента и продвижение товаров.

## Классы

### `Config`

**Описание**: Класс конфигурации для `EmilDesign`.

**Как работает класс**:
Класс `Config` предназначен для хранения и управления конфигурационными параметрами, необходимыми для работы с API PrestaShop и другими сервисами. Он определяет endpoint API, режим работы (разработка, production), формат POST-запросов и ключи API. Класс использует переменные окружения, если `USE_ENV` установлен в `True`, в противном случае использует значения, хранящиеся в `gs.credentials`.

Внутри класса происходят следующие действия и преобразования:
A: Определение константных значений, таких как `ENDPOINT` и `POST_FORMAT`.
|
B: Проверка использования переменных окружения (`USE_ENV`).
|
C: Если `USE_ENV` равен `True`, загружаются переменные окружения из файла `.env`.
|
D: В зависимости от значения `MODE` (dev, dev8, prod) устанавливаются значения `API_DOMAIN` и `API_KEY` из `gs.credentials` или переменных окружения. Если `MODE` не имеет валидного значения, устанавливается режим `dev`.

### `EmilDesign`

**Описание**: Класс для проектирования и продвижения изображений через различные платформы.

**Как работает класс**:
Класс `EmilDesign` содержит методы для описания изображений с использованием моделей AI (Gemini и OpenAI), а также для продвижения этих изображений и их описаний в Facebook и PrestaShop. Он инициализирует модели AI, загружает конфигурации и данные, необходимые для работы с API PrestaShop, и предоставляет интерфейс для автоматизации процессов продвижения контента.

Внутри класса происходят следующие действия и преобразования:
A: Инициализация моделей Gemini и OpenAI (опционально).
|
B: Загрузка конфигурации из файла `emil.json`.
|
C: Определение путей к данным и API-ключам.

**Методы**:

- `describe_images`: Описывает изображения на основе предоставленных инструкций и примеров.
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
    ...
```

**Как работает функция**:
Функция `describe_images` описывает изображения на основе предоставленных инструкций и примеров с использованием моделей AI Gemini и OpenAI. Она считывает инструкции из файлов, загружает изображения из указанной директории, генерирует описания с использованием AI и сохраняет результаты в JSON-файлы. Также ведется учет уже обработанных изображений, чтобы избежать повторной обработки.

Внутри функции происходят следующие действия и преобразования:
A: Считывание инструкций из файлов `system_instruction.{lang}.md` и `hand_made_furniture.{lang}.md`.
|
B: Загрузка списка категорий мебели из файла `main_categories_furniture.json`.
|
C: Определение путей к файлам вывода и обработанным изображениям.
|
D: Получение списка изображений для обработки.
|
E: Инициализация моделей Gemini и OpenAI (в зависимости от конфигурации).
|
F: Для каждого изображения генерируется описание с использованием AI, которое сохраняется в JSON-файл.
|
G: Список обработанных изображений обновляется и сохраняется в файл.

**Параметры**:
- `lang` (str): Язык для описания изображений.
- `models` (dict, optional): Конфигурация моделей AI. По умолчанию используются модели Gemini и OpenAI.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `FileNotFoundError`: Если файлы инструкций не найдены.
- `Exception`: Если возникает ошибка во время обработки изображений.

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

**Как работает функция**:
Функция `promote_to_facebook` продвигает изображения и их описания в Facebook. Она использует веб-драйвер для автоматического входа в Facebook и публикации сообщений в указанной группе. Функция загружает описания изображений из JSON-файла и использует их для создания сообщений в Facebook.

Внутри функции происходят следующие действия и преобразования:
A: Инициализация веб-драйвера (Chrome).
|
B: Открытие страницы Facebook-группы.
|
C: Загрузка описаний изображений из файла `images_descritions_he.json`.
|
D: Для каждого описания создается сообщение в Facebook с использованием функции `post_message`.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время продвижения в Facebook.

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
    ...
```

**Как работает функция**:
Функция `upload_described_products_to_prestashop` загружает информацию о продуктах в PrestaShop. Она считывает данные о продуктах из JSON-файлов, создает объекты `ProductFields` с информацией о продукте и использует API PrestaShop для добавления новых продуктов. Функция также обрабатывает информацию о языке, на котором будут отображаться названия и характеристики товара.

Внутри функции происходят следующие действия и преобразования:
A: Получение списка файлов с информацией о продуктах.
|
B: Загрузка данных о продуктах из JSON-файлов.
|
C: Создание объекта `PrestaProduct` для взаимодействия с API PrestaShop.
|
D: Определение языка, на котором будут отображаться названия и характеристики товара.
|
E: Для каждого продукта создается объект `ProductFields` с информацией о продукте, который затем передается в API PrestaShop для добавления нового продукта.

**Параметры**:
- `products_list` (Optional[List[SimpleNamespace]], optional): Список информации о продуктах. По умолчанию `None`.
- `id_lang` (Optional[int | str], optional): Идентификатор языка для базы данных PrestaShop. По умолчанию 2.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл локалей не найден.
- `Exception`: Если возникает ошибка во время загрузки в PrestaShop.