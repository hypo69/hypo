html
<h1>Module: hypotez/src/utils/convertors/tts.py</h1>

<h2>Overview</h2>
<p>This module provides functions for speech recognition (converting audio to text) and text-to-speech (converting text to audio) using various libraries.  It includes error handling and logging.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operation mode (currently 'dev').</p>


<h2>Functions</h2>

<h3><code>speech_recognizer</code></h3>

<p><strong>Description</strong>: Downloads an audio file (from URL or local path) and recognizes the speech using Google Speech Recognition. Converts OGG to WAV format.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>audio_url</code> (str, optional): URL of the audio file to be downloaded. Defaults to <code>None</code>.</li>
  <li><code>audio_file_path</code> (Path, optional): Local path to an audio file. Defaults to <code>None</code>.</li>
  <li><code>language</code> (str): Language code for recognition (e.g., 'ru-RU'). Defaults to 'ru-RU'.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: Recognized text from the audio or an error message.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
print(recognized_text)  # Output: "Привет"
</code></pre>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during the process.</li>
  <li><code>sr.UnknownValueError</code>: Google Speech Recognition cannot understand the audio.</li>
  <li><code>sr.RequestError</code>: Could not request results from Google Speech Recognition service.</li>
</ul>


<h3><code>text2speech</code></h3>

<p><strong>Description</strong>: Converts text to speech and saves the audio as a WAV file.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>text</code> (str): The text to be converted.</li>
  <li><code>lang</code> (str, optional): Language code for the speech (e.g., 'ru'). Defaults to 'ru'.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>str</code>: Path to the generated WAV audio file or an error message.</li>
</ul>

<p><strong>Example Usage</strong>:</p>
<pre><code class="language-python">audio_path = await text2speech('Привет', lang='ru')
print(audio_path)  # Output: "/tmp/response.wav"  (or similar)
</code></pre>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>: Any exception during the process.</li>
</ul>


<h2>Imports</h2>
<ul>
  <li><code>pathlib</code>: For path manipulation.</li>
  <li><code>tempfile</code>: For creating temporary files.</li>
  <li><code>asyncio</code>: For asynchronous operations.</li>
  <li><code>requests</code>: For downloading files.</li>
  <li><code>speech_recognition</code>: For speech recognition.</li>
  <li><code>pydub</code>: For audio manipulation.</li>
  <li><code>gtts</code>: For text-to-speech conversion.</li>
  <li><code>src.utils.jjson</code>: For JSON handling (likely for custom JSON handling).</li>
  <li><code>src.logger</code>: For logging.</li>
</ul>