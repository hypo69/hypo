## Анализ кода: `hypotez/src/utils/convertors/png.py`

### 1. Алгоритм

#### TextToImageGenerator
1.  **Инициализация**:
    *   Инициализируется класс `TextToImageGenerator` со значениями по умолчанию для каталога вывода, размера холста, отступов, цветов фона и текста, а также уровня ведения журнала.

2.  **Генерация изображений (`generate_images`)**:
    *   Определяет выходной каталог на основе предоставленного пути или значения по умолчанию.
    *   Настраивает ведение журнала на основе указанного уровня.
    *   Перебирает каждую строку текста.

    *   Для каждой строки:
        *   Формирует путь для выходного PNG-изображения.
        *   Проверяет, существует ли файл и следует ли его перезаписывать.
        *   Вызывает `generate_png` для создания изображения.
        *   Сохраняет изображение в указанный путь.
        *   Добавляет путь к изображению в список сгенерированных изображений.

    *   Возвращает список путей к сгенерированным изображениям.

#### Создание PNG (`generate_png`)
1.  **Создание изображения**:
    *   Создает новое RGB-изображение с заданным размером холста и цветом фона.
    *   Создает объект `ImageDraw` для рисования на изображении.
    *   Определяет размер шрифта на основе размера холста и отступа.
    *   Вычисляет позицию для центрирования текста на холсте.
    *   Рисует текст на изображении с использованием указанного шрифта и цвета текста.
    *   Возвращает созданное изображение.

#### Центрирование позиции текста (`center_text_position`)
1.  **Расчет позиции**:
    *   Получает ширину и высоту текста с использованием указанного шрифта.
    *   Вычисляет координаты для центрирования текста на холсте.
    *   Возвращает координаты.

#### Наложение изображений (`overlay_images`)
1.  **Открытие изображений**:
    *   Открывает фоновое и накладываемое изображения.
    *   Преобразует оба изображения в формат RGBA.

2.  **Изменение размера и прозрачности**:
    *   Если размер накладываемого изображения отличается от размера фона, изменяет размер накладываемого изображения в соответствии с размером фона.
    *   Регулирует прозрачность накладываемого изображения на основе предоставленного альфа-значения.

3.  **Накладывание**:
    *   Вставляет накладываемое изображение на фон в указанной позиции.

4.  **Возврат**:
    *   Возвращает результирующее изображение.

#### WEBP в PNG (`webp2png`)
1.  **Конвертация**:
    *   Пытается открыть WEBP-изображение.
    *   Сохраняет изображение как PNG.
    *   Возвращает True при успехе.

2.  **Обработка ошибок**:
    *   Перехватывает любые исключения, которые возникают во время конвертации.
    *   Выводит сообщение об ошибке.
    *   Возвращает None при сбое.

```mermaid
graph TD
    A[TextToImageGenerator] --> B(generate_images)
    B --> C{if not canvas_size}
    C -- True --> D[canvas_size = self.default_canvas_size]
    C -- False --> E[Использовать предоставленный canvas_size]
    B --> F{if not padding}
    F -- True --> G[padding = self.default_padding]
    F -- False --> H[Использовать предоставленный padding]
    B --> I[for line in lines]
    I --> J[img_path = output_directory / f"{line}.png"]
    I --> K{if img_path.exists() and not clobber}
    K -- True --> L[logger.warning(f"File {img_path} already exists. Skipping...")]
    K -- False --> M[img = self.generate_png(...)]
    M --> N[img.save(img_path)]
    N --> O[generated_images.append(img_path)]
    A --> P(generate_png)
    P --> Q[img = Image.new("RGB", canvas_size, background_color)]
    P --> R[draw = ImageDraw.Draw(img)]
    P --> S[font = ImageFont.truetype(font, size=self.get_font_size(canvas_size, padding))]
    P --> T[text_position = self.center_text_position(draw, text, font, canvas_size)]
    P --> U[draw.text(text_position, text, fill=text_color, font=font)]
    A --> V(center_text_position)
    V --> W[text_width, text_height = draw.textsize(text, font=font)]
    V --> X[return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2]
    A --> Y(overlay_images)
    Y --> Z[background = Image.open(background_path).convert("RGBA")]
    Y --> AA[overlay = Image.open(overlay_path).convert("RGBA")]
    Y --> BB{if overlay.size != background.size}
    BB -- True --> CC[overlay = overlay.resize(background.size, Image.ANTIALIAS)]
    BB -- False --> DD[Продолжить]
    Y --> EE[overlay = overlay.copy()]
    Y --> FF[overlay.putalpha(int(alpha * 255))]
    Y --> GG[background.paste(overlay, position, overlay)]
    subgraph "Функции класса TextToImageGenerator"
        B
        P
        V
        Y
    end
    style A fill:#f9f,stroke:#333,stroke-width:2px
```

### 2. Mermaid

