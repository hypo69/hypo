# Модуль beeper.py

## Обзор

Модуль `beeper.py` предназначен для генерации звуковых сигналов различных типов, соответствующих разным уровням событий в системе. Он позволяет визуально и аудиально определять, что происходит в системе, используя различные мелодии и звуки для разных уровней важности.

## Подробней

Модуль `beeper.py` предоставляет классы и функции для воспроизведения звуковых сигналов, чтобы уведомлять пользователя о различных событиях в системе. Он содержит перечисление `BeepLevel`, определяющее различные типы событий (например, успех, информация, предупреждение, ошибка и т.д.), и класс `Beeper`, который отвечает за воспроизведение звуков. Расположение файла в проекте `hypotez/src/logger/beeper.py` указывает на его принадлежность к подсистеме логирования и оповещения.

## Классы

### `BeepLevel`

**Описание**: Класс перечислитель типов событий. Разным событиям соответствуют разные мелодии.

**Уровни событий**:
- `SUCCESS`
- `INFO`
- `ATTENTION`
- `WARNING`
- `DEBUG`
- `ERROR`
- `LONG_ERROR`
- `CRITICAL`
- `BELL`

**Примеры**:

```python
from src.logger.beeper import BeepLevel

level = BeepLevel.WARNING
print(level)  # Вывод: BeepLevel.WARNING
```

### `BeepHandler`

**Описание**: Класс обработчика звуковых сигналов.

**Методы**:
- `emit`: Воспроизводит звук в зависимости от уровня записи лога.

**Параметры**:
- `record` (LogRecord): Запись лога, содержащая уровень события.

**Примеры**:

```python
import logging
from src.logger.beeper import BeepHandler

# Создаем логгер
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

# Добавляем обработчик звука
handler = BeepHandler()
logger.addHandler(handler)

# Отправляем сообщение в лог
logger.warning('Это предупреждение!')
```

### `Beeper`

**Описание**: Класс для воспроизведения звуковых сигналов.

**Методы**:
- `beep`: Воспроизводит звуковой сигнал оповещения.

**Параметры**:
- `level` (BeepLevel | str): Тип события (`info`, `attention`, `warning`, `debug`, `error`, `long_error`, `critical`, `bell`).
- `frequency` (int): Частота сигнала (от 37 до 32000).
- `duration` (int): Длительность сигнала.

**Примеры**:

```python
import asyncio
from src.logger.beeper import Beeper, BeepLevel

async def main():
    await Beeper.beep(level=BeepLevel.INFO)
    await Beeper.beep(level='warning', frequency=600, duration=500)

if __name__ == "__main__":
    asyncio.run(main())
```

## Функции

### `silent_mode`

```python
def silent_mode(func):
    """
     Функция-декоратор для управления режимом "беззвучия".
    
    Args:
        func: Функция для декорирования.
    
    Returns:
        Обернутая функция, добавляющая проверку режима "беззвучия".
    """
```

**Описание**: Функция-декоратор для управления режимом "беззвучия".

**Параметры**:
- `func` (function): Функция для декорирования.

**Возвращает**:
- `function`: Обернутая функция, добавляющая проверку режима "беззвучия".

**Как работает функция**:
1. Функция `silent_mode` принимает функцию `func` в качестве аргумента и возвращает новую функцию `wrapper`.
2. Внутри `wrapper` проверяется, включен ли режим "беззвучия" (`Beeper.silent`).
3. Если режим "беззвучия" включен, выводится сообщение о пропуске воспроизведения звука, и функция завершается.
4. Если режим "беззвучия" выключен, вызывается оригинальная функция `func` с переданными аргументами, и возвращается результат её выполнения.

**Примеры**:

```python
from src.logger.beeper import Beeper, silent_mode

Beeper.silent = True  # Включаем режим "беззвучия"

@silent_mode
def test_function():
    print("Эта функция должна быть выполнена только если режим 'беззвучия' выключен.")
    return True

result = test_function()  # Вывод: Silent mode is enabled. Skipping beep.
print(result)  # Вывод: None

Beeper.silent = False # Выключаем режим "беззвучия"
result = test_function()
print(result)
```
```
Эта функция должна быть выполнена только если режим 'беззвучия' выключен.
True
```
```