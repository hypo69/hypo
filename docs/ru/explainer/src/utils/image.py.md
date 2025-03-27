## <алгоритм>

### save_image_from_url
1.  **Начало:** Функция принимает `image_url` (URL изображения) и `filename` (имя файла для сохранения).
2.  **Загрузка изображения:**
    *   Используется `aiohttp.ClientSession` для асинхронной отправки GET-запроса по `image_url`.
    *   Если запрос успешен (код 200), читаются данные изображения (`image_data`).
    *   **Пример:** `image_url = "https://example.com/image.png"`, `filename = "local_image.png"`
3.  **Обработка ошибок:** Если при загрузке происходит ошибка (например, недоступный URL), выводится сообщение в лог и поднимается исключение `ImageError`.
4.  **Сохранение изображения:**
    *   Вызывается функция `save_image` для сохранения `image_data` в файл `filename`.
    *   **Поток данных:** `image_data` передается в `save_image`.
5.  **Возврат:** Функция возвращает путь к сохраненному файлу или `None`, если возникла ошибка.

### save_image
1.  **Начало:** Функция принимает `image_data` (байты изображения), `file_name` (имя файла) и `format` (формат изображения, по умолчанию "PNG").
2.  **Создание директории:**
    *   Формируется путь к файлу `file_path` на основе `file_name`.
    *   Создаются все родительские директории, если их нет.
    *   **Пример:** `file_name = "path/to/image.png"` - создается директория `path/to/`
3.  **Сохранение данных в файл:**
    *   Асинхронно открывается файл на запись (в режиме "wb").
    *   В файл записываются данные `image_data`.
4.  **Проверка файла:**
    *   Проверяется, что файл был создан и существует. Если нет, выбрасывается исключение `ImageError`.
    *   Проверяется, что размер файла больше 0 байт. Если файл пустой, выбрасывается исключение `ImageError`.
5.  **Форматирование:** Изображение открывается с помощью `PIL.Image.open` и сохраняется в нужном формате.
6.  **Возврат:** Функция возвращает путь к сохраненному файлу или `None`, если возникла ошибка.

### get_image_bytes
1.  **Начало:** Функция принимает `image_path` (путь к изображению) и `raw` (флаг, если `True` возвращает `BytesIO` объект, иначе `bytes`).
2.  **Открытие и чтение:**
    *   Открывает изображение с помощью `PIL.Image.open`.
    *   Создается объект `BytesIO` для хранения байтов изображения.
3.  **Сохранение в `BytesIO`:**
    *   Изображение сохраняется в `BytesIO` в формате JPEG.
4.  **Возврат:** Функция возвращает `BytesIO` объект (если `raw=True`) или `bytes` (если `raw=False`).
5.  **Обработка ошибок:** Если при чтении возникает ошибка, возвращает `None`.

### get_raw_image_data
1.  **Начало:** Функция принимает `file_name` (имя файла).
2.  **Проверка существования:**
    *   Формируется путь к файлу `file_path` на основе `file_name`.
    *   Если файл не существует, возвращает `None`.
3.  **Чтение байтов:**
    *   Файл читается как байты с помощью `Path.read_bytes()`.
4.  **Возврат:** Функция возвращает байты файла или `None`, если возникла ошибка.

### random_image
1.  **Начало:** Функция принимает `root_path` (путь к директории).
2.  **Поиск изображений:**
    *   Ищет все файлы с расширениями `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` внутри `root_path` рекурсивно.
    *   **Пример:** `root_path = "images/"` - поиск картинок во всех папках в images.
3.  **Проверка на наличие:** Если не найдено ни одного изображения, возвращает `None`.
4.  **Выбор случайного:** Выбирает случайный файл из списка найденных.
5.  **Возврат:** Функция возвращает путь к выбранному файлу или `None`.

### add_text_watermark
1.  **Начало:** Функция принимает `image_path`, `watermark_text` и опциональный `output_path`.
2.  **Открытие изображения:** Открывает изображение с помощью `PIL.Image.open`.
3.  **Создание прозрачного слоя:**
    *   Создается новый прозрачный слой.
    *   Создается объект `ImageDraw` для рисования.
