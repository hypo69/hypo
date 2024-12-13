```python
import pytest
import json

# Assuming the json data structure as a list of lists
# Each inner list contains 
#    - a hash string
#    - an instruction string
#    - null
#    - a dictionary containing agents, environments and factories
# In these tests, we mostly verify the configuration of agents in the dictionary
# since most modifications occur there

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return [
        [
        None,
            "(\'define\', (TinyPerson(name=\'Oscar\'), \'age\', 30), {})",
           None,
            {
                "agents": [
                    {
                        "name": "Oscar",
                        "_configuration": {
                            "name": "Oscar",
                            "age": 30,
                        }
                    },
                ]
            }
        ],
        [
            "9a614105c26e2f760144650f56b71415979b71fe278e716b90b9bfbba342b34d",
            "(\'define\', (TinyPerson(name=\'Oscar\'), \'nationality\', \'German\'), {})",
           None,
            {
                "agents": [
                    {
                        "name": "Oscar",
                        "_configuration": {
                            "name": "Oscar",
                            "nationality": "German",
                        }
                    },
                ]
            }
        ]
    ]
    
def test_load_json_default():
    """
    Tests if the json file can be loaded properly
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    assert isinstance(data, list)
    assert all(isinstance(item, list) for item in data)
    assert all(len(item) == 4 for item in data)
    
def test_agent_creation_and_attribute_definition_from_sample(sample_data):
    """
    Tests that an agent can be created, and then have attributes
    added to it, based on the provided sample data
    """
    for item in sample_data:
        agents = item[3]["agents"]
        assert len(agents) == 1
        agent = agents[0]
        assert agent["name"] == "Oscar"
        config = agent["_configuration"]
        if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'), \'age\', 30), {})":
            assert config["age"] == 30
        if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'), \'nationality\', \'German\'), {})":
            assert config["nationality"] == "German"
            
def test_agent_updates_from_full_cache_default():
    """
    Tests that the cache default, which represents many different
    updates to the agent, are correctly loaded, and have the last value applied.
    """

    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)

    last_agent_state = data[-1][3]["agents"][0]["_configuration"]

    assert last_agent_state["name"] == "Oscar"
    assert last_agent_state["age"] == 19
    assert last_agent_state["nationality"] == "Brazilian"
    assert last_agent_state["occupation"] == "Engineer"
    assert len(last_agent_state["routines"]) == 1
    assert last_agent_state["routines"][0]["routine"] == "Every morning, you wake up, feed your dog, and go to work."
    assert last_agent_state["occupation_description"].startswith("You are an architect")
    assert len(last_agent_state["personality_traits"]) == 4
    assert len(last_agent_state["professional_interests"]) == 3
    assert len(last_agent_state["personal_interests"]) == 3
    assert len(last_agent_state["skills"]) == 3
    assert len(last_agent_state["relationships"]) == 2
    
    assert last_agent_state["personality_traits"][0]["trait"] == "You are fast paced and like to get things done quickly."
    assert last_agent_state["personality_traits"][1]["trait"] == "You are very detail oriented and like to make sure everything is perfect."
    assert last_agent_state["personality_traits"][2]["trait"] == "You have a witty sense of humor and like to make jokes."
    assert last_agent_state["personality_traits"][3]["trait"] == "You don\'t get angry easily, and always try to stay calm. However, in the few occasions you do get angry, you get very very mad."
    
    assert last_agent_state["professional_interests"][0]["interest"] == "Modernist architecture and design."
    assert last_agent_state["professional_interests"][1]["interest"] == "New technologies for architecture."
    assert last_agent_state["professional_interests"][2]["interest"] == "Sustainable architecture and practices."

    assert last_agent_state["personal_interests"][0]["interest"] == "Traveling to exotic places."
    assert last_agent_state["personal_interests"][1]["interest"] == "Playing the guitar."
    assert last_agent_state["personal_interests"][2]["interest"] == "Reading books, particularly science fiction."

    assert last_agent_state["skills"][0]["skill"] == "You are very familiar with AutoCAD, and use it for most of your work."
    assert last_agent_state["skills"][1]["skill"] == "You are able to easily search for information on the internet."
    assert last_agent_state["skills"][2]["skill"] == "You are familiar with Word and PowerPoint, but struggle with Excel."

    assert last_agent_state["relationships"][0]["name"] == "Richard"
    assert last_agent_state["relationships"][0]["description"] == "your colleague, handles similar projects, but for a different market."
    
    assert last_agent_state["relationships"][1]["name"] == "John"
    assert last_agent_state["relationships"][1]["description"] == "your boss, he is always pushing you to reduce costs."

    assert last_agent_state["current_emotions"] == "Currently you feel calm and friendly."
    assert last_agent_state["current_attention"] ==  "The conversation with someone who asked how I'm doing."
    assert last_agent_state["current_goals"] == ""

def test_agent_age_change():
    """
    Tests the agent age is correctly changed
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    age_change_data_item = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'), \'age\', 19), {})"), None)
    assert age_change_data_item is not None
    agents = age_change_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert config["age"] == 19


def test_agent_occupation_change():
    """
    Tests the agent occupation is correctly changed
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    occupation_change_data_item = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'), \'occupation\', \'Engineer\'), {})"), None)
    assert occupation_change_data_item is not None
    agents = occupation_change_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert config["occupation"] == 'Engineer'

def test_agent_nationality_change():
    """
    Tests the agent nationality is correctly changed
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    nationality_change_data_item = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'), \'nationality\', \'Brazilian\'), {})"), None)
    assert nationality_change_data_item is not None
    agents = nationality_change_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert config["nationality"] == "Brazilian"

def test_agent_routine_addition():
    """
    Tests that the routine is correctly added
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    routine_change_data_item = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'), \'routine\', \'Every morning, you wake up, feed your dog, and go to work.\'), {\'group\': \'routines\'})"), None)
    assert routine_change_data_item is not None
    agents = routine_change_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert len(config["routines"]) == 1
    assert config["routines"][0]["routine"] == "Every morning, you wake up, feed your dog, and go to work."

def test_agent_occupation_description_addition():
    """
    Tests that the occupation description is correctly added
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    occupation_description_data_item = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'), \'occupation_description\', \'\\\\n                You are an architect. You work at a company called \\"Awesome Inc.\\". Though you are qualified to do any \\\\n                architecture task, currently you are responsible for establishing standard elements for the new appartment \\\\n                buildings built by Awesome, so that customers can select a pre-defined configuration for their appartment \\\\n                without having to go through the hassle of designing it themselves. You care a lot about making sure your \\\\n                standard designs are functional, aesthetically pleasing and cost-effective. Your main difficulties typically \\\\n                involve making trade-offs between price and quality - you tend to favor quality, but your boss is always \\\\n                pushing you to reduce costs. You are also responsible for making sure the designs are compliant with \\\\n                local building regulations.\\\\n                \'), {})"), None)
    assert occupation_description_data_item is not None
    agents = occupation_description_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert config["occupation_description"].startswith("You are an architect")

def test_agent_personality_trait_addition():
    """
    Tests that the personality trait is correctly added
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    personality_change_data_item_1 = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'),), {\'key\': None, \'value\': {\'trait\': \'You are fast paced and like to get things done quickly.\'}, \'group\': \'personality_traits\'})"), None)
    assert personality_change_data_item_1 is not None
    agents = personality_change_data_item_1[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert len(config["personality_traits"]) == 1
    assert config["personality_traits"][0]["trait"] == "You are fast paced and like to get things done quickly."

    personality_change_data_item_2 = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'),), {\'key\': None, \'value\': {\'trait\': \'You are very detail oriented and like to make sure everything is perfect.\'}, \'group\': \'personality_traits\'})"), None)
    assert personality_change_data_item_2 is not None
    agents = personality_change_data_item_2[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert len(config["personality_traits"]) == 2
    assert config["personality_traits"][1]["trait"] == "You are very detail oriented and like to make sure everything is perfect."
    
def test_agent_professional_interest_addition():
    """
    Tests that professional interest is correctly added
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    pro_interest_change_data_item_1 = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'),), {\'key\': None, \'value\': {\'interest\': \'Modernist architecture and design.\'}, \'group\': \'professional_interests\'})"), None)
    assert pro_interest_change_data_item_1 is not None
    agents = pro_interest_change_data_item_1[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert len(config["professional_interests"]) == 1
    assert config["professional_interests"][0]["interest"] == "Modernist architecture and design."

def test_agent_personal_interest_addition():
    """
    Tests that the personal interest is correctly added
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    personal_interest_change_data_item_1 = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'),), {\'key\': None, \'value\': {\'interest\': \'Traveling to exotic places.\'}, \'group\': \'personal_interests\'})"), None)
    assert personal_interest_change_data_item_1 is not None
    agents = personal_interest_change_data_item_1[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert len(config["personal_interests"]) == 1
    assert config["personal_interests"][0]["interest"] == "Traveling to exotic places."
    
def test_agent_skill_addition():
    """
    Tests that the skill is correctly added
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    skill_change_data_item_1 = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'),), {\'key\': None, \'value\': {\'skill\': \'You are very familiar with AutoCAD, and use it for most of your work.\'}, \'group\': \'skills\'})"), None)
    assert skill_change_data_item_1 is not None
    agents = skill_change_data_item_1[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert len(config["skills"]) == 1
    assert config["skills"][0]["skill"] == "You are very familiar with AutoCAD, and use it for most of your work."

def test_agent_relationships_addition():
    """
    Tests that the relationship is correctly added
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)
    relationship_change_data_item_1 = next((item for item in data if item[1] == "(\'define\', (TinyPerson(name=\'Oscar\'),), {\'key\': None, \'value\': {\'name\': \'Richard\', \'description\': \'your colleague, handles similar projects, but for a different market.\'}, \'group\': \'relationships\'})"), None)
    assert relationship_change_data_item_1 is not None
    agents = relationship_change_data_item_1[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    config = agent["_configuration"]
    assert len(config["relationships"]) == 1
    assert config["relationships"][0]["name"] == "Richard"
    assert config["relationships"][0]["description"] == "your colleague, handles similar projects, but for a different market."

def test_agent_stimulus_and_response_are_recorded():
    """
    Tests the stimulus and the response to a conversation is correctly registered in the messages buffer
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
        data = json.load(f)

    
    conversation_data_item = next((item for item in data if item[1] == "(\'listen_and_act\', (TinyPerson(name=\'Oscar\'), \'How are you doing?\'), {})"), None)
    assert conversation_data_item is not None
    agents = conversation_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    messages = agent["current_messages"]

    # There are 5 messages here
    assert len(messages) == 8

    # assert that there are 2 user messages: one asking how the agent is, and the second with the thought of acting
    assert messages[1]["role"] == "user"
    assert messages[1]["content"]["stimuli"][0]["type"] == "CONVERSATION"
    assert messages[1]["content"]["stimuli"][0]["content"] == "How are you doing?"
    
    assert messages[2]["role"] == "user"
    assert messages[2]["content"]["stimuli"][0]["type"] == "THOUGHT"
    assert messages[2]["content"]["stimuli"][0]["content"] == "I will now act a bit, and then issue DONE."
    
    # assert that the assistant replied by talking
    assert messages[3]["role"] == "assistant"
    assert messages[3]["content"]["action"]["type"] == "TALK"
    assert messages[3]["content"]["action"]["content"] == "I\'m doing well, thank you! How about you?"
    
    assert messages[4]["role"] == "user"
    assert messages[4]["content"]["stimuli"][0]["type"] == "THOUGHT"
    assert messages[4]["content"]["stimuli"][0]["content"] == "I will now act a bit, and then issue DONE."
    
    # assert that the assistant issued DONE
    assert messages[5]["role"] == "assistant"
    assert messages[5]["content"]["action"]["type"] == "DONE"
    

def test_agent_actions_buffer_is_correctly_populated():
    """
    Tests that the actions performed by the agent are correctly added
    to the buffer
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
        data = json.load(f)

    
    conversation_data_item = next((item for item in data if item[1] == "(\'listen_and_act\', (TinyPerson(name=\'Oscar\'), \'How are you doing?\'), {})"), None)
    assert conversation_data_item is not None
    agents = conversation_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    action_buffer = agent["_actions_buffer"]

    assert len(action_buffer) == 2

    # assert that the assistant replied by talking
    assert action_buffer[0]["type"] == "TALK"
    assert action_buffer[0]["content"] == "I\'m doing well, thank you! How about you?"
  
    # assert that the assistant issued DONE
    assert action_buffer[1]["type"] == "DONE"

def test_agent_displayed_comms_buffer_is_correctly_populated():
    """
    Tests that the communications displayed in the UI are correctly recorded in the displayed communications buffer
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
        data = json.load(f)

    
    conversation_data_item = next((item for item in data if item[1] == "(\'listen_and_act\', (TinyPerson(name=\'Oscar\'), \'How are you doing?\'), {})"), None)
    assert conversation_data_item is not None
    agents = conversation_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    displayed_comms_buffer = agent["_displayed_communications_buffer"]

    assert len(displayed_comms_buffer) == 5

    assert "[bold italic cyan1][underline]USER[/] --> [bold italic cyan1][underline]Oscar[/]: [CONVERSATION] \\n          > How are you doing?[/]" == displayed_comms_buffer[0]

    assert "[dim italic cyan1][underline]Oscar[/] --> [dim italic cyan1][underline]Oscar[/]: [THOUGHT] \\n           > I will now act a bit, and then issue DONE.[/]" == displayed_comms_buffer[1]

    assert "[bold green3][underline]Oscar[/] acts: [TALK] \\n           > I\'m doing well, thank you! How about you?[/]" == displayed_comms_buffer[2]

    assert "[dim italic cyan1][underline]Oscar[/] --> [dim italic cyan1][underline]Oscar[/]: [THOUGHT] \\n           > I will now act a bit, and then issue DONE.[/]" == displayed_comms_buffer[3]

    assert "[grey82][underline]Oscar[/] acts: [DONE] \\n[/]" == displayed_comms_buffer[4]

def test_agent_episodic_memory_is_populated():
    """
    Tests that the episodic memory is correctly populated
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
        data = json.load(f)

    conversation_data_item = next((item for item in data if item[1] == "(\'listen_and_act\', (TinyPerson(name=\'Oscar\'), \'How are you doing?\'), {})"), None)
    assert conversation_data_item is not None
    agents = conversation_data_item[3]["agents"]
    assert len(agents) == 1
    agent = agents[0]
    episodic_memory = agent["episodic_memory"]["memory"]

    # There should be 5 messages in memory: user stimulus, assistant talk, user thought, assistant done, and the message before
    assert len(episodic_memory) == 5

    assert episodic_memory[0]["role"] == "user"
    assert episodic_memory[0]["content"]["stimuli"][0]["type"] == "CONVERSATION"
    assert episodic_memory[0]["content"]["stimuli"][0]["content"] == "How are you doing?"
    
    assert episodic_memory[1]["role"] == "user"
    assert episodic_memory[1]["content"]["stimuli"][0]["type"] == "THOUGHT"
    assert episodic_memory[1]["content"]["stimuli"][0]["content"] == "I will now act a bit, and then issue DONE."
    
    assert episodic_memory[2]["role"] == "assistant"
    assert episodic_memory[2]["content"]["action"]["type"] == "TALK"
    assert episodic_memory[2]["content"]["action"]["content"] == "I\'m doing well, thank you! How about you?"

    assert episodic_memory[3]["role"] == "user"
    assert episodic_memory[3]["content"]["stimuli"][0]["type"] == "THOUGHT"
    assert episodic_memory[3]["content"]["stimuli"][0]["content"] == "I will now act a bit, and then issue DONE."

    assert episodic_memory[4]["role"] == "assistant"
    assert episodic_memory[4]["content"]["action"]["type"] == "DONE"
    assert episodic_memory[4]["content"]["action"]["content"] == ""

def test_semantic_memory_is_present_and_empty():
    """
    Tests that the semantic memory object is present in each agent and is
    correctly initialized
    """
    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)

    for item in data:
        agents = item[3]["agents"]
        assert len(agents) == 1
        agent = agents[0]
        semantic_memory = agent["semantic_memory"]

        assert semantic_memory["json_serializable_class_name"] == "SemanticMemory"
        assert semantic_memory["documents_paths"] == []
        assert semantic_memory["documents_web_urls"] == []
        assert semantic_memory["documents"] == []
        assert semantic_memory["filename_to_document"] == {}

def test_mental_faculties_is_present_and_empty():
    """
    Tests that the mental_faculties object is present in each agent and is empty
    """

    with open("hypotez/src/ai/tiny_troupe/TinyTroupe/tests/tinytroupe-cache-default.json", 'r') as f:
         data = json.load(f)

    for item in data:
        agents = item[3]["agents"]
        assert len(agents) == 1
        agent = agents[0]
        assert agent["_mental_faculties"] == []
```