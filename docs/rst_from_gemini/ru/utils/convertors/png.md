```markdown
# Модуль `hypotez/src/utils/convertors/png.py`

Этот модуль предоставляет функции для создания PNG изображений из текстовых строк.  Он использует библиотеку Pillow для работы с изображениями. Модуль предназначен для генерации изображений из текстовых данных, с возможностью настройки размеров, шрифтов, цветов и расположения текста.

## Класс `TextToImageGenerator`

Этот класс содержит методы для генерации PNG изображений.

**Атрибуты:**

* `default_output_dir`: Путь к директории по умолчанию для сохранения изображений (`./output`).
* `default_canvas_size`: Размер холста по умолчанию (ширина, высота) в пикселях.
* `default_padding`: Отступ от края холста в процентах от размера холста.
* `default_background`: Цвет фона по умолчанию.
* `default_text_color`: Цвет текста по умолчанию.
* `default_log_level`: Уровень ведения логов по умолчанию.

**Методы:**

* `__init__(self)`: Инициализирует класс с настройками по умолчанию.
* `generate_images(self, lines, output_dir=None, font=None, canvas_size=None, padding=None, background_color=None, text_color=None, log_level=None, clobber=False)`:  Генерирует список PNG изображений из списка текстовых строк.
    * `lines`: Список текстовых строк.
    * `output_dir`: Путь к директории для сохранения изображений.
    * `font`: Шрифт для текста.
    * `canvas_size`: Размеры холста в пикселях.
    * `padding`: Отступ от края холста в процентах.
    * `background_color`: Цвет фона.
    * `text_color`: Цвет текста.
    * `log_level`: Уровень ведения логов.
    * `clobber`: Перезаписывать существующие файлы.
    * Возвращает список путей к созданным изображениям.
* `generate_png(self, text, canvas_size, padding, background_color, text_color, font)`: Создает PNG изображение с заданным текстом, шрифтом и цветами.
* `center_text_position(self, draw, text, font, canvas_size)`: Рассчитывает позицию для центрирования текста на холсте.
* `overlay_images(self, background_path, overlay_path, position=(0, 0), alpha=1.0)`:  Накладывает одно PNG изображение поверх другого.
* `get_font_size(self, canvas_size, padding)`:  Рассчитывает размер шрифта, учитывая размер холста и отступ.  (Добавлен для улучшения структуры кода.)


## Функция `webp2png(webp_path, png_path)`

Преобразует изображение в формате WEBP в PNG.

**Аргументы:**

* `webp_path`: Путь к файлу WEBP.
* `png_path`: Путь для сохранения файла PNG.

**Возвращает:**

* `bool`: `True`, если преобразование успешно, `False` в случае ошибки.

## Логирование

Модуль использует класс `logger` из модуля `src.logger` для ведения логов. Уровень логов можно настроить.

## Пример использования

```python
from hypotez.src.utils.convertors.png import TextToImageGenerator

generator = TextToImageGenerator()
lines = ["Первая строка", "Вторая строка", "Третья строка"]
images = generator.generate_images(lines, output_dir="./output", font="Arial.ttf", canvas_size=(800, 600), padding=0.1, background_color="lightblue", text_color="darkred", log_level="INFO")
for img_path in images:
    print(f"Изображение сохранено: {img_path}")
```

Этот пример создаст три PNG изображения с указанными параметрами и выведет пути к сохранённым изображениям.


**Рекомендации:**

* Добавить обработку исключений в методах, особенно при работе с файлами.
* Уточнить типы аргументов в документации.
* Добавить пример использования функции `overlay_images`.
* Рассмотреть возможность использования более эффективных алгоритмов для вычисления размера шрифта, если это критично для производительности.
