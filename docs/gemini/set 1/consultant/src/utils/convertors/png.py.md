# Анализ кода модуля `png.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на классы и функции, что облегчает понимание и поддержку.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует базовая документация в виде docstring.
    - Имеется обработка ошибок, хотя и не везде оптимальная.
    - Используется `logger` для логирования.
- Минусы
    - Не все функции и методы документированы в формате reStructuredText (RST).
    - Используется `print` для вывода ошибок в `webp2png`, что не соответствует стандарту логирования через `logger`.
    - Некоторые блоки `try-except` могут быть заменены на более явную проверку условий и обработку с помощью `logger.error`.
    - Отсутствует проверка типа данных при инициализации класса.
    - Отсутствует использование `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Метод `overlay_images`  может быть улучшен за счет проверки типа аргументов.
    - Имена переменных и методов частично соответствуют общему стилю, но не все.

**Рекомендации по улучшению**

1.  **Документация**: Переписать все docstring в формате reStructuredText (RST) и добавить недостающую документацию для всех функций, методов и класса.
2.  **Логирование**: Заменить `print` на `logger.error` в функции `webp2png`. Использовать `logger.error` для обработки исключений в других методах, где это применимо.
3.  **Импорты**: Добавить необходимые импорты `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Обработка ошибок**:  Убрать лишние блоки `try-except` там, где можно использовать более явные проверки условий.
5.  **Проверки**: Добавить проверку типа аргументов при инициализации класса и в методе `overlay_images`.
6.  **Имена**: Привести имена переменных и методов в соответствие с ранее обработанными файлами (например, camelCase).
7. **Общее**: Добавить комментарии в формате RST к каждой строке кода.
8. **Использовать константы**: Используйте константы для значений по умолчанию, чтобы сделать код более читаемым.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для конвертации текста в PNG изображения
=========================================================================================

Этот модуль содержит класс :class:`TextToImageGenerator`, который используется для генерации PNG изображений
из текстовых строк. Он также включает функции для наложения изображений и конвертации WEBP в PNG.

Пример использования
--------------------

Пример использования класса `TextToImageGenerator`:

.. code-block:: python

    generator = TextToImageGenerator()
    lines = ["Text 1", "Text 2", "Text 3"]
    output_dir = "./output"
    images = await generator.generate_images(lines, output_dir=output_dir)
    print(images)

