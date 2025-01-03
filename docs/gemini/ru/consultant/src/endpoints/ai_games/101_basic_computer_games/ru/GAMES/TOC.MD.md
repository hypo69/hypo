# Анализ кода модуля TOC.MD

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и легко читается.
    - Игры разделены на разделы с указанием сложности и описанием.
    - Есть ссылки на исходный код каждой игры.
- Минусы
    - Отсутствует явное указание на использование RST в комментариях (хотя это подразумевается из инструкции).
    - Не использует `j_loads` или `j_loads_ns`.
    - Не реализована обработка ошибок.
    - Нет логирования.
    - Нет docstring для модуля.
    - Ссылки на код не соответствуют стандарту.

**Рекомендации по улучшению**

1. **Документация:**
   - Добавить docstring в формате RST для всего модуля.
   - Переписать комментарии в формате RST, используя соответствующие конструкции, такие как списки и гиперссылки.
   - Внедрить описание каждой игры в виде RST документации.
2. **Структура:**
   - Привести ссылки на код в более стандартизированный вид, возможно через анкорные ссылки или иные конструкции reStructuredText.
3. **Импорты:**
   - Добавить необходимые импорты (в данном случае, импорты не требуются, так как это файл Markdown).
4. **Логирование:**
    - Добавить логирование в случае возникновения ошибок при обработке файла, если это применимо.
5. **Обработка данных:**
    - Этот файл не обрабатывает данные, поэтому `j_loads` не нужен.

**Оптимизированный код**
```markdown
"""
Список игр
=========================================================================================

Этот модуль содержит перечень игр с их описаниями и ссылками на исходный код.

Пример использования
--------------------

Этот файл используется для навигации по играм и содержит ссылки на их исходный код.

"""
# Список игр

ACEDU
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Карточная игра, в которой игрок делает ставку на то, будет ли следующая карта между двумя открытыми картами.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроку показывают две карты, и он должен сделать ставку, будет ли следующая карта между ними.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/ACEDU>`_
---

AMAZIN
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра-лабиринт, где игрок пытается найти выход из случайно сгенерированного лабиринта.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок перемещается по лабиринту, выбирая направление, пока не найдет выход.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/AMAZIN>`_
---

ANIMAL
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра, в которой компьютер загадывает животное, а игрок пытается его угадать, задавая вопросы, на которые можно ответить "да" или "нет".
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Компьютер выбирает животное, игрок задает вопросы, и компьютер отвечает "да" или "нет". Если животное не отгадано, компьютер задает вопросы, чтобы расширить свою базу знаний.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/ANIMAL>`_
---

AWARI
========
Сложность 7

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Африканская игра-манкала на доске, где игроки перемещают семена по лункам, чтобы захватить камни противника.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди перемещают семена по лункам, пытаясь захватить семена противника.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/AWARI>`_
---

BAGLES
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Логическая игра, где игрок должен угадать загаданное компьютером число по подсказкам.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает число, компьютер дает подсказки: "Bagels" - нет цифр в числе, "Fermi" - цифра есть на правильной позиции, "Pico" - цифра есть в числе, но не на правильной позиции.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BAGLES>`_
---

BANNER
========
Сложность 2

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа для создания текстовых баннеров.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Пользователь вводит текст, и программа выводит его в виде баннера из символов.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BANNER>`_
---

BASKET
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор баскетбола, где игрок бросает мяч в корзину.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен рассчитать угол и силу броска, чтобы забросить мяч в корзину.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BASKET>`_
---

BATNUM
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с числами, где игрок должен угадать число, которое загадал компьютер.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок пытается угадать число, загаданное компьютером, получая подсказки о том, больше или меньше его предположение.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BATNUM>`_
---

BATTLE
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор морского боя, где игроки размещают корабли на поле и пытаются потопить корабли противника.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди называют координаты на поле противника, чтобы потопить его корабли.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BATTLE>`_
---

BINGO
========
Сложность 2

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в Бинго.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки отмечают числа на своих карточках, когда они выпадают, и выигрывает тот, кто первым заполнит линию или всю карточку.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BINGO>`_
---

BLKJAK
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в блэкджек, где игрок пытается набрать 21 очко или близкое к нему значение, не превышая его.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок набирает карты, стараясь набрать 21 очко или как можно ближе к нему, не перебрав.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BLKJAK>`_
---

BOAT
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра-симулятор управления лодкой, где нужно доплыть до цели, учитывая течение и ветер.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет лодкой, корректируя направление, чтобы добраться до цели, учитывая ветер и течение.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BOAT>`_
---

BOMBER
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор бомбардировки, где игрок должен точно сбросить бомбы на цель.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет бомбардировщиком и должен сбросить бомбы на цель, учитывая скорость и траекторию.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BOMBER>`_
---

