"""
BAGELS:
=================
Сложность: 4
-----------------
Игра "Баранки" - это логическая игра-угадайка, в которой игрок должен угадать секретное трехзначное число, сгенерированное компьютером. Компьютер сообщает игроку подсказки после каждой попытки угадать, используя слова "Pico" (одна цифра правильная, но не на своем месте), "Fermi" (одна цифра правильная и на своем месте) и "Bagels" (ни одна из цифр не правильная).

Правила игры: 
1. Компьютер генерирует случайное трехзначное число, где все цифры уникальны.
2. Игрок вводит свое предположение - трехзначное число.
3. Компьютер сравнивает введенное число с загаданным и дает подсказку:
   - "Fermi" - если цифра угадана и находится на своей позиции.
   - "Pico" - если цифра угадана, но находится на другой позиции.
   - "Bagels" - если ни одна цифра не угадана.
4. Игрок продолжает делать попытки, пока не угадает число или не закончится количество попыток.

-----------------
Алгоритм:
1. Инициализировать переменные:
   - `max_guesses` = 10 (максимальное количество попыток)
   - `secret_number` = случайное 3-значное число с уникальными цифрами
   - `number_of_guesses` = 0 (счетчик попыток)
2. Запустить цикл пока `number_of_guesses` меньше `max_guesses`:
    - увеличить счетчик `number_of_guesses` на 1
    - запросить ввод `guess_number` у игрока
    - Если `guess_number` == `secret_number`:
        - Вывести "You got it!" и выйти из цикла
    - Иначе:
       - Инициализировать пустую строку `feedback`
       - Пройти по каждой цифре в `guess_number` :
         - Если цифра на этой позиции совпадает с `secret_number`:
           - Добавить "Fermi" к `feedback`
         - Иначе, если цифра есть в `secret_number` но не на своей позиции:
           - Добавить "Pico" к `feedback`
       - Если `feedback` пуст:
          - Добавить "Bagels" к `feedback`
       - Вывести `feedback`
3. Если цикл закончился, а `secret_number` не угадан:
    - Вывести сообщение о проигрыше
    - Вывести `secret_number`
-----------------
Блок-схема: 
```mermaid
  graph TD
      Start --> Initialize;
      Initialize --> LoopCondition;
      LoopCondition -- Yes --> IncrementGuess;
      IncrementGuess --> InputGuess;
      InputGuess --> CheckWin;
      CheckWin -- Yes --> Win;
      CheckWin -- No --> StartFeedback;
      StartFeedback --> InitializeFeedback;
      InitializeFeedback --> LoopDigits;
      LoopDigits -- Yes --> CheckFermi;
      CheckFermi -- Yes --> AddFermi;
      AddFermi --> NextDigit;
      CheckFermi -- No --> CheckPico;
      CheckPico -- Yes --> AddPico;
      AddPico --> NextDigit;
      CheckPico -- No --> NextDigit;
      NextDigit --> LoopDigits;
      LoopDigits -- No --> CheckFeedback;
      CheckFeedback -- Yes --> OutputBagels;
      CheckFeedback -- No --> OutputFeedback;
      OutputFeedback --> LoopCondition;
      OutputBagels --> LoopCondition;
      LoopCondition -- No --> GameOver;
      Win --> End;
      GameOver --> OutputSecretNumber;
      OutputSecretNumber --> End;
      
      subgraph Initialize
          Initialize[max_guesses = 10, secret_number = Random, number_of_guesses = 0]
      end
      subgraph InputGuess
          InputGuess[input guess_number]
      end
     subgraph StartFeedback
          StartFeedback[feedback=""]
      end
     subgraph InitializeFeedback
      InitializeFeedback[Initialize feedback]
      end
    subgraph LoopDigits
      LoopDigits[ for each digit in guess_number]
    end
    subgraph CheckFermi
      CheckFermi{Is digit correct and in correct position?}
    end
     subgraph CheckPico
        CheckPico{Is digit correct but in wrong position?}
    end
    subgraph AddFermi
        AddFermi[feedback += "Fermi"]
    end
    subgraph AddPico
        AddPico[feedback += "Pico"]
    end
    subgraph NextDigit
         NextDigit[next digit]
    end
    subgraph CheckFeedback
      CheckFeedback{Is feedback empty?}
    end
    subgraph OutputBagels
      OutputBagels[feedback = "Bagels"]
    end
    subgraph OutputFeedback
         OutputFeedback[Output feedback]
    end
   subgraph LoopCondition
      LoopCondition{number_of_guesses < max_guesses?}
    end
    subgraph IncrementGuess
        IncrementGuess[number_of_guesses += 1]
    end
     subgraph CheckWin
         CheckWin{guess_number == secret_number?}
    end
    subgraph Win
         Win[Output "You got it!"]
    end
    subgraph GameOver
         GameOver[Output "You lost!"]
     end
     subgraph OutputSecretNumber
         OutputSecretNumber[Output secret_number]
    end
    subgraph End
         End[End]
    end
```
"""
import random

