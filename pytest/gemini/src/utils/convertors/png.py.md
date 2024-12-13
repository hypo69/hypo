```python
import pytest
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from hypotez.src.utils.convertors.png import TextToImageGenerator, webp2png


@pytest.fixture
def image_generator():
    """Provides an instance of TextToImageGenerator for tests."""
    return TextToImageGenerator()

@pytest.fixture
def temp_output_dir(tmp_path):
    """Provides a temporary output directory for tests."""
    return tmp_path / "output"

@pytest.fixture
def sample_font():
    """Provides a sample font path."""
    return "arial.ttf"


@pytest.fixture
def sample_image(tmp_path):
    """Provides a sample image for overlay tests."""
    image_path = tmp_path / "sample.png"
    img = Image.new("RGB", (100, 100), "white")
    img.save(image_path)
    return image_path


# Tests for TextToImageGenerator.generate_images
@pytest.mark.asyncio
async def test_generate_images_valid_input(image_generator, temp_output_dir):
    """Checks correct image generation with valid inputs."""
    lines = ["Test Line 1", "Test Line 2"]
    images = await image_generator.generate_images(lines, output_dir=temp_output_dir)
    assert len(images) == 2
    for line in lines:
        assert (temp_output_dir / f"{line}.png").exists()

@pytest.mark.asyncio
async def test_generate_images_default_output_dir(image_generator, tmp_path):
    """Checks image generation with the default output directory."""
    lines = ["Default Output"]
    images = await image_generator.generate_images(lines)
    assert len(images) == 1
    assert (Path("./output") / "Default Output.png").exists()
    # Cleanup default output dir
    import shutil
    shutil.rmtree(Path("./output"))

@pytest.mark.asyncio
async def test_generate_images_custom_settings(image_generator, temp_output_dir, sample_font):
    """Checks image generation with custom settings."""
    lines = ["Custom Settings"]
    canvas_size = (200, 100)
    padding = 0.2
    background_color = "red"
    text_color = "blue"
    images = await image_generator.generate_images(
        lines,
        output_dir=temp_output_dir,
        font=sample_font,
        canvas_size=canvas_size,
        padding=padding,
        background_color=background_color,
        text_color=text_color,
    )
    assert len(images) == 1
    img_path = temp_output_dir / "Custom Settings.png"
    assert img_path.exists()

    img = Image.open(img_path)
    assert img.size == canvas_size


@pytest.mark.asyncio
async def test_generate_images_clobber(image_generator, temp_output_dir):
    """Checks that existing files are overwritten when clobber is True."""
    lines = ["Clobber Test"]
    img_path = temp_output_dir / "Clobber Test.png"
    img_path.touch()
    assert img_path.exists()
    await image_generator.generate_images(lines, output_dir=temp_output_dir, clobber=True)
    assert img_path.exists()


@pytest.mark.asyncio
async def test_generate_images_skip_existing(image_generator, temp_output_dir):
    """Checks that existing files are skipped when clobber is False."""
    lines = ["Skip Test"]
    img_path = temp_output_dir / "Skip Test.png"
    img_path.touch()
    assert img_path.exists()
    images = await image_generator.generate_images(lines, output_dir=temp_output_dir)
    assert len(images) == 0


# Tests for TextToImageGenerator.generate_png
def test_generate_png_valid_input(image_generator, sample_font):
    """Checks correct image generation with valid inputs."""
    text = "Test Text"
    canvas_size = (200, 100)
    padding = 0.1
    background_color = "white"
    text_color = "black"

    img = image_generator.generate_png(
        text, canvas_size, padding, background_color, text_color, sample_font
    )
    assert img.size == canvas_size
    assert img.mode == "RGB"

# Tests for TextToImageGenerator.center_text_position
def test_center_text_position_valid_input(image_generator, sample_font):
    """Checks correct text position calculation with valid inputs."""
    img = Image.new("RGB", (200, 100), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(sample_font, size=20)
    text = "Centered Text"
    canvas_size = (200, 100)
    x, y = image_generator.center_text_position(draw, text, font, canvas_size)
    
    text_width, text_height = draw.textsize(text, font=font)
    expected_x = (canvas_size[0] - text_width) // 2
    expected_y = (canvas_size[1] - text_height) // 2
    
    assert x == expected_x
    assert y == expected_y
    
    
# Tests for TextToImageGenerator.overlay_images
def test_overlay_images_valid_input(image_generator, sample_image, tmp_path):
    """Checks correct overlay with valid inputs."""
    background_path = sample_image
    overlay_path = sample_image
    position = (10, 10)
    alpha = 0.5
    result_image = image_generator.overlay_images(
        background_path, overlay_path, position=position, alpha=alpha
    )
    assert isinstance(result_image, Image.Image)

def test_overlay_images_different_sizes(image_generator, sample_image, tmp_path):
    """Checks overlay with different image sizes."""
    background_path = sample_image
    overlay_path = tmp_path / "overlay.png"
    overlay_img = Image.new("RGB", (50, 50), "blue")
    overlay_img.save(overlay_path)
    
    result_image = image_generator.overlay_images(background_path, overlay_path)
    assert isinstance(result_image, Image.Image)
    assert result_image.size == (100, 100)


def test_overlay_images_invalid_alpha(image_generator, sample_image, tmp_path):
    """Checks that exception is not raised and it handles alpha out of range."""
    background_path = sample_image
    overlay_path = sample_image
    result_image = image_generator.overlay_images(background_path, overlay_path, alpha=1.5)
    assert isinstance(result_image, Image.Image)
    result_image_2 = image_generator.overlay_images(background_path, overlay_path, alpha=-0.1)
    assert isinstance(result_image_2, Image.Image)


def test_overlay_images_nonexistent_image(image_generator, tmp_path):
    """Checks exception handling with non-existent image paths."""
    background_path = tmp_path / "nonexistent_background.png"
    overlay_path = tmp_path / "nonexistent_overlay.png"
    with pytest.raises(FileNotFoundError):
        image_generator.overlay_images(background_path, overlay_path)
        
def test_webp2png_valid_input(tmp_path):
    """Checks correct WEBP to PNG conversion."""
    webp_path = tmp_path / "test.webp"
    png_path = tmp_path / "test.png"
    
    # Create a sample webp image
    img = Image.new("RGB", (100, 100), "red")
    img.save(webp_path, "webp")
    
    result = webp2png(str(webp_path), str(png_path))
    assert result is True
    assert png_path.exists()
    converted_img = Image.open(png_path)
    assert converted_img.format == "PNG"

def test_webp2png_nonexistent_file(tmp_path):
    """Checks handling of non-existent WEBP file."""
    webp_path = tmp_path / "nonexistent.webp"
    png_path = tmp_path / "output.png"
    
    result = webp2png(str(webp_path), str(png_path))
    assert result is None
    assert not png_path.exists()
```