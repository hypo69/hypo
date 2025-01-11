# Анализ кода модуля `png.py`

**Качество кода:** 8/10
   -  Плюсы
        -   Хорошая структура кода, разделение на классы и функции.
        -   Использование `Pathlib` для работы с путями.
        -   Наличие документации для функций.
        -   Логирование с использованием `logger`.
        -   Присутствует обработка исключений.
   -  Минусы
        -   Не везде используются константы.
        -   Некоторые функции имеют длинный список параметров.
        -   В функции `webp2png`  используется `print` вместо `logger.error` для вывода ошибок.
        -   В некоторых местах  не хватает подробных комментариев.
        -   Стиль кода не соответствует PEP8 (использование двойных кавычек в строках).

**Рекомендации по улучшению:**

1.  **Форматирование строк:**
    -   Заменить все двойные кавычки на одинарные для строк, кроме операций вывода.

2.  **Импорты:**
    -   Импортировать `logger` напрямую из `src.logger.logger` для соответствия стандартам.
        
3. **Константы:**
   -  Вынести значения по умолчанию для canvas_size, padding и т.д. в константы.

4.  **Обработка ошибок:**
    -   Использовать `logger.error`  вместо `print` в функции `webp2png`.
    -   Удалить излишние `try-except` блоки.
    
5.  **Документация:**
    -   Добавить RST документацию для класса `TextToImageGenerator`, методов и переменных.
    -   Добавить примеры использования в документацию.
    -  Использовать docstring для параметров функций.

6.  **Разбиение функций:**
    - Разбить функцию `generate_images` на более мелкие, для  уменьшения сложности.
    -  Рассмотреть возможность вынесения логики создания объекта `ImageFont` в отдельную функцию.

7. **`self`**:
    - Переименовать все аргументы `self` в методах классов на `cls` при использовании декоратора `@classmethod`.

**Оптимизированный код:**

