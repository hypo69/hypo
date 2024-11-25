html
<h1>Module: hypotez/src/ai/gemini/generative_ai.py</h1>

<h2>Overview</h2>
<p>This module provides a class for interacting with Google Generative AI models.  It handles sending requests, receiving responses, and saving dialogues to text and JSON files.</p>

<h2>Classes</h2>

<h3><code>GoogleGenerativeAI</code></h3>

<p><strong>Description</strong>: A class for interacting with Google Generative AI models, including sending requests, receiving responses, and saving dialogue history.  This class manages the API key, model selection, and configuration.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>MODELS (List[str])</code>: A list of available AI models.</li>
  <li><code>api_key (str)</code>: The API key for accessing the generative model.</li>
  <li><code>model_name (str)</code>: The name of the model to use.</li>
  <li><code>generation_config (Dict)</code>: Configuration for generation.</li>
  <li><code>mode (str)</code>: The operating mode (e.g., 'debug' or 'production').</li>
  <li><code>dialogue_log_path (Optional[Path])</code>: Path for logging dialogues.</li>
  <li><code>dialogue_txt_path (Optional[Path])</code>: Path to save dialogue text files.</li>
  <li><code>history_dir (Path)</code>: Directory for storing history.</li>
  <li><code>history_txt_file (Optional[Path])</code>: Path to store history in text format.</li>
  <li><code>history_json_file (Optional[Path])</code>: Path to store history in JSON format.</li>
  <li><code>model (Optional[genai.GenerativeModel])</code>: The Google Generative AI model object.</li>
  <li><code>system_instruction (Optional[str])</code>: System-level instructions for the model's behavior.</li>
</ul>


<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__(self, api_key: str, model_name: Optional[str] = None, generation_config: Optional[Dict] = None, system_instruction: Optional[str] = None, **kwargs)</code>: Initializes the GoogleGenerativeAI model with additional configurations.</li>
   <li><code>__post_init__(self)</code>: Method for initializing the model and other parameters after the instance is created.</li>
  <li><code>config()</code>: Retrieves configuration from a configuration file.</li>
  <li><code>_save_dialogue(self, dialogue: list)</code>: Saves the dialogue to text and JSON files, handling file size management.</li>
  <li><code>ask(self, q: str, attempts: int = 15) -> Optional[str]</code>: Sends a text request to the model and returns the response, handling potential errors and retries.</li>
  <li><code>describe_image(self, image_path: Path) -> Optional[str]</code>: Generates a description for an image, sending the image data to the model.</li>
</ul>


<h2>Functions</h2>

<h3><code>chat()</code></h3>

<p><strong>Description</strong>: Launches an interactive chat session with the AI model.  Allows users to ask questions and receive responses.</p>


<p><strong>Example Usage</strong>:</p>
<pre><code>python
chat() 
</code></pre>