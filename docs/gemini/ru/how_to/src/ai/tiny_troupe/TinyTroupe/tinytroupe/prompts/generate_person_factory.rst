Как использовать этот блок кода
=========================================================================================\n

Описание
-------------------------
Этот блок кода описывает задачу генерации множества контекстов для создания описаний людей.  Входной параметр — общее описание, содержащее характеристики потенциальных людей (возраст, место проживания, профессия, семейное положение и т.д.).  На выходе — массив контекстов, каждый из которых содержит более конкретные характеристики, необходимые для создания описания отдельного человека.  Цель — создать множество разнообразных персонажей на основе общего описания.

Шаги выполнения
-------------------------
1. **Определите широкую характеристику**:  Укажите общие параметры для генерируемых персонажей (например, «житель Латинской Америки», «возраст 20-40 лет», «профессия — врач»).
2. **Укажите количество**: Определите нужное количество персонажей, которые должны быть сгенерированы.
3. **Используйте функцию генерации**: Функция принимает широкую характеристику и количество персонажей и возвращает массив контекстов.
4. **Используйте контексты**: Каждый контекст в массиве используется как входной параметр для генерации подробного описания конкретного персонажа.

Пример использования
-------------------------
.. code-block:: python

    import json

    def generate_person_contexts(broad_context, num_persons):
        """Генерирует массив контекстов для создания описаний людей."""
        # Заглушка - здесь должен быть вызов функции для генерации массива контекстов на основе входных данных.
        # Пример (заменить на ваш код):
        if broad_context == "Please, generate 3 person(s) description(s) based on the following broad context: Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can be have children or not, it can be a professional or not, it can be a worker or not":
            contexts = [
                "Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies",
                "Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.",
                "Create a Colombian person that is a lawyer, like to read and drink coffee and is married with 2 children."
            ]
        else:
            contexts = []  # Если нет подходящего контекста, возвращаем пустой массив.

        return json.dumps(contexts, indent=2)


    broad_context = "Please, generate 3 person(s) description(s) based on the following broad context: Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can be have children or not, it can be a professional or not, it can be a worker or not"
    num_persons = 3
    contexts = generate_person_contexts(broad_context, num_persons)
    print(contexts)