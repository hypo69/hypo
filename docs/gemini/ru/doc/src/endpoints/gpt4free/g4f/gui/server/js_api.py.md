# Документация модуля `js_api.py`

## Обзор

Модуль `js_api.py` предоставляет класс `JsApi`, который служит интерфейсом между JavaScript-кодом в веб-интерфейсе и Python-кодом, выполняющим логику взаимодействия с различными провайдерами, например, для получения ответов от языковых моделей. Класс позволяет получать ввод от пользователя через веб-интерфейс, отправлять запросы к API и отображать результаты в веб-интерфейсе.

## Подробней

Этот модуль обеспечивает взаимодействие между веб-интерфейсом (GUI) и серверной частью приложения, используя библиотеку `webview` для создания окон и выполнения JavaScript-кода. Он включает функциональность для получения пользовательского ввода, выбора изображений, работы с камерой и обмена данными с различными API. Модуль предназначен для интеграции с различными провайдерами языковых моделей.
## Классы

### `JsApi`

**Описание**: Класс `JsApi` расширяет класс `Api` и предоставляет API для взаимодействия JavaScript-кода в веб-интерфейсе с Python-кодом.

**Наследует**:
- `Api`: Класс `JsApi` наследует функциональность от класса `Api`.

**Методы**:

- `get_conversation(options: dict, message_id: str = None, scroll: bool = None) -> Iterator`: Получает сообщения для текущего разговора.
- `choose_image()`: Позволяет пользователю выбрать изображение из файловой системы.
- `take_picture()`: Позволяет пользователю сделать снимок с камеры.
- `on_image_selection(self, filename)`: Обрабатывает выбор изображения пользователем.
- `on_camera(self, filename)`: Обрабатывает событие получения снимка с камеры.
- `set_selected(input_id: str = None)`: Управляет визуальным выделением выбранного элемента (например, изображения или камеры) в веб-интерфейсе.
- `get_version()`: Возвращает версию API.
- `get_models()`: Возвращает список доступных моделей.
- `get_providers()`: Возвращает список доступных провайдеров.
- `get_provider_models(provider: str, **kwargs)`: Возвращает список моделей, доступных у указанного провайдера.

---

## Функции

### `get_conversation`

```python
def get_conversation(self, options: dict, message_id: str = None, scroll: bool = None) -> Iterator:
    """Получает сообщения для текущего разговора.

    Args:
        options (dict): Словарь с различными опциями для настройки разговора.
        message_id (str, optional): ID сообщения, с которого нужно начать. По умолчанию `None`.
        scroll (bool, optional): Флаг, указывающий нужно ли прокручивать окно. По умолчанию `None`.

    Returns:
        Iterator: Итератор, предоставляющий сообщения для разговора.

    Как работает функция:
    1. Извлекает окно веб-просмотра.
    2. Проверяет, было ли выбрано изображение, и если да, открывает его для отправки.
    3. Итерируется по сообщениям, полученным из `_create_response_stream`, подготавливая аргументы разговора через `_prepare_conversation_kwargs`.
    4. Для каждого сообщения вызывает JavaScript-функцию `add_message_chunk` для добавления сообщения в веб-интерфейс.
    5. Проверяет, не была ли остановлена отправка сообщений через JavaScript-функцию `is_stopped`.
    6. Сбрасывает выбранное изображение и выделение.
    """

    #   Начало
    #   ↓
    #   Получение окна webview  - window = webview.windows[0]
    #   ↓
    #   Проверка наличия изображения - if hasattr(self, "image") and self.image is not None:
    #   ↓
    #   Подготовка аргументов разговора - _prepare_conversation_kwargs(options)
    #   ↓
    #   Создание потока ответов - _create_response_stream(...)
    #   ↓
    #   Цикл по сообщениям в потоке
    #   │
    #   │   window.evaluate_js(f"is_stopped() ? true : this.add_message_chunk(...)")
    #   │   ↓
    #   │   Проверка остановки - is_stopped()
    #   │
    #   Конец цикла
    #   ↓
    #   Сброс изображения - self.image = None, self.set_selected(None)
    #   ↓
    #   Конец
    window = webview.windows[0]
    if hasattr(self, "image") and self.image is not None:
        options["image"] = open(self.image, "rb")
    for message in self._create_response_stream(
        self._prepare_conversation_kwargs(options),
        options.get("conversation_id"),
        options.get('provider')
    ):
        if window.evaluate_js(
            f"""
                is_stopped() ? true :
                this.add_message_chunk({{
                    json.dumps(message)
                }}, {{
                    json.dumps(message_id)
                }}, {{
                    json.dumps(options.get('provider'))
                }}, {{
                    \'true\' if scroll else \'false\'
                }}); is_stopped();
            """) == True:
            break
    self.image = None
    self.set_selected(None)
### `choose_image`

```python
def choose_image(self):
    """Открывает диалоговое окно для выбора изображения.

    Как работает функция:
    1. Вызывает функцию `user_select_image` из модуля `plyer.filechooser`, чтобы открыть диалоговое окно выбора файла.
    2. Устанавливает обратный вызов `on_selection` для обработки выбранного изображения.
    """
    #   Начало
    #   ↓
    #   Вызов диалогового окна выбора файла - user_select_image(on_selection=self.on_image_selection)
    #   ↓
    #   Конец
    user_select_image(
        on_selection=self.on_image_selection
    )
