# Проект `hypotez`
# Роль `code explainer`

## АНАЛИЗ КОДА: `src/utils/image.py`

### 1. <алгоритм>

#### save_image_from_url_async
1.  **Начало**: Функция `save_image_from_url_async` принимает URL изображения (`image_url`) и имя файла (`filename`).
2.  **Скачивание изображения**:
    *   Используется `aiohttp.ClientSession` для асинхронного скачивания изображения по URL.
    *   Если возникает ошибка при скачивании, она логируется и возвращается `None`.
        ```python
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                image_data = await response.read()
        ```
3.  **Сохранение изображения**:
    *   Вызывается функция `save_image_async` для сохранения скачанных данных в файл.
        ```python
        return await save_image_async(image_data, filename)
        ```
4.  **Завершение**: Функция возвращает путь к сохраненному файлу или `None` в случае ошибки.

#### save_image
1.  **Начало**: Функция `save_image` принимает бинарные данные изображения (`image_data`), имя файла (`file_name`) и формат (`format`).
2.  **Создание директории**:
    *   Создается директория для файла, если она не существует.
        ```python
        file_path.parent.mkdir(parents=True, exist_ok=True)
        ```
3.  **Сохранение данных изображения**:
    *   Используется `BytesIO` для работы с данными в памяти.
    *   Изображение открывается с помощью `Image.open()`, сохраняется в указанном формате, а затем записывается в файл.
        ```python
        with BytesIO(image_data) as img_io:
            img = Image.open(img_io)
            img_io.seek(0)  # Reset buffer position before saving
            img.save(img_io, format=format)
            img_bytes = img_io.getvalue()

        # Write the formatted image data to the file
        with open(file_path, "wb") as file:
            file.write(img_bytes)
        ```
4.  **Верификация**:
    *   Проверяется, был ли создан файл и не является ли он пустым.
        ```python
        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            # raise ImageError(f"File {file_path} was not created.")

        file_size = file_path.stat().st_size
        if file_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            # raise ImageError(f"File {file_path} saved, but its size is 0 bytes.")
        ```
5.  **Завершение**: Функция возвращает путь к сохраненному файлу или `None` в случае ошибки.

#### save_image_async
1.  **Начало**: Функция `save_image_async` принимает бинарные данные изображения (`image_data`), имя файла (`file_name`) и формат (`format`).
2.  **Создание директории асинхронно**:
    *   Создается директория для файла, если она не существует, используя `asyncio.to_thread`.
        ```python
        await asyncio.to_thread(file_path.parent.mkdir, parents=True, exist_ok=True)
        ```
3.  **Сохранение данных изображения асинхронно**:
    *   Используется `aiofiles` для асинхронной записи данных изображения в файл.
        ```python
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)
        ```
4.  **Верификация асинхронно**:
    *   Проверяется, был ли создан файл и не является ли он пустым, используя `aiofiles`.
        ```python
        if not await aiofiles.os.path.exists(file_path):
            logger.error(f"File {file_path} was not created.", ex, exc_info=True)
            # raise ImageError(f"File {file_path} was not created.")

        file_size = await aiofiles.os.path.getsize(file_path)
        if file_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.", ex, exc_info=True)
            # raise ImageError(f"File {file_path} saved, but its size is 0 bytes.")
        ```
5.  **Завершение**: Функция возвращает путь к сохраненному файлу или `None` в случае ошибки.

#### get_image_bytes
1.  **Начало**: Функция `get_image_bytes` принимает путь к изображению (`image_path`) и флаг `raw`.
2.  **Чтение изображения**:
    *   Изображение открывается с помощью `Image.open()`.
    *   Сохраняется в формате JPEG в `BytesIO` объект.
        ```python
        img = Image.open(image_path)
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="JPEG")
        ```
3.  **Возврат данных**:
    *   Возвращается `BytesIO` объект или его содержимое в виде `bytes` в зависимости от значения `raw`.
        ```python
        return img_byte_arr if raw else img_byte_arr.getvalue()
        ```
