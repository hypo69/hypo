Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `Graber` для извлечения данных с сайта morlevi.co.il.  Класс наследуется от базового класса `Grbr` и предоставляет методы для извлечения различных полей товара, таких как название, описание, цена и т.д.  Важной особенностью является асинхронная обработка и возможность предварительного выполнения действий (например, закрытия всплывающих окон) перед извлечением данных.  Код использует декоратор `close_pop_up` для реализации такого предварительного действия.  Также в коде есть функция `local_saved_image`, которая загружает и сохраняет изображение товара в временную директорию.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует нужные модули, такие как `asyncio`, `Path`, `dataclass`, `pydantic`, `Driver`, и др., необходимые для работы с веб-драйвером, обработкой данных и логгированием.
2. **Определение класса `Graber`:** Класс `Graber` наследуется от базового класса `Grbr` и содержит методы для работы с веб-драйвером.
3. **Инициализация класса:** В методе `__init__` класса `Graber` происходит инициализация, устанавливается префикс для поставщика, и задается локатор для декоратора.
4. **Извлечение данных (`grab_page`):**  Функция `grab_page`  асинхронно извлекает данные, вызывая другие вспомогательные функции для каждого поля товара (например, `self.name`, `self.description`).
5. **Обработка полей (`fetch_all_data`):**  Внутри `fetch_all_data` вызываются функции для извлечения значений конкретных полей товара, используя переданные в качестве аргументов значения (если таковые есть).  Обратите внимание на использование `kwards.get()` для безопасного доступа к значениям.
6. **Сохранение изображения (`local_saved_image`):** Функция `local_saved_image` использует веб-драйвер для получения изображения товара, сохраняет его в временную директорию и сохраняет путь к сохраненному изображению в поле `local_saved_image` объекта `ProductFields`. Важно отметить, что эта функция использует декоратор `@close_pop_up` для закрытия всплывающих окон.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver import Driver
    from hypotez.src.suppliers.morlevi.graber import Graber
    from src import gs

    async def main():
        driver = Driver()  # Инициализация драйвера
        graber = Graber(driver)  # Создание экземпляра класса Graber
        
        # Пример получения данных товара с ID 123. Передадим id_product в kwargs
        product_data = await graber.grab_page(driver, id_product='123', local_saved_image = 'some_image_name')
        
        # Обработка полученных данных
        print(product_data.name)
        print(product_data.local_saved_image)  # Вывод пути к сохранённому изображению
        
        await driver.quit() # Закрытие драйвера

    if __name__ == "__main__":
        asyncio.run(main())