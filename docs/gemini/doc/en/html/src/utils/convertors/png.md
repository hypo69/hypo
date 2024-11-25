html
<h1>Module: hypotez/src/utils/convertors/png.py</h1>

<h2>Overview</h2>
<p>This module provides functionalities for converting text to PNG images using the Pillow library. It allows specifying various parameters like output directory, font, canvas size, padding, colors, and logging level.  The module includes error handling and logging mechanisms.</p>

<h2>Classes</h2>

<h3><code>TextToImageGenerator</code></h3>

<p><strong>Description</strong>: A class for generating PNG images from text lines. It handles various aspects of image generation, including determining paths, positioning text, creating images with custom parameters, and managing the logging process.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>: Initializes the class with default settings for output directory, canvas size, padding, background color, text color, and logging level.</li>
  <li><code>generate_images</code>: Generates PNG images from a list of text lines. Accepts various parameters to customize the output. This method handles existing file checks (and skips if clobber option is not true), image generation, and saving of images to the specified directory.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>lines</code> (List[str]): The list of text lines to generate images from.</li>
          <li><code>output_dir</code> (str | Path, optional): Output directory for saving images. Defaults to "./output".</li>
          <li><code>font</code> (str | ImageFont.ImageFont, optional): Font to use for the text. Defaults to "sans-serif".</li>
          <li><code>canvas_size</code> (Tuple[int, int], optional): Size of the canvas in pixels. Defaults to (1024, 1024).</li>
          <li><code>padding</code> (float, optional): Percentage of canvas size to use as a blank border. Defaults to 0.10.</li>
          <li><code>background_color</code> (str, optional): Background color for the images. Defaults to "white".</li>
          <li><code>text_color</code> (str, optional): Color of the text. Defaults to "black".</li>
          <li><code>log_level</code> (int | str | bool, optional): Logging verbosity level. Defaults to "WARNING".</li>
          <li><code>clobber</code> (bool, optional): If True, overwrites existing files. Defaults to False.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li>List[Path]: A list of paths to the generated PNG images.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>generate_png</code>: Creates a single PNG image from the given text with custom parameters.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>text</code> (str): Text to be rendered.</li>
          <li><code>canvas_size</code> (Tuple[int, int]): Size of the canvas.</li>
          <li><code>padding</code> (float): Padding percentage.</li>
          <li><code>background_color</code> (str): Background color.</li>
          <li><code>text_color</code> (str): Text color.</li>
          <li><code>font</code> (str | ImageFont.ImageFont): Font to be used.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li>Image: The generated PNG image object.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>center_text_position</code>: Calculates the coordinates to center text on the canvas.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>draw</code> (ImageDraw.Draw): ImageDraw object.</li>
          <li><code>text</code> (str): Text to be rendered.</li>
          <li><code>font</code> (ImageFont.ImageFont): Font to use.</li>
          <li><code>canvas_size</code> (Tuple[int, int]): Size of the canvas.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li>Tuple[int, int]: Centered coordinates for the text.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><code>overlay_images</code>: Overlays one PNG image on top of another at a specified position and with adjustable alpha transparency.
    <ul>
      <li><strong>Parameters</strong>:
        <ul>
          <li><code>background_path</code> (str | Path): Path to the background image.</li>
          <li><code>overlay_path</code> (str | Path): Path to the overlay image.</li>
          <li><code>position</code> (tuple[int, int], optional): Overlay position. Defaults to (0, 0).</li>
          <li><code>alpha</code> (float, optional): Transparency of the overlay. Defaults to 1.0.</li>
        </ul>
      </li>
      <li><strong>Returns</strong>:
        <ul>
          <li>Image: The resulting image with the overlay.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>


<h2>Functions</h2>

<h3><code>webp2png</code></h3>

<p><strong>Description</strong>: Converts a WEBP image to PNG format.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>webp_path</code> (str): Path to the input WEBP file.</li>
  <li><code>png_path</code> (str): Path to save the converted PNG file.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li>bool: True if conversion successful, otherwise None.</li>
</ul>


</ul>