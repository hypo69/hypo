# Модуль для работы с ответами от GPT4Free

## Обзор

Модуль `response.py` содержит классы и функции, предназначенные для форматирования и представления ответов, полученных от различных провайдеров в рамках проекта `GPT4Free`. Он включает в себя функции для обработки URL, заголовков, изображений и других типов данных, а также классы для представления различных типов ответов, таких как JSON, скрытые ответы, сообщения об окончании работы, инструменты, использование, источники и мультимедийные данные.

## Подробнее

Этот модуль предоставляет инструменты для стандартизации и форматирования данных, возвращаемых различными поставщиками услуг GPT4Free, обеспечивая единообразное представление информации для пользователей. Функции модуля обеспечивают корректную обработку URL-адресов, нормализацию текста и создание markdown-ссылок и изображений. Классы модуля предназначены для представления различных типов ответов, от простых текстовых сообщений до сложных мультимедийных данных, и обеспечивают удобный доступ к этим данным.

## Функции

### `quote_url`

```python
def quote_url(url: str) -> str:
    """
    Преобразует части URL, сохраняя структуру домена.

    Args:
        url (str): URL-адрес для обработки.

    Returns:
        str: URL-адрес с корректно преобразованными частями.

    Как работает функция:
    1. Проверяет, содержит ли URL-адрес символы `%`. Если да, то выполняет unquote_plus для избежания двойного unquoting.
    2. Разбивает URL-адрес на части, используя `//` в качестве разделителя (максимально один раз).
    3. Если в URL-адресе нет `//`, то считает его относительным и преобразует его целиком.
    4. Если `//` присутствует, то разделяет URL-адрес на протокол и остальную часть.
    5. Разбивает оставшуюся часть на домен и путь, используя `/` в качестве разделителя (максимально один раз).
    6. Если после домена нет `/`, то считает URL-адрес доменом и возвращает его.
    7. Если `/` присутствует, то преобразует только путь, сохраняя протокол и домен.

    ASCII flowchart:

    URL --> Проверка на '%' --> Unquote (если нужно) --> Разделение на протокол и остальную часть -->
    |
    Нет '//' --> Преобразование URL
    |
    Есть '//' --> Разделение на домен и путь --> Нет '/' после домена --> Возврат протокола и домена -->
    |
    Есть '/' после домена --> Преобразование пути --> Возврат протокола, домена и преобразованного пути

    Примеры:
        >>> quote_url('https://example.com/path%20with%20spaces?query=value')
        'https://example.com/path+with+spaces?query=value'
        >>> quote_url('example.com/path with spaces')
        'example.com%2Fpath+with+spaces'
    """
    ...
```

### `quote_title`

```python
def quote_title(title: str) -> str:
    """
    Нормализует пробелы в заголовке.

    Args:
        title (str): Заголовок для нормализации.

    Returns:
        str: Заголовок с нормализованными пробелами.

    Как работает функция:
    1. Проверяет, является ли заголовок непустой строкой.
    2. Если заголовок существует, разбивает его на слова, удаляя лишние пробелы, и соединяет обратно с одним пробелом между словами.

    ASCII flowchart:

    Заголовок --> Проверка на пустоту --> Разбиение на слова и соединение с одним пробелом --> Возврат нормализованного заголовка

    Примеры:
        >>> quote_title('  Пример   заголовка  ')
        'Пример заголовка'
        >>> quote_title('')
        ''
    """
    ...
```

### `format_link`

```python
def format_link(url: str, title: Optional[str] = None) -> str:
    """
    Форматирует URL-адрес и заголовок в виде markdown-ссылки.

    Args:
        url (str): URL-адрес для создания ссылки.
        title (Optional[str], optional): Заголовок ссылки. Если `None`, извлекается из URL-адреса.

    Returns:
        str: Сформатированная markdown-ссылка.

    Как работает функция:
    1. Проверяет, задан ли заголовок.
    2. Если заголовок не задан, пытается извлечь его из URL-адреса, разделяя URL-адрес на части и удаляя "www.".
    3. Если извлечь заголовок не удается, использует URL-адрес в качестве заголовка.
    4. Форматирует URL-адрес и заголовок в виде markdown-ссылки, используя `quote_title` и `quote_url`.

    ASCII flowchart:

    URL, Заголовок --> Заголовок задан? --> Нет --> Извлечение заголовка из URL --> Не удалось извлечь --> URL в качестве заголовка -->
    |
    Да --> Использовать заданный заголовок --> Форматирование в markdown-ссылку --> Возврат markdown-ссылки

    Примеры:
        >>> format_link('https://example.com', 'Example')
        '[Example](https://example.com)'
        >>> format_link('https://example.com/path?query=value')
        '[example.com/path?query=value](https://example.com/path?query=value)'
    """
    ...
```

### `format_image`

```python
def format_image(image: str, alt: str, preview: Optional[str] = None) -> str:
    """
    Форматирует изображение в виде markdown-строки.

    Args:
        image (str): URL-адрес изображения.
        alt (str): Альтернативный текст для изображения.
        preview (Optional[str], optional): URL-адрес для предварительного просмотра изображения. Defaults to the original image.

    Returns:
        str: Сформатированная markdown-строка.

    Как работает функция:
    1. Если предоставлен URL-адрес для предварительного просмотра, заменяет `{image}` в URL-адресе на URL-адрес изображения.
    2. Форматирует изображение в виде markdown-строки, используя альтернативный текст и URL-адреса изображения и предварительного просмотра.

    ASCII flowchart:

    URL-адрес изображения, Альтернативный текст, URL-адрес для предпросмотра --> URL-адрес для предпросмотра предоставлен? --> Замена '{image}' в URL-адресе предпросмотра --> Форматирование в markdown-строку --> Возврат markdown-строки

    Примеры:
        >>> format_image('https://example.com/image.png', 'Example Image')
        '[![Example Image](https://example.com/image.png)](https://example.com/image.png)'
        >>> format_image('https://example.com/image.png', 'Example Image', 'https://example.com/preview/{image}')
        '[![Example Image](https://example.com/preview/https://example.com/image.png)](https://example.com/image.png)'
    """
    ...
```

### `format_images_markdown`

```python
def format_images_markdown(images: Union[str, List[str]], alt: str,
                           preview: Union[str, List[str]] = None) -> str:
    """
    Форматирует заданные изображения в виде markdown-строки.

    Args:
        images (Union[str, List[str]]): Изображение или список изображений для форматирования.
        alt (str): Альтернативный текст для изображений.
        preview (Union[str, List[str]], optional): URL-адрес предпросмотра или список URL-адресов предпросмотра. Если не предоставлен, используются исходные изображения.

    Returns:
        str: Отформатированная markdown-строка.

    Как работает функция:
    1. Проверяет, является ли `images` списком из одного элемента. Если да, то извлекает этот элемент.
    2. Если `images` является строкой, форматирует ее как одно изображение.
    3. Если `images` является списком, форматирует каждое изображение в списке, добавляя индекс к альтернативному тексту.
    4. Оборачивает результат флагами начала и конца генерации изображений.

    ASCII flowchart:

    Изображения, Альтернативный текст, Предпросмотр --> images - список? --> Да, один элемент? --> Извлечение элемента -->
    |                                       Нет             Нет, более одного элемента
    |                                                           Форматирование каждого изображения с индексом
    |
    images - строка? --> Форматирование как одно изображение
    |
    Оборачивание результата флагами начала и конца генерации изображений --> Возврат markdown-строки

    Примеры:
        >>> format_images_markdown('https://example.com/image.png', 'Example Image')
        '\\n<!-- generated images start -->\\n[![Example Image](https://example.com/image.png)](https://example.com/image.png)\\n<!-- generated images end -->\\n\\n'
        >>> format_images_markdown(['https://example.com/image1.png', 'https://example.com/image2.png'], 'Example Image')
        '\\n<!-- generated images start -->\\n[![#1 Example Image](https://example.com/image1.png)](https://example.com/image1.png)\\n[![#2 Example Image](https://example.com/image2.png)](https://example.com/image2.png)\\n<!-- generated images end -->\\n\\n'
    """
    ...
```

## Классы

### `ResponseType`

```python
class ResponseType:
    """
    Базовый класс для всех типов ответов.
    """
    @abstractmethod
    def __str__(self) -> str:
        """
        Преобразует ответ в строковое представление.

        Raises:
            NotImplementedError: Если метод не реализован в подклассе.
        """
        raise NotImplementedError
```

### `JsonMixin`

```python
class JsonMixin:
    """
    Миксин для классов, которые можно представить в виде JSON.
    """

    def __init__(self, **kwargs) -> None:
        """
        Инициализирует атрибуты объекта на основе переданных ключевых слов.

        Args:
            **kwargs: Ключевые слова и значения для инициализации атрибутов.
        """
        ...

    def get_dict(self) -> Dict:
        """
        Возвращает словарь атрибутов объекта, исключая приватные атрибуты (начинающиеся с "__").

        Returns:
            Dict: Словарь атрибутов объекта.
        """
        ...

    def reset(self) -> None:
        """
        Сбрасывает все атрибуты объекта.
        """
        ...
```

### `RawResponse`

```python
class RawResponse(ResponseType, JsonMixin):
    """
    Класс для представления "сырого" ответа.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
    """
    pass
```

### `HiddenResponse`

```python
class HiddenResponse(ResponseType):
    """
    Класс для представления скрытого ответа.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
    """
    def __str__(self) -> str:
        """
        Возвращает пустую строку.

        Returns:
            str: Пустая строка.
        """
        return ""
```

### `FinishReason`

```python
class FinishReason(JsonMixin, HiddenResponse):
    """
    Класс для представления причины завершения.

    Inherits:
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    def __init__(self, reason: str) -> None:
        """
        Инициализирует объект с указанием причины завершения.

        Args:
            reason (str): Причина завершения.
        """
        self.reason = reason
