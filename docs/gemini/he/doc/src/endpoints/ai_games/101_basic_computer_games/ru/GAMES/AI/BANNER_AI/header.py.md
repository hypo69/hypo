# header

## סקירה כללית

מודול זה מגדיר את משתנה `__root__` (ספריית השורש של הפרויקט) ומספק פונקציה למציאת ספריית השורש של הפרויקט.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
    - [`set_project_root`](#set_project_root)
- [משתנים](#משתנים)
    - [`__root__`](#__root__)

## פונקציות

### `set_project_root`

**תיאור**:
פונקציה זו מוצאת את ספריית השורש של הפרויקט, החל מהספרייה הנוכחית של הקובץ, ועולה כלפי מעלה עד שמוצאת אחד מקבצי הסימון.

**פרמטרים**:
- `marker_files` (tuple): שמות של קבצים או ספריות לזיהוי ספריית השורש.

**החזרות**:
- `Path`: הנתיב לספריית השורש, אם נמצאה, אחרת הספרייה בה נמצא הסקריפט.

```python
def set_project_root(marker_files:tuple=('__root__','pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): שמות של קבצים או ספריות לזיהוי ספריית השורש.

    Returns:
        Path: הנתיב לספריית השורש, אם נמצאה, אחרת הספרייה בה נמצא הסקריפט.
    """
```

## משתנים

### `__root__`
**תיאור**:
נתיב לספריית השורש של הפרויקט.

```python
"""__root__ (Path): נתיב לספריית השורש של הפרויקט"""
```