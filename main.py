import time
from typing import Dict, List

from PIL import Image

def convert_to_rgb(file_to_convert: str, show_duration: bool = False) -> Dict[str, List[str]]:
    im = Image.open(file_to_convert)  # Opens and loads the image.
    pix = im.load()

    rgb_values: Dict[str, List[str]] = {}  # Sets the RGB value list.
    rgb_values_temp: List[str] = []

    start_time = time.time()  # Start timer.
    metadata = str(im.size)
    
    for i in range(im.size[1]):  # Vertical loop.
        for z in range(im.size[0]):  # Horizontal loop.
            rgb_values_temp.append(str(pix[z, i]))  # Append the RGB value for the pixel to a list.

    rgb_values['metadata'] = metadata
    rgb_values['rgbValues'] = rgb_values_temp

    if show_duration:
        print(f"Duration: {(time.time() - start_time) * 1000:.2f} ms")  # Shows duration.

    return rgb_values

def convert_to_image(file_to_convert: str, show_duration: bool = False) -> None:
    with open(file_to_convert, 'r') as f:  # Opens and reads the file to be converted.
        rgb_data = eval(f.read())

    metadata = list(eval(rgb_data['metadata']))  # Obtains the metadata of the image.
    im = Image.new(size=tuple(metadata), mode='RGB')  # Makes a new image, with the same size as the metadata.
    start_time = time.time()  # Start timer.
    
    for i in range(metadata[1]):
        for y in range(metadata[0]):
            rgb_value = eval(rgb_data['rgbValues'][i * metadata[0] + y])  # Evaluates the RGB value for given pixel.
            im.putpixel((y, i), rgb_value)  # Puts the evaluated RGB value on to the given pixel.
    if show_duration:
        print(f"Duration: {(time.time() - start_time) * 1000:.2f} ms")  # Shows duration if told to do so.
    im.save("converted_image.png", format="png")  # Saves the converted image.

def inputs(string_to_be_added: str = None) -> Tuple[str, bool]:
    file_to_convert = input(f"{string_to_be_added}\n> ")  # Input file to be converted.
    show_duration = input("Would you like to see the duration taken? (\"True\" or \"False\")\n> ")

    if show_duration.lower() not in ["true", "false"]:  # Ensures the entered value is a boolean.
        raise ValueError("Entered value is not
