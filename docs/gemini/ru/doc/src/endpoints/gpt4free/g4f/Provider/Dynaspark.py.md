# Модуль Dynaspark

## Обзор

Модуль `Dynaspark` предоставляет асинхронный генератор для взаимодействия с API Dynaspark для получения ответов от AI моделей, включая модели Gemini. Он поддерживает передачу текстовых сообщений и изображений. Модуль предназначен для использования в асинхронных приложениях.

## Подробней

Модуль реализует взаимодействие с Dynaspark API через асинхронные запросы. Он использует `aiohttp` для отправки запросов и `FormData` для передачи данных, включая текст и изображения. Поддерживается потоковая передача ответов от сервера.

## Классы

### `Dynaspark`

**Описание**: Класс `Dynaspark` является асинхронным провайдером, который реализует взаимодействие с API Dynaspark. Он поддерживает текстовые и визуальные запросы к различным моделям Gemini.

**Принцип работы**:
Класс использует `aiohttp.ClientSession` для отправки асинхронных HTTP-запросов к API Dynaspark. Основной метод `create_async_generator` формирует запрос с необходимыми данными (текстовые сообщения, изображения, параметры модели) и отправляет его на сервер. Ответ от сервера возвращается как асинхронный генератор, который выдает части ответа по мере их поступления.

**Атрибуты класса**:
- `url` (str): URL Dynaspark.
- `login_url` (Optional[str]): URL для логина (в данном случае `None`).
- `api_endpoint` (str): URL API Dynaspark для генерации ответов.
- `working` (bool): Флаг, указывающий, что провайдер работает (в данном случае `True`).
- `needs_auth` (bool): Флаг, указывающий необходимость аутентификации (в данном случае `False`).
- `use_nodriver` (bool): Флаг, указывающий на использование драйвера (в данном случае `True`).
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи (в данном случае `True`).
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений (в данном случае `False`).
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений (в данном случае `False`).
- `default_model` (str): Модель, используемая по умолчанию (`gemini-1.5-flash`).
- `default_vision_model` (str): Модель для обработки изображений по умолчанию.
- `vision_models` (List[str]): Список поддерживаемых моделей для обработки изображений.
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

## Функции

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        media: MediaListType = None,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для получения ответов от API Dynaspark.

        Args:
            model (str): Имя модели, используемой для генерации ответа.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            media (MediaListType, optional): Список медиафайлов (изображений) для отправки в API. По умолчанию `None`.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий части ответа от API.

        Raises:
            Exception: Если возникает ошибка при отправке запроса или обработке ответа.

        Как работает функция:
        1. **Формирование заголовков**: Функция создает заголовки HTTP-запроса, включая `accept`, `accept-language`, `origin`, `referer` и `user-agent`.
        2. **Создание асинхронной сессии**: Создается асинхронная сессия `aiohttp.ClientSession` с заданными заголовками.
        3. **Формирование данных формы**: Создается объект `FormData` для отправки данных в формате multipart/form-data. В форму добавляются текстовые сообщения (`user_input`) и имя модели (`ai_model`).
        4. **Обработка медиафайлов**: Если переданы медиафайлы (изображения), функция извлекает первый файл, преобразует его в байты и добавляет в форму с соответствующим именем файла и типом содержимого.
        5. **Отправка запроса**: Функция отправляет POST-запрос на `cls.api_endpoint` с данными формы и прокси-сервером (если указан).
        6. **Обработка ответа**: После получения ответа функция проверяет статус код, преобразует текст ответа в JSON и извлекает поле `response`.
        7. **Генерация результата**: Извлеченное значение `response` передается в генератор `yield`, который возвращает его вызывающей стороне.

        Внутри функции происхоят следующие действия и преобразования:
            - `create_headers` - Формирование заголовков HTTP-запроса.
            |
            - `create_session` - Создание асинхронной сессии для отправки запроса.
            |
            - `create_form_data` - Формирование данных формы, включая текстовые сообщения и медиафайлы.
            |
            - `send_request` - Отправка POST-запроса на API endpoint.
            |
            - `process_response` - Обработка ответа от сервера и извлечение данных.
            |
            - `yield_response` - Передача результата в генератор.

        Примеры:
            >>> model = "gemini-1.5-flash"
            >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
            >>> async for response in Dynaspark.create_async_generator(model=model, messages=messages):
            ...     print(response)
            'I am doing well, thank you for asking. How can I help you today?'

            >>> model = "gemini-1.5-flash"
            >>> messages = [{"role": "user", "content": "Describe this image."}]
            >>> media = [("image.jpg", b"image_bytes")]
            >>> async for response in Dynaspark.create_async_generator(model=model, messages=messages, media=media):
            ...     print(response)
            'The image shows...'
        """
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://dynaspark.onrender.com',
            'referer': 'https://dynaspark.onrender.com/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        async with ClientSession(headers=headers) as session:
            form = FormData()
            form.add_field('user_input', format_prompt(messages))
            form.add_field('ai_model', model)

            if media is not None and len(media) > 0:
                image, image_name = media[0]
                image_bytes = to_bytes(image)
                form.add_field('file', image_bytes, filename=image_name, content_type=is_accepted_format(image_bytes))

            async with session.post(f"{cls.api_endpoint}", data=form, proxy=proxy) as response:
                await raise_for_status(response)
                response_text = await response.text()
                response_json = json.loads(response_text)
                yield response_json["response"]