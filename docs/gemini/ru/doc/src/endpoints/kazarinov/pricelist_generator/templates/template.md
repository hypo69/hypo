# Шаблон HTML для генерации прайс-листа

## Обзор

Данный шаблон HTML (`template.html`) предназначен для генерации прайс-листа. Он позволяет отображать информацию о продуктах, включая заголовок, описание, спецификацию, изображение и цену. Шаблон использует стили CSS для визуального оформления.

## Структура

Шаблон состоит из нескольких блоков:

* **Заголовок:** Отображает название прайс-листа.
* **Описание:**  Краткое описание прайс-листа.
* **Список продуктов:**  Отображает информацию о каждом продукте в отдельной карточке.  Каждая карточка содержит заголовок продукта, изображение, описание и спецификацию.
* **Общая стоимость:**  Отображает общую стоимость всех продуктов с указанием валюты.
* **Футер:**  Нижняя часть страницы с указанием общей стоимости.

## Структура HTML-документа

### Тег `<html>`

* Определяет корневой элемент HTML-документа.

### Тег `<head>`

* Содержит мета-данные документа, такие как кодировка символов, viewport мета-тег и заголовок страницы.
    * `meta charset="UTF-8"`: Устанавливает кодировку символов для страницы.
    * `meta name="viewport" content="width=device-width, initial-scale=1.0"`:  Настройка отображения на разных устройствах.
    * `title={{ title }}`: Заголовок страницы, который динамически подставляется.


### Тег `<style>`

* Содержит CSS-стили для оформления страницы. Стиль задаёт:
    *  фон и цвет текста;
    *  шрифты;
    *  размер контейнера;
    *  стиль заголовков;
    *  стиль описаний;
    *  стиль карточек продукта;
    *  стиль изображений;
    *  стиль информации о продукте;
    *  стиль тега цены;
    *  стиль футера.


### Тег `<body>`

* Содержит основное содержимое страницы.

#### Контейнер `.container`

* Контейнер для всего содержимого страницы, обеспечивающий центрирование и задающий ширину.

#### Заголовок `<h1>`

* Отображает название прайс-листа, полученное из переменной `{{ title }}`. Центрирован по горизонтали.

#### Описание `<p class="lead">`

* Отображает описание прайс-листа, полученное из переменной `{{ description }}`. Центрирован по горизонтали.


#### Блок `.row`

* Блок для отображения карточек продуктов. Использование `flex` для адаптивного макета.

#### Карточка продукта `.product-card`

* Карточка для каждого продукта.  Используется для визуального оформления.

##### Заголовок продукта `<h3>`

* Заголовок продукта.


#####  Изображение `<img>`

* Изображение продукта.
    *  `src="{{ product.image_local_saved_path }}"`:  Путь к изображению продукта.
    * `alt="{{ product.product_title }}"`:  Альтернативный текст для изображения.

##### Информация о продукте `.product-info`

* Блок для отображения описания продукта и спецификации.
* `flex: 1;`: Занимает оставшееся пространство внутри карточки.

##### Описание продукта `<p>`
##### Спецификация продукта `<p>`

#### Общая стоимость `<div class="footer">`

* Блок для отображения общей стоимости. Использует теги `<span>` для выделения цены.

## Динамические данные

Шаблон использует шаблонизатор, как видно по синтаксису `{{ ... }}`.  Это позволяет подставлять в шаблон динамические данные (название, описание, продукты, цена и валюта), получаемые из Python кода.

## Заключение

Шаблон HTML позволяет динамически генерировать прайс-лист, отображая информацию о продуктах в удобном и наглядном формате.  Важны адаптивные стили для корректного отображения на разных устройствах.