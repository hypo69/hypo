# Модуль `doc_writer_rst_ru`

## Обзор

Модуль `doc_writer_rst_ru` предназначен для генерации документации для разработчиков в формате Markdown. 
Модуль анализирует Python файлы и создает документацию, следуя определенным стандартам форматирования и содержания.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
    - [`function`](#function)

## Функции

### `function`

**Описание**:
    
Функция `function` принимает на вход параметры `param` и `param1` и может возвращать словарь или `None`.

**Параметры**:
- `param` (str): Описание параметра `param`.
- `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Описание возвращаемого значения. Возвращает словарь или `None`.

**Вызывает исключения**:
- `SomeError`: Описание ситуации, в которой возникает исключение `SomeError`.

```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Описание параметра `param`.
        param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

    Returns:
        dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
    try:
        return {"value": param} if param else None
    except Exception as ex:
        raise SomeError("Произошла ошибка") from ex
```