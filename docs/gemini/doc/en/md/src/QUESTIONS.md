# QUESTIONS

## Overview

This file contains frequently asked questions (FAQs) about the project.  It details the rationale behind naming configuration files.

## Questions

### Q: Why are configuration files named after the module (e.g., `suppliers.json`)? Wouldn't `config.json` be a better approach?

### A:

**Description:**  This section explains the reasoning behind the naming convention.

**Answer:** The use of module-specific filenames (e.g., `suppliers.json`) was chosen for improved context and readability for AI models consuming the configuration files.  Using a generic name like `config.json` might make it harder for AI systems to understand the intended use of the configuration information within the larger system architecture.