4.  **Настройка шрифта:**
    *   Определяется размер шрифта.
    *   Пытается загрузить шрифт `arial.ttf`, если не получается, то используется шрифт по умолчанию.
5.  **Размещение текста:**
    *   Определяются координаты для размещения текста водяного знака по центру.
6.  **Нанесение водяного знака:**
    *   Текст водяного знака наносится на прозрачный слой.
7.  **Композиция:**
    *   Изображение и прозрачный слой с водяным знаком объединяются.
8.  **Сохранение:**
    *   Сохраняется результат.
9.  **Возврат:** Возвращает путь к изображению с водяным знаком, или `None` в случае ошибки.

### add_image_watermark
1.  **Начало:** Функция принимает `input_image_path`, `watermark_image_path` и опциональный `output_image_path`.
2.  **Открытие изображений:** Открываются основное изображение и изображение водяного знака.
3.  **Изменение размера водяного знака:** Размер водяного знака устанавливается в 8% от ширины основного изображения.
4.  **Определение позиции:** Определяется позиция водяного знака (нижний правый угол с отступом).
5.  **Создание прозрачного слоя:** Создается прозрачный слой для объединения изображений.
6.  **Композиция:**
    *   Основное изображение и водяной знак наносятся на прозрачный слой.
7.  **Сохранение:**
    *   Если `output_image_path` не указан, то выходной файл сохраняется в подпапке output с тем же именем.
    *   Файл сохраняется с оптимизированным качеством.
8.  **Возврат:** Возвращает путь к изображению с водяным знаком, или `None` в случае ошибки.

### resize_image
1.  **Начало:** Функция принимает `image_path`, `size` (новый размер) и опциональный `output_path`.
2.  **Открытие изображения:** Открывает изображение с помощью `PIL.Image.open`.
3.  **Изменение размера:** Изменяется размер изображения.
4.  **Сохранение:** Сохраняется измененное изображение.
5.  **Возврат:** Возвращает путь к измененному изображению, или `None` в случае ошибки.

### convert_image
1.  **Начало:** Функция принимает `image_path`, `format` (новый формат) и опциональный `output_path`.
2.  **Открытие изображения:** Открывает изображение с помощью `PIL.Image.open`.
3.  **Преобразование формата:** Сохраняет изображение в новом формате.
4.  **Возврат:** Возвращает путь к измененному изображению, или `None` в случае ошибки.

### process_images_with_watermark
1.  **Начало:** Функция принимает `folder_path` (путь к папке с изображениями) и `watermark_path` (путь к изображению водяного знака).
2.  **Проверка наличия папки:** Проверяется, существует ли папка.
3.  **Создание выходной папки:** Создается папка output.
4.  **Обработка изображений:**
    *   Для каждого изображения в папке:
    *   Создается `output_image_path` для файла в папке `output`.
    *   Вызывается функция `add_image_watermark`.

## <mermaid>

