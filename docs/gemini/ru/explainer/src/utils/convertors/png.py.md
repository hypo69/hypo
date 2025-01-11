## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid\
    flowchart TD\
        Start --> Header[<code>header.py</code><br> Determine Project Root]\
        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```
3.  **<объяснение>**: Предоставьте подробные объяснения:
    *   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    *   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    *   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    *   **Переменные**: Их типы и использование.
    *   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**`TextToImageGenerator.generate_images`:**
1. **Инициализация**: Создается экземпляр `TextToImageGenerator` с настройками по умолчанию (путь вывода, размер холста, отступы и т.д.).
    ```python
    generator = TextToImageGenerator()
    ```
2. **Настройка параметров**: В функцию `generate_images` передаются текст `lines`, путь вывода `output_dir`, шрифт `font`, размер холста `canvas_size`, отступ `padding`, цвета `background_color`, `text_color`, уровень логирования `log_level`, и флаг перезаписи `clobber`.
    ```python
    lines = ["Line 1", "Line 2"]
    output_dir = "./output_images"
    images = await generator.generate_images(lines, output_dir=output_dir, clobber=True)
    ```
3. **Обработка параметров**: Если путь вывода не указан, используется путь по умолчанию. Настраивается уровень логирования. Если размеры холста и отступы не указаны, используются значения по умолчанию.
4. **Цикл обработки строк**: Для каждой строки текста из `lines`:
    *   Формируется путь к файлу изображения: `f"{line}.png"`.
    *   Проверяется наличие файла:
        *   Если файл существует и `clobber` равен `False`, выводится предупреждение и итерация пропускается.
        *   Иначе, вызывается `generate_png`.
    *   Сохранение изображения.
    *   Путь к созданному файлу добавляется в список `generated_images`.
5.  **Возвращение результатов**: Функция возвращает список путей к созданным PNG файлам.

**`TextToImageGenerator.generate_png`:**

1. **Создание изображения**: Создается новое RGB изображение с заданным размером `canvas_size` и цветом фона `background_color`.
    ```python
    img = Image.new("RGB", canvas_size, background_color)
    ```
2. **Создание объекта для рисования**: Создается объект `ImageDraw.Draw` для рисования на изображении.
    ```python
    draw = ImageDraw.Draw(img)
    ```
3. **Определение размера шрифта**: Вызывается метод `get_font_size`, который возвращает размер шрифта.
    ```python
    font_size = self.get_font_size(canvas_size, padding)
    ```
4.  **Создание объекта шрифта**: Создается объект `ImageFont.truetype` на основе шрифта `font` и размера `font_size`.
    ```python
    font = ImageFont.truetype(font, size=font_size)
    ```
5.  **Определение позиции текста**: Вызывается метод `center_text_position` для определения координат центрирования текста.
    ```python
    text_position = self.center_text_position(draw, text, font, canvas_size)
    ```
6. **Отрисовка текста**: На изображение наносится текст `text` цветом `text_color` в позиции `text_position` с использованием шрифта `font`.
    ```python
    draw.text(text_position, text, fill=text_color, font=font)
    ```
7. **Возврат изображения**: Функция возвращает созданное изображение.

**`TextToImageGenerator.center_text_position`:**

1. **Определение размера текста**: Используя `draw.textsize`, рассчитываются ширина и высота текста `text` с учетом шрифта `font`.
    ```python
    text_width, text_height = draw.textsize(text, font=font)
    ```
2. **Расчет позиции**: Рассчитывается позиция для центрирования текста по горизонтали и вертикали:
    *   Горизонталь: `(canvas_size[0] - text_width) // 2`
    *   Вертикаль: `(canvas_size[1] - text_height) // 2`
3. **Возврат позиции**: Функция возвращает кортеж координат (x, y).

**`TextToImageGenerator.overlay_images`:**

1. **Открытие изображений**: Открываются фоновое и накладываемое изображения, конвертируются в формат RGBA.
   ```python
   background = Image.open(background_path).convert("RGBA")
   overlay = Image.open(overlay_path).convert("RGBA")
   ```
2. **Изменение размера накладываемого изображения**: Если размеры накладываемого и фонового изображений не совпадают, размер накладываемого изменяется до размеров фонового с применением сглаживания.
   ```python
   if overlay.size != background.size:
       overlay = overlay.resize(background.size, Image.ANTIALIAS)
   ```
3.  **Установка прозрачности**:  Создается копия накладываемого изображения,  и устанавливается его прозрачность в соответствии со значением alpha.
   ```python
   overlay = overlay.copy()
   overlay.putalpha(int(alpha * 255))
   ```
4.  **Накладывание изображений**: Накладываемое изображение вставляется в фоновое изображение в заданных координатах position.
    ```python
    background.paste(overlay, position, overlay)
    ```
5. **Возврат результирующего изображения**: Функция возвращает изображение с наложенным слоем.

