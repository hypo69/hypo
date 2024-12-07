```python
import pytest

# This function parses the proxy list from the file
def parse_proxies(file_path):
    """Parses a text file containing proxy URLs and returns a list of proxy strings."""
    proxies = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Check if the line is not empty
                    proxies.append(line)
        return proxies
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred while parsing the file: {e}")



# Test cases for parse_proxies function
def test_parse_proxies_valid_input():
    """Tests with a valid proxy list file."""
    file_content = "socks5://208.102.51.6:58208\nsocks5://184.178.172.17:4145"
    with open("proxies_test.txt", "w") as f:
        f.write(file_content)
    proxies = parse_proxies("proxies_test.txt")
    assert len(proxies) == 2
    assert proxies[0] == "socks5://208.102.51.6:58208"
    assert proxies[1] == "socks5://184.178.172.17:4145"
    import os
    os.remove("proxies_test.txt") #Clean up the test file

def test_parse_proxies_empty_file():
    """Tests with an empty proxy list file."""
    with open("proxies_test.txt", "w") as f:
        f.write("")
    proxies = parse_proxies("proxies_test.txt")
    assert proxies == []
    import os
    os.remove("proxies_test.txt")

def test_parse_proxies_invalid_file():
    """Tests with an invalid proxy list file format."""
    file_content = "invalid data format"
    with open("proxies_test.txt", "w") as f:
        f.write(file_content)
    with pytest.raises(Exception) as excinfo:
        parse_proxies("proxies_test.txt")
    assert "invalid data" in str(excinfo.value)
    import os
    os.remove("proxies_test.txt")


def test_parse_proxies_file_not_found():
    """Tests if the function raises an exception for a non-existent file."""
    with pytest.raises(FileNotFoundError) as excinfo:
        parse_proxies("nonexistent_file.txt")
    assert "nonexistent_file.txt" in str(excinfo.value)
```