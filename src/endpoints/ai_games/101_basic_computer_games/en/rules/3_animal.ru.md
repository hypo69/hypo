### Название игры: **Animal** (Угадай животное)

#### Описание
Игра помогает компьютеру "учиться" угадывать животных, основываясь на задаваемых пользователю вопросах. Если предположение компьютера неверное, игрок вводит новое животное и вопрос, который поможет отличить его от предыдущего. Таким образом, компьютер расширяет свою базу данных с каждым новым раундом.

---

### Пошаговая инструкция для реализации

#### 1. **Начало игры**
   - Компьютер приветствует игрока и спрашивает, готов ли он загадать животное:
     ```
     Готовы загадать животное? (да/нет)
     ```
   - Если пользователь вводит "нет", игра завершает работу.

#### 2. **Задание вопросов**
   - Компьютер начинает с корневого вопроса (например, "Это животное плавает?").
   - Игрок отвечает "да" или "нет".
   - Если текущий узел — вопрос:
     - Компьютер переходит к следующему узлу в зависимости от ответа.
   - Если текущий узел — это животное:
     - Компьютер делает предположение:
       ```
       Это [животное]? (да/нет)
       ```
     - Если ответ "да", компьютер поздравляет себя:
       ```
       Ура! Я угадал!
       ```
     - Если ответ "нет", игра переходит к добавлению нового животного.

#### 3. **Добавление нового животного**
   - Если компьютер ошибся, он спрашивает:
     ```
     Какое животное вы загадали? 
     ```
   - Игрок вводит название нового животного.
   - Компьютер просит уточнить вопрос, который поможет отличить это животное от предыдущего:
     ```
     Какой вопрос помог бы различить [новое животное]? 
     ```
   - Игрок вводит новый вопрос.
   - Компьютер добавляет новый узел в дерево, обновляя свою базу знаний.

#### 4. **Сохранение данных**
   - После добавления нового животного или по запросу игрока, компьютер сохраняет данные:
     ```
     База знаний обновлена. Спасибо!
     ```

#### 5. **Новая игра**
   - После завершения текущего раунда, компьютер предлагает сыграть снова:
     ```
     Готовы загадать новое животное? (да/нет)
     ```

---

### Пример работы

1. **Первый раунд**:
   ```
   Компьютер: Готовы загадать животное? (да/нет): да
   Компьютер: Это животное плавает? (да/нет): да
   Компьютер: Это рыба? (да/нет): нет
   Компьютер: Какое животное вы загадали? Ответ: дельфин
   Компьютер: Какой вопрос помог бы различить дельфина? Ответ: Это животное живет в воде?
   Компьютер: Спасибо! Теперь я знаю больше о животных.
   ```

2. **Второй раунд**:
   ```
   Компьютер: Готовы загадать новое животное? (да/нет): да
   Компьютер: Это животное плавает? (да/нет): да
   Компьютер: Это животное живет в воде? (да/нет): да
   Компьютер: Это дельфин? (да/нет): да
   Компьютер: Ура! Я угадал!
   ```

---

### Возможные ограничения
- Проверка на корректность ввода (например, ответы "да/нет").
- Сохранение базы данных на диск для использования в следующих играх.
- Предупреждение о слишком больших деревьях, если структура становится слишком громоздкой.

### Дополнения
- Используйте простую структуру дерева для хранения вопросов и животных.
- Реализация на Python может включать сохранение данных с помощью `json` или `pickle`. Если потребуется пример кода или более сложные сценарии, дайте знать!