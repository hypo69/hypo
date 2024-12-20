### Название игры: **GUESS** (Угадай число)

---

#### Описание  
**GUESS** — это простая игра, в которой игрок должен угадать случайное число, загаданное программой. Программа генерирует число в заданном диапазоне, и игроку предоставляется несколько попыток для угадывания этого числа. После каждого ввода программа сообщает, является ли введённое число больше, меньше или равно загаданному.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**  
   - При запуске игры программа приветствует пользователя и объясняет правила.  
   - Игрок выбирает диапазон для загаданного числа (например, от 1 до 100).  
   - Программа случайным образом выбирает число в этом диапазоне.

#### 2. **Основной процесс игры**
   - **Ввод игрока:**
     1. Игрок вводит число, которое, по его мнению, является загаданным.  
     2. Программа проверяет, правильно ли игрок угадал число:
        - Если введённое число меньше загаданного, программа сообщает: "Загаданное число больше."
        - Если введённое число больше загаданного, программа сообщает: "Загаданное число меньше."
        - Если число угадано, программа поздравляет игрока и сообщает количество попыток.

   - **Количество попыток:**  
     1. Игроку предоставляется ограниченное количество попыток для угадывания (например, 10 попыток).
     2. Если игрок не угадывает число за отведённое количество попыток, программа сообщает об этом и предлагает сыграть снова.

#### 3. **Завершение игры**
   - После завершения игры программа предлагает сыграть ещё раз:
     ```  
     Хотите сыграть снова? (да/нет)
     ```

   - Если игрок выбирает "да", начинается новый раунд с новым диапазоном.  
   - Если "нет", программа завершает работу.

---

### Пример работы программы  

1. **Начало игры:**  
   ```  
   Добро пожаловать в игру GUESS!  
   Угадайте число от 1 до 100. У вас 10 попыток.  
   Введите ваше предположение:  
   > 50  
   Загаданное число больше. У вас осталось 9 попыток.  
   ```  

2. **Продолжение игры:**  
   ```  
   Введите ваше предположение:  
   > 75  
   Загаданное число меньше. У вас осталось 8 попыток.  
   ```  

3. **Результат игры:**  
   ```  
   Введите ваше предположение:  
   > 60  
   Поздравляем! Вы угадали число 60 за 3 попытки!  
   Хотите сыграть снова? (да/нет):  
   > нет  
   Спасибо за игру!  
   ```  

---

### Возможные ограничения  
- Игрок может вводить только числа в пределах выбранного диапазона.  
- Количество попыток ограничено (например, 10 попыток).  
- Программа должна адекватно реагировать на некорректные вводы (например, текст вместо числа).

---

### Реализация  
Игра может быть реализована на Python с использованием следующих возможностей:  
- **Модуль `random`** для генерации случайного числа в заданном диапазоне.  
- **Циклы и условия** для обработки попыток игрока и проверки введённого числа.  
- Простая текстовая визуализация оставшихся попыток и подсказок.

Рекомендуется:  
- Реализовать дополнительные уровни сложности с уменьшением количества попыток или с более сложным диапазоном чисел.  
- Добавить обработку ошибок для ввода нечисловых значений.