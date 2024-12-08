rst
How to use the bot commands
========================================================================================

Description
-------------------------
This section provides instructions on how to use various commands available within the bot.  Each command performs a specific action, ranging from greeting users to training and testing machine learning models.

Execution steps
-------------------------
The bot offers a suite of commands to interact with it.  Each command has a specific purpose and expects input parameters in a predetermined format.  Refer to the command descriptions for details.

1. **!hi**:  This command greets the user.  No additional parameters are required.

2. **!train <data> <data_dir> <positive> <attachment>**: This command trains a model using the specified data.  The `<data>` parameter should be used for a single file path.  The `<data_dir>` parameter should be a path to a directory containing data.  `<positive>` indicates whether the data is positive or negative, and `<attachment>` specifies a file attachment if needed.

3. **!test <test_data>**: This command tests the trained model with provided JSON test data.  The `<test_data>` parameter is the file path to the JSON test data.

4. **!archive <directory>**: This command archives the files within the specified directory.  The `<directory>` parameter is the path to the directory to be archived.

5. **!select_dataset <path_to_dir_positive> <positive>**: This command selects a dataset for training.  The `<path_to_dir_positive>` parameter identifies the directory containing the positive examples.  The `<positive>` parameter confirms the nature of the dataset (e.g., 'positive').

6. **!instruction**: This command displays the instruction message, providing a list of available commands and their usage.


Usage example
-------------------------
.. code-block:: text

    !hi  # Greets the user

    !train data.txt data_dir positive # Train with a file named 'data.txt', in a folder 'data_dir', assuming 'positive' sentiment

    !test test_data.json # Tests the model with 'test_data.json'