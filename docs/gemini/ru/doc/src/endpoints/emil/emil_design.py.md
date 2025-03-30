# Модуль: src.endpoints.emil.emil_design

## Обзор

Модуль `emil_design.py` предназначен для управления и обработки изображений, а также для их продвижения на платформах Facebook и PrestaShop. Он включает в себя функциональность для описания изображений с использованием моделей Gemini AI и OpenAI, загрузки описаний продуктов в PrestaShop, а также для автоматизации публикаций в Facebook.

## Подробней

Этот модуль играет важную роль в автоматизации процессов, связанных с контентом и продвижением продукции. Он использует API различных платформ для загрузки и обновления информации о товарах, а также для публикации рекламных материалов. Использование AI для описания изображений позволяет создавать более привлекательные и информативные описания товаров, что, в свою очередь, может повысить их привлекательность для покупателей.

## Классы

### `Config`

**Описание**: Класс конфигурации для `EmilDesign`. Определяет основные параметры, такие как endpoint, режим работы (dev, dev8 или production), формат POST-запросов, а также API-ключи и домены для доступа к PrestaShop.

**Параметры**:
- `ENDPOINT` (str): Endpoint для модуля (по умолчанию 'emil').
- `MODE` (str): Режим работы ('dev', 'dev8', или production).
- `POST_FORMAT` (str): Формат POST-запросов (по умолчанию 'XML').
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): API-ключ для доступа к PrestaShop.

**Примеры**:
```python
config = Config()
print(f"API Domain: {config.API_DOMAIN}")
print(f"API Key: {config.API_KEY}")
```

### `EmilDesign`

**Описание**: Класс, предназначенный для проектирования и продвижения изображений через различные платформы, такие как PrestaShop и Facebook. Он содержит методы для описания изображений с использованием AI, загрузки описаний продуктов в PrestaShop и продвижения контента в Facebook.

**Методы**:
- `describe_images`: Описывает изображения на основе предоставленных инструкций и примеров.
- `promote_to_facebook`: Продвигает изображения и их описания в Facebook.
- `upload_described_products_to_prestashop`: Загружает информацию о продуктах в PrestaShop.

**Параметры**:
- `gemini` (Optional[GoogleGenerativeAI]): Экземпляр класса `GoogleGenerativeAI` для работы с моделью Gemini.
- `openai` (Optional[OpenAIModel]): Экземпляр класса `OpenAIModel` для работы с моделью OpenAI.
- `base_path` (Path): Базовый путь к файлам конфигурации и инструкциям.
- `config` (SimpleNamespace): Объект, содержащий конфигурационные параметры из файла `emil.json`.
- `data_path` (Path): Путь к директории с данными изображений и описаний.
- `gemini_api` (str): API-ключ для доступа к Gemini AI.
- `presta_api` (str): API-ключ для доступа к PrestaShop.
- `presta_domain` (str): Домен API PrestaShop.

**Примеры**:
```python
emil = EmilDesign()
emil.describe_images(lang='he')
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

**Описание**: Описывает изображения на основе предоставленных инструкций и примеров, используя модели Gemini AI и OpenAI. Загружает инструкции и категории мебели из файлов, обрабатывает изображения из указанной директории и сохраняет описания в формате JSON.

**Параметры**:
- `lang` (str): Язык, на котором должно быть выполнено описание изображений.
- `models` (dict, optional): Конфигурация моделей AI для использования. По умолчанию использует Gemini и OpenAI.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `FileNotFoundError`: Если не найдены файлы инструкций.
- `Exception`: Если произошла ошибка во время обработки изображения.

**Примеры**:
```python
emil = EmilDesign()
emil.describe_images(lang='he', models={'gemini': {'model_name': 'gemini-1.5-flash'}})
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

**Описание**: Продвигает изображения и их описания в Facebook. Использует Selenium WebDriver для автоматизации процесса публикации сообщений в группах Facebook.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если произошла ошибка во время продвижения в Facebook.

**Примеры**:
```python
emil = EmilDesign()
asyncio.run(emil.promote_to_facebook())
```

### `upload_described_products_to_prestashop`

```python
def upload_described_products_to_prestashop(
    self, products_list: Optional[List[SimpleNamespace]] = None, lang: Optional[str] = None, *args, **kwards
) -> bool:
    """Upload product information to PrestaShop.

    Args:
        products_list (Optional[List[SimpleNamespace]], optional): List of product info. Defaults to None.
        lang (Optional[str], optional): Language code. Defaults to None.

    Returns:
        bool: True if upload succeeds, False otherwise.

    Raises:
        FileNotFoundError: If locales file is not found.
        Exception: If any error occurs during PrestaShop upload.
    """
    ...
```

**Описание**: Загружает информацию о продуктах в PrestaShop. Читает JSON-файлы с описаниями продуктов, преобразует их в формат, необходимый для PrestaShop, и загружает через API PrestaShop.

**Параметры**:
- `products_list` (Optional[List[SimpleNamespace]], optional): Список объектов `SimpleNamespace`, содержащих информацию о продуктах. По умолчанию `None`.
- `lang` (Optional[str], optional): Языковой код для загрузки продуктов. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если не найден файл локалей.
- `Exception`: Если произошла ошибка во время загрузки в PrestaShop.

**Примеры**:
```python
emil = EmilDesign()
emil.upload_described_products_to_prestashop(lang='he')