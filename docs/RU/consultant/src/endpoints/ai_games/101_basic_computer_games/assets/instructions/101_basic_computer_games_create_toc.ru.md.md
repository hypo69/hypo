# Анализ кода модуля `101_basic_computer_games_create_toc.ru.md`

**Качество кода**
8
-   Плюсы
    *   Код представляет собой markdown-файл, содержащий оглавление для сборника игр, что соответствует задаче.
    *   Структура оглавления чёткая и последовательная.
    *   Присутствуют все необходимые элементы для каждого пункта оглавления: название игры, сложность, описание, правила, ссылка на код.
    *   Порядок игр соответствует порядку в книге, как и было запрошено.
-   Минусы
    *   Отсутствует reStructuredText (RST) документация для модуля.
    *   Нет обработки ошибок (в данном случае, это не критично, так как это markdown файл).
    *   Не используются логирование ошибок.
    *   Формат ответа соответствует markdown, но не содержит кода Python для обработки и создания этого файла.
    *   Нет примеров использования и инструкций для генерации такого оглавления.
    *   Нет разделения по сложности, пока все описания имеют значение сложности 6, необходима доработка этого момента.

**Рекомендации по улучшению**

1.  **Документирование:** Необходимо добавить в начале документа описание модуля в формате RST.
2.  **Сложность игры:** Необходимо продумать алгоритм проставления сложности.
3.  **Ссылки на код:** Ссылки на код должны быть сгенерированы динамически, если планируется автоматизировать этот процесс.
4.  **Автоматизация:** Для автоматического создания такого оглавления, нужно будет написать Python скрипт, который будет читать данные об играх и генерировать markdown.
5. **Комментарии** Необходимо прокомментировать каждую строку кода и сделать подробное описание в RST

**Оптимизированный код**

