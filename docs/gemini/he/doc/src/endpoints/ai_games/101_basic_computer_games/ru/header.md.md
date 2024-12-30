# `header.py`

## סקירה כללית

קוד זה נועד לזהות באופן אוטומטי את ספריית השורש של פרויקט ב-Python. הוא מפשט את העבודה עם נתיבים בפרויקט, במיוחד כאשר מבנה הפרויקט מורכב או כאשר יש צורך לקבוע באופן דינמי את ספריית השורש.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
    - [`set_project_root`](#set_project_root)

## פונקציות

### `set_project_root`

**תיאור**:
הפונקציה מחפשת את ספריית השורש של הפרויקט על ידי חיפוש קבצי "סמן" (marker files) כמו `pyproject.toml`, `requirements.txt` או `.git`. לאחר מכן היא מוסיפה את ספריית השורש ל-`sys.path` אם היא לא קיימת שם.

**פרמטרים**:
אין פרמטרים.

**החזרות**:
- `pathlib.Path`: מחזירה את נתיב ספריית השורש.

**דוגמה לשימוש**:
```python
from pathlib import Path
import sys
from header import __root__

# Определяем корневую директорию
__root__ = set_project_root()

# Теперь можно импортировать модули из корневой директории
from src.utils.helpers import some_function

print(f"Корневая директория: {__root__}")
some_function()
```
```python
def set_project_root() -> Path:
    """
    Args:
        None

    Returns:
         Path: הנתיב לספריית השורש של הפרויקט.

    Raises:
         None
    """
    current_file_path = Path(__file__).resolve()
    current_dir = current_file_path.parent

    marker_files = [
        "pyproject.toml",
        "requirements.txt",
        ".git",
    ]

    while True:
        for marker in marker_files:
            if (current_dir / marker).exists():
                if str(current_dir) not in sys.path:
                    sys.path.insert(0, str(current_dir))
                return current_dir

        if current_dir == current_dir.parent:
            raise FileNotFoundError("Project root not found")
        current_dir = current_dir.parent
```
```markdown