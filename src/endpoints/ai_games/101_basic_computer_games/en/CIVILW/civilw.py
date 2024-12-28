"""
CIVILW:
=================
Сложность: 7
-----------------
Игра "Гражданская война" представляет собой симуляцию сражения между двумя армиями: Конфедерацией и Союзом. Игрок управляет Конфедерацией и принимает решения о численности своих войск и типе атак (прямая атака или обходной маневр). Цель игры - победить армию Союза, минимизируя свои потери. Игра учитывает случайные факторы, влияющие на исход сражения, что делает каждое сражение уникальным.

Правила игры:
1.  Игрок управляет армией Конфедерации и должен победить армию Союза.
2.  Игрок вводит количество солдат для атаки.
3.  Игрок выбирает тип атаки: прямая (1) или обходная (2).
4.  В зависимости от выбора игрока и случайных факторов, производится расчет потерь для обеих сторон.
5.  После каждого сражения, игра выводит текущую численность войск обеих сторон.
6.  Игра завершается победой одной из сторон, когда численность войск противника становится равна или меньше 0.
-----------------
Алгоритм:
1. Установить начальную численность армии Союза (UnionForce) равной 1000 и армии Конфедерации (ConfederateForce) равной 800.
2. Начать цикл "пока обе армии имеют численность больше 0":
    2.1. Запросить у игрока количество солдат, которых он хочет отправить в атаку (AttackForce).
        2.1.1. Если AttackForce больше, чем имеющиеся силы Конфедерации (ConfederateForce), то вывести сообщение "Недостаточно сил" и вернуться к началу шага 2.1
    2.2. Запросить у игрока тип атаки: прямая (1) или обходная (2) (AttackType).
    2.3. Вычислить потери Конфедерации (ConfederateLosses) случайным образом, умножив AttackForce на случайное число от 0 до 0.4 (для прямой атаки) или на случайное число от 0 до 0.2 (для обходного маневра).
        2.3.1. Если ConfederateLosses больше, чем AttackForce, ConfederateLosses установить равным AttackForce.
    2.4. Вычислить потери Союза (UnionLosses) случайным образом, умножив AttackForce на случайное число от 0 до 0.3.
        2.4.1. Если AttackType равно 2, то увеличить UnionLosses на случайное число от 0 до 100.
    2.5. Обновить численность армий:
        ConfederateForce = ConfederateForce - ConfederateLosses
        UnionForce = UnionForce - UnionLosses
    2.6. Вывести текущую численность армий обеих сторон.
    2.7. Проверить условие победы:
        2.7.1. Если UnionForce меньше или равен 0, то вывести сообщение "Конфедерация победила!" и закончить игру.
        2.7.2. Если ConfederateForce меньше или равен 0, то вывести сообщение "Союз победил!" и закончить игру.
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeForces["<p align='left'>Инициализация переменных:<br><code><b>unionForce = 1000</b></code><br><code><b>confederateForce = 800</b></code></p>"]
    InitializeForces --> LoopStart{"Начало цикла: пока обе армии > 0"}
    LoopStart -- Да --> InputAttackForce["<p align='left'>Ввод количества атакующих:<br><code><b>attackForce</b></code></p>"]
    InputAttackForce --> CheckForce{"Проверка:<br><code><b>attackForce > confederateForce?</b></code>"}
    CheckForce -- Да --> OutputInsufficient["Вывод сообщения: <b>Недостаточно сил</b>"]
    OutputInsufficient --> InputAttackForce
    CheckForce -- Нет --> InputAttackType["<p align='left'>Ввод типа атаки:<br><b>1 - прямая</b>, <b>2 - обходная</b><br><code><b>attackType</b></code></p>"]
    InputAttackType --> CalculateConfederateLosses["<p align='left'>Расчет потерь Конфедерации:<br><code><b>confederateLosses = attackForce * random(0, 0.4)</b></code><br>(или <code><b>random(0, 0.2)</b></code> для обходной атаки)<br>Если <code><b>confederateLosses > attackForce</b></code>, то <code><b>confederateLosses = attackForce</b></code></p>"]
    CalculateConfederateLosses --> CalculateUnionLosses["<p align='left'>Расчет потерь Союза:<br><code><b>unionLosses = attackForce * random(0, 0.3)</b></code><br>Если <code><b>attackType = 2</b></code>, то <code><b>unionLosses += random(0, 100)</b></code></p>"]
    CalculateUnionLosses --> UpdateForces["<p align='left'>Обновление численности армий:<br><code><b>confederateForce -= confederateLosses</b></code><br><code><b>unionForce -= unionLosses</b></code></p>"]
    UpdateForces --> OutputForces["<p align='left'>Вывод численности армий:<br><code><b>confederateForce</b></code>, <code><b>unionForce</b></code></p>"]
    OutputForces --> CheckUnionWin{"Проверка:<br><code><b>unionForce <= 0?</b></code>"}
    CheckUnionWin -- Да --> OutputConfederateWin["Вывод сообщения: <b>Конфедерация победила!</b>"]
    OutputConfederateWin --> End["Конец"]
    CheckUnionWin -- Нет --> CheckConfederateWin{"Проверка:<br><code><b>confederateForce <= 0?</b></code>"}
     CheckConfederateWin -- Да --> OutputUnionWin["Вывод сообщения: <b>Союз победил!</b>"]
    OutputUnionWin --> End
    CheckConfederateWin -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
    
Legenda:
    Start - Начало программы.
    InitializeForces - Инициализация начальной численности войск Союза (unionForce = 1000) и Конфедерации (confederateForce = 800).
    LoopStart - Начало цикла, который продолжается, пока обе армии имеют численность больше 0.
    InputAttackForce - Запрос у игрока количества солдат для атаки (attackForce).
    CheckForce - Проверка, достаточно ли у Конфедерации сил для атаки (attackForce > confederateForce).
    OutputInsufficient - Вывод сообщения "Недостаточно сил", если атакующих больше, чем имеющихся сил.
    InputAttackType - Запрос у игрока выбора типа атаки: прямая (1) или обходная (2).
    CalculateConfederateLosses - Расчет потерь Конфедерации (confederateLosses) на основе attackForce и типа атаки, с учетом случайного фактора. Если потери превышают attackForce, потери устанавливаются равными attackForce.
    CalculateUnionLosses - Расчет потерь Союза (unionLosses) на основе attackForce и типа атаки, с учетом случайного фактора. При обходной атаке потери Союза дополнительно увеличиваются случайным числом.
    UpdateForces - Обновление численности войск обеих армий после сражения.
    OutputForces - Вывод текущей численности армий Конфедерации и Союза.
    CheckUnionWin - Проверка, победила ли Конфедерация (численность армии Союза <= 0).
    OutputConfederateWin - Вывод сообщения о победе Конфедерации.
    CheckConfederateWin - Проверка, победил ли Союз (численность армии Конфедерации <= 0).
    OutputUnionWin - Вывод сообщения о победе Союза.
    End - Конец программы.
"""
import random

