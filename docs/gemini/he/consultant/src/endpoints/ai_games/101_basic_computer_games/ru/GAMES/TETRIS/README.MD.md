# Анализ кода модуля `TETRIS`

**Качество кода**
- **Соответствие требованиям к формату кода (1-10):** 8
    - **Плюсы:**
        - Код написан на языке Python и хорошо структурирован.
        - Используется библиотека PyQt5 для создания графического интерфейса.
        - Присутствуют классы для представления игры, игрового поля и фигур тетрамино.
        - Код читабельный и содержит docstring для большинства функций и классов.
        -  Большая часть кода документирована в формате RST.
    - **Минусы:**
         - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`, так как нет работы с файлами.
         - Не используется `from src.logger.logger import logger` для записи ошибок, нужно добавить.
        -  В коде есть не все docstring  в формате RST.
        -  Используются стандартные блоки `try-except`.
        - Некоторые комментарии `#` не несут дополнительной информации, а дублируют код.

**Рекомендации по улучшению**

1.  **Импорты:**
    -   Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
2.  **Форматирование документации:**
    -   Полностью перевести все docstring в формат RST.
    -   Улучшить описания параметров и возвращаемых значений в docstring.
    -   Добавить описание модуля в начале файла.
3.  **Обработка ошибок:**
    -   Заменить `try-except` на использование `logger.error` для логирования ошибок.
4.  **Комментарии:**
    -   Сделать комментарии более информативными.
    -   Убрать дублирующие комментарии `#`.
5.  **Стиль кода:**
    -  Для `QMainWindow`, `QFrame` добавить импорт `from PyQt5.QtWidgets import`
    -  Для `Qt`, `QBasicTimer`, `pyqtSignal` добавить импорт `from PyQt5.QtCore import`
    -  Для `QPainter`, `QColor` добавить импорт `from PyQt5.QtGui import`
   
**Улучшенный код**

