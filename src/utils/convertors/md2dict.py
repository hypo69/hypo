## \file ../src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header 

import re
from typing import Dict
from markdown2 import markdown
from src.logger import logger


def extract_json_from_md(md_string: str) -> str:
    """Extract JSON content from Markdown string between ```json and ``` markers.

    Args:
        md_string (str): The Markdown string that contains JSON enclosed in ```json ```.

    Returns:
        str: The extracted JSON string or an empty string if not found.
    """
    try:
        match = re.search(r'```json\s*(.*?)\s*```', md_string, re.DOTALL)
        if match:
            json_string = match.group(1).strip()
            return json_string
        else:
            logger.warning("No JSON content found between ```json and ``` markers.")
            return ""
    except Exception as ex:
        logger.error("Error extracting JSON from Markdown.", exc_info=True)
        return ""


def md2dict(md_string: str) -> Dict:
    """Convert a Markdown string into a structured dictionary format with extracted JSON content.
    
    Args:
        md_string (str): The Markdown string to convert.
    
    Returns:
        Dict: A structured representation of the Markdown content.
    """
    try:
        # Extract JSON from Markdown if present
        json_content = extract_json_from_md(md_string)
        if json_content:
            return {"json": json_content}

        # If no JSON, process the Markdown normally
        html = markdown(md_string)
        sections = {}
        current_section = None

        for line in html.splitlines():
            if line.startswith('<h'):
                heading_level = int(re.search(r'h(\d)', line).group(1))
                section_title = re.sub(r'<.*?>', '', line).strip()

                if heading_level == 1:
                    current_section = section_title
                    sections[current_section] = []
                elif current_section:
                    sections[current_section].append(section_title)
            elif line.strip() and current_section:
                clean_text = re.sub(r'<.*?>', '', line).strip()
                sections[current_section].append(clean_text)

        return sections

    except Exception as ex:
        logger.error("Error parsing Markdown to structured JSON.", exc_info=True)
        return {}
