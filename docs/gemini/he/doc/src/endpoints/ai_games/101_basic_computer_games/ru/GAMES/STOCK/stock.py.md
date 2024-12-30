# STOCK

## סקירה כללית

משחק "STOCK" הוא סימולציה כלכלית פשוטה שבה השחקן מנסה להרוויח כסף על ידי קנייה ומכירה של מניות במהלך מספר מסוים של סיבובים (ימים). מחיר המניות משתנה באופן אקראי בכל סיבוב. מטרת המשחק היא למקסם את הרווח עד סוף המשחק.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [פונקציות](#פונקציות)

## פונקציות

### `main`

**Description**: המשחק הראשי של סימולציית המניות. מאפשר למשתמש לקנות ולמכור מניות במחירים משתנים באופן אקראי על פני מספר ימים מוגדר מראש.

**Parameters**:
- אין פרמטרים

**Returns**:
- אין ערך מוחזר.

**Raises**:
- `ValueError`: כאשר קלט המשתמש אינו מספר שלם.
```python
    if action == 'buy':
        try:
            stocksToBuy = int(input("Сколько акций купить? "))
            if money >= stocksToBuy * stockPrice:
                money -= stocksToBuy * stockPrice
                numberOfStocks += stocksToBuy
                print("Покупка совершена")
            else:
                print("Недостаточно денег для покупки.")
        except ValueError as ex:
             print("Некорректный ввод. Пожалуйста, введите целое число.")
    elif action == 'sell':
        try:
             stocksToSell = int(input("Сколько акций продать? "))
             if numberOfStocks >= stocksToSell:
                 money += stocksToSell * stockPrice
                 numberOfStocks -= stocksToSell
                 print("Продажа совершена")
             else:
                 print("Недостаточно акций для продажи.")
        except ValueError as ex:
            print("Некорректный ввод. Пожалуйста, введите целое число.")