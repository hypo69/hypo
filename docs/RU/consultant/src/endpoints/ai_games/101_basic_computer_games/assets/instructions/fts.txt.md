# Анализ кода модуля <fts.txt>

**Качество кода**
**7/10**
- Плюсы:
    - Код содержит текстовые инструкции для  BASIC.
    - Код хорошо структурирован и следует логической последовательности для имитации игр.
    - Присутствуют комментарии, хоть и не в формате RST.
- Минусы:
    - Отсутствуют импорты, так как это не код python.
    - Код не является Python, поэтому docstring не применяются напрямую.
    - Комментарии не соответствуют формату RST.
    - Присутствуют избыточные блоки кода, не соответствующие формату.
    - Нет обработки ошибок с помощью логгера, так как это не Python.

**Рекомендации по улучшению**
1.  **Использование reStructuredText (RST) для документации**:
    - Поскольку это текстовый файл с инструкциями, документация RST не применима, но можно оформить текст в стиле markdown.
2.  **Улучшение комментариев**:
    - Поскольку это текстовый файл с инструкциями, подробные комментарии RST не нужны.
3.  **Форматирование**:
    - Необходимо унифицировать форматирование документа, используя markdown.
4. **Логирование ошибок:** 
    - Данный пункт не применим к текстовому файлу, так как это не код Python.

**Оптимизированный код**

```markdown
# BASIC COMPUTER GAMES

## Инструкция

### Основные требования:
**Output Language**: RU (Русский)

1.  **Формат документации**:
    - Используйте **Markdown** для форматирования текста.
    - Текст должен быть читаемым и логически структурированным.

2.  **Сохранение комментариев**:
    - Комментарии и описания должны быть сохранены.

3.  **Анализ структуры**:
    - Содержание файла представляет собой список игр, которые можно улучшить,
    - но в рамках этого задания требуется только форматирование, без анализа кода.

4.  **Рефакторинг и улучшения**:
    -  Добавьте подзаголовки и разделите текст на логические части, используя Markdown.
    -  Обеспечьте удобочитаемость текста.
    -  Уберите избыточные строки и символы, не несущие смысловой нагрузки.

### Полный текст с форматированием:

```
BASIC COMPUTER GAMES S750
Digitized by the Internet Archive in 2023 with funding from No Sponsor
https://archive.org/details/101 basiccomputer0000davi

101 BASIC Computer Games
Digital Equipment Corporation Maynard, Massachusetts

Additional copies of 101 BASIC Computer Games are available for $7.50 plus 50 cents postage and handling from:
Software Distribution Center Digital Equipment Corporation Maynard, Massachusetts 01754
Write for discount schedule on quantities over 30.

Two supplemental guides are available for use with this book. They are:
Understanding Mathematics and Logic Using BASIC Computer Games, $4.50. Grades 7-12.
Getting Started in Classroom Computing, $3.00. Grades 2-7.

lst Printing -- July 1973 2nd Printing -- April 1974 3rd Printing -- March 1975
Copyright © 1975 by:
Digital Equipment Corporation Maynard, Massachusetts 01754

