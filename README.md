# ImageToRGB

# About
A simple project that allows for users to convert an image to RGB values, and vice versa.
Converting RGB data from a 4k image in to an image is **very** performance heavy.

# Functions included
`convertToRGB(file, showDuration: bool)`: Converts an image to RGB data. Which returns a dictionary of RGB values and metadata. <br>
`convertToImage(file Path: str, showDuration: bool)`: Converts RGB data in to an image. Which may be found as `convertedImage.png`. **This is very performance heavy.**
# Example
```python
with open("rgbData.txt", "w") as file:
    file.write(convertToRGB("cute cat.png", False))
    
convertToImage("rgbData.txt", True)
```

# Possible upcoming changes
1. More accurate timer.
