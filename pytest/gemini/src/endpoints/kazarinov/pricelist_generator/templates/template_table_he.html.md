```python
import pytest
from jinja2 import Environment, FileSystemLoader
import os

# Fixture to load the template
@pytest.fixture
def template_env():
    """Sets up the Jinja2 environment for template loading."""
    template_dir = os.path.dirname(os.path.abspath(__file__))
    return Environment(loader=FileSystemLoader(template_dir))

# Fixture to provide sample data for the template
@pytest.fixture
def sample_data():
    """Provides sample data for rendering the template."""
    return {
        "title": "Test Pricelist",
        "description": "This is a test pricelist description.",
        "products": [
            {
                "product_title": "Product 1",
                "product_description": "Description for product 1.",
                "specification": "Spec 1",
                "image_local_saved_path": "image1.jpg"
            },
            {
                "product_title": "Product 2",
                "product_description": "Description for product 2.",
                 "specification": "Spec 2",
                "image_local_saved_path": "image2.jpg"
            }
        ],
        "price": 100.00,
        "currency": "USD"
    }

def test_template_render_valid_data(template_env, sample_data):
    """Tests successful rendering of template with valid data."""
    template = template_env.from_string(
    """
    <!DOCTYPE html>
    <html dir="rtl">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
        <style>
            body {
                background-color: #ffffff; /* Белый фон */
                color: #000000; /* Черный текст */
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                direction: rtl; /* Направление текста справа налево */
            }
            h1 {
                text-align: center;
                margin-top: 50pt;
                font-size: 36pt;
            }
            .lead {
                text-align: center;
                font-size: 18pt;
                margin: 10pt 0;
            }
            .container {
                width: 90%;
                margin: 0 auto;
            }
            .product-card {
                background-color: #f8f9fa; /* Светлый фон карточек */
                border: 1pt solid #dee2e6;
                border-radius: 8pt;
                padding: 15pt;
                margin: 15pt 0;
                display: flex;
                align-items: flex-start;
                box-sizing: border-box;
            }
            .product-card h3 {
                margin-top: 0; /* Убираем верхний отступ у заголовка */
            }
            .product-card img {
                width: 150pt; /* Новая ширина */
                height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                object-fit: contain; /* Сохранение пропорций изображения */
                border-radius: 5pt;
                background-color: white; /* Белый фон под изображением */
                margin-left: 15pt; /* Отступ слева от изображения */
            }
            .product-info {
                flex: 1; /* Занимает оставшееся пространство */
            }
            .price-tag {
                background-color: #238636;
                color: white;
                padding: 5pt 10pt;
                border-radius: 5pt;
                font-weight: bold;
            }
            .footer {
                text-align: center;
                margin-top: 30pt;
                padding: 15pt;
                border-top: 1pt solid #dee2e6;
            }
        </style>
    </head>
    
    <body>
        <div class="container">
            <h1>{{ title }}</h1>
            <p class="lead">{{ description }}</p>
    
            {% for product in products %}
            <div class="product-card">
                <img src="{{ product.image_local_saved_path }}" alt="{{ product.product_title }}" />
                <div class="product-info">
                    <h3>{{ product.product_title }}</h3>
                    <p>{{ product.product_description }}</p>
                    <p>{{ product.specification }}</p>
                </div>
            </div>
            {% endfor %}
    
            <div class="footer">
                <p>מחיר כולל הכל: 
                    <span class="price-tag">{{ price }} {{ currency }}</span>
                </p>
            </div>
        </div>
    </body>
    
    </html>
    """
    )
    rendered_html = template.render(sample_data)
    assert "<title>Test Pricelist</title>" in rendered_html
    assert "<p class=\"lead\">This is a test pricelist description.</p>" in rendered_html
    assert "<h3>Product 1</h3>" in rendered_html
    assert "<h3>Product 2</h3>" in rendered_html
    assert "<span class=\"price-tag\">100.0 USD</span>" in rendered_html


def test_template_render_empty_products(template_env):
    """Tests rendering of template with empty product list."""
    template = template_env.from_string(
        """
        <!DOCTYPE html>
        <html dir="rtl">
        
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ title }}</title>
            <style>
                body {
                    background-color: #ffffff; /* Белый фон */
                    color: #000000; /* Черный текст */
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    direction: rtl; /* Направление текста справа налево */
                }
                h1 {
                    text-align: center;
                    margin-top: 50pt;
                    font-size: 36pt;
                }
                .lead {
                    text-align: center;
                    font-size: 18pt;
                    margin: 10pt 0;
                }
                .container {
                    width: 90%;
                    margin: 0 auto;
                }
                .product-card {
                    background-color: #f8f9fa; /* Светлый фон карточек */
                    border: 1pt solid #dee2e6;
                    border-radius: 8pt;
                    padding: 15pt;
                    margin: 15pt 0;
                    display: flex;
                    align-items: flex-start;
                    box-sizing: border-box;
                }
                .product-card h3 {
                    margin-top: 0; /* Убираем верхний отступ у заголовка */
                }
                .product-card img {
                    width: 150pt; /* Новая ширина */
                    height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                    object-fit: contain; /* Сохранение пропорций изображения */
                    border-radius: 5pt;
                    background-color: white; /* Белый фон под изображением */
                    margin-left: 15pt; /* Отступ слева от изображения */
                }
                .product-info {
                    flex: 1; /* Занимает оставшееся пространство */
                }
                .price-tag {
                    background-color: #238636;
                    color: white;
                    padding: 5pt 10pt;
                    border-radius: 5pt;
                    font-weight: bold;
                }
                .footer {
                    text-align: center;
                    margin-top: 30pt;
                    padding: 15pt;
                    border-top: 1pt solid #dee2e6;
                }
            </style>
        </head>
        
        <body>
            <div class="container">
                <h1>{{ title }}</h1>
                <p class="lead">{{ description }}</p>
        
                {% for product in products %}
                <div class="product-card">
                    <img src="{{ product.image_local_saved_path }}" alt="{{ product.product_title }}" />
                    <div class="product-info">
                        <h3>{{ product.product_title }}</h3>
                        <p>{{ product.product_description }}</p>
                        <p>{{ product.specification }}</p>
                    </div>
                </div>
                {% endfor %}
        
                <div class="footer">
                    <p>מחיר כולל הכל: 
                        <span class="price-tag">{{ price }} {{ currency }}</span>
                    </p>
                </div>
            </div>
        </body>
        
        </html>
        """
    )
    data = {
        "title": "Pricelist with no products",
        "description": "This pricelist has no products",
        "products": [],
        "price": 0.0,
        "currency": "USD"
    }
    rendered_html = template.render(data)
    assert "<title>Pricelist with no products</title>" in rendered_html
    assert "<p class=\"lead\">This pricelist has no products</p>" in rendered_html
    assert "מחיר כולל הכל:" in rendered_html
    assert "<span class=\"price-tag\">0.0 USD</span>" in rendered_html
    assert "product-card" not in rendered_html


def test_template_render_missing_data(template_env):
     """Tests behavior when required data is missing."""
     template = template_env.from_string(
         """
        <!DOCTYPE html>
        <html dir="rtl">
        
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ title }}</title>
            <style>
                body {
                    background-color: #ffffff; /* Белый фон */
                    color: #000000; /* Черный текст */
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    direction: rtl; /* Направление текста справа налево */
                }
                h1 {
                    text-align: center;
                    margin-top: 50pt;
                    font-size: 36pt;
                }
                .lead {
                    text-align: center;
                    font-size: 18pt;
                    margin: 10pt 0;
                }
                .container {
                    width: 90%;
                    margin: 0 auto;
                }
                .product-card {
                    background-color: #f8f9fa; /* Светлый фон карточек */
                    border: 1pt solid #dee2e6;
                    border-radius: 8pt;
                    padding: 15pt;
                    margin: 15pt 0;
                    display: flex;
                    align-items: flex-start;
                    box-sizing: border-box;
                }
                .product-card h3 {
                    margin-top: 0; /* Убираем верхний отступ у заголовка */
                }
                .product-card img {
                    width: 150pt; /* Новая ширина */
                    height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                    object-fit: contain; /* Сохранение пропорций изображения */
                    border-radius: 5pt;
                    background-color: white; /* Белый фон под изображением */
                    margin-left: 15pt; /* Отступ слева от изображения */
                }
                .product-info {
                    flex: 1; /* Занимает оставшееся пространство */
                }
                .price-tag {
                    background-color: #238636;
                    color: white;
                    padding: 5pt 10pt;
                    border-radius: 5pt;
                    font-weight: bold;
                }
                .footer {
                    text-align: center;
                    margin-top: 30pt;
                    padding: 15pt;
                    border-top: 1pt solid #dee2e6;
                }
            </style>
        </head>
        
        <body>
            <div class="container">
                <h1>{{ title }}</h1>
                <p class="lead">{{ description }}</p>
        
                {% for product in products %}
                <div class="product-card">
                    <img src="{{ product.image_local_saved_path }}" alt="{{ product.product_title }}" />
                    <div class="product-info">
                        <h3>{{ product.product_title }}</h3>
                        <p>{{ product.product_description }}</p>
                        <p>{{ product.specification }}</p>
                    </div>
                </div>
                {% endfor %}
        
                <div class="footer">
                    <p>מחיר כולל הכל: 
                        <span class="price-tag">{{ price }} {{ currency }}</span>
                    </p>
                </div>
            </div>
        </body>
        
        </html>
        """
     )

     with pytest.raises(Exception):  # Catch the jinja2.exceptions.UndefinedError
         template.render({"title": "Pricelist"})


def test_template_render_with_special_characters(template_env):
    """Tests template rendering with special characters in the data."""
    template = template_env.from_string(
        """
        <!DOCTYPE html>
        <html dir="rtl">
        
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ title }}</title>
            <style>
                body {
                    background-color: #ffffff; /* Белый фон */
                    color: #000000; /* Черный текст */
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    direction: rtl; /* Направление текста справа налево */
                }
                h1 {
                    text-align: center;
                    margin-top: 50pt;
                    font-size: 36pt;
                }
                .lead {
                    text-align: center;
                    font-size: 18pt;
                    margin: 10pt 0;
                }
                .container {
                    width: 90%;
                    margin: 0 auto;
                }
                .product-card {
                    background-color: #f8f9fa; /* Светлый фон карточек */
                    border: 1pt solid #dee2e6;
                    border-radius: 8pt;
                    padding: 15pt;
                    margin: 15pt 0;
                    display: flex;
                    align-items: flex-start;
                    box-sizing: border-box;
                }
                .product-card h3 {
                    margin-top: 0; /* Убираем верхний отступ у заголовка */
                }
                .product-card img {
                    width: 150pt; /* Новая ширина */
                    height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                    object-fit: contain; /* Сохранение пропорций изображения */
                    border-radius: 5pt;
                    background-color: white; /* Белый фон под изображением */
                    margin-left: 15pt; /* Отступ слева от изображения */
                }
                .product-info {
                    flex: 1; /* Занимает оставшееся пространство */
                }
                .price-tag {
                    background-color: #238636;
                    color: white;
                    padding: 5pt 10pt;
                    border-radius: 5pt;
                    font-weight: bold;
                }
                .footer {
                    text-align: center;
                    margin-top: 30pt;
                    padding: 15pt;
                    border-top: 1pt solid #dee2e6;
                }
            </style>
        </head>
        
        <body>
            <div class="container">
                <h1>{{ title }}</h1>
                <p class="lead">{{ description }}</p>
        
                {% for product in products %}
                <div class="product-card">
                    <img src="{{ product.image_local_saved_path }}" alt="{{ product.product_title }}" />
                    <div class="product-info">
                        <h3>{{ product.product_title }}</h3>
                        <p>{{ product.product_description }}</p>
                        <p>{{ product.specification }}</p>
                    </div>
                </div>
                {% endfor %}
        
                <div class="footer">
                    <p>מחיר כולל הכל: 
                        <span class="price-tag">{{ price }} {{ currency }}</span>
                    </p>
                </div>
            </div>
        </body>
        
        </html>
        """
    )
    data = {
        "title": "Test <title> & \"Quotes\"",
        "description": "Description with < and > & special chars like &amp;.",
        "products": [
            {
                "product_title": "Product with < > & \"",
                "product_description": "Desc < > & \"",
                "specification": "Spec < > & \"",
                "image_local_saved_path": "image.jpg"
            }
        ],
        "price": 99.99,
        "currency": "€"
    }
    rendered_html = template.render(data)
    assert "Test &lt;title&gt; &amp; &quot;Quotes&quot;" in rendered_html
    assert "Description with &lt; and &gt; &amp; special chars like &amp;amp;." in rendered_html
    assert "Product with &lt; &gt; &amp; &quot;" in rendered_html
    assert "Desc &lt; &gt; &amp; &quot;" in rendered_html
    assert "Spec &lt; &gt; &amp; &quot;" in rendered_html
    assert "<span class=\"price-tag\">99.99 €</span>" in rendered_html
```