# src.logger.header

## סקירה כללית

מודול זה מגדיר את נתיב השורש לפרויקט. כל הייבוא בנוי ביחס לנתיב זה.

**TODO**: בעתיד להעביר למשתנה מערכת.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
    - [`set_project_root`](#set_project_root)
- [משתנים](#משתנים)
    - [`__root__`](#__root__)
    - [`settings`](#settings)
    - [`doc_str`](#doc_str)
    - [`__project_name__`](#__project_name__)
    - [`__version__`](#__version__)
    - [`__doc__`](#__doc__)
    - [`__details__`](#__details__)
    - [`__author__`](#__author__)
    - [`__copyright__`](#__copyright__)
    - [`__cofee__`](#__cofee__)

## פונקציות

### `set_project_root`

**Description**:
מוצא את ספריית השורש של הפרויקט החל מהספרייה של הקובץ הנוכחי,
מחפש כלפי מעלה ועוצר בספרייה הראשונה המכילה אחד מקבצי הסימון.

**Parameters**:
- `marker_files` (tuple): שמות קבצים או שמות ספריות לזיהוי שורש הפרויקט.

**Returns**:
- `Path`: הנתיב לספריית השורש אם נמצא, אחרת לספרייה בה ממוקם הסקריפט.

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

## משתנים

### `__root__`

**Description**:
נתיב לספריית השורש של הפרויקט.

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

### `settings`

**Description**:
מילון המכיל את הגדרות הפרויקט מקובץ `settings.json`.

```python
settings:dict = None
```

### `doc_str`

**Description**:
מחרוזת המכילה את תוכן הקובץ `README.MD`.

```python
doc_str:str = None
```

### `__project_name__`

**Description**:
שם הפרויקט, נלקח מ-`settings.json` או `hypotez` כברירת מחדל.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Description**:
גרסת הפרויקט, נלקחת מ-`settings.json` או מחרוזת ריקה כברירת מחדל.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Description**:
תיעוד הפרויקט, נלקח מ-`README.MD` או מחרוזת ריקה כברירת מחדל.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Description**:
פרטי הפרויקט (כרגע ריק).

```python
__details__: str = ''
```

### `__author__`

**Description**:
מחבר הפרויקט, נלקח מ-`settings.json` או מחרוזת ריקה כברירת מחדל.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Description**:
זכויות יוצרים של הפרויקט, נלקח מ-`settings.json` או מחרוזת ריקה כברירת מחדל.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

### `__cofee__`

**Description**:
הודעה על תרומה לקפה למפתח, נלקחת מ-`settings.json` או הודעת ברירת מחדל.

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"