import os
import uuid
from PIL import Image, ImageDraw, ImageFont
import io

# Image Creation Functions
def wrap_text(draw, text, font, max_width):
    # Split the text into words
    words = text.split(' ')
    lines = []
    current_line = words[0]
    
    # Loop through the words and create lines
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

def draw_in_center(text, blob, state, font_blob):
    # Load the image# Download the image as bytes
    image_bytes = blob.download_as_bytes()

    # Load the image into PIL
    image = Image.open(io.BytesIO(image_bytes))
    draw = ImageDraw.Draw(image)
    
    # Set font and size
    try:
        # Download the font blob as bytes 
        font_bytes = blob.download_as_bytes() 
        # Load the font into PIL ImageFont 
        font = ImageFont.truetype(io.BytesIO(font_bytes), size=100)
    except IOError:
        print("Font not found. Ensure font is in the directory or provide the correct path.")
        return None
    
    # Determine text color based on state
    color = "white" if state == "night" else "black"
    
    # Get image dimensions
    img_width, img_height = image.size
    
    # Wrap the text to fit the image width
    lines = wrap_text(draw, text, font, img_width - 40)  # 40 is padding on both sides
    
    # Calculate the total text height (sum of heights of each line)
    total_text_height = sum([draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines])
    
    # Calculate vertical position to center the text
    y_position = (img_height - total_text_height) // 2
    
    # Draw each line of text, centered horizontally
    for line in lines:
        # Calculate horizontal position to center each line
        text_width, text_height = draw.textbbox((0, 0), line, font=font)[2:4]
        x_position = (img_width - text_width) // 2
        
        # Draw the text line
        draw.text((x_position, y_position), line, font=font, fill=color)
        
        # Move the vertical position down for the next line
        y_position += text_height
    
    # Return the modified image
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
    print(output_path)
    # Get the original format of the image
    original_format = image.format  # This is 'JPEG', 'PNG', etc.

    # Save the image while preserving its original quality
    if original_format == 'JPEG':
        # Set quality to 95 to maintain high quality
        image.save(output_path, format='JPEG', quality=95, optimize=True)
    elif original_format == 'PNG':
        # Save as PNG without compression loss
        image.save(output_path, format='PNG', compress_level=0)  # compress_level=0 for lossless compression
    else:
        # For other formats (e.g., TIFF), save as is
        image.save(output_path)