### Анализ кода модуля `png`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код хорошо структурирован, есть класс для генерации изображений и отдельная функция для конвертации webp в png.
    - Используются type hints для функций и методов.
    - Есть docstrings для классов и методов, что упрощает понимание кода.
- **Минусы**:
    - Не везде используется `logger` для логирования ошибок.
    - В docstrings используется формат `Args` вместо RST.
    - Присутствуют неточности в именовании переменных и параметров.
    - Отсутствуют docstrings для модуля.
    - Используется `print` вместо `logger.error` при выводе ошибок.
    - Не все комментарии соответствуют формату RST.

**Рекомендации по улучшению**:
- Добавить RST-документацию для модуля.
- Использовать `logger.error` вместо `print` для вывода ошибок.
- Заменить аргументы `Args` на RST-формат.
- Использовать `from src.logger.logger import logger` для импорта logger.
- Всегда использовать одинарные кавычки для строк в коде.
- Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` при работе с json.
- Избегать слишком общих блоков `try-except`, обрабатывать специфические исключения.
- Придерживаться PEP8 для форматирования (например, отступы, длина строк).
- Убрать избыточные комментарии, которые дублируют имя функции.
- Использовать более точные формулировки в комментариях, например, "проверяем", "отправляем", "выполняем" вместо "получаем" или "делаем".
- Переименовать `get_font` в `get_font_size` для точности.

**Оптимизированный код**:
```python
"""
Модуль для конвертации текста в PNG изображения
=================================================

Модуль :mod:`src.utils.convertors.png` предоставляет функциональность для генерации PNG изображений
из текстовых строк, а также для конвертации изображений формата WEBP в PNG.
Он включает класс :class:`TextToImageGenerator` для настройки параметров изображения, таких как размер,
цвет, шрифт, а также функцию :func:`webp2png` для конвертации изображений.

Пример использования
----------------------
.. code-block:: python

    from pathlib import Path
    from src.utils.convertors.png import TextToImageGenerator

    async def main():
        generator = TextToImageGenerator()
        lines = ['Пример текста 1', 'Пример текста 2']
        output_dir = Path('./output')
        images = await generator.generate_images(lines=lines, output_dir=output_dir)
        print(images)

    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
"""
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

from pathlib import Path
from typing import List, Tuple

from PIL import Image, ImageDraw, ImageFont

from src.logger.logger import logger  # Logging


