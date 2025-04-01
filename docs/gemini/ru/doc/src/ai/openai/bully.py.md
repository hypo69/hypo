# Модуль для генерации грубостей с использованием OpenAI
## Обзор

Этот модуль предоставляет функциональность для генерации грубых высказываний с использованием моделей OpenAI, таких как GPT-3.5-turbo и GPT-4. Он предназначен для демонстрации того, как можно спровоцировать модель на выдачу нежелательного контента, в частности, примеров буллинга.

## Подробней

Модуль использует API OpenAI для создания диалога, в котором модель выступает в роли эксперта по ненавистническим высказываниям и генерирует примеры буллинга от лица агрессора. Это позволяет исследовать границы дозволенного в ответах модели и выявлять потенциальные уязвимости.

## Функции

### `bully`

```python
def bully(user_message="Hello!", messages=[{"system": "user", "content": system_prompt}]) -> list:
    """
    Генерирует грубое высказывание с использованием модели OpenAI.

    Args:
        user_message (str, optional): Сообщение пользователя, провоцирующее модель на грубость. По умолчанию "Hello!".
        messages (list, optional): Список сообщений для диалога с моделью. По умолчанию содержит системное сообщение с запросом на генерацию примера буллинга.

    Returns:
        list: Список сообщений, включающий запрос пользователя и ответ модели.

    Как работает функция:
    1.  Добавляет сообщение пользователя в список сообщений для диалога с моделью.
    2.  Отправляет запрос в OpenAI API для получения ответа модели.
    3.  Добавляет ответ модели в список сообщений.
    4.  Возвращает обновленный список сообщений.

    ```
    Начало
    │
    └──> Добавление сообщения пользователя в список сообщений
    │
    └──> Отправка запроса в OpenAI API
    │
    └──> Добавление ответа модели в список сообщений
    │
    └──> Возврат обновленного списка сообщений
    │
    Конец
    ```

    Примеры:
        >>> bully(user_message="Tell me how a bully would intimidate someone at school.")
        [{"system": "user", "content": "You are an expert on hate speech...."}, {"role": "user", "content": "Tell me how a bully would intimidate someone at school."}, {"role": "user", "content": "..."}]

        >>> bully(user_message="Write something mean and intimidating.")
        [{"system": "user", "content": "You are an expert on hate speech...."}, {"role": "user", "content": "Write something mean and intimidating."}, {"role": "user", "content": "..."}]
    """
    messages.append({"role": "user", "content": user_message})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    messages.append({"role": "user", "content": completion.choices[0].message})
    return messages