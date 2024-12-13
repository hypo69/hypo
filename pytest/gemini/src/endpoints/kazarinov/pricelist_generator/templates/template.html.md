```python
import pytest
from jinja2 import Environment, FileSystemLoader
import os

# Define a fixture for the Jinja2 environment
@pytest.fixture
def jinja_env():
    """Sets up a Jinja2 environment for testing."""
    # Assuming the template is in the same directory as the test file
    template_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(template_dir))
    return env

# Define a fixture for sample product data
@pytest.fixture
def sample_products():
    """Provides sample product data for testing."""
    return [
        {
            "product_title": "Product 1",
            "product_description": "Description 1",
            "specification": "Spec 1",
            "image_local_saved_path": "/path/to/image1.jpg"
        },
        {
            "product_title": "Product 2",
            "product_description": "Description 2",
            "specification": "Spec 2",
            "image_local_saved_path": "/path/to/image2.jpg"
        }
    ]


def test_template_renders_with_valid_data(jinja_env, sample_products):
    """Tests if the template renders correctly with valid input data."""
    template = jinja_env.from_string("""
        <!DOCTYPE html>
        <html>
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
                    .row {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-between;
                    }
                    .product-card {
                        background-color: #f8f9fa; /* Светлый фон карточек */
                        border: 1pt solid #dee2e6;
                        border-radius: 8pt;
                        padding: 15pt;
                        margin: 15pt 0;
                        width: 100%;
                        box-sizing: border-box;
                    }
                    .product-card h3 {
                        margin-top: 0; /* Убираем верхний отступ у заголовка */
                    }
                    .product-card img {
                        width: 50pt; /* Новая ширина */
                        height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                        object-fit: contain; /* Сохранение пропорций изображения */
                        border-radius: 5pt;
                        background-color: white; /* Белый фон под изображением */
                        margin-right: 15pt; /* Отступ справа от изображения */
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

                    <div class="row">
                        {% for product in products %}
                        <div class="product-card">
                            <h3>{{ product.product_title }}</h3>
                            <div class="product-content">
                                <img src="{{ product.image_local_saved_path }}" 
                                     alt="{{ product.product_title }}" />
                                <div class="product-info">
                                    <p>{{ product.product_description }}</p>
                                    <p>{{ product.specification }}</p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>

                    <div class="footer">
                        <p>Общая стоимость: 
                            <span class="price-tag">{{ price }} {{ currency }}</span>
                        </p>
                    </div>
                </div>
            </body>
        </html>
        """)
    
    rendered_output = template.render(
        title="Test Title",
        description="Test Description",
        products=sample_products,
        price=100,
        currency="USD"
    )

    assert "<title>Test Title</title>" in rendered_output
    assert "<p class=\"lead\">Test Description</p>" in rendered_output
    assert "<h3>Product 1</h3>" in rendered_output
    assert "<h3>Product 2</h3>" in rendered_output
    assert "<span class=\"price-tag\">100 USD</span>" in rendered_output


def test_template_renders_with_empty_products_list(jinja_env):
    """Tests if the template renders correctly with an empty product list."""
    template = jinja_env.from_string("""
        <!DOCTYPE html>
        <html>
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
                    .row {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-between;
                    }
                    .product-card {
                        background-color: #f8f9fa; /* Светлый фон карточек */
                        border: 1pt solid #dee2e6;
                        border-radius: 8pt;
                        padding: 15pt;
                        margin: 15pt 0;
                        width: 100%;
                        box-sizing: border-box;
                    }
                    .product-card h3 {
                        margin-top: 0; /* Убираем верхний отступ у заголовка */
                    }
                    .product-card img {
                        width: 50pt; /* Новая ширина */
                        height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                        object-fit: contain; /* Сохранение пропорций изображения */
                        border-radius: 5pt;
                        background-color: white; /* Белый фон под изображением */
                        margin-right: 15pt; /* Отступ справа от изображения */
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

                    <div class="row">
                        {% for product in products %}
                        <div class="product-card">
                            <h3>{{ product.product_title }}</h3>
                            <div class="product-content">
                                <img src="{{ product.image_local_saved_path }}" 
                                     alt="{{ product.product_title }}" />
                                <div class="product-info">
                                    <p>{{ product.product_description }}</p>
                                    <p>{{ product.specification }}</p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>

                    <div class="footer">
                        <p>Общая стоимость: 
                            <span class="price-tag">{{ price }} {{ currency }}</span>
                        </p>
                    </div>
                </div>
            </body>
        </html>
        """)
    rendered_output = template.render(
        title="Test Title",
        description="Test Description",
        products=[],
        price=100,
        currency="USD"
    )

    assert "<title>Test Title</title>" in rendered_output
    assert "<p class=\"lead\">Test Description</p>" in rendered_output
    assert "<h3>" not in rendered_output
    assert "<span class=\"price-tag\">100 USD</span>" in rendered_output


def test_template_renders_with_missing_values(jinja_env, sample_products):
    """Tests the template's behavior when some input values are missing."""
    template = jinja_env.from_string("""
        <!DOCTYPE html>
        <html>
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
                    .row {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-between;
                    }
                    .product-card {
                        background-color: #f8f9fa; /* Светлый фон карточек */
                        border: 1pt solid #dee2e6;
                        border-radius: 8pt;
                        padding: 15pt;
                        margin: 15pt 0;
                        width: 100%;
                        box-sizing: border-box;
                    }
                    .product-card h3 {
                        margin-top: 0; /* Убираем верхний отступ у заголовка */
                    }
                    .product-card img {
                        width: 50pt; /* Новая ширина */
                        height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                        object-fit: contain; /* Сохранение пропорций изображения */
                        border-radius: 5pt;
                        background-color: white; /* Белый фон под изображением */
                        margin-right: 15pt; /* Отступ справа от изображения */
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

                    <div class="row">
                        {% for product in products %}
                        <div class="product-card">
                            <h3>{{ product.product_title }}</h3>
                            <div class="product-content">
                                <img src="{{ product.image_local_saved_path }}" 
                                     alt="{{ product.product_title }}" />
                                <div class="product-info">
                                    <p>{{ product.product_description }}</p>
                                    <p>{{ product.specification }}</p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>

                    <div class="footer">
                        <p>Общая стоимость: 
                            <span class="price-tag">{{ price }} {{ currency }}</span>
                        </p>
                    </div>
                </div>
            </body>
        </html>
        """)
    rendered_output = template.render(
        title="Test Title",
        description="Test Description",
        products=sample_products,
        # Missing price and currency
    )

    assert "<title>Test Title</title>" in rendered_output
    assert "<p class=\"lead\">Test Description</p>" in rendered_output
    assert "<h3>Product 1</h3>" in rendered_output
    assert "<h3>Product 2</h3>" in rendered_output
    assert "Общая стоимость:" in rendered_output
    #Price is not rendered due to missing variables, but no errors should be raised by jinja2
    assert "<span class=\"price-tag\"></span>" in rendered_output


def test_template_renders_with_empty_string_title_and_description(jinja_env, sample_products):
        """Tests the template rendering with an empty string for title and description"""
        template = jinja_env.from_string("""
        <!DOCTYPE html>
        <html>
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
                    .row {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-between;
                    }
                    .product-card {
                        background-color: #f8f9fa; /* Светлый фон карточек */
                        border: 1pt solid #dee2e6;
                        border-radius: 8pt;
                        padding: 15pt;
                        margin: 15pt 0;
                        width: 100%;
                        box-sizing: border-box;
                    }
                    .product-card h3 {
                        margin-top: 0; /* Убираем верхний отступ у заголовка */
                    }
                    .product-card img {
                        width: 50pt; /* Новая ширина */
                        height: auto; /* Автоматическая высота, чтобы сохранить пропорции */
                        object-fit: contain; /* Сохранение пропорций изображения */
                        border-radius: 5pt;
                        background-color: white; /* Белый фон под изображением */
                        margin-right: 15pt; /* Отступ справа от изображения */
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

                    <div class="row">
                        {% for product in products %}
                        <div class="product-card">
                            <h3>{{ product.product_title }}</h3>
                            <div class="product-content">
                                <img src="{{ product.image_local_saved_path }}" 
                                     alt="{{ product.product_title }}" />
                                <div class="product-info">
                                    <p>{{ product.product_description }}</p>
                                    <p>{{ product.specification }}</p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>

                    <div class="footer">
                        <p>Общая стоимость: 
                            <span class="price-tag">{{ price }} {{ currency }}</span>
                        </p>
                    </div>
                </div>
            </body>
        </html>
        """)
        rendered_output = template.render(
            title="",
            description="",
            products=sample_products,
            price=100,
            currency="USD"
        )

        assert "<title></title>" in rendered_output
        assert "<p class=\"lead\"></p>" in rendered_output
        assert "<h3>Product 1</h3>" in rendered_output
        assert "<h3>Product 2</h3>" in rendered_output
        assert "<span class=\"price-tag\">100 USD</span>" in rendered_output
```