```mermaid
flowchart TD
    Start_save_image_from_url[Start save_image_from_url]
    Download_image[Download image from URL]
    Save_image_func[Call save_image()]
    End_save_image_from_url[End save_image_from_url]
    Error_handling_save_image_from_url[Handle download error]
    
    Start_save_image[Start save_image]
    Create_dir[Create parent directories]
    Write_image_data[Write image data to file]
    Check_file[Check if file exists and not empty]
    Save_image_format[Save Image with correct format]
    End_save_image[End save_image]
    Error_handling_save_image[Handle file save error]

    Start_get_image_bytes[Start get_image_bytes]
    Open_image_PIL[Open image with PIL]
    Save_image_bytesio[Save image to BytesIO]
    Return_bytesio[Return BytesIO or bytes]
    End_get_image_bytes[End get_image_bytes]
    Error_handling_get_image_bytes[Handle image read error]

    Start_get_raw_image_data[Start get_raw_image_data]
    Check_file_exists[Check if file exists]
    Read_file_bytes[Read file bytes]
    Return_file_bytes[Return file bytes]
    End_get_raw_image_data[End get_raw_image_data]
    Error_handling_get_raw_image_data[Handle file read error]

    Start_random_image[Start random_image]
    Find_image_files[Find image files recursively]
    Check_images_found[Check if images were found]
    Select_random_image[Select random image]
    Return_random_image[Return random image path]
    End_random_image[End random_image]

    Start_add_text_watermark[Start add_text_watermark]
    Open_image_text[Open base image]
    Create_transparent_layer[Create transparent layer]
    Configure_font[Configure font]
    Position_text[Position text watermark]
    Draw_watermark[Draw watermark on transparent layer]
    Compose_image_watermark_text[Combine base and watermark images]
    Save_watermarked_text_image[Save watermarked image]
    End_add_text_watermark[End add_text_watermark]
    Error_handling_add_text_watermark[Handle text watermark error]
    
    Start_add_image_watermark[Start add_image_watermark]
    Open_images[Open base and watermark images]
    Resize_watermark[Resize watermark image]
    Position_watermark[Position watermark]
    Create_transparent_layer_image[Create transparent layer for image]
    Compose_image_watermark_image[Paste image and watermark on transparent layer]
    Save_watermarked_image[Save watermarked image]
    End_add_image_watermark[End add_image_watermark]
    Error_handling_add_image_watermark[Handle image watermark error]

    Start_resize_image[Start resize_image]
    Open_image_resize[Open image]
    Resize_image_processing[Resize image]
    Save_resized_image[Save resized image]
    End_resize_image[End resize_image]
    Error_handling_resize_image[Handle resize error]
    
    Start_convert_image[Start convert_image]
    Open_image_convert[Open image]
    Convert_image_format[Convert image format]
    Save_converted_image[Save converted image]
    End_convert_image[End convert_image]
    Error_handling_convert_image[Handle convert error]

    Start_process_images_with_watermark[Start process_images_with_watermark]
    Check_folder_exists[Check if folder exists]
    Create_output_folder[Create output folder]
    Loop_through_files[Loop through files in folder]
    Call_add_image_watermark[Call add_image_watermark for each image]
    End_process_images_with_watermark[End process_images_with_watermark]
    Error_handling_process_images_with_watermark[Handle folder or file error]
    
    Start_save_image_from_url --> Download_image
    Download_image -->|Success| Save_image_func
    Download_image -->|Failure| Error_handling_save_image_from_url
    Error_handling_save_image_from_url --> End_save_image_from_url
    Save_image_func --> End_save_image_from_url

    Start_save_image --> Create_dir
    Create_dir --> Write_image_data
    Write_image_data --> Check_file
    Check_file --> |File exist and not empty| Save_image_format
    Check_file --> |File not exist or empty| Error_handling_save_image
    Save_image_format --> End_save_image
    Error_handling_save_image --> End_save_image

    Start_get_image_bytes --> Open_image_PIL
    Open_image_PIL --> Save_image_bytesio
    Save_image_bytesio --> Return_bytesio
    Return_bytesio --> End_get_image_bytes
    Open_image_PIL --> |Error| Error_handling_get_image_bytes
    Error_handling_get_image_bytes --> End_get_image_bytes

    Start_get_raw_image_data --> Check_file_exists
    Check_file_exists --> |File exists| Read_file_bytes
    Check_file_exists --> |File does not exist| Error_handling_get_raw_image_data
    Read_file_bytes --> Return_file_bytes
    Return_file_bytes --> End_get_raw_image_data
    Error_handling_get_raw_image_data --> End_get_raw_image_data

    Start_random_image --> Find_image_files
    Find_image_files --> Check_images_found
    Check_images_found --> |Images Found| Select_random_image
    Check_images_found --> |No images| End_random_image
    Select_random_image --> Return_random_image
    Return_random_image --> End_random_image

    Start_add_text_watermark --> Open_image_text
    Open_image_text --> Create_transparent_layer
    Create_transparent_layer --> Configure_font
    Configure_font --> Position_text
    Position_text --> Draw_watermark
    Draw_watermark --> Compose_image_watermark_text
    Compose_image_watermark_text --> Save_watermarked_text_image
    Save_watermarked_text_image --> End_add_text_watermark
    Open_image_text --> |Error| Error_handling_add_text_watermark
    Error_handling_add_text_watermark --> End_add_text_watermark
    
    Start_add_image_watermark --> Open_images
    Open_images --> Resize_watermark
    Resize_watermark --> Position_watermark
    Position_watermark --> Create_transparent_layer_image
    Create_transparent_layer_image --> Compose_image_watermark_image
    Compose_image_watermark_image --> Save_watermarked_image
    Save_watermarked_image --> End_add_image_watermark
    Open_images --> |Error| Error_handling_add_image_watermark
    Error_handling_add_image_watermark --> End_add_image_watermark

    Start_resize_image --> Open_image_resize
    Open_image_resize --> Resize_image_processing
    Resize_image_processing --> Save_resized_image
    Save_resized_image --> End_resize_image
    Open_image_resize --> |Error| Error_handling_resize_image
    Error_handling_resize_image --> End_resize_image
    
    Start_convert_image --> Open_image_convert
    Open_image_convert --> Convert_image_format
    Convert_image_format --> Save_converted_image
    Save_converted_image --> End_convert_image
    Open_image_convert --> |Error| Error_handling_convert_image
    Error_handling_convert_image --> End_convert_image

    Start_process_images_with_watermark --> Check_folder_exists
    Check_folder_exists --> |Folder exists| Create_output_folder
    Check_folder_exists --> |Folder does not exist| Error_handling_process_images_with_watermark
    Create_output_folder --> Loop_through_files
    Loop_through_files --> Call_add_image_watermark
    Call_add_image_watermark --> Loop_through_files
    Loop_through_files --> End_process_images_with_watermark
    Error_handling_process_images_with_watermark --> End_process_images_with_watermark
```
## <объяснение>