```

### `ToolCalls`

```python
class ToolCalls(HiddenResponse):
    """
    Класс для представления вызовов инструментов.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
    """

    def __init__(self, list: List) -> None:
        """
        Инициализирует объект списком вызовов инструментов.

        Args:
            list (List): Список вызовов инструментов.
        """
        self.list = list

    def get_list(self) -> List:
        """
        Возвращает список вызовов инструментов.

        Returns:
            List: Список вызовов инструментов.
        """
        return self.list
```

### `Usage`

```python
class Usage(JsonMixin, HiddenResponse):
    """
    Класс для представления информации об использовании ресурсов.

    Inherits:
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    pass
```

### `AuthResult`

```python
class AuthResult(JsonMixin, HiddenResponse):
    """
    Класс для представления результата аутентификации.

    Inherits:
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    pass
```

### `TitleGeneration`

```python
class TitleGeneration(HiddenResponse):
    """
    Класс для представления сгенерированного заголовка.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    def __init__(self, title: str) -> None:
        """
        Инициализирует объект с указанием заголовка.

        Args:
            title (str): Сгенерированный заголовок.
        """
        self.title = title
```

### `DebugResponse`

```python
class DebugResponse(HiddenResponse):
    """
    Класс для представления отладочного сообщения.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    def __init__(self, log: str) -> None:
        """
        Инициализирует объект с указанием отладочного сообщения.

        Args:
            log (str): Отладочное сообщение.
        """
        self.log = log
