```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pathlib import Path
import asyncio
import discord
from discord.ext import commands
import json
from hypotez.src.endpoints.bots.discord.discord_bot_trainger import bot, model, store_correction, PREFIX, text_to_speech_and_play


@pytest.fixture
def mock_ctx():
    """Provides a mock context object for testing bot commands."""
    ctx = AsyncMock(spec=commands.Context)
    ctx.send = AsyncMock()
    ctx.author = AsyncMock()
    ctx.author.voice = AsyncMock()
    ctx.voice_client = None
    ctx.fetch_message = AsyncMock()
    ctx.guild = AsyncMock()
    return ctx

@pytest.fixture
def mock_message():
    """Provides a mock message object for testing bot commands."""
    message = AsyncMock(spec=discord.Message)
    message.author = AsyncMock()
    message.channel = AsyncMock()
    message.attachments = []
    message.content = ""
    return message

@pytest.fixture
def mock_voice_client():
    """Provides a mock voice client object for testing bot commands."""
    voice_client = AsyncMock(spec=discord.VoiceClient)
    voice_client.is_playing = MagicMock(return_value=False)
    voice_client.disconnect = AsyncMock()
    return voice_client

@pytest.fixture
def mock_attachment():
    """Provides a mock attachment object for testing bot commands."""
    attachment = AsyncMock(spec=discord.Attachment)
    attachment.filename = "test_file.txt"
    attachment.save = AsyncMock()
    return attachment


@pytest.mark.asyncio
async def test_on_ready():
    """Checks if on_ready event logs the bot's login."""
    with patch('hypotez.src.endpoints.bots.discord.discord_bot_trainger.logger') as mock_logger:
        bot.user = AsyncMock()
        bot.user.name = "TestBot"
        await bot.on_ready()
        mock_logger.info.assert_called_with('Logged in as TestBot')


@pytest.mark.asyncio
async def test_hi(mock_ctx):
    """Checks if the hi command sends a 'HI!' message."""
    await bot.commands.get('hi')(mock_ctx)
    mock_ctx.send.assert_called_with('HI!')
    
@pytest.mark.asyncio
async def test_join_user_in_voice_channel(mock_ctx):
    """Checks if the bot joins a voice channel when the user is in one."""
    mock_ctx.author.voice.channel = AsyncMock()
    mock_ctx.author.voice.channel.connect = AsyncMock()
    mock_ctx.author.voice.channel.name = "TestChannel"
    await bot.commands.get('join')(mock_ctx)
    mock_ctx.author.voice.channel.connect.assert_called_once()
    mock_ctx.send.assert_called_with('Joined TestChannel')

@pytest.mark.asyncio
async def test_join_user_not_in_voice_channel(mock_ctx):
    """Checks if the bot sends a message when the user is not in a voice channel."""
    mock_ctx.author.voice = None
    await bot.commands.get('join')(mock_ctx)
    mock_ctx.send.assert_called_with('You are not in a voice channel.')

@pytest.mark.asyncio
async def test_leave_bot_in_voice_channel(mock_ctx, mock_voice_client):
    """Checks if the bot leaves a voice channel when it's connected."""
    mock_ctx.voice_client = mock_voice_client
    await bot.commands.get('leave')(mock_ctx)
    mock_voice_client.disconnect.assert_called_once()
    mock_ctx.send.assert_called_with('Disconnected from the voice channel.')

@pytest.mark.asyncio
async def test_leave_bot_not_in_voice_channel(mock_ctx):
    """Checks if the bot sends a message when it's not in a voice channel."""
    await bot.commands.get('leave')(mock_ctx)
    mock_ctx.send.assert_called_with('I am not in a voice channel.')

@pytest.mark.asyncio
async def test_train_with_attachment(mock_ctx, mock_attachment):
    """Checks if the train command correctly handles file attachments."""
    mock_ctx.send = AsyncMock()
    mock_ctx.author.voice = True
    mock_ctx.attachments = [mock_attachment]
    model.train = MagicMock(return_value="job123")
    model.save_job_id = MagicMock()
    await bot.commands.get('train')(mock_ctx, attachment=mock_attachment)
    mock_attachment.save.assert_called()
    model.train.assert_called()
    model.save_job_id.assert_called()
    mock_ctx.send.assert_called_with('Model training started. Job ID: job123')

@pytest.mark.asyncio
async def test_train_no_attachment_no_data(mock_ctx):
    """Checks if the train command handles no attachment with no data."""
    model.train = MagicMock(return_value=None)
    await bot.commands.get('train')(mock_ctx, data_dir="test_dir")
    mock_ctx.send.assert_called_with('Failed to start training.')

@pytest.mark.asyncio
async def test_train_with_data_and_dir(mock_ctx):
    """Checks if the train command correctly handles data and data_dir."""
    model.train = MagicMock(return_value="job456")
    model.save_job_id = MagicMock()
    await bot.commands.get('train')(mock_ctx, data="test_data", data_dir="test_dir")
    model.train.assert_called_with("test_data", "test_dir", True)
    model.save_job_id.assert_called()
    mock_ctx.send.assert_called_with('Model training started. Job ID: job456')


@pytest.mark.asyncio
async def test_test_valid_json(mock_ctx):
    """Checks if the test command correctly handles valid JSON input."""
    test_data = '{"key": "value"}'
    model.predict = MagicMock(return_value=["prediction"])
    model.handle_errors = MagicMock()
    await bot.commands.get('test')(mock_ctx, test_data=test_data)
    model.predict.assert_called()
    model.handle_errors.assert_called()
    mock_ctx.send.assert_called()

@pytest.mark.asyncio
async def test_test_invalid_json(mock_ctx):
    """Checks if the test command correctly handles invalid JSON input."""
    test_data = 'invalid json'
    await bot.commands.get('test')(mock_ctx, test_data=test_data)
    mock_ctx.send.assert_called_with('Invalid test data format. Please provide a valid JSON string.')

@pytest.mark.asyncio
async def test_test_no_predictions(mock_ctx):
    """Checks if the test command handles no predictions correctly."""
    test_data = '{"key": "value"}'
    model.predict = MagicMock(return_value=None)
    await bot.commands.get('test')(mock_ctx, test_data=test_data)
    mock_ctx.send.assert_called_with('Failed to get predictions.')


@pytest.mark.asyncio
async def test_archive_success(mock_ctx):
    """Checks if the archive command correctly handles a successful archive operation."""
    model.archive_files = AsyncMock()
    await bot.commands.get('archive')(mock_ctx, directory="test_dir")
    model.archive_files.assert_called_with("test_dir")
    mock_ctx.send.assert_called_with('Files in test_dir have been archived.')


@pytest.mark.asyncio
async def test_archive_failure(mock_ctx):
    """Checks if the archive command correctly handles a failed archive operation."""
    model.archive_files = AsyncMock(side_effect=Exception("Test Error"))
    await bot.commands.get('archive')(mock_ctx, directory="test_dir")
    mock_ctx.send.assert_called_with('An error occurred while archiving files: Test Error')

@pytest.mark.asyncio
async def test_select_dataset_success(mock_ctx):
    """Checks if the select_dataset command correctly handles a successful dataset selection."""
    model.select_dataset_and_archive = AsyncMock(return_value="dataset1")
    await bot.commands.get('select_dataset')(mock_ctx, path_to_dir_positive="test_dir")
    model.select_dataset_and_archive.assert_called_with("test_dir", True)
    mock_ctx.send.assert_called_with('Dataset selected and archived. Dataset: dataset1')

@pytest.mark.asyncio
async def test_select_dataset_failure(mock_ctx):
    """Checks if the select_dataset command correctly handles a failed dataset selection."""
    model.select_dataset_and_archive = AsyncMock(return_value=None)
    await bot.commands.get('select_dataset')(mock_ctx, path_to_dir_positive="test_dir")
    model.select_dataset_and_archive.assert_called_with("test_dir", True)
    mock_ctx.send.assert_called_with('Failed to select dataset.')


@pytest.mark.asyncio
async def test_instruction_file_exists(mock_ctx, tmp_path):
    """Checks if the instruction command sends the content of an existing instruction file."""
    instructions_path = tmp_path / "_docs" / "bot_instruction.md"
    instructions_path.parent.mkdir(exist_ok=True)
    instructions_path.write_text("Test Instructions")
    await bot.commands.get('instruction')(mock_ctx)
    mock_ctx.send.assert_called_with('Test Instructions')


@pytest.mark.asyncio
async def test_instruction_file_not_exists(mock_ctx):
    """Checks if the instruction command sends a 'not found' message when the instruction file does not exist."""
    with patch("hypotez.src.endpoints.bots.discord.discord_bot_trainger.Path.exists", return_value=False):
        await bot.commands.get('instruction')(mock_ctx)
        mock_ctx.send.assert_called_with('Instructions file not found.')


@pytest.mark.asyncio
async def test_instruction_read_error(mock_ctx):
    """Checks if the instruction command correctly handles errors when reading the instruction file."""
    with patch("hypotez.src.endpoints.bots.discord.discord_bot_trainger.Path.exists", return_value=True):
      with patch("hypotez.src.endpoints.bots.discord.discord_bot_trainger.Path.open", side_effect=Exception("Read Error")):
        await bot.commands.get('instruction')(mock_ctx)
        mock_ctx.send.assert_called()


@pytest.mark.asyncio
async def test_correct_message_found(mock_ctx):
    """Checks if the correct command correctly handles a found message."""
    mock_ctx.fetch_message = AsyncMock(return_value=AsyncMock(content="Original Message"))
    with patch("hypotez.src.endpoints.bots.discord.discord_bot_trainger.store_correction") as mock_store_correction:
      await bot.commands.get('correct')(mock_ctx, message_id=123, correction="Corrected Message")
      mock_store_correction.assert_called_with("Original Message", "Corrected Message")
      mock_ctx.send.assert_called_with("Correction received: Corrected Message")

@pytest.mark.asyncio
async def test_correct_message_not_found(mock_ctx):
    """Checks if the correct command correctly handles a message not found."""
    mock_ctx.fetch_message = AsyncMock(return_value=None)
    await bot.commands.get('correct')(mock_ctx, message_id=123, correction="Corrected Message")
    mock_ctx.send.assert_called_with("Message not found.")

@pytest.mark.asyncio
async def test_correct_error(mock_ctx):
    """Checks if the correct command correctly handles errors."""
    mock_ctx.fetch_message = AsyncMock(side_effect=Exception("Test Error"))
    await bot.commands.get('correct')(mock_ctx, message_id=123, correction="Corrected Message")
    mock_ctx.send.assert_called()


def test_store_correction(tmp_path):
    """Checks if store_correction correctly appends corrections to a file."""
    correction_file = tmp_path / "corrections_log.txt"
    store_correction("Original Text", "Corrected Text")
    with correction_file.open("r") as file:
      content = file.read()
      assert "Original: Original Text\nCorrection: Corrected Text\n\n" == content


@pytest.mark.asyncio
async def test_feedback(mock_ctx):
    """Checks if the feedback command stores the feedback correctly."""
    with patch("hypotez.src.endpoints.bots.discord.discord_bot_trainger.store_correction") as mock_store_correction:
      await bot.commands.get('feedback')(mock_ctx, feedback_text="Test Feedback")
      mock_store_correction.assert_called_with("Feedback", "Test Feedback")
      mock_ctx.send.assert_called_with('Thank you for your feedback. We will use it to improve the model.')

@pytest.mark.asyncio
async def test_getfile_file_exists(mock_ctx, tmp_path):
    """Checks if the getfile command sends a file when the file exists."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Test file content")
    await bot.commands.get('getfile')(mock_ctx, file_path=str(file_path))
    mock_ctx.send.assert_called()

@pytest.mark.asyncio
async def test_getfile_file_not_exists(mock_ctx):
    """Checks if the getfile command sends a 'file not found' message when the file does not exist."""
    await bot.commands.get('getfile')(mock_ctx, file_path="non_existent_file.txt")
    mock_ctx.send.assert_called_with('File not found: non_existent_file.txt')

#TODO: Fix this
@pytest.mark.asyncio
async def test_text_to_speech_and_play(mock_voice_client):
    """Checks if text_to_speech_and_play correctly converts text to speech and plays in voice channel."""
    
    channel = AsyncMock()
    channel.guild = AsyncMock()
    channel.guild.voice_client = mock_voice_client
    mock_voice_client.play = MagicMock()
    
    await text_to_speech_and_play("Test text", channel)
    mock_voice_client.play.assert_called()
    #mock_voice_client.disconnect.assert_called()


@pytest.mark.asyncio
async def test_on_message_from_self(mock_message):
    """Checks if on_message ignores messages from the bot itself."""
    mock_message.author = bot.user
    await bot.on_message(mock_message)
    mock_message.channel.send.assert_not_called()

@pytest.mark.asyncio
async def test_on_message_with_command(mock_message):
    """Checks if on_message processes commands correctly."""
    mock_message.content = f'{PREFIX}hi'
    with patch.object(bot, 'process_commands', new_callable=AsyncMock) as mock_process_commands:
        await bot.on_message(mock_message)
        mock_process_commands.assert_called_with(mock_message)

@pytest.mark.asyncio
async def test_on_message_with_audio_attachment(mock_message):
    """Checks if on_message handles audio attachments correctly."""
    mock_message.attachments = [AsyncMock(content_type='audio/ogg', url='http://test.com/audio.ogg')]
    mock_message.author = AsyncMock()
    mock_message.author.voice = None
    with patch("hypotez.src.endpoints.bots.discord.discord_bot_trainger.recognizer", return_value="Recognized text") as mock_recognizer:
      with patch.object(model, 'send_message', return_value="Response") as mock_send_message:
          await bot.on_message(mock_message)
          mock_recognizer.assert_called_with('http://test.com/audio.ogg')
          mock_send_message.assert_called_with("Recognized text")
          mock_message.channel.send.assert_called_with("Response")

@pytest.mark.asyncio
async def test_on_message_with_text_content(mock_message):
    """Checks if on_message handles text content correctly."""
    mock_message.content = "Test message"
    mock_message.author = AsyncMock()
    mock_message.author.voice = None
    with patch.object(model, 'send_message', return_value="Response") as mock_send_message:
        await bot.on_message(mock_message)
        mock_send_message.assert_called_with("Test message")
        mock_message.channel.send.assert_called_with("Response")

@pytest.mark.asyncio
async def test_on_message_with_voice_channel(mock_message):
    """Checks if on_message plays voice response when user in voice channel."""
    mock_message.content = "Test message"
    mock_message.author = AsyncMock()
    mock_message.author.voice = AsyncMock()
    mock_message.author.voice.channel = AsyncMock()
    with patch.object(model, 'send_message', return_value="Response") as mock_send_message:
       with patch("hypotez.src.endpoints.bots.discord.discord_bot_trainger.text_to_speech_and_play", new_callable=AsyncMock) as mock_text_to_speech_and_play:
         await bot.on_message(mock_message)
         mock_send_message.assert_called_with("Test message")
         mock_text_to_speech_and_play.assert_called_with("Response", mock_message.author.voice.channel)

```