4.  **Завершение**: Функция возвращает данные изображения или `None` в случае ошибки.

#### get_raw_image_data
1.  **Начало**: Функция `get_raw_image_data` принимает имя файла (`file_name`).
2.  **Проверка существования файла**:
    *   Проверяется, существует ли файл по указанному пути.
        ```python
        if not file_path.exists():
            logger.error(f"File {file_path} does not exist.")
            return None
        ```
3.  **Чтение данных файла**:
    *   Если файл существует, его содержимое считывается в виде `bytes`.
        ```python
        return file_path.read_bytes()
        ```
4.  **Завершение**: Функция возвращает бинарные данные файла или `None` в случае ошибки или отсутствия файла.

#### random_image
1.  **Начало**: Функция `random_image` принимает корневой путь (`root_path`).
2.  **Поиск изображений**:
    *   Рекурсивно ищет файлы изображений с определенными расширениями в указанной директории.
        ```python
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        image_files = [file_path for file_path in root_path.rglob("*") 
                       if file_path.is_file() and file_path.suffix.lower() in image_extensions]
        ```
3.  **Выбор случайного изображения**:
    *   Если изображения найдены, выбирается случайное изображение из списка.
        ```python
        return str(random.choice(image_files))
        ```
4.  **Завершение**: Функция возвращает путь к случайному изображению или `None`, если изображения не найдены.

#### add_text_watermark
1.  **Начало**: Функция `add_text_watermark` принимает путь к изображению (`image_path`), текст водяного знака (`watermark_text`) и путь для сохранения (`output_path`).
2.  **Открытие изображения**:
    *   Открывается изображение и конвертируется в формат RGBA.
        ```python
        image = Image.open(image_path).convert("RGBA")
        ```
3.  **Создание водяного знака**:
    *   Создается прозрачный слой для водяного знака.
    *   Определяется размер шрифта на основе размера изображения.
    *   Текст водяного знака рисуется на прозрачном слое.
        ```python
        watermark_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_layer)

        font_size = min(image.size) // 10  # Adjust the font size based on the image
        try:
            font = ImageFont.truetype("arial.ttf", size=font_size)
        except IOError:
            font = ImageFont.load_default(size=font_size)
            logger.warning("Font arial.ttf not found; using default font.")

        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2

        # Draw text on the transparent layer
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
        ```
4.  **Композиция и сохранение**:
    *   Изображение и водяной знак объединяются.
    *   Сохраняется новое изображение.
        ```python
        watermarked_image = Image.alpha_composite(image, watermark_layer)
        watermarked_image.save(output_path)
        ```
5.  **Завершение**: Функция возвращает путь к изображению с водяным знаком или `None` в случае ошибки.

#### add_image_watermark
1.  **Начало**: Функция `add_image_watermark` принимает пути к основному изображению (`input_image_path`), изображению водяного знака (`watermark_image_path`) и путь для сохранения (`output_image_path`).
2.  **Открытие изображений**:
    *   Открываются основное изображение и изображение водяного знака.
        ```python
        base_image = Image.open(input_image_path)
        watermark = Image.open(watermark_image_path).convert("RGBA")
        ```
3.  **Изменение размера и позиционирование водяного знака**:
    *   Изменяется размер водяного знака.
    *   Определяется позиция для размещения водяного знака.
        ```python
        position = base_image.size  # Size of the base image (width, height)
        newsize = (int(position[0] * 8 / 100), int(position[0] * 8 / 100))  # New size of the watermark
        watermark = watermark.resize(newsize)  # Resize the watermark

        # Determine the position to place the watermark (bottom-right corner with 20px padding)
        new_position = position[0] - newsize[0] - 20, position[1] - newsize[1] - 20
        ```
