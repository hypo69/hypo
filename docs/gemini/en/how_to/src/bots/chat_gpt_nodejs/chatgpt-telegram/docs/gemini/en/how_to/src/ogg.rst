rst
How to use the OggConverter class
========================================================================================

Description
-------------------------
This code defines a class `OggConverter` for converting Ogg files to MP3 and downloading Ogg files from a URL.  It utilizes the `fluent-ffmpeg` library for MP3 conversion and handles potential errors during both conversion and download.

Execution steps
-------------------------
1. **Import necessary modules:** The code starts by importing necessary modules like `axios`, `fs` (for file streams), `path` (for file resolution), `url` (for URL handling), `fluent-ffmpeg`,  `ffmpeg-installer`, and a custom `removeFile` function (likely from a separate file `utils.js`).

2. **Set FFmpeg path:** The `ffmpeg.setFfmpegPath(installer.path)` line ensures that the `fluent-ffmpeg` library knows where to find the FFmpeg executable. This is crucial for the conversion process.

3. **OggConverter Class:** The code defines a class `OggConverter` to encapsulate the conversion logic:
    a. **Constructor:** Initializes the FFmpeg path in the class constructor.
    b. **toMp3 Method:** This method handles converting an Ogg file to MP3.
        i. It takes the input Ogg file path (`input`) and desired output filename (`output`) as arguments.
        ii. It resolves the output MP3 file path using `resolve`.
        iii. It uses a promise to handle the asynchronous FFmpeg conversion process, setting a 30-second time limit (`-t 30`).
        iv. It handles potential errors during the conversion process by logging an error message and rejecting the promise.
        v. Upon successful conversion, the original Ogg file is removed and the path of the newly created MP3 file is resolved.
    c. **create Method:** This method handles downloading an Ogg file from a specified URL (`url`) and saving it with a given filename (`filename`).
        i. It constructs the path to the output Ogg file (`oggPath`).
        ii. It uses `axios` to download the file from the given URL and handles the stream, ensuring the downloaded file is saved to disk.
        iii. It uses a promise to handle the asynchronous download process.
        iv. Upon successful download, it resolves with the path of the downloaded Ogg file.
        v. It logs error messages if any issues occur during the download.

4. **Export the OggConverter instance:** The line `export const ogg = new OggConverter()` creates an instance of the `OggConverter` class (named `ogg`) and exports it, making it available for use in other parts of the project.


Usage example
-------------------------
.. code-block:: javascript
    
    import { ogg } from './ogg.js'; // Assuming this file is named ogg.js

    async function convertAndDownload() {
        const inputFilePath = '/path/to/your/input.ogg';
        const outputFilePath = 'output';
        const url = 'https://example.com/audio.ogg';
        const fileName = 'downloadedFile';

        try {
          const mp3Path = await ogg.toMp3(inputFilePath, outputFilePath);
          console.log('MP3 conversion successful:', mp3Path);

          const oggPath = await ogg.create(url, fileName);
          console.log('Ogg download successful:', oggPath);
        } catch (error) {
          console.error('Error:', error);
        }
    }

    convertAndDownload();