BOUNCE
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Анимация прыгающего шара.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Простая программа, которая рисует анимированный прыгающий шар.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BOUNCE>`_
---

BOWL
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор боулинга, где игрок бросает шар и сбивает кегли.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен выбрать направление и силу броска, чтобы сбить как можно больше кеглей.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BOWL>`_
---

BOXING
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор бокса, где игрок управляет боксером и сражается с противником.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет боксером, наносит удары и защищается, чтобы победить противника.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BOXING>`_
---

BULLEYE
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в дартс, где игрок бросает дротики в мишень.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен бросить дротик в мишень, чтобы набрать очки, стараясь попасть в центр.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BULLEYE>`_
---

BULL
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор корриды, где игрок управляет тореадором и должен уворачиваться от быка.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет тореадором, маневрируя, чтобы увернуться от быка, и старается продержаться как можно дольше.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BULL>`_
---

BUZZWD
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра со словами, где компьютер генерирует жаргоны, а игрок пытается отгадать их значение.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Компьютер генерирует набор слов, и игрок пытается отгадать их значение.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/BUZZWD>`_
---

CALNDR
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа для вывода календаря на заданный год.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа выводит календарь для заданного года в текстовом формате.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CALNDR>`_
---

CHANGE
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с монетами, где игрок должен дать сдачу определенной суммы, используя минимальное количество монет.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен посчитать и выдать сдачу минимальным количеством монет.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CHANGE>`_
---

CHECKR
========
Сложность 7

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в шашки.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди перемещают шашки, чтобы захватить шашки противника и достичь противоположного края доски.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CHECKR>`_
---

CHEMST
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра-викторина по химии, где игроки отвечают на вопросы о химических элементах и соединениях.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок отвечает на вопросы по химии, чтобы проверить свои знания.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CHEMST>`_
---

CHIEF
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Логическая игра, где игрок должен правильно расставить солдат в звании по росту.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен расположить фигуры по росту, используя ограниченные ходы.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CHIEF>`_
---

CHOMP
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с поеданием, где игроки по очереди "откусывают" части прямоугольника, и кто откусит последнюю часть, проигрывает.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди откусывают части прямоугольника, пытаясь не откусить последнюю часть.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CHOMP>`_
---

CIVILW
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор гражданской войны, где игрок управляет войсками и сражается с противником.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет войсками, перемещает их по полю и участвует в битвах.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CIVILW>`_
---

CRAPS
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в крэпс, где игроки бросают кости и делают ставки на результат броска.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки делают ставки на результат броска костей, стараясь угадать комбинацию.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CRAPS>`_
---

CUBE
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с кубами, где игрок должен раскрасить грани куба в правильной последовательности.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен расположить грани куба так, чтобы цвета на соседних гранях соответствовали правилам.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/CUBE>`_
---

DIAMND
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с алмазами, где игрок должен найти алмазы на карте.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок исследует карту, пытаясь найти алмазы.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/DIAMND>`_
---

DICE
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в кости, где игрок должен угадать сумму выпавших очков.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает сумму очков, которые выпадут на костях.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/DICE>`_
---

DIGITS
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с цифрами, где игрок должен угадать число, загаданное компьютером.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен угадать число, загаданное компьютером, получая подсказки о том, больше или меньше его предположение.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/DIGITS>`_
---

EVEN
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с четными числами, где игрок должен выбрать четное число.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает четное число из предложенных, чтобы выиграть.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/EVEN>`_
---

FIPFOP
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с переворотом, где игрок должен перевернуть фишки так, чтобы они стали одного цвета.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок переворачивает фишки, чтобы сделать их все одного цвета.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/FIPFOP>`_
---

FOOTBL
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор футбола, где игрок управляет командой и пытается забить голы.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок выбирает стратегию и управляет командой, чтобы забить голы и победить противника.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/FOOTBL>`_
---

FURS
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра о торговле мехом, где игрок должен покупать и продавать меха, чтобы заработать деньги.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен покупать и продавать меха, пытаясь заработать как можно больше денег.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/FURS>`_
---

GOLF
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор гольфа, где игрок должен забить мяч в лунку.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен рассчитать силу и направление удара, чтобы забить мяч в лунку.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/GOLF>`_
---

GOMOKO
========
Сложность 7

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в гомоку, где игроки по очереди ставят свои знаки на доску, чтобы выстроить пять в ряд.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди ставят свои знаки, пытаясь первыми выстроить пять в ряд.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/GOMOKO>`_
---

