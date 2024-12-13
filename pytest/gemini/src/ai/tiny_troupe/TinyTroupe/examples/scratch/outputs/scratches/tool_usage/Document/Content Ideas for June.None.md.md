```python
import pytest

# The provided content is a Markdown document, not Python code.
# Therefore, it's not directly testable using pytest in a traditional sense.
# We will mock the reading and parsing of the document content to write tests for hypothetical processing.
# These tests will check if different parts of the document are correctly extracted.

# Mocking function to represent reading and processing the document
def read_and_process_document(file_path):
    """
    Mocks reading and processing of the markdown document.
    This would normally read from the file, but in the absence of a parser,
    we directly return the content.
    """
    content = """## Content Ideas for June

### 1. Blog Post: Latest Trends in Content Marketing

**Objective:** To inform our audience about the latest trends in content marketing and how they can leverage these trends to improve their own strategies.

**Key Points to Cover:**
- The rise of AI in content creation
- The importance of personalized content
- The growing influence of video content
- How to measure the success of content marketing efforts

### 2. Social Media Campaign: Engaging Audiences Through Interactive Content

**Objective:** To increase audience engagement on social media platforms by using interactive content such as polls, quizzes, and live Q&A sessions.

**Key Elements:**
- Create a series of polls related to industry topics
- Develop fun and informative quizzes that relate to our brand
- Host live Q&A sessions with industry experts
- Encourage user-generated content by asking followers to share their experiences and tag our brand"""
    return content


@pytest.fixture
def document_content():
    """Fixture to get the mocked document content."""
    return read_and_process_document("hypotez/src/ai/tiny_troupe/TinyTroupe/examples/scratch/outputs/scratches/tool_usage/Document/Content Ideas for June.None.md")

def test_document_title_extraction(document_content):
    """Checks if the document title is correctly extracted."""
    assert document_content.startswith("## Content Ideas for June")

def test_blog_post_section_presence(document_content):
    """Checks if blog post content section is present in the document."""
    assert "### 1. Blog Post: Latest Trends in Content Marketing" in document_content

def test_social_media_campaign_section_presence(document_content):
    """Checks if the social media campaign content section is present."""
    assert "### 2. Social Media Campaign: Engaging Audiences Through Interactive Content" in document_content


def test_blog_post_objective_extraction(document_content):
    """Checks if objective of blog post is correctly present."""
    assert "**Objective:** To inform our audience about the latest trends in content marketing and how they can leverage these trends to improve their own strategies." in document_content

def test_social_media_objective_extraction(document_content):
    """Checks if objective of social media campaign is correctly present."""
    assert "**Objective:** To increase audience engagement on social media platforms by using interactive content such as polls, quizzes, and live Q&A sessions." in document_content

def test_blog_post_key_points_presence(document_content):
    """Check if the key points for blog posts are present."""
    assert "- The rise of AI in content creation" in document_content
    assert "- The importance of personalized content" in document_content
    assert "- The growing influence of video content" in document_content
    assert "- How to measure the success of content marketing efforts" in document_content

def test_social_media_key_elements_presence(document_content):
    """Checks if the key elements for social media campaign are present."""
    assert "- Create a series of polls related to industry topics" in document_content
    assert "- Develop fun and informative quizzes that relate to our brand" in document_content
    assert "- Host live Q&A sessions with industry experts" in document_content
    assert "- Encourage user-generated content by asking followers to share their experiences and tag our brand" in document_content
```