# Документация по игре Acey Ducey

## Обзор

Данный файл представляет собой документацию для разработчиков, описывающую логику игры Acey Ducey. Игра реализована в виде блок-схемы, описывающей последовательность шагов игрового процесса.

## Оглавление

- [Обзор](#обзор)
- [Блок-схема игры](#блок-схема-игры)
    - [Начало игры](#начало-игры)
    - [Инициализация](#инициализация)
    - [Игровой цикл](#игровой-цикл)
    - [Проверка баланса](#проверка-баланса)
    - [Отображение баланса](#отображение-баланса)
    - [Раздача карт](#раздача-карт)
    - [Проверка одинаковых карт](#проверка-одинаковых-карт)
    - [Пересдача карт](#пересдача-карт)
    - [Отображение карт](#отображение-карт)
    - [Совершение ставки](#совершение-ставки)
    - [Проверка ставки](#проверка-ставки)
    - [Вытягивание следующей карты](#вытягивание-следующей-карты)
    - [Проверка результата](#проверка-результата)
    - [Победа](#победа)
    - [Поражение](#поражение)
    - [Обновление баланса при победе](#обновление-баланса-при-победе)
    - [Обновление баланса при поражении](#обновление-баланса-при-поражении)
    - [Конец игры](#конец-игры)
    - [Отображение финального баланса](#отображение-финального-баланса)
    - [Конец](#конец)

## Блок-схема игры

### Начало игры

- **Описание**: Начало игры. Игрок запускает игру Acey Ducey.

### Инициализация

- **Описание**: Инициализация начальных параметров игры, таких как создание колоды карт и установка начального баланса игрока в $100.

### Игровой цикл

- **Описание**: Основной цикл игры, повторяющийся до тех пор, пока у игрока есть деньги и достаточно карт в колоде.

### Проверка баланса

- **Описание**: Проверка, достаточно ли у игрока баланса и карт в колоде (минимум 3) для продолжения игры.
    
### Отображение баланса

- **Описание**: Отображает текущий баланс игрока.

### Раздача карт

- **Описание**: Раздача двух карт из колоды.

### Проверка одинаковых карт

- **Описание**: Проверка, являются ли выданные карты одинаковыми. Если карты одинаковы, требуется пересдача.

### Пересдача карт

- **Описание**: Если карты одинаковы, колода перетасовывается и вытягиваются две новые карты.

### Отображение карт

- **Описание**: Отображение двух выданных карт игроку.

### Совершение ставки

- **Описание**: Игрок делает ставку на то, что следующая карта будет между двумя выданными.

### Проверка ставки

- **Описание**: Проверка, является ли ставка корректной (не отрицательной и не больше текущего баланса). Если нет, игрок делает ставку снова.

### Вытягивание следующей карты

- **Описание**: Вытягивание следующей карты из колоды.

### Проверка результата

- **Описание**: Проверка, находится ли вытянутая карта между двумя картами, или равна одной из них, или является тузом.

### Победа

- **Описание**: Игрок выигрывает, если третья карта находится между двумя первыми картами.

### Поражение

- **Описание**: Игрок проигрывает, если третья карта равна одной из первых двух карт или является тузом.

### Обновление баланса при победе

- **Описание**: Баланс игрока увеличивается на размер ставки.

### Обновление баланса при поражении

- **Описание**: Баланс игрока уменьшается на размер ставки.

### Конец игры

- **Описание**: Игра заканчивается, если у игрока заканчиваются деньги или недостаточно карт в колоде.

### Отображение финального баланса

- **Описание**: Отображается итоговый баланс игрока.

### Конец

- **Описание**: Конец игры. Завершение игровой сессии.