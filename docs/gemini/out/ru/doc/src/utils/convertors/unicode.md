# Модуль `unicode`

## Обзор

Модуль `unicode` содержит функцию `decode_unicode_escape`, предназначенную для декодирования юникодных escape-последовательностей в строках, словарях и списках. Функция рекурсивно обрабатывает вложенные структуры данных.

## Функции

### `decode_unicode_escape`

**Описание**: Функция декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

**Параметры**:
- `input_data` (dict | list | str): Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.


**Возвращает**:
- `dict | list | str`: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.

**Обрабатывает исключения**:
- `UnicodeDecodeError`: Если строка не может быть декодирована как юникод. В этом случае функция возвращает исходную строку без изменений.


**Пример использования**:

```python
input_dict = {
    'product_name': r'\u05de\u05e7"\\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
    'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
    'price': 123.45
}

input_list = [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']

input_string = r'\u05de\u05e7"\\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'

decoded_dict = decode_unicode_escape(input_dict)
decoded_list = decode_unicode_escape(input_list)
decoded_string = decode_unicode_escape(input_string)

print(decoded_dict)
print(decoded_list)
print(decoded_string)
```
```
```
```
```


```
```
```
```
```

```


```
```

```
```
```
```
```


```


```
```


```


```


```



```
```