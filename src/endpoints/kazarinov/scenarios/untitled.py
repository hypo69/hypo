## \file hypotez/src/endpoints/kazarinov/scenarios/untitled.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.kazarinov.scenarios """
def j_loads(
        jjson: dict | SimpleNamespace | str | Path | list[dict] | list[SimpleNamespace],
        ordered: bool = True,
        exc_info: bool = True
    ) -> Any | False:
    """Load JSON or CSV data from a file, directory, or string.

    Args:
        jjson (Path | Dict | str): Path to a file, directory, or JSON data as a string, or JSON object.
        ordered (bool, optional): Return OrderedDict instead of regular dict to preserve element order. Defaults to True.
        exc_info (bool, optional): Log exceptions with traceback if True. Defaults to True.

    Returns:
        Any | False: A dictionary or list of dictionaries if successful, or False if an error occurred.

    Examples:
        >>> j_loads('data.json')
        {'key': 'value'}

        >>> j_loads(Path('/path/to/directory'))
        [{'key1': 'value1'}, {'key2': 'value2'}]

        >>> j_loads('{"key": "value"}')
        {'key': 'value'}

        >>> j_loads(Path('/path/to/file.csv'))
        [{'column1': 'value1', 'column2': 'value2'}]
    """

    def merge_dicts(dict_list: List[Dict]) -> Dict:
        """Merge a list of dictionaries into a single dictionary if they have the same structure."""
        merged = dict_list[0]
        for d in dict_list[1:]:
            for key in merged.keys():
                if key in d:
                    if isinstance(merged[key], dict) and isinstance(d[key], dict):
                        merged[key] = merge_dicts([merged[key], d[key]])
                    elif isinstance(merged[key], list) and isinstance(d[key], list):
                        merged[key].extend(d[key])
                    else:
                        merged[key] = d[key]
        return merged

    def _load_csv_from_file(file_path: Path) -> List[Dict]:
        """Load data from a CSV file and return as a list of dictionaries."""
        try:
            return pd.read_csv(file_path).to_dict(orient='records')
        except Exception:
            logger.error(f"Error reading CSV file: {file_path}", exc_info=exc_info)
            return []

    try:
        # Handle file paths (JSON, CSV) or directories.
        if isinstance(jjson, Path):
            json_path = Path(jjson)

            if json_path.is_dir():
                # Load all JSON files from the directory.
                json_files = list(json_path.glob("*.json"))
                if not json_files:
                    logger.warning(f"No JSON files found in directory: {json_path}", exc_info=exc_info)
                    return False

                dict_list = [j_loads(file)[1] for file in json_files]
                if all(isinstance(d, dict) for d in dict_list):
                    return merge_dicts(dict_list)
                return dict_list

            elif json_path.suffix == ".csv":
                return _load_csv_from_file(json_path)

            elif json_path.suffix == ".json":
                with json_path.open("r", encoding="utf-8") as f:
                    return json.load(f)

        # Handle raw JSON strings or dictionaries directly.
        elif isinstance(jjson, (str, dict)):
            if isinstance(jjson, str):
                # Check if it's a valid JSON string.
                try:
                    return json.loads(jjson)
                except json.JSONDecodeError:
                    logger.error("Invalid JSON string provided.", exc_info=exc_info)
                    return False
            return jjson

        # Handle lists of JSON objects or SimpleNamespace objects.
        elif isinstance(jjson, list):
            if all(isinstance(item, SimpleNamespace) for item in jjson):
                return [vars(item) for item in jjson]
            return jjson

    except FileNotFoundError:
        logger.error(f"File not found: {jjson}", exc_info=exc_info)
        return False
    except json.JSONDecodeError:
        logger.error(f"Failed to decode JSON: {jjson}", exc_info=exc_info)
        return False
    except Exception:
        logger.error("Unexpected error occurred during loading JSON data.", exc_info=exc_info)
        return False