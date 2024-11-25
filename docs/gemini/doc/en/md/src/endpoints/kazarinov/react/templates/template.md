# template.html

## Overview

This HTML template (`template.html`) defines the structure for displaying product information.  It utilizes Bootstrap for styling and dynamically renders product cards with images, titles, and descriptions.  The template also displays a total price.

## HTML Structure

This template uses standard HTML5 structure with semantic elements like `<head>`, `<body>`, `<div>`, and `<p>`, as well as  `<table>`, `<tr>`, and `<td>` for structuring content. It effectively utilizes Bootstrap classes for styling elements and arranging them in a grid.

## Variables

The following variables are used within the template:

- `language`: String representing the language.
- `title`: String representing the page title.
- `description`: String representing a brief description.
- `products`: List of product dictionaries. Each product dictionary should contain:
    - `image_local_saved_path`: Path to the product image.
    - `product_title`: String representing the product title.
    - `product_description`: String describing the product.
- `price`: Numeric value representing the total price.
- `currency`: String representing the currency.


## Styling

The `template.html` file includes inline CSS to customize the look and feel.  Key styles include:

- Background colors and text colors for the body and card elements.
- Font family.
- Styling for product cards (display, background, borders, padding, margins).
- Styling for images (width, height, object fit).
- Styling for the price tags (background, color).
- Styling for the footer (text alignment, margin).

## Usage

This template expects a list of products, and the total price, to be passed to it from a backend or controller in order to render the page. It handles showing the product images, titles, descriptions and the total price for all items rendered.

## Example Usage (Conceptual)

```html
{% extends "base.html" %}

{% block content %}
    {% include "template.html" with language='en' title='Products' description='List of available products' products=products price=totalPrice currency='$' %}
{% endblock %}
```

This example demonstrates how to render the template, passing necessary data to it.  Replace `products` and `totalPrice` with the actual variables from your application.

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