## Содержание
**Игра** | **Описание**
---------|------------------------------------------------------------------------------------
ACEYDU | Play acey-ducey with the computer
AMAZIN | Computer constructs a maze
ANIMAL | Computer guesses animals and learns new ones from you
AWARI | Ancient game of rotating beans in pits
BAGLES | Guess a mystery 3-digit number by logic
BANNER | Prints any message on a large banner
BASBAL | Baseball game
BASKET | Basketball game
BATNUM | Match wits in a battle of numbers vs. the computer
BATTLE | Decode a matrix to locate enemy battleship
BINGO | Computer prints your card and calls the numbers
BLKJAC | Blackjack (very comprehensive), Las Vegas rules
BLKJAK | Blackjack (standard game)
BOAT | Destroy a gunboat from your submarine
BOMBER | Fly World War II bombing missions
BOUNCE | Plot a bouncing ball
BOWL | Bowling at the neighborhood lanes
BOXING | 3-round Olympic boxing match
BUG | Roll dice vs. the computer to draw a bug
BULCOW | Guess a mystery 5-digit number vs. the computer
BULEYE | Throw darts
BULL | You're the matador in a championship bullfight
BUNNY | Computer drawing of the Playboy bunny
BUZZWD | Compose your speeches with the latest buzzwords
CALNDR | Calendar for any year
CAN-AM | Drive a Group 7 car in a Can-Am road race
CHANGE | Computer imitates a cashier
CHECKR | Game of checkers
CHEMST | Dilute kryptocyanic acid to make it harmless
CHIEF | Silly arithmetic drill
CHOMP | Eat a cookie avoiding the poison piece (2 or more players)
CIVILW | Fight the Civil War
CRAPS | Play craps (dice), Las Vegas style
CUBE | Negotiate a 3-D cube avoiding hidden landmines
DIAMND | Prints l-page diamond patterns
DICE | Summarizes dice rolls
DIGITS | Computer tries to guess digits you select at random
DOGS | Penny arcade dog race
EVEN | Take objects from a pile--try to end with an even number
EVENL | Same as EVEN--computer improves its play
FIPFOP | Solitaire logic game--change a row of Xs to Os
FOOTBL | Professional football (very comprehensive)
FOTBAL | High School football
FURS | Trade furs with the white man
GOLF | Golf game--choose your clubs and swing
HANOI | Ancient board game of logic and strategy
HI-Q | Guess a mystery number--computer gives you clues
GUNNER | Fire a cannon at a stationary target
GUNER1 | Fire a cannon at a moving target
HANG | Hangman word guessing game
HELLO | Computer becomes your friendly psychiatrist
HEX | Hexapawn game
HI-LO | Try to hit the mystery jackpot
HIQ | Try to remove all the pegs from a board
HMRABI | Govern the ancient city-state of Sumeria
HOCKEY | Ice hockey vs. Cornell
HORSES | Off-track betting on a horse race
HURKLE | Find the Hurkle hiding on a 10x10 grid
KINEMA | Drill in simple kinematics
KING | Govern a modern island kingdom wisely
LETTER | Guess a mystery letter--computer gives you clues
LIFE | John Conway's Game of Life
LIFE-2 | Competitive game of life (2 or more players)
LITQZ | Children's literature quiz
MATHD1 | Children's arithmetic drill using pictures of dice
MCNOPLY | Monopoly for 2 players
MUGWMP | Locate 4 Mugwumps hiding on a 10x10 grid
NUMBER | Computer guesses number you think of
NIM | Chinese game of Nim
NUMBR | Silly number matching game
ORBIT | Challenging game to remove checkers from a board
POETRY | Destroy an orbiting germ-laiden enemy spaceship
POET | Deliver pizzas successfully
POKER | Computer composes poetry in 4-part harmony
QUBIC | Computer composes random poetry
REVERSE | Poker game
ROCKT1 | 3-dimensional tic-tac-toe
ROCKT2 | Move a single chess queen vs. the computer
ROCKET | Order a series of numbers by reversing
RULLET | Land an Apollo capsule on the moon
RUS ROU | Lunar landing from 500 feet (with plot)
SALVO | Very comprehensive lunar landing
SPLAT | Game of rock, scissors, paper
STARS | European roulette table
STOCK | Russian roulette
SYNONM | Destroy an enemy fleet of ships
TARGET | Destroy 4 enemy outposts
3DPLOT | Slot machine (one-arm bandit)
LICTAC | Pictures of Snoopy
TOWER | Comprehensive game of spacewar
TRAIN | Open a parachute at the last possible moment
TRAP | Guess a mystery number--stars give you clues
23MTCH | Stock market simulation
UGLY | Word synonym drill
WAR | Destroy a target in 3-D space--very tricky
WAR-2 | Plots families of curves--looks 3-dimensional
WEKDAY | Tic-tac-toe
WORD | Towers of Hanoi puzzle
YAHTZE | Time-speed-distance quiz
ZOOP | Trap a mystery number--computer gives you clues
 | Game of 23 matches--try not to take the last one
 | Silly profile plot of an ugly woman
 | Card game of war
 | Troop tactics in war
 | Facts about your birthday
 | Word guessing game
 | Dice game of Yahtzee
 | BASIC programmer's nightmare

