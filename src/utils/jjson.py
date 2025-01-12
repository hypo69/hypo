import json
import os
import re
import codecs
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from types import SimpleNamespace
import pandas as pd
from json_repair import repair_json
from collections import OrderedDict


from src.logger.logger import logger
from .convertors.dict import dict2ns



MODE_WRITE = "w"
MODE_APPEND_START = "a+"
MODE_APPEND_END = "+a"

def _convert_to_dict(value: Any) -> Any:
    """Convert SimpleNamespace and lists to dict."""
    if isinstance(value, SimpleNamespace):
        return {key: _convert_to_dict(val) for key, val in vars(value).items()}
    if isinstance(value, dict):
        return {key: _convert_to_dict(val) for key, val in value.items()}
    if isinstance(value, list):
        return [_convert_to_dict(item) for item in value]
    return value

def _read_existing_data(path: Path, exc_info: bool = True) -> dict:
    """Read existing JSON data from a file."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding existing JSON in {path}: {e}", exc_info=exc_info)
        return {}
    except Exception as ex:
        logger.error(f"Error reading {path=}: {ex}", exc_info=exc_info)
        return {}

def _merge_data(
    data: Dict, existing_data: Dict, mode: str
) -> Dict:
    """Merge new data with existing data based on mode."""
    try:
        if mode == MODE_APPEND_START:
            if isinstance(data, list) and isinstance(existing_data, list):
               return data + existing_data
            if isinstance(data, dict) and isinstance(existing_data, dict):
                 existing_data.update(data)
            return existing_data
        elif mode == MODE_APPEND_END:
            if isinstance(data, list) and isinstance(existing_data, list):
                return existing_data + data
            if isinstance(data, dict) and isinstance(existing_data, dict):
                 data.update(existing_data)
            return data
        return data
    except Exception as ex:
        logger.error(ex)
        return {}

def j_dumps(
    data: Union[Dict, SimpleNamespace, List[Dict], List[SimpleNamespace]],
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = MODE_WRITE,
    exc_info: bool = True,
) -> Optional[Dict]:
    """
    Dump JSON data to a file or return the JSON data as a dictionary.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-compatible data or SimpleNamespace objects to dump.
        file_path (Optional[Path], optional): Path to the output file. If None, returns JSON as a dictionary. Defaults to None.
        ensure_ascii (bool, optional): If True, escapes non-ASCII characters in output. Defaults to True.
        mode (str, optional): File open mode ('w', 'a+', '+a'). Defaults to 'w'.
        exc_info (bool, optional): If True, logs exceptions with traceback. Defaults to True.

    Returns:
        Optional[Dict]: JSON data as a dictionary if successful, or nothing if an error occurs.

    Raises:
        ValueError: If the file mode is unsupported.
    """

    path = Path(file_path) if isinstance(file_path, (str, Path)) else None

    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f"Error converting string: {data}", ex, exc_info)
            return None

    data = _convert_to_dict(data)

    if mode not in {MODE_WRITE, MODE_APPEND_START, MODE_APPEND_END}:
        mode = MODE_WRITE

    existing_data = {}
    if path and path.exists() and mode in {MODE_APPEND_START, MODE_APPEND_END}:
        existing_data = _read_existing_data(path, exc_info)
    
    data = _merge_data(data, existing_data, mode)
    
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(data, ensure_ascii=ensure_ascii, indent=4), encoding='utf-8')
        except Exception as ex:
             logger.error(f"Failed to write to {path}: ", ex, exc_info=exc_info)
             return None
        return data
    return data

def _decode_strings(data: Any) -> Any:
    """Recursively decode strings in a data structure."""
    if isinstance(data, str):
        try:
           return codecs.decode(data, 'unicode_escape')
        except Exception:
            return data
    if isinstance(data, list):
        return [_decode_strings(item) for item in data]
    if isinstance(data, dict):
        return {
            _decode_strings(key): _decode_strings(value) for key, value in data.items()
        }
    return data

def _string_to_dict(json_string: str) -> dict:
    """Remove markdown quotes and parse JSON string."""
    if json_string.startswith(("```", "```json")) and json_string.endswith(
        ("```", "```\n")
    ):
        json_string = json_string.strip("`").replace("json", "", 1).strip()
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as ex:
        logger.error(f"JSON parsing error:\n {json_string}", ex, False)
        return {}


def j_loads(
    jjson: Union[dict, SimpleNamespace, str, Path, list], ordered: bool = True
) -> Union[dict, list]:
    """
    Load JSON or CSV data from a file, directory, string, or object.

    Args:
        jjson (dict | SimpleNamespace | str | Path | list): Path to file/directory, JSON string, or JSON object.
        ordered (bool, optional): Use OrderedDict to preserve element order. Defaults to True.

    Returns:
        dict | list: Processed data (dictionary or list of dictionaries).

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If the JSON data cannot be parsed.
    """
    try:
        if isinstance(jjson, SimpleNamespace):
            jjson = vars(jjson)

        if isinstance(jjson, Path):
            if jjson.is_dir():
                files = list(jjson.glob("*.json"))
                return [j_loads(file, ordered=ordered) for file in files]
            if jjson.suffix.lower() == ".csv":
                return pd.read_csv(jjson).to_dict(orient="records")
             
            return json.loads(jjson.read_text(encoding="utf-8"))
        if isinstance(jjson, str):
            return _string_to_dict(jjson)
        if isinstance(jjson, list):
             return _decode_strings(jjson)
        if isinstance(jjson, dict):
            return _decode_strings(jjson)
    except FileNotFoundError:
        logger.error(f"File not found: {jjson}")
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f"JSON parsing error:\n{jjson}\n", ex, False)
        return {}
    except Exception as ex:
        logger.error(f"Error loading data: {ex}", False)
        return {}
    return {}


def j_loads_ns(
    jjson: Union[Path, SimpleNamespace, Dict, str], ordered: bool = True
) -> Union[SimpleNamespace, List[SimpleNamespace], Dict]:
    """Load JSON/CSV data and convert to SimpleNamespace."""
    data = j_loads(jjson, ordered=ordered)
    if data:
        if isinstance(data, list):
            return [dict2ns(item) for item in data]
        return dict2ns(data)
    return {}