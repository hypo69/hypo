```python
import pytest
from tinytroupe.agent import TinyPerson
from tinytroupe.examples import (
    create_oscar_the_architect,
    create_lisa_the_data_scientist,
    create_marcos_the_physician,
    create_lila_the_linguist,
)

# Fixtures for creating example TinyPerson instances
@pytest.fixture
def oscar():
    """Fixture to create an Oscar the Architect instance."""
    return create_oscar_the_architect()

@pytest.fixture
def lisa():
    """Fixture to create a Lisa the Data Scientist instance."""
    return create_lisa_the_data_scientist()

@pytest.fixture
def marcos():
    """Fixture to create a Marcos the Physician instance."""
    return create_marcos_the_physician()

@pytest.fixture
def lila():
    """Fixture to create a Lila the Linguist instance."""
    return create_lila_the_linguist()


# Tests for create_oscar_the_architect
def test_create_oscar_the_architect_instance(oscar):
    """Test that create_oscar_the_architect returns a TinyPerson instance."""
    assert isinstance(oscar, TinyPerson)

def test_create_oscar_the_architect_name(oscar):
    """Test that the name is correctly set."""
    assert oscar.name == "Oscar"

def test_create_oscar_the_architect_attributes(oscar):
    """Test that the attributes are correctly set."""
    assert oscar.get("age") == 30
    assert oscar.get("nationality") == "German"
    assert oscar.get("occupation") == "Architect"
    assert oscar.get("routine", group="routines") == "Every morning, you wake up, feed your dog, and go to work."
    assert "cost-effective" in oscar.get("occupation_description")
    assert len(oscar.get("personality_traits")) == 4
    assert "Modernist architecture and design." in [item["interest"] for item in oscar.get("professional_interests")]
    assert "Traveling to exotic places." in [item["interest"] for item in oscar.get("personal_interests")]
    assert "You are very familiar with AutoCAD, and use it for most of your work." in [item["skill"] for item in oscar.get("skills")]
    assert "Richard" in [item["name"] for item in oscar.get("relationships")]
    assert "your colleague, handles similar projects, but for a different market." in [item["description"] for item in oscar.get("relationships")]
   

# Tests for create_lisa_the_data_scientist
def test_create_lisa_the_data_scientist_instance(lisa):
    """Test that create_lisa_the_data_scientist returns a TinyPerson instance."""
    assert isinstance(lisa, TinyPerson)

def test_create_lisa_the_data_scientist_name(lisa):
    """Test that the name is correctly set."""
    assert lisa.name == "Lisa"

def test_create_lisa_the_data_scientist_attributes(lisa):
    """Test that the attributes are correctly set."""
    assert lisa.get("age") == 28
    assert lisa.get("nationality") == "Canadian"
    assert lisa.get("occupation") == "Data Scientist"
    assert lisa.get("routine", group="routines") == "Every morning, you wake up, do some yoga, and check your emails."
    assert "scalable" in lisa.get("occupation_description")
    assert len(lisa.get("personality_traits")) == 4
    assert "Artificial intelligence and machine learning." in [item["interest"] for item in lisa.get("professional_interests")]
    assert "Cooking and trying new recipes." in [item["interest"] for item in lisa.get("personal_interests")]
    assert "You are proficient in Python, and use it for most of your work." in [item["skill"] for item in lisa.get("skills")]
    assert "Alex" in [item["name"] for item in lisa.get("relationships")]
    assert "your colleague, works on the same team, and helps you with data collection and processing." in [item["description"] for item in lisa.get("relationships")]


# Tests for create_marcos_the_physician
def test_create_marcos_the_physician_instance(marcos):
    """Test that create_marcos_the_physician returns a TinyPerson instance."""
    assert isinstance(marcos, TinyPerson)

def test_create_marcos_the_physician_name(marcos):
    """Test that the name is correctly set."""
    assert marcos.name == "Marcos"

def test_create_marcos_the_physician_attributes(marcos):
    """Test that the attributes are correctly set."""
    assert marcos.get("age") == 35
    assert marcos.get("nationality") == "Brazilian"
    assert marcos.get("occupation") == "Physician"
    assert "You alternate between two clinics" in marcos.get("routine", group="routines")
    assert "communicating with patients and their families" in marcos.get("occupation_description")
    assert len(marcos.get("personality_traits")) == 9
    assert "Neuroscience and neurology." in [item["interest"] for item in marcos.get("professional_interests")]
    assert "Pets and animals." in [item["interest"] for item in marcos.get("personal_interests")]
    assert "You are very skilled in diagnosing and treating neurological disorders." in [item["skill"] for item in marcos.get("skills")]
    assert "Julia" in [item["name"] for item in marcos.get("relationships")]
    assert "your wife, she is an educator, and works at a school for children with special needs." in [item["description"] for item in marcos.get("relationships")]


# Tests for create_lila_the_linguist
def test_create_lila_the_linguist_instance(lila):
    """Test that create_lila_the_linguist returns a TinyPerson instance."""
    assert isinstance(lila, TinyPerson)

def test_create_lila_the_linguist_name(lila):
    """Test that the name is correctly set."""
    assert lila.name == "Lila"

def test_create_lila_the_linguist_attributes(lila):
    """Test that the attributes are correctly set."""
    assert lila.get("age") == 28
    assert lila.get("nationality") == "French"
    assert lila.get("occupation") == "Linguist"
    assert lila.get("routine", group="routines") == "Every morning, you wake up, make yourself a cup of coffee, and check your email."
    assert "You have a deep understanding of human nature and preferences" in lila.get("occupation_description")
    assert len(lila.get("personality_traits")) == 8
    assert "Computational linguistics and artificial intelligence." in [item["interest"] for item in lila.get("professional_interests")]
    assert "Cooking and baking." in [item["interest"] for item in lila.get("personal_interests")]
    assert "You are fluent in French, English, and Spanish, and have a basic knowledge of German and Mandarin." in [item["skill"] for item in lila.get("skills")]
    assert "Emma" in [item["name"] for item in lila.get("relationships")]
    assert "your best friend, also a linguist, but works for a university." in [item["description"] for item in lila.get("relationships")]
```