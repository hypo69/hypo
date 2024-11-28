Как использовать модуль `src.logger`
========================================================================================

Описание
-------------------------
Модуль `src.logger` предоставляет гибкую систему логгирования, поддерживающую логгирование в консоль, файлы и в формате JSON. Он использует паттерн Singleton, гарантируя, что по всей программе используется только один экземпляр логгера. Логгер поддерживает различные уровни логгирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для логов в консоль. Также можно настраивать форматы вывода логов и управлять логгированием в разные файлы.

Шаги выполнения
-------------------------
1. **Импортируйте модуль:**
   ```python
   from logger import Logger
   import logging
   import colorama  # для цветного вывода в консоли
   ```

2. **Создайте экземпляр `Logger`:**
   ```python
   logger: Logger = Logger()
   ```

3. **Настройте логгеры для разных типов вывода:**
   ```python
   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
       'json_log_path': 'logs/log.json'
   }
   logger.initialize_loggers(**config)
   ```
   Этот шаг инициализирует логгирование в файлы (для info, debug, error и JSON). Пути к файлам указываются в словаре `config`.

4. **Логгируйте сообщения различных уровней:**
   ```python
   logger.info('Это информационное сообщение')
   logger.debug('Это отладочное сообщение')
   logger.warning('Это предупреждение')
   logger.error('Это ошибка')
   logger.critical('Критическая ошибка')
   ```
   Эти функции (`info`, `debug`, `warning`, `error`, `critical`) записывают сообщения в соответствующие логгеры.

5. **(Опционально) Настройте цветной вывод в консоль:**
   ```python
   logger.info('Это сообщение будет зелёным', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
   logger.error('Это сообщение будет с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
   ```
   Допустимые значения цвета в `colors` - это константы из модуля `colorama`.


Пример использования
-------------------------
.. code-block:: python

   import logging
   import colorama
   from logger import Logger
   
   colorama.init(autoreset=True)  # инициализирует цветной вывод
   
   logger: Logger = Logger()
   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
   }
   logger.initialize_loggers(**config)
   
   try:
       # Некоторый код, который может вызвать ошибку
       result = 10 / 0
   except Exception as e:
       logger.error("Произошла ошибка: ", ex=e, exc_info=True)
   
   logger.info("Программа завершена.")