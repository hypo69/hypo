Как использовать модуль logger
========================================================================================

Описание
-------------------------
Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую консоль, файлы и JSON-логирование. Он использует паттерн Singleton для обеспечения того, что в приложении используется только один экземпляр логгера. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Также можно настраивать форматы вывода логов и управлять логированием в разные файлы.

Шаги выполнения
-------------------------
1. **Импортируйте модуль:**
   ```python
   from hypotez.src.logger import Logger
   import logging
   import colorama  # Необходимо для цветного вывода
   ```

2. **Создайте конфигурационный словарь:**
   ```python
   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
       'json_log_path': 'logs/log.json'
   }
   ```
   Замените пути (`'info_log_path'`, `'debug_log_path'`, `'errors_log_path'`, `'json_log_path'`) на нужные вам.

3. **Инициализируйте логгер:**
   ```python
   logger: Logger = Logger()
   logger.initialize_loggers(**config)
   ```
   Это создает и настраивает логгер, используя пути из `config`.

4. **Логируйте сообщения:**
   ```python
   logger.info('Это информационное сообщение')
   logger.warning('Это предупреждающее сообщение')
   logger.error('Это ошибка', ex=Exception('some error')) # Логирование исключения
   logger.debug('Это отладочное сообщение')
   ```
   Используйте методы `info`, `warning`, `error`, `debug`, `success` и т.д. для записи сообщений различных уровней. Аргумент `ex` позволяет логгировать исключения.

5. **Настройте цвета для консольного вывода (необязательно):**
   ```python
   logger.info('Это информационное сообщение с цветом', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
   ```
   Укажите `colors` как кортеж с кодами цвета для текста и фона, используя библиотеку `colorama`.

6. **Закройте логгер (необязательно, но рекомендуется):**
   ```python
   logger.close_loggers()
   ```
   Этот шаг рекомендуется для корректного закрытия файлов логов.


Пример использования
-------------------------
.. code-block:: python

    import logging
    import colorama
    from hypotez.src.logger import Logger

    colorama.init(autoreset=True)  # Инициализация colorama

    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log'
    }

    logger: Logger = Logger()
    logger.initialize_loggers(**config)

    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.error("Деление на ноль!", ex=e, exc_info=True)

    logger.info("Выполнение прошло успешно")

    logger.close_loggers()
```
```
**Примечание:**  Библиотека `colorama` необходима для работы цветного вывода. Не забудьте ее установить: `pip install colorama`.  Так же, не забудьте заменить пути в `config` на ваши собственные.