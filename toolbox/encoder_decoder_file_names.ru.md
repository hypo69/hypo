```markdown
# PathEncoderDecoder: Руководство пользователя

Модуль `PathEncoderDecoder` предоставляет методы для кодирования полного пути к файлу в короткий уникальный идентификатор и его обратного декодирования. Этот инструмент полезен для оптимизации хранения и обработки длинных путей. В данном руководстве описаны шаги для использования класса `PathEncoderDecoder`.

---

## Установка

1. Убедитесь, что у вас установлен Python версии 3.7 или выше.
2. Сохраните файл модуля `PathEncoderDecoder` под именем `encoder_decoder_file_names.py` в нужной директории.

---

## Описание функциональности

### Методы

1. **`encode(file_path: str) -> str`**  
   Кодирует полный путь файла в короткий идентификатор (8 символов от MD5-хэша).  
   - Создает запись в SQLite базе данных.
   - Возвращает уникальный идентификатор.

2. **`decode(short_id: str) -> Optional[str]`**  
   Декодирует идентификатор обратно в полный путь.  
   - Ищет путь в базе данных.
   - Возвращает полный путь или `None`, если идентификатор не найден.

3. **`clear_mapping()`**  
   Очищает все записи в базе данных.

---

## Пример использования

### 1. Подготовка

Сохраните модуль с классом `PathEncoderDecoder` и создайте тестовый скрипт для проверки функциональности. Пример файла:

```python
from encoder_decoder_file_names import PathEncoderDecoder

# Создаем экземпляр PathEncoderDecoder
encoder_decoder = PathEncoderDecoder()

# Исходный путь к файлу
original_path = 'src/same_folder/same_sub_folder/same-file.ext'

# Кодирование пути
encoded = encoder_decoder.encode(original_path)
print(f'Кодированный путь: {encoded}')

# Декодирование пути
decoded = encoder_decoder.decode(encoded)
print(f'Декодированный путь: {decoded}')
```

---

### 2. Кодирование пути

**Шаги:**
1. Передайте полный путь файла в метод `encode`.
2. Метод вернет короткий идентификатор (например, `id-1a2b3c4d`).
3. В базе данных будет создана запись с соответствием между идентификатором и исходным путем.

**Пример кода:**
```python
encoded = encoder_decoder.encode('src/my_folder/my_file.txt')
print(f'Кодированный путь: {encoded}')
```

**Результат:**
```
Кодированный путь: id-9f8e7d6c
```

---

### 3. Декодирование пути

**Шаги:**
1. Передайте короткий идентификатор в метод `decode`.
2. Метод вернет исходный путь файла.

**Пример кода:**
```python
decoded = encoder_decoder.decode('id-9f8e7d6c')
print(f'Декодированный путь: {decoded}')
```

**Результат:**
```
Декодированный путь: src/my_folder/my_file.txt
```

---

### 4. Очистка таблицы

**Шаги:**
1. Вызовите метод `clear_mapping`.
2. Все записи в базе данных будут удалены.

**Пример кода:**
```python
encoder_decoder.clear_mapping()
print('Все записи удалены.')
```

**Результат:**
```
Все записи удалены.
```

---

## Хранение данных

Все соответствия хранятся в SQLite базе данных `path_mapping.db`, которая создается автоматически при использовании класса. Таблица `path_mapping` содержит две колонки:
- `id`: короткий идентификатор пути.
- `file_path`: полный путь файла.

---

## Возможные ошибки

1. **Декодирование несуществующего идентификатора**
   - Если передан идентификатор, отсутствующий в базе, метод `decode` вернет `None`.

2. **Повторное кодирование**
   - Если путь уже был закодирован, `encode` вернет существующий идентификатор.

---

## Заключение

Модуль `PathEncoderDecoder` упрощает работу с длинными путями, минимизируя их до компактного формата и обеспечивая возможность восстановления. Его легко интегрировать в существующие проекты для оптимизации хранения и обработки файлов.
```