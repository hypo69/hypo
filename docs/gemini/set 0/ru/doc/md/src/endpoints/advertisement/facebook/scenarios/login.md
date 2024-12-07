# Модуль hypotez/src/endpoints/advertisement/facebook/scenarios/login.py

## Обзор

Данный модуль содержит сценарий для авторизации на Facebook. Он предоставляет функцию `login`, которая использует драйвер для заполнения полей логина и пароля, и нажатия кнопки входа.  Модуль использует данные авторизации из файла конфигурации и локаторы из JSON-файла.


## Функции

### `login`

**Описание**: Функция выполняет вход на Facebook, используя предоставленный драйвер.

**Параметры**:

- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-элементами.


**Возвращает**:

- `bool`: `True`, если авторизация прошла успешно, иначе `False`.


**Вызывает исключения**:

- `Exception`: Если возникает ошибка при вводе логина, пароля или нажатии кнопки входа.


## Локаторы

Локаторы для элементов Facebook загружаются из файла `login.json` в папке `locators` в подпапке `facebook` каталога `endpoints/advertisement`.


## Использование

```python
# Пример использования
from src.webdriver import Driver  # Импортируйте нужный класс из вашей библиотеки
from hypotez.src.endpoints.advertisement.facebook.scenarios.login import login  # Импортируйте функцию

# ... (создание экземпляра Driver) ...

if login(driver):
    print("Вход на Facebook выполнен успешно!")
else:
    print("Ошибка входа на Facebook.")
```

**Примечание**:  В примере предполагается, что `gs.facebook_credentials` содержит корректные данные авторизации, а `locators` успешно загружен.  В реальном коде необходимо добавить обработку потенциальных ошибок при загрузке данных и проверку доступности драйвера.