```
### `take_picture`

```python
def take_picture(self):
    """Делает снимок с камеры и сохраняет его во временный файл.

    Как работает функция:
    1. Формирует имя файла для сохранения снимка, используя UUID для уникальности.
    2. Вызывает функцию `camera.take_picture` из модуля `plyer`, чтобы сделать снимок.
    3. Устанавливает обратный вызов `on_complete` для обработки завершения операции камеры.
    """
    #   Начало
    #   ↓
    #   Формирование имени файла - filename = os.path.join(app_storage_path(), f"chat-{uuid4()}.png")
    #   ↓
    #   Вызов камеры - camera.take_picture(filename=filename, on_complete=self.on_camera)
    #   ↓
    #   Конец
    filename = os.path.join(app_storage_path(), f"chat-{uuid4()}.png")
    camera.take_picture(filename=filename, on_complete=self.on_camera)
```
### `on_image_selection`

```python
def on_image_selection(self, filename):
    """Обрабатывает выбор изображения пользователем.

    Args:
        filename (str): Имя выбранного файла.

    Как работает функция:
    1. Проверяет, является ли `filename` списком и извлекает первый элемент, если это так.
    2. Проверяет существование выбранного файла.
    3. Устанавливает атрибут `self.image` в имя выбранного файла.
    4. Вызывает функцию `set_selected` для обновления визуального состояния элемента "image" в веб-интерфейсе.
    """

    #   Начало
    #   ↓
    #   Проверка и извлечение имени файла - filename = filename[0] if isinstance(filename, list) and filename else filename
    #   ↓
    #   Проверка существования файла - if filename and os.path.exists(filename):
    #   │
    #   │   Установка self.image = filename
    #   │
    #   Установка self.image = None
    #   ↓
    #   Вызов set_selected - self.set_selected(None if self.image is None else "image")
    #   ↓
    #   Конец
    filename = filename[0] if isinstance(filename, list) and filename else filename
    if filename and os.path.exists(filename):
        self.image = filename
    else:
        self.image = None
    self.set_selected(None if self.image is None else "image")
```

### `on_camera`

```python
def on_camera(self, filename):
    """Обрабатывает событие получения снимка с камеры.

    Args:
        filename (str): Имя файла, в который был сохранен снимок.

    Как работает функция:
    1. Проверяет существование файла со снимком.
    2. Устанавливает атрибут `self.image` в имя файла со снимком.
    3. Вызывает функцию `set_selected` для обновления визуального состояния элемента "camera" в веб-интерфейсе.
    """

    #   Начало
    #   ↓
    #   Проверка существования файла - if filename and os.path.exists(filename):
    #   │
    #   │   Установка self.image = filename
    #   │
    #   Установка self.image = None
    #   ↓
    #   Вызов set_selected - self.set_selected(None if self.image is None else "camera")
    #   ↓
    #   Конец

    if filename and os.path.exists(filename):
        self.image = filename
    else:
        self.image = None
    self.set_selected(None if self.image is None else "camera")
```

### `set_selected`

```python
def set_selected(self, input_id: str = None):
    """Устанавливает визуальное выделение для выбранного элемента интерфейса.

    Args:
        input_id (str, optional): ID выбранного элемента. По умолчанию `None`.

    Как работает функция:
    1. Получает ссылку на окно веб-интерфейса.
    2. Удаляет класс "selected" у предыдущего выбранного элемента (если есть).
    3. Если `input_id` указан и является "image" или "camera", добавляет класс "selected" к соответствующему элементу.
    """
    #   Начало
    #   ↓
    #   Получение окна webview - window = webview.windows[0]
    #   ↓
    #   Удаление класса "selected" у предыдущего элемента - document.querySelector(`.image-label.selected`)?.classList.remove(`selected`)
    #   ↓
    #   Проверка input_id - if input_id is not None and input_id in ("image", "camera"):
    #   │
    #   │   Добавление класса "selected" к элементу - document.querySelector(`label[for="{input_id}"]`)?.classList.add(`selected`)
    #   │
    #   Конец
    window = webview.windows[0]
    if window is not None:
        window.evaluate_js(
            f"document.querySelector(`.image-label.selected`)?.classList.remove(`selected`);"
        )
        if input_id is not None and input_id in ("image", "camera"):
            window.evaluate_js(
                f'document.querySelector(`label[for="{input_id}"]`)?.classList.add(`selected`);'
            )
```

### `get_version`

```python
def get_version(self):
    """Возвращает версию API.

    Returns:
        str: Версия API.
    """
    return super().get_version()
```

### `get_models`

```python
def get_models(self):
    """Возвращает список доступных моделей.

    Returns:
        list: Список доступных моделей.
    """
    return super().get_models()
```

### `get_providers`

```python
def get_providers(self):
    """Возвращает список доступных провайдеров.

    Returns:
        list: Список доступных провайдеров.
    """
    return super().get_providers()
```

### `get_provider_models`

```python
def get_provider_models(self, provider: str, **kwargs):
    """Возвращает список моделей, доступных у указанного провайдера.

    Args:
        provider (str): Имя провайдера.
        **kwargs: Дополнительные аргументы.

    Returns:
        list: Список моделей, доступных у указанного провайдера.
    """
    return super().get_provider_models(provider, **kwargs)