# Алгоритмы сортировки

## סקירה כללית

בחיים היומיומיים ובפיתוח תוכנה, לעיתים קרובות אנחנו נדרשים למיין נתונים.
זה יכול להיות כל דבר: רשימת קניות, ספרים על מדף או תוצאות חיפוש.
אלגוריתמי מיון הם אוסף של הוראות המסייעות לנו לסדר פריטים בסדר מסוים, בין אם זה בסדר עולה, יורד או לפי קריטריון אחר כלשהו.

לצורך הדוגמה, אני משתמש בפירות בגדלים שונים.

**ייצוג של פירות עם גדלים:**

בואו נקשר פירות לגדלים. נשתמש בטופלים (tuple), כאשר:

*   האלמנט הראשון הוא גודל הפרי:
    *   🍎 (קטן) - תפוח
    *   🍐 (בינוני) - אגס
    *   🍉 (גדול) - אבטיח
    *   🧺 (גדול מאוד) - סל
*   האלמנט השני הוא מזהה ייחודי, לשימוש בתוכנית.

דוגמה: `(🍎, 1)` - זה תפוח קטן עם מזהה 1.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
  - [`compare_fruits`](#compare_fruits)
  - [`bubble_sort`](#bubble_sort)
  - [`insertion_sort`](#insertion_sort)
  - [`selection_sort`](#selection_sort)
  - [`display_fruits`](#display_fruits)
- [הסבר קוד](#הסבר-קוד)

## פונקציות

### `compare_fruits`

**תיאור**: משווה שני פירות לפי גודל.

**פרמטרים**:
- `fruit1` (tuple): טופל (גודל, מזהה).
- `fruit2` (tuple): טופל (גודל, מזהה).

**החזרות**:
- `int`: -1 אם `fruit1` קטן מ-`fruit2`, 1 אם `fruit1` גדול מ-`fruit2`, 0 אם שווים.

```python
def compare_fruits(fruit1: Tuple[str, int], fruit2: Tuple[str, int]) -> int:
    """
    Сравнивает два фрукта по размеру.

    Args:
        fruit1: Кортеж (размер, идентификатор).
        fruit2: Кортеж (размер, идентификатор).

    Returns:
        -1, если fruit1 меньше fruit2, 1, если fruit1 больше fruit2, 0, если равны.
    """
    order = {"🍎": 0, "🍐": 1, "🍉": 2, "🧺": 3}  # Определяю порядок фруктов по размеру
    size1 = order.get(fruit1[0]) # Получаю размер первого фрукта
    size2 = order.get(fruit2[0]) # Получаю размер второго фрукта
    if size1 < size2: # Если размер первого фрукта меньше, возвращаю -1
        return -1
    elif size1 > size2: # Если размер первого фрукта больше, возвращаю 1
        return 1
    else: # Если размеры равны, возвращаю 0
      return 0
```

### `bubble_sort`

**תיאור**: ממיין רשימת פירות לפי גודל באמצעות אלגוריתם "מיון בועות".

**פרמטרים**:
- `fruits` (List[tuple]): רשימה של טופלים (גודל, מזהה).

**החזרות**:
- `List[tuple]`: רשימה ממוינת של טופלים.

```python
def bubble_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Сортирует список фруктов по размеру, используя алгоритм "пузырьковая сортировка".

    Args:
        fruits: Список кортежей (размер, идентификатор).

    Returns:
        Отсортированный список кортежей.
    """
    n = len(fruits)  # Получаю количество фруктов
    for i in range(n):  # Прохожу по списку n раз
        for j in range(0, n - i - 1):  # Прохожу по неотсортированной части списка
            if compare_fruits(fruits[j], fruits[j + 1]) == 1:  # Если фрукт слева больше, чем фрукт справа
                fruits[j], fruits[j + 1] = fruits[j + 1], fruits[j]  # Меняю местами
    return fruits
```

### `insertion_sort`

**תיאור**: ממיין רשימת פירות לפי גודל באמצעות אלגוריתם "מיון הכנסה".

**פרמטרים**:
- `fruits` (List[tuple]): רשימה של טופלים (גודל, מזהה).

**החזרות**:
- `List[tuple]`: רשימה ממוינת של טופלים.

```python
def insertion_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Сортирует список фруктов по размеру, используя алгоритм "сортировка вставками".

    Args:
        fruits: Список кортежей (размер, идентификатор).

    Returns:
        Отсортированный список кортежей.
    """
    for i in range(1, len(fruits)): # Начинаю со второго фрукта (первый считается отсортированным)
        key = fruits[i] # Беру следующий фрукт
        j = i - 1 # Индекс предыдущего фрукта
        while j >= 0 and compare_fruits(fruits[j], key) == 1: # Ищу позицию в отсортированной части, куда вставить фрукт
            fruits[j + 1] = fruits[j] # Сдвигаю фрукты, что бы освободить место для нового
            j -= 1
        fruits[j + 1] = key # Вставляю фрукт на нужное место
    return fruits
```

### `selection_sort`

**תיאור**: ממיין רשימת פירות לפי גודל באמצעות אלגוריתם "מיון בחירה".

**פרמטרים**:
- `fruits` (List[tuple]): רשימה של טופלים (גודל, מזהה).

**החזרות**:
- `List[tuple]`: רשימה ממוינת של טופלים.

```python
def selection_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Сортирует список фруктов по размеру, используя алгоритм "сортировка выбором".

    Args:
        fruits: Список кортежей (размер, идентификатор).

    Returns:
        Отсортированный список кортежей.
    """
    n = len(fruits) # Получаю количество фруктов в списке
    for i in range(n): # Прохожу по всем фруктам в списке
        min_index = i # Индекс самого маленького фрукта
        for j in range(i + 1, n): # Ищу самый маленький фрукт в неотсортированной части
            if compare_fruits(fruits[j], fruits[min_index]) == -1: # Если нашел фрукт меньше текущего минимума
                min_index = j # Запоминаю индекс нового минимума
        fruits[i], fruits[min_index] = fruits[min_index], fruits[i] # Меняю текущий фрукт с самым маленьким из неотсортированной части
    return fruits
```

### `display_fruits`

**תיאור**: ממיר רשימת פירות למחרוזת לצורך תצוגה.

**פרמטרים**:
- `fruits` (List[tuple]): רשימה של טופלים (גודל, מזהה).

**החזרות**:
- `str`: מחרוזת להצגת רשימת הפירות.

```python
def display_fruits(fruits: List[Tuple[str, int]]) -> str:
    """
    Преобразует список фруктов в строку для отображения.

    Args:
        fruits: Список кортежей (размер, идентификатор).

    Returns:
        Строка для отображения списка фруктов.
    """
    return ", ".join(f"{fruit[0]}{fruit[1]}" for fruit in fruits)  # Собираю строку для вывода
```

## הסבר קוד

1.  **`compare_fruits(fruit1, fruit2)`:** פונקציה זו משווה שני פירות לפי גודל ומחזירה -1 אם הפרי הראשון קטן יותר, 1 אם גדול יותר ו-0 אם הם שווים. אני משתמש במילון `order` כדי לקבוע את סדר גדלי הפירות.
2.  **`bubble_sort(fruits)`:** אני מיישם את אלגוריתם מיון בועות, בו פירות סמוכים מושווים ומוחלפים אם הם בסדר שגוי.
3.  **`insertion_sort(fruits)`:** אני מיישם את אלגוריתם מיון הכנסה, בו כל פרי חדש מוכנס למקום הנכון בחלק שכבר ממוין של הרשימה.
4.  **`selection_sort(fruits)`:** אני מיישם את אלגוריתם מיון הבחירה, בו בכל מעבר אני מוצא את הפרי הקטן ביותר ומציב אותו במקום הנכון.
5.  **`display_fruits(fruits)`:** פונקציה זו ממירה רשימת פירות למחרוזת להצגה נוחה.
6.  **דוגמאות:** בסוף אני יוצר רשימת פירות ומיישם עליה את שלושת אלגוריתמי המיון, ומציג את התוצאות של כל אחד מהם. אני גם מראה לך את הסדר שבו הפירות ממוינים.