```

### `Reasoning`

```python
class Reasoning(ResponseType):
    """
    Класс для представления логических рассуждений.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
    """
    def __init__(
            self,
            token: Optional[str] = None,
            label: Optional[str] = None,
            status: Optional[str] = None,
            is_thinking: Optional[str] = None
        ) -> None:
        """
        Инициализирует объект с указанием токена, статуса и состояния обдумывания.

        Args:
            token (Optional[str], optional): Токен. Defaults to None.
            status (Optional[str], optional): Статус. Defaults to None.
            is_thinking (Optional[str], optional): Состояние обдумывания. Defaults to None.
        """
        self.token = token
        self.label = label
        self.status = status
        self.is_thinking = is_thinking

    def __str__(self) -> str:
        """
        Возвращает строковое представление на основе доступных атрибутов.

        Returns:
            str: Строковое представление.
        """
        ...

    def __eq__(self, other: Reasoning):
        """
        Сравнивает два объекта Reasoning на равенство.

        Args:
            other (Reasoning): Другой объект Reasoning для сравнения.

        Returns:
            bool: True, если объекты равны, иначе False.
        """
        return (self.token == other.token and
                self.status == other.status and
                self.is_thinking == other.is_thinking)

    def get_dict(self) -> Dict:
        """
        Возвращает словарь атрибутов объекта.

        Returns:
            Dict: Словарь атрибутов объекта.
        """
        ...
