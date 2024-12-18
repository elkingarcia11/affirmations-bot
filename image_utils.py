from PIL import Image, ImageDraw, ImageFont
import random
import os

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

# Function to generate image with text
def generate_image(text, font_blob):
    gradient_pairs = [
        ("#e0f7fa", "#00796b"),  # Serene Blue
        ("#f3e5f5", "#6a1b9a"),  # Radiant Purple
        ("#e8f5e9", "#2e7d32"),  # Peaceful Green
        ("#fffde7", "#f57f17"),  # Warm Yellow
        ("#fce4ec", "#ad1457"),  # Gentle Pink
        ("#efebe9", "#4e342e"),  # Earthy Brown
        ("#fafafa", "#424242"),  # Calming Gray
        ("#fff3e0", "#e65100"),  # Energizing Orange
        ("#e0f2f1", "#004d40"),  # Tranquil Teal
        ("#e3f2fd", "#0d47a1"),  # Mystic Blue
        ("#ede7f6", "#4527a0"),  # Spiritual Violet
        ("#fbe9e7", "#bf360c"),  # Cozy Coral
        ("#f9fbe7", "#827717"),  # Earthly Olive
        ("#e8eaf6", "#1a237e"),  # Deep Indigo
        ("#edeff2", "#2c3e50"),  # Sophisticated Slate
        ("#ffebee", "#b71c1c"),  # Rose Glow
        ("#e1f5fe", "#01579b")   # Crystal Blue
    ]
    background_color, text_color = random.choice(gradient_pairs)

    # Image dimensions
    width, height = 1080, 1080
    image = Image.new("RGB", (width, height), background_color)
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
    lines = wrap_text(draw, text, font, width - 80)  # 80 is padding on both sides

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


# Add Image To Filepath
def add_image_to(image, output_filepath):
    # Ensure the output folder exists, if not, create it
    if not os.path.exists(output_filepath):
        os.makedirs(output_filepath)
    
    # Generate a unique filename using UUID (v4)
    unique_filename = "image.jpg"
    
    # Save the modified image with a unique name
    output_path = os.path.join(output_filepath, unique_filename)

    # Save the image while preserving its original quality
    image.save(output_path)