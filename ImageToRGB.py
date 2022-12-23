from PIL import Image
import time

def convertToRGB(fileToConvert, showDuration: bool=False):
    im = Image.open(fileToConvert) # Opens and loads the image.
    pix = im.load() 

    rgbValues = {} # Sets the RGB value list.
    rgbValuesTemp = []

    x = time.time()
    rgbValues['metadata'] = str(im.size)
    for i in range(im.size[1]): # Vertical loop.
        for z in range(im.size[0]): # Horizontal loop.
            rgbValuesTemp.append(str(pix[z, i])) # Append the RGB value for the pixel to a list.

    rgbValues['rgbValues'] = list(rgbValuesTemp)

    if showDuration:
        print(f"{(time.time()-x)*1000} ms") # Shows duration.

    return rgbValues

def convertToImage(fileToConvert: str=None, showDuration: bool=False):
    if fileToConvert is None:
        return None
    x = open(fileToConvert, 'r') # Opens, reads and evaluates the file to be converted.
    fileToConvert = x.read()
    rgbData = eval(fileToConvert)

    metadata = list(eval(rgbData['metadata'])) # Likely is a better method than this. Obtains the metadata of the image.
    im = Image.new(size=tuple(metadata), mode='RGB') # Makes a new image, with the same size as the metadata.
    z = 0
    startTime = time.time() # Starts timer.
    for i in range(metadata[1]):
        for y in range(metadata[0]):
            rgbValue = eval(rgbData['rgbValues'][z]) # Evaluates the RGB value for given pixel.
            im.putpixel((y, i), rgbValue) # Puts the evaluated RGB value on to the given pixel.
            z += 1
    if showDuration:
        print(f"{(time.time()-startTime)*1000} ms") # Shows duration if told to do so.
    im.save("convertedImage.png", format="png") # Saves the converted image.
    x.close()

def inputs(stringToBeAdded: str=None):
    fileToConvert = input(f"{stringToBeAdded}\n> ") # Input file to be converted and an additional option.
    showDuration = input("Would you like to see the duration taken? (\"True\" or \"False\")\n> ")

    if "False" != showDuration and "True" != showDuration: # Ensures the entered value is a boolean.
        raise Exception("Entered value is not a boolean.")
    
    valueList = [fileToConvert, showDuration]
    return valueList

if __name__ == "__main__":
    while True:
        optionalMode = input("Please input a mode. Either \"To RGB\" or \"To image\"\n> ") # Gets input for the mode.
        if optionalMode.lower() == "to image":
            values = inputs("Please enter the RGB data path and name.") # Gets input from the input function.
            convertToImage(values[0], values[1]) # Calls the image conversion function.
            continue

        values = inputs("Please enter the image path and name.") # Gets input from the input function.
        rgbValues = convertToRGB(values[0], eval(values[1])) # Runs the convertToRGB function.

        with open('rgbValues.txt', 'w') as file: # Opens and writes rgbValues to a file.
            file.write(str(rgbValues))
