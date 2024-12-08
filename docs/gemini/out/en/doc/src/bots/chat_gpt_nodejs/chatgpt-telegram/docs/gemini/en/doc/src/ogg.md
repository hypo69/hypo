# OggConverter Class Documentation

## Overview

This module provides a class `OggConverter` for converting Ogg Vorbis audio files to MP3 and downloading Ogg audio from a URL. It utilizes the `fluent-ffmpeg` library for MP3 conversion and Node.js built-in modules for file system operations and HTTP requests.

## Table of Contents

- [OggConverter Class](#oggconverter-class)
    - [toMp3 Method](#tomp3-method)
    - [create Method](#create-method)


## OggConverter Class

### Description

The `OggConverter` class handles the conversion and download of Ogg Vorbis audio files. It uses `fluent-ffmpeg` for conversion and `axios` for HTTP requests.

### Methods

#### `toMp3`

**Description**: Converts an Ogg file to MP3.

**Parameters**:
- `input` (string): The path to the input Ogg file.
- `output` (string): The desired name for the output MP3 file (without extension).

**Returns**:
- `Promise<string | null>`: A `Promise` that resolves to the path of the output MP3 file if successful, or `null` if an error occurs.

**Raises**:
- `Error`: Any error during the conversion process.


#### `create`

**Description**: Downloads an Ogg Vorbis audio file from a given URL and saves it to the specified file path.

**Parameters**:
- `url` (string): The URL of the Ogg Vorbis audio file.
- `filename` (string): The desired name for the downloaded Ogg file (without extension).

**Returns**:
- `Promise<string | null>`: A `Promise` that resolves to the path of the downloaded Ogg file if successful, or `null` if an error occurs.

**Raises**:
- `Error`: Any error during the download process.


## Module Export

The module exports an instance of the `OggConverter` class named `ogg`. This allows other modules to utilize its functionalities without instantiating it directly.