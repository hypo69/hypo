Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет собой HTML-страницу с интерфейсом для взаимодействия с моделью OpenAI.  Страница позволяет пользователю ввести сообщение и (необязательно) инструкцию для модели, а также загрузить данные для обучения.  После отправки запроса страница отображает ответ модели.  Код также реализует функцию обучения модели на предоставленных данных.

Шаги выполнения
-------------------------
1. **Ввод сообщения:** Пользователь вводит сообщение в поле "Message" и нажимает кнопку "Ask Model".

2. **Отправка запроса:**  Код отправляет POST-запрос на `/ask` с данными сообщения и (если указано) системой инструкции.

3. **Получение ответа:** Сервер обрабатывает запрос и возвращает ответ модели.

4. **Вывод ответа:** Страница отображает ответ модели в области "Response:".  Если возникла ошибка при отправке или обработке запроса, то будет выведено соответствующее сообщение об ошибке.

5. **Загрузка данных для обучения:** Пользователь вводит данные для обучения в поле "Training Data" в формате CSV.

6. **Обучение модели:** Пользователь нажимает кнопку "Train Model".

7. **Отправка данных обучения:** Код отправляет POST-запрос на `/train` с данными обучения (CSV).

8. **Получение ID задания обучения:** Сервер возвращает ID задания обучения.

9. **Вывод ID задания:**  Страница отображает ID задания обучения в области "Training Job ID:".  При ошибке будет выведено сообщение об ошибке.


Пример использования
-------------------------
.. code-block:: html+javascript
    
    <!DOCTYPE html>
    <html>
    <head>
        ... (HTML head, включая стили Bootstrap и AngularJS)
    </head>
    <body>
        <div class="form-group">
            <label for="message">Message</label>
            <input type="text" class="form-control" id="message" ng-model="ctrl.message" placeholder="Enter your message">
        </div>

        <button class="btn btn-primary" ng-click="ctrl.askModel()">Ask Model</button>

        <div class="mt-4">
            <h5>Response:</h5>
            <pre>{{ ctrl.response }}</pre>
        </div>
        
        <div class="form-group">
            <label for="data">Training Data (CSV string)</label>
            <textarea class="form-control" id="data" ng-model="ctrl.trainingData" rows="3" placeholder="Enter CSV data"></textarea>
        </div>

        <button class="btn btn-success" ng-click="ctrl.trainModel()">Train Model</button>
        
        <div class="mt-4">
            <h5>Training Job ID:</h5>
            <pre>{{ ctrl.jobId }}</pre>
        </div>
        
        ... (Остальной HTML и Javascript)

    </body>
    </html>