```python
"""
Модуль для работы с PNG изображениями
======================================

Этот модуль предоставляет класс :class:`TextToImageGenerator` для генерации PNG изображений из текстовых строк,
а также функцию :func:`webp2png` для конвертации WEBP в PNG формат.

Класс `TextToImageGenerator` позволяет настраивать размер холста, шрифты, цвета и другие параметры.

Примеры использования
--------------------
Для использования класса `TextToImageGenerator`, создайте экземпляр класса и вызовите метод `generate_images`.
  
.. code-block:: python

    from pathlib import Path
    from src.utils.convertors.png import TextToImageGenerator

    async def main():
        generator = TextToImageGenerator()
        lines = ['Строка 1', 'Строка 2', 'Строка 3']
        output_dir = Path('./output')
        images = await generator.generate_images(lines, output_dir=output_dir)
        print(images)
    
    if __name__ == '__main__':
        import asyncio
        asyncio.run(main())
  
Для использования функции `webp2png`, вызовите ее с путями к файлам WEBP и PNG.

.. code-block:: python
    
    from src.utils.convertors.png import webp2png
    
    webp_file = 'input.webp'
    png_file = 'output.png'
    
    if webp2png(webp_file, png_file):
        print(f'Файл {webp_file} успешно сконвертирован в {png_file}')
    else:
        print(f'Ошибка при конвертации файла {webp_file}')
"""
from pathlib import Path
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
from src.logger.logger import logger  # Logging

DEFAULT_OUTPUT_DIR = Path('./output')
DEFAULT_CANVAS_SIZE = (1024, 1024)
DEFAULT_PADDING = 0.10
DEFAULT_BACKGROUND_COLOR = 'white'
DEFAULT_TEXT_COLOR = 'black'
DEFAULT_LOG_LEVEL = 'WARNING'

class TextToImageGenerator:
    """
    Класс для генерации PNG изображений из текстовых строк.

    :ivar default_output_dir: Путь к каталогу вывода по умолчанию.
    :vartype default_output_dir: Path
    :ivar default_canvas_size: Размер холста по умолчанию.
    :vartype default_canvas_size: Tuple[int, int]
    :ivar default_padding: Отступ по умолчанию.
    :vartype default_padding: float
    :ivar default_background: Цвет фона по умолчанию.
    :vartype default_background: str
    :ivar default_text_color: Цвет текста по умолчанию.
    :vartype default_text_color: str
    :ivar default_log_level: Уровень логирования по умолчанию.
    :vartype default_log_level: str
    
    **Методы:**
    
    *   `assign_path`: Определяет корректный путь для выходных PNG файлов, создавая директорию, если необходимо.
    *   `center_text_position`: Вычисляет позицию для центрирования текста на холсте.
    *   `generate_png`: Создает PNG изображение с заданным текстом, шрифтом, цветами и т.д.
    *   `not_comment_or_blank`: Проверяет, является ли строка ни комментарием, ни пустой.
    *   `which_exist`: Проверяет, какие имена файлов уже существуют в директории.
    *   `get_characters`: Извлекает текстовые строки из входного файла или списка, фильтруя комментарии и пустые строки.
    *   `parse_size`: Преобразует строку в объект `Size`.
    *   `get_max_text_size`: Вычисляет максимальный размер текста на основе шрифта и текстовых строк.
    *   `get_font`: Определяет размер шрифта на основе размера холста и отступа.
    *   `setup_logging`: Настраивает логирование на основе заданного уровня логирования.
    *   `error`: Логирует сообщение об ошибке и вызывает исключение.
    *   `overlay_images`: Накладывает одно PNG изображение поверх другого.
    """
    def __init__(self):
        """
        Инициализирует класс `TextToImageGenerator` с настройками по умолчанию.
        """
        #  Путь к каталогу вывода по умолчанию
        self.default_output_dir = DEFAULT_OUTPUT_DIR
        #  Размер холста по умолчанию
        self.default_canvas_size = DEFAULT_CANVAS_SIZE
        #  Отступ по умолчанию
        self.default_padding = DEFAULT_PADDING
        #  Цвет фона по умолчанию
        self.default_background = DEFAULT_BACKGROUND_COLOR
        #  Цвет текста по умолчанию
        self.default_text_color = DEFAULT_TEXT_COLOR
        # Уровень логирования по умолчанию
        self.default_log_level = DEFAULT_LOG_LEVEL

    async def generate_images(
        self,
        lines: List[str],
        output_dir: str | Path = None,
        font: str | ImageFont.ImageFont = 'sans-serif',
        canvas_size: Tuple[int, int] = None,
        padding: float = None,
        background_color: str = None,
        text_color: str = None,
        log_level: int | str | bool = None,
        clobber: bool = False,
    ) -> List[Path]:
        """
        Генерирует PNG изображения из предоставленных текстовых строк.
    
        :param lines: Список строк с текстом для создания изображений.
        :type lines: List[str]
        :param output_dir: Каталог для сохранения выходных изображений. По умолчанию './output'.
        :type output_dir: str | Path, optional
        :param font: Шрифт для использования в тексте. По умолчанию 'sans-serif'.
        :type font: str | ImageFont.ImageFont, optional
        :param canvas_size: Размер холста в пикселях. По умолчанию (1024, 1024).
        :type canvas_size: Tuple[int, int], optional
        :param padding: Процент от размера холста, используемый в качестве границы. По умолчанию 0.10.
        :type padding: float, optional
        :param background_color: Цвет фона для изображений. По умолчанию 'white'.
        :type background_color: str, optional
        :param text_color: Цвет текста. По умолчанию 'black'.
        :type text_color: str, optional
        :param log_level: Уровень детализации логирования. По умолчанию 'WARNING'.
        :type log_level: int | str | bool, optional
        :param clobber: Если True, перезаписывает существующие файлы. По умолчанию False.
        :type clobber: bool, optional
        :return: Список путей к сгенерированным PNG изображениям.
        :rtype: List[Path]
    
        :Example:
            >>> generator = TextToImageGenerator()
            >>> lines = ['Text 1', 'Text 2', 'Text 3']
            >>> output_dir = './output'
            >>> images = await generator.generate_images(lines, output_dir=output_dir)
            >>> print(images)
            [PosixPath('./output/Text 1.png'), PosixPath('./output/Text 2.png'), PosixPath('./output/Text 3.png')]
        """
        #  Определение выходной директории
        output_directory = Path(output_dir) if output_dir else self.default_output_dir
        #  Настройка логирования
        self.setup_logging(level=log_level)
    
        #  Определение размера холста
        if not canvas_size:
            canvas_size = self.default_canvas_size
    
        # Определение отступа
        if not padding:
            padding = self.default_padding
    
        generated_images = []
        for line in lines:
            img_path = output_directory / f'{line}.png'
            # Проверка существования файла и флага перезаписи
            if img_path.exists() and not clobber:
                logger.warning(f'File {img_path} already exists. Skipping...')
                continue
            #  Генерация PNG изображения
            img = self.generate_png(line, canvas_size, padding, background_color, text_color, font)
            img.save(img_path)
            generated_images.append(img_path)
    
        return generated_images

    def generate_png(
        self,
        text: str,
        canvas_size: Tuple[int, int],
        padding: float,
        background_color: str,
        text_color: str,
        font: str | ImageFont.ImageFont,
    ) -> Image:
        """
        Создает PNG изображение с заданным текстом, шрифтом и цветами.
    
        :param text: Текст для отображения на изображении.
        :type text: str
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :param padding: Процент от размера холста, используемый в качестве границы.
        :type padding: float
        :param background_color: Цвет фона изображения.
        :type background_color: str
        :param text_color: Цвет текста.
        :type text_color: str
        :param font: Шрифт для использования в тексте.
        :type font: str | ImageFont.ImageFont
        :return: Сгенерированное PNG изображение.
        :rtype: Image
        """
        # Создание нового изображения
        img = Image.new('RGB', canvas_size, background_color)
        draw = ImageDraw.Draw(img)
        #  Создание объекта шрифта
        font = ImageFont.truetype(font, size=self.get_font_size(canvas_size, padding))
    
        #  Определение позиции для текста
        text_position = self.center_text_position(draw, text, font, canvas_size)
        #  Отрисовка текста на изображении
        draw.text(text_position, text, fill=text_color, font=font)
    
        return img

    def center_text_position(
        self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Вычисляет позицию для центрирования текста на холсте.
    
        :param draw: Экземпляр ImageDraw.Draw.
        :type draw: ImageDraw.Draw
        :param text: Текст, который необходимо центрировать.
        :type text: str
        :param font: Шрифт, используемый для текста.
        :type font: ImageFont.ImageFont
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :return: Координаты для центрирования текста.
        :rtype: Tuple[int, int]
        """
        #  Получение размера текста
        text_width, text_height = draw.textsize(text, font=font)
        # Вычисление координат для центрирования
        return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2

    def overlay_images(
        self,
        background_path: str | Path,
        overlay_path: str | Path,
        position: tuple[int, int] = (0, 0),
        alpha: float = 1.0,
    ) -> Image:
        """
        Накладывает одно PNG изображение поверх другого в заданной позиции.
    
        :param background_path: Путь к фоновому PNG изображению.
        :type background_path: str | Path
        :param overlay_path: Путь к накладываемому PNG изображению.
        :type overlay_path: str | Path
        :param position: (x, y) координаты для размещения накладываемого изображения. По умолчанию (0, 0).
        :type position: tuple[int, int], optional
        :param alpha: Уровень прозрачности накладываемого изображения (0.0 - 1.0). По умолчанию 1.0.
        :type alpha: float, optional
        :return: Изображение с наложенным оверлеем.
        :rtype: Image
    
        :Example:
            >>> result_image = overlay_images('background.png', 'overlay.png', position=(50, 50), alpha=0.8)
            >>> result_image.save('result.png')
        """
        # Открытие фонового изображения и накладываемого
        background = Image.open(background_path).convert('RGBA')
        overlay = Image.open(overlay_path).convert('RGBA')
    
        #  Изменение размера накладываемого изображения, если нужно
        if overlay.size != background.size:
            overlay = overlay.resize(background.size, Image.ANTIALIAS)
    
        #  Регулировка прозрачности накладываемого изображения
        overlay = overlay.copy()
        overlay.putalpha(int(alpha * 255))
    
        #  Накладываем изображение на фон
        background.paste(overlay, position, overlay)
    
        return background

    def get_font_size(self, canvas_size: Tuple[int, int], padding: float) -> int:
        """
        Определяет размер шрифта на основе размера холста и отступа.
    
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :param padding: Процент от размера холста, используемый в качестве границы.
        :type padding: float
        :return: Размер шрифта.
        :rtype: int
        """
        #  Вычисление доступного пространства для текста
        available_width = canvas_size[0] * (1 - 2 * padding)
        #  Определение размера шрифта
        font_size = int(available_width / 10) # 10 - условное число
        return font_size
    
    def setup_logging(self, level: int | str | bool = None) -> None:
        """
        Настраивает логирование на основе заданного уровня логирования.
    
        :param level: Уровень детализации логирования. Может быть int, str или bool.
        :type level: int | str | bool, optional
        """
        if level:
            logger.setLevel(level)

def webp2png(webp_path: str, png_path: str) -> bool:
    """
    Конвертирует изображение в формате WEBP в формат PNG.

    :param webp_path: Путь к входному файлу WEBP.
    :type webp_path: str
    :param png_path: Путь для сохранения сконвертированного файла PNG.
    :type png_path: str
    :return: True, если конвертация прошла успешно, иначе False.
    :rtype: bool
    :Example:
       >>> webp2png('image.webp', 'image.png')
    """
    try:
        # Открытие изображения webp
        with Image.open(webp_path) as img:
            # Сохраняем в png формате
            img.save(png_path, 'PNG')
        return True
    except Exception as e:
        logger.error(f'Ошибка при конвертации: {e}')
        return False
```