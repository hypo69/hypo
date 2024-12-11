```python
import pytest
import discord
from discord.ext import commands
# Replace with actual import if available
# from src.endpoints.bots.discord import Bot # Assuming your bot class is in this file


# Placeholder for the actual bot class
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@pytest.fixture
def bot_instance():
    """Fixture to create a Discord bot instance for testing."""
    intents = discord.Intents.default()
    intents.message_content = True  # Needed for message content
    intents.members = True  # Needed for member information (if used)
    intents.voice_states = True  # Needed for voice channel state

    bot = Bot(command_prefix="!", intents=intents)
    return bot


def test_bot_initialization(bot_instance):
    """Tests that the bot initializes correctly."""
    assert isinstance(bot_instance, Bot)
    assert bot_instance.command_prefix == "!"


def test_hi_command(bot_instance):
    """Tests the !hi command."""
    # Mock the message object for testing.
    # Replace with the actual message object if possible.
    message = discord.message.Message(
        content="!hi", channel=discord.TextChannel(id=1)
    )

    # Mock the send method if needed
    def mock_send(content):
        assert content == "Hello!"
    bot_instance.send = mock_send
    bot_instance.process_commands(message)



def test_join_command(bot_instance):
    """Tests the !join command."""
    # Mock the message and voice channel
    message = discord.message.Message(content="!join", channel=discord.TextChannel(id=1))
    voice_channel = discord.VoiceChannel(id=123, name="test-channel")

    # Mock the voice_client
    voice_client = discord.VoiceClient(guild=discord.Guild(id=456))
    bot_instance.voice_clients = {'guild_id': voice_client}

    # Mock the connect method
    def mock_connect(channel):
        assert channel == voice_channel
    voice_client.connect = mock_connect


    bot_instance.get_channel = lambda x: voice_channel
    bot_instance.process_commands(message)


def test_leave_command(bot_instance):
    """Tests the !leave command."""
    # Mock the message and voice client
    message = discord.message.Message(content="!leave", channel=discord.TextChannel(id=1))
    voice_client = discord.VoiceClient(guild=discord.Guild(id=456))
    bot_instance.voice_clients = {'guild_id': voice_client}

    # Mock the disconnect method
    def mock_disconnect():
        pass
    voice_client.disconnect = mock_disconnect
    bot_instance.process_commands(message)

# Add more test cases for other commands (!train, !test, etc.) following the same pattern,
# mocking the necessary Discord objects and functions.  Remember to replace placeholders with actual calls/objects.
#  Don't forget to handle potential exceptions (e.g., missing voice channel)
```

**Explanation and Crucial Improvements:**

1. **Placeholders:** The code now includes placeholder comments (`# Replace with actual import if available`) and example `Bot` class, which you need to replace with your actual implementation.  This is **vital** to make the tests work.

2. **`pytest.fixture` for `bot_instance`:** A `bot_instance` fixture is created to manage a Discord bot instance for testing.  This is a much better approach than trying to create a bot object directly in each test, ensuring proper initialization and clean-up.  Crucially, it includes necessary `intents`.

3. **Mocking:**  The tests now use mocking (`mock_send`, `mock_connect`, `mock_disconnect`) instead of relying on actual Discord interactions.  This is **essential** for unit testing because it isolates the bot's functions from the Discord API.  Remember to mock *everything* that's not a simple function call.


4. **Example Test Cases (Crucial):**  I've added `test_hi_command`, `test_join_command`, and `test_leave_command` as *example* test cases.  Each needs to be adapted to your actual code's methods and how they handle the command input. **You need to add similar tests for *all* the commands and functions you want to verify.**

5. **Error Handling:** The provided structure is designed to be easily extended for other commands and error cases.

6. **Clearer Comments:** Improved comments help understand the purpose of each test.

**How to use with your code:**

* **Replace Placeholders:** Replace the `# ...` parts with the actual imports and classes from your `src.endpoints.bots.discord` module.
* **Mock Everything:** Mock the Discord API calls (e.g., `bot_instance.send`, `bot_instance.get_channel`,  `voice_client.connect`, `voice_client.disconnect`) within your test cases.
* **Complete Test Cases:** Create more test cases for each function and command (e.g., `!train`, `!test`), thoroughly testing valid inputs, edge cases, and potential errors (using `pytest.raises`).  Make sure to test exceptions for invalid user input or missing data.

**Example of a more complete `!train` test:**

```python
def test_train_command_valid_input(bot_instance):
    # ... (mocks as before) ...
    
    # Mock the training function (replace with your actual training logic)
    def mock_train(data):
        assert data == "example_data"
        return True

    bot_instance.train = mock_train
    message = discord.message.Message(content="!train example_data", channel=discord.TextChannel(id=1))
    
    # Mock successful response. Replace with your actual response behavior
    mock_send_response = lambda x: assert x == "Training successful!"
    bot_instance.send = mock_send_response


    bot_instance.process_commands(message)
```

Remember to install `pytest` if you haven't already (`pip install pytest`).  Then, run your tests using `pytest`.  This revised answer now provides a *much* more robust and practical testing framework for your Discord bot.