"""
from pathlib import Path
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
from src.logger.logger import logger # Логирование
# from src.utils.jjson import j_loads, j_loads_ns  # TODO: Verify if needed and uncomment if needed


MODE = 'dev'

class TextToImageGenerator:
    """
    Класс для генерации PNG изображений из текстовых строк.

    :ivar default_output_dir: Путь к директории вывода по умолчанию.
    :vartype default_output_dir: Path
    :ivar default_canvas_size: Размер холста по умолчанию (ширина, высота).
    :vartype default_canvas_size: Tuple[int, int]
    :ivar default_padding: Отступ от края холста по умолчанию (процент от размера холста).
    :vartype default_padding: float
    :ivar default_background: Цвет фона по умолчанию.
    :vartype default_background: str
    :ivar default_text_color: Цвет текста по умолчанию.
    :vartype default_text_color: str
    :ivar default_log_level: Уровень логирования по умолчанию.
    :vartype default_log_level: str

    **Методы:**

    - :meth:`generate_images`: Генерирует PNG изображения из списка строк.
    - :meth:`generate_png`: Создает PNG изображение с заданным текстом, шрифтом и цветами.
    - :meth:`center_text_position`: Вычисляет позицию для центрирования текста на холсте.
    - :meth:`overlay_images`: Накладывает одно PNG изображение на другое.
    """
    DEFAULT_OUTPUT_DIR = Path("./output")
    DEFAULT_CANVAS_SIZE = (1024, 1024)
    DEFAULT_PADDING = 0.10
    DEFAULT_BACKGROUND = "white"
    DEFAULT_TEXT_COLOR = "black"
    DEFAULT_LOG_LEVEL = "WARNING"

    def __init__(self):
        """
        Инициализирует класс TextToImageGenerator со значениями по умолчанию.
        """
        # Инициализация пути к директории вывода по умолчанию
        self.default_output_dir = self.DEFAULT_OUTPUT_DIR
        # Инициализация размера холста по умолчанию
        self.default_canvas_size = self.DEFAULT_CANVAS_SIZE
        # Инициализация отступа от края холста по умолчанию
        self.default_padding = self.DEFAULT_PADDING
        # Инициализация цвета фона по умолчанию
        self.default_background = self.DEFAULT_BACKGROUND
        # Инициализация цвета текста по умолчанию
        self.default_text_color = self.DEFAULT_TEXT_COLOR
        # Инициализация уровня логирования по умолчанию
        self.default_log_level = self.DEFAULT_LOG_LEVEL

    async def generate_images( # type: ignore
        self,
        lines: List[str],
        output_dir: str | Path = None,
        font: str | ImageFont.ImageFont = "sans-serif",
        canvas_size: Tuple[int, int] = None,
        padding: float = None,
        background_color: str = None,
        text_color: str = None,
        log_level: int | str | bool = None,
        clobber: bool = False,
    ) -> List[Path]:
        """
        Генерирует PNG изображения из предоставленных текстовых строк.

        :param lines: Список строк с текстом для генерации изображений.
        :type lines: List[str]
        :param output_dir: Директория для сохранения выходных изображений. По умолчанию "./output".
        :type output_dir: str | Path, optional
        :param font: Шрифт для текста. По умолчанию "sans-serif".
        :type font: str | ImageFont.ImageFont, optional
        :param canvas_size: Размер холста в пикселях (ширина, высота). По умолчанию (1024, 1024).
        :type canvas_size: Tuple[int, int], optional
        :param padding: Процент от размера холста для использования в качестве границы. По умолчанию 0.10.
        :type padding: float, optional
        :param background_color: Цвет фона для изображений. По умолчанию "white".
        :type background_color: str, optional
        :param text_color: Цвет текста. По умолчанию "black".
        :type text_color: str, optional
        :param log_level: Уровень детализации логирования. По умолчанию "WARNING".
        :type log_level: int | str | bool, optional
        :param clobber: Если True, перезаписывает существующие файлы. По умолчанию False.
        :type clobber: bool, optional
        :raises TypeError: If parameters have incorrect type
        :return: Список путей к сгенерированным PNG изображениям.
        :rtype: List[Path]

        :Example:
        >>> generator = TextToImageGenerator()
        >>> lines = ["Text 1", "Text 2", "Text 3"]
        >>> output_dir = "./output"
        >>> images = await generator.generate_images(lines, output_dir=output_dir)
        >>> print(images)
        [PosixPath('./output/Text 1.png'), PosixPath('./output/Text 2.png'), PosixPath('./output/Text 3.png')]
        """
        # Проверка типа для output_dir
        if output_dir and not isinstance(output_dir, (str, Path)):
            logger.error(f"Неверный тип параметра output_dir: {type(output_dir)}. Ожидается str или Path")
            raise TypeError(f"Неверный тип параметра output_dir: {type(output_dir)}. Ожидается str или Path")
        # Преобразование output_dir в Path если это строка, или использование значения по умолчанию если параметр не задан
        output_directory = Path(output_dir) if output_dir else self.default_output_dir
        # Настройка логирования
        self.setup_logging(level=log_level)
        # Установка размера холста, если параметр не задан
        if not canvas_size:
            canvas_size = self.default_canvas_size
        # Установка отступа, если параметр не задан
        if not padding:
            padding = self.default_padding
        # Инициализация списка для хранения путей к сгенерированным изображениям
        generated_images = []
        # Итерация по каждой строке текста
        for line in lines:
            # Формирование имени файла изображения
            img_path = output_directory / f"{line}.png"
            # Проверка существования файла и флага clobber
            if img_path.exists() and not clobber:
                logger.warning(f"Файл {img_path} уже существует. Пропуск...")
                continue
            # Генерация изображения
            img = self.generate_png(line, canvas_size, padding, background_color, text_color, font)
            # Сохранение изображения
            img.save(img_path)
            # Добавление пути к изображению в список
            generated_images.append(img_path)
        # Возвращение списка путей к сгенерированным изображениям
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

        :param text: Текст для отрисовки на изображении.
        :type text: str
        :param canvas_size: Размер холста в пикселях (ширина, высота).
        :type canvas_size: Tuple[int, int]
        :param padding: Отступ от края холста (процент от размера холста).
        :type padding: float
        :param background_color: Цвет фона изображения.
        :type background_color: str
        :param text_color: Цвет текста.
        :type text_color: str
        :param font: Шрифт для текста.
        :type font: str | ImageFont.ImageFont
        :return: Сгенерированное PNG изображение.
        :rtype: Image
        """
        # Создание нового изображения с заданным размером и цветом фона
        img = Image.new("RGB", canvas_size, background_color)
        # Создание объекта для рисования на изображении
        draw = ImageDraw.Draw(img)
        # Загрузка шрифта с заданным размером
        font = ImageFont.truetype(font, size=self.get_font_size(canvas_size, padding))
        # Определение позиции текста для центрирования
        text_position = self.center_text_position(draw, text, font, canvas_size)
        # Отрисовка текста на изображении
        draw.text(text_position, text, fill=text_color, font=font)
        # Возвращение созданного изображения
        return img

    def center_text_position(
        self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Вычисляет позицию для центрирования текста на холсте.

        :param draw: Объект ImageDraw для рисования.
        :type draw: ImageDraw.Draw
        :param text: Текст для центрирования.
        :type text: str
        :param font: Используемый шрифт.
        :type font: ImageFont.ImageFont
        :param canvas_size: Размер холста (ширина, высота).
        :type canvas_size: Tuple[int, int]
        :return: Координаты для центрирования текста (x, y).
        :rtype: Tuple[int, int]
        """
        # Вычисление размеров текста
        text_width, text_height = draw.textsize(text, font=font)
        # Вычисление координат для центрирования текста
        return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2

    def overlay_images(
        self,
        background_path: str | Path,
        overlay_path: str | Path,
        position: tuple[int, int] = (0, 0),
        alpha: float = 1.0,
    ) -> Image:
        """
        Накладывает одно PNG изображение на другое в заданной позиции.

        :param background_path: Путь к фоновому PNG изображению.
        :type background_path: str | Path
        :param overlay_path: Путь к накладываемому PNG изображению.
        :type overlay_path: str | Path
        :param position: Координаты (x, y) для размещения накладываемого изображения. По умолчанию (0, 0).
        :type position: tuple[int, int], optional
        :param alpha: Уровень прозрачности накладываемого изображения (0.0 - 1.0). По умолчанию 1.0.
        :type alpha: float, optional
        :raises TypeError: If parameters have incorrect type
        :return: Результирующее изображение с наложением.
        :rtype: Image

        :Example:
        >>> result_image = overlay_images("background.png", "overlay.png", position=(50, 50), alpha=0.8)
        >>> result_image.save("result.png")
        """
        # Проверка типов для аргументов
        if not isinstance(background_path, (str, Path)):
             logger.error(f"Неверный тип параметра background_path: {type(background_path)}. Ожидается str или Path")
             raise TypeError(f"Неверный тип параметра background_path: {type(background_path)}. Ожидается str или Path")
        if not isinstance(overlay_path, (str, Path)):
             logger.error(f"Неверный тип параметра overlay_path: {type(overlay_path)}. Ожидается str или Path")
             raise TypeError(f"Неверный тип параметра overlay_path: {type(overlay_path)}. Ожидается str или Path")
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(coord, int) for coord in position):
             logger.error(f"Неверный тип параметра position: {type(position)}. Ожидается tuple[int, int]")
             raise TypeError(f"Неверный тип параметра position: {type(position)}. Ожидается tuple[int, int]")
        if not isinstance(alpha, float):
            logger.error(f"Неверный тип параметра alpha: {type(alpha)}. Ожидается float")
            raise TypeError(f"Неверный тип параметра alpha: {type(alpha)}. Ожидается float")

        # Открытие фонового изображения и преобразование в RGBA
        background = Image.open(background_path).convert("RGBA")
        # Открытие накладываемого изображения и преобразование в RGBA
        overlay = Image.open(overlay_path).convert("RGBA")
        # Изменение размера накладываемого изображения, если необходимо
        if overlay.size != background.size:
            overlay = overlay.resize(background.size, Image.ANTIALIAS)
        # Создание копии накладываемого изображения для изменения прозрачности
        overlay = overlay.copy()
        # Установка прозрачности накладываемого изображения
        overlay.putalpha(int(alpha * 255))
        # Наложение изображения на фон
        background.paste(overlay, position, overlay)
        # Возвращение результирующего изображения
        return background

    def get_font_size(self, canvas_size: Tuple[int, int], padding: float) -> int:
         """
         Вычисляет размер шрифта на основе размера холста и отступа.

         :param canvas_size: Размер холста (ширина, высота).
         :type canvas_size: Tuple[int, int]
         :param padding: Отступ от края холста (процент от размера холста).
         :type padding: float
         :return: Размер шрифта.
         :rtype: int
         """
         # Вычисление доступной высоты для текста с учетом отступов
         available_height = canvas_size[1] * (1 - 2 * padding)
         # Возвращение целого значения размера шрифта
         return int(available_height)

    def setup_logging(self, level: int | str | bool = None) -> None:
        """
        Настраивает логирование на основе заданного уровня.

        :param level: Уровень логирования (int, str или bool).
                     Если True, устанавливает уровень DEBUG,
                     если False - WARNING,
                     если None - использует уровень по умолчанию,
                     в противном случае пытается преобразовать значение в уровень логирования.
        :type level: int | str | bool, optional
        """
        # Установка уровня логирования в зависимости от переданного значения
        if level is True:
            logger.setLevel("DEBUG")
        elif level is False:
            logger.setLevel("WARNING")
        elif level is None:
            logger.setLevel(self.default_log_level)
        else:
            try:
                logger.setLevel(level)
            except ValueError as e:
                logger.error(f"Неверный уровень логирования: {level}, используется уровень по умолчанию. Ошибка: {e}")
                logger.setLevel(self.default_log_level)


def webp2png(webp_path: str, png_path: str) -> bool:
    """
    Конвертирует WEBP изображение в формат PNG.

    :param webp_path: Путь к входному WEBP файлу.
    :type webp_path: str
    :param png_path: Путь для сохранения сконвертированного PNG файла.
    :type png_path: str
    :return: True если конвертация прошла успешно, False в противном случае
    :rtype: bool
    :Example:
    >>> webp2png('image.webp', 'image.png')
    """
    try:
        # Открытие webp изображения
        with Image.open(webp_path) as img:
            # Сохранение изображения в формате PNG
            img.save(png_path, 'PNG')
        # Возвращение True в случае успеха
        return True
    except Exception as e:
        # Логирование ошибки с использованием logger.error
        logger.error(f"Ошибка во время конвертации: {e}")
        return False
```