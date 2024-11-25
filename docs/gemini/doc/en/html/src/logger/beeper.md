html
<h1>Module: hypotez/src/logger/beeper.py</h1>

<h2>Overview</h2>
<p>This module provides a beeper functionality for generating audio alerts based on different log levels.</p>

<h2>Constants</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: Defines the operating mode of the beeper (currently 'dev').</p>

<h2>Classes</h2>

<h3><code>BeepLevel</code></h3>

<p><strong>Description</strong>: An enumeration representing different log levels and corresponding melodies.</p>

<p><strong>Members</strong>:</p>
<ul>
  <li><code>SUCCESS</code>: A list of notes and durations for a success beep.</li>
  <li><code>INFO_LONG</code>: A list of notes and durations for a long info beep.</li>
  <li><code>INFO</code>: A list of notes and durations for an info beep.</li>
  <li><code>ATTENTION</code>: A list of notes and durations for an attention beep.</li>
  <li><code>WARNING</code>: A list of notes and durations for a warning beep.</li>
  <li><code>DEBUG</code>: A list of notes and durations for a debug beep.</li>
  <li><code>ERROR</code>: A list of notes and durations for an error beep.</li>
  <li><code>LONG_ERROR</code>: A list of notes and durations for a long error beep.</li>
  <li><code>CRITICAL</code>: A list of notes and durations for a critical beep.</li>
  <li><code>BELL</code>: A list of notes and durations for a bell beep.</li>
</ul>


<h3><code>BeepHandler</code></h3>

<p><strong>Description</strong>: Handles the emission of beeps based on log records.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>emit(self, record)</code>:
    <p><strong>Description</strong>: Processes a log record and plays the corresponding beep sound.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>record</code> (dict): The log record containing the log level.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: If there's an error playing the sound.</li>
    </ul>
  </li>

  <li><code>play_sound(self, frequency: int, duration: int)</code>: 
     (Implied, not explicitly defined in the code snippet, but likely exists within the class.)
	  <p><strong>Description</strong>: Plays a sound with a given frequency and duration.</p>
	  <p><strong>Parameters</strong>:</p>
		<ul>
			<li><code>frequency</code> (int): The frequency of the sound.</li>
			<li><code>duration</code> (int): The duration of the sound.</li>
		</ul>
  </li>
  
    <li><code>play_default_sound(self)</code>:
    	(Implied, not explicitly defined in the code snippet, but likely exists within the class.)
	  <p><strong>Description</strong>: Plays the default beep sound.</p>
  </li>
</ul>



<h3><code>Beeper</code></h3>

<p><strong>Description</strong>: The main beeper class.</p>

<p><strong>Attributes</strong>:</p>
<ul>
<li><code>silent</code> (bool): A flag indicating whether the beeper should be silent.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>beep(level: BeepLevel | str = BeepLevel.INFO, frequency: int = 400, duration: int = 1000) -> None</code>:
    <p><strong>Description</strong>: Plays a beep sound based on the specified level.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>level</code> (<code>BeepLevel</code> or <code>str</code>, optional): The log level for the beep. Defaults to <code>BeepLevel.INFO</code>. Can be a string like "success", or an enum value.</li>
      <li><code>frequency</code> (int, optional): The frequency of the beep. Defaults to 400.</li>
      <li><code>duration</code> (int, optional): The duration of the beep. Defaults to 1000.</li>
    </ul>
	<p><strong>Returns</strong>:</p>
    <ul>
      <li><code>None</code>: Does not return a value.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>Exception</code>: If there's an error playing the sound.</li>
    </ul>
  </li>
</ul>

<h2>Functions</h2>

<h3><code>silent_mode(func)</code></h3>

<p><strong>Description</strong>: A decorator function to control the silent mode of the beeper.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>func</code> (function): The function to be decorated.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>A wrapper function that checks the silent mode before calling the decorated function.</li>
</ul>


<p><strong>Note</strong>: The documentation for some methods (e.g., play_sound, play_default_sound) are implied since they aren't explicitly defined in the provided code snippet.  A complete HTML documentation would need to include all these details if these methods are indeed part of the class.</p>