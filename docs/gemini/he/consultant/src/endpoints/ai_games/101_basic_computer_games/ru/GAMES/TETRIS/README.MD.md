# Анализ кода модуля `TETRIS`

**Качество кода**
*   **Соответствие требованиям к формату кода (1-10):** 7
    *   **Преимущества:**
        *   Код хорошо структурирован, разделен на классы и функции, что улучшает читаемость.
        *   Используются аннотации типов, что повышает понимание кода.
        *   Есть docstring для классов и функций.
    *   **Недостатки:**
        *   Не все docstring соответствуют формату reStructuredText (RST).
        *   Отсутствует использование `from src.logger.logger import logger` для логирования ошибок.
        *   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        *   Используется `super(Board, self).keyPressEvent(event)` и `super(Board, self).timerEvent(event)` вместо `super().keyPressEvent(event)` и `super().timerEvent(event)`.
        *   Некоторые docstring написаны на русском, некоторые на английском.

**Рекомендации по улучшению**

1.  **Формат документации:**
    *   Переписать все docstring в формате reStructuredText (RST).
    *   Все docstring должны быть на русском языке.
2.  **Логирование:**
    *   Использовать `from src.logger.logger import logger` для логирования ошибок и отладки.
    *   Заменить `try-except` блоки на `logger.error` для обработки ошибок.
3.  **Импорты:**
    *   Добавить необходимые импорты, если они отсутствуют.
4.  **Упрощение кода:**
    *   Заменить `super(Board, self).keyPressEvent(event)` на `super().keyPressEvent(event)`.
    *   Заменить `super(Board, self).timerEvent(event)` на `super().timerEvent(event)`.
5.  **Константы:**
    *   Вынести константы (например, `BoardWidth`, `BoardHeight`) в начало класса `Board` как статические переменные, используя CamelCase.