```mermaid
graph TD
    A[TextToImageGenerator] --> B(generate_images)
    B --> C{if not canvas_size}
    C -- True --> D[canvas_size = self.default_canvas_size]
    C -- False --> E[Использовать предоставленный canvas_size]
    B --> F{if not padding}
    F -- True --> G[padding = self.default_padding]
    F -- False --> H[Использовать предоставленный padding]
    B --> I[for line in lines]
    I --> J[img_path = output_directory / f"{line}.png"]
    I --> K{if img_path.exists() and not clobber}
    K -- True --> L[logger.warning(f"File {img_path} already exists. Skipping...")]
    K -- False --> M[img = self.generate_png(...)]
    M --> N[img.save(img_path)]
    N --> O[generated_images.append(img_path)]
    A --> P(generate_png)
    P --> Q[img = Image.new("RGB", canvas_size, background_color)]
    P --> R[draw = ImageDraw.Draw(img)]
    P --> S[font = ImageFont.truetype(font, size=self.get_font_size(canvas_size, padding))]
    P --> T[text_position = self.center_text_position(draw, text, font, canvas_size)]
    P --> U[draw.text(text_position, text, fill=text_color, font=font)]
    A --> V(center_text_position)
    V --> W[text_width, text_height = draw.textsize(text, font=font)]
    V --> X[return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2]
    A --> Y(overlay_images)
    Y --> Z[background = Image.open(background_path).convert("RGBA")]
    Y --> AA[overlay = Image.open(overlay_path).convert("RGBA")]
    Y --> BB{if overlay.size != background.size}
    BB -- True --> CC[overlay = overlay.resize(background.size, Image.ANTIALIAS)]
    BB -- False --> DD[Продолжить]
    Y --> EE[overlay = overlay.copy()]
    Y --> FF[overlay.putalpha(int(alpha * 255))]
    Y --> GG[background.paste(overlay, position, overlay)]
    subgraph "Функции класса TextToImageGenerator"
        B
        P
        V
        Y
    end
    style A fill:#f9f,stroke:#333,stroke-width:2px
```

**Зависимости и пояснения:**

*   `TextToImageGenerator`: Основной класс, который координирует генерацию изображений на основе заданных параметров и текста.
*   `generate_images`: Метод, который принимает список строк, определяет параметры выходного каталога, шрифта, размера холста, отступов, цветов и уровня ведения журнала. Он вызывает метод `generate_png` для каждой строки текста, чтобы создать изображение, и сохраняет его в указанном каталоге.
*   `generate_png`: Метод, который создает фактическое PNG-изображение с заданным текстом, шрифтом и цветами. Он использует библиотеку `PIL` для создания нового изображения, рисования текста и сохранения результата.
*   `center_text_position`: Метод, который вычисляет координаты для центрирования текста на холсте. Он использует методы `PIL` для определения размера текста и вычисления позиции для центрирования.
*   `overlay_images`: Метод, который накладывает одно PNG-изображение на другое в указанной позиции. Он открывает оба изображения, изменяет размер и прозрачность накладываемого изображения, а затем вставляет его на фон.

### 3. Объяснение

#### Импорты:

*   `pathlib.Path`: Используется для работы с путями файлов и каталогов.
*   `typing.List`, `typing.Tuple`: Используются для аннотаций типов, указывающих типы списков и кортежей.
*   `PIL.Image`, `PIL.ImageDraw`, `PIL.ImageFont`: Модули из библиотеки Pillow (PIL), используемые для работы с изображениями, рисования на изображениях и работы со шрифтами.
*   `src.logger.logger`: Модуль для логирования, используемый для записи информации о работе программы.

#### Классы:

*   `TextToImageGenerator`:
    *   **Роль**: Генерирует PNG-изображения из текстовых строк.
    *   **Атрибуты**:
        *   `default_output_dir`: Путь к каталогу вывода по умолчанию.
        *   `default_canvas_size`: Размер холста по умолчанию (ширина, высота).
        *   `default_padding`: Отступ по умолчанию (процент от размера холста).
        *   `default_background`: Цвет фона по умолчанию.
        *   `default_text_color`: Цвет текста по умолчанию.
        *   `default_log_level`: Уровень логирования по умолчанию.
    *   **Методы**:
        *   `__init__`: Инициализирует объект класса с значениями по умолчанию.
        *   `generate_images`: Генерирует изображения из списка строк.
        *   `generate_png`: Создает одно PNG-изображение с заданным текстом.
        *   `center_text_position`: Вычисляет позицию для центрирования текста на изображении.
        *   `overlay_images`: Накладывает одно PNG-изображение на другое.

#### Функции:

*   `webp2png(webp_path: str, png_path: str) -> bool`:
    *   **Аргументы**:
        *   `webp_path` (str): Путь к файлу WEBP.
        *   `png_path` (str): Путь для сохранения PNG-файла.
    *   **Возвращаемое значение**:
        *   `bool`: True, если конвертация прошла успешно, иначе None.
    *   **Назначение**: Конвертирует изображение из формата WEBP в формат PNG.
    *   **Пример**:
        ```python
        webp2png('image.webp', 'image.png')
        ```

#### Переменные:

*   `lines` (List[str]): Список строк текста для генерации изображений.
*   `output_dir` (str | Path): Путь к каталогу для сохранения изображений.
*   `font` (str | ImageFont.ImageFont): Шрифт, используемый для текста.
*   `canvas_size` (Tuple[int, int]): Размер холста (ширина, высота).
*   `padding` (float): Отступ (процент от размера холста).
*   `background_color` (str): Цвет фона изображения.
*   `text_color` (str): Цвет текста на изображении.
*   `log_level` (int | str | bool): Уровень логирования.
*   `clobber` (bool): Флаг, указывающий, следует ли перезаписывать существующие файлы.

#### Потенциальные ошибки и области для улучшения:

*   Отсутствует обработка ошибок при создании каталога вывода.
*   Размер шрифта определяется внутри метода `generate_png`, что может привести к проблемам с масштабированием.
*   Не реализована поддержка разных шрифтов (только "sans-serif").

#### Взаимосвязи с другими частями проекта:

*   Использует модуль `src.logger.logger` для логирования, что позволяет интегрировать данный модуль в общую систему логирования проекта.

```mermaid
flowchart TD
    Start --> Header[<code>src.logger.logger</code><br> Logging module]
    Header --> setup_logging[<code>setup_logging</code><br> Configure logging]
    setup_logging --> logger.error[<code>logger.error</code><br> Log error messages]
    setup_logging --> logger.warning[<code>logger.warning</code><br> Log warning messages]
    style Start fill:#f9f,stroke:#333,stroke-width:2px