## Appendices
### Families of Games
   * Game Diagrams
   * Instructions to Game Authors

```

Preface
Mots eis not the first collection of computer games and. simula— tions nor will it by any means be the last. However, in many Weyer it 1S unigue. It is the first collection of games all mernciC, lt 1s also the only collection that.contains both a complete listing and a sample run of each game along with a descriptive write-up.

Educational Value of Games
Educators have widely different opinions as to the educational value of games. There tends to be agreement that games are highly motivational and frequently very addictive. Most educators agree that games generally foster learning by dis- covery--1.e., the player doesn't sit down at the terminal with the purpose of learning a-principle of togic but after playing BAGLES three or four times he most assuredly has learned some- thing about logic. Newton's second law is probably the furthest thing from the mind of a person sitting down to play ROCKET. However, when the player finally lands his LEM successfully on the moon, the chances are very good that he has discovered something about gravity varying inversely with the mass of the LEM and the distance from the moon.

The main objection to games as a learning tool seems to be the fact that it's largely unguided learning and potentially waste- ful of computer time. Art Leuhrmann of Dartmouth joked that some computer center directors might be willing to pay to not have the book sold on campus because of the computer time that would be burned up by playing the games; however, the educational value of games can be enormous - not only in their playing but in their creation,
The majority of games submitted tend to simulate a sport, card or board game, a game of chance or something which already exists. Only a few games begin to use the logical and computational Capabilities of the computer to come up with something new and Geuly unique. Some that do are STARES, BULCOW, ROCKET, and
Certain games are, of course, more popular with game authors that others. There were no less than ten versions of NIM submitted, nine versions each of HORSES (Horse Race) and TICTAC (Tic-Tac-Toe), and eight versions of CRAPS. Other popular ones were simulations of baseball, basketball, football, blackjack, and hangman.

Families of Games
A word about the title of the book. The astute, quantitatively-\nofLented reader might notice that “there seem to be more coan\n101 games in the book. In fact, there are 108 individual games;\n(-are-different verSrons of another -game.. There are 101. ceparate write-ups; thus, the title of the book.\nPerhaps it is a disease of using the computer or perhaps it is just a compulsion of man that he must categorize things. fThe games in this book could be categorized by level of GLEE Led dey, as is often the case in collections of puzzles. They could also be categorized in an educational sense, for example, those that could be used to teach logic principles, those that foster learing by discovery, those that require the “user -to- solve—an algebra problem, etc.
In the first two groups, Number or Letter Guessing and Piles of Objects, you will probably get more enjoyment 12 youcpilay the games in the numbered order as there is a definite sequential MoeUbe CO tneir dittiieulty. In the other fourteen categories, the games may be played in any order; one does not generally build upon another except in a few cases. INsPpantlcular,../OU should play:\nBAGLES before BULCOW HI-Q before 1CHECK BATTLE before SALVO GUNNER before SUNERL ROCKET before ROCKT2 HMRABI before KING

Equipment to Play, Computer and Otherwise
Most of the games in this book require no special knowledge, tools Or equipment to play, except, .Otccourse, a BASIC-speaking computer. Hour of the matrix games will probably be more enjoyable if you use a grid or quadrille paper to Play. Unless you have a photo- graphic memory, QUBIC almost certainly requires a diagram. There is a page included as Appendix B which contains some supplemental diagrams; you may wish to reproduce it if you become addicted to the games on it.

With few exceptions, the games all run in "standard" BASTC. Any exceptions are noted in the write-ups under the heading, "Computer Limitations." The major difference between various computer systems appears to be in the handling of alphabetic strings. On Digital systems a subscripted string variable, for example, AS(8) or en SM Gh Rey's refers to a variable in an array or matrix. Other BASIC compilers may not have string arrays.
On some systems, in particular, Digital's Edusystems 20, 25, and 50, strings are limited to 6 characters. Several strings may, or course, be combined in an array to permit longer than 6-letter words to be used.
Many programs use the RANDOMIZE command to start the random number generator at a random point. Some BASIC compilers do not recognize RANDOMIZE and it must be removed in order for the program to run.

Digital BASIC permits more than one statement on each program line.
Statement separators on the line may be one of three characters -- Z-Or = .Or O A
Digital Equipment Corporation Maynard, Massachusetts wuly 1973

ACKNOWLEDGEMENTS
Rusty Whitney Oregon Museum of Science and Industry Portland, Oregon
Bob Albrecht People's Computer Company Menlo Park, California
Walt Koetke Lexington High School Lexington, Massachusetts
Charles Lund The American School of the International Schools The Hague, Netherlands
Mary C. Jones Southwest High School POrte Worth, Texas
Victor Nahigian (student) Weston High School Weston, Massachusetts
Keiwit Computation Center Dartmouth College Hanover, New Hampshire
Education and DECsystem-10 Groups Digital Equipment Corporation Maynard, Massachusetts

Illustrations courtesy of:
MAD Magazine
Scott, Foresman & Co.
Bob Barner
Creative Publications Peoples Press
and several other sources.

## The Games....

### ACEYDU
**Description**
This is a simulation of the Acey Ducey card game. In the game, the dealer (the computer) deals two cards face up. You have an option to bet or not to bet depending on whether or not you feel the next card dealt will have a value between the first. two.
Your initial money (Q) is set to $100; you may alter Statement 170 if you want to start with more or less than $100. The game keeps going on until you lose all your money or interrupt the program.

**Program Author**
Bill Palmby Adlai E. Stevenson High School Prairie View, Illinois 60069

### SAMPLE RUN

```
RUNNH
PROGRAM LISTING
CISTNH edhnrn ACEY-CUCEY IS PLAYED IN THE FOLLOWING MANNER: 26 REM +++ GAME OF ACEY-DUCEY WRITTEN 64 BILL PRUMB' THE CEALER “COMPUTER? DEALS TWO CARDS FACE UF
28 REM dr ADLAT STEVENSON HIGH SCHOOL. PRAIRE VIEW. ILL YOU HAVE THE OPTION TO BET OR NOT TO GET DEPENDING Sec NaI MAS UI I SRS esha taller ice cull ON WHETHER OR NOT YOU FEEL THE NEXT CARO WILL HAYE Ho R OMI ZE HS i a4 BRING HEE Y-DUCEY 1S PLAYED IN THE FOLLOWING MANNER: ® A VALUE BETWEEN THE FIRST TWO 492 PRINT "THE DEALER (COMPLITER) DEALS TWO CARDS FACE UP." 83 PRINT "YOU HAYE THE OPTION Ti EET OR NOT To BET GEFENDING" PRINT "ON WHETHER OR NOT YO! FEEL THE NEXT CARD WILL HAYE"\nIF YOU DO NOT WANT TO BET. INFUT AG,\nVOU NOW HAVE 168 DOLLARS\nPRINT "A YALUE BETWEEN THE FIRST Tw\nMe PRINT "IF YOU CO NOT WANT TO GET. INPUT A ow, "\nPRINT\nN=180 > Q=1048\nPRINT “YOU NOW HAYE"@"DOLLARS. " PRINT ooTo 2\n196\ngato\nR=INTC144#RND +2 3\nB=INTC14#RNDO +2 IF &<2 THEN a8 IF B>i¢ IF AD>=B ine i IF\na)\nPRINT "JACK" GoTo 5a PRINT BOTO See PRINT "KING" GOTO See PRINT "ACE"\n41 THEN 554 THEN THEN THEN THEN 62\nEES GOB is\nWEEN"\na2ftdih one\nFSGHAGM aT eaanaae\nVan + MWh Re om oy\nGOTO 656 PRINT “JRGEK" GOTO 654 PRINT "GUEEN" 50TO 656 PRINT "KING" GOTO 656 PRINT "ACE" PRINT\nINPUT "WHAT IF M<>8 THEN 6 PRINT "CHICKEN! !"- PRINT GOTO 2668\nIF M<=G@ THEN 736\naa\nYOUR BET"s M4 a\nBABAAABAHMHUKUY SAN OW MR eo oo ms\nPV OO GDeHanaoas\noy =\nSOTO 65a C=INTCAd4+RND D+ IF C<2 THEN\nIF THEN 5 ids THEN 314 IF 1 THEN LS) ie 2 THEN 4 IF = THEN S78 IF THEN #948\nPRINT ©\nGOTO 346\nB PRINT "JACK"\n846 GOTO 346\n854 PRINT "GUEEN"\n368 GOTO 944\n874 PRINT "KING"\n885 60TO 344\n8965 PRINT "ACE"\n914 IF C>A THEN 324\n926 GOTO 374\n936 IF C>=B THEN 376\n956 PRINT "YOU WINtHI8\n966 GOTO 246\n970 PRINT "SORRY. YoU Lose. "\n938 IF MS THEN 244\n16696 PRINT\n1616 PRINT "SORRY. FRIEND. BUT You BLEW 1926 INPUT "TRY AGAIN <YES oR NO) "5 AS A826 IF AS="YES" THEN 144\n1955 END\nREADY\nPRINT "HERE ARE SOUR NEXT TWO CARDS. .\n”\nPRINT "SORRY. MY FRIEND. BUT SOU BET TOO Much" PRINT "SOU HAVE ONLY" O"DOLLARS To BET, "\nSOUR WAC. *\nPRINT:PRINT "C.K. HOPE SU) HAD FLINT) ®\n14\nHERE ARE YOUR NEXT TWO CRROS. . 6\n169\nWHAT IS YOUR BET? 16\n6\nSORRY. YOU LOSE\nYOU NOW HAVE 38 COLLARS\nHERE ARE YOUR NEXT TWO CAROS... 6\nRUEEN\nWHAT I5 YOUR BET? 2H\nJACK\nYOU WIN!!!\nOU NOW HAYE 114 DOLLARS HERE ARE YOUR NEXT THO CARDS 169\nKING\nWHAT 15 YOUR BET? CHICKEN! !\nH\nmm\nRE ARE YOUR NEXT TWO CARDS. .\nLo fo\nWHAT IS YOUR BET? 24 168 SORRY. YOU LOSE YOU NOW HPVE 38 DOLLARS HERE ARE YOUR NEXT TWO CARDS. .\nco\nWHAT I5 YOUR BET? 26\nSORRY, You LOSE\nYOU NOW HAVE 64 DOLLARS\nHERE ARE YOUR NEXT THO CARDS. . 3\nRUEEN\nWHAT I5 YOUR BET? CHICKEN! !\nHERE ARE YOUR NEXT TWO CAROS\neh\nWHAT I5 YOUR BET? @ CHICKEN! !\nHERE ARE YOUR NEXT TWO CARDS\n16\nWHAT IS YOUR BET? CHICKEN! !\nHERE ARE YOUR NEXT TWO CARDS\nRCE\nWHAT I5 YOUR BET? 244 SORRY. MY FRIEND. BUT You BET Ton MUCH YOU HAVE ONLY 68 DOLLARS To BET\nWHAT 15 YOUR BET? 64 5 YOU WIN! YOU NOW HAVE 126 COLLARS. HERE ARE YOUR NEXT TWO CARDS. . 5 g\nMHAT I5 YOUR BET? 2a ? SORRY. YOU LOSE YOU NOW HAVE 194 DOLLAR HERE ARE YOUR NEXT TWO CARDS\nco |,\nWHAT IS YQUR BET? 30 16 SORRY, YOU LOSE YOU NOW HAVE 16 DOLLARS\nWHAT IS YOUR BET? 16 QUEEN SORRY, YOU LOSE.\nSORRY. FRIEND, BUT You BLEW YOUR WAC TRY AGAIN ¢YES OR NOD? NO\nO.K. HOPE YOU HAD FUN!
```

### AMAZIN
**Description**
This program will print out a different maze every time it is run and guarantees only one path through. You can choose the dimensions of the maze--i.e. the number of squares wide and long.
**Computer Limitations**
The amount of memory available will determine the maximum size maze that may be constructed. An 8K EduSystem 20 initialized £o0r one user can draw a 13x13 maze. *RSTS/E can draw a 23 (width of paper limit) x 50 maze, even larger uSing virtual memory. Experiment on your system with the maze dimensions in Statement 110.
**Program Author**
Jack Hauber Loomis School Winasor, Cr 06095

### PROGRAM LISTING
```
35 694 LET G=1\nUSYSTEM SY ee ue 692 GO To $30\nDOMI2 708 IF WKR,S+1)<>6 THEN 734 a SEE Bere 746 LET X=INTCRND(B)#2+4) 426 PRINT "WHAT ARE YOUR WICTH ANC LENGTH?" 728 IF X=1 THEN S68\n421 INPUT H,Y Ret IP kc Hen Se TZSVERENT 736 GO TO 866 ‘\n41236 IF H<>4 THEN 158 740 IF S<>¥ THEN 766\nUS ES Me THEN 154 756 IF 2=14 THEN 736\n132 PRINT “MEANINGLESS DIMENSIONS, TRY AGAIN” (st LET @=4\n144 PRINT 752 GO TO 774 I d41 G0 To 126 766 IF NCR, S+42<>8 THEN 736 156 PRINT 776 GO TO 914\n50 TO 1646\n454 PRINT LET WCR-41,S5)=€\n166 LET =\n16t LET 2=8 LET €=C+4\n162 LET X=INTCRNO(G)+#H+1) LET V¢CR-41, S9=2\n163 FOR I=4 TO H LET R=R-14\n78 TE T=% THEN 473 IF C=H*¥+1 THEN 1614\nER PRN tuba ONS LET @=4\n4172 GO TO 184 GO TO 266\nA IPRUNT Ones. ahs LET WOR, S-1)=\n166 NEXT I CET €=cC+4\nLOO TP RINT EET WCRS S=s S21\ni397 Cer e=2 LET S=s-4\n192 IF C=H*¥+41 THEN 1446 LET @=6\nGo TO 266\nLET WCR+4,. S9=0 LET C=cC+1\nIF ¥CR.5)=6 THEN 338 LET ¥CR,5)=\nGO TO $336 LET ¥CR, S2=2\nLET R=R+4\nIF C=H*#¥+1 THEN 1616 60 TO 524\nIF @=4 THEN 366\nLET WOR, S+49=C\n5 =@ THEN 214 PET €=c+4\n26@ IF R @ THEN Sse IF ¥CR,S52=@ THEN 944\n264 IF WeR-41,.59¢>8 THEN Sia 930 LET ¥¢R.S)=2\nEa olemee tee =68 THEN 394 931 60 TO 954\n236 IF WER,S-1)¢>@ THEN 29a 946 LET VCR, S)=4\n296 IF R=H THEN a 956 LET S=S+4\n308 IF WCR+4,5)<5@ THEN 230 954 IF C=H+*V¥+4 THEN 1414 LET S=INTOCRNO CA) # E44) 952 GO TO 266\n960 LET 2=4 970 IF YER, 974 LET YER, S) nie 972 LET g=6\n72 60 TO 1406 986 LET VCR, 5)=4 981 LET @=6 >&@ THEN 374 982 LET R=4 356 LET X= INTCRND CB) *244) 996 LET S=4 368 IF X=41 THEN ?: 991 GO TO 256 5 ; THEN 1469 GO TO 216 THEN a 1416 FOR J=4 To ¥ INTORND(G) #244) 1011 PRINT" IMs THEN 7? 1412 FOR I=1 TO H THEN 820 1913 IF ¥¢1.J 396 IF R= H THEN 474 1626 PRINT" 406 IF WOR+1,5)9<>6 THEN 474 1621 G0 TO 14448 401 IF S<>Vv THEN 4248 DUSGCR RENT" oT)"; 416 IF 2=4 THEN 456 14646 NEXT I 444 LET Rad 1444 PRINT 442 60 TO 436 s 1642 FOR I=4 TO H 426 IF WOR, St4 <> THEN 454 1045 IF Vcr,\nINTE RNG\n1959 IF Wer. J) 1854 PRINT": 1852 GO TO 1976 4869 PRINT "--~-"; 1878 NEXT I\nTHEN THEN INTY RNG\nTHEN 7? 4071 PRINT": ® THEN ¢ 1972 NEXT J THEN 43 4873 END THEN 431 LET R24 432 G0 TO Soa 498 IF WOR, $449<> 586 LET X=INTCRN 519 IF THEN 541 IF ¥=2 THEN 528 80 10 798 530 IF S-1=9 THEN 670 54@ IF WCR,S-1)<30 THEN 676 544 IF R=H THEN SAMPLE RUN S42 1F WCR+4,5)<>4 THEN 616 558 IF S<>¥v THEN Sea B54 (ced THEN See AMAZIN EDUSYSTEM 2a 552 LET @=4 552 G0 To S70 WHAT ARE YOUR WIDTH AND LENGTH? 566 IF NCR. 5+4)¢>0 THEN Soa 2907 578 LET X=INTCRND(B) #244) 520 IF X=4 THEN 22 % 6 : EA a A alr aE Bel ke ; 1 Toel I I 2 5 eae eae ¥ F ie al et 4 I I 518 >Y THEN 6 = ina 620 IF 2=4 THEN 6ea IT HE Sih oll I 624 LET @=4 ne oa Varn ok en ind oe ae Cs 622 GO TO 640 aa I I 636 IF WOR, S+1)<>G THEN 66a Sean a pop Oe ie We 64 LET X=INTCRND(B) 4244) I I u ye 654 IF X=4 THEN s2a SL ier bk May ee aw Io 654 IF X=2 THEN 910 Ee I I I 564 60 TO 82a ot SS MME Reema Pleas an 678 IF R=H THEN 740 See eee «ike OLY Silene Le! 686 IF WCR+1,5)<>6 THEN 746 Derg Se eer cera ag, Pe 684 IF S<>¥ THEN 7a40 698 IF 2=1 THEN 72a READY
```

### ANIMAL
**Description**
Unlike other computer games in which the computer picks a number or letter and you must guess what it is, in this game you think of an animal and the computer asks you questions and tries to guess the name of your animal. If the computer, guesses incorrectly, it will ask you for a question that differentiates the animal it guessed from the One you were thinking of. In this way the computer "learns" new animals. Questions to differentiate new animals should be input without a question mark.
IMPORTANT: At the end of a playing session, to the question, "ARE YOU THINKING OF AN ANIMAL," you must respond "SAVE" in order that the computer save all the new animals you have introduced. To that same question, at any point in the game, if you respond "LIST," the computer will tell you all the animals it knows so far.
The program starts originally by knowing only "FISH" and "BIRD." Additional animals are stored in the file "ANIMAL.GME,."

**Computer Limitations**
This program was written for a DIGITAL RSTS-1l1 and uses several unique features, in particular, multiple user access to a common data file and several advanced string handling functions. It has been converted with some minor changes to OS/8 BASIC and could be adapted to other systems as well.

**Program Author**
Nathan Teichholtz Digital Equipment Corporation Maynard, MA 01754

### PROGRAM LISTING
```
190\n15a 5289 525\n558\nCREATED @6=APR=73 04144 PM "PLAY \'GUESS THE ANIMAL! WITH RSTS te THINK OF aN ANIMAL AND THE COMPUTER WILL TRY TO GUESS IT.eo"28 DIM A$(2g0) FSe"ANIMAL GME"\ntON ERROR GOTO 700 OPEN FS FOR INPUT AS FILE 1%\ntINPUT #1%)N%\nHINPUT wi,Ag(Ix) FOR Ixei1xTO Nx\ntCLOSE 4%\n2A$(O%) eNUMS$ (NZ)\nON ERROR GOTO @\nsGOTO 1300\n708 ON ERROR GOTO 1052\n1050 1120 1300\n1310\n1322\n1352@ 1400\n145\n2080 2050\n2100\n2200\n2500 3000\n9999\ntFSa"Suyrs TRESUME 559 READ ASC(I%) FOR 1%e8X% TO 3% DATA "4","\\QDOES IT SWIM\\Y2\\N3\\","\\AFISH","\\ABIRD" INPUT "ARE YOU THINKING OF AN ANIMAL"3Z9$ tGoTo 1356 IF LEFTC(Z9$,1x%)e"y" 1GOTO 1300 IF LEFT(Z95,1%)e0Nn IF Z9S=E"SAVE" THEN OPEN "ANIMAL GME" FOR OUTPUT AS FILE 1% HPRINT #1%,A8(1%) FOR 1%eB% TO VALCA$(0%)) tPRINT #1,CHRS (26%) sCLOSE 1% 1GOTO 1300 IF ZoSs"LIST" THEN PRINT "ANIMALS I ALREADY KNOW ARES" tPRINT RIGHTCASCI%)/3X%), IF INSTR(L%/ASCIX),"\\A") FOR T%21% TO 200% tPRINT tGOTO {300 Kxe1x KXBFNAXCAS(K%)) $GOTO 3000 IF LENCAS (Kx) ) 80x #GOTO 4499 IF LEFT CAS(K%) , 2%) a" \\Qu tPRINT "IS IT a "RIGHTCASC(KX) »3%)9 sINPUT Z7$ tZ7$8LEFT(Z27$,1%) IF Z7ga"¥" THEN PRINT "WHY NOT TRY ANOTHER ANIMAL" 1GOTO 1300 INPUT "THE ANIMAL YOU WERE THINKING OF WAS A "VZ9$\nPRINT "PLEASE TYPE IN A QUESTION THAT WOULD DISTINGUISH A " Z9o$ " FROM A "RIGHT(AS(K%),3%) tINPUT 785\nPRINT "FOR A "Z9S" THE ANSWER WOULD BE") fINPUT 275\n§Z7$2LEFT(Z7$,1%) tTF Z7Se"y" THEN Z6Setyn ELSE IF Z7g2nNw ELSE PRINT tGOTO 2100 Zi%eVAL(AS(O%)) 1A$ (2%) SNUMS(Z1%42%) ASC 71%) BAS(KK) PAS (ZIX+1 KX) BINAT4Z9OS TASC KK) BN\\QUHZESH"\\"4Z7S4NUMS(ZIZ4F1%) + "\\"HZGERENUMB(ZIXDHNAN GOTO 1{3a¢@ DEF FNAX%(Q$) tPRINT HIDCQS&,3%, INSTR(3%,9$,"\\" 03%) ) tINPUT Z9$ tZ9SBLEFT(Z9$,1%) tZ9gE"N" ITF ZOgcrnyn tZ1%EINSTRO3%X%, OS, "\\"479$) 42% §Z2KB8INSTRIZ1% + QS,"\\") tFNA%MVAL (MID (98, 21%, Z2%=Z1%)) tFNEND END\nTHEN Z6ganyu\n"PLEASE ANSWER \'YES\' OR \'NQI"\n
```