```python
"""
Модуль для реализации игры Тетрис.
=========================================================================================

Модуль содержит классы для создания игрового окна, игрового поля и управления фигурами тетрамино.
Использует библиотеку PyQt5 для графического интерфейса.

Пример использования:
--------------------

.. code-block:: python

    if __name__ == '__main__':
        app = QApplication([])
        tetris = Tetris()
        sys.exit(app.exec_())
"""
import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication # Импорт необходимых классов из PyQt5 #
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal # Импорт необходимых классов из PyQt5 #
from PyQt5.QtGui import QPainter, QColor # Импорт необходимых классов из PyQt5 #
from src.logger.logger import logger # Импорт модуля логирования #


class Tetris(QMainWindow):
    """
    Главное окно приложения Tetris.
    
    :ivar tboard: Игровое поле.
    :vartype tboard: Board
    :ivar statusbar: Строка состояния.
    :vartype statusbar: QStatusBar
    """
    def __init__(self) -> None:
        """
        Инициализация окна Tetris.
        
        Создает главное окно приложения и инициализирует его.
        """
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        """
         Инициализация пользовательского интерфейса.
         
         Создает и настраивает интерфейс пользователя, включая игровое поле и строку состояния.
        """
        self.tboard = Board(self) # Создание экземпляра игрового поля #
        self.setCentralWidget(self.tboard) # Установка игрового поля в качестве центрального виджета #
        self.statusbar = self.statusBar() # Получение строки состояния #
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage) # Подключение сигнала для отображения сообщений в строке состояния #
        self.tboard.start() # Запуск игры #
        self.resize(180, 380) # Установка размера окна #
        self.center() # Центрирование окна #
        self.setWindowTitle('Tetris') # Установка заголовка окна #
        self.show() # Отображение окна #

    def center(self) -> None:
        """
        Центрирует окно на экране.

        Вычисляет координаты для центрирования окна на экране и перемещает его.
        """
        screen = QDesktopWidget().screenGeometry() # Получение геометрии экрана #
        size = self.geometry() # Получение геометрии окна #
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2) # Перемещение окна в центр экрана #


class Board(QFrame):
    """
    Класс, представляющий игровое поле Tetris.

    :ivar msg2Statusbar: Сигнал для отправки сообщений в строку состояния.
    :vartype msg2Statusbar: pyqtSignal
    :ivar BoardWidth: Ширина игрового поля в клетках.
    :vartype BoardWidth: int
    :ivar BoardHeight: Высота игрового поля в клетках.
    :vartype BoardHeight: int
    :ivar Speed: Скорость падения фигур.
    :vartype Speed: int
    :ivar timer: Таймер для управления падением фигур.
    :vartype timer: QBasicTimer
    :ivar isWaitingAfterLine: Флаг, указывающий на ожидание после удаления линии.
    :vartype isWaitingAfterLine: bool
    :ivar curX: Текущая координата X падающей фигуры.
    :vartype curX: int
    :ivar curY: Текущая координата Y падающей фигуры.
    :vartype curY: int
    :ivar numLinesRemoved: Количество удаленных линий.
    :vartype numLinesRemoved: int
    :ivar board: Массив, представляющий состояние игрового поля.
    :vartype board: list
    :ivar isStarted: Флаг, указывающий, что игра началась.
    :vartype isStarted: bool
    :ivar isPaused: Флаг, указывающий, что игра на паузе.
    :vartype isPaused: bool
    :ivar curPiece: Текущая падающая фигура.
    :vartype curPiece: Shape
    """
    msg2Statusbar = pyqtSignal(str)
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent: QMainWindow) -> None:
        """
        Инициализация игрового поля.
        
        :param parent: Родительское окно.
        :type parent: QMainWindow
        """
        super().__init__(parent)
        self.initBoard()

    def initBoard(self) -> None:
         """
        Инициализирует доску и игровые переменные.
        
        Устанавливает начальные значения для переменных игры, создаёт таймер.
        """
        self.timer = QBasicTimer() # Создание таймера #
        self.isWaitingAfterLine = False # Инициализация флага ожидания после удаления линии #
        self.curX = 0 # Инициализация текущей координаты X фигуры #
        self.curY = 0 # Инициализация текущей координаты Y фигуры #
        self.numLinesRemoved = 0 # Инициализация количества удаленных линий #
        self.board = [] # Инициализация игрового поля #
        self.setFocusPolicy(Qt.StrongFocus) # Установка политики фокуса #
        self.isStarted = False # Инициализация флага начала игры #
        self.isPaused = False # Инициализация флага паузы игры #
        self.clearBoard() # Очистка игрового поля #

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
        return self.board[(y * Board.BoardWidth) + x]

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
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self) -> int:
         """
        Возвращает ширину одного квадрата.
        
        :return: Ширина квадрата.
        :rtype: int
        """
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self) -> int:
        """
        Возвращает высоту одного квадрата.
         
        :return: Высота квадрата.
        :rtype: int
        """
        return self.contentsRect().height() // Board.BoardHeight

    def start(self) -> None:
         """
        Запускает игру.
        
        Устанавливает начальные значения для игры и запускает таймер.
        """
        if self.isPaused: # Проверка, если игра на паузе #
            return
        self.isStarted = True # Установка флага начала игры #
        self.isWaitingAfterLine = False # Сброс флага ожидания после удаления линии #
        self.numLinesRemoved = 0 # Сброс количества удаленных линий #
        self.clearBoard() # Очистка игрового поля #
        self.msg2Statusbar.emit(str(self.numLinesRemoved)) # Отправка сообщения о количестве удаленных линий #
        self.newPiece() # Создание новой фигуры #
        self.timer.start(Board.Speed, self) # Запуск таймера #

    def pause(self) -> None:
         """
        Ставит игру на паузу или возобновляет ее.
        
        Останавливает или запускает таймер и обновляет строку состояния.
        """
        if not self.isStarted: # Проверка, если игра не начата #
            return
        self.isPaused = not self.isPaused # Инвертирование флага паузы #
        if self.isPaused: # Проверка, если игра на паузе #
            self.timer.stop() # Остановка таймера #
            self.msg2Statusbar.emit("paused") # Отправка сообщения о паузе #
        else:
            self.timer.start(Board.Speed, self) # Запуск таймера #
            self.msg2Statusbar.emit(str(self.numLinesRemoved)) # Отправка сообщения о количестве удаленных линий #
        self.update() # Обновление экрана #

    def paintEvent(self, event: object) -> None:
          """
         Отрисовывает игровое поле и текущую фигуру.
         
         :param event: Событие отрисовки.
         :type event: object
         """
        painter = QPainter(self) # Создание объекта для рисования #
        rect = self.contentsRect() # Получение прямоугольника игрового поля #
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight() # Вычисление верхней границы игрового поля #
        for i in range(Board.BoardHeight): # Цикл по строкам игрового поля #
            for j in range(Board.BoardWidth): # Цикл по столбцам игрового поля #
                shape = self.shapeAt(j, Board.BoardHeight - i - 1) # Получение формы фигуры в текущей позиции #
                if shape != Tetrominoe.NoShape: # Проверка, если фигура существует #
                    self.drawSquare(painter, # Рисование квадрата #
                        rect.left() + j * self.squareWidth(), # Координата X квадрата #
                        boardTop + i * self.squareHeight(), shape) # Координата Y квадрата, форма фигуры #
        if self.curPiece.shape() != Tetrominoe.NoShape: # Проверка, если текущая фигура существует #
            for i in range(4): # Цикл по квадратам текущей фигуры #
                x = self.curX + self.curPiece.x(i) # Вычисление координаты X квадрата текущей фигуры #
                y = self.curY - self.curPiece.y(i) # Вычисление координаты Y квадрата текущей фигуры #
                self.drawSquare(painter, rect.left() + x * self.squareWidth(), # Рисование квадрата текущей фигуры #
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(), # Координаты квадрата текущей фигуры, форма фигуры #
                    self.curPiece.shape()) # Форма текущей фигуры #

    def keyPressEvent(self, event: object) -> None:
        """
        Обрабатывает нажатия клавиш.
        
         :param event: Событие нажатия клавиши.
         :type event: object
        """
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape: # Проверка, если игра не начата или текущей фигуры нет #
            super(Board, self).keyPressEvent(event) # Передача события родительскому классу #
            return
        key = event.key() # Получение кода нажатой клавиши #
        if key == Qt.Key_P: # Проверка, если нажата клавиша P #
            self.pause() # Постановка игры на паузу #
            return
        if self.isPaused: # Проверка, если игра на паузе #
            return
        elif key == Qt.Key_Left: # Проверка, если нажата клавиша влево #
            self.tryMove(self.curPiece, self.curX - 1, self.curY) # Попытка перемещения фигуры влево #
        elif key == Qt.Key_Right: # Проверка, если нажата клавиша вправо #
            self.tryMove(self.curPiece, self.curX + 1, self.curY) # Попытка перемещения фигуры вправо #
        elif key == Qt.Key_Down: # Проверка, если нажата клавиша вниз #
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY) # Попытка поворота фигуры вправо #
        elif key == Qt.Key_Up: # Проверка, если нажата клавиша вверх #
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY) # Попытка поворота фигуры влево #
        elif key == Qt.Key_Space: # Проверка, если нажата клавиша пробел #
            self.dropDown() # Опускание фигуры до упора #
        elif key == Qt.Key_D: # Проверка, если нажата клавиша D #
            self.oneLineDown() # Опускание фигуры на одну линию #
        else:
            super(Board, self).keyPressEvent(event) # Передача события родительскому классу #

    def timerEvent(self, event: object) -> None:
          """
         Обрабатывает события таймера.
         
         :param event: Событие таймера.
         :type event: object
        """
        if event.timerId() == self.timer.timerId(): # Проверка, если событие от таймера #
            if self.isWaitingAfterLine: # Проверка, если ожидается после удаления линии #
                self.isWaitingAfterLine = False # Сброс флага ожидания #
                self.newPiece() # Создание новой фигуры #
            else:
                self.oneLineDown() # Опускание фигуры на одну линию #
        else:
            super(Board, self).timerEvent(event) # Передача события родительскому классу #

    def clearBoard(self) -> None:
        """
        Очищает игровое поле.
        
        Заполняет массив игрового поля значениями, указывающими на отсутствие фигур.
        """
        for i in range(Board.BoardHeight * Board.BoardWidth): # Цикл по всем клеткам игрового поля #
            self.board.append(Tetrominoe.NoShape) # Установка значения отсутствия фигуры в текущей клетке #

    def dropDown(self) -> None:
         """
        Опускает текущую фигуру до упора.
        
        Опускает фигуру до тех пор, пока не столкнется с другой фигурой или низом поля.
        """
        newY = self.curY # Сохранение текущей координаты Y #
        while newY > 0: # Цикл до достижения низа поля #
            if not self.tryMove(self.curPiece, self.curX, newY - 1): # Попытка перемещения фигуры на одну линию вниз #
                break # Выход из цикла, если перемещение не удалось #
            newY -= 1 # Уменьшение координаты Y #
        self.pieceDropped() # Фиксация фигуры на поле #

    def oneLineDown(self) -> None:
         """
        Опускает текущую фигуру на одну линию.
        
        Пытается переместить текущую фигуру на одну линию вниз, если это возможно.
        """
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1): # Попытка перемещения фигуры на одну линию вниз #
            self.pieceDropped() # Фиксация фигуры на поле, если перемещение не удалось #

    def pieceDropped(self) -> None:
        """
        Фиксирует упавшую фигуру на поле.
        
        Записывает форму текущей фигуры в массив игрового поля.
        """
        for i in range(4): # Цикл по всем квадратам текущей фигуры #
            x = self.curX + self.curPiece.x(i) # Вычисление координаты X квадрата текущей фигуры #
            y = self.curY - self.curPiece.y(i) # Вычисление координаты Y квадрата текущей фигуры #
            self.setShapeAt(x, y, self.curPiece.shape()) # Установка формы текущей фигуры в текущую позицию #
        self.removeFullLines() # Удаление полных линий #
        if not self.isWaitingAfterLine: # Проверка, если нет ожидания после удаления линии #
            self.newPiece() # Создание новой фигуры #

    def removeFullLines(self) -> None:
        """
        Удаляет полные линии и обновляет счетчик очков.
        
        Проверяет наличие полных линий и удаляет их, обновляя счетчик и статус игры.
        """
        numFullLines = 0 # Инициализация количества полных линий #
        rowsToRemove = [] # Инициализация списка удаляемых строк #
        for i in range(Board.BoardHeight): # Цикл по всем строкам игрового поля #
            n = 0 # Инициализация счетчика заполненных клеток в строке #
            for j in range(Board.BoardWidth): # Цикл по всем клеткам в строке #
                if not self.shapeAt(j, i) == Tetrominoe.NoShape: # Проверка, если клетка не пустая #
                    n = n + 1 # Увеличение счетчика заполненных клеток #
            if n == 10: # Проверка, если строка полная #
                rowsToRemove.append(i) # Добавление номера строки в список удаляемых строк #
        rowsToRemove.reverse() # Инвертирование списка удаляемых строк #
        for m in rowsToRemove: # Цикл по всем удаляемым строкам #
            for k in range(m, Board.BoardHeight): # Цикл по всем строкам после удаляемой #
                for l in range(Board.BoardWidth): # Цикл по всем клеткам в строке #
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1)) # Смещение строк вниз #
        numFullLines = numFullLines + len(rowsToRemove) # Подсчет количества удаленных линий #
        if numFullLines > 0: # Проверка, если были удалены линии #
            self.numLinesRemoved = self.numLinesRemoved + numFullLines # Обновление количества удаленных линий #
            self.msg2Statusbar.emit(str(self.numLinesRemoved)) # Отправка сообщения о количестве удаленных линий #
            self.isWaitingAfterLine = True # Установка флага ожидания после удаления линии #
            self.curPiece.setShape(Tetrominoe.NoShape) # Установка формы текущей фигуры в отсутствие формы #
            self.update() # Обновление экрана #

    def newPiece(self) -> None:
         """
        Генерирует новую фигуру для игры.
        
        Создаёт новую фигуру случайной формы и проверяет возможность её размещения на поле.
        """
        self.curPiece = Shape() # Создание нового объекта фигуры #
        self.curPiece.setRandomShape() # Установка случайной формы фигуры #
        self.curX = Board.BoardWidth // 2 + 1 # Установка начальной координаты X фигуры #
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY() # Установка начальной координаты Y фигуры #
        if not self.tryMove(self.curPiece, self.curX, self.curY): # Проверка возможности перемещения фигуры на начальную позицию #
            self.curPiece.setShape(Tetrominoe.NoShape) # Установка отсутствия формы у текущей фигуры #
            self.timer.stop() # Остановка таймера #
            self.isStarted = False # Установка флага окончания игры #
            self.msg2Statusbar.emit("Game over") # Отправка сообщения о конце игры #

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
        for i in range(4): # Цикл по всем квадратам фигуры #
            x = newX + newPiece.x(i) # Вычисление координаты X квадрата #
            y = newY - newPiece.y(i) # Вычисление координаты Y квадрата #
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight: # Проверка выхода за границы игрового поля #
                return False # Возврат False, если выход за границу #
            if self.shapeAt(x, y) != Tetrominoe.NoShape: # Проверка, если клетка занята другой фигурой #
                return False # Возврат False, если клетка занята #
        self.curPiece = newPiece # Установка новой формы фигуры #
        self.curX = newX # Установка новой координаты X фигуры #
        self.curY = newY # Установка новой координаты Y фигуры #
        self.update() # Обновление экрана #
        return True # Возврат True, если перемещение успешно #

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
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC, # Таблица цветов для фигур #
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        color = QColor(colorTable[shape]) # Выбор цвета для фигуры #
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, # Заполнение квадрата цветом #
            self.squareHeight() - 2, color)
        painter.setPen(color.lighter()) # Установка более светлого цвета для границ квадрата #
        painter.drawLine(x, y + self.squareHeight() - 1, x, y) # Рисование верхней границы квадрата #
        painter.drawLine(x, y, x + self.squareWidth() - 1, y) # Рисование левой границы квадрата #
        painter.setPen(color.darker()) # Установка более темного цвета для границ квадрата #
        painter.drawLine(x + 1, y + self.squareHeight() - 1, # Рисование нижней границы квадрата #
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, # Рисование правой границы квадрата #
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    """
    Перечисление всех возможных фигур тетрамино.
    """
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

class Shape(object):
    """
    Класс, представляющий фигуру тетрамино.
    
    :ivar coordsTable: Таблица координат для фигур.
    :vartype coordsTable: tuple
    :ivar coords: Координаты точек фигуры.
    :vartype coords: list
    :ivar pieceShape: Форма фигуры.
    :vartype pieceShape: int
    """
    coordsTable = (
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
         
         Устанавливает начальные координаты и форму фигуры.
        """
        self.coords = [[0, 0] for i in range(4)] # Создание массива для координат фигуры #
        self.pieceShape = Tetrominoe.NoShape # Инициализация формы фигуры #
        self.setShape(Tetrominoe.NoShape) # Установка формы фигуры #

    def shape(self) -> int:
        """
        Возвращает форму фигуры.
        
        :return: Форма фигуры.
        :rtype: int
        """
        return self.pieceShape

    def setShape(self, shape: int) -> None:
        """
        Устанавливает форму фигуры.
         
        :param shape: Форма тетрамино.
        :type shape: int
        """
        table = Shape.coordsTable[shape] # Получение таблицы координат для заданной формы #
        for i in range(4): # Цикл по всем точкам фигуры #
            for j in range(2): # Цикл по координатам x и y #
                self.coords[i][j] = table[i][j] # Установка координат точки фигуры #
        self.pieceShape = shape # Установка формы фигуры #

    def setRandomShape(self) -> None:
        """
        Устанавливает случайную форму фигуры.
        
        Выбирает случайную форму из доступных и устанавливает её.
        """
        self.setShape(random.randint(1, 7)) # Установка случайной формы фигуры #

    def x(self, index: int) -> int:
         """
        Возвращает координату x для заданной точки фигуры.
        
        :param index: Индекс точки фигуры.
        :type index: int
        :return: Координата x.
        :rtype: int
        """
        return self.coords[index][0] # Возврат координаты X #

    def y(self, index: int) -> int:
         """
        Возвращает координату y для заданной точки фигуры.
        
         :param index: Индекс точки фигуры.
         :type index: int
        :return: Координата y.
        :rtype: int
        """
        return self.coords[index][1] # Возврат координаты Y #

    def setX(self, index: int, x: int) -> None:
          """
         Устанавливает координату x для заданной точки фигуры.
          
        :param index: Индекс точки фигуры.
        :type index: int
        :param x: Новая координата x.
        :type x: int
        """
        self.coords[index][0] = x # Установка координаты X #

    def setY(self, index: int, y: int) -> None:
         """
        Устанавливает координату y для заданной точки фигуры.
         
        :param index: Индекс точки фигуры.
        :type index: int
        :param y: Новая координата y.
        :type y: int
        """
        self.coords[index][1] = y # Установка координаты Y #

    def minX(self) -> int:
        """
         Возвращает минимальную координату x для фигуры.
         
        :return: Минимальная координата x.
        :rtype: int
        """
        m = self.coords[0][0] # Инициализация минимальной координаты X #
        for i in range(4): # Цикл по всем точкам фигуры #
            m = min(m, self.coords[i][0]) # Обновление минимальной координаты X #
        return m # Возврат минимальной координаты X #

    def maxX(self) -> int:
          """
         Возвращает максимальную координату x для фигуры.
         
        :return: Максимальная координата x.
        :rtype: int
        """
        m = self.coords[0][0] # Инициализация максимальной координаты X #
        for i in range(4): # Цикл по всем точкам фигуры #
            m = max(m, self.coords[i][0]) # Обновление максимальной координаты X #
        return m # Возврат максимальной координаты X #

    def minY(self) -> int:
         """
         Возвращает минимальную координату y для фигуры.
         
        :return: Минимальная координата y.
        :rtype: int
        """
        m = self.coords[0][1] # Инициализация минимальной координаты Y #
        for i in range(4): # Цикл по всем точкам фигуры #
            m = min(m, self.coords[i][1]) # Обновление минимальной координаты Y #
        return m # Возврат минимальной координаты Y #

    def maxY(self) -> int:
        """
        Возвращает максимальную координату y для фигуры.
        
        :return: Максимальная координата y.
        :rtype: int
        """
        m = self.coords[0][1] # Инициализация максимальной координаты Y #
        for i in range(4): # Цикл по всем точкам фигуры #
            m = max(m, self.coords[i][1]) # Обновление максимальной координаты Y #
        return m # Возврат максимальной координаты Y #

    def rotateLeft(self) -> object:
         """
        Поворачивает фигуру на 90 градусов влево.
        
        :return: Новая фигура после поворота.
        :rtype: Shape
        """
        if self.pieceShape == Tetrominoe.SquareShape: # Проверка, если форма фигуры - квадрат #
            return self # Возврат текущей фигуры, если форма - квадрат #
        result = Shape() # Создание нового объекта Shape #
        result.pieceShape = self.pieceShape # Установка формы новой фигуры #
        for i in range(4): # Цикл по всем точкам фигуры #
            result.setX(i, self.y(i)) # Установка новой координаты X #
            result.setY(i, -self.x(i)) # Установка новой координаты Y #
        return result # Возврат повернутой фигуры #

    def rotateRight(self) -> object:
        """
        Поворачивает фигуру на 90 градусов вправо.
        
        :return: Новая фигура после поворота.
        :rtype: Shape
        """
        if self.pieceShape == Tetrominoe.SquareShape: # Проверка, если форма фигуры - квадрат #
            return self # Возврат текущей фигуры, если форма - квадрат #
        result = Shape() # Создание нового объекта Shape #
        result.pieceShape = self.pieceShape # Установка формы новой фигуры #
        for i in range(4): # Цикл по всем точкам фигуры #
            result.setX(i, -self.y(i)) # Установка новой координаты X #
            result.setY(i, self.x(i)) # Установка новой координаты Y #
        return result # Возврат повернутой фигуры #

if __name__ == '__main__':
    app = QApplication([]) # Создание экземпляра приложения QApplication #
    tetris = Tetris() # Создание экземпляра игры Tetris #
    sys.exit(app.exec_()) # Запуск цикла обработки событий приложения #
```