**`webp2png`:**
1. **Открытие WEBP изображения**: Открывается WEBP изображение, используя `Image.open`.
   ```python
   with Image.open(webp_path) as img:
   ```
2.  **Сохранение в PNG**: Открытое изображение сохраняется в формате PNG по указанному пути.
   ```python
   img.save(png_path, 'PNG')
   ```
3. **Обработка исключений**: Если во время преобразования происходит ошибка, она выводится в консоль и возвращается `None`, иначе функция возвращает `True`.
   ```python
   except Exception as e:
        print(f"Error during conversion: {e}")
        return
   return True
   ```

## <mermaid>

```mermaid
flowchart TD
    subgraph TextToImageGenerator
        Start(Начало) --> Init[__init__: Инициализация]
        Init --> generate_images[generate_images: Генерация изображений]

        subgraph generate_images
            generate_images --> SetupLog[setup_logging: Настройка логирования]
            SetupLog --> CheckCanvasSize[Проверка canvas_size:  Использование default, если не указан]
            CheckCanvasSize --> CheckPadding[Проверка padding: Использование default, если не указан]
            CheckPadding --> LoopLines[Цикл по строкам (lines)]
            LoopLines --> CheckFileExists{Проверка существует ли файл?}
            CheckFileExists -- Да, clobber=false --> SkipFile[Пропуск файла]
            CheckFileExists -- Нет или clobber=true --> GeneratePNG[generate_png: Генерация PNG]
            GeneratePNG --> SaveImage[Сохранение изображения]
            SaveImage --> AddPathToList[Добавление пути к списку]
            AddPathToList --> LoopLines
            LoopLines -- Завершение цикла --> ReturnPaths[Возврат списка путей]
        end
        
        generate_images --> ReturnPaths
        ReturnPaths --> End(Конец)

        subgraph generate_png
            generate_png --> CreateImage[Создание нового изображения]
            CreateImage --> CreateDraw[Создание объекта ImageDraw]
             CreateDraw --> GetFontSize[get_font_size: Определение размера шрифта]
            GetFontSize --> CreateFont[Создание объекта шрифта]
            CreateFont --> CenterTextPos[center_text_position: Определение позиции текста]
            CenterTextPos --> DrawText[Отрисовка текста]
            DrawText --> ReturnImage[Возврат изображения]
         end
        generate_png --> ReturnImage

         subgraph center_text_position
            center_text_position --> GetTextSize[draw.textsize: Получение размера текста]
             GetTextSize --> CalcPosition[Расчет позиции центрирования]
            CalcPosition --> ReturnPosition[Возврат координат]
         end
         center_text_position --> ReturnPosition

         subgraph overlay_images
             overlay_images --> OpenBackground[Открытие фонового изображения]
             OpenBackground --> OpenOverlay[Открытие накладываемого изображения]
             OpenOverlay --> ResizeOverlay{Проверка размеров изображений}
             ResizeOverlay -- Не совпадают --> Resize[Изменение размера накладываемого изображения]
             ResizeOverlay -- Совпадают --> AdjustTransparency[Настройка прозрачности]
             Resize --> AdjustTransparency
             AdjustTransparency --> PasteOverlay[Накладывание изображения]
             PasteOverlay --> ReturnOverlayedImage[Возврат результирующего изображения]
         end
         overlay_images --> ReturnOverlayedImage
    end

    subgraph webp2png
         webp2pngStart(Начало) --> OpenWebpImage[Открытие WEBP изображения]
         OpenWebpImage --> SavePngImage[Сохранение PNG изображения]
         SavePngImage --> ReturnTrue[Возврат True]
          ReturnTrue --> webp2pngEnd(Конец)
         OpenWebpImage --> ErrorCatch[Блок try ... except]
         ErrorCatch --> ErrorLog[Логирование ошибки]
          ErrorLog --> ReturnNone[Возврат None]
        ReturnNone --> webp2pngEnd
    end
    
```

**Описание зависимостей `mermaid`:**

*   `TextToImageGenerator` - основной класс, содержащий методы для генерации изображений.
    *   `__init__`: Инициализирует значения по умолчанию для пути вывода, размера холста, отступов, и т.д.
    *   `generate_images`: Метод, обрабатывающий список строк и генерирующий PNG файлы.
    *   `generate_png`: Метод, создающий PNG изображение с заданным текстом.
    *    `center_text_position`: Метод, вычисляющий позицию для центрирования текста.
    *   `overlay_images`: Метод, накладывающий одно изображение на другое.
*   `generate_images` вызывает `setup_logging`, `generate_png` внутри цикла.
*   `generate_png` вызывает `get_font_size` и `center_text_position`.
*   `center_text_position` использует `draw.textsize` для определения размера текста.
*   `overlay_images` использует  `Image.open` для открытия изображений и `paste` для их наложения.
*   `webp2png` конвертирует webp в png формат.

