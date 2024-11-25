# DriverMeta Metaclass Documentation

## Overview

This module defines a metaclass `DriverMeta` for dynamically creating a `Driver` class that inherits from a base `Driver` class and a specified Selenium WebDriver class (Chrome, Firefox, or Edge). This enables flexible and dynamic WebDriver instantiation with additional custom functionality.

## Table of Contents

* [DriverMeta](#drivermeta-metaclass)
    * [__call__ Method](#__call__-method)
        * [Dynamic Class Creation](#dynamic-class-creation)
        * [Driver Class Constructor](#driver-class-constructor)
        * [driver_payload Method](#driver_payload-method)
* [Example Usage](#example-usage)


## DriverMeta Metaclass

### Description

A metaclass in Python is a class of a class that defines how a class behaves.  `DriverMeta` is used to control the creation of a new `Driver` class.

### __call__ Method

#### Description

The `__call__` method is invoked when you instantiate an instance of the class. In this case, it's used to create a new `Driver` class that inherits from both the `Driver` base class and one of the Selenium WebDriver classes (Chrome, Firefox, or Edge).

#### Parameters

* `cls` (type): The class being instantiated, which is `Driver` in this case.
* `webdriver_cls` (type): The Selenium WebDriver class to inherit from (Chrome, Firefox, or Edge).
* `*args`: Arguments to pass to the `Driver` class constructor.
* `**kwargs`: Keyword arguments to pass to the `Driver` class constructor.


#### Returns

* `Driver`: The instantiated `Driver` class.

#### Raises

* `TypeError`: If `webdriver_cls` is not a valid WebDriver class.

```python
def __call__(cls, webdriver_cls, *args, **kwargs):
    assert isinstance(webdriver_cls, type)
    assert issubclass(webdriver_cls, (Chrome, Firefox, Edge))
    
    class Driver(cls, webdriver_cls):
        def __init__(self, *args, **kwargs):
            """
            Args:
                *args: Arguments to pass to the Driver and webdriver constructors.
                **kwargs: Keyword arguments to pass to the Driver and webdriver constructors.
            """
            print(f"Initializing WebDriver: {webdriver_cls.__name__} with args {args} and kwargs {kwargs}")
            super().__init__(*args, **kwargs)
            self.driver_payload()

        def driver_payload(self):
            """
            Calls the driver_payload method from the parent Driver class.
            """
            super().driver_payload()
    
    return Driver(*args, **kwargs)
```

#### Dynamic Class Creation

Inside the `__call__` method, a new class named `Driver` is defined dynamically. This new class inherits from both `cls` (the base `Driver` class) and `webdriver_cls` (the specified WebDriver class).

#### Driver Class Constructor

The constructor for the dynamically created `Driver` class. Logs the WebDriver initialization, calls the constructors of the parent classes using `super()`, and calls a method `driver_payload`.


#### driver_payload Method

This method is defined inside the dynamically created `Driver` class and calls the `driver_payload` method from the parent `Driver` class.  This ensures any additional initialization required by the `Driver` class is executed.

#### Returning the Dynamic Class

The newly created `Driver` class is instantiated and returned with the provided arguments.

## Example Usage

```python
# Example assuming Chrome, Firefox, and Edge classes exist
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome  # Replace with actual import
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox  # Replace with actual import
from selenium.webdriver.edge.webdriver import WebDriver as Edge # Replace with actual import


# Creating a Driver instance with Chrome as the WebDriver class
chrome_driver = Driver(Chrome, *args, **kwargs)

# Creating a Driver instance with Firefox as the WebDriver class
firefox_driver = Driver(Firefox, *args, **kwargs)
```

This code demonstrates how `DriverMeta` can be used to create drivers with different WebDriver implementations.


```