### Импорты:
*   **`aiohttp`**: Асинхронная HTTP-клиентская библиотека. Используется для скачивания изображений из URL (`save_image_from_url`).
*   **`aiofiles`**: Асинхронная файловая библиотека. Используется для асинхронной записи данных изображения в файл (`save_image`).
*   **`asyncio`**: Библиотека для работы с асинхронным кодом. Используется для организации асинхронных операций.
*   **`random`**: Библиотека для генерации случайных чисел. Используется для выбора случайного файла из списка (`random_image`).
*   **`pathlib.Path`**: Библиотека для работы с файловыми путями в объектно-ориентированном стиле.
*   **`typing.Optional, typing.Union, typing.Tuple`**: Модуль для аннотации типов, что делает код более читаемым и помогает в отладке.
*   **`io.BytesIO`**: Класс для работы с байтами в памяти как с файлами. Используется для конвертации изображения в байты (`get_image_bytes`).
*   **`PIL (Pillow)`**: Библиотека для работы с изображениями. Используется для открытия, обработки и сохранения изображений.
    *   `Image`: Основной класс для работы с изображениями.
    *   `ImageDraw`: Класс для рисования на изображениях. Используется для добавления водяных знаков.
    *   `ImageFont`: Класс для работы со шрифтами. Используется для добавления текстовых водяных знаков.
*   **`src.logger.logger`**: Кастомный модуль для логирования событий.
    *   `logger`: Объект логгера, используемый для записи ошибок, предупреждений и отладочной информации.
    
*   **Взаимосвязи:**
     -  `aiohttp` и `aiofiles` используются для асинхронных операций.
     - `PIL` используется для обработки изображений (открытие, изменение размера, добавление водяных знаков).
     - `src.logger.logger` используется для логирования.
     - `pathlib.Path` используется для работы с путями к файлам и папкам, что улучшает переносимость и читаемость.

### Классы:
*   **`ImageError(Exception)`**: Пользовательское исключение для ошибок, связанных с обработкой изображений.

