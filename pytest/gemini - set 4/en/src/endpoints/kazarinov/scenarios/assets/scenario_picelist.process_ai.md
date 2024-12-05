```python
import pytest
import logging


# Mock classes for testing
class MockAIModel:
    def __init__(self, attempts=3):
        self.attempts = attempts
        self.response = None

    def process(self, products_list):
        # Mock AI model behavior
        if self.attempts > 0:
            self.attempts -= 1
            return self.response
        else:
            return None

    def set_response(self, data):
        self.response = data


class MockLogger:
    def __init__(self):
        self.messages = []

    def log_error(self, message):
        self.messages.append(message)

    def log_info(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages


# Function to be tested
def process_ai(products_list, ai_model, logger, attempts=3):
    # Mock the data processing flow
    ai_model.set_response(None)  # No Response by default
    for attempt in range(attempts):
        result = ai_model.process(products_list)
        if result is not None:
            if isinstance(result, list):
                if len(result) == 2 and isinstance(result[0], str) and isinstance(result[1], str):
                    return result[0], result[1]
                elif len(result) == 1:
                    if isinstance(result[0], dict):
                        try:
                            return result[0]['ru'], result[0]['he']
                        except (KeyError, TypeError):
                            logger.log_error("Проблема парсинга ответа")
                    else:
                        logger.log_error("Проблема парсинга ответа")
                else:
                    logger.log_error("Проблема парсинга ответа")
            elif isinstance(result, dict):
                try:
                    return result['ru'], result['he']
                except (KeyError, TypeError):
                    logger.log_error("Invalid ru or he data")
            else:
                logger.log_error("Error in data from gemini")

        else:
            logger.log_error("no response from gemini")
    return None, None # Return default values on fail.


@pytest.fixture
def ai_model_fixture():
    return MockAIModel()

@pytest.fixture
def logger_fixture():
    return MockLogger()


def test_process_ai_valid_list(ai_model_fixture, logger_fixture):
    ai_model_fixture.set_response([ "Hello", "Shalom"])
    ru, he = process_ai([], ai_model_fixture, logger_fixture)
    assert ru == "Hello"
    assert he == "Shalom"
    assert len(logger_fixture.get_messages()) == 0

def test_process_ai_valid_dict(ai_model_fixture, logger_fixture):
    ai_model_fixture.set_response({"ru": "Hello", "he": "Shalom"})
    ru, he = process_ai([], ai_model_fixture, logger_fixture)
    assert ru == "Hello"
    assert he == "Shalom"
    assert len(logger_fixture.get_messages()) == 0


def test_process_ai_no_response(ai_model_fixture, logger_fixture):
    ru, he = process_ai([], ai_model_fixture, logger_fixture)
    assert ru is None
    assert he is None
    assert "no response from gemini" in logger_fixture.get_messages()


def test_process_ai_invalid_data(ai_model_fixture, logger_fixture):
    ai_model_fixture.set_response([{"ru": "Hello"}])  # Invalid structure for list
    ru, he = process_ai([], ai_model_fixture, logger_fixture)
    assert ru is None
    assert he is None
    assert "Проблема парсинга ответа" in logger_fixture.get_messages()
```