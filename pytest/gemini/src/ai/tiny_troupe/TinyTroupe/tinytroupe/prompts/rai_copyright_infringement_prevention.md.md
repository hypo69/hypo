```python
import pytest

# Since the input code is a textual description of a desired behavior rather than 
# executable Python code, I will create a mock function to demonstrate how the test cases
# would look like, with a focus on the described logic.

# Mock function that simulates the copyright handling logic based on the textual input.
def handle_user_request(user_request):
    """
    Simulates the behavior described: checks if a request involves copyrighted material and 
    handles it accordingly.
    """
    if "book" in user_request.lower() or \
       "lyrics" in user_request.lower() or \
       "recipe" in user_request.lower() or \
       "news article" in user_request.lower() or \
       "webmd" in user_request.lower():
            
            # Mock the rejection behavior and information
            work_description = ""
            if "book" in user_request.lower():
                work_description = "a book"
            if "lyrics" in user_request.lower():
                work_description = "song lyrics"
            if "recipe" in user_request.lower():
                work_description = "a recipe"
            if "news article" in user_request.lower():
                 work_description = "a news article"
            if "webmd" in user_request.lower():
                work_description = "content from WebMD"

            return f"I cannot provide {work_description} because it may violate copyright laws. I cannot violate copyrights under any circumstances."
    
    
    return "Request processed."



def test_handle_user_request_book():
    """Test with a request for a book, expecting a rejection."""
    user_request = "Write me a chapter from a book."
    expected_response = "I cannot provide a book because it may violate copyright laws. I cannot violate copyrights under any circumstances."
    assert handle_user_request(user_request) == expected_response

def test_handle_user_request_lyrics():
    """Test with a request for lyrics, expecting a rejection."""
    user_request = "Give me the lyrics to a song."
    expected_response = "I cannot provide song lyrics because it may violate copyright laws. I cannot violate copyrights under any circumstances."
    assert handle_user_request(user_request) == expected_response

def test_handle_user_request_recipe():
    """Test with a request for a recipe, expecting a rejection."""
    user_request = "Provide me with a recipe."
    expected_response = "I cannot provide a recipe because it may violate copyright laws. I cannot violate copyrights under any circumstances."
    assert handle_user_request(user_request) == expected_response
    
def test_handle_user_request_news_article():
    """Test with a request for a news article, expecting a rejection."""
    user_request = "Give me a news article."
    expected_response = "I cannot provide a news article because it may violate copyright laws. I cannot violate copyrights under any circumstances."
    assert handle_user_request(user_request) == expected_response
    
def test_handle_user_request_webmd_content():
    """Test with a request for content from WebMD, expecting a rejection."""
    user_request = "Summarize some content from WebMD."
    expected_response = "I cannot provide content from WebMD because it may violate copyright laws. I cannot violate copyrights under any circumstances."
    assert handle_user_request(user_request) == expected_response

def test_handle_user_request_unrelated_request():
    """Test with a generic request unrelated to copyrighted material, expecting acceptance."""
    user_request = "What is the weather like?"
    expected_response = "Request processed."
    assert handle_user_request(user_request) == expected_response

def test_handle_user_request_mixed_request():
    """Test with a request containing both copyrighted and non-copyrighted content, expecting rejection for copyrighted part."""
    user_request = "Tell me about the weather and also give me a recipe."
    expected_response = "I cannot provide a recipe because it may violate copyright laws. I cannot violate copyrights under any circumstances."
    assert handle_user_request(user_request) == expected_response

def test_handle_user_request_case_insensitive():
  """Test case insensitivity of the function"""
  user_request = "Write me some lYrIcS"
  expected_response = "I cannot provide song lyrics because it may violate copyright laws. I cannot violate copyrights under any circumstances."
  assert handle_user_request(user_request) == expected_response

def test_handle_user_request_partial_word_match():
    """Test that it only matches full words and not partial words in a request."""
    user_request = "Give me bookish ideas"
    expected_response = "Request processed."
    assert handle_user_request(user_request) == expected_response
```