Discord Bot Trainer
=====================

This module provides a step-by-step guide on training a large language model using a Discord bot. It details how to prepare training data, initiate training, monitor progress, test the model, and manage data using various commands.

.. automodule:: hypotez.src.bots.openai_bots.discord_bot_traigner  # Replace with actual module path if needed
    :members:
    :undoc-members:
    :show-inheritance:


Training Guide
-------------

~ Step-by-Step Training Procedure ~

^ Ensure Bot is Running ^
Make sure your bot is running. You should see a message in your console indicating the bot is logged in.

.. code-block:: plaintext
   Logged in as YourBotName#1234


^ Invite the Bot to Your Server ^
Ensure the bot is invited to your server with the necessary permissions to read messages and send messages.


^ Prepare Your Training Data ^
You can train the model using text data or files containing the training data.

1. **Training with Text Data**:
   Prepare a string of text data that you want to use for training.

2. **Training with a File**:
   Prepare a file containing the training data. Ensure the file is accessible on your local machine.


^ Use the Training Command ^

**Method 1: Using Text Data Directly**
1. In a Discord channel where the bot has access, type the following command:
   .. code-block:: plaintext
      !train "Your training data here" positive=True
   Example:
   .. code-block:: plaintext
      !train "Sample training data" positive=True


**Method 2: Uploading a File**
1. Attach the file containing the training data in a message.
2. In the same message, type the following command and send:
   .. code-block:: plaintext
      !train positive=True
   Example:
   .. code-block:: plaintext
      !train positive=True


The bot will save the file and start training the model with the provided data.


^ Monitor Training ^
After you send the training command, the bot should respond with a message indicating the status of the training job:

.. code-block:: plaintext
   Model training started. Job ID: <job_id>


^ Verify Training Status ^
You can add additional commands to your bot to check the status of the training job if needed. This would typically involve querying the model object for job status.


^ Testing the Model ^
Once the model is trained, you can test it with the test command.

1. Prepare a JSON string of test data.
2. In a Discord channel where the bot has access, type the following command:
   .. code-block:: plaintext
      !test {"test_key": "test_value"}
   Example:
   .. code-block:: plaintext
      !test {"input": "Test input data"}


The bot will respond with the model's predictions.


^ Using Additional Commands ^
Your bot also supports other commands such as archiving files and selecting datasets. Use these commands similarly to manage your data and model.

**Archiving Files**:
.. code-block:: plaintext
   !archive <directory_path>
Example:
.. code-block:: plaintext
   !archive /path/to/directory


**Selecting Dataset**:
.. code-block:: plaintext
   !select_dataset <path_to_dir_positive> positive=True
Example:
.. code-block:: plaintext
   !select_dataset /path/to/positive_data positive=True



Summary
-------

1. **Start Bot**: Ensure your bot is running.
2. **Invite Bot**: Make sure the bot is in your Discord server.
3. **Prepare Data**: Have your training data ready as text or in a file.
4. **Train Model**: Use the `!train` command with either text data or file attachment.
5. **Monitor Training**: Look for the bot's response about the training job status.
6. **Test Model**: Use the `!test` command with test data to verify model performance.
7. **Manage Data**: Use `!archive` and `!select_dataset` commands as needed.



Q&A Command Guide
-----------------

~ Adding a Q&A Command ~


1. **Start the Bot**: Make sure your bot is running.

2. **Ask a Question**:
   In a Discord channel where the bot has access, type the following command:

.. code-block:: plaintext
   !ask What is the capital of France?


3. **Receive the Response**:
   The bot should respond with the model's answer:

.. code-block:: plaintext
   Model response: The capital of France is Paris.


Summary
-------

1. **Add `ask` Command**:
   - Update your bot script to include the `ask` command.
   - Implement the `ask` method in your `Model` class to query the model and return a response.

2. **Run the Bot**:
   - Start your bot to make it available in your Discord server.

3. **Ask Questions**:
   - Use the `!ask` command to interact with the trained model and get answers.