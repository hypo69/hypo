"""
MNOPLY:
=================
Сложность: 5
-----------------
Игра "Монополия" (текстовая версия) - это упрощенная версия классической настольной игры, где игроки по очереди бросают кубик и перемещаются по игровому полю. 
Цель игры - купить как можно больше недвижимости и заставить других игроков платить за посещение вашей собственности. 
Победителем становится игрок, у которого остается больше всего денег.

Правила игры:
1. Игроки по очереди бросают кубик и передвигаются на соответствующее количество позиций.
2. Каждая позиция на поле является либо свободной, либо уже купленной недвижимостью.
3. Если игрок попадает на свободную позицию, он может ее купить за определенную сумму.
4. Если игрок попадает на чужую собственность, он должен заплатить владельцу арендную плату.
5. Игра заканчивается, когда у одного из игроков заканчиваются деньги, и побеждает игрок с наибольшим количеством денег.
-----------------
Алгоритм:
1. Инициализация:
    - Установить количество игроков (2).
    - Установить начальный капитал для каждого игрока.
    - Создать игровое поле (массив) и заполнить его названиями позиций (свойствами) и ценами.
    - Установить массив владельцев недвижимости, изначально все позиции свободны (0).
2. Начало игры:
    - Повторять для каждого игрока по очереди пока кто-то не проиграет:
        2.1. Вывести текущую ситуацию на игровом поле, включая позицию каждого игрока, его деньги и список недвижимости.
        2.2. Запросить у игрока нажатие клавиши (бросок кубика).
        2.3. Сгенерировать случайное число от 1 до 6 (бросок кубика) и переместить игрока на соответствующее количество позиций.
        2.4. Проверить позицию, на которую попал игрок:
        2.4.1 Если позиция принадлежит игроку, ничего не делать.
        2.4.2 Если позиция свободна, спросить игрока, хочет ли он купить ее. Если да, вычесть стоимость из денег игрока и установить его владельцем.
        2.4.3 Если позиция принадлежит другому игроку, вычесть арендную плату из денег текущего игрока и добавить ее владельцу недвижимости.
        2.5. Проверить, не обанкротился ли игрок. Если да, то вывести сообщение о поражении и завершить игру.
3. Конец игры:
    - Вывести сообщение о победе игрока, у которого осталось больше денег.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeGame["<p align='left'>Инициализация игры:<br><code><b>numberOfPlayers = 2</b></code><br><code><b>initialMoney = 1500</b></code><br><code><b>createGameBoard()</b></code><br><code><b>createOwnersArray()</b></code></p>"]
    InitializeGame --> GameLoopStart{"Начало цикла игры: пока есть игроки с деньгами"}
    GameLoopStart -- Да --> PlayerTurnStart{"Начало хода игрока"}
    PlayerTurnStart --> ShowGameState["Вывод текущего состояния игры"]
    ShowGameState --> RollDice["<code><b>diceRoll = random(1, 6)</b></code>"]
     RollDice --> MovePlayer["<code><b>currentPlayerPosition = currentPlayerPosition + diceRoll</b></code>"]
    MovePlayer --> CheckProperty{"Проверка свойства: на какую позицию попал игрок"}
    CheckProperty -- "Собственная" --> PlayerTurnEnd["Конец хода игрока"]
    CheckProperty -- "Свободная" --> AskToBuy["Спросить игрока, купить ли недвижимость"]
    AskToBuy -- Да --> BuyProperty["<code><b>currentPlayerMoney = currentPlayerMoney - propertyCost</b></code><br><code><b>setOwner(currentPlayer, currentPosition)</b></code>"]
        BuyProperty -->PlayerTurnEnd
     AskToBuy -- Нет --> PlayerTurnEnd

    CheckProperty -- "Чужая" --> PayRent["<code><b>currentPlayerMoney = currentPlayerMoney - rentCost</b></code><br><code><b>ownerMoney = ownerMoney + rentCost</b></code>"]
        PayRent --> PlayerTurnEnd
     PlayerTurnEnd --> CheckBankrupt{"Проверка: <code><b>currentPlayerMoney <= 0?</b></code>"}
        CheckBankrupt -- Да --> PlayerLose["Игрок банкрот, конец игры"]
           PlayerLose --> GameEnd["Конец игры"]
            CheckBankrupt -- Нет --> NextPlayer["Переход к следующему игроку"]

            NextPlayer --> GameLoopStart
    GameLoopStart -- Нет --> GameEnd["Конец игры"]
     GameEnd --> ShowWinner["Вывод победителя"]
    ShowWinner --> End["Конец"]
```
**Legenda:**
   Start - Начало программы.
   InitializeGame - Инициализация игры: установка количества игроков, начального капитала, создание игрового поля и массива владельцев.
   GameLoopStart - Начало основного цикла игры, который продолжается, пока есть игроки с деньгами.
   PlayerTurnStart - Начало хода текущего игрока.
   ShowGameState - Вывод текущего состояния игры: позиции игроков, их деньги и владения.
   RollDice - Бросок кубика, генерируется случайное число от 1 до 6.
   MovePlayer - Перемещение текущего игрока на количество позиций, выпавшее на кубике.
   CheckProperty - Проверка, кому принадлежит позиция, на которую попал игрок.
   AskToBuy - Вопрос игроку, хочет ли он купить свободную недвижимость.
   BuyProperty - Покупка недвижимости: вычет стоимости из денег игрока и установка его владельцем.
   PayRent - Уплата арендной платы владельцу недвижимости.
    PlayerTurnEnd - Конец хода текущего игрока
   CheckBankrupt - Проверка, не обанкротился ли игрок (не осталось ли у него денег).
   PlayerLose - Сообщение о поражении игрока, который обанкротился.
   NextPlayer - Переход хода к следующему игроку.
   GameEnd - Конец игры, когда все игроки, кроме одного, обанкротились.
   ShowWinner - Вывод сообщения о победителе.
   End - Конец программы.
"""
import random

