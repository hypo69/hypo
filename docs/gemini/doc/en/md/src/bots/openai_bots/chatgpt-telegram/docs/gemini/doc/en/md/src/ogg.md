# Ogg Converter Module Documentation

## Overview

This module provides functionality for converting OGG audio files to MP3 and for downloading OGG audio from a URL.  It utilizes the `fluent-ffmpeg` library for conversion and `axios` for HTTP requests.  Error handling and file cleanup are included.


## Classes

### `OggConverter`

**Description**: This class encapsulates the logic for converting and downloading OGG audio files.

**Methods**:

#### `toMp3`

**Description**: Converts an OGG audio file to MP3 within a given timeframe.

**Parameters**:

- `input` (str): The path to the input OGG file.
- `output` (str): The name for the output MP3 file (without extension).

**Returns**:
- `Promise<string>`: Resolves with the path to the generated MP3 file, or rejects with an error message.

**Raises**:
- `Error`: General error during the conversion process.


#### `create`

**Description**: Downloads an OGG audio file from a given URL and saves it to a specified location.

**Parameters**:

- `url` (str): The URL of the OGG audio file to download.
- `filename` (str): The desired name for the downloaded OGG file (without extension).

**Returns**:
- `Promise<string>`: Resolves with the path to the downloaded OGG file, or rejects with an error message.

**Raises**:
- `Error`: General error during the download process.


## Functions

(None)


## Module Exports

- `ogg`: An instance of the `OggConverter` class, ready for use.