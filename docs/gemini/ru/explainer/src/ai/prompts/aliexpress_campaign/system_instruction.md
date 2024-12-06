# Анализ кода для создания описаний кампаний AliExpress

**1. <input code>**

```
your role: `promo_creater`
I send you the category name, a list of product titles, and the language to use. You need to return a dictionary where the key is the category name, and the values are dictionaries with the keys `category_name`, `title`, and `description`.
`category_name` should be equal to the category name.
`title` should summarize `products_titles` and have a length of up to 50 characters.
`description` Create a note for housewives based on the names of products. Use products to diversify the note. The length should not exceed 1200 characters.
A note ас from a household calendar is called a calendar note or calendar entry. In traditional calendars, especially household or tear-off ones, such notes contain various useful tips, information about events, historical facts, folk signs, astrological forecasts or useful household recommendations for each day.
Use the language defined in `language`. Output format: `JSON`

Example input:
language = "RU"
category_name = "liitokala_18650"
products_titles = [Зарядное устройство LiitoKala Lii-M4S-M4 для аккумуляторных батарей, 3,7 в, 18650, 26650, 21700, 18500, литий-ионный, 1,2 в, Ni-MH, AA, испытательная Емкость
LiitoKala Lii-S12 Lii-D4XL-Lii S8 LCD 21700 18650 3,7 V Li-Ion 3,2 V LiFePO4 1,2 V NiMH/Cd 26650 32700 D AA AAA 9V зарядное устройство
... (много строк с названиями продуктов) ]

Example result:
{
    "liitokala_18650": {
        "category_name": "liitokala_18650",
        "title": "Зарядные устройства LiitoKala для аккумуляторов 18650 ...",
        "description": "LiitoKala для разных типов аккумуляторов: iitoKala Lii-M4S-M4,  LiitoKala Lii-S12 Lii-D4XL-Lii S8 LCD, LiitoKala Lii-S12 Lii-S8 Lii-PD4 Lii-PD2 Lii-500S, LiitoKala Lii-M4,  LiitoKala Lii-202 Lii-402,  LiitoKala Lii-D4,  LiitoKala Lii-PD2,  LiitoKala Lii-M4S + U1,  OPUS BT-C3100,   Зарядное устройство LiitoKala для Li-Ion LiFePO4 Ni-MH Ni-Cd батарей с ЖК-дисплеем,  Зарядное устройство LiitoKala для аккумуляторов  AA AAA 10440 14500 16340 17335 17500 18490 17670  и другие. Все зарядные устройства отличаются высоким качеством, функциональностью и надежностью. Выбирайте зарядное устройство LiitoKala для ваших аккумуляторов и будьте уверены в их безопасности и долговечности"
    }
}
```

**2. <algorithm>**

Алгоритм принимает на вход `category_name`, список `products_titles` и `language`.  Возвращает JSON-словарь, содержащий `category_name`,  сокращенное название `title` (до 50 символов) и описание `description` (не более 1200 символов) для домохозяек.

1. **Получить входные данные:** Прочитать `category_name`, `products_titles`, и `language` из входного текста.
2. **Сгенерировать заголовок (`title`):**
    - Объединить названия продуктов из `products_titles` с помощью пробелов.
    - Укоротить получившуюся строку до 50 символов, возможно с использованием обрезки или алгоритма выбора наиболее значимых слов.
3. **Сгенерировать описание (`description`):**
    - Проанализировать названия продуктов из `products_titles` для выделения ключевых слов и характеристик (например, тип аккумулятора, функции зарядного устройства).
    - Сформировать описание, которое учитывает `language` и целевую аудиторию (домохозяйки).  Описание должно включать общую информацию о продуктах, их преимуществах и особенностях, связанных с домашним хозяйством.
    - Ограничить длину описания 1200 символами.
4. **Сформировать выходной JSON:** Составить словарь с `category_name`, `title`, и `description` и сконвертировать его в JSON.


**3. <mermaid>**

```mermaid
graph TD
    A[Входные данные: category_name, products_titles, language] --> B{Генерирование заголовка (title)};
    B --> C[Укорочение title до 50 символов];
    C --> D{Генерирование описания (description)};
    D --> E[Проверка длины description (<= 1200 символов)];
    E -- true --> F[Формирование выходного JSON];
    E -- false --> G[Обработка ошибки: description слишком длинное];
    F --> H[Выходной JSON];
    G --> H;
```

**4. <explanation>**

* **Импорты:**  Нет импортов. Код описывает функциональность, необходимую для формирования описания для кампаний AliExpress.

* **Классы:** Нет классов. Код описывает функцию `promo_creater`.

* **Функции:** Код представляет собой инструкцию, описывающую функцию `promo_creater`, которая должна обрабатывать входные данные и формировать выходной JSON.  Она должна:
    - Принимать `category_name`, `products_titles` и `language`.
    - Возвращать словарь в формате JSON с `category_name`, `title`, и `description`.
    - `title` — это сокращенная версия названия категорий.
    - `description` — это описание для домохозяек, основанное на названиях продуктов.

* **Переменные:** `category_name`, `products_titles`, и `language` - переменные, передаваемые в функцию.  На вход подается список (`products_titles`), а результат должен быть JSON (`description`).

* **Возможные ошибки/улучшения:**

    * Необходимо добавить логику обработки ошибок (например, пустой список `products_titles`, превышение длины описания).
    * Не хватает конкретных правил обработки имен продуктов для создания `title` и `description`.
    * Нужно добавить логику обработки различных языков.
    * Важно использовать библиотеки для работы с текстом и языками (например, для автоматического сокращения заголовков, перевода, выделения ключевых слов).
    * Лучше использовать библиотеку для работы с JSON.
    * Дополнительные проверки данных (например, длина названия категории, проверка наличия элементов в списке и т.д.)


**Цепочка взаимосвязей:**

Функция `promo_creater` является частью системы создания описаний для кампаний на AliExpress. Входные данные (названия продуктов и язык) могут быть предоставлены внешним модулем.  Выходные данные (JSON-описание) используются другими компонентами системы для генерации или отображения кампаний.