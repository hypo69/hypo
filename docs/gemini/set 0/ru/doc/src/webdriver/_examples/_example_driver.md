# Модуль hypotez/src/webdriver/_examples/_example_driver.py

## Обзор

Данный модуль содержит примеры использования класса `Driver` для управления различными веб-драйверами (Chrome, Firefox, Edge). Примеры включают навигацию по URL, извлечение домена, прокрутку страницы и сохранение куки в файлы.

## Оглавление

* [Функция `main`](#функция-main)


## Функции

### `main`

**Описание**: Основная функция, демонстрирующая использование класса `Driver` с различными веб-драйверами.

**Описание тела функции**:

Функция создаёт экземпляры класса `Driver` для Chrome, Firefox и Edge, навигирует к URL `https://www.example.com`, извлекает домен, прокручивает страницу вверх/вниз/в обе стороны, сохраняет куки в файлы `cookies_chrome.pkl`, `cookies_firefox.pkl` и `cookies_edge.pkl`, а также закрывает браузеры. Обработка исключений `try...finally` гарантирует, что драйвер закрывается даже при ошибках.

**Вызывает исключения**:

* Любые исключения, которые могут быть подняты методами класса `Driver` при работе с веб-драйверами.


```python
def main():
    """ Main function to demonstrate how to use the Driver class with different web browsers."""
    # ... (код функции) ...
```

**Обратите внимание**:

*  В примере используется `url = "https://www.example.com"`. Замените его на нужный вам URL.
*  Имена файлов для сохранения куки (`cookies_chrome.pkl`, `cookies_firefox.pkl`, `cookies_edge.pkl`) могут быть изменены по вашему желанию.

```