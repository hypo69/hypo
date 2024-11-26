How to use the `ogg.js` file to convert OGG audio files to MP3 and download/save audio from URLs.

This JavaScript file, `ogg.js`, provides classes for converting OGG audio files to MP3 and downloading audio from URLs.  It relies on `fluent-ffmpeg` for the conversion and `axios` for the downloads.

**1. Installation:**

Before using the code, you need to install the required packages:

```bash
npm install axios fluent-ffmpeg @ffmpeg-installer/ffmpeg fs
```

**2. Using `ogg.js` to convert OGG to MP3:**

```javascript
import { ogg } from './ogg.js'; // Import the OggConverter class

// Example usage:
const inputOggPath = '/path/to/your/input.ogg';
const outputMp3Path = '/path/to/your/output.mp3';
const audioFilename = 'example-audio'

ogg.toMp3(inputOggPath, audioFilename)
  .then((outputPath) => {
    console.log(`Conversion successful! Output saved to: ${outputPath}`);
  })
  .catch((error) => {
    console.error(`Conversion failed: ${error}`);
  });
```

*   **`inputOggPath`:** Replace `/path/to/your/input.ogg` with the actual path to your OGG audio file.
*   **`outputMp3Path`:**  Replace `/path/to/your/output.mp3` with the desired path for the output MP3 file.
*   This code converts the input OGG file to MP3 and overwrites any existing file with the same name. 
*   Crucially, it will *remove the input OGG file* after a successful conversion.  If you need to keep the original OGG, adjust the code to not remove it.

**3. Using `ogg.js` to download and save audio from a URL:**

```javascript
import { ogg } from './ogg.js';

const url = 'https://example.com/audio.ogg';
const filename = 'downloaded-audio'; // Choose a name for your file

ogg.create(url, filename)
  .then((outputPath) => {
    console.log(`Download and save successful!  File saved to: ${outputPath}`);
  })
  .catch((error) => {
    console.error(`Download and save failed: ${error}`);
  });
```

*   **`url`:** Replace `'https://example.com/audio.ogg'` with the actual URL of the audio file.
*   **`filename`:**  The name you want for the downloaded file (e.g., 'myAudio').  Note that the filename extension is set automatically to `.ogg`
*   The downloaded audio is saved to a file named `filename.ogg` in a `voices` subdirectory relative to the `src/` directory.


**Important Considerations:**

*   **Error Handling:** The `try...catch` blocks are crucial for handling potential errors during conversions and downloads.  Always check the returned promises for errors.
*   **File Paths:** Ensure the file paths you use are correct and the necessary directories exist.  The `resolve` function is used to handle file paths more robustly.
*   **ffmpeg Installation:** Make sure the `ffmpeg` executable is installed and available in your system's PATH. The package `@ffmpeg-installer/ffmpeg` helps with this.  If you encounter issues finding ffmpeg, refer to that package's documentation.
*   **`-t 30`:**  This limits the conversion to the first 30 seconds of the input audio. Adjust this if you need to process the entire file.


This expanded explanation provides a more comprehensive guide for using the `ogg.js` file, including practical examples, error handling, and crucial points to keep in mind. Remember to replace placeholders with your actual file paths and URLs.