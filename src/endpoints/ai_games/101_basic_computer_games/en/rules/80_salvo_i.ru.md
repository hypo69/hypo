### Название игры: **SALVO I** (Артиллерийская битва)

---

#### Описание  
**SALVO I** — это игра, в которой игрок и компьютер сражаются на двух игровых полях размером 5x5. Каждый игрок имеет четыре взвода, которые могут быть размещены на любом из 25 выходов (от 1 до 25). Цель игры — первым уничтожить все четыре взвода противника, выбирая выходы для обстрела.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - Программа выводит приветственное сообщение и объясняет правила:  
     ```
     Вы находитесь на поле боя с 4 взводами.  
     У вас есть 25 выходов, где можно разместить взводы.  
     Вы можете разместить только один взвод на каждом выходе.  
     Компьютер делает то же самое со своими четырьмя взводами.  
     Цель игры — обстреливать выходы противника, пытаясь уничтожить все его взводы.  
     Побеждает тот, кто первым уничтожит все четыре взвода противника.  
     Удачи!  
     ```

   - Программа создаёт два игровых поля размером 5x5 для игрока и компьютера.  
   - Игрок и компьютер размещают свои взводы на своих полях.  
   - Игроки поочерёдно выбирают выходы для обстрела.

---

#### 2. **Основной процесс игры**

##### **2.1. Размещение взводов:**
   - Игрок выбирает четыре выхода (от 1 до 25), где будут размещены его взводы.  
   - Компьютер случайным образом выбирает четыре выхода для своих взводов.  
   - Программа проверяет, что выходы игрока и компьютера не пересекаются.  

##### **2.2. Ход игрока:**
   - Игрок выбирает выход для обстрела.  
   - Программа проверяет, был ли обстрел успешным:  
     - Если обстрел попал во взвод компьютера, программа сообщает о попадании:  
       ```
       Вы уничтожили один из моих взводов!  
       ```
     - Если обстрел не попал, программа сообщает о промахе:  
       ```
       Промах. Мой ход.  
       ```

##### **2.3. Ход компьютера:**
   - Компьютер случайным образом выбирает выход для обстрела.  
   - Программа проверяет, был ли обстрел успешным:  
     - Если обстрел попал во взвод игрока, программа сообщает о попадании:  
       ```
       Компьютер уничтожил ваш взвод на выходе X.  
       ```
     - Если обстрел не попал, программа сообщает о промахе:  
       ```
       Компьютер промахнулся. Ваш ход.  
       ```

##### **2.4. Проверка условий победы:**
   - После каждого хода программа проверяет, уничтожены ли все взводы противника.  
   - Если все взводы уничтожены, программа объявляет победителя:  
     ```
     Игра окончена! Победил игрок.  
     ```

---

#### 3. **Завершение игры**
   - После завершения игры программа предлагает сыграть снова:  
     ```
     Хотите сыграть снова? (да/нет)  
     ```

   - Если игрок выбирает "да", игра начинается заново с новыми расстановками взводов.  

---

### Пример работы программы

1. **Начало игры:**  
   ```  
   Вы находитесь на поле боя с 4 взводами.  
   У вас есть 25 выходов, где можно разместить взводы.  
   Вы можете разместить только один взвод на каждом выходе.  
   Компьютер делает то же самое со своими четырьмя взводами.  
   Цель игры — обстреливать выходы противника, пытаясь уничтожить все его взводы.  
   Побеждает тот, кто первым уничтожит все четыре взвода противника.  
   Удачи!  

   Введите четыре выхода для ваших взводов (например, 1, 5, 10, 25):  
   > 3, 7, 12, 18  
   ```

2. **Игровой процесс:**  
   ```  
   Ваш ход.  
   Введите выход для обстрела:  
   > 7  
   Промах. Мой ход.  

   Компьютер обстреливает выход 12.  
   Компьютер уничтожил ваш взвод на выходе 12.  
   У вас осталось три взвода.  
   ```

3. **Завершение игры:**  
   ```  
   Игра окончена! Победил компьютер.  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```

---

### Возможные ограничения  
- Игрок должен вводить выходы в правильном диапазоне (от 1 до 25).  
- Программа должна обрабатывать неверный ввод и предлагать повторить попытку.  
- Выходы игрока и компьютера не могут пересекаться.

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Массивы или списки** для представления полей и взводов.  
- **Циклы и условия** для проверки ввода игрока и обработки его ходов.  
- **Функции** для проверки условий победы и обновления состояния полей.  

---

### Рекомендуемые улучшения  
- Добавить возможность выбора количества взводов (например, 3 или 5).  
- Реализовать графический интерфейс для визуализации полей и взводов.  
- Добавить возможность выбора размера поля (например, 6x6 или 7x7).