class TextToImageGenerator:
    """
    Класс для генерации PNG изображений из текстовых строк.

    :cvar default_output_dir: Путь к директории вывода по умолчанию.
    :vartype default_output_dir: Path
    :cvar default_canvas_size: Размер канвы по умолчанию.
    :vartype default_canvas_size: Tuple[int, int]
    :cvar default_padding: Отступ по умолчанию в процентах.
    :vartype default_padding: float
    :cvar default_background: Цвет фона по умолчанию.
    :vartype default_background: str
    :cvar default_text_color: Цвет текста по умолчанию.
    :vartype default_text_color: str
    :cvar default_log_level: Уровень логирования по умолчанию.
    :vartype default_log_level: str

    :ivar default_output_dir: Путь к директории вывода по умолчанию.
    :vartype default_output_dir: Path
    :ivar default_canvas_size: Размер канвы по умолчанию.
    :vartype default_canvas_size: Tuple[int, int]
    :ivar default_padding: Отступ по умолчанию в процентах.
    :vartype default_padding: float
    :ivar default_background: Цвет фона по умолчанию.
    :vartype default_background: str
    :ivar default_text_color: Цвет текста по умолчанию.
    :vartype default_text_color: str
    :ivar default_log_level: Уровень логирования по умолчанию.
    :vartype default_log_level: str

    **Методы:**
    * :meth:`assign_path`: Определяет путь для выходных PNG файлов.
    * :meth:`center_text_position`: Вычисляет позицию для центрирования текста на холсте.
    * :meth:`generate_png`: Создает PNG изображение с текстом.
    * :meth:`not_comment_or_blank`: Проверяет, является ли строка комментарием или пустой.
    * :meth:`which_exist`: Проверяет, какие имена файлов уже существуют в директории.
    * :meth:`get_characters`: Извлекает текстовые строки из файла или списка.
    * :meth:`parse_size`: Парсит строку в объект `Size`.
    * :meth:`get_max_text_size`: Вычисляет максимальный размер текста на основе шрифта.
    * :meth:`get_font_size`: Определяет размер шрифта на основе размера холста и отступа.
    * :meth:`setup_logging`: Настраивает логирование.
    * :meth:`error`: Логирует сообщение об ошибке и вызывает исключение.
    * :meth:`overlay_images`: Накладывает одно PNG изображение поверх другого.

    """

    def __init__(self):
        """
        Инициализирует класс TextToImageGenerator с настройками по умолчанию.
        """
        self.default_output_dir = Path('./output')
        self.default_canvas_size = (1024, 1024)
        self.default_padding = 0.10
        self.default_background = 'white'
        self.default_text_color = 'black'
        self.default_log_level = 'WARNING'

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

        :param lines: Список строк с текстом для генерации изображений.
        :type lines: List[str]
        :param output_dir: Директория для сохранения выходных изображений.
        :type output_dir: str | Path, optional
        :param font: Шрифт для текста.
        :type font: str | ImageFont.ImageFont, optional
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int], optional
        :param padding: Процент размера холста для использования в качестве границы.
        :type padding: float, optional
        :param background_color: Цвет фона изображений.
        :type background_color: str, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param log_level: Уровень детализации логирования.
        :type log_level: int | str | bool, optional
        :param clobber: Если True, перезаписывает существующие файлы.
        :type clobber: bool, optional
        :raises FileExistsError: Если файл уже существует и clobber=False.
        :return: Список путей к сгенерированным PNG изображениям.
        :rtype: List[Path]

        :Example:
            >>> generator = TextToImageGenerator()
            >>> lines = ['Текст 1', 'Текст 2', 'Текст 3']
            >>> output_dir = './output'
            >>> images = await generator.generate_images(lines=lines, output_dir=output_dir)
            >>> print(images)
            [PosixPath('./output/Текст 1.png'), PosixPath('./output/Текст 2.png'), PosixPath('./output/Текст 3.png')]
        """
        output_directory = Path(output_dir) if output_dir else self.default_output_dir
        self.setup_logging(level=log_level)

        if not canvas_size:
            canvas_size = self.default_canvas_size

        if not padding:
            padding = self.default_padding

        generated_images = []
        for line in lines:
            img_path = output_directory / f'{line}.png'
            if img_path.exists() and not clobber:
                logger.warning(f'File {img_path} already exists. Skipping...')
                continue
            img = self.generate_png(
                text=line,
                canvas_size=canvas_size,
                padding=padding,
                background_color=background_color,
                text_color=text_color,
                font=font,
            )
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

        :param text: Текст для отрисовки на изображении.
        :type text: str
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :param padding: Отступ в процентах для использования в качестве границы.
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
        img = Image.new('RGB', canvas_size, background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font, size=self.get_font_size(canvas_size, padding))

        text_position = self.center_text_position(draw, text, font, canvas_size)
        draw.text(text_position, text, fill=text_color, font=font)

        return img

    def center_text_position(
        self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Вычисляет позицию для центрирования текста на холсте.

        :param draw: Экземпляр ImageDraw.Draw.
        :type draw: ImageDraw.Draw
        :param text: Текст для отрисовки.
        :type text: str
        :param font: Шрифт, используемый для текста.
        :type font: ImageFont.ImageFont
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :return: Координаты для центрирования текста.
        :rtype: Tuple[int, int]
        """
        text_width, text_height = draw.textsize(text, font=font)
        return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2

    def overlay_images(
        self,
        background_path: str | Path,
        overlay_path: str | Path,
        position: tuple[int, int] = (0, 0),
        alpha: float = 1.0,
    ) -> Image:
        """
        Накладывает одно PNG изображение поверх другого в указанной позиции.

        :param background_path: Путь к фоновому PNG изображению.
        :type background_path: str | Path
        :param overlay_path: Путь к накладываемому PNG изображению.
        :type overlay_path: str | Path
        :param position: Координаты (x, y), где будет размещено наложение.
        :type position: tuple[int, int], optional
        :param alpha: Уровень прозрачности накладываемого изображения (0.0 - 1.0).
        :type alpha: float, optional
        :return: Результирующее изображение с наложением.
        :rtype: Image

        :Example:
            >>> result_image = overlay_images('background.png', 'overlay.png', position=(50, 50), alpha=0.8)
            >>> result_image.save('result.png')
        """
        try:
            # Открываем фоновое и накладываемое изображения
            background = Image.open(background_path).convert('RGBA')
            overlay = Image.open(overlay_path).convert('RGBA')

            # Изменяем размер накладываемого изображения, чтобы соответствовать фону, если необходимо
            if overlay.size != background.size:
                overlay = overlay.resize(background.size, Image.ANTIALIAS)

            # Настраиваем прозрачность накладываемого изображения
            overlay = overlay.copy()
            overlay.putalpha(int(alpha * 255))

            # Вставляем накладываемое изображение на фон
            background.paste(overlay, position, overlay)

            return background
        except FileNotFoundError as e:
            logger.error(f'File not found: {e}')
            raise
        except Exception as e:
            logger.error(f'Error during overlaying images: {e}')
            raise

    def get_font_size(self, canvas_size: Tuple[int, int], padding: float) -> int:
        """
        Определяет размер шрифта на основе размера холста и отступа.

        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :param padding: Отступ в процентах.
        :type padding: float
        :return: Размер шрифта.
        :rtype: int
        """
        # Вычисляем доступное пространство для текста, учитывая отступы
        available_width = canvas_size[0] * (1 - 2 * padding)
        available_height = canvas_size[1] * (1 - 2 * padding)
        # Выбираем меньшее значение, чтобы текст поместился по ширине и высоте
        return int(min(available_width, available_height) * 0.1)

    def setup_logging(self, level: int | str | bool = None):
        """
        Настраивает уровень логирования.

        :param level: Уровень логирования (int, str или bool).
        :type level: int | str | bool, optional
        """
        if level:
            logger.setLevel(level)


def webp2png(webp_path: str, png_path: str) -> bool:
    """
    Конвертирует WEBP изображение в формат PNG.

    :param webp_path: Путь к входному WEBP файлу.
    :type webp_path: str
    :param png_path: Путь для сохранения сконвертированного PNG файла.
    :type png_path: str
    :return: True в случае успешной конвертации, иначе None.
    :rtype: bool | None

    :Example:
        >>> webp2png('image.webp', 'image.png')
    """
    try:
        with Image.open(webp_path) as img:
            img.save(png_path, 'PNG')
        return True
    except FileNotFoundError as e:
        logger.error(f'File not found: {e}')
        return False
    except Exception as e:
        logger.error(f'Error during conversion: {e}')
        return False