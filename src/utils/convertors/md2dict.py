## \file src/utils/convertors/md2dict.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header 

import re
from typing import Dict
from markdown2 import markdown
from src.logger import logger




def md2dict(md_string: str) -> Dict:
    """Convert a Markdown string into a structured dictionary format with extracted JSON content.
    
    Args:
        md_string (str): The Markdown string to convert.
    
    Returns:
        Dict: A structured representation of the Markdown content.
    """
    try:
        # Extract JSON from Markdown if present
        json_content = extract_json_from_string(md_string)
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
