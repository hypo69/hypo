Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет собой шаблон HTML для отображения карточек товаров.  Он использует Bootstrap для стилизации и отображает изображения товаров, заголовки, описания и общую стоимость.  Шаблон динамически генерирует карточки товаров, получая данные о продуктах из переменной `products`.

Шаги выполнения
-------------------------
1. **Загрузка внешних ресурсов:** Шаблон подключает CSS Bootstrap для стилизации и задает размеры окна браузера.
2. **Определение переменных:**  Используются переменные `language`, `title`, `description`, `products`, `price` и `currency`.  Эти переменные должны быть заданы в контексте шаблона, обычно передаваясь из контроллера.
3. **Отображение заголовка и описания:**  Шаблон выводит значение `title` и `description` в качестве заголовка и краткого описания страницы.
4. **Отображение карточек товаров:**  Цикл `{% for product in products %}` перебирает каждый продукт из списка `products`.
5. **Отображение изображения, названия и описания:** Для каждого продукта выводится изображение (`product.image_local_saved_path`), заголовок (`product.product_title`) и описание (`product.product_description`).  Обратите внимание, что пути к изображениям должны быть корректными.
6. **Отображение общей стоимости:** Выводится общая стоимость (`price`) с указанием валюты (`currency`). Разметка оформлена для красивого отображения цены (в блоке price-tag).

Пример использования
-------------------------
.. code-block:: html+django

    {# Шаблон в Django #}
    {% extends "base.html" %}  {# Базовый шаблон #}

    {% block content %}
        {% load static %}

        {% load humanize %}

        {% load django_bootstrap5 %}

        {% load currency_filters %}

        {% load i18n %}

        {% block title %}Товары{% endblock %}

        {% block description %}Список всех доступных товаров{% endblock %}

        {% load i18n %}

        <div class="container">
        
            {% if products %}
                {% include 'kazarinov/react/templates/template.html' with language="en" title="Products" description="Product catalog" products=products price=total_price currency="USD" %}
            {% else %}
            <p>Товары не найдены.</p>
            {% endif %}
        </div>
    
    {% endblock %}


    {# Пример данных в Python #}
    products = [
        {'image_local_saved_path': 'path/to/image1.jpg', 'product_title': 'Product 1', 'product_description': 'Description 1'},
        {'image_local_saved_path': 'path/to/image2.jpg', 'product_title': 'Product 2', 'product_description': 'Description 2'}
    ]
    total_price = 100