```

### `Sources`

```python
class Sources(ResponseType):
    """
    Класс для представления источников информации.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
    """
    def __init__(self, sources: List[Dict[str, str]]) -> None:
        """
        Инициализирует объект списком словарей, представляющих источники.

        Args:
            sources (List[Dict[str, str]]): Список словарей с информацией об источниках.
        """
        self.list = []
        for source in sources:
            self.add_source(source)

    def add_source(self, source: Union[Dict[str, str], str]) -> None:
        """
        Добавляет источник в список, очищая URL-адрес при необходимости.

        Args:
            source (Union[Dict[str, str], str]): Источник в виде словаря или URL-адреса.
        """
        ...

    def __str__(self) -> str:
        """
        Возвращает отформатированные источники в виде строки.

        Returns:
            str: Отформатированная строка с источниками.
        """
        ...
```

### `YouTube`

```python
class YouTube(HiddenResponse):
    """
    Класс для представления идентификаторов YouTube.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    def __init__(self, ids: List[str]) -> None:
        """
        Инициализирует объект списком идентификаторов YouTube.

        Args:
            ids (List[str]): Список идентификаторов YouTube.
        """
        self.ids = ids

    def to_string(self) -> str:
        """
        Возвращает встроенные элементы YouTube в виде строки.

        Returns:
            str: Строка с встроенными элементами YouTube.
        """
        ...
```

### `AudioResponse`

```python
class AudioResponse(ResponseType):
    """
    Класс для представления аудио-ответа.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
    """
    def __init__(self, data: Union[bytes, str]) -> None:
        """
        Инициализирует объект с аудио-данными в виде байтов.

        Args:
            data (Union[bytes, str]): Аудио-данные в виде байтов.
        """
        self.data = data

    def to_uri(self) -> str:
        """
        Возвращает аудио-данные в виде URI, закодированного в base64.

        Returns:
            str: URI, закодированный в base64.
        """
        if isinstance(self.data, str):
            return self.data
        """Return audio data as a base64-encoded data URI."""
        data_base64 = base64.b64encode(self.data).decode()
        return f"data:audio/mpeg;base64,{data_base64}"

    def __str__(self) -> str:
        """
        Возвращает аудио в виде html-элемента.

        Returns:
            str: html-элемент audio.
        """
        return f'<audio controls src="{self.to_uri()}"></audio>'
```

### `BaseConversation`

```python
class BaseConversation(ResponseType):
    """
    Базовый класс для представлений бесед.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
    """
    def __str__(self) -> str:
        """
        Возвращает пустую строку по умолчанию.

        Returns:
            str: Пустая строка.
        """
        return ""
```

### `JsonConversation`

```python
class JsonConversation(BaseConversation, JsonMixin):
    """
    Класс для представления бесед в формате JSON.

    Inherits:
        BaseConversation: Базовый класс для представлений бесед.
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
    """
    pass
```

### `SynthesizeData`

```python
class SynthesizeData(HiddenResponse, JsonMixin):
    """
    Класс для представления синтезированных данных.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
    """
    def __init__(self, provider: str, data: Dict) -> None:
        """
        Инициализирует объект с указанием провайдера и данных.

        Args:
            provider (str): Провайдер данных.
            data (Dict): Данные.
        """
        self.provider = provider
        self.data = data
```

### `SuggestedFollowups`

```python
class SuggestedFollowups(HiddenResponse):
    """
    Класс для представления предложенных последующих действий.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
    """

    def __init__(self, suggestions: list[str]):
        """
        Инициализирует объект списком предложений.
        """
        self.suggestions = suggestions
```

### `RequestLogin`

```python
class RequestLogin(HiddenResponse):
    """
    Класс для представления запроса на вход в систему.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    def __init__(self, label: str, login_url: str) -> None:
        """
        Инициализирует объект с указанием метки и URL-адреса для входа.

        Args:
            label (str): Метка.
            login_url (str): URL-адрес для входа.
        """
        self.label = label
        self.login_url = login_url

    def to_string(self) -> str:
        """
        Возвращает отформатированную ссылку для входа в виде строки.

        Returns:
            str: Отформатированная строка со ссылкой для входа.
        """
        ...
