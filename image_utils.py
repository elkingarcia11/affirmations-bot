from PIL import Image, ImageDraw, ImageFont
import random
import os
import io

# Wrap text function
def wrap_text(draw, text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + ' ' + word
        width, _ = draw.textbbox((0, 0), test_line, font=font)[2:4]

        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)  # Add the last line
    return lines

# Function to generate image from list of colors
def generate_image_from_colors(text, font_blob):
    colors = [
        "#e0f7fa",  # Serene Blue
        "#f3e5f5",  # Radiant Purple
        "#e8f5e9",  # Peaceful Green
        "#fffde7",  # Warm Yellow
        "#fce4ec",  # Gentle Pink
        "#efebe9",  # Earthy Brown
        "#fafafa",  # Calming Gray
        "#fff3e0",  # Energizing Orange
        "#e0f2f1",  # Tranquil Teal
        "#e3f2fd",  # Mystic Blue
        "#ede7f6",  # Spiritual Violet
        "#fbe9e7",  # Cozy Coral
        "#f9fbe7",  # Earthly Olive
        "#e8eaf6",  # Deep Indigo
        "#edeff2",  # Sophisticated Slate
        "#ffebee",  # Rose Glow
        "#e1f5fe",  # Crystal Blue
    ]
    background_color = random.choice(colors)

    # Image dimensions
    width, height = 1080, 1080
    image = Image.new("RGB", (width, height), background_color)
    return generate_image(image, width, height, text, font_blob)

def generate_image_from_blob(blob, text, font_blob):

    # Download the blob content as bytes
    blob_data = blob.download_as_bytes()
    
    # Load the image using Pillow
    image = Image.open(io.BytesIO(blob_data)).convert("RGBA")  # Ensure RGBA format for transparency
    
    # Image dimensions
    width, height = 1080, 1080
    return generate_image(image, width, height, text, font_blob)

def generate_image(image, width, height, text, font_blob):
    draw = ImageDraw.Draw(image)
    # Set font and size
    try:
        output_path = os.path.join("/tmp/", "font.ttf")
        font_blob.download_to_filename(output_path)
        font = ImageFont.truetype(output_path, size=100)
    except IOError:
        print("Font not found. Ensure font is in the directory or provide the correct path.")
        return None

    # Wrap the text to fit the image width
    lines = wrap_text(draw, text, font, width - 160)  # 120 is padding on both sides

    # Define the padding between lines
    padding = 10  # Padding between lines

    # Calculate the height of each line
    line_heights = [draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines]
    
    # Calculate the total height of the text block including padding
    total_text_height = sum(line_heights) + (len(lines) - 1) * padding
    
    # Calculate the vertical position to center the text block
    y_position = (height - total_text_height) // 2

    # Draw each line of text, centered horizontally
    for line, line_height in zip(lines, line_heights):
        text_width, _ = draw.textbbox((0, 0), line, font=font)[2:4]
        x_position = (width - text_width) // 2  # Center horizontally

        draw.text((x_position, y_position), line, font=font, fill="#000000")

        # Move the vertical position down for the next line
        y_position += line_height + padding  # Add padding between lines

    return image