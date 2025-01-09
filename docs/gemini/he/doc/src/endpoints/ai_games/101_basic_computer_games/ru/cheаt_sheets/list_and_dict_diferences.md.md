# הבדלים בין רשימות ומילונים

## סקירה כללית

מסמך זה מסביר כיצד ניתן להשתמש ברשימות ובמילונים כדי לייצג נתוני מוצרים. הוא מדגים כיצד ניתן להשתמש במילון כדי לייצג את המאפיינים של מוצר בודד וכיצד ניתן להשתמש ברשימה כדי לייצג אוסף של מוצרים.

## תוכן עניינים

- [מילון (dict) לייצוג מאפייני מוצר](#מילון-dict-לייצוג-מאפייני-מוצר)
- [רשימה (list) לייצוג מוצרים בקטגוריה](#רשימה-list-לייצוג-מוצרים-בקטגוריה)

## מילון (`dict`) לייצוג מאפייני מוצר

המילון (`dict`) הוא דרך אידיאלית לייצג את המאפיינים של מוצר בודד באמצעות זוגות של "מפתח-ערך". המפתחות מייצגים את שמות המאפיינים, והערכים מייצגים את הערכים המתאימים.

```python
product = {
    "id": "12345",
    "name": "Смартфон SuperPhone X",
    "brand": "SuperTech",
    "price": 999.99,
    "color": "Space Gray",
    "screen_size": 6.7,
    "storage": "256 GB",
    "camera": "108 MP",
    "os": "Android 13",
    "available": True
}

print("--- Характеристики товара ---")
for key, value in product.items():
    print(f"{key}: {value}")

print("\n--- Доступ к конкретным характеристикам ---")
print(f"Название: {product['name']}")
print(f"Цена: ${product['price']}")
print(f"Доступен: {'да' if product['available'] else 'нет'}")
```

**הסבר קוד:**

* המילון `product` משמש לייצוג מאפייני המוצר, כאשר המפתחות הם שמות המאפיינים (id, name, brand, price וכו') והערכים הם הערכים המתאימים.
* `product.items()` משמש לאיטרציה על כל זוגות "מפתח-ערך" והדפסה שלהם.

## רשימה (`list`) לייצוג מוצרים בקטגוריה

הרשימה (`list`) היא דרך מצוינת לייצג אוסף של מוצרים מאותו סוג. כל רכיב ברשימה מייצג מוצר נפרד, אשר ניתן לייצג אותו כמילון.

```python
products = [
    {
        "id": "12345",
        "name": "Смартфон SuperPhone X",
        "brand": "SuperTech",
        "price": 999.99,
        "available": True
    },
    {
        "id": "67890",
        "name": "Планшет TabPro S",
        "brand": "TechGenius",
        "price": 799.99,
        "available": False
    },
    {
        "id": "13579",
        "name": "Наушники SoundBeats Pro",
        "brand": "AudioMax",
        "price": 199.99,
        "available": True
    }
]
print("\n--- Список товаров в категории ---")

for product in products:
   print(f"{product['name']} ({product['brand']}), Price: ${product['price']}, Available: {'Yes' if product['available'] else 'No'}")

print("\n--- Доступ к первому товару ---")

first_product = products[0]
print(f"ID: {first_product['id']}, Name: {first_product['name']}")

print("\n--- Вывод только имен товаров ---")
for product in products:
  print(f"Name: {product['name']}")
```

**הסבר קוד:**

* הרשימה `products` מכילה מילונים, כאשר כל מילון מייצג מוצר נפרד.
* הקוד מבצע איטרציה על הרשימה ומדפיס מידע על כל מוצר, תוך שימוש במפתחות המילון כדי לגשת למאפייני המוצר.
* הוא מראה כיצד לגשת למוצר הראשון ברשימה באמצעות האינדקס `0`.
* הקוד מדגים כיצד להדפיס רק את שמות המוצרים.