```

### `MediaResponse`

```python
class MediaResponse(ResponseType):
    """
    Класс для представления медиа-ответа.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
    """
    def __init__(
        self,
        urls: Union[str, List[str]],
        alt: str,
        options: Dict = {},
        **kwargs
    ) -> None:
        """
        Инициализирует объект с указанием изображений, альтернативного текста и опций.

        Args:
            urls (Union[str, List[str]]): URL-адрес или список URL-адресов медиа.
            alt (str): Альтернативный текст.
            options (Dict, optional): Опции. Defaults to {}.
            **kwargs: Дополнительные аргументы.
        """
        self.urls = kwargs.get("images", urls)
        self.alt = alt
        self.options = options

    def get(self, key: str) -> any:
        """
        Возвращает значение опции по ключу.

        Args:
            key (str): Ключ опции.

        Returns:
            any: Значение опции.
        """
        return self.options.get(key)

    def get_list(self) -> List[str]:
        """
        Возвращает изображения в виде списка.

        Returns:
            List[str]: Список URL-адресов изображений.
        """
        return [self.urls] if isinstance(self.urls, str) else self.urls
```

### `ImageResponse`

```python
class ImageResponse(MediaResponse):
    """
    Класс для представления ответа с изображением.

    Inherits:
        MediaResponse: Базовый класс для медиа-ответов.
    """
    def __str__(self) -> str:
        """
        Возвращает изображения в формате markdown.

        Returns:
            str: Строка с изображениями в формате markdown.
        """
        return format_images_markdown(self.urls, self.alt, self.get("preview"))
```

### `VideoResponse`

```python
class VideoResponse(MediaResponse):
    """
    Класс для представления ответа с видео.

    Inherits:
        MediaResponse: Базовый класс для медиа-ответов.
    """
    def __str__(self) -> str:
        """
        Возвращает видео в виде html-элементов.

        Returns:
            str: Строка с видео в виде html-элементов.
        """
        return "\\n".join([f'<video controls src="{video}"></video>\' for video in self.get_list()])
```

### `ImagePreview`

```python
class ImagePreview(ImageResponse):
    """
    Класс для представления предпросмотра изображения.

    Inherits:
        ImageResponse: Базовый класс для ответов с изображениями.
    """
    def __str__(self) -> str:
        """
        Возвращает пустую строку для предпросмотра.

        Returns:
            str: Пустая строка.
        """
        return ""

    def to_string(self) -> str:
        """
        Возвращает изображения в формате markdown.

        Returns:
            str: Строка с изображениями в формате markdown.
        """
        return super().__str__()
```

### `PreviewResponse`

```python
class PreviewResponse(HiddenResponse):
    """
    Класс для представления ответа с предпросмотром.

    Inherits:
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    def __init__(self, data: str) -> None:
        """
        Инициализирует объект с указанием данных.

        Args:
            data (str): Данные.
        """
        self.data = data

    def to_string(self) -> str:
        """
        Возвращает данные в виде строки.

        Returns:
            str: Строка с данными.
        """
        return self.data
```

### `Parameters`

```python
class Parameters(ResponseType, JsonMixin):
    """
    Класс для представления параметров.

    Inherits:
        ResponseType: Базовый класс для всех типов ответов.
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
    """
    def __str__(self) -> str:
        """
        Возвращает пустую строку.

        Returns:
            str: Пустая строка.
        """
        return ""
```

### `ProviderInfo`

```python
class ProviderInfo(JsonMixin, HiddenResponse):
    """
    Класс для представления информации о провайдере.

    Inherits:
        JsonMixin: Миксин для классов, которые можно представить в виде JSON.
        HiddenResponse: Базовый класс для скрытых ответов.
    """
    pass