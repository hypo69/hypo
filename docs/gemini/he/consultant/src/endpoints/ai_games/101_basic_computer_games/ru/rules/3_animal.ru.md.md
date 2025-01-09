# Анализ кода модуля `3_animal.ru.md`

**Качество кода**
- **Соответствие требованиям к формату кода (1-10):** 8
  -   **Преимущества:**
      -   Документ содержит подробное описание игры "Угадай животное".
      -   Предоставлены пошаговые инструкции для реализации игры.
      -   Есть примеры работы и возможные ограничения.
      -   Логика игры чётко описана.
  -   **Недостатки:**
      -   Представлен markdown документ, а не код.
      -   Отсутствует фактический код на Python.
      -   Не используются reStructuredText (RST).

**Рекомендации по улучшению**

1. **Перевод в код:** На основе описания необходимо написать код на Python.
2. **Использование RST:** Добавить docstring в стиле RST.
3. **Реализация:** Создать классы и функции для реализации описанной логики игры.
4. **Обработка ввода:** Добавить проверки корректности ввода пользователя.
5. **Сохранение данных:** Реализовать сохранение и загрузку базы знаний.
6. **Использовать `j_loads`:**  При чтении файлов использовать `j_loads` вместо `json.load`.
7. **Логгирование:** Использовать `src.logger.logger` для обработки ошибок и предупреждений.
8. **Структура дерева:** Реализовать структуру дерева для хранения вопросов и животных.

**Улучшенный код**

```python
"""
Модуль для реализации игры "Угадай животное".
=========================================================================================

Модуль содержит класс :class:`AnimalGame`, который позволяет компьютеру
"учиться" угадывать животных, задавая вопросы пользователю.

Пример использования:
--------------------

.. code-block:: python

    game = AnimalGame()
    game.play()

"""
import json
from typing import Any, Dict, List

from src.utils.jjson import j_loads, j_dumps  # Импортирован j_loads и j_dumps
from src.logger.logger import logger # Импортирован logger


class Node:
    """
    Класс для представления узла в дереве вопросов и ответов.
    """
    def __init__(self, data: Any, yes_child: "Node" = None, no_child: "Node" = None):
        """
        Инициализация узла.

        :param data: Данные, хранящиеся в узле (вопрос или животное).
        :param yes_child: Узел-потомок для ответа "да".
        :param no_child: Узел-потомок для ответа "нет".
        """
        self.data = data
        self.yes_child = yes_child
        self.no_child = no_child


class AnimalGame:
    """
    Класс для реализации игры "Угадай животное".
    """

    def __init__(self, file_path: str = 'animal_data.json'):
        """
        Инициализация игры.

        :param file_path: Путь к файлу для сохранения/загрузки базы знаний.
        """
        self.file_path = file_path
        self.root = self.load_data() or Node("Это животное плавает?") # Загружаем данные или создаём начальный узел


    def load_data(self) -> Node | None:
        """
        Загружает данные из JSON файла.

        :return: Корневой узел дерева или None, если файл не существует или пуст.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f: # Открывает файл для чтения
                data = j_loads(f) # Использует j_loads для чтения файла
                if data:
                    return self._reconstruct_tree(data) # Восстанавливает дерево из данных
        except FileNotFoundError:
            logger.info(f"Файл {self.file_path} не найден, начинаем с нуля.")
            return None
        except Exception as e:
            logger.error(f"Ошибка при загрузке данных из файла {self.file_path}: {e}") # Логирует ошибку загрузки
            return None
        return None

    def _reconstruct_tree(self, data: dict) -> Node:
        """
        Рекурсивно восстанавливает дерево из словаря.

        :param data: Словарь, представляющий узел дерева.
        :return:  Узел дерева.
        """
        if not data:
            return None
        node = Node(data['data']) # Создаёт узел из данных
        if 'yes_child' in data:
             node.yes_child = self._reconstruct_tree(data['yes_child']) # Рекурсивно восстанавливает потомка для "да"
        if 'no_child' in data:
            node.no_child = self._reconstruct_tree(data['no_child']) # Рекурсивно восстанавливает потомка для "нет"
        return node

    def save_data(self):
        """
        Сохраняет текущее состояние базы знаний в JSON файл.
        """
        try:
            data = self._serialize_tree(self.root) # Сериализует дерево в словарь
            with open(self.file_path, 'w', encoding='utf-8') as f: # Открывает файл для записи
                j_dumps(data, f, ensure_ascii=False, indent=4) # Записывает словарь в JSON с помощью j_dumps
            logger.info("База знаний обновлена и сохранена.")
        except Exception as e:
             logger.error(f"Ошибка при сохранении данных в файл {self.file_path}: {e}") # Логирует ошибку сохранения

    def _serialize_tree(self, node: Node) -> dict:
        """
        Рекурсивно преобразует дерево в словарь.

        :param node: Узел дерева.
        :return: Словарь, представляющий узел дерева.
        """
        if not node:
            return None
        data = {'data': node.data} # Создаёт словарь для узла
        if node.yes_child:
            data['yes_child'] = self._serialize_tree(node.yes_child) # Рекурсивно сериализует потомка для "да"
        if node.no_child:
            data['no_child'] = self._serialize_tree(node.no_child) # Рекурсивно сериализует потомка для "нет"
        return data

    def play(self):
        """
        Запускает игровой цикл.
        """
        while True:
            print("Готовы загадать животное? (да/нет)")
            start = input().lower()
            if start != 'да':
                print("Пока!")
                break
            self.current_node = self.root # Начинает с корневого узла
            self._ask_question() # Начинает задавать вопросы

    def _ask_question(self):
        """
        Рекурсивно задаёт вопросы и обрабатывает ответы пользователя.
        """
        while True:
            if self.current_node.yes_child is None and self.current_node.no_child is None: # Если текущий узел - животное
                print(f"Это {self.current_node.data}? (да/нет)")
                answer = input().lower()
                if answer == 'да':
                    print("Ура! Я угадал!")
                    break
                else:
                    self._add_new_animal() # Добавляет новое животное
                    break
            else: # Если текущий узел - вопрос
                 print(f"{self.current_node.data} (да/нет)")
                 answer = input().lower()
                 if answer == 'да':
                     self.current_node = self.current_node.yes_child # Переходит к узлу "да"
                 else:
                     self.current_node = self.current_node.no_child # Переходит к узлу "нет"

    def _add_new_animal(self):
        """
        Добавляет новое животное и вопрос в базу знаний.
        """
        print("Какое животное вы загадали?")
        new_animal = input()
        print(f"Какой вопрос помог бы различить {new_animal} от {self.current_node.data}?")
        new_question = input()

        new_node = Node(new_animal) # Создаёт новый узел с животным
        old_node_data = self.current_node.data # Сохраняет предыдущие данные
        self.current_node.data = new_question # Меняет данные на новый вопрос
        self.current_node.yes_child = new_node # Потомком для "да" будет новый узел
        self.current_node.no_child = Node(old_node_data) # Потомком для "нет" будет старый узел

        self.save_data() # Сохраняет изменения
        print("Спасибо! Теперь я знаю больше о животных.")


if __name__ == '__main__':
    game = AnimalGame()
    game.play()
```