4.  **Композиция и сохранение**:
    *   Создается прозрачный слой, на который накладываются основное изображение и водяной знак.
    *   Сохраняется новое изображение.
        ```python
        transparent = Image.new(mode='RGBA', size=position, color=(0, 0, 0, 0))

        # Paste the base image onto the new layer
        transparent.paste(base_image, (0, 0))

        # Paste the watermark on top of the base image
        transparent.paste(watermark, new_position, watermark)
        ```
5.  **Завершение**: Функция возвращает путь к изображению с водяным знаком или `None` в случае ошибки.

#### resize_image
1.  **Начало**: Функция `resize_image` принимает путь к изображению (`image_path`), размер (`size`) и путь для сохранения (`output_path`).
2.  **Открытие и изменение размера изображения**:
    *   Открывается изображение и изменяется его размер.
        ```python
        img = Image.open(image_path)
        resized_img = img.resize(size)
        ```
3.  **Сохранение изображения**:
    *   Сохраняется изображение нового размера.
        ```python
        resized_img.save(output_path)
        ```
4.  **Завершение**: Функция возвращает путь к измененному изображению или `None` в случае ошибки.

#### convert_image
1.  **Начало**: Функция `convert_image` принимает путь к изображению (`image_path`), формат (`format`) и путь для сохранения (`output_path`).
2.  **Открытие и конвертация изображения**:
    *   Открывается изображение и конвертируется в указанный формат.
        ```python
        img = Image.open(image_path)
        img.save(output_path, format=format)
        ```
3.  **Завершение**: Функция возвращает путь к конвертированному изображению или `None` в случае ошибки.

#### process_images_with_watermark
1.  **Начало**: Функция `process_images_with_watermark` принимает путь к папке (`folder_path`) и путь к изображению водяного знака (`watermark_path`).
2.  **Проверка директории**:
    *   Проверяется, существует ли указанная директория.
        ```python
        if not folder_path.is_dir():
            logger.error(f"Folder {folder_path} does not exist.")
            return
        ```
3.  **Создание выходной директории**:
    *   Создается директория "output", если она не существует.
        ```python
        output_dir = folder_path / "output"
        output_dir.mkdir(parents=True, exist_ok=True)
        ```
4.  **Обработка изображений**:
    *   Для каждого файла изображения в папке вызывается функция `add_image_watermark` для добавления водяного знака.
        ```python
        for file_path in folder_path.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
                output_image_path = output_dir / file_path.name
                add_image_watermark(file_path, watermark_path, output_image_path)
        ```
5.  **Завершение**: Функция не возвращает значения.

### 2. <mermaid>

```mermaid
flowchart TD
    subgraph Image Processing
        A[save_image_from_url_async] --> B(save_image_async)
        C[save_image] --> D{BytesIO}
        D --> E[Image.open]
        E --> F[img.save]
        G[get_image_bytes] --> H[Image.open]
        H --> I[img.save]
        J[get_raw_image_data] --> K{file_path.read_bytes()}
        L[random_image] --> M{root_path.rglob("*")}
        N[add_text_watermark] --> O[Image.open]
        O --> P{ImageDraw.Draw}
        Q[add_image_watermark] --> R[Image.open]
        R --> S[watermark.resize]
        S --> T{transparent.paste}
        U[resize_image] --> V[Image.open]
        V --> W[img.resize]
        X[convert_image] --> Y[Image.open]
        Y --> Z[img.save]
        AA[process_images_with_watermark] --> BB(add_image_watermark)
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#f9f,stroke:#333,stroke-width:2px
    style J fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#f9f,stroke:#333,stroke-width:2px
    style N fill:#f9f,stroke:#333,stroke-width:2px
    style Q fill:#f9f,stroke:#333,stroke-width:2px
    style U fill:#f9f,stroke:#333,stroke-width:2px
    style X fill:#f9f,stroke:#333,stroke-width:2px
     style AA fill:#f9f,stroke:#333,stroke-width:2px
```

**Объяснение диаграммы:**