# Функция для создания игрового поля
def createGameBoard():
    # Игровое поле (названия свойств)
    return [
        "GO", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax",
        "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue",
        "Just Visiting Jail", "St. Charles Place", "Electric Company", "States Avenue", "Virginia Avenue",
        "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Avenue", "New York Avenue",
        "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue",
        "B&O Railroad", "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens",
        "Go to Jail", "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue",
        "Short Line Railroad", "Chance", "Park Place", "Luxury Tax", "Boardwalk"
    ]

# Функция для создания массива владельцев
def createOwnersArray(numberOfProperties):
    # Массив владельцев (0 - никто не владеет)
    return [0] * numberOfProperties

# Функция для вывода состояния игры
def showGameState(players, gameBoard, owners, playerPositions):
    print("\n--- Состояние игры ---")
    for i, player in enumerate(players):
        print(f"Игрок {i+1}: Деньги = {player['money']}, Позиция = {gameBoard[playerPositions[i]]}")
        properties = [gameBoard[j] for j, owner in enumerate(owners) if owner == i+1]
        print(f"  Собственность: {', '.join(properties) if properties else 'Нет собственности'}")
    print("-----------------------\n")

# Функция для определения стоимости собственности
def getPropertyCost(position):
    # Цены на недвижимость
    propertyCosts = {
        1: 60, 3: 60, 6: 200, 8: 100, 9: 120,
        11: 140, 12: 150, 13: 140, 14: 160, 15: 200,
        16: 180, 18: 200, 19: 220, 21: 220, 23: 240,
        24: 240, 25: 200, 26: 260, 27: 260, 28: 150, 29: 280,
         31: 300, 32: 300, 34: 320, 35: 200, 37: 350, 39:400
    }
    return propertyCosts.get(position, 0)

# Функция для определения арендной платы
def getRentCost(position):
    # Арендная плата за недвижимость
    rentCosts = {
        1: 2, 3: 4, 6: 25, 8: 6, 9: 8,
        11: 10, 12: 10, 13: 10, 14: 12, 15: 25,
        16: 14, 18: 16, 19: 18, 21: 18, 23: 20,
        24: 20, 25: 25, 26: 22, 27: 22, 28: 10, 29: 24,
        31: 26, 32: 26, 34: 28, 35: 25, 37: 35, 39:50
    }
    return rentCosts.get(position, 0)

# Функция для покупки собственности
def buyProperty(player, position, owners, propertyCost):
        player['money'] -= propertyCost
        owners[position] = players.index(player)+1
        print(f"Игрок {players.index(player)+1} купил {gameBoard[position]} за {propertyCost}")

# Функция для оплаты аренды
def payRent(player, position, owners, players, rentCost):
    ownerIndex = owners[position] -1
    owner = players[ownerIndex]
    if(owner != player):
        player['money'] -= rentCost
        owner['money'] += rentCost
        print(f"Игрок {players.index(player)+1} заплатил {rentCost} арендной платы игроку {ownerIndex+1} за {gameBoard[position]}")
    else:
         print(f"Игрок {players.index(player)+1} на своей позиции {gameBoard[position]}")


