## \file hypotez/src/suppliers/morlevi/graber.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.morlevi 
	:platform: Windows, Unix
	:synopsis: Класс собирает значение полей на странице  товара `morlevi.co.il`. 
    Для каждого поля страницы товара сделана функция обработки поля в родительском классе.
    Если нужна нестандертная обработка, функция перегружается в этом классе.
    ------------------
    Перед отправкой запроса к вебдрайверу можно совершить предварительные действия через декоратор. 
    Декоратор по умолчанию находится в родительском классе. Для того, чтобы декоратор сработал надо передать значение 
    в `Context.locator`, Если надо реализовать свой декоратор - раскоментируйте строки с декоратором и переопределите его поведение


"""
MODE = 'dev'
from pathlib import Path
from typing import Any
import header
from src import gs
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up
from src.webdriver.driver import Driver
from src.utils.image import save_png
from src.logger.logger import logger



# # Определение декоратора для закрытия всплывающих окон
# # В каждом отдельном поставщике (`Supplier`) декоратор может использоваться в индивидуальных целях
# # Общее название декоратора `@close_pop_up` можно изменить 


# def close_pop_up(value: Any = None) -> Callable:
#     """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

#     Args:
#         value (Any): Дополнительное значение для декоратора.

#     Returns:
#         Callable: Декоратор, оборачивающий функцию.
#     """
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         async def wrapper(*args, **kwargs):
#             try:
#                 await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close   
#             except ExecuteLocatorException as ex:
#                 logger.debug(f'Ошибка выполнения локатора: ',ex)
#             return await func(*args, **kwargs)  # Await the main function
#         return wrapper
#     return decorator

class Graber(Grbr):
    """Класс для операций захвата Morlevi."""
    supplier_prefix: str

    def __init__(self, driver: Driver):
        """Инициализация класса сбора полей товара."""
        self.supplier_prefix = 'morlevi'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver)
        #Context.locator_for_decorator = self.locator.close_pop_up  # <- Вместо этого я делаю рефреш

    # # 
    # @close_pop_up()
    # async def local_saved_image(self, value: Any = None):
    #     """Fetch and save image locally.
    #     Функция получает изображение как скриншот сохраняет через файл в `tmp` и сохраняет путь к локальному файлу в поле `local_saved_image` объекта `ProductFields`
    #     Args:
    #     value (Any): это значение можно передать в словаре kwargs через ключ {local_saved_image = `value`} при определении класса.
    #     Если `value` был передан, его значение подставляется в поле `ProductFields.local_saved_image`.
    #     .. note:
    #         путь к изображению ведет в директорию  `tmp`
    #     .. todo:
    #         - Как передать значение из `**kwards` функции `grab_product_page(**kwards)`
    #         - Как передать путь кроме жестко указанного   
    #     """
       
    #     if not value:
    #         try:
    #             if not self.fields.id_product:
    #                 self.id_product() # < ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  BUG! Как передать значение из `**kwards` функции `grab_product_page(**kwards)`
    #             raw = await self.driver.execute_locator(self.locator.default_image_url) # <- получаю скриншот как `bytes` 
    #             img_tmp_path = await save_png(raw[0] if isinstance(raw, list) else raw , Path( gs.path.tmp / f'{self.fields.id_product}.png'))
    #             if img_tmp_path:
    #                 self.fields.local_saved_image = img_tmp_path
    #                 return True
    #             else:
    #                 logger.debug(f"Ошибка сохранения изображения")
    #                 ...
    #                 return
    #         except Exception as ex:
    #             logger.error(f'Ошибка сохранения изображения в поле `local_saved_image`', ex)
    #             ...
    #             return
