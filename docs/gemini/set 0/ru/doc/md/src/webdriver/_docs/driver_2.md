# Модуль `driver`

## Обзор

Данный модуль предоставляет базовый класс `DriverBase` для работы с веб-драйверами.  Этот класс инкапсулирует общие методы и атрибуты, используемые различными веб-драйверами (например, Chrome, Firefox, Edge), что способствует повторному использованию кода и упрощению управления различными типами драйверов.  Модуль также включает метакласс `DriverMeta`, который позволяет динамически создавать классы веб-драйверов, наследующие от `DriverBase` и конкретного класса веб-драйвера.

## Оглавление

* [Модуль `driver`](#модуль-driver)
* [Обзор](#обзор)
* [Классы](#классы)
    * [`DriverBase`](#driverbase)
    * [`DriverMeta`](#drivermeta)
    * [`Driver`](#driver)
* [Как использовать](#как-использовать)
* [Примеры использования методов](#примеры-использования-методов)

## Классы

### `DriverBase`

**Описание**: Базовый класс для веб-драйвера, содержащий общие атрибуты и методы.  Этот класс предоставляет базовый функционал для взаимодействия с веб-страницей, выполнения JavaScript-кода и управления куками.

**Атрибуты**:

- `previous_url`: URL предыдущей страницы (str).
- `referrer`: URL реферера (str).
- `page_lang`: Язык страницы (str).
- `ready_state`:  Состояние загрузки страницы (см. внутри).
- `get_page_lang()`: Функция получения языка страницы.
- ... (Другие атрибуты, если имеются)


**Методы**:

- `driver_payload()`: Инициализирует методы JavaScript и `ExecuteLocator` для выполнения команд на странице.

    ```python
    def driver_payload(self) -> None:
        """Инициализирует методы JavaScript и ExecuteLocator.

        Returns:
            None
        """
    ```

- `scroll(scrolls: int = 1, frame_size: int = 1000, direction: str = 'forward', delay: float = 0.5) -> None`: Прокручивает страницу в заданном направлении.

    ```python
    def scroll(self, scrolls: int = 1, frame_size: int = 1000, direction: str = 'forward', delay: float = 0.5) -> None:
        """Прокручивает страницу.

        Args:
            scrolls (int, optional): Количество прокруток. Defaults to 1.
            frame_size (int, optional): Размер фрейма для прокрутки. Defaults to 1000.
            direction (str, optional): Направление прокрутки ('forward' или 'backward'). Defaults to 'forward'.
            delay (float, optional): Задержка между прокрутками. Defaults to 0.5.

        Returns:
            None
        """
    ```


- `locale() -> str | None`: Определяет язык страницы.

    ```python
    def locale(self) -> str | None:
        """Определяет язык страницы.

        Returns:
            str | None: Язык страницы или None, если не удалось определить.
        """
    ```

- `get_url(url: str) -> bool`: Переходит по указанному URL и проверяет успешность перехода.

    ```python
    def get_url(self, url: str) -> bool:
        """Переходит по указанному URL.

        Args:
            url (str): URL для перехода.

        Returns:
            bool: True, если переход успешен, False в противном случае.
        """
    ```

- `extract_domain(url: str) -> str | None`: Извлекает доменное имя из URL.

    ```python
    def extract_domain(self, url: str) -> str | None:
        """Извлекает доменное имя из URL.

        Args:
            url (str): URL.

        Returns:
            str | None: Доменное имя или None, если URL некорректен.
        """
    ```

- `_save_cookies_localy(to_file: Union[str, Path]) -> None`: Сохраняет куки в файл.

    ```python
    def _save_cookies_localy(self, to_file: Union[str, Path]) -> None:
        """Сохраняет куки в файл.

        Args:
            to_file (Union[str, Path]): Путь к файлу для сохранения куков.
        """
    ```


- `page_refresh() -> None`: Обновляет текущую страницу.

    ```python
    def page_refresh(self) -> None:
        """Обновляет текущую страницу."""
    ```


- `window_focus() -> None`: Восстанавливает фокус на странице.

    ```python
    def window_focus(self) -> None:
        """Восстанавливает фокус на странице."""
    ```

- `wait(interval: float) -> None`: Делает паузу на указанное время.

    ```python
    def wait(self, interval: float) -> None:
        """Делает паузу на заданное время.

        Args:
            interval (float): Длительность паузы в секундах.
        """
    ```
- `delete_driver_logs() -> None`: Удаляет временные файлы и логи WebDriver.

    ```python
    def delete_driver_logs(self) -> None:
        """Удаляет временные файлы и логи WebDriver."""
    ```

**(Другие методы, если есть)**

### `DriverMeta`

### `Driver`


## Как использовать

Для использования класса `Driver` необходимо импортировать нужные классы веб-драйверов (например, `Chrome`, `Firefox`, `Edge`) и создать экземпляр класса `Driver` с указанным классом веб-драйвера.


## Примеры использования методов

(Примеры использования методов `DriverBase`, аналогично предоставленным в исходном коде)
```