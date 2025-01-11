# FOOTBL

## Обзор

Этот модуль реализует простую текстовую игру в американский футбол. Игрок пытается продвинуть мяч по полю, выбирая между бегом, пасом и ударом. Цель игры - достичь зачетной зоны (100 ярдов) для победы.

## Содержание

- [Функции](#Функции)

## Функции

### `main`

**Описание**: Основная функция, управляющая логикой игры. Инициализирует начальные переменные, обрабатывает ввод пользователя и определяет окончание игры.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

**Вызывает исключения**:
- Нет вызываемых исключений.

```python
import random

# Initialize player's distance from the start
yardage = 0
# Initialize a variable indicating whether the player has reached the end zone
endZone = False

# Main game loop
while not endZone:
    # Display the player's current distance
    print("Current distance: ", yardage)
    # Ask the player to choose a move
    move = input("Choose a move (R=Run, P=Pass, K=Kick): ").upper()

    # Perform a running move
    if move == 'R':
        # Generate a random distance between 1 and 5
        gain = random.randint(1, 5)
        # Update player's distance
        yardage += gain
    # Perform a passing move
    elif move == 'P':
        # Generate a random distance between 5 and 10
        gain = random.randint(5, 10)
        # Update player's distance
        yardage += gain
    # Perform a kick move
    elif move == 'K':
        # Generate a random distance between 10 and 20
        gain = random.randint(10, 20)
        # Update player's distance
        yardage += gain
    else:
        # Message about invalid input
        print("Invalid move, please choose R, P or K.")
        continue

    # Check if the player has reached the end zone
    if yardage >= 100:
        # Update the game ending variable
        endZone = True

# Display victory message
print("TOUCHDOWN!")

```