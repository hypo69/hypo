Отлично, давайте превратим этот код в игру с графическим интерфейсом, используя Tkinter. Это добавит визуализацию и сделает игру интерактивной.

**Основные шаги:**

1.  **Создание GUI:** Создание окна Tkinter, стержней, дисков и кнопок для управления игрой.
2.  **Отрисовка:** Отрисовка дисков на стержнях.
3.  **Управление:** Обеспечение возможности выбора диска и перемещения его на другой стержень с учетом правил игры.
4.  **Логика игры:** Реализация логики проверки правильности перемещений и выигрыша.

**Полный код игры с комментариями:**

```python
import tkinter as tk
from tkinter import messagebox

class HanoiGame(tk.Tk):
    def __init__(self, n_disks=3):
        super().__init__()
        self.title("Ханойская Башня")
        self.geometry("600x400")
        self.n_disks = n_disks
        self.towers = [[], [], []]  # Изначальное положение дисков
        self.selected_disk = None   # Выбранный диск для перемещения
        self.create_widgets()
        self.setup_game()

    def create_widgets(self):
        # Canvas для рисования дисков и стержней
        self.canvas = tk.Canvas(self, bg="white", width=580, height=300)
        self.canvas.pack(pady=20)
        # Кнопки для перемещения дисков
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)
        self.create_buttons()

    def create_buttons(self):
      # Создание кнопок для выбора стержня
      for i in range(3):
            button = tk.Button(self.buttons_frame, text=f"Стержень {chr(ord('A') + i)}", command=lambda index=i: self.select_tower(index))
            button.pack(side=tk.LEFT, padx=10)


    def setup_game(self):
        # Инициализация начального положения дисков
        for i in range(self.n_disks, 0, -1):
            self.towers[0].append(i)
        self.draw_towers()

    def draw_towers(self):
        self.canvas.delete("all")  # Очистка canvas
        tower_width = 20
        tower_height = 150
        tower_spacing = 150
        base_height = 10
        y_offset = 50 # отступ сверху
        base_pos = base_height + tower_height + y_offset


        for i in range(3):
            # Рисуем основание
            x = 100 + tower_spacing * i
            self.canvas.create_rectangle(x - 50, base_pos, x + 50, base_pos + base_height, fill="brown")

            # Рисуем стержень
            x = 100 + tower_spacing * i
            self.canvas.create_rectangle(x - tower_width/2, y_offset , x + tower_width/2 , base_pos, fill="black")

            # Рисуем диски на стержне
            for j, disk_size in enumerate(self.towers[i]):
                disk_y = base_pos - (j+1) * 20
                disk_x1 = x - (disk_size * 10)
                disk_x2 = x + (disk_size * 10)
                self.canvas.create_rectangle(disk_x1, disk_y, disk_x2, disk_y + 20, fill="blue")

    def select_tower(self, tower_index):
        if self.selected_disk is None:
             # Если диск не выбран, пытаемся взять верхний диск со стержня
           if self.towers[tower_index]:
                self.selected_disk = (tower_index, self.towers[tower_index][-1])
                self.buttons_frame.winfo_children()[tower_index].config(bg="yellow") # Подсветка выбранного стержня
        else:
            # Если диск выбран, перемещаем его на выбранный стержень
            start_tower, disk_value = self.selected_disk
            if self.is_valid_move(start_tower, tower_index):
                 self.towers[start_tower].pop()
                 self.towers[tower_index].append(disk_value)
                 self.selected_disk = None
                 self.draw_towers()
                 self.check_win()
                 # Возвращаем цвет кнопки к обычному
                 self.buttons_frame.winfo_children()[start_tower].config(bg="SystemButtonFace")
                 self.buttons_frame.winfo_children()[tower_index].config(bg="SystemButtonFace")
            else:
                  messagebox.showinfo("Неверный ход", "Нельзя переместить диск на больший")
                  # Возвращаем цвет кнопки к обычному
                  self.buttons_frame.winfo_children()[start_tower].config(bg="SystemButtonFace")
                  self.selected_disk = None

    def is_valid_move(self, start_tower, end_tower):
        #Проверка правильности хода
        if  not self.towers[end_tower] or self.selected_disk[1] < self.towers[end_tower][-1]:
              return True
        else:
             return False

    def check_win(self):
        # Проверка, выиграна ли игра
        if len(self.towers[1]) == self.n_disks:
            messagebox.showinfo("Победа!", "Вы выиграли!")
            self.destroy()

if __name__ == "__main__":
    game = HanoiGame(3)
    game.mainloop()
```

**Разбор кода:**

1.  **Импорт библиотек:**
    *   `tkinter`: для создания графического интерфейса.
    *   `messagebox`: для отображения диалоговых окон.
2.  **Класс `HanoiGame`:**
    *   `__init__`: Инициализация игры: устанавливает окно, диски, кнопки и начальное положение дисков.
    *   `create_widgets`: Создает виджеты (canvas, кнопки).
    *   `create_buttons`: Создает кнопки выбора стержня.
    *   `setup_game`: Устанавливает начальное положение дисков на первом стержне.
    *   `draw_towers`: Отрисовывает стержни и диски на canvas.
    *   `select_tower`: Обрабатывает выбор стержня, перемещает диск при необходимости.
    *   `is_valid_move`: Проверяет, корректно ли перемещение диска.
    *   `check_win`: Проверяет, выиграна ли игра.
3.  **Логика игры:**
    *   Диски хранятся как числа в списках, представляющих стержни (например, `towers[0]`, `towers[1]`, `towers[2]`).
    *   При выборе стержня проверяется, выбран ли уже диск.
    *   При выборе целевого стержня, проверяется, возможно ли на него переместить диск.
    *   Если ход корректный, то диск перемещается, canvas обновляется, и проверяется выигрыш.

**Как запустить:**

1.  Сохраните код в файл с расширением `.py` (например, `hanoi_game.py`).
2.  Запустите файл через командную строку или IDLE.
3.  Игра откроется в новом окне.

**Как играть:**

1.  Нажмите на кнопку, соответствующую стержню, с которого вы хотите взять диск.
2.  Нажмите на кнопку, соответствующую стержню, на который вы хотите перенести диск.
3.  Повторяйте, пока не перенесете все диски на второй стержень.

**Дополнительные улучшения:**

*   **Подсчет ходов:** Добавьте счетчик ходов и выводите его на экран.
*   **Меню:** Добавьте меню для выбора количества дисков.
*   **Анимация:** Реализуйте анимацию перемещения дисков, чтобы игра выглядела более плавной.
*   **Уровни сложности:** Добавьте уровни сложности, меняя количество дисков.
*   **Улучшение графики:** Используйте другие виджеты Tkinter для более красивого дизайна.

Этот пример представляет собой основу для полноценной игры в Ханойскую башню с GUI. Вы можете дальше ее улучшать и кастомизировать по своему желанию.
