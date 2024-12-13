```python
import pytest

def test_instruction_analysis():
    """
    Test that the instruction analysis is done correctly.
    This test checks if the steps identify the purpose of analyzing code.
    """
    instruction = "1. **Анализируй код**: Пойми логику и действия, выполняемые данным фрагментом кода."
    assert "Анализируй код" in instruction
    assert "Пойми логику" in instruction
    assert "действия" in instruction
    assert "фрагментом кода" in instruction

def test_instruction_step_creation():
    """
    Test that the step creation instruction is structured as expected.
    This test checks if the required keys for step instructions are present.
    """
    instruction = "2. **Создай пошаговую инструкцию**:\n    - **Описание**: Объясни, что делает данный блок кода.\n    - **Шаги выполнения**: Опиши последовательность действий в коде.\n    - **Пример использования**: Приведи пример кода, как использовать данный фрагмент в проекте."
    assert "Создай пошаговую инструкцию" in instruction
    assert "Описание" in instruction
    assert "Шаги выполнения" in instruction
    assert "Пример использования" in instruction

def test_instruction_formatting_rst():
    """
    Test if the formatting instruction is in `reStructuredText (RST)`.
    This test checks if the formatting example is using the right structure.
    """
    instruction = "3. **Форматирование**: Следуй структуре в `reStructuredText (RST)`:\n\n```rst\nКак использовать этот блок кода\n=========================================================================================\n\nОписание\n-------------------------\n[Объяснение, что делает код.]\n\nШаги выполнения\n-------------------------\n1. [Описание первого шага.]\n2. [Описание второго шага.]\n3. [Продолжай по необходимости...]\n\nПример использования\n-------------------------\n.. code-block:: python\n\n    [Пример использования кода]\n```"
    assert "Форматирование" in instruction
    assert "reStructuredText (RST)" in instruction
    assert "Как использовать этот блок кода" in instruction
    assert "Описание" in instruction
    assert "Шаги выполнения" in instruction
    assert "Пример использования" in instruction
    assert ".. code-block:: python" in instruction

def test_instruction_avoid_vague_terms():
    """
    Test if the instruction avoids vague terms.
    This test checks if the instruction suggests concrete terms.
    """
    instruction = "4. **Избегай расплывчатых терминов** вроде \"получаем\" или \"делаем\". Будь конкретным, что именно делает код, например: \"проверяет\", \"валидирует\" или \"отправляет\"."
    assert "Избегай расплывчатых терминов" in instruction
    assert "получаем" in instruction
    assert "делаем" in instruction
    assert "проверяет" in instruction
    assert "валидирует" in instruction
    assert "отправляет" in instruction
```