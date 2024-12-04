Как использовать модуль логгирования `src.logger`
==========================================================================================

Описание
-------------------------
Модуль `src.logger` предоставляет гибкую систему логгирования, поддерживающую вывод в консоль, файлы и JSON-формат. Он использует паттерн Singleton, гарантируя, что в приложении используется только один экземпляр логгера.  Логгер поддерживает различные уровни логгирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для логов в консоль.  Вы можете настроить форматы вывода логов и управлять логгированием в разные файлы.

Шаги выполнения
-------------------------
1. **Импортируйте модуль:**
   ```python
   import src.logger as logger
   ```

2. **Создайте экземпляр логгера:**
   ```python
   logger_instance = logger.Logger()
   ```

3. **Настройте логгирование для файлов (необязательно):**
   ```python
   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
       'json_log_path': 'logs/log.json'
   }
   logger_instance.initialize_loggers(**config)
   ```
   Данный шаг инициализирует логгирование в файлы, указанные в словаре `config`.

4. **Запишите лог-сообщения с различными уровнями:**
   ```python
   logger_instance.info('Это информационное сообщение')
   logger_instance.debug('Это отладочное сообщение')
   logger_instance.error('Это сообщение об ошибке', ex=Exception('Ошибка!'))
   ```
   Эти методы запишут сообщения в соответствующие файлы/консоль.  Можно передавать исключения (`ex`) для записи подробностей ошибки.


5. **Настройте цвета вывода в консоль (необязательно):**
   ```python
   import colorama
   logger_instance.info('Это сообщение с зеленым цветом', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
   ```
   Для использования цветов в консоли необходимо предварительно импортировать `colorama`.


Пример использования
-------------------------
.. code-block:: python

   import src.logger as logger
   import colorama
   colorama.init()  # Инициализация colorama для работы с цветами

   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log'
   }

   logger_instance = logger.Logger()
   logger_instance.initialize_loggers(**config)

   try:
       result = 10 / 0
   except Exception as e:
       logger_instance.error("Произошла ошибка:", ex=e, exc_info=True, colors=(colorama.Fore.RED, colorama.Back.WHITE))

   logger_instance.info('Данные успешно обработаны', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))

   logger_instance.debug("Дополнительная информация о процессе")