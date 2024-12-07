Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный блок кода представляет собой инструкцию для создания приложения, которое собирает информацию о компьютерных компонентах, определяет тип сборки (например, игровая, офисная, рабочая станция), генерирует описательные заголовки и описания сборки на иврите и русском языках, а также переводит названия и описания компонентов на эти языки. Входные данные предоставляются в формате JSON, а вывод - тоже в формате JSON.

Шаги выполнения
-------------------------
1. **Получение входных данных:** Приложение принимает на вход JSON массив с информацией о компонентах компьютера.  Каждый элемент массива представляет собой словарь с ключами `product_id`, `product_title`, `product_description` и `image_local_saved_path`.
2. **Определение типа сборки:**  На основе характеристик компонентов, приложение определяет вероятностное распределение типов сборки (например, игровая, рабочая станция).  Вероятность каждого типа сборки указывается в формате `build_types` в результирующем JSON ответе.
3. **Генерация заголовка и описания:**  Приложение генерирует заголовок и подробное описание сборки на иврите и русском языках, используя предоставленные компоненты.  Заголовки и описания добавляются в результирующий JSON ответ.
4. **Перевод компонентов:** Приложение переводит названия компонентов (`product_title`) и их описания (`product_description`) на иврит и русский.  Переведенные данные сохраняются в соответствующих словарях `he` и `ru`.
5. **Формирование выходных данных:** Приложение формирует JSON ответ в соответствии с заданной структурой.  Ответ содержит заголовки и описания на обоих языках, список переведенных компонентов с их идентификаторами, названиями, описаниями и техническими характеристиками, а также вероятностные оценки типов сборок.
6. **Обработка неполных данных:** Если некоторые данные отсутствуют, приложение должно заполнить их по возможности лучшим образом или оставить соответствующие поля пустыми с соответствующими метками.
7. **Конкретизация терминологии:**  Вместо общих терминов, следует использовать конкретную и точную терминологию, например, "высокопроизводительный" вместо "хороший".
8. **Соответствие формату:**  Ответ должен строго соответствовать заданному формату JSON. Все переводы должны быть точными и соответствовать контексту, особенно техническим спецификациям.
9. **Категоризация компонентов:**  Если несколько компонентов относятся к одной категории (например, мониторы, видеокарты), необходимо создать список цен и выделить уникальные характеристики.



Пример использования
-------------------------
.. code-block:: json
    [
        {
            "product_id": "123",
            "product_title": "Процессор Intel Core i9-14900K",
            "product_description": "Высокопроизводительный процессор...",
            "image_local_saved_path": "path/to/image.jpg"
        },
        {
            "product_id": "456",
            "product_title": "Видеокарта NVIDIA RTX 4060 Ti",
            "product_description": "Современная видеокарта...",
            "image_local_saved_path": "path/to/image2.jpg"
        }
    ]

Пример ожидаемого результата (упрощенный):
.. code-block:: json
{
  "he": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "מחשב גיימינג בעל ביצועים גבוהים",
    "description": "מחשב מודרני למשחקים ותוכנות תובעניים...",
    "products": [
      {
        "product_id": "123",
        "product_title": "מעבד Intel Core i9-14900K",
        "product_description": "...",
        "image_local_saved_path": "path/to/image.jpg",
        "language": "he"
      },
      {
        "product_id": "456",
        "product_title": "כרטיס מסך NVIDIA RTX 4060 Ti",
        "product_description": "...",
        "image_local_saved_path": "path/to/image2.jpg",
        "language": "he"
      }
    ]
  },
  "ru": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "Высокопроизводительный игровой компьютер",
    "description": "Современный компьютер для требовательных игр...",
    "products": [
      {
        "product_id": "123",
        "product_title": "Процессор Intel Core i9-14900K",
        "product_description": "...",
        "image_local_saved_path": "path/to/image.jpg",
        "language": "ru"
      },
      {
        "product_id": "456",
        "product_title": "Видеокарта NVIDIA RTX 4060 Ti",
        "product_description": "...",
        "image_local_saved_path": "path/to/image2.jpg",
        "language": "ru"
      }
    ]
  }
}