### Функции:
*   **`save_image_from_url(image_url: str, filename: Union[str, Path]) -> Optional[str]`**:
    *   **Аргументы:**
        *   `image_url` (str): URL изображения для скачивания.
        *   `filename` (Union[str, Path]): Имя файла, в который нужно сохранить изображение.
    *   **Возвращаемое значение:**
        *   `Optional[str]`: Путь к сохраненному файлу или `None` в случае ошибки.
    *   **Назначение:** Асинхронно скачивает изображение по URL и сохраняет его локально. Использует `aiohttp` для скачивания и `save_image` для сохранения.
*   **`save_image(image_data: bytes, file_name: Union[str, Path], format: str = 'PNG') -> Optional[str]`**:
    *   **Аргументы:**
        *   `image_data` (bytes): Байты изображения.
        *   `file_name` (Union[str, Path]): Имя файла для сохранения.
        *   `format` (str): Формат изображения (по умолчанию 'PNG').
    *   **Возвращаемое значение:**
        *   `Optional[str]`: Путь к сохраненному файлу или `None` в случае ошибки.
    *   **Назначение:** Асинхронно сохраняет данные изображения в файл. Использует `aiofiles` для записи.
*  **`get_image_bytes(image_path: Path, raw: bool = True) -> Optional[Union[BytesIO, bytes]]`**:
    *   **Аргументы:**
        *   `image_path` (Path): Путь к изображению.
        *    `raw` (bool): Если `True`, возвращает `BytesIO` объект, иначе возвращает `bytes`. По умолчанию `True`.
    *    **Возвращаемое значение:**
        *   `Optional[Union[BytesIO, bytes]]`: Байты изображения в формате JPEG или `None` в случае ошибки.
    *    **Назначение:** Открывает изображение и возвращает его байтовое представление в формате JPEG. Использует `io.BytesIO`.
*   **`get_raw_image_data(file_name: Union[str, Path]) -> Optional[bytes]`**:
    *   **Аргументы:**
        *   `file_name` (Union[str, Path]): Имя или путь файла.
    *   **Возвращаемое значение:**
        *   `Optional[bytes]`: Байты файла или `None` в случае ошибки.
    *   **Назначение:** Возвращает байты файла. Использует `pathlib.Path.read_bytes()`.
*   **`random_image(root_path: Union[str, Path]) -> Optional[str]`**:
    *   **Аргументы:**
        *   `root_path` (Union[str, Path]): Путь к директории для поиска изображений.
    *   **Возвращаемое значение:**
        *   `Optional[str]`: Случайный путь к изображению или `None`, если изображения не найдены.
    *   **Назначение:** Рекурсивно ищет случайное изображение в указанной директории.
*   **`add_text_watermark(image_path: Union[str, Path], watermark_text: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]`**:
    *   **Аргументы:**
        *   `image_path` (Union[str, Path]): Путь к изображению.
        *   `watermark_text` (str): Текст водяного знака.
        *   `output_path` (Optional[Union[str, Path]]): Путь для сохранения водяного знака, если не указан, перезаписывает исходное изображение.
    *    **Возвращаемое значение:**
        *   `Optional[str]`: Путь к изображению с водяным знаком или `None` в случае ошибки.
    *   **Назначение:** Добавляет текстовый водяной знак к изображению.
*    **`add_image_watermark(input_image_path: Path, watermark_image_path: Path, output_image_path: Optional[Path] = None) -> Optional[Path]`**:
     *   **Аргументы:**
          *   `input_image_path` (Path): Путь к исходному изображению.
          *   `watermark_image_path` (Path): Путь к изображению водяного знака.
          *   `output_image_path` (Optional[Path]): Путь к выходному изображению, если не указан, сохраняет в подпапке `output`.
     *   **Возвращаемое значение:**
          *   `Optional[Path]`: Путь к изображению с водяным знаком или `None` в случае ошибки.
     *   **Назначение:** Добавляет изображение водяного знака к изображению.
