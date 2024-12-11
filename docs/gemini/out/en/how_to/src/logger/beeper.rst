rst
How to use the Beeper class
========================================================================================

Description
-------------------------
This code defines a `Beeper` class for generating sound signals, primarily for logging purposes. It allows customizing the type of signal (e.g., success, error) and its frequency and duration. The `silent_mode` decorator allows silencing these signals. The class utilizes the `winsound` module for sound generation on Windows.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports `asyncio`, `winsound`, `time`, `enum`, and `typing`. It also defines a dictionary `note_freq` mapping musical notes to their frequencies.


2. **Define the `BeepLevel` enum:** This defines different types of signals (`SUCCESS`, `INFO`, `ATTENTION`, etc.). Each signal type corresponds to a list of notes and durations, for a specific musical melody.


3. **Implement the `BeepHandler` class:**  This class handles emitting signals based on the log level. It calls the `play_sound` method with specific frequencies and durations for different log levels (error, warning, info) and a default sound for other cases.


4. **Define the `silent_mode` decorator:** This decorator allows temporarily disabling sound generation.


5. **Implement the `Beeper` class:** This class is the core sound generation component.
    - It has a class-level variable `silent` to control the silent mode.
    - The `beep` method is the main function for generating the signal. It takes a `level` (a `BeepLevel` enum value or a string), a `frequency`, and a `duration` as input.
    - It translates strings for the `level` to enum values.
    - It iterates through the defined notes and durations for the specified `level`.
    - It calls `winsound.Beep` to generate the sound signal.
    - It handles potential `winsound` errors.

6. **Example Usage:** The code demonStartes how to use the `Beeper` class to generate different sound signals.


Usage example
-------------------------
.. code-block:: python

    import asyncio
    from hypotez.src.logger.beeper import Beeper, BeepLevel

    # Set silent mode to False
    Beeper.silent = False

    async def main():
        # Generate a success beep
        await Beeper.beep(BeepLevel.SUCCESS)
        # Generate an error beep
        await Beeper.beep(BeepLevel.ERROR)

    if __name__ == "__main__":
        asyncio.run(main())

    # Example usage with string input:
    async def main():
        await Beeper.beep('warning')

    if __name__ == "__main__":
        asyncio.run(main())