```markdown
# Список игр

Acey Ducey
=========
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Карточная игра, где нужно угадывать, находится ли следующая карта между двумя открытыми картами.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку показывают две карты, а затем он должен сделать ставку, будет ли следующая карта между ними.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/AceyDucey)
---

Amazing
========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра, в которой нужно найти выход из лабиринта.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок начинает в начале лабиринта и, следуя указаниям, должен найти выход.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Amazing)
---

Animal
=======
Сложность 3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра, где нужно угадывать задуманное животное, задавая вопросы.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра начинает задавать вопросы, на которые игрок отвечает "да" или "нет", пока не угадает загаданное животное.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Animal)
---

Awari
======
Сложность 8
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Африканская игра на доске, в которой игроки перемещают фишки по лункам.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди берут все фишки из одной лунки и начинают раскладывать их в соседние лунки. Цель - собрать как можно больше фишек в свою лунку-накопитель.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Awari)
---

Bagels
======
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Логическая игра, где нужно угадывать загаданное число по подсказкам.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает число, а компьютер дает подсказки: "Bagels", если нет ни одной правильной цифры; "Fermi", если есть правильная цифра на правильном месте; "Pico", если есть правильная цифра, но не на своем месте.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Bagels)
---

Banner
======
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа для создания баннеров из символов.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок вводит текст, и программа выводит его в виде баннера.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Banner)
---

Basketball
==========
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор баскетбола, где игрок совершает броски.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок вводит параметры броска, а компьютер моделирует его результат.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Basketball)
---

Batnum
======
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с числами, где нужно победить компьютер, беря спички.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди берут от 1 до 3 спичек, кто забирает последнюю, тот проигрывает.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Batnum)
---

Battle
======
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор морского боя, где нужно потопить корабли противника.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки размещают свои корабли на игровом поле и по очереди стреляют по координатам противника, пока все корабли противника не будут потоплены.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Battle)
---

Blackjack
=========
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в блэкджек (21), где нужно набрать 21 очко или близкое к этому значение, но не больше, чем у дилера.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки получают карты и берут дополнительные, пока не решат остановиться. Задача набрать сумму очков как можно ближе к 21, но не больше.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Blackjack)
---

Bombardment
===========
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор бомбардировки, где нужно попасть в цель.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок вводит параметры для бомбометания, а компьютер показывает результат.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Bombardment)
---

Bombs Away
==========
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор бомбардировки самолётов, где нужно попасть в цель.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок вводит параметры для бомбометания с самолета, а компьютер показывает результат.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BombsAway)
---

Bounce
======
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Анимация прыгающего шара на экране.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;На экране отображается анимация прыгающего шара.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Bounce)
---

Bowling
=======
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор боулинга, где нужно сбивать кегли.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок вводит параметры броска шара, а компьютер моделирует результат.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Bowling)
---

Boxing
======
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор бокса, где игрок управляет боксёром.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает действия боксера, а компьютер моделирует бой.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Boxing)
---

Bug
===
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра, где нужно ловить жуков на экране.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен успеть поймать убегающих жуков.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Bug)
---

Bullfight
=========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор корриды, где игрок управляет матадором.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает действия матадора, а компьютер моделирует действия быка.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Bullfight)
---

Bullseye
========
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в дартс, где нужно попасть в цель.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает силу и угол броска, а компьютер показывает результат.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Bullseye)
---

Buzzword
========
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра со словами, где нужно угадывать жаргонные выражения.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку даются подсказки, и он должен угадать жаргонное выражение.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Buzzword)
---

Calendar
========
Сложность 3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа для вывода календаря на экран.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа выводит календарь на экран.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Calendar)
---

Change
======
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с монетами, где нужно выдать сдачу.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку нужно выдать сдачу минимальным количеством монет.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Change)
---

Checkers
========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в шашки, где нужно обыграть компьютер.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок играет в шашки против компьютера, по правилам шашек.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Checkers)
---

Chemist
=======
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра-викторина по химии, где нужно угадывать элементы.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку задаются вопросы о химических элементах.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Chemist)
---

Chief
=====
Сложность 8
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Логическая игра, где нужно определить местоположение объекта.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку нужно определить местоположение объекта, задавая вопросы.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Chief)
---

Chomp
=====
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра, где нужно избегать съеденного кусочка, "ядовитый" кусочек.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди убирают кусочки из решетки, проигрывает тот, кто съест ядовитый.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Chomp)
---

Civil War
=========
Сложность 8
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор гражданской войны, где игрок управляет армией.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет армией, принимая стратегические решения.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CivilWar)
---

Combat
======
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор боя, где нужно победить противника.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает действия, а компьютер моделирует бой.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Combat)
---

Craps
=====
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в кости крэпс, где нужно угадать результат броска.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок делает ставку на результат броска костей.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Craps)
---

Cube
====
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с кубами, где нужно угадать их расположение.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен угадать расположение кубов.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Cube)
---

Depth Charge
============
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор глубинных бомб, где нужно потопить субмарину.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок бросает глубинные бомбы, чтобы потопить субмарину.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/DepthCharge)
---

Diamond
=======
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с алмазами, где нужно угадать их расположение.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен угадать расположение алмазов.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Diamond)
---

Dice
====
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в кости, где нужно угадать результат.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок делает ставку на результат броска костей.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Dice)
---

Digits
======
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с цифрами, где нужно их угадать.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку нужно угадать последовательность цифр.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Digits)
---

Even Wins
=========
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с четными числами, где нужно сделать ставку.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок делает ставку на то, выпадет ли четное число.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/EvenWins)
---

Flip Flop
=========
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с переворотом, где нужно собрать одинаковые элементы.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку нужно перевернуть элементы, чтобы найти одинаковые.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/FlipFlop)
---

Football
========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор футбола, где игрок управляет командой.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает действия команды, а компьютер моделирует игру.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Football)
---

Fur Trader
==========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра о торговле мехом, где нужно разбогатеть.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок покупает и продает мех, пытаясь получить прибыль.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/FurTrader)
---

Golf
====
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор гольфа, где нужно забить мяч в лунку.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает параметры удара, а компьютер моделирует результат.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Golf)
---

Gomoko
======
Сложность 8
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в гомоку (пять в ряд), где нужно обыграть компьютер.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди ставят свои фишки, пытаясь составить ряд из 5 штук.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Gomoko)
---

Guess
=====
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в угадывание чисел, где нужно отгадать задуманное.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает задуманное число.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Guess)
---

Gunner
======
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор стрельбы, где нужно попасть в цель.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает параметры стрельбы, а компьютер показывает результат.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Gunner)
---

Hammurabi
=========
Сложность 8
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра-симулятор правления Хаммурапи, где нужно управлять городом.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет городом, принимает решения о посевах, налогах и т.д.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Hammurabi)
---

Hangman
=======
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра "Виселица", где нужно отгадать слово по буквам.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает буквы в загаданном слове, пока не будет нарисована виселица.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Hangman)
---

Hello
=====
Сложность 1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Простая программа для приветствия.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа выводит на экран приветствие.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Hello)
---

Hexapawn
========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в гексапау, где нужно обыграть компьютер.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди двигают свои фишки по доске, цель - достичь противоположного конца доски.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Hexapawn)
---

Hi-Lo
=====
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в угадывание чисел, где нужно угадать больше или меньше.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок пытается угадать загаданное число, выбирая больше или меньше.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Hi-Lo)
---

Hockey
======
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор хоккея, где игрок управляет командой.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает действия команды, а компьютер моделирует игру.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Hockey)
---

Horserace
==========
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор скачек, где нужно угадать победителя.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок делает ставку на лошадь, и компьютер моделирует гонку.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Horserace)
---

Hurkle
======
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с поиском объекта, где нужно его найти.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен найти объект, опираясь на подсказки.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Hurkle)
---

Kinema
======
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с кино, где нужно угадать фильм.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает фильм по описанию или кадрам.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Kinema)
---

King
====
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в короля, где нужно его спасти.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен спасти короля, решая головоломки.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/King)
---

Letter
======
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с буквами, где нужно составить слово.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен составить слово из предложенных букв.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Letter)
---

Life
====
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра "Жизнь", моделирующая эволюцию клеточных автоматов.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки наблюдают за тем, как изменяется популяция клеток на экране.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Life)
---

Literature
==========
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с литературой, где нужно угадать автора или произведение.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает автора или произведение по описанию.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Literature)
---

Love
====
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра о любви, где нужно ответить на вопросы.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку задаются вопросы о любви.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Love)
---

Lunar Lander
============
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор посадки на Луну, где нужно управлять кораблем.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет кораблем, чтобы безопасно посадить его на Луну.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/LunarLander)
---

Mastermind
==========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра "Мастермайнд", где нужно угадать последовательность.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает секретную последовательность, получая подсказки.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Mastermind)
---

Math Dice
=========
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с математическими кубиками, где нужно решать примеры.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок решает математические примеры, используя результаты бросков кубиков.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/MathDice)
---

Mugwump
=======
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с поиском объекта, где нужно его найти.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен найти объект, используя подсказки.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Mugwump)
---

Name
====
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с именами, где нужно угадать имя.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает имя по подсказкам.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Name)
---

Nicomachus
==========
Сложность 7
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с числами, где нужно получить заданную сумму.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен получить заданную сумму, складывая числа.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Nicomachus)
---

Nim
===
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра Ним, где нужно забрать последнюю спичку.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди берут от 1 до 3 спичек, проигрывает тот, кто забирает последнюю.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Nim)
---

Number
======
Сложность 4
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с числами, где нужно их угадать.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает число по подсказкам.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Number)
---

One Check
=========
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с шашками, где нужно обыграть компьютер.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок играет в шашки против компьютера, по правилам шашек.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/OneCheck)
---

Orbit
=====
Сложность 6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с орбитой, где нужно управлять космическим кораблем.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет космическим кораблем, чтобы не столкнуться с препятствиями.
* [Перейти к коду](https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/Orbit)
---

Pizza
=====
Сложность 5
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с пиццей, где