# Документация для файла hypotez/src/fast_api/html/openai/index.html

## Обзор

Этот HTML-файл представляет собой страницу взаимодействия с моделью OpenAI, реализованную с использованием AngularJS.  Страница позволяет пользователю вводить сообщение и (необязательно) системную инструкцию для модели, а также загружать данные для обучения модели.  Результаты запроса и информация об обучении отображаются на странице.

## Оглавление

- [Обзор](#обзор)
- [Интерактивный интерфейс](#интерактивный-интерфейс)
    - [Запрос модели](#запрос-модели)
    - [Обучение модели](#обучение-модели)
- [Скрипт JavaScript](#скрипт-javascript)


## Интерактивный интерфейс

### Запрос модели

Данный раздел описывает интерфейс для отправки запросов к модели OpenAI.

**Элементы интерфейса:**

- **Поле "Сообщение":** Текстовое поле для ввода сообщения, которое будет отправлено модели.
- **Поле "Системная инструкция":** Необязательное текстовое поле для предоставления модели системной инструкции.
- **Кнопка "Запрос модели":** Кнопка, при нажатии на которую отправляется запрос к модели.
- **Поле "Ответ":**  Отображает ответ модели на запрос.


**Обработка запросов:**

При нажатии на кнопку "Запрос модели", AngularJS отправляет POST-запрос на `/ask` с данными из полей "Сообщение" и "Системная инструкция". Ответ, полученный от сервера, отображается в поле "Ответ". Обработка ошибок также реализована. При возникновении ошибки в поле "Ответ" отображается сообщение об ошибке.


### Обучение модели

Этот раздел описывает функциональность для обучения модели.

**Элементы интерфейса:**

- **Поле "Данные обучения":** Текстовое поле для ввода данных обучения в формате CSV.
- **Кнопка "Обучить модель":** Кнопка, запускающая процесс обучения.
- **Поле "ID задачи обучения":** Отображает ID задачи обучения.


**Обработка обучения:**

При нажатии на кнопку "Обучить модель", AngularJS отправляет POST-запрос на `/train` с данными из поля "Данные обучения".  ID задачи обучения, полученный от сервера, отображается в поле "ID задачи обучения". Обработка ошибок реализована аналогично запросу модели.


## Скрипт JavaScript

Данный раздел содержит JavaScript-код, реализующий функционал страницы.

В коде используются следующие AngularJS функции:

- `vm.askModel()`: Отправляет запрос к модели.
- `vm.trainModel()`: Запускает процесс обучения модели.

Функции обрабатывают POST-запросы к соответствующим API-точкам (`/ask` и `/train`).  Они также реализуют обработку ошибок и отображения результатов.


**Обработка ошибок:**

В коде предусмотрены обработчики ошибок для `$http.post()`, которые выводят сообщения об ошибках в соответствующие поля.

**Использование AngularJS:**

В коде используется AngularJS для управления данными и обновлением интерфейса.


**Зависимости:**

- Bootstrap CSS и JS для стилей и функционала.
- AngularJS библиотека.
- jQuery для поддержки JavaScript.