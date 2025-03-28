# Модуль `beeper`

## Обзор

Модуль `beeper` предназначен для генерации звуковых сигналов, оповещающих о различных событиях в системе. Он поддерживает несколько уровней оповещений, каждый из которых представлен уникальной мелодией. Модуль работает на Windows и Unix платформах и использует библиотеку `winsound` для генерации звуков.

## Оглавление
1. [Классы](#классы)
    - [BeepLevel](#beeplevel)
    - [BeepHandler](#beephandler)
    - [Beeper](#beeper)
2. [Функции](#функции)
    - [silent_mode](#silent_mode)

## Классы

### `BeepLevel`
**Описание**: Перечисление типов событий, определяющих мелодии для разных уровней оповещений.

**Атрибуты**:
-   `SUCCESS`: Мелодия для успешных событий.
-   `INFO`: Мелодия для информационных сообщений.
-   `INFO_LONG`: Длинная мелодия для информационных сообщений.
-   `ATTENTION`: Мелодия для сообщений, требующих внимания.
-   `WARNING`: Мелодия для предупреждений.
-   `DEBUG`: Мелодия для отладочных сообщений.
-   `ERROR`: Мелодия для ошибок.
-   `LONG_ERROR`: Длинная мелодия для ошибок.
-   `CRITICAL`: Мелодия для критических ошибок.
-   `BELL`: Мелодия звонка.

### `BeepHandler`
**Описание**: Обработчик звуковых сигналов, используемый для логгирования.

**Методы**:

#### `emit`
**Описание**: Метод для отправки звукового сигнала на основе уровня логгирования.
    
**Параметры**:
    - `record` (dict): Запись лога, содержащая уровень события.
  
**Вызывает исключения**:
  - `Exception`: Возникает при ошибке воспроизведения звука.
  
#### `beep`
**Описание**: Метод для воспроизведения звукового сигнала.
    
**Параметры**:
    - `level` (BeepLevel | str, optional): Уровень события. По умолчанию `BeepLevel.INFO`.
    - `frequency` (int, optional): Частота сигнала. По умолчанию `400`.
    - `duration` (int, optional): Длительность сигнала. По умолчанию `1000`.

### `Beeper`
**Описание**: Класс для управления звуковыми сигналами.

**Атрибуты**:
-   `silent` (bool): Флаг, определяющий, включен ли "беззвучный" режим. По умолчанию `False`.

**Методы**:
  
#### `beep`
**Описание**: Метод для воспроизведения звукового сигнала.
    
**Параметры**:
- `level` (BeepLevel | str, optional): Уровень события или его строковое представление (`success`, `info`, `attention` и т.д.). По умолчанию `BeepLevel.INFO`.
- `frequency` (int, optional): Частота сигнала. По умолчанию `400`.
- `duration` (int, optional): Длительность сигнала. По умолчанию `1000`.
    
**Возвращает**:
-   `None`: Метод ничего не возвращает.
    
**Вызывает исключения**:
-   `Exception`: Возникает при ошибке воспроизведения звука.

## Функции

### `silent_mode`
**Описание**: Декоратор для управления режимом "беззвучия".

**Параметры**:
   - `func` (function): Функция для декорирования.

**Возвращает**:
-   `function`: Обернутая функция, добавляющая проверку режима "беззвучия".

**Принцип работы**:
  - Если режим "беззвучия" включен, выводит сообщение о пропуске воспроизведения звука и не вызывает декорируемую функцию.
  - Если режим "беззвучия" выключен, вызывает декорируемую функцию.