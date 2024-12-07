# Код для создания описания рекламной кампании AliExpress

```
your role: `promo_creater`
I send you the category name, a list of product titles, and the language to use. You need to return a dictionary where the key is the category name, and the values are dictionaries with the keys `category_name`, `title`, and `description`.
`category_name` should be equal to the category name.
`title` should summarize `products_titles` and have a length of up to 50 characters.
`description` Create a note for housewives based on the names of products. Use products to diversify the note. The length should not exceed 1200 characters.
A note ас from a household calendar is called a calendar note or calendar entry. In traditional calendars, especially household or tear-off ones, such notes contain various useful tips, information about events, historical facts, folk signs, astrological forecasts or useful household recommendations for each day.
Use the language defined in `language`. Output forrmat: `JSON`

Example input:
language = "RU"
category_name = "liitokala_18650"
products_titles = [Зарядное устройство LiitoKala Lii-M4S-M4 для аккумуляторных батарей, 3,7 в, 18650, 26650, 21700, 18500, литий-ионный, 1,2 в, Ni-MH, AA, испытательная Емкость
LiitoKala Lii-S12 Lii-D4XL-Lii S8 LCD 21700 18650 3,7 V Li-Ion 3,2 V LiFePO4 1,2 V NiMH/Cd 26650 32700 D AA AAA 9V зарядное устройство
LiitoKala Lii-S12 Lii-S8 Lii-PD4 Lii-PD2 Lii-500S 3,7 V 18650 18350 зарядное устройство для аккумуляторов с автоматическим определение полярности 26650 21700 1,2 V AA AAA
LiitoKala Lii-M4 18650 Зарядное устройство с ЖК-дисплеем Универсальное смарт-зарядное устройство Тестовая емкость 26650 18650 21700 AA AAA Батарея 4 слота 5V 2A
Умное зарядное устройство с ЖК-дисплеем, 18650 в, 3,7, 26650, 18350, 21700 в, 4 слота
Liitokala Lii-202 Lii-402 1,2 В 3,7 В 3,2 В 3,85 В 18650 18350 26650 18490 AA AAA 14500 21700 Интеллектуальное зарядное устройство для литиевых Ni-MH аккумуляторов
Аккумуляторное зарядное устройство Liitokala для 18650 3,7 V 9V 26650 18350 16340 18500 14500 1,2 V AA AAA
Зарядное устройство LiitoKala для батарей li-ion 3,7 V и NiMH 1,2 V, подходит для батарей 18650 26650 21700 26700 AA AAA 12V5A
LiitoKala Lii-D4 21700 для 18650 18350 26650 16340 RCR123 14500 3,7 v 1,2 V Ni-MH/Cd, зарядное устройство AA AAA SC D C
Зарядное устройство LiitoKala для аккумуляторов 3,7 в 1,2 в 18650 26650 21700 14500 18350 AA AAA A C и других батарей.
OPUS BT-C3100 4 слота умное Универсальное зарядное устройство адаптер для перезаряжаемых литий-ионных батарей NiCd NiMH AA AAA 10440 18650
Зарядное устройство LiitoKala для Li-Ion LiFePO4 Ni-MH Ni-Cd батарей с ЖК-дисплеем 9 В 21700 20700 26650 18350 RCR123 18650
Умное зарядное устройство LiitoKala Lii-M4S + U1 18650 с ЖК-дисплеем для батарей 26650 21700 32650 18500 20700 CR123A AA AAA
Зарядное устройство Liitokala Lii-PD2 18650, 3,7 в 26650 18350 16340 18500 14500 1,2 в Ni-MH AA AAA LCD многофункциональное зарядное устройство
Зарядное устройство LiitoKala Lii-PD2 для литиевых и NiMH батарей 18650, 26650, 21700, AA, AAA, 18350 в, 3,7 в
Зарядное устройство LiitoKala для аккумуляторов AA AAA 10440 14500 16340 17335 17500 18490 17670

]
```

## <algorithm>

**Шаг 1:** Принимаем на вход `category_name`, `products_titles`, и `language`.

**Шаг 2:** Формируем `title` из `products_titles`.  Сводка должна содержать существенные слова из названий продуктов.  Например, "Зарядные устройства LiitoKala для аккумуляторов 18650".

**Шаг 3:** Создаем `description`.  Описание должно включать список названий продуктов, написанных в определённом порядке, с упором на пользе для домохозяек.  При этом нужно избегать повторов.  Например, `LiitoKala Lii-M4S-M4` и `LiitoKala Lii-S12` не повторяются, а составляются в список.

**Шаг 4:**  Проверяем, чтобы длина `title` не превышала 50 символов, а `description` не превышала 1200 символов.

**Шаг 5:** Возвращаем словарь с `category_name`, `title`, и `description`.


## <mermaid>

```mermaid
graph TD
    A[Входные данные: category_name, products_titles, language] --> B{Формирование title};
    B --> C[Проверка длины title];
    C -- Длина title <= 50 -- D[Формирование description];
    C -- Длина title > 50 -- E[Ошибка: title слишком длинный];
    D --> F[Проверка длины description];
    F -- Длина description <= 1200 -- G[Возврат результата];
    F -- Длина description > 1200 -- H[Ошибка: description слишком длинный];
    E --> I[Ошибка];
    H --> I;
    I --> J[Конец];
```

## <explanation>

**Импорты:** В данном коде нет импортов, так как это описание функции.  Это фрагмент кода, представляющий собой инструкцию для  программного агента, который должен сгенерировать описание рекламной кампании.

**Классы:** Нет классов.

**Функции:** Отсутствует явное определение функций в представленном фрагменте кода.  Это скорее описание ожидаемого поведения агента.

**Переменные:** Переменные `language`, `category_name`, и `products_titles` представляют собой входные данные для агента. Результатом работы будет словарь.

**Возможные ошибки или области для улучшений:**

* **Неопределенный формат данных:** Не указано, что делать с ошибками в формате входных данных (например, если `products_titles` не является списком).
* **Недостаточно гибкое описание:**  Описание может быть слишком зависимым от конкретных названий продуктов.  Для большей гибкости  лучше было бы использовать более абстрактное описание.
* **Сложность генерации описания:**  Генерация естественного языка, особенно описания, требующего логики и вывода,  — сложная задача.  Можно добавить дополнительные инструкции для агента, чтобы улучшить качество результата.
* **Отсутствие обработки ошибок:**  Код не содержит обработки ошибок, что может привести к аварийному завершению программы, если входные данные не соответствуют ожидаемому формату.

**Взаимосвязи с другими частями проекта:** Данный фрагмент кода скорее относится к функции, которая взаимодействует с системой, генерирующей рекламные тексты или  с API, получающим данные о продуктах.  Связь с другими частями проекта, например, базами данных, определяется логикой программы, в которой эта функция используется.


**Важно:**  Представленный код - это не обычный код на языке программирования. Это инструкция для  программного агента.  Он не исполняется напрямую, а используется для управления его поведением.  Объяснение, алгоритм и диаграмма описывают, как должен работать этот программный агент.