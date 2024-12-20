# Документация модуля

## Обзор

Этот модуль содержит набор функций и классов, предназначенных для работы с веб-страницами и браузерами в контексте автоматизированного тестирования с использованием Selenium WebDriver. В основном, он занимается управлением различными аспектами браузера, включая настройки профиля, взаимодействия со страницей и обработку ошибок.

## Содержание

1. [Функции](#Функции)
2. [Классы](#Классы)

## Функции

### `function(sttc)`

**Описание**:
Эта функция представляет собой обертку, которая устанавливает строгий режим (`'use strict'`) для JavaScript. Она инициализирует глобальные объекты и обеспечивает корректную работу с окружением.

**Параметры**:
- `sttc` (object): Объект для инициализации.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `ia(a, b, c)`

**Описание**:
Инициализирует символы для использования в качестве свойств объектов.

**Параметры**:
- `a` (str): Строка с именем символа.
- `b` (function): Функция для вычисления значения символа.
- `c` (str): Строка для указания версии (например, 'es6').

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `ja(a, b)`

**Описание**:
Получает значение флага из `CLOSURE_FLAGS` или возвращает значение по умолчанию.

**Параметры**:
- `a` (str): Строка с именем флага.
- `b` (any): Значение по умолчанию.

**Возвращает**:
- `any`: Значение флага или значение по умолчанию.

### `ka(a)`

**Описание**:
Получает значение объекта из вложенной структуры или возвращает `null`, если путь не существует.

**Параметры**:
- `a` (str): Строка с путем через точку.

**Возвращает**:
- `any | null`: Значение объекта или `null`.

### `la(a)`

**Описание**:
Проверяет, является ли значение объектом или функцией.

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `bool`: `True`, если объект или функция, иначе `False`.

### `ma(a)`

**Описание**:
Возвращает уникальный идентификатор объекта.

**Параметры**:
- `a` (object): Объект, для которого нужно получить идентификатор.

**Возвращает**:
- `int`: Уникальный идентификатор.

### `pa(a, b, c)`

**Описание**:
Вызывает функцию `bind` как функцию.

**Параметры**:
- `a` (function): Функция для привязки.
- `b` (object): Контекст `this` для привязки.
- `c` (any, optional): Дополнительные аргументы для привязки.

**Возвращает**:
- `function`: Привязанная функция.

### `qa(a, b, c)`

**Описание**:
Создает замыкание для функции, которая вызывается с определенным контекстом и аргументами.

**Параметры**:
- `a` (function): Функция, для которой нужно создать замыкание.
- `b` (object): Контекст `this` для вызова.
- `c` (any, optional): Дополнительные аргументы для вызова.

**Возвращает**:
- `function`: Замыкание функции.

### `ra(a, b, c)`

**Описание**:
Функция `bind`  если `bind` доступен, иначе вызывает `qa`.

**Параметры**:
- `a` (function): Функция для привязки.
- `b` (object): Контекст `this` для привязки.
- `c` (any, optional): Дополнительные аргументы для привязки.

**Возвращает**:
- `function`: Привязанная функция.

### `sa(a, b)`

**Описание**:
Создает функцию, которая вызывает исходную функцию с добавленными аргументами.

**Параметры**:
- `a` (function): Исходная функция.
- `b` (any, optional): Дополнительные аргументы.

**Возвращает**:
- `function`: Новая функция.

### `ta(a, b, c)`

**Описание**:
Создает путь к свойству объекта.

**Параметры**:
- `a` (str): Путь к свойству объекта, разделенный точками.
- `b` (any): Значение для установки.
- `c` (object): Объект, в котором устанавливается путь.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `ua(a)`

**Описание**:
Возвращает аргумент без изменений.

**Параметры**:
- `a` (any): Аргумент.

**Возвращает**:
- `any`: Тот же аргумент.

### `wa(a)`

**Описание**:
Использует `setTimeout` для выбрасывания ошибки.

**Параметры**:
- `a` (Error): Ошибка для выбрасывания.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `xa(a)`

**Описание**:
Убирает пробелы и специальные символы в начале и конце строки.

**Параметры**:
- `a` (str): Строка для обработки.

**Возвращает**:
- `str`: Строка без пробелов и специальных символов в начале и конце.

### `ya(a, b)`

**Описание**:
Сравнивает две строки с учетом числовых и нечисловых частей.

**Параметры**:
- `a` (str): Первая строка.
- `b` (str): Вторая строка.

**Возвращает**:
- `int`: Результат сравнения (-1, 0, 1).

### `za(a, b)`

**Описание**:
Сравнивает два числа или две строки.

**Параметры**:
- `a` (number | str): Первое значение.
- `b` (number | str): Второе значение.

**Возвращает**:
- `int`: Результат сравнения (-1, 0, 1).

### `Oa(a)`

**Описание**:
Создает функцию, которая возвращает значение из объекта на основе поиска ключа.

**Параметры**:
- `a` (Array): Массив пар ключ-значение.

**Возвращает**:
- `function`: Функция, возвращающая значение на основе ключа.

### `Pa()`

**Описание**:
Получает версию браузера на основе UserAgent.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `str`: Строка с версией браузера.

### `Qa(a, b)`

**Описание**:
Ищет подстроку в строке или возвращает индекс в массиве.

**Параметры**:
- `a` (str | Array): Строка или массив для поиска.
- `b` (str | any): Подстрока или элемент для поиска.

**Возвращает**:
- `int`: Индекс подстроки или элемента, или -1, если не найдено.

### `Ra(a, b)`

**Описание**:
Фильтрует элементы массива с помощью callback-функции.

**Параметры**:
- `a` (Array): Массив для фильтрации.
- `b` (function): Функция для фильтрации.

**Возвращает**:
- `Array`: Отфильтрованный массив.

### `Sa(a, b)`

**Описание**:
Создает новый массив, применяя callback к каждому элементу.

**Параметры**:
- `a` (Array): Исходный массив.
- `b` (function): Функция для преобразования элементов.

**Возвращает**:
- `Array`: Новый массив с преобразованными элементами.

### `Ta(a, b)`

**Описание**:
Проверяет, существует ли элемент в массиве с помощью callback.

**Параметры**:
- `a` (Array): Исходный массив.
- `b` (function): Функция для проверки.

**Возвращает**:
- `bool`: `True`, если условие выполняется хотя бы для одного элемента, иначе `False`.

### `Ua(a, b)`

**Описание**:
Ищет первый элемент, удовлетворяющий условию callback, начиная с конца массива.

**Параметры**:
- `a` (Array): Исходный массив.
- `b` (function): Функция для проверки.

**Возвращает**:
- `any | null`: Первый найденный элемент или `null`, если не найдено.

### `Va(a, b)`

**Описание**:
Проверяет, содержит ли массив элемент.

**Параметры**:
- `a` (Array): Исходный массив.
- `b` (any): Элемент для поиска.

**Возвращает**:
- `bool`: `True`, если элемент найден, иначе `False`.

### `Wa(a)`

**Описание**:
Копирует массив.

**Параметры**:
- `a` (Array): Исходный массив.

**Возвращает**:
- `Array`: Копия массива.

### `Xa(a)`

**Описание**:
Функция-пустышка. Возвращает полученный аргумент.

**Параметры**:
- `a` (any): Аргумент.

**Возвращает**:
- `any`: Тот же аргумент.

### `ab(a)`

**Описание**:
Декодирует строку base64 в массив байтов.

**Параметры**:
- `a` (str): Строка base64.

**Возвращает**:
- `Array`: Массив байтов.

### `bb(a, b)`

**Описание**:
Декодирует строку base64 и применяет callback к каждому байту.

**Параметры**:
- `a` (str): Строка base64.
- `b` (function): Функция для вызова на каждый байт.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `fb(a)`

**Описание**:
Разбивает число на 2 32-битных числа.

**Параметры**:
- `a` (number): Число для преобразования.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `hb(a)`

**Описание**:
Устанавливает внутренние свойства для работы с 64-битными числами.

**Параметры**:
- `a` (number): Число для преобразования.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `jb()`

**Описание**:
Возвращает строку 64-битного числа.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `str`: Строка, представляющая 64-битное число.

### `kb(a)`

**Описание**:
Преобразует `arguments` в массив.

**Параметры**:
- `a` (arguments): `arguments`.

**Возвращает**:
- `Array`: Массив с аргументами.

### `pb(a)`

**Описание**:
Устанавливает флаг на объекте.

**Параметры**:
- `a` (object): Объект, в котором нужно установить флаг.

**Возвращает**:
- `object`: Тот же объект.

### `qb(a, b)`

**Описание**:
Устанавливает флаг на объекте с маской.

**Параметры**:
- `a` (number): Маска.
- `b` (object): Объект, в котором нужно установить флаг.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `rb(a, b)`

**Описание**:
Устанавливает флаг на объекте с маской.

**Параметры**:
- `a` (number): Маска.
- `b` (object): Объект, в котором нужно установить флаг.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `ub(a)`

**Описание**:
Проверяет, является ли объект объектом с определенным свойством `g`.

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `bool`: `True`, если объект, иначе `False`.

### `vb(a)`

**Описание**:
Проверяет, является ли значение обычным объектом (`{}`).

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `bool`: `True`, если обычный объект, иначе `False`.

### `wb(a, b, c)`

**Описание**:
Устанавливает флаг на массив, если он пуст и удовлетворяет условию.

**Параметры**:
- `a` (Array): Массив.
- `b` (Array | Set): Набор данных для сравнения.
- `c` (any): Элемент для проверки.

**Возвращает**:
- `bool`: `True`, если массив модифицирован, иначе `False`.

### `zb(a)`

**Описание**:
Выбрасывает ошибку, если установлен определенный флаг.

**Параметры**:
- `a` (number): Флаг для проверки.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `Cb(a, b)`

**Описание**:
Устанавливает контекст для ошибки.

**Параметры**:
- `a` (Error): Объект ошибки.
- `b` (string): Строка с уровнем ошибки.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `Fb(a)`

**Описание**:
Устанавливает callback-функцию, которая вызывается в `setTimeout`.

**Параметры**:
- `a` (function): Callback.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `Gb(a)`

**Описание**:
Вызывает установленную callback-функцию для обработки ошибки.

**Параметры**:
- `a` (Error): Объект ошибки.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `Hb()`

**Описание**:
Создает и выбрасывает `Error` и устанавливает ему контекст "incident".

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `Ib(a)`

**Описание**:
Создает `Error` с контекстом "warning" и выводит его.

**Параметры**:
- `a` (string): Сообщение об ошибке.

**Возвращает**:
- `Error`: Объект ошибки.

### `Jb(a)`

**Описание**:
Проверяет, является ли значение булевым.

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `bool`: Значение.

**Вызывает исключения**:
- `Error`: если значение не является булевым.

### `Lb(a)`

**Описание**:
Проверяет, является ли значение строкой, содержащей число, или числом.

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `bool`: True, если строка с числом или число, иначе False.

### `w(a)`

**Описание**:
Преобразует число в целочисленное.

**Параметры**:
- `a` (number): Число для преобразования.

**Возвращает**:
- `int`: Целочисленное значение.

**Вызывает исключения**:
- `Ib`: если не является конечным числом.

### `Mb(a)`

**Описание**:
Преобразует значение в целое число. Возвращает `void` или `null`, если невозможно.

**Параметры**:
- `a` (any): Значение для преобразования.

**Возвращает**:
- `int | void`: Целочисленное значение или `undefined`.

### `Nb(a)`

**Описание**:
Проверяет, является ли значение 32-битным целым числом.

**Параметры**:
- `a` (number): Значение для проверки.

**Возвращает**:
- `int`: 32-битное целое число.

**Вызывает исключения**:
- `Ib`: если значение не является 32-битным целым числом.

### `Ob(a)`

**Описание**:
Преобразует значение в 32-битное целое число или возвращает `null`.

**Параметры**:
- `a` (any): Значение для преобразования.

**Возвращает**:
- `int | null`: 32-битное целое число или null.

### `Pb(a)`

**Описание**:
Преобразует строку или число в 32-битное целое число или возвращает `undefined`.

**Параметры**:
- `a` (string | number): Значение для преобразования.

**Возвращает**:
- `int | void`: 32-битное целое число или `undefined`.

### `Qb(a)`

**Описание**:
Преобразует строку или число в беззнаковое 32-битное целое число или возвращает `undefined`.

**Параметры**:
- `a` (string | number): Значение для преобразования.

**Возвращает**:
- `int | void`: Беззнаковое 32-битное целое число или `undefined`.

### `Rb(a)`

**Описание**:
Проверяет, может ли строка быть целым числом.

**Параметры**:
- `a` (str): Строка для проверки.

**Возвращает**:
- `bool`: `True`, если строка является корректным числом, иначе `False`.

### `Sb(a)`

**Описание**:
Преобразует число в 64-битное целое число (с проверкой).

**Параметры**:
- `a` (number): Число для преобразования.

**Возвращает**:
- `number`: 64-битное целое число.

### `Tb(a)`

**Описание**:
Преобразует число в 64-битную строку.

**Параметры**:
- `a` (number): Число для преобразования.

**Возвращает**:
- `str`: Строка 64-битного числа.

### `Ub(a)`

**Описание**:
Преобразует строку в 64-битное целое число.

**Параметры**:
- `a` (str): Строка для преобразования.

**Возвращает**:
- `str`: Строка, представляющая 64-битное целое число.

### `Vb(a)`

**Описание**:
Проверяет, является ли значение строкой.

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `str`: Строка.

**Вызывает исключения**:
- `Error`: если значение не является строкой.

### `Wb(a)`

**Описание**:
Проверяет, является ли значение строкой или `null`.

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `str | null`: Строка или `null`.

**Вызывает исключения**:
- `Error`: если значение не является строкой.

### `Xb(a)`

**Описание**:
Проверяет, является ли значение строкой или `null`, или `undefined`.

**Параметры**:
- `a` (any): Значение для проверки.

**Возвращает**:
- `str | void`: Строка или `undefined`.

### `Yb(a, b, c, d)`

**Описание**:
Возвращает объект с типом `b`, если переданный аргумент `a` является массивом, или `undefined` в противном случае.

**Параметры**:
- `a` (any): Значение для проверки.
- `b` (Function): Конструктор объекта.
- `c` (bool, optional): Если True, объект будет создан, если не массив
- `d` (int, optional): Флаг для установки.

**Возвращает**:
- `object | void`: Объект или `undefined`.

### `$b(a)`

**Описание**:
Создает объект с помощью конструктора, кэшируя результат.

**Параметры**:
- `a` (function): Конструктор.

**Возвращает**:
- `object`: Созданный объект.

### `bc(a, b)`

**Описание**:
Создает объект с помощью конструктора и устанавливает контекст.

**Параметры**:
- `a` (function): Конструктор.
- `b` (any): Контекст для конструктора.

**Возвращает**:
- `object`: Созданный объект.

### `cc(a, b)`

**Описание**:
Вызывает `dc`.

**Параметры**:
- `a` (any): Игнорируется.
- `b` (any): Значение для преобразования.

**Возвращает**:
- `any`: результат `dc`.

### `dc(a)`

**Описание**:
Преобразует значение в строку или число (для чисел и boolean)

**Параметры**:
- `a` (any): Значение для преобразования.

**Возвращает**:
- `any`: Строка, число или null.

### `ec(a, b, c)`

**Описание**:
Применяет callback к каждому элементу массива или объекта.

**Параметры**:
- `a` (Array | Object): Массив или объект для обработки.
- `b` (number): Флаги.
- `c` (function): Callback-функция.

**Возвращает**:
- `Array`: Преобразованный массив.

### `fc(a, b, c, d, e)`

**Описание**:
Рекурсивно применяет callback к каждому элементу объекта или массива.

**Параметры**:
- `a` (any): Исходное значение.
- `b` (function): Callback-функция.
- `c` (function, optional): Callback для массивов.
- `d` (bool, optional): Флаг.
- `e` (bool, optional): Флаг.

**Возвращает**:
- `any`: Преобразованное значение.

### `gc(a, b, c, d, e)`

**Описание**:
Применяет callback к элементам массива рекурсивно.

**Параметры**:
- `a` (Array): Исходный массив.
- `b` (function): Callback для преобразования элементов.
- `c` (function, optional): Callback для массива.
- `d` (bool, optional): Флаг для  использования `d` как `bool`.
- `e` (bool, optional): Флаг для преобразования элементов массива.

**Возвращает**:
- `Array`: Преобразованный массив.

### `hc(a)`

**Описание**:
Преобразует объект в JSON.

**Параметры**:
- `a` (any): Значение для преобразования.

**Возвращает**:
- `any`: Значение для JSON.

### `ic(a)`

**Описание**:
Преобразует значение в строку или число.

**Параметры**:
- `a` (any): Значение для преобразования.

**Возвращает**:
- `any`: Строка или число.

### `kc(a, b, c)`

**Описание**:
Клонирует массив, объект или `Uint8Array`.

**Параметры**:
- `a` (any): Значение для клонирования.
- `b` (bool, optional): Флаг для модификации массива.
- `c` (function, optional): Callback-функция.

**Возвращает**:
- `any`: Клон значения.

### `lc(a, b, c)`

**Описание**:
Преобразует массив или объект и устанавливает флаг.

**Параметры**:
- `a` (Array | Object): Массив или объект для преобразования.
- `b` (number): Флаги.
- `c` (bool): Флаг.

**Возвращает**:
- `Array`: Преобразованный массив.

### `mc(a)`

**Описание**:
Возвращает копию объекта с возможностью вызова конструктора.

**Параметры**:
- `a` (any): Объект для получения копии.

**Возвращает**:
- `any`: Копия объекта.

### `nc(a)`

**Описание**:
Создает `Proxy` для объекта.

**Параметры**:
- `a` (object): Объект для создания `Proxy`.

**Возвращает**:
- `object`: `Proxy` объект.

### `pc()`

**Описание**:
Вызывает обработчик ошибок.

**Параметры**:
- `void`: Функция не принимает параметров.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `qc(a, b)`

**Описание**:
Создает связь между объектом и его `Proxy`.

**Параметры**:
- `a` (object): Оригинальный объект.
- `b` (object): `Proxy` объект.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `sc(a, b, c, d)`

**Описание**:
Проверяет, следует ли разрешить запись свойства в объекте.

**Параметры**:
- `a` (object): Объект для записи свойства.
- `b` (number): Флаги.
- `c` (any, optional): Значение свойства.
- `d` (bool, optional): Флаг.

**Возвращает**:
- `bool`: `True`, если запись разрешена, иначе `False`.

### `tc(a, b)`

**Описание**:
Получает свойство объекта.

**Параметры**:
- `a` (object): Объект.
- `b` (any): Ключ свойства.

**Возвращает**:
- `any`: Значение свойства или `null`.

### `vc(a, b, c, d)`

**Описание**:
Получает элемент массива по индексу.

**Параметры**:
- `a` (Array): Исходный массив.
- `b` (number): Флаг.
- `c` (number): Максимальный размер массива.
- `d` (number): Индекс.

**Возвращает**:
- `any | void`: Значение элемента по индексу.

### `uc(a, b, c, d)`

**Описание**:
Получает значение из массива или объекта.

**Параметры**:
- `a` (Array | Object): Массив или объект.
- `b` (number): Флаги.
- `c` (number): Ключ или индекс.
- `d` (bool): Флаг.

**Возвращает**:
- `any | null`: Значение свойства или `null`.

### `y(a, b, c)`

**Описание**:
Устанавливает значение свойства объекта.

**Параметры**:
- `a` (object): Объект для изменения.
- `b` (any): Ключ свойства.
- `c` (any): Значение свойства.

**Возвращает**:
- `object`: Модифицированный объект.

### `z(a, b, c, d, e)`

**Описание**:
Устанавливает значение в массиве или объекте.

**Параметры**:
- `a` (Array | Object): Массив или объект.
- `b` (number): Флаги.
- `c` (number): Ключ или индекс.
- `d` (any, optional): Значение свойства.
- `e` (bool, optional): Флаг.

**Возвращает**:
- `number`: Флаги.

### `wc(a, b, c)`

**Описание**:
Проверяет, есть ли у объекта свойство.

**Параметры**:
- `a` (any): Объект для проверки.
- `b` (object): Объект для проверки.
- `c` (number): Ключ или индекс.

**Возвращает**:
- `bool`: `True`, если свойство есть, иначе `False`.

### `A(a)`

**Описание**:
Возвращает константу 2 или 5 (с условием).

**Параметры**:
- `a` (object): Объект для проверки.

**Возвращает**:
- `number`: 2 или 5.

### `yc(a, b, c, d)`

**Описание**:
Возвращает новый объект на основе переданного.

**Параметры**:
- `a` (object): Объект для обработки.
- `b` (number): ключ в объекте.
- `c` (function): Callback функция.
- `d` (int): Тип

**Возвращает**:
- `object`: Новый объект.

### `zc(a, b, c)`

**Описание**:
Получает массив или объект из объекта.

**Параметры**:
- `a` (Array | Object): Объект.
- `b` (number): Флаги.
- `c` (number): Ключ или индекс.

**Возвращает**:
- `any`:  массив или `xb`.

### `Bc(a, b)`

**Описание**:
Устанавливает флаг на число.

**Параметры**:
- `a` (number): Число для установки флага.
- `b` (number): Флаги.

**Возвращает**:
- `number`: Число с установленным флагом.

### `Cc(a)`

**Описание**:
Проверяет, является ли значение объектом.

**Параметры**:
- `a` (number): Значение для проверки.

**Возвращает**:
- `bool`: `True` если объект, иначе `False`.

### `Ec(a, b, c, d)`

**Описание**:
Устанавливает значение в массив или объект.

**Параметры**:
- `a` (object): Объект для установки значения.
- `b` (number): Ключ или индекс.
- `c` (any, optional): Значение для установки.
- `d` (function): Callback-функция для установки значения.

**Возвращает**:
- `object`: Модифицированный объект.

### `B(a, b, c, d)`

**Описание**:
Устанавливает значение в объекте.

**Параметры**:
- `a` (object): Объект для изменения.
- `b` (any): Ключ свойства.
- `c` (any): Значение свойства.
- `d` (string): Строка для проверки на равенство

**Возвращает**:
- `object`: Модифицированный объект.

### `Fc(a, b)`

**Описание**:
Добавляет элементы в массив или объект.

**Параметры**:
- `a` (object): Объект для изменения.
- `b` (Array | Object): Элементы для добавления.

**Возвращает**:
- `void`: Функция ничего не возвращает явно.

### `Gc(a, b, c, d)`

**Описание**:
Устанавливает значения в Map.

**Параметры**:
- `a` (object): Объект для установки.
- `b` (number): Значение, которое ищется в Map
- `c` (Map): Map.
- `d` (any, optional): Значение для установки.

**Возвращает**:
- `object`: Модифицированный объект.

### `Jc(a, b, c)`

**Описание**:
Ищет значение в Map или возвращает -1.

**Параметры**:
- `a` (object): Объект для поиска.
- `b` (any): Значение для поиска.
- `c` (Map): Map.

**Возвращает**:
- `any`: Значение из Map или -1.

### `Kc(a, b)`

**Описание**:
Ищет значение в Map.

**Параметры**:
- `a` (object): Объект для поиска.
- `b` (Map): Map для поиска.

**Возвращает**:
- `any`: Значение из Map или `null`.

### `Hc(a)`

**Описание**:
Возвращает `Map` для объекта.

**Параметры**:
- `a` (object): Объект.

**Возвращает**:
- `Map`: Map.

### `Ic(a, b, c, d)`

**Описание**:
Ищет значение в Map.

**Параметры**:
- `a` (Map): Map для поиска.
- `b` (Array | Object): Массив или объект.
- `c` (number): Флаг.
- `d` (number): ключ в Map.

**Возвращает**:
- `any`: Значение из Map или 0.

### `Lc(a, b, c)`

**Описание**:
Возвращает свойство объекта.

**Параметры**:
- `a` (object): Исходный объект.
- `b` (function): Конструктор.
- `c` (number): Ключ или индекс.

**Возвращает**:
- `any`: Полученное свойство.

### `xc(a, b, c, d)`

**Описание**:
Возвращает свойство объекта, устанавливая значение, если найдено.

**Параметры**:
- `a` (object): Исходный объект.
- `b` (function): Конструктор.
- `c` (number): Ключ или индекс.
- `d` (bool): Флаг.

**Возвращает**:
- `any`: Свойство или `null`.

### `Mc(a)`

**Описание**:
Возвращает значение свойства объекта.

**Параметры**:
- `a` (object): Объект для извлечения свойства.

**Возвращает**:
- `any`: Значение свойства.

### `D(a, b, c)`

**Описание**:
Возвращает свойство объекта, если оно не равно `null`.

**Параметры**:
- `a` (object): Исходный объект.
- `b` (object): Конструктор.
- `c` (number): Ключ или индекс.

**Возвращает**:
- `any | null`: Свойство или `null`.

### `E(a, b, c, d)`

**Описание**:
Возвращает массив элементов, соответствующих условию.

**Па