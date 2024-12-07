# Анализ кода - Промпт для генерации документации `how to`

## <input code>

```
Понял, вот промпт в первом лице, с командами для модели:

---

**Промпт для генерации `how to` документации для блоков кода**

1. Ты должен проанализировать текущий блок кода и все ранее загруженные блоки кода в проекте. На основе этого анализа ты сформулируешь пошаговую инструкцию, которая описывает, какие действия нужно выполнить для исполнения данного блока кода.

2. Для каждого блока кода ты должен создать подробную инструкцию в формате reStructuredText (RST), следуя следующим шагам:

    - **Описание**: Объясни, что делает этот блок кода, например, какую задачу решает или какую проверку выполняет.
    - **Шаги выполнения**: Описывай последовательность действий, которые нужно выполнить для того, чтобы код исполнился. Для каждого шага подробно укажи, что именно происходит в процессе.
    - **Пример использования**: Приведи пример того, как этот код можно использовать в проекте, в том числе с возможными вызовами функций или методов.

3. Структура документации для каждого блока кода должна быть следующей:

```rst
Как использовать блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода выполняет [описание действий блока кода, например, "проверку на валидность ввода данных"].

Шаги выполнения
-------------------------
1. [Первый шаг выполнения, например, "Получение данных через вызов функции `get_data()`." ]
2. [Второй шаг выполнения, например, "Проверка данных на валидность с использованием метода `validate_data()`." ]
3. [Третий шаг выполнения, например, "Если данные валидны, выполняется дальнейшая обработка." ]
4. [И так далее...]

Пример использования
-------------------------
Пример того, как можно использовать данный блок кода в проекте:

.. code-block:: python

    <пример_кода_с_использованием>
```

4. При написании документации обязательно учитывай:

    - Если блок кода выполняет проверку, то опиши, как она работает и какие данные проверяются.
    - Если блок кода включает в себя вызовы других функций или методов, обязательно укажи, какие именно функции вызываются и с какими параметрами.
    - Важно использовать точные формулировки, избегая общих терминов типа "получаем" или "делаем". Вместо этого опиши, что конкретно делает код: "код проверяет", "код выполняет отправку запроса", и так далее.

5. Пример для блока кода, который выполняет проверку переменной:

```rst
Как использовать блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода выполняет проверку на валидность значения переменной `value` перед дальнейшей обработкой.

Шаги выполнения
-------------------------
1. Получение значения переменной `value` через вызов метода `get_value()`.
2. Проверка, является ли значение пустым или невалидным. Если да, то логируется сообщение об ошибке и выполнение кода прекращается.
3. Если значение валидно, оно передается в следующую функцию для дальнейшей обработки.

Пример использования
-------------------------
Пример того, как можно использовать данный блок кода:

.. code-block:: python

    value = get_value()
    if value:
        process_value(value)
    else:
        logger.error('Невалидное значение')
```

6. Каждый блок кода должен быть документирован в этом формате, с четкими и понятными шагами, поясняющими, что именно делает код, и с примером того, как его можно использовать.

---

Этот промпт даст тебе команду для создания подробной документации для каждого блока кода на основе его анализа. Ты будешь генерировать документацию, которая объяснит последовательность действий для исполнения кода, а также приведет примеры использования.
```

## <algorithm>

Этот код не содержит блок кода для анализа, а представляет собой промпт, задачу для модели, описывающий желаемый алгоритм (шаги) для генерации документации по коду.  Поэтому блок-схема и примеры не применимы.

## <mermaid>

```mermaid
graph TD
    A[Промпт] --> B{Анализ кода};
    B --> C[Генерация документации (RST)];
    C --> D[Документированный блок кода];
```

## <explanation>

Этот промпт - это инструкция, которая описывает, как должен вести себя LLM (большая языковая модель) при получении блока кода.  Она не является кодом, а представляет собой *описание процесса* генерации документации `how to`.

- **Импорты**: Нет импортов, так как это не код.
- **Классы**: Нет классов, так как это не код.
- **Функции**: Нет функций, так как это не код.
- **Переменные**: Нет переменных, так как это не код.
- **Возможные ошибки или улучшения**: Промпт достаточно подробен, но можно добавить возможность указывать формат выходного файла (например, `markdown` или `rst`) для большей гибкости.  Также можно было бы уточнить, какая именно модель кода должна быть обработана.

**Цепочка взаимосвязей с другими частями проекта**: Промпт задает задачу для системы генерации документации, которая должна быть интегрирована с системой обработки кода.  Следовательно, этот промпт выступает в качестве связующего звена между анализом кода и его документированием.