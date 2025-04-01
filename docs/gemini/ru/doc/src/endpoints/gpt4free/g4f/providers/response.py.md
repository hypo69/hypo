# Модуль для работы с ответами от GPT4Free

## Обзор

Этот модуль содержит классы для обработки различных типов ответов, возвращаемых провайдерами GPT4Free. Он включает в себя инструменты для форматирования URL, работы с изображениями, аудио и видео, а также для представления ответов в различных форматах, таких как JSON, Markdown и HTML.

## Подробней

Модуль предоставляет набор классов, предназначенных для стандартизации и упрощения работы с ответами от различных источников GPT4Free. Он включает в себя утилиты для обработки текста, форматирования ссылок и изображений, а также классы для представления различных типов контента, таких как JSON, аудио и видео.

## Функции

### `quote_url`

```python
def quote_url(url: str) -> str:
    """Преобразует части URL, сохраняя структуру домена.

    Args:
        url (str): URL для преобразования.

    Returns:
        str: Преобразованный URL.

    Как работает функция:
    1. Проверяет, содержит ли URL закодированные символы (`%`). Если да, то декодирует URL, чтобы избежать двойного декодирования.
    2. Разбивает URL на части, разделяя протокол и остальную часть URL по разделителю `//`.
    3. Если в URL отсутствует `//`, считает его относительным и кодирует целиком.
    4. Если `//` присутствует, разделяет остальную часть URL на домен и путь по первому символу `/`.
    5. Если после домена нет символа `/`, считает URL доменом и возвращает его без изменений.
    6. Кодирует путь, сохраняя символы `/?&=#` и возвращает полный URL.

    Примеры:
    >>> quote_url("https://example.com/path%20with%20spaces?query=value")
    'https://example.com/path%20with%20spaces?query=value'

    >>> quote_url("example.com/path with spaces")
    'example.com/path%20with%20spaces'
    """
    ...
```

### `quote_title`

```python
def quote_title(title: str) -> str:
    """Нормализует пробелы в заголовке.

    Args:
        title (str): Заголовок для нормализации.

    Returns:
        str: Заголовок с нормализованными пробелами.

    Как работает функция:
    1. Проверяет, является ли заголовок непустой строкой.
    2. Если заголовок непустой, разделяет строку на слова, удаляя лишние пробелы, и объединяет их обратно в строку с одним пробелом между словами.
    3. Если заголовок пустой, возвращает пустую строку.

    Примеры:
    >>> quote_title("  Example   Title  ")
    'Example Title'

    >>> quote_title("")
    ''
    """
    ...
```

### `format_link`

```python
def format_link(url: str, title: Optional[str] = None) -> str:
    """Форматирует URL и заголовок в виде Markdown ссылки.

    Args:
        url (str): URL для ссылки.
        title (Optional[str], optional): Заголовок для отображения. Если None, извлекается из URL.

    Returns:
        str: Отформатированная Markdown ссылка.

    Как работает функция:
    1. Если заголовок не предоставлен, пытается извлечь его из URL.
    2. Если извлечь заголовок не удалось, использует сам URL в качестве заголовка.
    3. Форматирует URL и заголовок в виде Markdown ссылки, используя функции `quote_title` и `quote_url`.

    Примеры:
    >>> format_link("https://example.com", "Example")
    '[Example](https://example.com)'

    >>> format_link("https://example.com")
    '[example.com](https://example.com)'
    """
    ...
```

### `format_image`

```python
def format_image(image: str, alt: str, preview: Optional[str] = None) -> str:
    """Форматирует изображение в виде Markdown строки.

    Args:
        image (str): URL изображения.
        alt (str): Альтернативный текст для изображения.
        preview (Optional[str], optional): URL для предварительного просмотра. По умолчанию используется оригинальное изображение.

    Returns:
        str: Отформатированная Markdown строка для изображения.

    Как работает функция:
    1. Если предоставлен URL для предварительного просмотра, заменяет плейсхолдер `{image}` в URL предварительного просмотра на URL изображения.
    2. Форматирует изображение в виде Markdown, используя альтернативный текст и URL для предварительного просмотра и URL изображения.

    Примеры:
    >>> format_image("https://example.com/image.jpg", "Example Image")
    '[![Example Image](https://example.com/image.jpg)](https://example.com/image.jpg)'

    >>> format_image("https://example.com/image.jpg", "Example Image", "https://example.com/preview/{image}")
    '[![Example Image](https://example.com/preview/https%3A//example.com/image.jpg)](https://example.com/image.jpg)'
    """
    ...
```

### `format_images_markdown`

```python
def format_images_markdown(images: Union[str, List[str]], alt: str,
                           preview: Union[str, List[str]] = None) -> str:
    """Форматирует изображения в виде Markdown строки.

    Args:
        images (Union[str, List[str]]): Изображение или список изображений для форматирования.
        alt (str): Альтернативный текст для изображений.
        preview (Union[str, List[str]], optional): URL или список URL для предварительного просмотра. Если не предоставлен, используются оригинальные изображения.

    Returns:
        str: Отформатированная Markdown строка для изображений.

    Как работает функция:
    1. Если передан список изображений с одним элементом, извлекает этот элемент.
    2. Если передан один URL изображения, форматирует его с помощью функции `format_image`.
    3. Если передан список URL изображений, форматирует каждое изображение и объединяет их в строку, разделенную символом новой строки.
    4. Оборачивает результат флагами `<!-- generated images start -->` и `<!-- generated images end -->`.

    Примеры:
    >>> format_images_markdown("https://example.com/image.jpg", "Example Image")
    '\\n<!-- generated images start -->\\n[![Example Image](https://example.com/image.jpg)](https://example.com/image.jpg)\\n<!-- generated images end -->\\n'

    >>> format_images_markdown(["https://example.com/image1.jpg", "https://example.com/image2.jpg"], "Example Images")
    '\\n<!-- generated images start -->\\n[![#1 Example Images](https://example.com/image1.jpg)](https://example.com/image1.jpg)\\n[![#2 Example Images](https://example.com/image2.jpg)](https://example.com/image2.jpg)\\n<!-- generated images end -->\\n'
    """
    ...
```

## Классы

### `ResponseType`

```python
class ResponseType:
    @abstractmethod
    def __str__(self) -> str:
        """Преобразует ответ в строковое представление."""
        raise NotImplementedError
```

**Описание**:
Абстрактный базовый класс для всех типов ответов. Определяет абстрактный метод `__str__`, который должен быть реализован в подклассах для преобразования ответа в строковое представление.

**Методы**:
- `__str__`: Абстрактный метод, который должен быть реализован в подклассах.

### `JsonMixin`

```python
class JsonMixin:
    def __init__(self, **kwargs) -> None:
        """Инициализирует атрибуты объекта с использованием переданных именованных аргументов."""
        ...

    def get_dict(self) -> Dict:
        """Возвращает словарь атрибутов объекта, исключая приватные атрибуты (начинающиеся с "__")."""
        ...

    def reset(self) -> None:
        """Сбрасывает все атрибуты объекта."""
        ...
```

**Описание**:
Миксин для классов, которые могут быть представлены в виде JSON. Предоставляет методы для инициализации атрибутов объекта из именованных аргументов, получения словаря атрибутов и сброса всех атрибутов.

**Методы**:
- `__init__`: Инициализирует атрибуты объекта с использованием переданных именованных аргументов.
- `get_dict`: Возвращает словарь атрибутов объекта, исключая приватные атрибуты (начинающиеся с "__").
- `reset`: Сбрасывает все атрибуты объекта.

### `RawResponse`

```python
class RawResponse(ResponseType, JsonMixin):
    pass
```

**Описание**:
Класс для представления "сырых" ответов. Наследуется от `ResponseType` и `JsonMixin`.

### `HiddenResponse`

```python
class HiddenResponse(ResponseType):
    def __str__(self) -> str:
        """Скрытые ответы возвращают пустую строку."""
        return ""
```

**Описание**:
Базовый класс для "скрытых" ответов, которые не должны отображаться.

**Методы**:
- `__str__`: Возвращает пустую строку.

### `FinishReason`

```python
class FinishReason(JsonMixin, HiddenResponse):
    def __init__(self, reason: str) -> None:
        """Инициализирует объект с указанием причины завершения."""
        self.reason = reason
```

**Описание**:
Класс для представления причины завершения. Наследуется от `JsonMixin` и `HiddenResponse`.

**Методы**:
- `__init__`: Инициализирует объект с указанием причины завершения.

### `ToolCalls`

```python
class ToolCalls(HiddenResponse):
    def __init__(self, list: List) -> None:
        """Инициализирует объект списком вызовов инструментов."""
        self.list = list

    def get_list(self) -> List:
        """Возвращает список вызовов инструментов."""
        return self.list
```

**Описание**:
Класс для представления вызовов инструментов. Наследуется от `HiddenResponse`.

**Методы**:
- `__init__`: Инициализирует объект списком вызовов инструментов.
- `get_list`: Возвращает список вызовов инструментов.

### `Usage`

```python
class Usage(JsonMixin, HiddenResponse):
    pass
```

**Описание**:
Класс для представления информации об использовании. Наследуется от `JsonMixin` и `HiddenResponse`.

### `AuthResult`

```python
class AuthResult(JsonMixin, HiddenResponse):
    pass
```

**Описание**:
Класс для представления результата аутентификации. Наследуется от `JsonMixin` и `HiddenResponse`.

### `TitleGeneration`

```python
class TitleGeneration(HiddenResponse):
    def __init__(self, title: str) -> None:
        """Инициализирует объект заголовком."""
        self.title = title
```

**Описание**:
Класс для представления сгенерированного заголовка. Наследуется от `HiddenResponse`.

**Методы**:
- `__init__`: Инициализирует объект заголовком.

### `DebugResponse`

```python
class DebugResponse(HiddenResponse):
    def __init__(self, log: str) -> None:
        """Инициализирует объект сообщением лога."""
        self.log = log
```

**Описание**:
Класс для представления отладочной информации. Наследуется от `HiddenResponse`.

**Методы**:
- `__init__`: Инициализирует объект сообщением лога.

### `Reasoning`

```python
class Reasoning(ResponseType):
    def __init__(
            self,
            token: Optional[str] = None,
            label: Optional[str] = None,
            status: Optional[str] = None,
            is_thinking: Optional[str] = None
        ) -> None:
        """Инициализирует объект токеном, статусом и состоянием "размышления"."""
        self.token = token
        self.label = label
        self.status = status
        self.is_thinking = is_thinking

    def __str__(self) -> str:
        """Возвращает строковое представление на основе доступных атрибутов."""
        if self.is_thinking is not None:
            return self.is_thinking
        if self.token is not None:
            return self.token
        if self.status is not None:
            if self.label is not None:
                return f"{self.label}: {self.status}\\n"
            return f"{self.status}\\n"
        return ""

    def __eq__(self, other: Reasoning):
        return (self.token == other.token and
                self.status == other.status and
                self.is_thinking == other.is_thinking)

    def get_dict(self) -> Dict:
        """Возвращает словарное представление рассуждения."""
        if self.label is not None:
            return {"label": self.label, "status": self.status}
        if self.is_thinking is None:
            if self.status is None:
                return {"token": self.token}
            return {"token": self.token, "status": self.status}
        return {"token": self.token, "status": self.status, "is_thinking": self.is_thinking}
```

**Описание**:
Класс для представления информации о процессе рассуждения.

**Методы**:
- `__init__`: Инициализирует объект токеном, статусом и состоянием "размышления".
- `__str__`: Возвращает строковое представление на основе доступных атрибутов.
- `__eq__`: Сравнивает два объекта `Reasoning` на равенство.
- `get_dict`: Возвращает словарное представление рассуждения.

### `Sources`

```python
class Sources(ResponseType):
    def __init__(self, sources: List[Dict[str, str]]) -> None:
        """Инициализирует объект списком словарей источников."""
        self.list = []
        for source in sources:
            self.add_source(source)

    def add_source(self, source: Union[Dict[str, str], str]) -> None:
        """Добавляет источник в список, очищая URL при необходимости."""
        source = source if isinstance(source, dict) else {"url": source}
        url = source.get("url", source.get("link", None))
        if url is not None:
            url = re.sub(r"[&?]utm_source=.+", "", url)
            source["url"] = url
            self.list.append(source)

    def __str__(self) -> str:
        """Возвращает отформатированные источники в виде строки."""
        if not self.list:
            return ""
        return "\\n\\n\\n\\n" + ("\\n>\\n".join([
            f"> [{idx}] {format_link(link['url'], link.get('title', None))}"
            for idx, link in enumerate(self.list)
        ]))
```

**Описание**:
Класс для представления источников информации.

**Методы**:
- `__init__`: Инициализирует объект списком словарей источников.
- `add_source`: Добавляет источник в список, очищая URL при необходимости.
- `__str__`: Возвращает отформатированные источники в виде строки.

### `YouTube`

```python
class YouTube(HiddenResponse):
    def __init__(self, ids: List[str]) -> None:
        """Инициализирует объект списком идентификаторов YouTube видео."""
        self.ids = ids

    def to_string(self) -> str:
        """Возвращает вставки YouTube в виде строки."""
        if not self.ids:
            return ""
        return "\\n\\n" + ("\\n".join([
            f'<iframe type="text/html" src="https://www.youtube.com/embed/{id}"></iframe>'
            for id in self.ids
        ]))
```

**Описание**:
Класс для представления YouTube видео.

**Методы**:
- `__init__`: Инициализирует объект списком идентификаторов YouTube видео.
- `to_string`: Возвращает вставки YouTube в виде строки.

### `AudioResponse`

```python
class AudioResponse(ResponseType):
    def __init__(self, data: Union[bytes, str]) -> None:
        """Инициализирует объект байтами аудиоданных."""
        self.data = data

    def to_uri(self) -> str:
        if isinstance(self.data, str):
            return self.data
        """Возвращает аудиоданные в виде URI, закодированного в base64."""
        data_base64 = base64.b64encode(self.data).decode()
        return f"data:audio/mpeg;base64,{data_base64}"

    def __str__(self) -> str:
        """Возвращает аудио как HTML-элемент."""
        return f'<audio controls src="{self.to_uri()}"></audio>'
```

**Описание**:
Класс для представления аудиоданных.

**Методы**:
- `__init__`: Инициализирует объект байтами аудиоданных.
- `to_uri`: Возвращает аудиоданные в виде URI, закодированного в base64.
- `__str__`: Возвращает аудио как HTML-элемент.

### `BaseConversation`

```python
class BaseConversation(ResponseType):
    def __str__(self) -> str:
        """Возвращает пустую строку по умолчанию."""
        return ""
```

**Описание**:
Базовый класс для представления разговора.

**Методы**:
- `__str__`: Возвращает пустую строку по умолчанию.

### `JsonConversation`

```python
class JsonConversation(BaseConversation, JsonMixin):
    pass
```

**Описание**:
Класс для представления разговора в формате JSON. Наследуется от `BaseConversation` и `JsonMixin`.

### `SynthesizeData`

```python
class SynthesizeData(HiddenResponse, JsonMixin):
    def __init__(self, provider: str, data: Dict) -> None:
        """Инициализирует объект провайдером и данными."""
        self.provider = provider
        self.data = data
```

**Описание**:
Класс для представления синтезированных данных. Наследуется от `HiddenResponse` и `JsonMixin`.

**Методы**:
- `__init__`: Инициализирует объект провайдером и данными.

### `SuggestedFollowups`

```python
class SuggestedFollowups(HiddenResponse):
    def __init__(self, suggestions: list[str]):
        self.suggestions = suggestions
```

**Описание**:
Класс для представления предлагаемых продолжений.

**Методы**:
- `__init__`: Инициализирует объект списком предложений.

### `RequestLogin`

```python
class RequestLogin(HiddenResponse):
    def __init__(self, label: str, login_url: str) -> None:
        """Инициализирует объект меткой и URL для входа."""
        self.label = label
        self.login_url = login_url

    def to_string(self) -> str:
        """Возвращает отформатированную ссылку для входа в виде строки."""
        return format_link(self.login_url, f"[Login to {self.label}]") + "\\n\\n"
```

**Описание**:
Класс для представления запроса на вход.

**Методы**:
- `__init__`: Инициализирует объект меткой и URL для входа.
- `to_string`: Возвращает отформатированную ссылку для входа в виде строки.

### `MediaResponse`

```python
class MediaResponse(ResponseType):
    def __init__(
        self,
        urls: Union[str, List[str]],
        alt: str,
        options: Dict = {},
        **kwargs
    ) -> None:
        """Инициализирует объект изображениями, альтернативным текстом и опциями."""
        self.urls = kwargs.get("images", urls)
        self.alt = alt
        self.options = options

    def get(self, key: str) -> any:
        """Возвращает значение опции по ключу."""
        return self.options.get(key)

    def get_list(self) -> List[str]:
        """Возвращает изображения в виде списка."""
        return [self.urls] if isinstance(self.urls, str) else self.urls
```

**Описание**:
Базовый класс для представления медиа-ответов (изображений, видео).

**Методы**:
- `__init__`: Инициализирует объект URL, альтернативным текстом и опциями.
- `get`: Возвращает значение опции по ключу.
- `get_list`: Возвращает URL в виде списка.

### `ImageResponse`

```python
class ImageResponse(MediaResponse):
    def __str__(self) -> str:
        """Возвращает изображения в виде Markdown."""
        return format_images_markdown(self.urls, self.alt, self.get("preview"))
```

**Описание**:
Класс для представления ответа с изображением.

**Методы**:
- `__str__`: Возвращает изображения в виде Markdown.

### `VideoResponse`

```python
class VideoResponse(MediaResponse):
    def __str__(self) -> str:
        """Возвращает видео в виде HTML-элементов."""
        return "\\n".join([f'<video controls src="{video}"></video>\' for video in self.get_list()])
```

**Описание**:
Класс для представления видео-ответа.

**Методы**:
- `__str__`: Возвращает видео в виде HTML-элементов.

### `ImagePreview`

```python
class ImagePreview(ImageResponse):
    def __str__(self) -> str:
        """Возвращает пустую строку для предварительного просмотра."""
        return ""

    def to_string(self) -> str:
        """Возвращает изображения в виде Markdown."""
        return super().__str__()
```

**Описание**:
Класс для представления предварительного просмотра изображения.

**Методы**:
- `__str__`: Возвращает пустую строку для предварительного просмотра.
- `to_string`: Возвращает изображения в виде Markdown.

### `PreviewResponse`

```python
class PreviewResponse(HiddenResponse):
    def __init__(self, data: str) -> None:
        """Инициализирует объект данными."""
        self.data = data

    def to_string(self) -> str:
        """Возвращает данные в виде строки."""
        return self.data
```

**Описание**:
Класс для представления ответа с предварительным просмотром.

**Методы**:
- `__init__`: Инициализирует объект данными.
- `to_string`: Возвращает данные в виде строки.

### `Parameters`

```python
class Parameters(ResponseType, JsonMixin):
    def __str__(self) -> str:
        """Возвращает пустую строку."""
        return ""
```

**Описание**:
Класс для представления параметров.

**Методы**:
- `__str__`: Возвращает пустую строку.

### `ProviderInfo`

```python
class ProviderInfo(JsonMixin, HiddenResponse):
    pass
```

**Описание**:
Класс для представления информации о провайдере. Наследуется от `JsonMixin` и `HiddenResponse`.