**Улучшенный код**
```python
"""
Модуль для реализации классической игры Тетрис.
=========================================================================================

Этот модуль содержит классы и методы для создания и управления игрой Тетрис.
Игра включает в себя игровое поле, фигуры (тетрамино) и логику игры.

Пример использования
--------------------

Пример создания и запуска игры:

.. code-block:: python

    if __name__ == '__main__':
        app = QApplication([])
        tetris = Tetris()
        sys.exit(app.exec_())
"""
import sys
import random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor

from src.logger.logger import logger # Импорт модуля логирования

class Tetris(QMainWindow):
    """
    Главное окно приложения Тетрис.

    :ivar tboard: Игровое поле.
    :vartype tboard: Board
    :ivar statusbar: Строка состояния.
    :vartype statusbar: QStatusBar
    """
    def __init__(self) -> None:
        """
        Инициализирует главное окно приложения.
        """
        super().__init__()
        self.initUI() # Инициализация пользовательского интерфейса

    def initUI(self) -> None:
        """
        Инициализирует пользовательский интерфейс:
        создаёт игровое поле, строку состояния и задает основные параметры окна.
        """
        self.tboard = Board(self) # Создание игрового поля
        self.setCentralWidget(self.tboard) # Установка игрового поля в центр окна
        self.statusbar = self.statusBar() # Создание строки состояния
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage) # Соединение сигнала для вывода сообщений в строку состояния
        self.tboard.start() # Запуск игры
        self.resize(180, 380) # Установка размера окна
        self.center() # Центрирование окна
        self.setWindowTitle('Tetris') # Установка заголовка окна
        self.show() # Отображение окна

    def center(self) -> None:
        """
        Центрирует окно приложения на экране.
        """
        screen = QDesktopWidget().screenGeometry() # Получение геометрии экрана
        size = self.geometry() # Получение геометрии окна
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2) # Расчет и установка позиции окна


class Board(QFrame):
    """
    Класс, представляющий игровое поле Тетриса.

    :ivar msg2Statusbar: Сигнал для отправки сообщений в строку состояния.
    :vartype msg2Statusbar: pyqtSignal
    :ivar BoardWidth: Ширина игрового поля.
    :vartype BoardWidth: int
    :ivar BoardHeight: Высота игрового поля.
    :vartype BoardHeight: int
    :ivar Speed: Скорость падения фигур.
    :vartype Speed: int
    :ivar timer: Таймер игры.
    :vartype timer: QBasicTimer
    :ivar isWaitingAfterLine: Флаг ожидания после удаления линии.
    :vartype isWaitingAfterLine: bool
    :ivar curX: Текущая X-координата фигуры.
    :vartype curX: int
    :ivar curY: Текущая Y-координата фигуры.
    :vartype curY: int
    :ivar numLinesRemoved: Количество удаленных линий.
    :vartype numLinesRemoved: int
    :ivar board: Игровое поле.
    :vartype board: list
    :ivar isStarted: Флаг, указывающий, что игра начата.
    :vartype isStarted: bool
    :ivar isPaused: Флаг, указывающий, что игра на паузе.
    :vartype isPaused: bool
    :ivar curPiece: Текущая фигура.
    :vartype curPiece: Shape
    """
    msg2Statusbar = pyqtSignal(str) # Сигнал для отправки сообщений в строку состояния
    BoardWidth = 10 # Ширина игрового поля
    BoardHeight = 22 # Высота игрового поля
    Speed = 300 # Скорость падения фигур

    def __init__(self, parent: QMainWindow) -> None:
        """
        Инициализирует игровое поле.

        :param parent: Родительское окно.
        :type parent: QMainWindow
        """
        super().__init__(parent)
        self.initBoard() # Инициализация игрового поля

    def initBoard(self) -> None:
        """
        Инициализирует доску и игровые переменные.
        """
        self.timer = QBasicTimer() # Создание таймера
        self.isWaitingAfterLine = False # Установка флага ожидания после удаления линии в False
        self.curX = 0 # Инициализация текущей X-координаты
        self.curY = 0 # Инициализация текущей Y-координаты
        self.numLinesRemoved = 0 # Инициализация количества удаленных линий
        self.board = [] # Инициализация игрового поля
        self.setFocusPolicy(Qt.StrongFocus) # Установка политики фокусировки
        self.isStarted = False # Установка флага начала игры в False
        self.isPaused = False # Установка флага паузы в False
        self.clearBoard() # Очистка игрового поля

    def shapeAt(self, x: int, y: int) -> int:
        """
        Возвращает форму фигуры в заданной позиции.

        :param x: Координата x.
        :type x: int
        :param y: Координата y.
        :type y: int
        :return: Форма тетрамино в позиции.
        :rtype: int
        """
        return self.board[(y * Board.BoardWidth) + x] # Получение формы фигуры в заданной позиции

    def setShapeAt(self, x: int, y: int, shape: int) -> None:
        """
        Устанавливает форму фигуры в заданной позиции.

        :param x: Координата x.
        :type x: int
        :param y: Координата y.
        :type y: int
        :param shape: Форма тетрамино.
        :type shape: int
        """
        self.board[(y * Board.BoardWidth) + x] = shape # Установка формы фигуры в заданной позиции

    def squareWidth(self) -> int:
        """
        Возвращает ширину одного квадрата.

        :return: Ширина квадрата.
        :rtype: int
        """
        return self.contentsRect().width() // Board.BoardWidth # Расчет ширины квадрата

    def squareHeight(self) -> int:
        """
        Возвращает высоту одного квадрата.

        :return: Высота квадрата.
        :rtype: int
        """
        return self.contentsRect().height() // Board.BoardHeight # Расчет высоты квадрата

    def start(self) -> None:
        """
        Запускает игру.
        """
        if self.isPaused: # Проверка, если игра на паузе
            return
        self.isStarted = True # Установка флага начала игры в True
        self.isWaitingAfterLine = False # Установка флага ожидания после удаления линии в False
        self.numLinesRemoved = 0 # Сброс счетчика удаленных линий
        self.clearBoard() # Очистка игрового поля
        self.msg2Statusbar.emit(str(self.numLinesRemoved)) # Отправка сообщения с количеством удаленных линий в строку состояния
        self.newPiece() # Создание новой фигуры
        self.timer.start(Board.Speed, self) # Запуск таймера

    def pause(self) -> None:
        """
        Ставит игру на паузу или возобновляет ее.
        """
        if not self.isStarted: # Проверка, что игра начата
            return
        self.isPaused = not self.isPaused # Инвертирование флага паузы
        if self.isPaused: # Проверка, если игра на паузе
            self.timer.stop() # Остановка таймера
            self.msg2Statusbar.emit("paused") # Отправка сообщения "paused" в строку состояния
        else:
            self.timer.start(Board.Speed, self) # Запуск таймера
            self.msg2Statusbar.emit(str(self.numLinesRemoved)) # Отправка количества удаленных линий в строку состояния
        self.update() # Обновление игрового поля

    def paintEvent(self, event: object) -> None:
        """
        Отрисовывает игровое поле и текущую фигуру.

        :param event: Событие отрисовки.
        :type event: object
        """
        painter = QPainter(self) # Создание объекта QPainter
        rect = self.contentsRect() # Получение прямоугольника игрового поля
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight() # Расчет верхней границы игрового поля
        for i in range(Board.BoardHeight): # Цикл по высоте игрового поля
            for j in range(Board.BoardWidth): # Цикл по ширине игрового поля
                shape = self.shapeAt(j, Board.BoardHeight - i - 1) # Получение формы фигуры в текущей позиции
                if shape != Tetrominoe.NoShape: # Проверка, что форма не пустая
                    self.drawSquare(painter, # Отрисовка квадрата
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)
        if self.curPiece.shape() != Tetrominoe.NoShape: # Проверка, что текущая фигура не пустая
            for i in range(4): # Цикл по координатам фигуры
                x = self.curX + self.curPiece.x(i) # Расчет X-координаты
                y = self.curY - self.curPiece.y(i) # Расчет Y-координаты
                self.drawSquare(painter, rect.left() + x * self.squareWidth(), # Отрисовка квадрата
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())

    def keyPressEvent(self, event: object) -> None:
        """
        Обрабатывает нажатия клавиш.

        :param event: Событие нажатия клавиши.
        :type event: object
        """
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape: # Проверка, что игра начата и текущая фигура не пустая
            super().keyPressEvent(event) # Вызов родительского обработчика события
            return
        key = event.key() # Получение кода клавиши
        if key == Qt.Key_P: # Проверка, что нажата клавиша P
            self.pause() # Пауза
            return
        if self.isPaused: # Проверка, что игра на паузе
            return
        elif key == Qt.Key_Left: # Проверка, что нажата клавиша влево
            self.tryMove(self.curPiece, self.curX - 1, self.curY) # Попытка перемещения влево
        elif key == Qt.Key_Right: # Проверка, что нажата клавиша вправо
            self.tryMove(self.curPiece, self.curX + 1, self.curY) # Попытка перемещения вправо
        elif key == Qt.Key_Down: # Проверка, что нажата клавиша вниз
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY) # Попытка поворота вправо
        elif key == Qt.Key_Up: # Проверка, что нажата клавиша вверх
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY) # Попытка поворота влево
        elif key == Qt.Key_Space: # Проверка, что нажата клавиша пробел
            self.dropDown() # Падение вниз
        elif key == Qt.Key_D: # Проверка, что нажата клавиша D
            self.oneLineDown() # Опускание на одну линию
        else:
            super().keyPressEvent(event) # Вызов родительского обработчика события

    def timerEvent(self, event: object) -> None:
        """
        Обрабатывает события таймера.

        :param event: Событие таймера.
        :type event: object
        """
        if event.timerId() == self.timer.timerId(): # Проверка, что событие от таймера
            if self.isWaitingAfterLine: # Проверка, что ожидание после удаления линии
                self.isWaitingAfterLine = False # Сброс флага ожидания после удаления линии
                self.newPiece() # Создание новой фигуры
            else:
                self.oneLineDown() # Опускание фигуры на одну линию
        else:
            super().timerEvent(event) # Вызов родительского обработчика события

    def clearBoard(self) -> None:
        """
        Очищает игровое поле.
        """
        for i in range(Board.BoardHeight * Board.BoardWidth): # Цикл по всем ячейкам игрового поля
            self.board.append(Tetrominoe.NoShape) # Добавление пустой формы в игровое поле

    def dropDown(self) -> None:
        """
        Опускает текущую фигуру до упора.
        """
        newY = self.curY # Получение текущей Y-координаты
        while newY > 0: # Пока фигура не достигла дна
            if not self.tryMove(self.curPiece, self.curX, newY - 1): # Попытка перемещения вниз
                break # Выход из цикла, если перемещение невозможно
            newY -= 1 # Уменьшение Y-координаты
        self.pieceDropped() # Фиксация фигуры на поле

    def oneLineDown(self) -> None:
        """
        Опускает текущую фигуру на одну линию.
        """
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1): # Попытка перемещения фигуры на одну линию вниз
            self.pieceDropped() # Фиксация фигуры на поле

    def pieceDropped(self) -> None:
        """
        Фиксирует упавшую фигуру на поле.
        """
        for i in range(4): # Цикл по всем квадратам фигуры
            x = self.curX + self.curPiece.x(i) # Получение X-координаты
            y = self.curY - self.curPiece.y(i) # Получение Y-координаты
            self.setShapeAt(x, y, self.curPiece.shape()) # Установка формы фигуры в игровом поле
        self.removeFullLines() # Удаление заполненных линий
        if not self.isWaitingAfterLine: # Проверка, что нет ожидания после удаления линии
            self.newPiece() # Создание новой фигуры

    def removeFullLines(self) -> None:
        """
        Удаляет полные линии и обновляет счетчик очков.
        """
        numFullLines = 0 # Инициализация количества полных линий
        rowsToRemove = [] # Список удаляемых линий
        for i in range(Board.BoardHeight): # Цикл по всем строкам игрового поля
            n = 0
            for j in range(Board.BoardWidth): # Цикл по всем столбцам игрового поля
                if not self.shapeAt(j, i) == Tetrominoe.NoShape: # Проверка, что ячейка не пустая
                    n = n + 1
            if n == 10: # Проверка, что строка полная
                rowsToRemove.append(i) # Добавление индекса строки в список удаляемых
        rowsToRemove.reverse() # Переворачивание списка удаляемых линий, для правильного удаления
        for m in rowsToRemove: # Цикл по всем удаляемым строкам
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1)) # Сдвиг строк вниз
        numFullLines = numFullLines + len(rowsToRemove) # Подсчет количества полных линий
        if numFullLines > 0: # Если есть полные линии
            self.numLinesRemoved = self.numLinesRemoved + numFullLines # Увеличение счетчика удаленных линий
            self.msg2Statusbar.emit(str(self.numLinesRemoved)) # Отправка количества удаленных линий в строку состояния
            self.isWaitingAfterLine = True # Установка флага ожидания после удаления линии
            self.curPiece.setShape(Tetrominoe.NoShape) # Установка пустой формы для текущей фигуры
            self.update() # Обновление игрового поля

    def newPiece(self) -> None:
        """
        Генерирует новую фигуру для игры.
        """
        self.curPiece = Shape() # Создание нового объекта фигуры
        self.curPiece.setRandomShape() # Установка случайной формы для фигуры
        self.curX = Board.BoardWidth // 2 + 1 # Установка X-координаты для новой фигуры
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY() # Установка Y-координаты для новой фигуры
        if not self.tryMove(self.curPiece, self.curX, self.curY): # Попытка переместить фигуру на начальную позицию
            self.curPiece.setShape(Tetrominoe.NoShape) # Установка пустой формы для текущей фигуры
            self.timer.stop() # Остановка таймера
            self.isStarted = False # Установка флага начала игры в False
            self.msg2Statusbar.emit("Game over") # Отправка сообщения "Game over" в строку состояния

    def tryMove(self, newPiece: object, newX: int, newY: int) -> bool:
        """
        Пытается переместить фигуру на новые координаты.

        :param newPiece: Новая форма фигуры.
        :type newPiece: Shape
        :param newX: Новая координата X.
        :type newX: int
        :param newY: Новая координата Y.
        :type newY: int
        :return: True, если перемещение успешно, иначе False.
        :rtype: bool
        """
        for i in range(4): # Цикл по всем координатам фигуры
            x = newX + newPiece.x(i) # Расчет X-координаты
            y = newY - newPiece.y(i) # Расчет Y-координаты
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight: # Проверка границ игрового поля
                return False # Возвращение False, если выход за границы
            if self.shapeAt(x, y) != Tetrominoe.NoShape: # Проверка столкновения с другими фигурами
                return False # Возвращение False, если столкновение
        self.curPiece = newPiece # Установка новой фигуры
        self.curX = newX # Установка новой X-координаты
        self.curY = newY # Установка новой Y-координаты
        self.update() # Обновление игрового поля
        return True # Возвращение True, если перемещение успешно

    def drawSquare(self, painter: QPainter, x: int, y: int, shape: int) -> None:
        """
        Рисует квадрат на игровом поле.

        :param painter: Объект QPainter.
        :type painter: QPainter
        :param x: Координата x.
        :type x: int
        :param y: Координата y.
        :type y: int
        :param shape: Форма тетрамино.
        :type shape: int
        """
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC, # Цветовая таблица для фигур
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        color = QColor(colorTable[shape]) # Получение цвета фигуры
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, # Заполнение квадрата цветом
            self.squareHeight() - 2, color)
        painter.setPen(color.lighter()) # Установка более светлого цвета для обводки
        painter.drawLine(x, y + self.squareHeight() - 1, x, y) # Отрисовка верхней линии квадрата
        painter.drawLine(x, y, x + self.squareWidth() - 1, y) # Отрисовка левой линии квадрата
        painter.setPen(color.darker()) # Установка более темного цвета для обводки
        painter.drawLine(x + 1, y + self.squareHeight() - 1, # Отрисовка нижней линии квадрата
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, # Отрисовка правой линии квадрата
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    """
    Перечисление всех возможных форм тетрамино.

    :cvar NoShape: Нет формы.
    :vartype NoShape: int
    :cvar ZShape: Z-образная форма.
    :vartype ZShape: int
    :cvar SShape: S-образная форма.
    :vartype SShape: int
    :cvar LineShape: Прямая форма.
    :vartype LineShape: int
    :cvar TShape: T-образная форма.
    :vartype TShape: int
    :cvar SquareShape: Квадратная форма.
    :vartype SquareShape: int
    :cvar LShape: L-образная форма.
    :vartype LShape: int
    :cvar MirroredLShape: Зеркальная L-образная форма.
    :vartype MirroredLShape: int
    """
    NoShape = 0 # Нет формы
    ZShape = 1 # Z-образная форма
    SShape = 2 # S-образная форма
    LineShape = 3 # Прямая форма
    TShape = 4 # T-образная форма
    SquareShape = 5 # Квадратная форма
    LShape = 6 # L-образная форма
    MirroredLShape = 7 # Зеркальная L-образная форма


class Shape(object):
    """
    Класс, представляющий фигуру тетрамино.

    :ivar coordsTable: Таблица координат для всех форм фигур.
    :vartype coordsTable: tuple
    :ivar coords: Координаты текущей фигуры.
    :vartype coords: list
    :ivar pieceShape: Форма текущей фигуры.
    :vartype pieceShape: int
    """
    coordsTable = ( # Таблица координат для всех фигур
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )
    def __init__(self) -> None:
        """
        Инициализация фигуры тетрамино.
        """
        self.coords = [[0, 0] for i in range(4)] # Инициализация координат
        self.pieceShape = Tetrominoe.NoShape # Инициализация формы фигуры
        self.setShape(Tetrominoe.NoShape) # Установка начальной формы

    def shape(self) -> int:
        """
        Возвращает форму фигуры.

        :return: Форма фигуры.
        :rtype: int
        """
        return self.pieceShape # Возвращение текущей формы фигуры

    def setShape(self, shape: int) -> None:
        """
        Устанавливает форму фигуры.

        :param shape: Форма тетрамино.
        :type shape: int
        """
        table = Shape.coordsTable[shape] # Получение координат для заданной формы
        for i in range(4): # Цикл по всем координатам
            for j in range(2): # Цикл по X и Y
                self.coords[i][j] = table[i][j] # Установка координат
        self.pieceShape = shape # Установка формы фигуры

    def setRandomShape(self) -> None:
        """
        Устанавливает случайную форму фигуры.
        """
        self.setShape(random.randint(1, 7)) # Установка случайной формы фигуры

    def x(self, index: int) -> int:
        """
        Возвращает координату x для заданной точки фигуры.

        :param index: Индекс точки фигуры.
        :type index: int
        :return: Координата x.
        :rtype: int
        """
        return self.coords[index][0] # Возвращение X-координаты

    def y(self, index: int) -> int:
        """
        Возвращает координату y для заданной точки фигуры.

        :param index: Индекс точки фигуры.
        :type index: int
        :return: Координата y.
        :rtype: int
        """
        return self.coords[index][1] # Возвращение Y-координаты

    def setX(self, index: int, x: int) -> None:
        """
        Устанавливает координату x для заданной точки фигуры.

        :param index: Индекс точки фигуры.
        :type index: int
        :param x: Новая координата x.
        :type x: int
        """
        self.coords[index][0] = x # Установка X-координаты

    def setY(self, index: int, y: int) -> None:
        """
        Устанавливает координату y для заданной точки фигуры.

        :param index: Индекс точки фигуры.
        :type index: int
        :param y: Новая координата y.
        :type y: int
        """
        self.coords[index][1] = y # Установка Y-координаты

    def minX(self) -> int:
        """
        Возвращает минимальную координату x для фигуры.

        :return: Минимальная координата x.
        :rtype: int
        """
        m = self.coords[0][0] # Инициализация минимальной X-координаты
        for i in range(4): # Цикл по всем координатам
            m = min(m, self.coords[i][0]) # Поиск минимальной X-координаты
        return m # Возвращение минимальной X-координаты

    def maxX(self) -> int:
        """
        Возвращает максимальную координату x для фигуры.

        :return: Максимальная координата x.
        :rtype: int
        """
        m = self.coords[0][0] # Инициализация максимальной X-координаты
        for i in range(4): # Цикл по всем координатам
            m = max(m, self.coords[i][0]) # Поиск максимальной X-координаты
        return m # Возвращение максимальной X-координаты

    def minY(self) -> int:
        """
        Возвращает минимальную координату y для фигуры.

        :return: Минимальная координата y.
        :rtype: int
        """
        m = self.coords[0][1] # Инициализация минимальной Y-координаты
        for i in range(4): # Цикл по всем координатам
            m = min(m, self.coords[i][1]) # Поиск минимальной Y-координаты
        return m # Возвращение минимальной Y-координаты

    def maxY(self) -> int:
        """
        Возвращает максимальную координату y для фигуры.

        :return: Максимальная координата y.
        :rtype: int
        """
        m = self.coords[0][1] # Инициализация максимальной Y-координаты
        for i in range(4): # Цикл по всем координатам
            m = max(m, self.coords[i][1]) # Поиск максимальной Y-координаты
        return m # Возвращение максимальной Y-координаты

    def rotateLeft(self) -> object:
        """
        Поворачивает фигуру на 90 градусов влево.

        :return: Новая фигура после поворота.
        :rtype: Shape
        """
        if self.pieceShape == Tetrominoe.SquareShape: # Проверка, что фигура квадрат
            return self # Возвращение текущей фигуры, если она квадрат
        result = Shape() # Создание нового объекта фигуры
        result.pieceShape = self.pieceShape # Установка формы для новой фигуры
        for i in range(4): # Цикл по всем координатам
            result.setX(i, self.y(i)) # Поворот X-координаты
            result.setY(i, -self.x(i)) # Поворот Y-координаты
        return result # Возвращение новой фигуры

    def rotateRight(self) -> object:
        """
        Поворачивает фигуру на 90 градусов вправо.

        :return: Новая фигура после поворота.
        :rtype: Shape
        """
        if self.pieceShape == Tetrominoe.SquareShape: # Проверка, что фигура квадрат
            return self # Возвращение текущей фигуры, если она квадрат
        result = Shape() # Создание нового объекта фигуры
        result.pieceShape = self.pieceShape # Установка формы для новой фигуры
        for i in range(4): # Цикл по всем координатам
            result.setX(i, -self.y(i)) # Поворот X-координаты
            result.setY(i, self.x(i)) # Поворот Y-координаты
        return result # Возвращение новой фигуры

if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
```