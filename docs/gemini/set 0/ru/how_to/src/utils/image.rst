Как использовать модуль image.py
========================================================================================

Описание
-------------------------
Модуль `image.py` предоставляет асинхронные функции для загрузки, сохранения и получения данных изображений.  Он позволяет загружать изображения из URL, сохранять их в формате PNG и получать данные изображений из файла.  Модуль использует библиотеки `aiohttp`, `aiofiles`, `PIL` для работы с изображениями и асинхронными операциями.  Включает в себя обработку ошибок и логирование для отслеживания проблем.

Шаги выполнения
-------------------------
1. **Загрузка изображения из URL (save_png_from_url):**
    - Принимает URL изображения и имя файла для сохранения.
    - Инициализирует асинхронную сессию `aiohttp.ClientSession`.
    - Выполняет GET-запрос к URL изображения.
    - Обрабатывает возможные ошибки при запросе (например, ошибки сети).
    - Читает полученные данные изображения.
    - Вызывает функцию `save_png` для сохранения полученных данных.

2. **Сохранение изображения в формате PNG (save_png):**
    - Принимает бинарные данные изображения и имя файла для сохранения.
    - Создает директорию, если она не существует, используя `Path.parent.mkdir(parents=True, exist_ok=True)`.
    - Открывает файл для записи в двоичном режиме с помощью `aiofiles.open`.
    - Записывает бинарные данные изображения в файл.
    - Проверяет, что файл был успешно создан и имеет ненулевой размер.
    - Использует библиотеку PIL для открытия изображения и сохранения его в формате PNG, сохраняя файл.
    - Обрабатывает возможные исключения при записи и сохранении файла.

3. **Получение данных изображения из файла (get_image_data):**
    - Принимает имя файла.
    - Проверяет, что файл существует с помощью `Path.exists()`.
    - Открывает файл для чтения в двоичном режиме с помощью `open`.
    - Читает все данные из файла в переменную.
    - Обрабатывает возможные исключения при чтении файла.


Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from hypotez.src.utils.image import save_png_from_url, save_png, get_image_data

    async def main():
        # Загрузка изображения из URL
        await save_png_from_url("https://www.easygifanimator.net/images/examples/sample_image.png", "downloaded_image.png")

        # Сохранение изображения из байтовых данных
        with open("example_image.png", "rb") as f:
            image_data = f.read()
        await save_png(image_data, "saved_image.png")
        
        # Чтение данных из сохраненного изображения
        image_bytes = get_image_data("saved_image.png")
        if image_bytes:
            print(len(image_bytes))  #  Выведем длину, чтобы убедиться в успехе


    if __name__ == "__main__":
        asyncio.run(main())