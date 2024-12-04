Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет собой HTML-форму для отправки данных на сервер FastAPI.  Форма содержит поля для ввода имени и фамилии.  После нажатия кнопки "Отправить", данные из формы отправляются на сервер с помощью AJAX запроса в формате JSON.  Код обрабатывает успешный ответ от сервера и ошибки при отправке данных.

Шаги выполнения
-------------------------
1. **Создание HTML формы:** Код генерирует HTML форму, включающую поля ввода для имени и фамилии, а также кнопку "Отправить".  Используются классы Bootstrap для стилизации.
2. **Подключение JavaScript библиотек:** Подключаются JavaScript библиотеки jQuery для обработки AJAX запросов.
3. **Обработка события отправки формы (JavaScript):** Функция `$(\'#dataForm\').submit(...)` регистрирует обработчик события отправки формы.
4. **Предотвращение стандартной отправки формы:** `event.preventDefault();` предотвращает перезагрузку страницы после отправки формы.
5. **Получение данных из полей формы (JavaScript):**  Извлекаются значения из полей ввода имени и фамилии.
6. **Формирование JSON данных:** Значения из полей ввода формируются в JSON объект с ключами `first_name` и `last_name`.
7. **Отправка AJAX запроса (JavaScript):** AJAX запрос типа POST отправляется на сервер FastAPI по адресу `/process_data` с данными в формате JSON.
8. **Обработка успешного ответа (JavaScript):** Если запрос успешен, обработчик `success` выполняет код, выводящий ответ от сервера в консоль.
9. **Обработка ошибок (JavaScript):** В случае ошибки, обработчик `error` выводит ошибку в консоль.


Пример использования
-------------------------
.. code-block:: html+javascript

    <!DOCTYPE html>
    <html>
    <body>
        <form id="dataForm">
            <input type="text" id="firstName" placeholder="Имя">
            <input type="text" id="lastName" placeholder="Фамилия">
            <button type="submit">Отправить</button>
        </form>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            $('#dataForm').submit(function(event) {
                event.preventDefault();
                var firstName = $('#firstName').val();
                var lastName = $('#lastName').val();
                $.ajax({
                    type: 'POST',
                    url: '/process_data',
                    contentType: 'application/json',
                    data: JSON.stringify({first_name: firstName, last_name: lastName}),
                    success: function(response) {
                        console.log('Успех:', response);
                    },
                    error: function(error) {
                        console.error('Ошибка:', error);
                    }
                });
            });
        </script>
    </body>
    </html>