*   **save\_image\_from\_url\_async**: Асинхронно скачивает изображение по URL и вызывает `save_image_async` для его сохранения.
*   **save\_image\_async**: Асинхронно сохраняет изображение в файл.
*   **save\_image**: Сохраняет изображение в файл, используя `BytesIO` для работы с данными в памяти.
*   **get\_image\_bytes**: Читает изображение и возвращает его байты в формате JPEG.
*   **get\_raw\_image\_data**: Читает бинарные данные файла.
*   **random\_image**: Ищет случайное изображение в указанной директории.
*   **add\_text\_watermark**: Добавляет текстовый водяной знак на изображение.
*   **add\_image\_watermark**: Добавляет изображение в качестве водяного знака на другое изображение.
*   **resize\_image**: Изменяет размер изображения.
*   **convert\_image**: Конвертирует изображение в указанный формат.
*   **process\_images\_with\_watermark**: Обрабатывает все изображения в указанной папке, добавляя водяной знак.

**Зависимости:**

*   `aiohttp`: Используется для асинхронных HTTP-запросов.
*   `aiofiles`: Используется для асинхронной работы с файлами.
*   `asyncio`: Используется для асинхронного программирования.
*   `random`: Используется для выбора случайного изображения.
*   `pathlib.Path`: Используется для работы с путями к файлам и директориям.
*   `typing`: Используется для аннотации типов.
*   `io.BytesIO`: Используется для работы с данными в памяти как с файлами.
*   `PIL (Pillow)`: Используется для обработки изображений.
*   `src.logger.logger`: Используется для логирования.

### 3. <объяснение>

#### Импорты:

*   `aiohttp`: Асинхронный HTTP клиент/сервер. Используется для асинхронной загрузки изображений из URL.
*   `aiofiles`: Асинхронная файловая библиотека для асинхронной записи изображений в файлы.
*   `asyncio`: Библиотека для написания конкурентного кода с использованием синтаксиса async/await.
*   `random`: Генератор случайных чисел. Используется для выбора случайного изображения.
*   `pathlib.Path`: Объектно-ориентированный способ представления путей файловой системы.
*   `typing.Optional, typing.Union, typing.Tuple`: Используется для аннотации типов.
*   `io.BytesIO`: Работа с байтовыми потоками в памяти. Используется для обработки изображений без сохранения на диск.
*   `PIL (Pillow)`: Библиотека для работы с изображениями. Предоставляет функции для открытия, изменения размера, добавления водяных знаков и сохранения изображений.
*   `src.logger.logger`: Модуль логирования из проекта `hypotez`. Используется для записи информации об ошибках и других событиях.

#### Классы:

*   `ImageError(Exception)`: Пользовательское исключение для ошибок, связанных с обработкой изображений.

#### Функции:

*   `save_image_from_url_async(image_url: str, filename: Union[str, Path]) -> Optional[str]`:
    *   **Аргументы**:
        *   `image_url` (str): URL изображения.
        *   `filename` (Union[str, Path]): Имя файла для сохранения изображения.
    *   **Возвращает**: Путь к сохраненному файлу (str) или None в случае ошибки.
    *   **Назначение**: Асинхронно скачивает изображение из URL и сохраняет его локально.
    *   **Пример**:
        ```python
        image_path = await save_image_from_url_async('http://example.com/image.jpg', 'image.jpg')
        if image_path:
            print(f'Image saved to {image_path}')
        ```