# Начальная численность армий
unionForce = 1000  # Армия Союза
confederateForce = 800  # Армия Конфедерации

# Основной игровой цикл
while unionForce > 0 and confederateForce > 0:
    # Запрос количества солдат для атаки
    while True:
         try:
            attackForce = int(input("Введите количество солдат для атаки (Конфедерация): "))
            if attackForce > confederateForce:
                print("Недостаточно сил! Попробуйте еще раз.")
            else:
                break
         except ValueError:
                print("Пожалуйста, введите целое число.")

    # Запрос типа атаки
    while True:
        try:
             attackType = int(input("Выберите тип атаки (1 - прямая, 2 - обходная): "))
             if attackType in [1, 2]:
                break
             else:
                 print("Неверный тип атаки, попробуйте еще раз")
        except ValueError:
            print("Пожалуйста, введите целое число 1 или 2.")

    # Расчет потерь Конфедерации
    if attackType == 1:  # Прямая атака
        confederateLosses = int(attackForce * random.random() * 0.4)
    else:  # Обходной маневр
        confederateLosses = int(attackForce * random.random() * 0.2)
    
    if confederateLosses > attackForce:
        confederateLosses = attackForce

    # Расчет потерь Союза
    unionLosses = int(attackForce * random.random() * 0.3)
    if attackType == 2:
        unionLosses += random.randint(0, 100)

    # Обновление численности армий
    confederateForce -= confederateLosses
    unionForce -= unionLosses

    # Вывод текущей численности армий
    print(f"Конфедерация: {confederateForce} солдат")
    print(f"Союз: {unionForce} солдат")

    # Проверка условий победы
    if unionForce <= 0:
        print("Конфедерация победила!")
    elif confederateForce <= 0:
        print("Союз победил!")
    
