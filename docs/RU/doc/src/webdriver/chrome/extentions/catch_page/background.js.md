# Модуль `background.js`

## Обзор

Этот модуль является фоновым скриптом для расширения Chrome и отвечает за обработку событий клика на иконке расширения, а также за прослушивание сообщений от других частей расширения, таких как контентные скрипты. Когда пользователь кликает на иконку расширения, модуль отправляет сообщение контентному скрипту для сбора данных. Также, модуль обрабатывает сообщения с действием 'collectData' и отправляет собранные данные на сервер.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`sendDataToServer`](#sendDataToServer)

## Функции

### `sendDataToServer`

**Описание**: Отправляет собранные данные на сервер.

**Параметры**:
- `url` (string): URL текущей страницы.

**Возвращает**:
- `undefined`: Функция ничего не возвращает.

**Вызывает исключения**:
- `Error`: Возникает, если не удается отправить данные на сервер.

```javascript
function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez/catch_request.php'; // Change to your server endpoint
    chrome.storage.local.get('collectedData', (result) => {
        const collectedData = result.collectedData;
        if (collectedData) {
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to send data to server');
                    }
                    console.log('Data sent to server successfully');
                })
                .catch(error => {
                    console.error('Error sending data to server:', error);
                });
        } else {
            console.error('No collected data found');
        }
    });
}
```