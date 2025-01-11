# Анализ кода модуля `45_gunner.ru.md`

**Качество кода: 7/10**

-   **Плюсы:**
    -   Документ содержит подробное описание игры "GUNNER".
    -   Присутствует пошаговая инструкция по реализации игры.
    -   Приведены примеры работы программы.
    -   Описаны возможные ограничения и необходимые модули для реализации.
-   **Минусы:**
    -   Документ не содержит кода, а только описание концепции и инструкции.
    -   Нет комментариев в формате RST.
    -   Не хватает документации для функций и методов, так как их нет.

**Рекомендации по улучшению**

1.  **Добавить пример кода:**
    -   Включить пример реализации игры на Python с использованием `pygame`.
    -   Предоставить примеры функций для инициализации игры, управления, стрельбы, подсчёта очков и завершения игры.
2.  **Форматирование:**
    -   Преобразовать весь текст в соответствии с требованиями reStructuredText (RST), где это возможно, например, для заголовков и выделения текста.
    -   Добавить блок с примером кода, оформленного как code-block в RST.
3.  **Логирование:**
    -   Добавить примеры использования логгера для отслеживания ошибок и событий в игре.

**Оптимизированный код**

```markdown
### Название игры: **GUNNER** (Стрельба по мишеням)
=========================================================================================

Игра GUNNER - аркадная игра, в которой игрок управляет стрелком, стреляющим по движущимся мишеням.

.. note::
   Цель игры - попасть в как можно больше мишеней за ограниченное время, зарабатывая очки за каждое попадание.
   С каждым уровнем мишени становятся быстрее и сложнее.

---

#### Описание
**GUNNER** — это аркадная игра, в которой игрок управляет стрелком, стреляющим по движущимся мишеням. Цель игры — попасть в как можно больше мишеней за ограниченное время, зарабатывая очки за каждое попадание. С каждым уровнем мишени становятся быстрее и сложнее, а игра усложняется.

---

### Пошаговая инструкция для реализации

#### 1. **Инициализация игры**
   - При запуске игры программа приветствует игрока и объясняет основные правила.
   - Игрок может выбрать уровень сложности (например, "Легкий", "Средний", "Сложный").
   - В зависимости от сложности программа будет устанавливать скорость движения мишеней.
   - Программа генерирует несколько мишеней, которые появляются в случайных точках экрана.

#### 2. **Основной процесс игры**
   - **Управление:**
     1. Игрок управляет прицелом с помощью клавиш стрелок (или мыши) для наведения на мишени.
     2. Игрок стреляет с помощью клавиши "пробел" или левой кнопки мыши.
   - **Стрельба:**
     1. Программа отслеживает попадания и вычитает очки за промахи.
     2. За каждое попадание в мишень начисляются очки.
     3. Мишени двигаются по экрану случайным образом. С каждым уровнем они становятся быстрее.

   - **Уровни сложности:**
     1. На лёгком уровне мишени двигаются медленно, а их количество ограничено.
     2. На среднем уровне мишени двигаются быстрее, и их больше.
     3. На сложном уровне мишени двигаются с высокой скоростью и появляются в большем количестве.

#### 3. **Подсчёт очков**
   - Программа ведёт счётчик очков, который увеличивается с каждым попаданием.
   - Игрок теряет очки за промахи, если пропустил мишень или не успел выстрелить.

#### 4. **Завершение игры**
   - Игра заканчивается, когда время на уровне истекает или игрок пропускает слишком много мишеней.
   - Программа сообщает финальный счёт и предлагает начать новую игру или выйти:

     ```
     Игра завершена! Ваши очки: X
     Хотите сыграть снова? (да/нет)
     ```

   - Если игрок выбирает "да", начинается новый раунд с тем же уровнем сложности или с выбором другого.
   - Если "нет", программа завершает работу.

---

### Пример работы программы

1. **Начало игры:**
   ```
   Добро пожаловать в игру GUNNER!
   Выберите уровень сложности (Легкий/Средний/Сложный):
   > Средний
   Начинаем игру!
   ```

2. **Игровой процесс:**
   ```
   Мишень 1 появилась в точке (x=50, y=30).
   Вы прицеливаетесь с помощью стрелок и стреляете с помощью пробела.
   Вы попали в мишень! Ваши очки: 10
   Мишень 2 появляется в точке (x=100, y=60).
   Вы промахнулись. Ваши очки: 5
   ```

3. **Результат игры:**
   ```
   Время вышло!
   Ваши очки: 150
   Хотите сыграть снова? (да/нет):
   > нет
   Спасибо за игру!
   ```

---

### Возможные ограничения
- Время на уровне ограничено.
- Игрок может промахнуться, что приведёт к потере очков.
- Мишени не должны быть слишком быстрыми, чтобы игрок мог успеть нацелиться.

---

### Реализация
Игра может быть реализована на Python с использованием следующих возможностей:
- **Модуль `pygame`** для создания графического интерфейса и анимации мишеней.
- **Модуль `random`** для случайного появления мишеней.
- Логика движения мишеней с учётом выбранного уровня сложности.

Рекомендуется:
- Добавить систему сохранения лучших результатов.
- Реализовать различные типы мишеней (например, статичные и движущиеся мишени).

### Пример кода на Python

.. code-block:: python
   
    """
    Пример реализации игры GUNNER с использованием pygame.
    """
    import pygame
    import random
    import sys
    from src.logger.logger import logger  # Добавлен импорт логгера

    # Инициализация Pygame
    pygame.init()

    # Константы
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    TARGET_SIZE = 50
    PLAYER_SPEED = 5
    TARGET_SPEED = 2
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Создание окна
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GUNNER")

    # Класс для мишени
    class Target:
        """
        Класс для представления мишени.

        :param x: Координата x мишени.
        :param y: Координата y мишени.
        :param speed_x: Скорость движения по оси x.
        :param speed_y: Скорость движения по оси y.
        """
        def __init__(self, x, y, speed_x, speed_y):
            self.rect = pygame.Rect(x, y, TARGET_SIZE, TARGET_SIZE)
            self.speed_x = speed_x
            self.speed_y = speed_y

        def move(self):
             """
             Изменяет положение мишени.
             """
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            # Проверка столкновений со стенками экрана
            if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
                self.speed_x *= -1
            if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
                self.speed_y *= -1
                
        def draw(self, screen):
           """
           Отрисовывает мишень на экране.

           :param screen: Экран pygame, на котором будет отрисована мишень.
           """
           pygame.draw.rect(screen, RED, self.rect)

    # Класс для игрока
    class Player:
        """
        Класс для представления игрока.

        :param x: Координата x игрока.
        :param y: Координата y игрока.
        """
        def __init__(self, x, y):
            self.rect = pygame.Rect(x, y, 20, 20)

        def move(self, dx, dy):
            """
            Перемещает игрока на экране.

            :param dx: Изменение положения по оси x.
            :param dy: Изменение положения по оси y.
            """
            self.rect.x += dx
            self.rect.y += dy
            # Ограничение игрока пределами экрана
            self.rect.clamp_ip(screen.get_rect())

        def draw(self, screen):
            """
            Отрисовывает игрока на экране.

            :param screen: Экран pygame, на котором будет отрисован игрок.
            """
            pygame.draw.rect(screen, GREEN, self.rect)

    def display_message(text, screen, color=WHITE, font_size=30):
        """
         Отображает сообщение на экране.

        :param text: Текст сообщения для отображения.
        :param screen: Экран pygame, на котором будет отображено сообщение.
        :param color: Цвет сообщения.
        :param font_size: Размер шрифта сообщения.
        """
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

    def game_over(screen, score):
        """
        Обрабатывает завершение игры, отображая сообщение о конце игры и предлогая сыграть еще раз.

        :param screen: Экран pygame.
        :param score: Итоговый счет игрока.
        """
        display_message(f'Игра окончена! Ваш счет: {score}. Начать заново (y/n)?', screen, color=RED)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        # Логируем перезапуск игры
                        logger.info("Начало новой игры")
                        return True
                    elif event.key == pygame.K_n:
                        # Логируем завершение игры
                        logger.info("Завершение игры")
                        return False
                elif event.type == pygame.QUIT:
                     # Логируем закрытие игры
                    logger.info("Закрытие игры")
                    pygame.quit()
                    sys.exit()

    def init_game(difficulty):
        """
        Инициализирует игру, устанавливает параметры в зависимости от выбранной сложности.

        :param difficulty: Уровень сложности игры ("Легкий", "Средний", "Сложный").
        :return: Список мишеней и скорость мишеней.
        """
        if difficulty == "Легкий":
            num_targets = 5
            target_speed = 1
        elif difficulty == "Средний":
            num_targets = 8
            target_speed = 2
        elif difficulty == "Сложный":
            num_targets = 12
            target_speed = 3
        else:
            # Логируем ошибку неправильного уровня сложности
            logger.error(f"Неизвестный уровень сложности: {difficulty}")
            return None, None

        targets = []
        for _ in range(num_targets):
            x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
            y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)
            speed_x = random.choice([-target_speed, target_speed])
            speed_y = random.choice([-target_speed, target_speed])
            targets.append(Target(x, y, speed_x, speed_y))
        return targets, target_speed

    def main():
        """
        Основная функция игры, запускает и управляет игровым процессом.
        """
        display_message('Добро пожаловать в игру GUNNER! Выберите уровень сложности (Легкий/Средний/Сложный)', screen)
        # Запрашиваем уровень сложности
        difficulty = ""
        while difficulty not in ["Легкий", "Средний", "Сложный"]:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        difficulty = "Легкий"
                    elif event.key == pygame.K_m:
                        difficulty = "Средний"
                    elif event.key == pygame.K_h:
                        difficulty = "Сложный"
                elif event.type == pygame.QUIT:
                    # Логируем закрытие игры
                    logger.info("Закрытие игры")
                    pygame.quit()
                    sys.exit()
            pygame.time.delay(100)
            display_message('Выберите уровень сложности (Легкий - L, Средний - M, Сложный - H)', screen)


        targets, _ = init_game(difficulty)
        if targets is None:
            pygame.quit()
            sys.exit()

        display_message('Начинаем игру!', screen)
        pygame.time.delay(1000)

        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        score = 0
        clock = pygame.time.Clock()
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     # Логируем закрытие игры
                    logger.info("Закрытие игры")
                    pygame.quit()
                    sys.exit()
            
            # Управление игроком
            keys = pygame.key.get_pressed()
            dx = 0
            dy = 0
            if keys[pygame.K_LEFT]:
                dx = -PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                dx = PLAYER_SPEED
            if keys[pygame.K_UP]:
                dy = -PLAYER_SPEED
            if keys[pygame.K_DOWN]:
                dy = PLAYER_SPEED
            player.move(dx, dy)

            # Движение мишеней
            for target in targets:
                target.move()

             # Проверка попаданий
            for target in targets:
                if player.rect.colliderect(target.rect):
                   score += 10
                   x = random.randint(0, SCREEN_WIDTH - TARGET_SIZE)
                   y = random.randint(0, SCREEN_HEIGHT - TARGET_SIZE)
                   speed_x = random.choice([-TARGET_SPEED, TARGET_SPEED])
                   speed_y = random.choice([-TARGET_SPEED, TARGET_SPEED])
                   target.rect = pygame.Rect(x, y, TARGET_SIZE, TARGET_SIZE)
                   target.speed_x = speed_x
                   target.speed_y = speed_y

            # Отрисовка экрана
            screen.fill(BLACK)
            player.draw(screen)
            for target in targets:
                target.draw(screen)
            display_message(f'Счет: {score}', screen, color=GREEN, font_size=24)
            pygame.display.flip()
            clock.tick(60)

            if len(targets) == 0:
                 # Логируем завершение игры
                logger.info("Завершение игры")
                game_running = False
                
        if game_over(screen, score):
            main()
        else:
           pygame.quit()
           sys.exit()

    if __name__ == "__main__":
        main()
```