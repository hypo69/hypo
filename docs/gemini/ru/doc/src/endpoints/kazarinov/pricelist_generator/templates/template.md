# Шаблон HTML для генерации прайс-листа

## Обзор

Данный HTML-шаблон предназначен для генерации прайс-листа. Он динамически отображает информацию о продуктах, включая изображение, название, описание и спецификацию.  Шаблон также включает общую стоимость заказа.


## Структура

### Тег `<html>`

Содержит основную структуру HTML-документа.

### Тег `<head>`

Содержит мета-данные, такие как заголовок страницы (`{{ title }}`) и CSS-стили.

### Тег `<body>`

Содержит основное содержимое страницы, включая заголовок, описание, карточки с продуктами и общую стоимость.


### Заголовок (`<h1>`)

Выводит заданный заголовок (`{{ title }}`).

### Описание (`<p class="lead">`)

Отображает краткое описание (`{{ description }}`).

### Карточки продуктов (`<div class="row">`)

Динамически генерирует карточки для каждого продукта (`{% for product in products %}...{% endfor %}`).

#### Карточка продукта (`<div class="product-card">`)

- Отображает изображение продукта (`{{ product.image_local_saved_path }}`).
- Выводит заголовок продукта (`{{ product.product_title }}`).
- Отображает описание продукта (`{{ product.product_description }}`).
- Отображает спецификацию продукта (`{{ product.specification }}`).


### Общая стоимость (`<div class="footer">`)

Отображает общую стоимость (`{{ price }} {{ currency }}`)  в выделенном формате.


## Динамические переменные

Шаблон использует следующие динамические переменные:

- `{{ title }}`: Заголовок страницы.
- `{{ description }}`: Краткое описание страницы.
- `{{ products }}`: Список продуктов (список словарей).  Каждый словарь должен содержать поля `image_local_saved_path`, `product_title`, `product_description` и `specification`.
- `{{ price }}`: Общая стоимость заказа.
- `{{ currency }}`: Валюта.


## CSS-стили

CSS-стили контролируют внешний вид страницы:

- Фон, цвет текста и шрифт.
- Выравнивание и размер заголовков.
- Стиль карточек продуктов.
- Разметка и отображение изображений.
- Стиль для информации о цене.
- Стиль подвала.


## Пример использования

```html
<!DOCTYPE html>
<html>
<body>
  <!-- ... (rest of the template) ... -->
</body>
</html>
```

В примере выше показан фрагмент кода, показывающий структуру HTML-шаблона. В реальном использовании, данные для переменных должны быть предоставлены через контекст или данные модели.  Например, `{{ products }}` должен содержать список словарей с необходимыми полями.


```python
# Пример данных для заполнения шаблона
products_data = [
    {'image_local_saved_path': 'image1.jpg', 'product_title': 'Продукт 1', 'product_description': 'Описание продукта 1', 'specification': 'Характеристики 1'},
    {'image_local_saved_path': 'image2.jpg', 'product_title': 'Продукт 2', 'product_description': 'Описание продукта 2', 'specification': 'Характеристики 2'},
]
```

Данный пример иллюстрирует как можно использовать шаблон и заполнить его данными.


## Заключение

Данный HTML-шаблон позволяет динамически создавать прайс-листы с отображением изображений, названий, описаний и спецификаций продуктов. Он подходит для использования в системах, где необходимо генерировать и отображать прайс-листы.