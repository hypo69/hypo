```python
import pytest
from unittest.mock import Mock

# Assume these classes exist (replace with actual implementations if available)
class Driver:
    def __init__(self, *args, **kwargs):
        print(f'Driver initialized with {args}, {kwargs}')
        self.driver_payload()  # Call driver_payload

    def driver_payload(self):
        print('Driver payload called')

class Chrome:
    def __init__(self, *args, **kwargs):
        print(f'Chrome initialized with {args}, {kwargs}')
        self.name = 'Chrome'

class Firefox:
    def __init__(self, *args, **kwargs):
        print(f'Firefox initialized with {args}, {kwargs}')
        self.name = 'Firefox'

class Edge:
    def __init__(self, *args, **kwargs):
        print(f'Edge initialized with {args}, {kwargs}')
        self.name = 'Edge'

class DriverMeta(type):
    def __call__(cls, webdriver_cls, *args, **kwargs):
        assert isinstance(webdriver_cls, type)
        assert issubclass(webdriver_cls, (Chrome, Firefox, Edge))

        class DriverClass(cls, webdriver_cls):
            def __init__(self, *args, **kwargs):
                print(f'DriverClass initialized with {args}, {kwargs}')
                super().__init__(*args, **kwargs)
                self.driver_payload()

            def driver_payload(self):
                super().driver_payload()  # Call the parent's driver_payload

        return DriverClass(*args, **kwargs)


# Example usage (replace with your actual Driver class)
class MyDriver(metaclass=DriverMeta):
    pass



@pytest.fixture
def chrome_instance():
    return Chrome(1,2)

@pytest.fixture
def firefox_instance():
    return Firefox(3,4)

@pytest.fixture
def edge_instance():
    return Edge(5,6)

def test_driver_meta_chrome(chrome_instance):
    """Tests instantiation with Chrome."""
    DriverClass = DriverMeta(MyDriver, chrome_instance)  # Correct Usage
    driver = DriverClass()
    assert isinstance(driver, Chrome)
    assert driver.name == 'Chrome'


def test_driver_meta_firefox(firefox_instance):
    """Tests instantiation with Firefox."""
    DriverClass = DriverMeta(MyDriver, firefox_instance)
    driver = DriverClass()
    assert isinstance(driver, Firefox)
    assert driver.name == 'Firefox'

def test_driver_meta_edge(edge_instance):
    """Tests instantiation with Edge."""
    DriverClass = DriverMeta(MyDriver, edge_instance)
    driver = DriverClass()
    assert isinstance(driver, Edge)
    assert driver.name == 'Edge'


def test_driver_meta_invalid_webdriver_type():
    """Tests handling of invalid WebDriver class."""
    with pytest.raises(AssertionError):
        DriverMeta(MyDriver, str)


def test_driver_meta_non_webdriver_type():
    with pytest.raises(AssertionError):
        DriverMeta(MyDriver, object) #Example of invalid type
```