## <объяснение>

**Импорты:**

*   `from pathlib import Path`: Используется для работы с путями к файлам и директориям, упрощает создание и манипулирование путями, что делает код более читаемым и кроссплатформенным.
*   `from typing import List, Tuple`: Используется для аннотации типов, делает код более читаемым и помогает избежать ошибок.
    *   `List` - используется для аннотации списков.
    *   `Tuple` - используется для аннотации кортежей.
*   `from PIL import Image, ImageDraw, ImageFont`: Импортирует необходимые модули из библиотеки Pillow (PIL) для работы с изображениями, рисованием и шрифтами.
    *   `Image`: Предоставляет функции для работы с изображениями (создание, открытие, сохранение).
    *   `ImageDraw`: Предоставляет функции для рисования на изображениях (текст, фигуры).
    *   `ImageFont`: Предоставляет функции для работы со шрифтами.
*  `from src.logger.logger import logger`: импортирует объект `logger` из модуля `src.logger.logger`, что позволяет использовать логирование в данном модуле, обеспечивая более эффективное управление ошибками и отслеживание работы программы.

**Классы:**

*   `TextToImageGenerator`:
    *   **Роль:** Класс предназначен для генерации PNG изображений на основе текстовых строк. Он инкапсулирует логику создания изображений, центрирования текста, настройки шрифта и т.д.
    *   **Атрибуты:**
        *   `default_output_dir`: `Path`, путь к директории вывода по умолчанию.
        *   `default_canvas_size`: `Tuple[int, int]`, размер холста по умолчанию.
        *   `default_padding`: `float`, отступ от края холста по умолчанию.
        *   `default_background`: `str`, цвет фона по умолчанию.
        *   `default_text_color`: `str`, цвет текста по умолчанию.
        *   `default_log_level`: `str`, уровень логирования по умолчанию.
    *   **Методы:**
        *   `__init__(self)`: Конструктор класса, инициализирует значения по умолчанию.
        *   `async generate_images(self, lines, output_dir=None, font="sans-serif", canvas_size=None, padding=None, background_color=None, text_color=None, log_level=None, clobber=False) -> List[Path]`: Основной метод, генерирующий PNG изображения из списка строк. Принимает различные параметры для настройки.
        *    `generate_png(self, text: str, canvas_size: Tuple[int, int], padding: float, background_color: str, text_color: str, font: str | ImageFont.ImageFont) -> Image`: Создает PNG изображение для одной текстовой строки.
        *   `center_text_position(self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]) -> Tuple[int, int]`: Вычисляет координаты для центрирования текста на изображении.
         *  `overlay_images(self, background_path: str | Path, overlay_path: str | Path, position: tuple[int, int] = (0, 0), alpha: float = 1.0) -> Image`:  Накладывает одно изображение на другое, создавая эффект композиции.

**Функции:**

*   `webp2png(webp_path: str, png_path: str) -> bool`:
    *   **Аргументы:**
        *   `webp_path`: `str`, путь к исходному WEBP файлу.
        *   `png_path`: `str`, путь для сохранения PNG файла.
    *   **Возвращаемое значение:**
        *   `True`, если конвертация прошла успешно, `None` в случае ошибки.
    *   **Назначение:** Конвертирует WEBP изображение в PNG формат.

**Переменные:**

*   Переменные, объявленные внутри методов, используются для хранения промежуточных результатов, например, пути к файлам, размеры изображений, цвета, параметры шрифтов.

**Потенциальные ошибки и области для улучшения:**

*   **Отсутствие обработки шрифтов**: Код использует "sans-serif" в качестве шрифта по умолчанию, но не проверяет его наличие в системе. Если шрифт не найден,  может возникнуть ошибка.
*   **Недостаточная обработка исключений**: В методе `generate_png` не предусмотрена обработка ошибок, возникающих при создании шрифта или отрисовке текста.
*   **Невозможность выбора размера шрифта**: Размер шрифта рассчитывается автоматически на основе размера холста и отступа, нет возможности задать его явно.
*   **Ограниченная настройка `overlay_images`**: Не предусмотрено масштабирование или обрезка накладываемого изображения.
*  **Неэффективная обработка больших файлов**: Функция `webp2png` загружает изображение целиком в память, что может привести к проблемам при обработке очень больших файлов. Возможно, стоит использовать потоковую обработку.
*   **Логика определения имени файла**:  Файл именуется на основе текста, это может привести к проблемам, если текст содержит недопустимые символы или слишком длинный.

**Взаимосвязь с другими частями проекта:**

*   `src.logger.logger`: Используется для логирования событий.
*   Файл является частью пакета `src.utils.convertors`.

Этот анализ предоставляет детальное понимание кода, его структуры и функциональности, а также выделяет области, которые могут быть улучшены.