# Основная логика игры
def playMonopoly():
    numberOfPlayers = 2 # Количество игроков
    initialMoney = 1500 # Начальный капитал у каждого игрока
    gameBoard = createGameBoard() # Создание игрового поля
    numberOfProperties = len(gameBoard)
    owners = createOwnersArray(numberOfProperties) # Массив для хранения владельцев недвижимости
    playerPositions = [0] * numberOfPlayers # Позиция каждого игрока на поле

    # Создание игроков
    players = [
        {"money": initialMoney},
        {"money": initialMoney}
    ]

    currentPlayer = 0 # Текущий игрок

    # Основной игровой цикл
    while True:
        showGameState(players, gameBoard, owners, playerPositions) # Вывод состояния игры
        input(f"Игрок {currentPlayer + 1}, нажмите Enter чтобы бросить кубик...")

        # Бросок кубика
        diceRoll = random.randint(1, 6)
        print(f"Выпало {diceRoll}")

        # Перемещение игрока
        playerPositions[currentPlayer] = (playerPositions[currentPlayer] + diceRoll) % len(gameBoard)
        currentPosition = playerPositions[currentPlayer]
        print(f"Игрок {currentPlayer + 1} переместился на позицию {gameBoard[currentPosition]}")

        # Проверка собственности
        if owners[currentPosition] == 0:
            # Свободная позиция
            propertyCost = getPropertyCost(currentPosition)
            if propertyCost > 0:
                buy = input(f"Хотите купить {gameBoard[currentPosition]} за {propertyCost}? (y/n): ")
                if buy.lower() == 'y':
                    buyProperty(players[currentPlayer], currentPosition, owners, propertyCost)

        elif owners[currentPosition] != (currentPlayer+1):
            # Чужая собственность
            rentCost = getRentCost(currentPosition)
            if rentCost > 0:
                payRent(players[currentPlayer], currentPosition, owners, players, rentCost)


        # Проверка на банкротство
        if players[currentPlayer]['money'] <= 0:
            print(f"Игрок {currentPlayer + 1} обанкротился! Выбывает из игры.")
            players.pop(currentPlayer) # Удаляем обанкротившегося игрока
            playerPositions.pop(currentPlayer) # Удаляем позицию
            # Если остался только один игрок, объявляем победу и заканчиваем игру
            if len(players) == 1:
                print(f"Победил игрок {players[0]}!")
                break
            currentPlayer = currentPlayer % len(players)
        else:
            # Переход к следующему игроку
            currentPlayer = (currentPlayer + 1) % len(players)

# Запуск игры
if __name__ == "__main__":
    playMonopoly()
"""
Пояснения:
1.  **Импорт модуля `random`**:
    -  `import random`: Импортирует модуль `random` для генерации случайных чисел.
2.  **Функция `createGameBoard()`**:
    -   Создает список с названиями позиций игрового поля.
3.  **Функция `createOwnersArray(numberOfProperties)`**:
    -   Создает массив для хранения информации о владельцах недвижимости, где 0 означает, что никто не владеет собственностью.
4.  **Функция `showGameState(players, gameBoard, owners, playerPositions)`**:
    -   Выводит текущее состояние игры, включая деньги каждого игрока, его текущую позицию на поле и его собственность.
5.   **Функция `getPropertyCost(position)`**:
     - Возвращает стоимость покупки для конкретной позиции.
6.  **Функция `getRentCost(position)`**:
    - Возвращает стоимость аренды для конкретной позиции.
7.  **Функция `buyProperty(player, position, owners, propertyCost)`**:
    -   Обрабатывает покупку недвижимости игроком.
    -   Списывает стоимость недвижимости с денег игрока.
    -   Устанавливает текущего игрока владельцем данной недвижимости.
8.  **Функция `payRent(player, position, owners, players, rentCost)`**:
    -   Обрабатывает оплату аренды.
    -   Списывает арендную плату с денег игрока, который попал на чужую собственность.
    -   Добавляет арендную плату к деньгам владельца.
9. **Функция `playMonopoly()`**:
    -   **Инициализация**:
        -   `numberOfPlayers = 2`: Устанавливает количество игроков.
        -   `initialMoney = 1500`: Устанавливает начальный капитал для каждого игрока.
        -   `gameBoard = createGameBoard()`: Создаёт игровое поле.
        -   `numberOfProperties = len(gameBoard)`: Определяет количество позиций на поле.
        -   `owners = createOwnersArray(numberOfProperties)`: Создает массив владельцев недвижимости.
        -   `playerPositions = [0] * numberOfPlayers`: Создает массив, в котором хранятся текущие позиции игроков на игровом поле.
        -  `players`: Создается массив игроков, каждый игрок представлен словарем с начальным капиталом.
         - `currentPlayer = 0`: Устанавливает начального игрока.
    -   **Основной цикл игры**:
        - `while True:`: Бесконечный цикл, который продолжается пока есть игроки с деньгами
        -  `showGameState(players, gameBoard, owners, playerPositions)`: Выводит текущее состояние игры.
        - `input(...)`: Предлагает текущему игроку бросить кубик.
        -  `diceRoll = random.randint(1, 6)`: Генерирует случайное число от 1 до 6, имитируя бросок кубика.
        -   `playerPositions[currentPlayer] = ...`: Вычисляет новую позицию игрока на доске.
        -  **Обработка положения на поле**:
            -  `if owners[currentPosition] == 0`: Проверяет, свободна ли ячейка.
            -   Если ячейка свободна, предлагается купить ее.
            -  `elif owners[currentPosition] != (currentPlayer+1)`: Проверяет, является ли ячейка чужой.
            -    Если ячейка чужая, взимается арендная плата.
        -   **Проверка на банкротство**:
            -   `if players[currentPlayer]['money'] <= 0`: Проверяет, обанкротился ли игрок.
            -  Если игрок обанкротился, он удаляется из игры.
            -  Если остался только один игрок, он объявляется победителем.
        -  **Переход хода**:
            -    `currentPlayer = (currentPlayer + 1) % len(players)`: Передает ход следующему игроку.
10. **Запуск игры:**
    -   `if __name__ == "__main__":`: Проверяет, запущен ли скрипт напрямую, а не импортирован как модуль.
    -  `playMonopoly()`: Вызывает функцию, запускающую игру.
"""
