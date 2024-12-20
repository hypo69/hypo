# Документация для файла `category.json`

## Обзор

Файл `category.json` содержит JSON-структуру с настройками для извлечения ссылок на продукты из HTML-страницы. 
Он определяет, какой атрибут следует использовать, каким методом искать элементы, и какие дополнительные параметры применяются.

## Содержание

- [Описание структуры JSON](#описание-структуры-json)
- [Раздел `product_links`](#раздел-product_links)
    - [Описание](#описание-product_links)
    - [Атрибуты](#атрибуты-product_links)
   

## Описание структуры JSON

JSON-файл состоит из одного объекта верхнего уровня, содержащего ключ `product_links`. Этот ключ связан с объектом, который описывает параметры для извлечения ссылок на продукты.

## Раздел `product_links`

### Описание

Объект `product_links` описывает конфигурацию для поиска и извлечения ссылок на продукты. 

### Атрибуты

- **`attribute`** (`str`):
    - Описывает HTML-атрибут, из которого нужно извлечь значение. В данном случае это `href`, атрибут HTML-тега `<a>`.
   
- **`by`** (`str`):
    - Указывает метод поиска элементов на странице. В данном случае используется `XPATH`, что означает поиск элементов с помощью XPath-запроса.
    
- **`selector`** (`str`):
    - Задает XPath-селектор для поиска нужных элементов. В данном случае, он нацелен на все `<a>` теги, расположенные внутри `<span>` элементов с атрибутом `data-component-type` равным `s-product-image`.
    
- **`if_list`** (`str`):
    - Определяет, как обрабатывать список найденных элементов. Значение `first` говорит о том, что из списка найденных элементов будет выбран только первый.
    
- **`use_mouse`** (`bool`):
    - Указывает, нужно ли имитировать действие мыши. Значение `false` означает, что это действие не требуется.
   
- **`mandatory`** (`bool`):
   -  Указывает, является ли элемент обязательным для нахождения на странице. `true` означает, что скрипт не продолжит работу, если элемент не будет найден.
   
- **`timeout`** (`int`):
    - Задает максимальное время ожидания (в секундах) для выполнения поиска элементов. Значение `0` может интерпретироваться как отсутствие таймаута или использование значения по умолчанию.
    
- **`timeout_for_event`** (`str`):
   - Определяет событие, которого нужно дождаться перед выполнением поиска. В данном случае `presence_of_element_located` означает, что скрипт будет ждать появления хотя бы одного элемента, удовлетворяющего селектору.

- **`event`** (`None`):
   - Событие, которое нужно дождаться. В данном случае не указанно.