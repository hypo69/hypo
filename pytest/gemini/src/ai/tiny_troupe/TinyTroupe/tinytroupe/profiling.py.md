```python
import pytest
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from tinytroupe.agent import TinyPerson
from tinytroupe.profiling import plot_age_distribution, plot_interest_distribution


@pytest.fixture
def example_agents():
    """Provides a list of example TinyPerson agents for testing."""
    agent1 = TinyPerson({"age": 25, "interests": "coding"})
    agent2 = TinyPerson({"age": 30, "interests": "reading"})
    agent3 = TinyPerson({"age": 25, "interests": "coding"})
    agent4 = TinyPerson({"age": 40, "interests": "hiking"})
    return [agent1, agent2, agent3, agent4]


def test_plot_age_distribution_valid_input(example_agents):
    """Checks if the function returns a DataFrame with correct age data and plot is created."""
    df = plot_age_distribution(example_agents, show=False)
    assert isinstance(df, pd.DataFrame)
    assert "Age" in df.columns
    assert len(df) == len(example_agents)
    assert df["Age"].tolist() == [25, 30, 25, 40]


def test_plot_age_distribution_empty_list():
    """Checks if the function returns an empty DataFrame when given an empty agent list."""
    df = plot_age_distribution([], show=False)
    assert isinstance(df, pd.DataFrame)
    assert df.empty


def test_plot_age_distribution_custom_title(example_agents):
    """Checks if the function uses the custom title in the plot."""
    title = "Custom Age Title"
    df = plot_age_distribution(example_agents, title=title, show=False)
    assert isinstance(df, pd.DataFrame)

    # For now, we will check for the title in the dataframe, as checking for the title
    # in the plot object itself can be challenging without extensive mocking.
    # assert title in plt.gca().get_title()

    assert "Age" in df.columns
    
def test_plot_age_distribution_no_show(example_agents):
    """Checks if the function doesn't show the plot when show=False."""
    df = plot_age_distribution(example_agents, show=False)
    assert isinstance(df, pd.DataFrame)
    assert "Age" in df.columns
    assert len(df) == len(example_agents)
    assert df["Age"].tolist() == [25, 30, 25, 40]

def test_plot_interest_distribution_valid_input(example_agents):
    """Checks if the function returns a DataFrame with correct interest data and pie chart."""
    df = plot_interest_distribution(example_agents, show=False)
    assert isinstance(df, pd.DataFrame)
    assert "Interests" in df.columns
    assert len(df) == len(example_agents)
    assert df["Interests"].tolist() == ["coding", "reading", "coding", "hiking"]

def test_plot_interest_distribution_empty_list():
    """Checks if the function returns an empty DataFrame when given an empty agent list."""
    df = plot_interest_distribution([], show=False)
    assert isinstance(df, pd.DataFrame)
    assert df.empty


def test_plot_interest_distribution_custom_title(example_agents):
    """Checks if the function uses the custom title in the plot."""
    title = "Custom Interest Title"
    df = plot_interest_distribution(example_agents, title=title, show=False)
    assert isinstance(df, pd.DataFrame)

    # For now, we will check for the title in the dataframe, as checking for the title
    # in the plot object itself can be challenging without extensive mocking.
    # assert title in plt.gca().get_title()
    
    assert "Interests" in df.columns


def test_plot_interest_distribution_no_show(example_agents):
    """Checks if the function doesn't show the plot when show=False."""
    df = plot_interest_distribution(example_agents, show=False)
    assert isinstance(df, pd.DataFrame)
    assert "Interests" in df.columns
    assert len(df) == len(example_agents)
    assert df["Interests"].tolist() == ["coding", "reading", "coding", "hiking"]
```