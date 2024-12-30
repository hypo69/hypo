# קובץ JSON: `banner_.ai.json`

## סקירה כללית

קובץ זה מכיל מבנה נתונים בפורמט JSON המתאר הוראות מערכת. ההוראות מסודרות לפי מפתחות מספריים, כאשר כל מפתח מכיל מחרוזת המייצגת הוראה ספציפית.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [מבנה הנתונים](#מבנה-הנתונים)
   - [`system_instructions`](#system_instructions)

## מבנה הנתונים

### `system_instructions`

**Description**: אובייקט המכיל הוראות מערכת. כל מפתח מספרי (1, 2, 3) מייצג הוראה ספציפית כמחרוזת.

**Format**:

```json
{
    "1": "system_instruction_asterisk",
    "2": "system_instruction_tilde",
    "3": "system_instruction_hash"
}
```

**Details**:

-   `"1"`: הוראה שמייצגת "system_instruction_asterisk".
-   `"2"`: הוראה שמייצגת "system_instruction_tilde".
-   `"3"`: הוראה שמייצגת "system_instruction_hash".

**שימוש**:

המבנה הזה משמש כבסיס להגדרת הוראות מערכת שונות. כל הוראה מיוצגת על ידי מחרוזת, ומספור המפתחות מאפשר ארגון וגישה להוראות.