def generate_secret_number():
    """Генерирует случайное трехзначное число с уникальными цифрами."""
    digits = list(range(10))  # Создаем список цифр от 0 до 9
    random.shuffle(digits)  # Перемешиваем цифры
    while digits[0] == 0:
      random.shuffle(digits) # убеждаемся, что первая цифра не 0
    return str(digits[0]) + str(digits[1]) + str(digits[2])  # Возвращаем число в виде строки


def get_feedback(guess_number, secret_number):
    """
    Сравнивает guess_number с secret_number и возвращает подсказку
    (Fermi, Pico, Bagels).
    """
    feedback = ""  # Инициализируем пустую строку для подсказки
    # Проходим по каждой цифре в guess_number
    for i in range(len(guess_number)):
        if guess_number[i] == secret_number[i]:
            feedback += "Fermi " # Если цифра и позиция совпадают, добавляем "Fermi"
        elif guess_number[i] in secret_number:
            feedback += "Pico "  # Если цифра есть в числе, но не на своем месте, добавляем "Pico"
    if not feedback:
        feedback = "Bagels" # Если ни одна цифра не угадана, добавляем "Bagels"
    return feedback.strip()  # Возвращаем строку с подсказкой, убирая пробелы в конце


def play_bagels():
    """Запускает игру 'Баранки'."""
    max_guesses = 10  # Максимальное количество попыток
    secret_number = generate_secret_number()  # Генерируем секретное число
    number_of_guesses = 0  # Счетчик попыток
    print("Я загадал трехзначное число с уникальными цифрами.")
    print("Попробуй угадать его. У тебя есть 10 попыток.")
    
    while number_of_guesses < max_guesses:  # Цикл продолжается, пока есть попытки
        number_of_guesses += 1  # Увеличиваем счетчик попыток
        guess_number = input(f"Попытка #{number_of_guesses}: ") # Запрашиваем ввод числа от игрока
         
        if guess_number == secret_number: # Проверяем, угадал ли игрок число
            print("Вы угадали!")  # Если угадал, выводим сообщение и выходим из цикла
            return
        
        feedback = get_feedback(guess_number, secret_number) # Получаем подсказку от компьютера
        print(feedback) # Выводим подсказку игроку

    print(f"Вы проиграли. Секретное число было {secret_number}") # Если попытки закончились, сообщаем о проигрыше и выводим загаданное число


if __name__ == "__main__":
    play_bagels()
"""
Пояснения:
1. **`generate_secret_number()`**:
   - Эта функция создает случайное трехзначное число, где все цифры уникальны.
   - Сначала создается список цифр от 0 до 9.
   - Затем список перемешивается, чтобы получить случайную последовательность.
   - Далее происходит проверка, что первая цифра не равна нулю
   - После этого первые три цифры из перемешанного списка преобразуются в строку и возвращаются.

2.  **`get_feedback(guess_number, secret_number)`**:
   - Эта функция сравнивает введенное пользователем число (`guess_number`) с секретным числом (`secret_number`) и формирует подсказку.
   - Инициализируется пустая строка `feedback` для хранения подсказок.
   - Цикл `for i in range(len(guess_number))` перебирает каждую цифру введенного числа.
   - Если цифра на текущей позиции в `guess_number` совпадает с цифрой на той же позиции в `secret_number`, то в `feedback` добавляется "Fermi ".
   - Если цифра из `guess_number` присутствует в `secret_number`, но не на той же позиции, то в `feedback` добавляется "Pico ".
   - Если после проверки всех цифр `feedback` остается пустой, это означает, что ни одна цифра не угадана, и в `feedback` записывается "Bagels".
   - В конце функция возвращает строку с подсказкой, убрав лишние пробелы с помощью `.strip()`.

3.  **`play_bagels()`**:
   - Эта функция запускает игру "Баранки".
   - Определяются начальные значения:
      - `max_guesses` равно 10 (максимальное количество попыток).
      - `secret_number` генерируется с помощью `generate_secret_number()`.
      - `number_of_guesses` устанавливается в 0 для отслеживания количества сделанных попыток.
   - Далее выводится приветственное сообщение, объясняющее правила игры.
   - Цикл `while number_of_guesses < max_guesses:` позволяет игроку делать попытки, пока не будет исчерпано их максимальное количество.
   - В начале каждой итерации цикла количество попыток (`number_of_guesses`) увеличивается на 1.
   - Затем у пользователя запрашивается ввод трехзначного числа (`guess_number`).
   - Если введенное число равно `secret_number`, выводится сообщение об успехе, и функция завершается.
   - Если же числа не совпадают, функция вызывает `get_feedback` для получения подсказки.
   - Полученная подсказка выводится на экран, и цикл продолжается.
   - Если цикл завершается (все попытки исчерпаны), выводится сообщение о проигрыше и раскрывается загаданное число.

4.  **`if __name__ == "__main__":`**
   - Это стандартная конструкция в Python, которая гарантирует, что функция `play_bagels()` будет вызвана только тогда, когда файл запускается напрямую, а не когда он импортируется как модуль.

licence:MIT(../licence)
"""
__author__ = 'hypo69 (hypo69@davidka.net)'
```