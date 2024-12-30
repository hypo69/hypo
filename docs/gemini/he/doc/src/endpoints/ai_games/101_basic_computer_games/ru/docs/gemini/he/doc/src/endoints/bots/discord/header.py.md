# `header.py`

## סקירה כללית

קובץ זה מגדיר משתנים גלובליים ופונקציות עזר עבור בוט ה-Discord, כולל הגדרת נתיב השורש של הפרויקט, טעינת הגדרות מ-`settings.json`, וטעינת תיעוד מ-`README.MD`.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
  - [`set_project_root`](#set_project_root)
- [משתנים גלובליים](#משתנים-גלובליים)

## פונקציות

### `set_project_root`

**תיאור**:
מוצא את ספריית השורש של הפרויקט החל מהספרייה של הקובץ הנוכחי, מחפש כלפי מעלה ועוצר בספרייה הראשונה המכילה אחד מקבצי הסימון.

**פרמטרים**:
- `marker_files` (tuple, אופציונלי): שמות קבצים או שמות ספריות לזיהוי שורש הפרויקט. ברירת מחדל: `('__root__', '.git')`.

**Returns**:
- `Path`: נתיב לספריית השורש אם נמצאה, אחרת הספרייה בה נמצא הסקריפט.

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

## משתנים גלובליים

- `MODE` (str): מצב הפעולה של הבוט. ערך ברירת מחדל: `'dev'`.
- `__root__` (Path): נתיב לספריית השורש של הפרויקט. מוגדר על ידי הפונקציה `set_project_root`.
- `settings` (dict): הגדרות הפרויקט שנטענו מ-`settings.json`. ערך ברירת מחדל: `None`.
- `doc_str` (str): תיעוד הפרויקט שנטען מ-`README.MD`. ערך ברירת מחדל: `None`.
- `__project_name__` (str): שם הפרויקט. נטען מההגדרות או ברירת מחדל `'hypotez'`.
- `__version__` (str): גרסת הפרויקט. נטענת מההגדרות או ברירת מחדל `''`.
- `__doc__` (str): תיעוד הפרויקט. נטען מ-`doc_str` או ברירת מחדל `''`.
- `__details__` (str): פרטים נוספים על הפרויקט. ברירת מחדל `''`.
- `__author__` (str): מחבר הפרויקט. נטען מההגדרות או ברירת מחדל `''`.
- `__copyright__` (str): זכויות יוצרים של הפרויקט. נטען מההגדרות או ברירת מחדל `''`.
- `__cofee__` (str): הודעת תרומה למפתח. נטענת מההגדרות או ברירת מחדל: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69".