Ogg Converter Module
=====================

This module provides a class for converting OGG audio files to MP3 and downloading OGG audio from URLs.

.. automodule:: ogg
    :members:
    :undoc-members:
    :show-inheritance:

Classes
-------

.. autoclass:: ogg.OggConverter
    :members:
    :special-members: __init__
    :show-inheritance:
    
    .. automethod:: ogg.OggConverter.toMp3
        :noindex:
        :special-members: __init__
        :show-inheritance:

        :param input: (str): Path to the input OGG file.
        :param output: (str): Name for the output MP3 file.

        :returns: (str): Path to the output MP3 file. Returns the path to the created MP3 file.  Returns None if an error occurs during conversion.


    .. automethod:: ogg.OggConverter.create
        :noindex:
        :special-members: __init__
        :show-inheritance:

        :param url: (str): URL of the audio file to download.
        :param filename: (str): Name for the downloaded OGG file.

        :returns: (str): Path to the downloaded OGG file. Returns the path to the downloaded OGG file. Returns None if an error occurs during download.