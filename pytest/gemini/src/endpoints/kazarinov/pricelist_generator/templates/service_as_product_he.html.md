```python
import pytest
from pathlib import Path

# Define the path to the HTML file
HTML_FILE_PATH = Path("hypotez/src/endpoints/kazarinov/pricelist_generator/templates/service_as_product_he.html")

def test_html_file_exists():
    """
    Test that the HTML file exists at the specified path.
    """
    assert HTML_FILE_PATH.exists(), f"HTML file not found at: {HTML_FILE_PATH}"

def test_html_file_is_not_empty():
    """
    Test that the HTML file is not empty.
    """
    assert HTML_FILE_PATH.stat().st_size > 0, "HTML file is empty."

def test_html_contains_assembly_service_header():
    """
    Test that the HTML file contains the main heading related to computer assembly service.
    """
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<h3>שירותי הרכבה והגדרת מחשב</h3>" in content, "Main header for computer assembly service not found."

def test_html_contains_assembly_step1():
    """
    Test that the HTML file contains the description of computer assembly service step 1.
    """
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<h4>1. הרכבת המחשב</h4>" in content, "Computer assembly step 1 heading not found."
        assert "<p>אני מרכיב את המחשב שלכם, תוך התאמת כל הרכיבים לדרישות ולצרכים שלכם. אני משתמש רק ברכיבים בדוקים ואמינים כדי להבטיח שהמערכת תעבוד ביציבות לאורך זמן.</p>" in content, "Computer assembly step 1 description not found."

def test_html_contains_assembly_step2():
    """
    Test that the HTML file contains the description of computer assembly service step 2.
    """
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<h4>2. הגדרה מלאה</h4>" in content, "Computer assembly step 2 heading not found."
        assert "<p>לאחר ההרכבה, אני מתקין את מערכת ההפעלה, הדרייברים והתוכנות הנדרשות ומבצע את כל העדכונים. המחשב שלכם יהיה מוכן לשימוש מיד עם ההפעלה הראשונה.</p>" in content, "Computer assembly step 2 description not found."
        assert '<p class="note">*(תנאי: רישיון למערכת ההפעלה ולתוכנות אחרות אינו כלול במחיר. לפרטים נוספים התקשרו ל-054-422-94-97)*</p>' in content, "Computer assembly step 2 note not found."

def test_html_contains_assembly_step3():
     """
     Test that the HTML file contains the description of computer assembly service step 3.
     """
     with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<h4>3. הרצה וניסוי למשך 24 שעות</h4>" in content, "Computer assembly step 3 heading not found."
        assert "<p>לפני שאספק לכם את המחשב, אני מבצע בדיקות במשך 24 שעות כדי לוודא את הביצועים והיציבות של המערכת תחת עומסים שונים. כך אני מבטיח שתקבלו מחשב אמין וללא תקלות בלתי צפויות.</p>" in content, "Computer assembly step 3 description not found."

def test_html_contains_assembly_step4():
    """
    Test that the HTML file contains the description of computer assembly service step 4.
    """
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<h4>4. משלוח</h4>" in content, "Computer assembly step 4 heading not found."
        assert "<p>אני מבצע את המשלוח באופן אישי בזמן ובמקום שנוחים לכם, בין אם זה לבית או למשרד. במהלך המשלוח המחשב ייארז בצורה בטוחה כדי להבטיח את שלמותו.</p>" in content, "Computer assembly step 4 description not found."

def test_html_contains_assembly_step5():
    """
    Test that the HTML file contains the description of computer assembly service step 5.
    """
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<h4>5. חיבור והגדרה במקום</h4>" in content, "Computer assembly step 5 heading not found."
        assert "<p>בעת המשלוח, אני אחבר את המחשב למסך, למקלדת, לעכבר ולשאר ההתקנים שלכם. בנוסף, אגדיר את חיבור האינטרנט ואוודא שהכול פועל בצורה חלקה.</p>" in content, "Computer assembly step 5 description not found."

def test_html_contains_assembly_step6():
    """
    Test that the HTML file contains the description of computer assembly service step 6.
    """
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<h4>6. הסבר על תפעול המערכת</h4>" in content, "Computer assembly step 6 heading not found."
        assert "<p>לאחר החיבור, אסביר לכם כיצד להשתמש במערכת החדשה, אענה על כל שאלותיכם ואדגים את הפונקציות העיקריות. כך תוכלו להתחיל לעבוד בצורה קלה ומהירה.</p>" in content, "Computer assembly step 6 description not found."

def test_html_contains_ready_to_use_message():
    """
    Test that the HTML file contains the 'ready to use' message.
    """
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
        assert "<p><strong>המחשב שלכם יהיה מוכן לשימוש מיד לאחר ההתקנה.</strong></p>" in content, "Ready to use message not found."
```