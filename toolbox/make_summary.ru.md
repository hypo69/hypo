```rst
.. module:: src.endpoints.hypo69.code_assistant.make_summary
```
<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/readme.ru.md'>src</A> \ 
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/readme.ru.md'>endpoints</A>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/readme.ru.md'>hypo69</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/code_assistant/make_summary.md'>English</A>
</TD>
</TR>
</TABLE>
# Модуль `make_summary.py`

## Описание

Этот модуль предназначен для автоматического создания файла `SUMMARY.md`, который используется для компиляции документации с помощью инструментов, таких как `mdbook`. Модуль рекурсивно обходит указанную директорию с исходными файлами `.md` и генерирует оглавление, включая или исключая файлы в зависимости от указанного языка.

## Основные возможности

- **Генерация `SUMMARY.md`**:
  - Рекурсивно обходит директорию с исходными файлами `.md`.
  - Создает файл `SUMMARY.md` с оглавлением для каждого `.md` файла.

- **Фильтрация по языку**:
  - Поддерживает фильтрацию файлов по языку:
    - `ru`: Включает только файлы с суффиксом `.ru.md`.
    - `en`: Исключает файлы с суффиксом `.ru.md`.

- **Универсальность**:
  - Все пути строятся относительно корня проекта, что делает модуль устойчивым к изменениям структуры директорий.

## Установка и запуск

### Требования

- Python 3.8 или выше.
- Установленные зависимости из файла `requirements.txt`.

### Установка

1. Убедитесь, что у вас установлен Python и все зависимости:
   ```bash
   pip install -r requirements.txt
   ```

### Использование

1. Запустите скрипт `make_summary.py` с указанием директории `src` и языка фильтрации:
   ```bash
   python src/endpoints/hypo69/code_assistant/make_summary.py -lang ru src
   ```

   - Параметр `-lang` может принимать значения `ru` или `en`.
   - Аргумент `src` указывает на директорию с исходными `.md` файлами.

2. После выполнения скрипта в директории `docs` будет создан файл `SUMMARY.md`.

## Пример вывода

### Пример `SUMMARY.md` для языка `ru`:
```
# Summary

- [file1](file1.md)
- [file2](file2.ru.md)
```

### Пример `SUMMARY.md` для языка `en`:
```
# Summary

- [file1](file1.md)
- [file3](file3.en.md)
```

## Автор

- **Имя автора**: [Ваше имя]
- **Email**: [Ваш email]
- **Ссылка на Boosty**: [https://boosty.to/hypo69](https://boosty.to/hypo69)

## Лицензия

Этот модуль лицензирован под [MIT License](../../../LICENSE).
