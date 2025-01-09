# LIT QZ

## סקירה כללית

המשחק "LIT QZ" הוא חידון בו המחשב שואל שאלות והשחקן צריך לענות עליהן. בגרסה המקורית של המשחק, השאלות והתשובות מקודדות כנתונים, אך ניתן להפוך את החידון לאינטראקטיבי וניתן להרחבה, ולאפשר הוספה קלה של שאלות ותשובות חדשות. המשחק בודק את הידע של השחקן בכך שהוא מאפשר לעבור סדרת שאלות.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [משתנים גלובליים](#משתנים-גלובליים)
- [לולאת המשחק הראשית](#לולאת-המשחק-הראשית)

## משתנים גלובליים

- `questions`: רשימה של שאלות ותשובות בצורה של טופלים (tuples).
- `questionIndex`: אינדקס השאלה הנוכחית.

## לולאת המשחק הראשית

הקוד מכיל לולאה ראשית אחת (`while`):
-   **תיאור**: הלולאה ממשיכה כל עוד `questionIndex` קטן מאורך הרשימה `questions`.
-   **מהלך הלולאה**:
    1.  השאלות והתשובות מוצגות מהרשימה על פי האינדקס הנוכחי.
    2.  השאלה מוצגת למשתמש.
    3.  התשובה של המשתמש נקלטת.
    4.  התשובה של המשתמש נבדקת כנגד התשובה הנכונה (לא תלוי רישיות).
    5.  מוצגת הודעה אם התשובה נכונה או לא נכונה.
    6.  האינדקס של השאלה גדל ב-1.
-   **סיום המשחק**: בסיום הלולאה (כלומר לאחר שהוצגו כל השאלות) מוצגת הודעת הסיום "THAT'S ALL FOLKS!".

```python
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the chemical symbol for water?", "H2O"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci")
]

questionIndex = 0

while questionIndex < len(questions):
    currentQuestion, correctAnswer = questions[questionIndex]
    print(currentQuestion)
    
    userAnswer = input("Your answer: ")
    
    if userAnswer.lower() == correctAnswer.lower():
        print("RIGHT")
    else:
        print("WRONG")
    
    questionIndex += 1

print("THAT'S ALL FOLKS!")
```