*   `save_image(image_data: bytes, file_name: str | Path, format: str = 'PNG') -> Optional[str]`:
    *   **Аргументы**:
        *   `image_data` (bytes): Бинарные данные изображения.
        *   `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
        *   `format` (str): Формат изображения (по умолчанию 'PNG').
    *   **Возвращает**: Путь к сохраненному файлу (str) или None в случае ошибки.
    *   **Назначение**: Сохраняет данные изображения в файл в указанном формате.
    *   **Пример**:
        ```python
        with open('image.png', 'rb') as f:
            image_data = f.read()
        image_path = save_image(image_data, 'new_image.png')
        if image_path:
            print(f'Image saved to {image_path}')
        ```

*   `save_image_async(image_data: bytes, file_name: str | Path, format: str = 'PNG') -> Optional[str]`:
    *   **Аргументы**:
        *   `image_data` (bytes): Бинарные данные изображения.
        *   `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
        *   `format` (str): Формат изображения (по умолчанию 'PNG').
    *   **Возвращает**: Путь к сохраненному файлу (str) или None в случае ошибки.
    *   **Назначение**: Асинхронно сохраняет данные изображения в файл в указанном формате.
    *   **Пример**:
        ```python
        with open('image.png', 'rb') as f:
            image_data = f.read()
        image_path = await save_image_async(image_data, 'new_image.png')
        if image_path:
            print(f'Image saved to {image_path}')
        ```

*   `get_image_bytes(image_path: Path, raw: bool = True) -> Optional[BytesIO | bytes]`:
    *   **Аргументы**:
        *   `image_path` (Path): Путь к файлу изображения.
        *   `raw` (bool): Если True, возвращает BytesIO объект, иначе возвращает bytes (по умолчанию True).
    *   **Возвращает**: Байты изображения в формате JPEG (BytesIO или bytes) или None в случае ошибки.
    *   **Назначение**: Читает изображение и возвращает его байты.
    *   **Пример**:
        ```python
        image_bytes = get_image_bytes(Path('image.png'))
        if image_bytes:
            print(f'Image bytes: {image_bytes[:100]}...')
        ```

*   `get_raw_image_data(file_name: Union[str, Path]) -> Optional[bytes]`:
    *   **Аргументы**:
        *   `file_name` (Union[str, Path]): Имя файла.
    *   **Возвращает**: Бинарные данные файла (bytes) или None, если файл не существует или произошла ошибка.
    *   **Назначение**: Получает бинарные данные файла.
    *   **Пример**:
        ```python
        file_data = get_raw_image_data('data.txt')
        if file_data:
            print(f'File data: {file_data[:100]}...')
        ```

*   `random_image(root_path: Union[str, Path]) -> Optional[str]`:
    *   **Аргументы**:
        *   `root_path` (Union[str, Path]): Путь к директории для поиска изображений.
    *   **Возвращает**: Путь к случайному изображению (str) или None, если изображения не найдены.
    *   **Назначение**: Ищет случайное изображение в указанной директории.
    *   **Пример**:
        ```python
        random_image_path = random_image('images')
        if random_image_path:
            print(f'Random image: {random_image_path}')
        ```

*   `add_text_watermark(image_path: str | Path, watermark_text: str, output_path: Optional[str | Path] = None) -> Optional[str]`:
    *   **Аргументы**:
        *   `image_path` (Union[str, Path]): Путь к файлу изображения.
        *   `watermark_text` (str): Текст водяного знака.
        *   `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком (по умолчанию перезаписывает оригинальное изображение).
    *   **Возвращает**: Путь к изображению с водяным знаком (str) или None в случае ошибки.
    *   **Назначение**: Добавляет текстовый водяной знак на изображение.
    *   **Пример**:
        ```python
        watermarked_image_path = add_text_watermark('image.png', 'Watermark')
        if watermarked_image_path:
            print(f'Watermarked image: {watermarked_image_path}')
        ```

*   `add_image_watermark(input_image_path: Path, watermark_image_path: Path, output_image_path: Optional[Path] = None) -> Optional[Path]`:
    *   **Аргументы**:
        *   `input_image_path` (Path): Путь к основному изображению.
        *   `watermark_image_path` (Path): Путь к изображению водяного знака.
        *   `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком (по умолчанию сохраняется в директории "output").
    *   **Возвращает**: Путь к изображению с водяным знаком (Path) или None в случае ошибки.
    *   **Назначение**: Добавляет изображение в качестве водяного знака на другое изображение.
    *   **Пример**:
        ```python
        watermarked_image_path = add_image_watermark(Path('image.png'), Path('watermark.png'))
        if watermarked_image_path:
            print(f'Watermarked image: {watermarked_image_path}')
        ```