*  **`resize_image(image_path: Union[str, Path], size: Tuple[int, int], output_path: Optional[Union[str, Path]] = None) -> Optional[str]`**:
    *   **Аргументы:**
        *   `image_path` (Union[str, Path]): Путь к изображению.
        *   `size` (Tuple[int, int]): Новый размер изображения (ширина, высота).
        *   `output_path` (Optional[Union[str, Path]]): Путь для сохранения измененного изображения, если не указан, перезаписывает исходное изображение.
    *   **Возвращаемое значение:**
        *    `Optional[str]`: Путь к измененному изображению или `None` в случае ошибки.
    *   **Назначение:** Изменяет размер изображения.
*   **`convert_image(image_path: Union[str, Path], format: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]`**:
    *   **Аргументы:**
        *   `image_path` (Union[str, Path]): Путь к изображению.
        *   `format` (str): Новый формат изображения.
        *   `output_path` (Optional[Union[str, Path]]): Путь для сохранения сконвертированного изображения, если не указан, перезаписывает исходное изображение.
    *    **Возвращаемое значение:**
        *   `Optional[str]`: Путь к сконвертированному изображению или `None` в случае ошибки.
    *   **Назначение:** Конвертирует изображение в новый формат.
*   **`process_images_with_watermark(folder_path: Path, watermark_path: Path) -> None`**:
    *   **Аргументы:**
        *   `folder_path` (Path): Путь к папке с изображениями.
        *   `watermark_path` (Path): Путь к изображению водяного знака.
    *   **Возвращаемое значение:**
        *   `None`.
    *   **Назначение:** Проходит по всем изображениям в папке, добавляет водяной знак и сохраняет их в подпапке `output`.

### Переменные:
*   Переменные используются для хранения данных, путей к файлам и настройках, необходимых для работы функций. Типы переменных определены в аннотациях функций и помогают в понимании их назначения.
*   `image_extensions`: Список расширений файлов, определяющих, что файл является изображением.

### Потенциальные ошибки и области улучшения:
*   **Обработка ошибок**: В коде есть базовая обработка исключений, но ее можно расширить, чтобы обрабатывать больше типов ошибок, связанных с чтением/записью файлов, асинхронными операциями и обработкой изображений.
*   **Производительность**: При обработке большого количества изображений можно оптимизировать код, например, используя асинхронные операции для обработки нескольких изображений одновременно.
*   **Управление памятью**: При работе с большими изображениями необходимо следить за использованием памяти. Можно использовать генераторы или другие техники для эффективного использования памяти.
*    **Зависимость от шрифта**:  `add_text_watermark` зависит от наличия шрифта `arial.ttf`.  Можно добавить больше опций для выбора шрифта или его автоматической загрузки, если он не найден.
*   **Конфигурация:** Можно добавить глобальные настройки для размеров водяных знаков, отступов, и т.д.
*   **Размер водяного знака:** В функции `add_image_watermark` размер водяного знака задан как 8% от ширины, что может быть не всегда оптимально. Следует сделать размер настраиваемым параметром.
*   **Оптимизация:** В функции `add_image_watermark` можно использовать `optimize=True` при сохранении и в других функциях, которые сохраняют изображения.

### Цепочка взаимосвязей:
1.  **`save_image_from_url`** вызывает **`save_image`**.
2.  **`process_images_with_watermark`** вызывает **`add_image_watermark`**.
3.  **`add_image_watermark`** использует **`PIL`** для обработки изображений.
4.  **`save_image`** использует **`aiofiles`** для асинхронной записи в файл и `PIL` для конвертации формата.
5.  **`get_image_bytes`** использует **`PIL`** и **`io.BytesIO`** для конвертации изображения в байты.
6.  **`add_text_watermark`** использует **`PIL.ImageDraw`** и **`PIL.ImageFont`**.
7.  Все функции используют **`src.logger.logger`** для логирования.
8.  Все функции работают с **`pathlib.Path`** для работы с файлами.
9.  Функции, которые скачивают и сохраняют изображения, используют асинхронность с помощью **`asyncio`, `aiohttp`, `aiofiles`**.
10. **`random_image`** зависит от файловой системы и `pathlib`.