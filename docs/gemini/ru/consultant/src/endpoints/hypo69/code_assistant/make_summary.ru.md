# Анализ кода модуля `make_summary.py`

**Качество кода**
8
- Плюсы
    -   Хорошая документация модуля.
    -   Четкое описание назначения модуля, требований и порядка использования.
    -   Примеры вывода и лицензирование.
    -   Использование табличной структуры для навигации по проекту.
- Минусы
    -   Отсутствует код самого модуля, что делает невозможным оценку качества кода и его соответствия требованиям.

**Рекомендации по улучшению**

1.  **Добавление кода модуля**: Необходимо добавить код модуля `make_summary.py`, чтобы можно было провести его анализ и дать конкретные рекомендации по улучшению.
2.  **Форматирование:** Необходимо добавить форматирование кода, чтобы он был более читаемым и соответствовал стандартам PEP-8.

**Оптимизированный код**
```markdown
# Анализ кода модуля `make_summary.py`

**Качество кода**
8
-  Плюсы
    -   Хорошая документация модуля.
    -   Четкое описание назначения модуля, требований и порядка использования.
    -   Примеры вывода и лицензирование.
    -   Использование табличной структуры для навигации по проекту.
-  Минусы
    -   Отсутствует код самого модуля, что делает невозможным оценку качества кода и его соответствия требованиям.

**Рекомендации по улучшению**

1.  **Добавление кода модуля**: Необходимо добавить код модуля `make_summary.py`, чтобы можно было провести его анализ и дать конкретные рекомендации по улучшению.
2.  **Форматирование:** Необходимо добавить форматирование кода, чтобы он был более читаемым и соответствовал стандартам PEP-8.

**Оптимизированный код**
    ```python
    """
    Модуль для автоматического создания файла SUMMARY.md для mdbook.
    ==============================================================

    Этот модуль сканирует указанную директорию, ищет файлы .md
    и создает файл SUMMARY.md с оглавлением для mdbook.

    Пример использования
    --------------------

    .. code-block:: python

        python src/endpoints/hypo69/code_assistant/make_summary.py -lang ru src

    """

    import os
    import argparse
    from pathlib import Path
    from src.utils.jjson import j_loads_ns #Импортируем j_loads_ns
    from src.logger import logger #Импортируем logger

    def generate_summary(root_dir: str, lang: str) -> str:
        """
        Генерирует содержимое файла SUMMARY.md.

        Args:
            root_dir (str): Корневая директория для поиска файлов .md.
            lang (str): Язык для фильтрации файлов ('ru' или 'en').

        Returns:
            str: Содержимое файла SUMMARY.md.

        """
        summary_lines = ['# Summary', '']
        for root, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.md'):
                    if lang == 'ru' and not file.endswith('.ru.md'): # проверяем для ru
                        continue
                    if lang == 'en' and file.endswith('.ru.md'): # проверяем для en
                        continue

                    file_path = Path(os.path.join(root, file))
                    relative_path = file_path.relative_to(Path(root_dir).parent) # получаем относительный путь
                    file_name = str(relative_path).replace('\\\\', '/') # нормализуем путь
                    summary_lines.append(f'- [{file.replace(".md","")}]({file_name})')

        return '\n'.join(summary_lines)

    def save_summary(summary: str, output_dir: str = 'docs') -> bool:
        """
        Сохраняет сгенерированное содержимое в файл SUMMARY.md.

        Args:
            summary (str): Содержимое файла SUMMARY.md.
            output_dir (str): Директория для сохранения файла.

        Returns:
            bool: True, если файл успешно сохранен, False в противном случае.

        """
        try:
             # код исполняет создание директории если её нет
            os.makedirs(output_dir, exist_ok=True)
            # код исполняет запись в файл summary.md
            with open(Path(output_dir) / 'SUMMARY.md', 'w', encoding='utf-8') as f:
                f.write(summary)
            return True
        except Exception as ex:
            logger.error(f'Ошибка при записи файла SUMMARY.md: {ex}')
            return False


    def main():
        """
        Основная функция для запуска скрипта.
        """
        parser = argparse.ArgumentParser(description='Генератор SUMMARY.md для mdbook.')
        parser.add_argument('-lang', type=str, choices=['ru', 'en'], required=True, help='Язык для фильтрации файлов (ru или en).')
        parser.add_argument('root_dir', type=str, help='Корневая директория для поиска файлов .md.')

        args = parser.parse_args()
        try:
            # код исполняет генерацию summary
            summary_content = generate_summary(args.root_dir, args.lang)
            # код исполняет сохранение summary
            if save_summary(summary_content):
               print(f'Файл SUMMARY.md успешно создан в директории docs')
            else:
               print(f'Не удалось создать файл SUMMARY.md')

        except Exception as ex:
            logger.error(f'Произошла ошибка: {ex}')


    if __name__ == '__main__':
        main()
    ```
```