*   `resize_image(image_path: Union[str, Path], size: Tuple[int, int], output_path: Optional[Union[str, Path]] = None) -> Optional[str]`:
    *   **Аргументы**:
        *   `image_path` (Union[str, Path]): Путь к файлу изображения.
        *   `size` (Tuple[int, int]): Новый размер изображения (ширина, высота).
        *   `output_path` (Optional[Union[str, Path]]): Путь для сохранения измененного изображения (по умолчанию перезаписывает оригинальное изображение).
    *   **Возвращает**: Путь к измененному изображению (str) или None в случае ошибки.
    *   **Назначение**: Изменяет размер изображения.
    *   **Пример**:
        ```python
        resized_image_path = resize_image('image.png', (500, 500))
        if resized_image_path:
            print(f'Resized image: {resized_image_path}')
        ```

*   `convert_image(image_path: Union[str, Path], format: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]`:
    *   **Аргументы**:
        *   `image_path` (Union[str, Path]): Путь к файлу изображения.
        *   `format` (str): Формат изображения (например, "JPEG", "PNG").
        *   `output_path` (Optional[Union[str, Path]]): Путь для сохранения конвертированного изображения (по умолчанию перезаписывает оригинальное изображение).
    *   **Возвращает**: Путь к конвертированному изображению (str) или None в случае ошибки.
    *   **Назначение**: Конвертирует изображение в указанный формат.
    *   **Пример**:
        ```python
        converted_image_path = convert_image('image.png', 'JPEG')
        if converted_image_path:
            print(f'Converted image: {converted_image_path}')
        ```

*   `process_images_with_watermark(folder_path: Path, watermark_path: Path) -> None`:
    *   **Аргументы**:
        *   `folder_path` (Path): Путь к папке с изображениями.
        *   `watermark_path` (Path): Путь к изображению водяного знака.
    *   **Возвращает**: None.
    *   **Назначение**: Обрабатывает все изображения в указанной папке, добавляя водяной знак и сохраняя их в директории "output".
    *   **Пример**:
        ```python
        process_images_with_watermark(Path('images'), Path('watermark.png'))
        ```

#### Переменные:

*   `image_extensions`: Список расширений файлов, которые считаются изображениями.

#### Потенциальные ошибки и области для улучшения:

1.  **Обработка исключений**:
    *   Во многих функциях есть блоки `try...except`, которые логируют ошибки, но затем продолжают выполнение. В некоторых случаях может быть лучше прекратить выполнение функции и вернуть ошибку.

2.  **Асинхронность**:
    *   Не все функции используют асинхронность, хотя могли бы. Например, `get_raw_image_data` и `random_image` могут быть переписаны для использования асинхронных операций.

3.  **Валидация ввода**:
    *   Некоторые функции не проверяют входные данные на корректность. Например, `resize_image` не проверяет, что `size` является кортежем из двух положительных чисел.

4.  **Обработка путей**:
    *   В некоторых функциях пути к файлам создаются с использованием `/`, что может быть несовместимо с разными операционными системами. Лучше использовать `os.path.join` или `pathlib.Path` для создания путей.

5.  **Водяные знаки**:
    *   Функции для добавления водяных знаков не позволяют настраивать положение и прозрачность водяного знака.

#### Взаимосвязи с другими частями проекта:

*   Этот модуль использует `src.logger.logger` для логирования ошибок и информации о работе функций. Он является частью системы логирования проекта `hypotez`.
*   Функции `save_image_from_url_async`, `save_image_async` и `get_raw_image_data` используют асинхронные операции, что позволяет им эффективно работать в асинхронных приложениях, таких как веб-серверы или боты.
*   Функция `process_images_with_watermark` может быть использована для автоматической обработки изображений в пакете, например, для добавления водяных знаков на все изображения в папке перед их публикацией.