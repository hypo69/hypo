rst
How to use the OpenAI API wrapper
========================================================================================

Description
-------------------------
This code defines a JavaScript class `OpenAI` that provides an interface for interacting with the OpenAI API. It includes methods for sending chat messages and transcribing audio files.  The class uses the `openai` library to handle API calls and manages error handling for these calls.  It also incorporates configuration using the `config` module to fetch the OpenAI API key.

Execution steps
-------------------------
1. **Import necessary modules**: The code imports the `Configuration`, `OpenAIApi`, and `createReadStream` modules from the `openai` and `fs` libraries, respectively. It also imports the `config` module for accessing the OpenAI API key.

2. **Define the `OpenAI` class**: The class `OpenAI` is defined with a constructor that takes the API key as input.  It initializes the `OpenAIApi` object, storing it in the `this.openai` property. This object is used to make API calls to the OpenAI service.

3. **Define the `chat` method**: This method takes an array of messages as input (messages object should contain role and content for each message).  It sends a chat completion request to the OpenAI API using the `createChatCompletion` method, specifying the 'gpt-3.5-turbo' model.  It handles potential errors during the API call.

4. **Define the `transcription` method**: This method takes the filepath of an audio file as input. It reads the audio file using `createReadStream` and sends a transcription request to the OpenAI API using the `createTranscription` method, specifying the 'whisper-1' model. It handles potential errors during the API call.

5. **Create an instance of the `OpenAI` class**: An instance of the `OpenAI` class is created, passing the OpenAI API key obtained from the `config` module.

6. **Export the OpenAI instance**: The `openai` instance is exported, making it available for use in other parts of the application.

Usage example
-------------------------
.. code-block:: javascript
    
    // Assuming 'config.js' exists with the following contents:
    // export default {
    //   get: (key) => {
    //     if (key === 'OPENAI_KEY') {
    //       return 'YOUR_OPENAI_API_KEY';
    //     }
    //     return null;
    //   },
    // };

    import { openai } from './openai';
    
    async function runExample() {
        const messages = [
            { role: 'user', content: 'What is the capital of France?' },
        ];

        const response = await openai.chat(messages);
        console.log(response.content); // Outputs the assistant's response

        // Example with transcription
        const filepath = 'audio.wav'; // Replace with the actual file path
        const transcription = await openai.transcription(filepath);
        console.log(transcription); // Outputs the transcribed text
    }

    runExample();