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