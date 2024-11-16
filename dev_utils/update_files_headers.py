def add_or_replace_file_header(file_path: str, project_root: Path, force_update: bool):
    """Adds or replaces a header, interpreter lines, and module docstring in the specified Python file.

    Args:
        file_path (str): Path to the Python file being processed.
        project_root (Path): The root directory of the project.
        force_update (bool): If True, forces update even if headers already exist.
    """
    # Определяем относительный путь от корня проекта
    relative_path = Path(file_path).resolve().relative_to(project_root)
    header_line = f'## \\file hypotez/{relative_path.as_posix()}\n'
    coding_index = '# -*- coding: utf-8 -*-\n'
    
    # Получаем пути к интерпретаторам
    w_venv_interpreter, w_system_interpreter, linux_venv_interpreter, linux_system_interpreter = get_interpreter_paths(project_root)
    
    # Формируем строки для интерпретаторов
    w_venv_interpreter_line = f'#! {w_venv_interpreter}\n'
    # w_system_interpreter_line = f'#! {w_system_interpreter}
    linux_venv_interpreter_line = f'#! {linux_venv_interpreter}\n'
    # linux_system_interpreter_line = f'#! {linux_system_interpreter}
    closing_line = '## ~~~~~~~~~~~~~\n'
    
    # Создаем строку документации модуля и заменяем символы `/` на `.` 
    module_path = relative_path.parent.as_posix().replace('/', '.')
    module_docstring = f'""" module: {module_path} """\n'
    mode_line = "MODE = 'debug'\n"

    print(f"Processing file: {file_path}")

    try:
        with open(file_path, 'r+', encoding='utf-8', newline='') as file:
            lines = file.readlines()

            # Удаляем BOM и ненужные строки заголовка, кодировки и интерпретатора
            cleaned_lines = [line.lstrip('\ufeff') for line in lines]  # Удаление BOM
            filtered_lines = [
                line for line in cleaned_lines
                if not (line.startswith("## \\file")
                        or line.startswith("# -*- coding")
                        or line.startswith("#!"))
                        or line.strip().startswith('""" module:')
                        or line.strip().startswith('MODE:')
            ]

            # Проверка необходимости обновления
            header_needs_update = not any(line == header_line for line in filtered_lines)
            coding_needs_update = not any(line == coding_index for line in filtered_lines)
            venv_interpreter_needs_update = not any(line == w_venv_interpreter_line or line == linux_venv_interpreter_line for line in filtered_lines)
            #system_interpreter_needs_update = not any(line == w_system_interpreter_line or line == linux_system_interpreter_line for line in filtered_lines)
            #closing_needs_update = not any(line == closing_line for line in filtered_lines)
            module_docstring_needs_update = not any(line.strip() == module_docstring.strip() for line in filtered_lines)
            mode_needs_update = not any(line.strip() == mode_line.strip() for line in filtered_lines)

            # Если force_update включен, всегда обновляем кроме строк 'MODE' и 'module:'
            if force_update:
                if not any(line.strip() == mode_line.strip() for line in filtered_lines):
                    mode_needs_update = True
                if not any(line.strip() == module_docstring.strip() for line in filtered_lines):
                    module_docstring_needs_update = True
            else:
                # Если force_update не включен, обновляем только если строки отсутствуют
                header_needs_update = not any(line == header_line for line in filtered_lines)
                coding_needs_update = not any(line == coding_index for line in filtered_lines)
                venv_interpreter_needs_update = not any(line == w_venv_interpreter_line or line == linux_venv_interpreter_line for line in filtered_lines)

            # Добавляем новые строки заголовка, если это необходимо
            new_lines = []
            if header_needs_update:
                new_lines.append(header_line)
            if coding_needs_update:
                new_lines.append(coding_index)
            if venv_interpreter_needs_update:
                new_lines.append(w_venv_interpreter_line)
                #new_lines.append(linux_venv_interpreter_line)
            # if system_interpreter_needs_update:
            #     new_lines.append(w_system_interpreter_line)
            #     new_lines.append(linux_system_interpreter_line)
            # if closing_needs_update:
            #     new_lines.append(closing_line)
            if module_docstring_needs_update:
                new_lines.append(module_docstring)
            if mode_needs_update:
                new_lines.append(mode_line)

            # Запись изменений в файл
            if new_lines:
                file.seek(0)  # Перемещаем указатель в начало файла
                file.writelines(new_lines + filtered_lines)  # Записываем новые строки и оставшиеся строки файла
                file.truncate()  # Обрезаем файл после добавленных строк
                print(f"Updated {file_path} successfully.")
            else:
                print(f"No updates necessary for {file_path}.")
                
    except IOError as ex:
        print(f"Error processing file {file_path}: {ex}")
