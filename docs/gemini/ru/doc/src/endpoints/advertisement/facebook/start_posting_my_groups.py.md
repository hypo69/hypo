# Модуль `start_posting_my_groups.py`

## Обзор

Модуль `start_posting_my_groups.py` предназначен для автоматической отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook, считывает информацию о группах из JSON-файлов и запускает рекламные кампании, определенные в списке.

## Подробней

Этот скрипт является частью системы автоматизации рекламы в Facebook. Он выполняет следующие шаги:

1.  Инициализирует веб-драйвер Chrome.
2.  Авторизуется на сайте Facebook.
3.  Загружает списки групп из JSON-файлов.
4.  Запускает рекламные кампании, используя информацию о группах и текстах объявлений.
5.  Повторяет процесс до прерывания пользователем.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` отвечает за продвижение рекламных кампаний в Facebook.

**Методы**:

*   `run_campaigns`: Запускает рекламные кампании.

**Параметры**:

*   `d`: Экземпляр веб-драйвера.
*   `group_file_paths`: Список путей к файлам JSON со списками групп.
*   `no_video`: Флаг, указывающий на отсутствие видео в рекламных материалах.

**Примеры**

```python
promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = True)
```

## Функции

### `FacebookPromoter.run_campaigns`

```python
def run_campaigns(campaigns:list = copy.copy(campaigns), group_file_paths:list = filenames) -> None:
    """
    Args:
        campaigns (list): Список названий рекламных кампаний.
        group_file_paths (list): Список путей к файлам JSON со списками групп.
    Returns:
        None
    Raises:
        Exception: Если возникает ошибка во время выполнения кампании.
    Example:
        >>> promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
    """
```

**Описание**: Запускает рекламные кампании в Facebook.

**Параметры**:

*   `campaigns`: Список названий рекламных кампаний.
*   `group_file_paths`: Список путей к файлам JSON со списками групп.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка во время выполнения кампании.

**Примеры**:

```python
promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)