Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код предоставляет примеры создания агентов с помощью библиотеки tinytroupe.  Он демонстрирует, как создавать персонализированных агентов с различными характеристиками, такими как возраст, национальность, профессия, описание профессии, личностные черты, профессиональные и личные интересы, навыки и отношения.  Функции `create_oscar_the_architect`, `create_lisa_the_data_scientist`, `create_marcos_the_physician` и `create_lila_the_linguist` возвращают объекты `TinyPerson` с заданными параметрами.

Шаги выполнения
-------------------------
1. **Импортируйте необходимый модуль:**
   ```python
   from tinytroupe.agent import TinyPerson
   ```

2. **Выберите нужную функцию создания агента:**
   - `create_oscar_the_architect()`: создает агента Оскара, архитектора.
   - `create_lisa_the_data_scientist()`: создает агента Лизу, специалиста по данным.
   - `create_marcos_the_physician()`: создает агента Маркоса, врача-невролога.
   - `create_lila_the_linguist()`: создает агента Лилу, лингвиста.


3. **Вызовите функцию, соответствующую вашему агенту:**
   ```python
   oscar = create_oscar_the_architect()
   lisa = create_lisa_the_data_scientist()
   marcos = create_marcos_the_physician()
   lila = create_lila_the_linguist()
   ```

4. **Получите доступ к атрибутам агента (при необходимости):**
   ```python
   print(oscar.get_attribute("occupation"))
   print(lisa.get_several_attributes(["age", "nationality"]))
   ```
   Для получения нескольких атрибутов используется метод `get_several_attributes`.  В `get_attribute` передается имя атрибута.


Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.agent import TinyPerson

    # Пример создания и использования агента архитектора
    def main():
        oscar = create_oscar_the_architect()

        # Вывод профессии
        print(oscar.get_attribute("occupation"))  # Выведет "Architect"

        # Вывод описания профессии
        print(oscar.get_attribute("occupation_description"))

    if __name__ == "__main__":
        main()
```
```python
```
**Примечание:**  Код примера в  `examples.py` предоставляет несколько функций для создания разных агентов.  Чтобы использовать какой-либо из примеров, просто вызовите соответствующую функцию, например `create_oscar_the_architect()`, и сохранённый результат присвойте переменной (как показано в примере). Затем вы можете получить доступ к атрибутам агента с помощью метода `get_attribute`. Обратите внимание на разные атрибуты для разных агентов.