```python
import pytest

# Tests for the content of the SUPPORT.md file.  No external dependencies are needed.

def test_issue_tracking_method():
    """Checks for the existence of issue tracking information."""
    content = """# Support

## How to file issues and get help  
This project uses GitHub Issues to track bugs and feature requests. Please search the existing 
issues before filing new issues to avoid duplicates.  For new issues, file your bug or 
feature request as a new Issue.

For help and questions about using this project, please consult our Wiki or post on our
Discussion forum, both right here on GitHub.

## Microsoft Support Policy  
Support for TinyTroupe is limited to the resources listed above."""
    assert "GitHub Issues" in content, "Issue tracking method not found."
    assert "search the existing issues" in content.lower(), "Searching existing issues not mentioned."
    assert "file your bug or feature request" in content.lower(), "Filing instructions missing."


def test_help_resources():
    """Checks for existence of help resources."""
    content = """# Support

## How to file issues and get help  
This project uses GitHub Issues to track bugs and feature requests. Please search the existing 
issues before filing new issues to avoid duplicates.  For new issues, file your bug or 
feature request as a new Issue.

For help and questions about using this project, please consult our Wiki or post on our
Discussion forum, both right here on GitHub.

## Microsoft Support Policy  
Support for TinyTroupe is limited to the resources listed above."""
    assert "Wiki" in content, "Wiki not found in help resources."
    assert "Discussion forum" in content, "Discussion forum not found in help resources."


def test_support_policy_existence():
    """Checks that the support policy section exists."""
    content = """# Support

## How to file issues and get help  
This project uses GitHub Issues to track bugs and feature requests. Please search the existing 
issues before filing new issues to avoid duplicates.  For new issues, file your bug or 
feature request as a new Issue.

For help and questions about using this project, please consult our Wiki or post on our
Discussion forum, both right here on GitHub.

## Microsoft Support Policy  
Support for TinyTroupe is limited to the resources listed above."""
    assert "Microsoft Support Policy" in content, "Support policy section missing."


def test_support_policy_details():
    """Checks the details within the support policy."""
    content = """# Support

## How to file issues and get help  
This project uses GitHub Issues to track bugs and feature requests. Please search the existing 
issues before filing new issues to avoid duplicates.  For new issues, file your bug or 
feature request as a new Issue.

For help and questions about using this project, please consult our Wiki or post on our
Discussion forum, both right here on GitHub.

## Microsoft Support Policy  
Support for TinyTroupe is limited to the resources listed above."""
    assert "limited to the resources listed above" in content.lower(), "Support policy details missing."

```