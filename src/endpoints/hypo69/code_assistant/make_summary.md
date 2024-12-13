```rst
.. module:: src.endpoints.hypo69.code_assistant.make_summary
```

<TABLE>
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> \ 
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/README.MD'>endpoints</A>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/README.MD'>hypo69</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/endpoints/hypo69/code_assistant/make_summary.ru.md'>Русский</A>
</TD>
</TR>
</TABLE>

# Module `make_summary.py`

## Description

This module is designed to automatically generate the `SUMMARY.md` file, which is used for compiling documentation using tools like `mdbook`. The module recursively traverses the specified directory containing source `.md` files and generates a table of contents, including or excluding files based on the specified language.

## Key Features

- **Generation of `SUMMARY.md`**:
  - Recursively traverses the directory with source `.md` files.
  - Creates a `SUMMARY.md` file with a table of contents for each `.md` file.

- **Language Filtering**:
  - Supports filtering files by language:
    - `ru`: Includes only files with the `.ru.md` suffix.
    - `en`: Excludes files with the `.ru.md` suffix.

- **Universal Paths**:
  - All paths are relative to the project root, making the module robust to changes in directory structure.

## Installation and Usage

### Requirements

- Python 3.8 or higher.
- Installed dependencies from the `requirements.txt` file.

### Installation

1. Ensure you have Python and all dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the `make_summary.py` script with the specified `src` directory and language filter:
   ```bash
   python src/endpoints/hypo69/code_assistant/make_summary.py -lang ru src
   ```

   - The `-lang` parameter can take values `ru` or `en`.
   - The `src` argument specifies the directory containing the source `.md` files.

2. After running the script, the `SUMMARY.md` file will be created in the `docs` directory.

## Example Output

### Example `SUMMARY.md` for Language `ru`:
```
# Summary

- [file1](file1.md)
- [file2](file2.ru.md)
```

### Example `SUMMARY.md` for Language `en`:
```
# Summary

- [file1](file1.md)
- [file3](file3.en.md)
```

## Author

- **Author Name**: [Your Name]
- **Email**: [Your Email]
- **Boosty Link**: [https://boosty.to/hypo69](https://boosty.to/hypo69)

## License

This module is licensed under the [MIT License](../../../LICENSE).

