# header

## סקירה כללית

המודול הזה אחראי על הגדרת משתנה ה-`__root__`, שמייצג את ספריית השורש של הפרויקט.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`set_project_root`](#set_project_root)

## פונקציות

### `set_project_root`

**Description**:
הפונקציה מוצאת את ספריית השורש של הפרויקט, החל מהספרייה הנוכחית של הקובץ, ועולה למעלה עד שהיא מוצאת אחד מקבצי הסימון.

**Parameters**:
- `marker_files` (tuple): שמות של קבצים או ספריות המשמשים לזיהוי ספריית השורש. ברירת מחדל: `('__root__', 'pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:
- `Path`: נתיב לספריית השורש אם נמצאה, או לספרייה שבה נמצא הסקריפט אם לא.

```python
def set_project_root(marker_files:tuple=('__root__','pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): שמות של קבצים או ספריות המשמשים לזיהוי ספריית השורש.

    Returns:
        Path: נתיב לספריית השורש אם נמצאה, או לספרייה שבה נמצא הסקריפט אם לא.
    """