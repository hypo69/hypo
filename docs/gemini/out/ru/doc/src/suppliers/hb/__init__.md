# Модуль hypotez/src/suppliers/hb/__init__.py

## Обзор

Этот модуль содержит начальную инициализацию для поставщика данных HB.  Он импортирует класс `Graber` из подмодуля `graber`.  Настоящий файл, по-видимому, предназначен для управления режимом работы (MODE) и импорта других компонентов.

## Конфигурация

### `MODE`

**Описание**: Переменная, определяющая режим работы системы.

**Значение**: `'dev'`


## Модули

### `Graber`

**Описание**: Класс для сбора данных от поставщика HB.

**Примечание**: Подробная документация для класса `Graber` должна находиться в файле `hypotez/src/suppliers/hb/graber.py`.



## Импорты

### `from .graber import Graber`

**Описание**: Импортирует класс `Graber` из модуля `graber` в текущем пакете.