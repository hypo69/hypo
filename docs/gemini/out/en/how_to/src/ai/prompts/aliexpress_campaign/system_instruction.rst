rst
How to generate product category summaries
============================================================================================

Description
-------------------------
This code block defines a function (`promo_creater`) that generates summaries for product categories. It takes the category name, a list of product titles, and the desired language as input.  The function returns a JSON object where each category is a key, and the value is a dictionary containing the category name, a summarized title (up to 50 characters), and a detailed description tailored for housewives. The description draws on the product titles to provide a diverse and useful note.

Execution steps
-------------------------
1. **Input:** The function receives the `category_name`, `products_titles`, and `language` as input.
2. **Title Generation:** The function creates a concise `title` for the category that summarizes the `products_titles`. The summary should not exceed 50 characters.
3. **Description Generation:** The function generates a description tailored for housewives, drawing on the products mentioned in `products_titles`. The description must be concise and not exceed 1200 characters.  It focuses on practical and useful information regarding the products in the category.
4. **Output:** The function returns a JSON object with the `category_name` as the key, and a dictionary containing the `category_name`, `title`, and `description` as the value.

Usage example
-------------------------
.. code-block:: python

    language = "RU"
    category_name = "liitokala_18650"
    products_titles = [
        "Зарядное устройство LiitoKala Lii-M4S-M4 для аккумуляторных батарей, 3,7 в, 18650, 26650, 21700, 18500, литий-ионный, 1,2 в, Ni-MH, AA, испытательная Емкость",
        # ... (rest of the product titles)
    ]

    # Call the promo_creater function
    result = promo_creater(category_name, products_titles, language)
    print(result)