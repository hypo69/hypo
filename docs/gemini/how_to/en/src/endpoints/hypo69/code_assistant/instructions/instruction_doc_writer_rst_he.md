# הוראות ליצירת תיעוד Python ב-reStructuredText (rst)

הוראות אלה מתארות כיצד ליצור תיעוד ב-reStructuredText (rst) לקובצי Python, עבור שימוש עם Sphinx.

**1. פורמט תיעוד**

* השתמש בסטנדרט `reStructuredText (rst)`.
* כל קובץ צריך להתחיל בכותרת ובתיאור קצר של התוכן שלו.
* עבור כל מחלקה ופונקציה, השתמש בפורמט ההערות הבא:

```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    ארגומנטים:
        param (str): תיאור הפרמטר `param`.
        param1 (Optional[str | dict | str], optional): תיאור הפרמטר `param1`. ברירת המחדל היא `None`.

    ערך מוחזר:
        dict | None: תיאור הערך המוחזר. מחזיר מילון או `None`.

    יוצאים:
        SomeError: תיאור המצב שבו מתרחש החריג `SomeError`.
    """
```

* השתמש ב-`ex` במקום `e` בחסימות טיפול בחריגים. לדוגמה: `try...ex...except`

**2. עץ תוכן (TOC)**

* כלול פרקים בתיעוד באמצעות `.. toctree::`.
* קובץ `index.rst` צריך לכלול קישורים לכל התיאורים של המודולים.


**3. עיצוב תיעוד**

* כל כותרות מחלקות, פונקציות ושיטות צריכות להיות מתועדות באמצעות פקודות Sphinx (`autoclass`, `autofunction`).
* דוגמה:

```rst
.. automodule:: module_name
    :members:
    :undoc-members:
    :show-inheritance:
```

**4. כותרות פרקים**

* השתמש בכותרות ברמה 1 (`=`), רמה 2 (`-`), רמה 3 (`~`) ורמה 4 (`^`).

**5. דוגמת קובץ (index.rst)**

```rst
שם המודול
==========

.. automodule:: module_name
    :members:
    :undoc-members:
    :show-inheritance:

פונקציות
--------

.. autofunction:: module_name.function_name
```

**דוגמה נוספת (module_name.py):**

```python
def my_function(name: str) -> str:
    """
    ארגומנטים:
        name (str): שם האדם.

    ערך מוחזר:
        str: תוכל להחזיר מסר אישי.
    """
    return f"Hello, {name}!"
```


**הנחיות נוספות:**

* ודא שאתה משתמש בפורמט הנכון של `reStructuredText`.
* ודא שכל קובצי ה-Python שלך מקיימים את הנחיות התיעוד.
* בדוק את התיעוד המוגמר עם Sphinx כדי לוודא שהוא נראה כרצוי.

**הערה:** השתמש בפקודות `autodoc` ו-`autosummary` של Sphinx לתיעוד אוטומטי של קובצי Python.


```