GUESS
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в угадывание чисел, где игрок пытается угадать загаданное число.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен угадать число, загаданное компьютером, получая подсказки о том, больше или меньше его предположение.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/GUESS>`_
---

GUNNER
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор стрельбы из пушки, где игрок должен точно стрелять по целям.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен рассчитать угол и силу выстрела, чтобы поразить цель.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/GUNNER>`_
---

HANG
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра "Виселица", где игрок должен угадать загаданное слово, угадывая буквы.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен угадать слово, угадывая буквы, прежде чем будет дорисована виселица.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HANG>`_
---

HELLO
========
Сложность 1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Программа для приветствия.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Простая программа, которая выводит на экран "HELLO".
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HELLO>`_
---

HEX
========
Сложность 7

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в гексапау, где игроки по очереди перемещают фишки, чтобы добраться до противоположной стороны доски.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди перемещают свои фишки, чтобы добраться до противоположной стороны доски.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HEX>`_
---

HI LO
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра в угадывание чисел, где игрок должен угадать число, получая подсказки "выше" или "ниже".
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает число, получая подсказки от компьютера, выше или ниже загаданное число.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HI LO>`_
---

HMRABI
========
Сложность 7

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра-симулятор правления Хаммурапи, где игрок управляет городом и должен принимать решения, чтобы город процветал.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок принимает решения по управлению городом, стараясь поддерживать население и экономику.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HMRABI>`_
---

HOCKEY
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор хоккея, где игрок управляет командой и пытается забить шайбу.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок управляет командой, перемещает игроков и пытается забить шайбу.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HOCKEY>`_
---

HORSES
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Симулятор скачек, где игрок делает ставки на лошадей.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок делает ставки на лошадей, пытаясь угадать победителя забега.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HORSES>`_
---

HURKLE
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с поиском, где игрок должен найти спрятанное существо на карте.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок исследует карту, получая подсказки о том, где находится спрятанное существо.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/HURKLE>`_
---

KINEMA
========
Сложность 2

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с кино, где компьютер выводит кадры из фильма, а игрок пытается угадать название.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Компьютер выводит кадры, а игрок пытается угадать название фильма.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/KINEMA>`_
---

KING
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра, где игрок играет роль короля и должен управлять королевством.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок принимает решения в качестве короля, управляя финансами, военными делами и другими сферами.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/KING>`_
---

LETTER
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с буквами, где игрок должен составить слово из предложенных букв.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок составляет слова из предложенных букв.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/LETTER>`_
---

LIFE
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра "Жизнь", симуляция клеточного автомата, где клетки рождаются, умирают и размножаются.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Клетки на сетке рождаются, умирают и размножаются по правилам игры, создавая различные шаблоны.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/LIFE>`_
---

LIT QZ
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра-викторина по литературе, где игроки отвечают на вопросы о писателях и книгах.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок отвечает на вопросы по литературе, чтобы проверить свои знания.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/LIT QZ>`_
---

MATHDI
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с математическими кубиками, где игрок должен решить примеры, используя числа на кубиках.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок решает математические примеры, используя числа, выпавшие на кубиках.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/MATHDI>`_
---

MUGWMP
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с поиском, где игрок должен найти спрятанное существо на карте.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок исследует карту, получая подсказки о местоположении спрятанного существа.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/MUGWMP>`_
---

NIKOMA
========
Сложность 6

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с числами, где игрок должен составить последовательность, используя правило Нихомахуса.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен составить числовую последовательность, используя правило Нихомахуса.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/NIKOMA>`_
---

NIM
========
Сложность 4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра Ним, где игроки по очереди берут предметы из кучи, и проигрывает тот, кто возьмет последний.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди берут предметы из кучи, стараясь не взять последний.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/NIM>`_
---

NUMBER
========
Сложность 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с числами, где игрок должен угадать число, загаданное компьютером.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок угадывает число, загаданное компьютером.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/NUMBER>`_
---

ICHECK
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с шашками, где игрок должен захватить все шашки противника.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игроки по очереди перемещают свои шашки, чтобы захватить шашки противника.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games/ru/ICHECK>`_
---

ORBIT
========
Сложность 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игра с орбитой, где игрок должен управлять кораблем, чтобы выйти на орбиту.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Игрок должен рассчитать тягу, чтобы вывести корабль на орбиту.
* `Перейти к коду <https://github.com/hypo69/hypo/blob/master/src/endpoints/ai_games/101_basic_computer_games