"""
Объяснение кода:
1.  **Импорт модуля `random`**:
    -   `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел при расчете потерь.
2.  **Инициализация численности армий**:
    -   `unionForce = 1000`: Устанавливает начальную численность армии Союза в 1000.
    -   `confederateForce = 800`: Устанавливает начальную численность армии Конфедерации в 800.
3.  **Основной цикл `while unionForce > 0 and confederateForce > 0:`**:
    -   Цикл продолжается, пока обе армии имеют численность больше 0, т.е. пока не будет достигнута победа одной из сторон.
    - **Ввод данных**:
        -   Цикл `while True: try: ... except ValueError:` обеспечивает корректный ввод данных. Если пользователь вводит не число, то программа выведет ошибку и попросит повторить ввод.
        - `attackForce = int(input("Введите количество солдат для атаки (Конфедерация): "))`: Запрашивает у игрока количество солдат для атаки и конвертирует ввод в целое число.
        - Проверка введенного количества солдат
        - `if attackForce > confederateForce: print("Недостаточно сил! Попробуйте еще раз.")`: Проверяет, что количество атакующих солдат не больше численности армии Конфедерации. Если это так, то выводится ошибка и цикл продолжается.
        - `attackType = int(input("Выберите тип атаки (1 - прямая, 2 - обходная): "))`: Запрашивает у игрока тип атаки и конвертирует ввод в целое число.
         - Проверка введенного типа атаки
        - `if attackType in [1, 2]: break`: Проверяет, что тип атаки равен 1 или 2. Если это так, то выход из цикла. Иначе, выводит ошибку и просит повторить ввод.
    -   **Расчет потерь Конфедерации**:
        -   `if attackType == 1: ... else:`:  В зависимости от типа атаки рассчитывается размер потерь.
        -   `confederateLosses = int(attackForce * random.random() * 0.4)`: Для прямой атаки потери Конфедерации - это случайное число от 0 до 40% от атакующей силы.
        -  `confederateLosses = int(attackForce * random.random() * 0.2)`: Для обходного маневра потери Конфедерации - это случайное число от 0 до 20% от атакующей силы.
        -  `if confederateLosses > attackForce: confederateLosses = attackForce`: Гарантирует, что потери не будут больше чем число атакующих
    -   **Расчет потерь Союза**:
        -   `unionLosses = int(attackForce * random.random() * 0.3)`: Потери Союза - это случайное число от 0 до 30% от атакующей силы.
        -   `if attackType == 2: unionLosses += random.randint(0, 100)`: При обходном маневре к потерям Союза добавляется случайное число от 0 до 100.
    -   **Обновление численности армий**:
        -   `confederateForce -= confederateLosses`: Уменьшает численность армии Конфедерации на потери.
        -   `unionForce -= unionLosses`: Уменьшает численность армии Союза на потери.
    -   **Вывод текущей численности армий**:
        -   `print(f"Конфедерация: {confederateForce} солдат")`: Выводит текущую численность армии Конфедерации.
        -   `print(f"Союз: {unionForce} солдат")`: Выводит текущую численность армии Союза.
    -   **Проверка условий победы**:
        -   `if unionForce <= 0: print("Конфедерация победила!")`: Если численность армии Союза стала меньше или равна 0, то Конфедерация объявляется победителем.
        -   `elif confederateForce <= 0: print("Союз победил!")`: Если численность армии Конфедерации стала меньше или равна 0, то Союз объявляется победителем.
"""
